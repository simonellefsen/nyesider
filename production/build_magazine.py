#!/usr/bin/env python3
"""Build the print PDF for a Nye Sider issue from its markdown content.

Reads content/<slug>/magazine.json + issues/<issue>/issue.json + articles/*.md
and renders an A4 magazine PDF: cover, contents, articles (with images,
figures, blockquotes, lists, GFM footnotes), kolofon, back cover.

Usage:
  .venv/bin/python production/build_magazine.py <slug> <issue-slug>
  .venv/bin/python production/build_magazine.py gnisten 2026-07-nr1
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as canvas_mod
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    Image,
    KeepTogether,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from svglib.svglib import svg2rlg

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENT_ROOT = REPO_ROOT / "content"
FONT_DIR = Path("/System/Library/Fonts/Supplemental")

MONTHS_DA = {
    1: "januar", 2: "februar", 3: "marts", 4: "april", 5: "maj", 6: "juni",
    7: "juli", 8: "august", 9: "september", 10: "oktober", 11: "november", 12: "december",
}

PAGE_W, PAGE_H = A4
MARGIN = 1.5 * cm
CONTENT_W = PAGE_W - 2 * MARGIN


def register_fonts():
    pdfmetrics.registerFont(TTFont("Serif", FONT_DIR / "Georgia.ttf"))
    pdfmetrics.registerFont(TTFont("Serif-Bold", FONT_DIR / "Georgia Bold.ttf"))
    pdfmetrics.registerFont(TTFont("Serif-Italic", FONT_DIR / "Georgia Italic.ttf"))
    pdfmetrics.registerFont(TTFont("Serif-BoldItalic", FONT_DIR / "Georgia Bold Italic.ttf"))
    pdfmetrics.registerFontFamily(
        "Serif", normal="Serif", bold="Serif-Bold", italic="Serif-Italic", boldItalic="Serif-BoldItalic"
    )
    pdfmetrics.registerFont(TTFont("Sans", FONT_DIR / "Arial.ttf"))
    pdfmetrics.registerFont(TTFont("Sans-Bold", FONT_DIR / "Arial Bold.ttf"))
    pdfmetrics.registerFont(TTFont("Sans-Italic", FONT_DIR / "Arial Italic.ttf"))
    pdfmetrics.registerFontFamily("Sans", normal="Sans", bold="Sans-Bold", italic="Sans-Italic")


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_frontmatter(raw: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if not m:
        return {}, raw
    data = yaml.safe_load(m.group(1)) or {}
    return data, m.group(2)


class Ctx:
    def __init__(self, slug: str, issue_slug: str):
        self.slug = slug
        self.mag = load_json(CONTENT_ROOT / slug / "magazine.json")
        self.issue_dir = CONTENT_ROOT / slug / "issues" / issue_slug
        self.issue = load_json(self.issue_dir / "issue.json")
        colors_cfg = self.mag["theme"]["colors"]
        self.primary = HexColor(colors_cfg.get("primary") or "#0b1220")
        self.accent = HexColor(colors_cfg.get("accent") or "#2a6f97")
        self.highlight = HexColor(colors_cfg.get("highlight") or "#c9842f")
        self.ink = HexColor("#1a1a1a")
        self.ink_muted = HexColor("#5c5c5c")
        self.paper = HexColor("#f7f4ef")


def styles(ctx: Ctx) -> dict:
    return {
        "cover_kicker": ParagraphStyle(
            "cover_kicker", fontName="Sans-Bold", fontSize=12, textColor=colors.white,
            alignment=TA_CENTER, spaceAfter=6,
        ),
        "cover_title": ParagraphStyle(
            "cover_title", fontName="Serif-Bold", fontSize=52, leading=56, textColor=colors.white,
            alignment=TA_CENTER, spaceAfter=14,
        ),
        "cover_theme": ParagraphStyle(
            "cover_theme", fontName="Serif-Italic", fontSize=19, leading=24, textColor=colors.white,
            alignment=TA_CENTER, spaceAfter=10,
        ),
        "cover_meta": ParagraphStyle(
            "cover_meta", fontName="Sans", fontSize=11, textColor=colors.white,
            alignment=TA_CENTER,
        ),
        "toc_h1": ParagraphStyle(
            "toc_h1", fontName="Serif-Bold", fontSize=24, textColor=ctx.ink, spaceAfter=12,
        ),
        "toc_section": ParagraphStyle(
            "toc_section", fontName="Sans-Bold", fontSize=8.5, textColor=ctx.accent,
            spaceBefore=7, spaceAfter=1, leading=10,
        ),
        "toc_title": ParagraphStyle(
            "toc_title", fontName="Serif-Bold", fontSize=12.5, textColor=ctx.ink, leading=15,
        ),
        "toc_standfirst": ParagraphStyle(
            "toc_standfirst", fontName="Serif-Italic", fontSize=8.7, textColor=ctx.ink_muted,
            leading=11, spaceAfter=1,
        ),
        "toc_byline": ParagraphStyle(
            "toc_byline", fontName="Sans", fontSize=8, textColor=ctx.ink_muted,
        ),
        "eyebrow": ParagraphStyle(
            "eyebrow", fontName="Sans-Bold", fontSize=8.5, textColor=ctx.accent, spaceAfter=4,
        ),
        "article_title": ParagraphStyle(
            "article_title", fontName="Serif-Bold", fontSize=17.5, leading=20, textColor=ctx.ink,
            spaceAfter=5,
        ),
        "standfirst": ParagraphStyle(
            "standfirst", fontName="Serif-Italic", fontSize=10.8, leading=14.5, textColor=ctx.ink_muted,
            spaceAfter=5,
        ),
        "byline": ParagraphStyle(
            "byline", fontName="Sans-Bold", fontSize=8.7, textColor=ctx.ink, spaceAfter=9,
        ),
        "h2": ParagraphStyle(
            "h2", fontName="Sans-Bold", fontSize=12, textColor=ctx.primary,
            spaceBefore=9, spaceAfter=3, leading=14,
        ),
        "h3": ParagraphStyle(
            "h3", fontName="Serif-Bold", fontSize=10.6, textColor=ctx.ink,
            spaceBefore=7, spaceAfter=2, leading=13,
        ),
        "body": ParagraphStyle(
            "body", fontName="Serif", fontSize=9.0, leading=12.2, textColor=ctx.ink,
            spaceAfter=5, alignment=TA_JUSTIFY,
        ),
        "list_item": ParagraphStyle(
            "list_item", fontName="Serif", fontSize=9.0, leading=12.2, textColor=ctx.ink,
            spaceAfter=3, leftIndent=14, alignment=TA_JUSTIFY,
        ),
        "quote": ParagraphStyle(
            "quote", fontName="Serif-Italic", fontSize=11.5, leading=15, textColor=ctx.primary,
            leftIndent=16, spaceBefore=6, spaceAfter=6,
        ),
        "figure_caption": ParagraphStyle(
            "figure_caption", fontName="Sans", fontSize=8, textColor=ctx.ink_muted,
            alignment=TA_CENTER, spaceAfter=10,
        ),
        "footnotes_h": ParagraphStyle(
            "footnotes_h", fontName="Sans-Bold", fontSize=8, textColor=ctx.accent,
            spaceBefore=9, spaceAfter=3,
        ),
        "footnote": ParagraphStyle(
            "footnote", fontName="Sans", fontSize=7.2, leading=10, textColor=ctx.ink_muted,
            spaceAfter=2,
        ),
        "kolofon_h": ParagraphStyle(
            "kolofon_h", fontName="Serif-Bold", fontSize=22, textColor=colors.white, spaceAfter=16,
        ),
        "kolofon_line": ParagraphStyle(
            "kolofon_line", fontName="Sans", fontSize=10, textColor=colors.white, spaceAfter=5,
            leading=14,
        ),
        "kolofon_note": ParagraphStyle(
            "kolofon_note", fontName="Sans", fontSize=9, textColor=colors.white, spaceBefore=16,
            leading=13,
        ),
        "backcover": ParagraphStyle(
            "backcover", fontName="Serif-Italic", fontSize=18, leading=24, textColor=colors.white,
            alignment=TA_CENTER,
        ),
    }


# ---------------------------------------------------------------- markdown --

FOOTNOTE_DEF_RE = re.compile(r"^\[\^(\d+)\]:\s*(.*)$")
FOOTNOTE_REF_RE = re.compile(r"\[\^(\d+)\]")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
ITALIC_RE = re.compile(r"(?<!\*)\*(?!\*)([^*]+?)\*(?!\*)")
CODE_RE = re.compile(r"`([^`]+)`")


def inline_markup(text: str, accent_hex: str) -> str:
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = FOOTNOTE_REF_RE.sub(
        lambda m: f'<super><font color="{accent_hex}" size="6.5">{m.group(1)}</font></super>', text
    )
    text = LINK_RE.sub(
        lambda m: f'<link href="{m.group(2)}"><font color="{accent_hex}"><u>{m.group(1)}</u></font></link>',
        text,
    )
    text = BOLD_RE.sub(r"<b>\1</b>", text)
    text = ITALIC_RE.sub(r"<i>\1</i>", text)
    text = CODE_RE.sub(r'<font face="Courier" size="9">\1</font>', text)
    return text


def image_flowable(path: Path, max_width: float, max_height: float | None = None):
    if path.suffix.lower() == ".svg":
        drawing = svg2rlg(str(path))
        scale = max_width / drawing.width
        if max_height and drawing.height * scale > max_height:
            scale = max_height / drawing.height
        drawing.width *= scale
        drawing.height *= scale
        drawing.scale(scale, scale)
        return drawing
    reader = ImageReader(str(path))
    iw, ih = reader.getSize()
    w = max_width
    h = w * ih / iw
    if max_height and h > max_height:
        h = max_height
        w = h * iw / ih
    return Image(str(path), width=w, height=h)


def resolve_asset(issue_dir: Path, rel: str) -> Path:
    cleaned = rel.replace("../", "").replace("./", "")
    return issue_dir / cleaned


def render_markdown(
    body: str, sty: dict, ctx: Ctx, figures: list[str], hero_used: bool = False
) -> list:
    accent_hex = "#%02x%02x%02x" % (
        int(ctx.accent.red * 255), int(ctx.accent.green * 255), int(ctx.accent.blue * 255)
    )
    footnotes: dict[str, str] = {}
    lines = body.split("\n")
    kept = []
    for line in lines:
        m = FOOTNOTE_DEF_RE.match(line.strip())
        if m:
            footnotes[m.group(1)] = m.group(2)
        else:
            kept.append(line)

    flowables = []
    i = 0
    n = len(kept)
    fig_idx = 0
    while i < n:
        line = kept[i].strip()
        if not line:
            i += 1
            continue
        if line.startswith("### "):
            flowables.append(Paragraph(inline_markup(line[4:].strip(), accent_hex), sty["h3"]))
            i += 1
        elif line.startswith("## "):
            flowables.append(Paragraph(inline_markup(line[3:].strip(), accent_hex), sty["h2"]))
            i += 1
        elif re.match(r"^\[FIGUR\s*\d*\]$", line, re.I):
            if fig_idx < len(figures):
                img_path = resolve_asset(ctx.issue_dir, figures[fig_idx])
                if img_path.exists():
                    flowables.append(Spacer(1, 6))
                    flowables.append(image_flowable(img_path, CONTENT_W, 4.6 * cm))
                    flowables.append(Spacer(1, 6))
                fig_idx += 1
            i += 1
        elif line.startswith(">"):
            buf = []
            while i < n and kept[i].strip().startswith(">"):
                buf.append(kept[i].strip().lstrip(">").strip())
                i += 1
            flowables.append(Paragraph(inline_markup(" ".join(buf), accent_hex), sty["quote"]))
        elif re.match(r"^(-|\*|\d+\.)\s+", line):
            while i < n and re.match(r"^(-|\*|\d+\.)\s+", kept[i].strip()):
                item = re.sub(r"^(-|\*|\d+\.)\s+", "", kept[i].strip())
                flowables.append(Paragraph("• " + inline_markup(item, accent_hex), sty["list_item"]))
                i += 1
        else:
            buf = [line]
            i += 1
            while i < n and kept[i].strip() and not re.match(
                r"^(#{2,3}\s|>|(-|\*|\d+\.)\s|\[FIGUR)", kept[i].strip(), re.I
            ):
                buf.append(kept[i].strip())
                i += 1
            flowables.append(Paragraph(inline_markup(" ".join(buf), accent_hex), sty["body"]))

    if footnotes:
        flowables.append(Paragraph("Kilder &amp; links", sty["footnotes_h"]))
        for num in sorted(footnotes, key=int):
            txt = f"{num}. " + inline_markup(footnotes[num], accent_hex)
            flowables.append(Paragraph(txt, sty["footnote"]))

    return flowables


# --------------------------------------------------------------- doc build --


def cover_bg(color: HexColor):
    def draw(c: canvas_mod.Canvas, doc):
        c.setFillColor(color)
        c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    return draw


def kolofon_bg(color: HexColor):
    def draw(c: canvas_mod.Canvas, doc):
        c.setFillColor(color)
        c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    return draw


def article_footer(ctx: Ctx):
    def draw(c: canvas_mod.Canvas, doc):
        c.setFont("Sans", 8)
        c.setFillColor(ctx.ink_muted)
        c.drawString(MARGIN, 1.2 * cm, f"{ctx.mag['name']} · Nr. {ctx.issue['number']}")
        c.drawRightString(PAGE_W - MARGIN, 1.2 * cm, str(doc.page))
        c.setStrokeColor(ctx.accent)
        c.setLineWidth(1.4)
        c.line(MARGIN, 1.55 * cm, PAGE_W - MARGIN, 1.55 * cm)
    return draw


def build(slug: str, issue_slug: str) -> Path:
    register_fonts()
    ctx = Ctx(slug, issue_slug)
    sty = styles(ctx)
    issue_dir = ctx.issue_dir
    articles = sorted(ctx.issue["articles"], key=lambda a: a["order"])

    out_month = MONTHS_DA[int(ctx.issue["published"][5:7])]
    out_year = ctx.issue["published"][:4]
    out_name = f"{slug.upper()}_nr{ctx.issue['number']}_{out_month}{out_year}.pdf"
    out_path = issue_dir / out_name

    doc = BaseDocTemplate(
        str(out_path), pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN,
        title=ctx.issue["title"], author=f"{ctx.mag['name']} redaktion",
    )

    def full_frame():
        return Frame(0, 0, PAGE_W, PAGE_H, id="full", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)

    body_frame = Frame(
        MARGIN, MARGIN, CONTENT_W, PAGE_H - 2 * MARGIN, id="body",
        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0.6 * cm,
    )

    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[full_frame()], onPage=cover_bg(ctx.primary)),
        PageTemplate(id="article", frames=[body_frame], onPage=article_footer(ctx)),
        PageTemplate(id="kolofon", frames=[full_frame()], onPage=kolofon_bg(ctx.primary)),
    ])

    story = []

    # ---- Cover ----
    story.append(Spacer(1, 6.5 * cm))
    story.append(Paragraph(f"NR. {ctx.issue['number']} &nbsp;·&nbsp; {out_month.upper()} {out_year}", sty["cover_kicker"]))
    story.append(Paragraph(ctx.mag["name"], sty["cover_title"]))
    if ctx.issue.get("issueTheme"):
        story.append(Paragraph(f"“{ctx.issue['issueTheme']}”", sty["cover_theme"]))
    cover_img = ctx.issue.get("cover")
    if cover_img:
        p = resolve_asset(issue_dir, cover_img)
        if p.exists():
            story.append(Spacer(1, 0.8 * cm))
            img = image_flowable(p, 11 * cm, 11 * cm)
            story.append(KeepTogether([img]))
    story.append(Spacer(1, 1 * cm))
    story.append(Paragraph(ctx.mag["tagline"], sty["cover_meta"]))
    story.append(NextPageTemplate("article"))
    story.append(PageBreak())

    # ---- Contents ----
    story.append(Paragraph("Indhold", sty["toc_h1"]))
    for a in articles:
        story.append(Paragraph(a["section"].upper(), sty["toc_section"]))
        story.append(Paragraph(f"{a['order']:02d}&nbsp;&nbsp;{a['title']}", sty["toc_title"]))
        if a.get("standfirst"):
            story.append(Paragraph(a["standfirst"], sty["toc_standfirst"]))
        story.append(Paragraph(f"Af {a['byline']}", sty["toc_byline"]))
    story.append(PageBreak())

    # ---- Articles ----
    loaded = []
    for a in articles:
        md_path = issue_dir / a["file"]
        raw = md_path.read_text(encoding="utf-8")
        data, body = parse_frontmatter(raw)
        loaded.append((a, data, body))

    for idx, (a, data, body) in enumerate(loaded):
        title = data.get("title", a["title"])
        section = data.get("section", a["section"])
        byline = data.get("byline", a["byline"])
        standfirst = data.get("standfirst", a.get("standfirst"))
        figures = data.get("figures", [])

        if idx > 0:
            if data.get("flow", False):
                story.append(
                    HRFlowable(width="100%", thickness=0.6, color=ctx.accent, spaceBefore=4, spaceAfter=12)
                )
            else:
                story.append(PageBreak())
        story.append(Paragraph(section.upper(), sty["eyebrow"]))
        story.append(Paragraph(title, sty["article_title"]))
        if standfirst:
            story.append(Paragraph(standfirst, sty["standfirst"]))
        story.append(Paragraph(f"Af <b>{byline}</b>", sty["byline"]))

        hero = data.get("image")
        if hero:
            p = resolve_asset(issue_dir, hero)
            if p.exists():
                story.append(image_flowable(p, CONTENT_W, 4.6 * cm))
                story.append(Spacer(1, 5))

        story.extend(render_markdown(body, sty, ctx, figures))

        if idx == len(loaded) - 1:
            story.append(NextPageTemplate("kolofon"))
            story.append(PageBreak())

    # ---- Kolofon ----
    story.append(Paragraph("Kolofon", sty["kolofon_h"]))
    for a in articles:
        story.append(Paragraph(f"{a['order']:02d} — {a['title']} — <i>Af {a['byline']}</i>", sty["kolofon_line"]))
    credits = ctx.issue.get("imageCredits")
    note = (
        f"{ctx.mag['name']} er skrevet af en redaktion af AI-sprogmodeller via OpenRouter, "
        f"redigeret af chefredaktionen (Claude), og udgivet af forlaget Nye Sider."
    )
    if credits:
        note += " " + credits
    story.append(Paragraph(note, sty["kolofon_note"]))
    story.append(PageBreak())

    # ---- Back cover ----
    promise = ctx.issue.get(
        "backCoverPromise",
        f"{ctx.mag['name']} nr. {ctx.issue['number'] + 1} udkommer, når den næste gnist har taget fat.",
    )
    story.append(Spacer(1, 12 * cm))
    story.append(Paragraph(f"“{promise}”", sty["backcover"]))

    doc.build(story)
    return out_path


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    out = build(sys.argv[1], sys.argv[2])
    print(f"Built {out} ({out.stat().st_size / 1024:.0f} KB)")
