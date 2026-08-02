"""Validate a Nye Sider issue for the defects that silently degrade today.

Neither `web/src/lib/server/content.ts` (the site's markdown pipeline) nor
`build_magazine.py` (the PDF builder) checks any of the following — a typo
just renders as a 404 image, a vanished chart, or a dropped figure marker,
with no error anywhere. This script is the check that has never existed.

Usage:

    python production/check_issue.py <slug> <issue-slug>
    python production/check_issue.py --all
    python production/check_issue.py --all --errors-only

Exit code is non-zero iff any ERROR was found (across all checked issues).
Warnings never affect the exit code — see the module docstring in
redaktion/README.md for why the errors/warnings split is deliberate: a
blocking check the editor can't satisfy at 23:00 gets bypassed, and then
nothing is enforced at all.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = REPO_ROOT / "content"

FIGURE_MARKER_RE = re.compile(r"^\[FIGUR\s*\d*\]$", re.IGNORECASE | re.MULTILINE)
CHART_MARKER_RE = re.compile(r"\[CHART\s+([a-z0-9_-]+)\]", re.IGNORECASE)
FOOTNOTE_DEF_RE = re.compile(r"^\[\^([^\]]+)\]:", re.MULTILINE)
FOOTNOTE_REF_RE = re.compile(r"\[\^([^\]]+)\](?!:)")
PLAIN_PERCENT_RE = re.compile(r"(?<! )\d %")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)
HEDGES = [
    "ofte", "omkring", "typisk", "ca.", "cirka", "de fleste", "en del",
    "markant", "svinger", "mange danskere", "angiveligt", "i omegnen af",
    "voksende", "tusindvis", "hundredvis", "i stigende grad", "betydelig andel",
]


class Finding:
    def __init__(self, level: str, issue: str, msg: str):
        self.level = level  # "error" | "warning"
        self.issue = issue
        self.msg = msg

    def __str__(self) -> str:
        tag = "ERROR" if self.level == "error" else "warn "
        return f"[{tag}] {self.issue}: {self.msg}"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    raw, body = m.group(1), m.group(2)
    data: dict = {}
    # Minimal YAML-subset parser matching what these files actually use:
    # scalars, quoted strings, and `key: [a, b]` / `key:\n  - a\n  - b` lists.
    lines = raw.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.strip().startswith("#"):
            i += 1
            continue
        km = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if not km:
            i += 1
            continue
        key, val = km.group(1), km.group(2).strip()
        if val == "" and i + 1 < len(lines) and lines[i + 1].lstrip().startswith("- "):
            items = []
            i += 1
            while i < len(lines) and lines[i].lstrip().startswith("- "):
                items.append(lines[i].lstrip()[2:].strip().strip('"'))
                i += 1
            data[key] = items
            continue
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            data[key] = [v.strip().strip('"').strip("'") for v in inner.split(",") if v.strip()] if inner else []
        elif val.lower() == "true":
            data[key] = True
        elif val.lower() == "false":
            data[key] = False
        elif re.match(r"^-?\d+$", val):
            data[key] = int(val)
        else:
            data[key] = val.strip('"').strip("'")
        i += 1
    return data, body


def check_issue(magazine_dir: Path, issue_dir: Path) -> list[Finding]:
    slug = magazine_dir.name
    issue_slug = issue_dir.name
    tag = f"{slug}/{issue_slug}"
    findings: list[Finding] = []

    issue_json_path = issue_dir / "issue.json"
    if not issue_json_path.exists():
        return [Finding("error", tag, "issue.json missing")]
    issue = load_json(issue_json_path)

    magazine_json_path = magazine_dir / "magazine.json"
    ledger_path = REPO_ROOT / "redaktion" / slug / "numre" / issue_slug / "bestilling.json"
    ledger = load_json(ledger_path) if ledger_path.exists() else None
    ledger_by_slug = {o["slug"]: o for o in ledger["opgaver"]} if ledger else {}

    roster_path = REPO_ROOT / "redaktion" / "modeller.json"
    roster_bylines = None
    if roster_path.exists():
        roster = load_json(roster_path)
        roster_bylines = {m["byline"] for m in roster.get("modeller", [])}

    # --- issue-level checks ---
    if issue.get("status") == "published" and issue.get("productionCostUSD") is None:
        findings.append(Finding("warning", tag, "status=published but productionCostUSD is null"))

    declared_images = set(issue.get("images", []))
    seen_images: set[str] = set()

    def check_image(rel: str | None, where: str):
        if not rel:
            return
        seen_images.add(rel)
        p = (issue_dir / rel).resolve()
        if not p.exists():
            findings.append(Finding("error", tag, f"{where}: image file missing on disk: {rel}"))

    check_image(issue.get("cover"), "issue.cover")
    for img in issue.get("images", []):
        check_image(img, "issue.images[]")
    if issue.get("cover") and not (issue.get("coverCredit") and issue.get("coverSource")):
        findings.append(Finding("warning", tag, "cover has no coverCredit/coverSource"))

    # --- charts ---
    charts_dir = issue_dir / "charts"
    chart_ids: set[str] = set()
    if charts_dir.is_dir():
        for cf in charts_dir.glob("*.json"):
            try:
                chart = load_json(cf)
            except json.JSONDecodeError as e:
                findings.append(Finding("error", tag, f"charts/{cf.name}: invalid JSON ({e})"))
                continue
            chart_ids.add(chart.get("id", cf.stem))
            years_len = len(chart.get("years", []))
            for s in chart.get("series", []):
                if len(s.get("values", [])) != years_len:
                    findings.append(
                        Finding(
                            "error", tag,
                            f"charts/{cf.name}: series '{s.get('name')}' has "
                            f"{len(s.get('values', []))} values, years has {years_len}",
                        )
                    )

    # --- per-article checks ---
    articles = sorted(issue.get("articles", []), key=lambda a: a["order"])
    for art in articles:
        aslug = art["slug"]
        atag = f"{tag}/{aslug}"
        rel_path = art.get("file")
        if not rel_path:
            findings.append(Finding("error", tag, f"{aslug}: no 'file' in issue.json"))
            continue
        md_path = issue_dir / rel_path
        if not md_path.exists():
            findings.append(Finding("error", tag, f"{aslug}: file missing on disk: {rel_path}"))
            continue

        # filename prefix vs order
        fname = md_path.name
        m = re.match(r"^(\d+)-", fname)
        if m and int(m.group(1)) != art["order"]:
            findings.append(
                Finding("error", tag, f"{aslug}: filename prefix {m.group(1)} != order {art['order']}")
            )

        text = md_path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)

        # frontmatter <-> issue.json divergence
        for field in ("title", "byline", "section", "order"):
            if field in meta and field in art and meta[field] != art[field]:
                findings.append(
                    Finding(
                        "error", tag,
                        f"{aslug}: frontmatter {field}={meta[field]!r} != issue.json {field}={art[field]!r}",
                    )
                )

        if not meta.get("standfirst") and not art.get("standfirst"):
            findings.append(Finding("warning", tag, f"{aslug}: missing standfirst"))

        # images
        img = meta.get("image") or art.get("image")
        if img:
            norm = img[3:] if img.startswith("../") else img
            check_image(norm, f"{aslug}.image")
            if not (meta.get("imageCredit") or art.get("imageCredit")):
                findings.append(Finding("warning", tag, f"{aslug}: image without imageCredit/imageSource"))

        # pre-generated article audio (optional while the back catalogue is migrated)
        audio = art.get("audio")
        if audio is not None:
            if not isinstance(audio, dict):
                findings.append(Finding("error", tag, f"{aslug}: audio must be an object"))
            else:
                url = audio.get("url")
                duration = audio.get("durationSeconds")
                audio_hash = audio.get("contentHash")
                generation = audio.get("generation")
                if not isinstance(url, str) or not re.match(r"^https://", url):
                    findings.append(Finding("error", tag, f"{aslug}: audio.url must be an https URL"))
                if not isinstance(duration, (int, float)) or duration <= 0:
                    findings.append(Finding("error", tag, f"{aslug}: audio.durationSeconds must be positive"))
                if not isinstance(audio_hash, str) or not re.fullmatch(r"[0-9a-f]{64}", audio_hash):
                    findings.append(Finding("error", tag, f"{aslug}: audio.contentHash must be a SHA-256 hex hash"))
                if not isinstance(generation, str) or not generation:
                    findings.append(Finding("error", tag, f"{aslug}: audio.generation is required"))

        # roster check
        byline = art.get("byline") or meta.get("byline")
        if roster_bylines is not None and byline and byline not in roster_bylines:
            findings.append(
                Finding("error", tag, f"{aslug}: byline {byline!r} not in redaktion/modeller.json roster")
            )

        # figures vs [FIGUR] markers
        figure_markers = FIGURE_MARKER_RE.findall(body)
        figures_declared = meta.get("figures") or []
        if len(figure_markers) != len(figures_declared):
            findings.append(
                Finding(
                    "error", tag,
                    f"{aslug}: {len(figure_markers)} [FIGUR] markers in body vs "
                    f"{len(figures_declared)} in frontmatter figures:",
                )
            )

        # chart markers
        for cid in CHART_MARKER_RE.findall(body):
            if cid not in chart_ids:
                findings.append(Finding("error", tag, f"{aslug}: [CHART {cid}] has no matching chart json"))

        # footnotes
        defined = set(FOOTNOTE_DEF_RE.findall(body))
        referenced = set(FOOTNOTE_REF_RE.findall(body))
        for undefined in referenced - defined:
            findings.append(Finding("error", tag, f"{aslug}: footnote [^{undefined}] referenced but never defined"))
        for unreferenced in defined - referenced:
            findings.append(Finding("error", tag, f"{aslug}: footnote [^{unreferenced}] defined but never referenced"))

        # nbsp before %
        if PLAIN_PERCENT_RE.search(body):
            n = len(PLAIN_PERCENT_RE.findall(body))
            findings.append(
                Finding("warning", tag, f"{aslug}: {n} instance(s) of plain space before %% (should be \\u00a0%%)")
            )

        # hedge density, "Tallet"-format sections only
        section = art.get("section", "")
        if "tallet" in section.lower() or "tallet" in aslug.lower():
            words = re.findall(r"\S+", body)
            hedge_count = sum(body.lower().count(h) for h in HEDGES)
            if words and (hedge_count / len(words)) * 1000 > 15:
                findings.append(
                    Finding(
                        "warning", tag,
                        f"{aslug}: hedge density {hedge_count / len(words) * 1000:.1f}/1000w in a "
                        f"'Tallet'-format article — numbers column reads as vague",
                    )
                )

        # against the commission ledger, if one exists
        opgave = ledger_by_slug.get(aslug)
        if opgave:
            brief = opgave.get("brief", {})
            words_n = len(re.findall(r"\S+", body))
            lo, hi = brief.get("words", [None, None])
            if lo and hi and not (lo * 0.75 <= words_n <= hi * 1.25):
                findings.append(
                    Finding("warning", tag, f"{aslug}: {words_n} words, outside briefed [{lo}, {hi}] by >25%")
                )
            must_cite = brief.get("mustCite")
            actual_cites = len(defined)
            if must_cite is not None and actual_cites < must_cite:
                findings.append(
                    Finding("warning", tag, f"{aslug}: {actual_cites} citations, briefed mustCite={must_cite}")
                )

    # orphan images on disk
    images_dir = issue_dir / "images"
    if images_dir.is_dir():
        on_disk = {f"images/{p.name}" for p in images_dir.iterdir() if p.is_file() and p.suffix != ".md"}
        orphans = on_disk - declared_images - seen_images
        for o in sorted(orphans):
            findings.append(Finding("warning", tag, f"orphan image on disk, not referenced anywhere: {o}"))

    return findings


def iter_issues():
    for magazine_dir in sorted(CONTENT_DIR.iterdir()):
        if not magazine_dir.is_dir():
            continue
        issues_dir = magazine_dir / "issues"
        if not issues_dir.is_dir():
            continue
        for issue_dir in sorted(issues_dir.iterdir()):
            if issue_dir.is_dir():
                yield magazine_dir, issue_dir


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug", nargs="?", help="Magazine slug, e.g. dosis")
    ap.add_argument("issue_slug", nargs="?", help="Issue slug, e.g. 2026-08-nr1")
    ap.add_argument("--all", action="store_true", help="Check every issue in content/")
    ap.add_argument("--errors-only", action="store_true", help="Print/exit on errors only, suppress warnings")
    args = ap.parse_args()

    if args.all:
        targets = list(iter_issues())
    elif args.slug and args.issue_slug:
        magazine_dir = CONTENT_DIR / args.slug
        issue_dir = magazine_dir / "issues" / args.issue_slug
        if not issue_dir.is_dir():
            print(f"No such issue: {issue_dir}", file=sys.stderr)
            sys.exit(2)
        targets = [(magazine_dir, issue_dir)]
    else:
        ap.error("either <slug> <issue-slug>, or --all")
        return

    all_findings: list[Finding] = []
    for magazine_dir, issue_dir in targets:
        all_findings.extend(check_issue(magazine_dir, issue_dir))

    errors = [f for f in all_findings if f.level == "error"]
    warnings = [f for f in all_findings if f.level == "warning"]

    for f in errors:
        print(f)
    if not args.errors_only:
        for f in warnings:
            print(f)

    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s) across {len(targets)} issue(s).")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
