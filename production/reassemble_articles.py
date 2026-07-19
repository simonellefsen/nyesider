#!/usr/bin/env python3
"""Reassemble extracted PDF pages into per-article markdown files.

Reads pages.json from _extract/, joins lines into clean Danish prose,
splits by known article boundaries, writes articles/*.md and updates issue.json.
"""
from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

# ---------------------------------------------------------------------------
# Text cleanup
# ---------------------------------------------------------------------------

HEADER_RE = re.compile(
    r"^(SPÆNDING|PULSEN|SPAENDING)\s*·\s*Nr\.?\s*\d+",
    re.I,
)
FOOTER_PAGE_RE = re.compile(
    r"^(Leder|Tema|Køretest|Teknologi|Politik|Rygtebørsen|Essay|Kort\s*&\s*Watt|"
    r"Feature|Analyse|Ergoterapi|Vandrehistorier|Sjov\s*&\s*Spil|"
    r"Indhold|Kolofon)\s*·\s*\d+\s*$",
    re.I,
)
PAGE_NUM_ONLY = re.compile(r"^\d{1,2}$")
# spaced-out cover titles like "P U L S E N"
SPACED_OUT = re.compile(r"^(?:[A-ZÆØÅ]\s+){2,}[A-ZÆØÅ]\s*$")


def dehyphenate_join(parts: list[str]) -> str:
    """Join line fragments; repair hyphenation at line ends."""
    if not parts:
        return ""
    out: list[str] = []
    buf = parts[0].rstrip()
    for nxt in parts[1:]:
        nxt = nxt.strip()
        if not nxt:
            continue
        # hyphenation: word- \n continuation
        if buf.endswith("-") and nxt and nxt[0].islower():
            buf = buf[:-1] + nxt
            continue
        # soft hyphen / discretionary
        if buf.endswith("\u00ad"):
            buf = buf[:-1] + nxt
            continue
        # single-word orphan lines that belong to previous (PDF wrapping of short words)
        # Always space-join otherwise
        # If previous ends mid-sentence without punctuation and next is lowercase continuation...
        if buf and not buf[-1].isspace():
            # special case: very short tokens that were split letter-by-letter? skip
            buf = buf + " " + nxt
        else:
            buf = buf + nxt
    out.append(buf)
    return " ".join(out)


def normalize_spaces(s: str) -> str:
    s = s.replace("\u00a0", " ").replace("\u202f", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r" +([,.;:!?])", r"\1", s)
    s = re.sub(r"\( ", "(", s)
    s = re.sub(r" \)", ")", s)
    # fix spaced letters like "I  maj  2026" already space-joined as separate lines
    return s.strip()


def is_furniture(text: str, role: str) -> bool:
    t = text.strip()
    if not t:
        return True
    if PAGE_NUM_ONLY.match(t):
        return True
    if HEADER_RE.match(t):
        return True
    if FOOTER_PAGE_RE.match(t):
        return True
    if SPACED_OUT.match(t):
        return True
    # "P U L S E N" style with multiple spaces already stripped differently
    if re.fullmatch(r"(?:[A-ZÆØÅ] ){3,}[A-ZÆØÅ]", t):
        return True
    return False


def join_paragraph_lines(lines: list[str]) -> str:
    """Join consecutive body lines into a paragraph with dehyphenation."""
    if not lines:
        return ""
    cleaned = [ln.strip() for ln in lines if ln.strip()]
    if not cleaned:
        return ""
    # Rebuild with hyphenation repair
    result = cleaned[0]
    for nxt in cleaned[1:]:
        if result.endswith("-") and nxt and nxt[0].islower():
            result = result[:-1] + nxt
        elif result.endswith("\u00ad"):
            result = result[:-1] + nxt
        else:
            # If the previous line is a single short token (PDF word wrap of narrow columns),
            # still space-join — dehyphenate_join already handled hyphens.
            result = result + " " + nxt
    return normalize_spaces(result)


# ---------------------------------------------------------------------------
# Article manifests
# ---------------------------------------------------------------------------

@dataclass
class ArticleSpec:
    slug: str
    title: str  # primary title for matching start
    title_alt: list[str] = field(default_factory=list)
    section: str = ""
    byline: str = ""
    standfirst: str = ""  # if known; else taken from extraction
    order: int = 0
    image: str | None = None
    # start matching: page number and headline substring
    start_page: int = 1
    # roles treated as body for this article type
    kind: str = "article"  # article | leader | kolofon | rumours | quiz | shorts


SPAENDING_ARTICLES: list[ArticleSpec] = [
    ArticleSpec(
        slug="leder-strom-til-folket",
        title="Strøm til folket",
        section="Leder",
        byline="Claude Fable 5",
        order=1,
        start_page=2,
        kind="leader",
    ),
    ArticleSpec(
        slug="folkebilen-er-tilbage",
        title="Folkebilen er tilbage – denne gang med stik",
        title_alt=["Folkebilen er tilbage – denne gang", "Folkebilen er tilbage"],
        section="Tema: Gennembruddet",
        byline="GPT-5.6 Terra (OpenAI)",
        order=2,
        start_page=3,
        image="../images/spaending_folkebil.png",
    ),
    ArticleSpec(
        slug="koere-test-bmw-ix3",
        title="BMW iX3 er landet – og den griner ad rækkeviddeangst",
        title_alt=["BMW iX3 er landet – og den griner ad", "BMW iX3 er landet"],
        section="Køretest",
        byline="Grok 4.5 (xAI)",
        order=3,
        start_page=5,
        image=None,
    ),
    ArticleSpec(
        slug="faststofbatteriet",
        title="Faststofbatteriet rykker ud på asfalten",
        section="Teknologi",
        byline="Gemini 3.5 Flash (Google)",
        order=4,
        start_page=6,
        image="../images/spaending_faststof.png",
    ),
    ArticleSpec(
        slug="foereloes-i-zagreb",
        title="Fremtiden kører allerede rundt i Zagreb – men reglerne sidder fast i garagen",
        title_alt=["Fremtiden kører allerede rundt i Zagreb"],
        section="Teknologi",
        byline="Claude Sonnet 5 (Anthropic)",
        order=5,
        start_page=8,
        image="../images/spaending_robotaxi.png",
    ),
    ArticleSpec(
        slug="afgiftspokeren",
        title="Den politiske djævlepagt: Når elbilens triumf bliver vejenes ruin",
        title_alt=["Den politiske djævlepagt"],
        section="Politik & afgifter",
        byline="GLM-5.2 (Z.ai)",
        order=6,
        start_page=10,
    ),
    ArticleSpec(
        slug="rygteboersen",
        title="Ugler i mosen og megawatt i asfalten",
        section="Rygtebørsen",
        byline="Qwen3.7 Max (Alibaba)",
        order=7,
        start_page=11,
        kind="rumours",
    ),
    ArticleSpec(
        slug="essay-sommerflugt",
        title="Elbilen, børnene og den store sommerflugt",
        title_alt=["Elbilen, børnene og den store"],
        section="Essay",
        byline="Mistral Medium 3.5 (Mistral AI)",
        order=8,
        start_page=12,
    ),
    ArticleSpec(
        slug="kort-og-watt",
        title="Kort & Watt",
        section="Kort & Watt",
        byline="MiniMax M3 (MiniMax)",
        order=9,
        start_page=13,
        kind="shorts",
    ),
]

PULSEN_ARTICLES: list[ArticleSpec] = [
    ArticleSpec(
        slug="leder-lyt-engang",
        title="Lyt engang",
        title_alt=["Leder · Lyt engang"],
        section="Leder",
        byline="Claude Fable 5",
        order=1,
        start_page=2,
        kind="leader",
    ),
    ArticleSpec(
        slug="corti-maskinen-der-laerte-at-lytte",
        title="Maskinen der lærte at lytte på dansk",
        title_alt=["Maskinen der lærte at lytte"],
        section="Feature · Dansk sundheds-AI",
        byline="Claude Opus 4.8 (Anthropic)",
        order=2,
        start_page=3,
    ),
    ArticleSpec(
        slug="bupa-digitale-tvilling",
        title="Din digitale tvilling har det fint — endnu",
        title_alt=["Din digitale tvilling har det fint"],
        section="Analyse · Forebyggelse & dataetik",
        byline="GPT-5.5 (OpenAI)",
        order=3,
        start_page=5,
    ),
    ArticleSpec(
        slug="dedalus-giganten",
        title="Giganten du aldrig har hørt om",
        section="Feature",
        byline="Mistral Large 2512 (Mistral AI)",
        order=4,
        start_page=6,
    ),
    ArticleSpec(
        slug="journalen-skriver-sig-selv",
        title="Journalen skriver sig selv",
        section="Feature · Ambient AI",
        byline="Gemini 3.5 Flash (Google)",
        order=5,
        start_page=7,
    ),
    ArticleSpec(
        slug="nyt-fra-ergoterapien",
        title="Hænder, hjem og høreapparater til hjernen",
        title_alt=["Hænder, hjem og høreapparater til"],
        section="Nyt fra ergoterapien",
        byline="Qwen 3.7 Max (Alibaba)",
        order=6,
        start_page=8,
    ),
    ArticleSpec(
        slug="vandrehistorier",
        title="Vandrehistorier fra vagtstuen",
        section="Vandrehistorier fra vagtstuen",
        byline="Llama 4 Maverick (Meta)",
        order=7,
        start_page=9,
        kind="anecdotes",
    ),
    ArticleSpec(
        slug="rygteboersen",
        title="Rygtebørsen",
        section="Rygtebørsen",
        byline="Grok 4.3 (xAI)",
        order=8,
        start_page=10,
        kind="rumours",
    ),
    ArticleSpec(
        slug="sjov-og-spil",
        title="Skarpe hjerner, skarpere blyanter",
        section="Sjov & Spil",
        byline="DeepSeek V3.2 (DeepSeek)",
        order=9,
        start_page=11,
        kind="quiz",
    ),
]


def load_pages(extract_dir: Path) -> list[dict]:
    return json.loads((extract_dir / "pages.json").read_text(encoding="utf-8"))


def all_lines(pages: list[dict], from_page: int, to_page: int | None = None) -> list[dict]:
    out = []
    for p in pages:
        if p["page"] < from_page:
            continue
        if to_page is not None and p["page"] >= to_page:
            break
        for b in p["blocks"]:
            item = dict(b)
            item["page"] = p["page"]
            out.append(item)
    return out


def match_title(text: str, spec: ArticleSpec) -> bool:
    t = normalize_spaces(text)
    candidates = [spec.title, *spec.title_alt]
    for c in candidates:
        if t.startswith(c[: min(20, len(c))]) or c[:30] in t or t in c:
            return True
        # partial: first words
        if t.rstrip(" –—-") and any(t.startswith(c.split("–")[0].strip()[:15]) for c in candidates):
            # more careful
            pass
    for c in candidates:
        # normalize dashes
        a = re.sub(r"[–—-]", "-", t.lower())
        b = re.sub(r"[–—-]", "-", c.lower())
        if a.startswith(b[:25]) or b.startswith(a[:25]) or a in b or b in a:
            return True
    return False


def find_article_start(pages: list[dict], spec: ArticleSpec) -> tuple[int, int] | None:
    """Return (page, block_index_in_page) for article start headline."""
    for p in pages:
        if p["page"] < spec.start_page:
            continue
        if p["page"] > spec.start_page + 1:
            break
        for i, b in enumerate(p["blocks"]):
            if b["role"] in ("headline", "subhead", "section", "emphasis") or (
                spec.kind == "leader" and "Leder" in b["text"]
            ):
                if match_title(b["text"], spec):
                    return p["page"], i
            # leader special: "Lyt engang" / "Strøm til folket"
            if match_title(b["text"], spec):
                return p["page"], i
    # fallback: first non-furniture on start_page
    for p in pages:
        if p["page"] == spec.start_page:
            return p["page"], 0
    return None


def collect_raw_lines(pages: list[dict], start: tuple[int, int], end: tuple[int, int] | None) -> list[dict]:
    lines = []
    started = False
    for p in pages:
        for i, b in enumerate(p["blocks"]):
            pos = (p["page"], i)
            if not started:
                if pos == start:
                    started = True
                else:
                    continue
            if end is not None and pos == end:
                return lines
            item = dict(b)
            item["page"] = p["page"]
            lines.append(item)
    return lines


def build_body_markdown(lines: list[dict], spec: ArticleSpec) -> tuple[str, str, str]:
    """Return (title, standfirst, body_md)."""
    # Merge consecutive headline lines into title
    title_parts: list[str] = []
    standfirst_parts: list[str] = []
    byline = spec.byline
    body_md: list[str] = []
    para_buf: list[str] = []
    mode = "title"  # title -> standfirst/byline -> body
    seen_title = False
    skip_next_section_labels = True

    def flush_para():
        nonlocal para_buf
        if para_buf:
            text = join_paragraph_lines(para_buf)
            if text and not is_furniture(text, "body"):
                body_md.append(text)
            para_buf = []

    def flush_heading(level: int, text: str):
        flush_para()
        t = normalize_spaces(text)
        if t:
            body_md.append(f"{'#' * level} {t}")

    i = 0
    while i < len(lines):
        b = lines[i]
        text = b["text"].strip()
        role = b["role"]
        if is_furniture(text, role):
            i += 1
            continue

        # Skip section label on first lines (e.g. TEMA: GENNEMBRUDDET, KØRETEST)
        if not seen_title and role in ("body", "emphasis", "label", "section") and (
            text.isupper() or text.startswith("TEMA") or "FEATURE" in text.replace(" ", "")
            or text.startswith("ANALYSE") or text.startswith("RYGTE")
            or "LEDER" in text.upper()
            or text in ("KØRETEST", "ESSAY", "KOLOFON")
            or re.match(r"^[A-ZÆØÅ ·]+$", text) and len(text) < 60
        ):
            # spaced section labels like "F E A T U R E · ..."
            if re.search(r"\s{1}[A-ZÆØÅ]\s{1}", text) or text.isupper() or "·" in text:
                i += 1
                continue

        if not seen_title and role in ("headline", "subhead") or (
            not seen_title and match_title(text, spec)
        ):
            # gather consecutive headline lines
            title_parts.append(text)
            j = i + 1
            while j < len(lines) and lines[j]["role"] == "headline":
                title_parts.append(lines[j]["text"].strip())
                j += 1
            seen_title = True
            mode = "after_title"
            i = j
            continue

        if mode == "after_title":
            # standfirst often comes as standfirst role or slightly larger body
            if role == "standfirst" or (role == "body" and b.get("size", 0) >= 10.5 and not text.lower().startswith("af ")):
                # might still be standfirst
                if text.lower().startswith("af ") and ("·" in text or "redigeret" in text.lower()):
                    # byline
                    byline = re.sub(r"^[Aa]f\s+", "", text)
                    byline = re.sub(r"\s*·\s*[Rr]edigeret.*$", "", byline).strip()
                    i += 1
                    continue
                standfirst_parts.append(text)
                i += 1
                # absorb more standfirst lines
                while i < len(lines) and lines[i]["role"] == "standfirst":
                    standfirst_parts.append(lines[i]["text"].strip())
                    i += 1
                mode = "body"
                continue
            if role in ("caption", "body") and text.lower().startswith("af "):
                byline = re.sub(r"^[Aa]f\s+", "", text)
                byline = re.sub(r"\s*·\s*[Rr]edigeret.*$", "", byline).strip()
                byline = re.sub(r"\s*·\s*[Rr]edigeret af chefredaktionen\s*$", "", byline, flags=re.I).strip()
                i += 1
                mode = "body"
                continue
            if role == "caption" and "redigeret" in text.lower():
                byline = re.sub(r"^[Aa]f\s+", "", text)
                byline = re.sub(r"\s*·\s*[Rr]edigeret.*$", "", byline).strip()
                i += 1
                mode = "body"
                continue
            mode = "body"
            # fall through

        # body mode
        if role in ("headline", "subhead", "section") and seen_title:
            # subheading inside article
            # merge consecutive
            hparts = [text]
            j = i + 1
            while j < len(lines) and lines[j]["role"] in ("headline", "subhead", "section"):
                # don't swallow next article title — those won't appear since we cut range
                hparts.append(lines[j]["text"].strip())
                j += 1
            h = join_paragraph_lines(hparts)
            # skip if it looks like next article (shouldn't happen)
            if h and not is_furniture(h, role):
                level = 2 if role in ("headline", "subhead") else 3
                # section labels that are short uppercase → h3
                if role == "section" or (h.isupper() and len(h) < 40):
                    level = 3
                flush_heading(level, h)
            i = j
            continue

        if role in ("body", "standfirst", "emphasis", "caption", "label"):
            # skip bylines that appear late
            if text.lower().startswith("af ") and "redigeret" in text.lower():
                i += 1
                continue
            # skip captions that are image credits only? keep for now unless furniture
            if role == "caption" and is_furniture(text, role):
                i += 1
                continue
            # emphasis that is a subhead-like short line
            if role == "emphasis" and len(text) < 60 and not text.endswith("."):
                flush_para()
                # rumours style items
                if spec.kind in ("rumours", "shorts", "anecdotes", "quiz"):
                    body_md.append(f"### {normalize_spaces(text)}")
                else:
                    body_md.append(f"**{normalize_spaces(text)}**")
                i += 1
                continue
            para_buf.append(text)
            # paragraph break heuristic: if line ends with . ! ? and next has capital, or blank gap
            # PDF doesn't give blank lines easily — break when next role changes or size drops
            if i + 1 < len(lines):
                nxt = lines[i + 1]
                # end paragraph if next is heading-like
                if nxt["role"] in ("headline", "subhead", "section"):
                    flush_para()
                # or if current ends sentence and next starts new (hard)
                elif text.rstrip().endswith((".", "!", "?", "»", '"')) and nxt["role"] in ("body", "standfirst"):
                    # still same paragraph often in magazines — keep joining unless next is clearly new
                    # Use: if next starts with uppercase and previous is long enough → new para
                    if len(join_paragraph_lines(para_buf)) > 280:
                        flush_para()
            i += 1
            continue

        i += 1

    flush_para()

    title = join_paragraph_lines(title_parts) if title_parts else spec.title
    title = normalize_spaces(title)
    # Prefer catalog title if extracted is fragment
    if len(title) < len(spec.title) // 2:
        title = spec.title
    # If extracted is prefix of catalog, use catalog
    if spec.title.startswith(title.rstrip(" –-")) or title in spec.title:
        title = spec.title

    standfirst = join_paragraph_lines(standfirst_parts) if standfirst_parts else ""
    standfirst = normalize_spaces(standfirst)

    # post-process body: convert some patterns for special kinds
    body = "\n\n".join(body_md)
    body = postprocess_body(body, spec)
    return title, standfirst, body, byline


def postprocess_body(body: str, spec: ArticleSpec) -> str:
    # Clean double spaces
    body = re.sub(r"  +", " ", body)
    # Leader signature
    body = re.sub(r"—\s*Claude Fable 5,\s*chefredaktør", "\n\n— Claude Fable 5, chefredaktør", body)
    if spec.kind == "rumours":
        # already mostly headings
        pass
    if spec.kind == "quiz":
        # Wrap answer-like lines: "Svar:" sections into details later editorially
        body = re.sub(
            r"(?m)^(Svar[: ].+)$",
            r"<details>\n<summary>Se svar</summary>\n\n\1\n\n</details>",
            body,
        )
    return body.strip() + "\n"


def yaml_escape(s: str) -> str:
    if s is None:
        return ""
    if any(c in s for c in ':\\"\n') or s.startswith("'") or s.startswith('"'):
        return json.dumps(s, ensure_ascii=False)
    return s


def write_article(out_dir: Path, spec: ArticleSpec, title: str, standfirst: str, byline: str, body: str) -> str:
    out_dir.mkdir(parents=True, exist_ok=True)
    fname = f"{spec.order:02d}-{spec.slug}.md"
    path = out_dir / fname
    fm = [
        "---",
        f"title: {yaml_escape(title)}",
    ]
    if standfirst:
        fm.append(f"standfirst: {yaml_escape(standfirst)}")
    fm.append(f"byline: {yaml_escape(byline)}")
    fm.append(f"section: {yaml_escape(spec.section)}")
    fm.append(f"order: {spec.order}")
    if spec.image:
        fm.append(f"image: {yaml_escape(spec.image)}")
    fm.append("---")
    content = "\n".join(fm) + "\n\n" + body
    if not content.endswith("\n"):
        content += "\n"
    path.write_text(content, encoding="utf-8")
    return fname


def reassemble_issue(issue_dir: Path, articles: list[ArticleSpec], cover_image: str | None = None) -> None:
    extract = issue_dir / "_extract"
    pages = load_pages(extract)
    starts: list[tuple[ArticleSpec, tuple[int, int]]] = []
    for spec in articles:
        st = find_article_start(pages, spec)
        if st is None:
            print(f"  WARN: no start for {spec.slug}")
            continue
        starts.append((spec, st))
        print(f"  {spec.slug}: page {st[0]} block {st[1]}")

    arts_out = []
    articles_dir = issue_dir / "articles"
    for idx, (spec, start) in enumerate(starts):
        end = starts[idx + 1][1] if idx + 1 < len(starts) else None
        # For leader on page 2 of pulsen/spaending, don't swallow whole page of TOC
        raw = collect_raw_lines(pages, start, end)
        # For spaending leader: stop before Indhold / before col 1 KOLOFON content mixed
        if spec.kind == "leader":
            filtered = []
            for b in raw:
                t = b["text"].strip()
                if t == "Indhold" or t.startswith("03  ") or t.startswith("3\n"):
                    break
                if re.match(r"^\d{2}\s{2}\S", t):  # TOC lines
                    break
                if t == "KOLOFON" or (b.get("col") == 1 and "Kolofon" in (b.get("text") or "")):
                    # spaending: kolofon is col 1 — stop leader at col change after title
                    if b.get("col") == 1:
                        break
                filtered.append(b)
            raw = filtered

        title, standfirst, body, byline = build_body_markdown(raw, spec)
        # Drop the article's own H2 title if it got duplicated in body
        body_lines = body.split("\n")
        if body_lines and body_lines[0].startswith("# ") and title in body_lines[0]:
            body = "\n".join(body_lines[1:]).lstrip() + ("\n" if body.endswith("\n") else "")
        # remove first ## title duplicate
        body = re.sub(rf"^##\s+{re.escape(title)}\s*\n+", "", body)

        fname = write_article(articles_dir, spec, title, standfirst, byline or spec.byline, body)
        word_count = len(re.findall(r"\w+", body, re.UNICODE))
        arts_out.append(
            {
                "slug": spec.slug,
                "file": f"articles/{fname}",
                "order": spec.order,
                "title": title,
                "section": spec.section,
                "byline": byline or spec.byline,
                "standfirst": standfirst or None,
                "image": spec.image,
                "wordCount": word_count,
            }
        )
        print(f"    → {fname} ({word_count} words)")

    # update issue.json
    issue_path = issue_dir / "issue.json"
    issue = json.loads(issue_path.read_text(encoding="utf-8"))
    issue["articles"] = [
        {
            "slug": a["slug"],
            "file": a["file"],
            "order": a["order"],
            "title": a["title"],
            "section": a["section"],
            "byline": a["byline"],
            **({"standfirst": a["standfirst"]} if a.get("standfirst") else {}),
            **({"image": a["image"]} if a.get("image") else {}),
        }
        for a in arts_out
    ]
    if cover_image and "cover" not in issue:
        issue["cover"] = cover_image
    issue.pop("notes", None)
    issue_path.write_text(json.dumps(issue, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"  updated {issue_path}")


def copy_pulsen_images(issue_dir: Path) -> None:
    src = issue_dir / "_extract" / "images"
    dst = issue_dir / "images"
    dst.mkdir(exist_ok=True)
    # cover is the portrait one
    for p in sorted(src.glob("*.png")):
        target = dst / p.name
        if not target.exists():
            target.write_bytes(p.read_bytes())
    # also create friendly names
    cover = list(src.glob("*896x1200*"))
    if cover:
        (dst / "pulsen_cover.png").write_bytes(cover[0].read_bytes())
    landscapes = sorted(src.glob("*1376x768*"))
    for i, img in enumerate(landscapes, 1):
        (dst / f"pulsen_art_{i}.png").write_bytes(img.read_bytes())


def main():
    root = Path(__file__).resolve().parents[1]
    spa = root / "content/spaending/issues/2026-07-nr1"
    pul = root / "content/pulsen/issues/2026-07-nr1"

    print("=== SPÆNDING nr. 1 ===")
    reassemble_issue(spa, SPAENDING_ARTICLES, cover_image="images/spaending_cover.png")

    print("=== PULSEN nr. 1 ===")
    copy_pulsen_images(pul)
    # assign images to articles where sensible
    for a in PULSEN_ARTICLES:
        if a.slug == "corti-maskinen-der-laerte-at-lytte":
            a.image = "../images/pulsen_art_1.png"
        elif a.slug == "bupa-digitale-tvilling":
            a.image = "../images/pulsen_art_2.png"
        elif a.slug == "journalen-skriver-sig-selv":
            a.image = "../images/pulsen_art_3.png"
    reassemble_issue(pul, PULSEN_ARTICLES, cover_image="images/pulsen_cover.png")

    # PULSEN brand colors from samples
    mag = json.loads((root / "content/pulsen/magazine.json").read_text(encoding="utf-8"))
    mag["theme"]["colors"] = {
        "primary": "#064253",
        "accent": "#1A8A8C",
        "highlight": "#C4A35A",
    }
    (root / "content/pulsen/magazine.json").write_text(
        json.dumps(mag, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print("Updated pulsen theme colors")


if __name__ == "__main__":
    main()
