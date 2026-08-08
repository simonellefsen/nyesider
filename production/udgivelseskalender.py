#!/usr/bin/env python3
"""Publish calendar ledger for Nye Sider.

Rebuilds redaktion/udgivelseskalender.md from content/*/issues/*/issue.json
so editors and agents can see which calendar days are already taken *per
magazine* before stamping a new published date.

Rule (enforced by production/check_issue.py):
  At most one status=published issue per magazine per calendar day (YYYY-MM-DD).

Usage:
    python3 production/udgivelseskalender.py           # rewrite the ledger
    python3 production/udgivelseskalender.py --check    # exit 1 if collisions
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = REPO_ROOT / "content"
LEDGER_PATH = REPO_ROOT / "redaktion" / "udgivelseskalender.md"


def collect() -> dict[str, list[dict]]:
    """magazine -> list of {slug, number, published, status, theme}."""
    out: dict[str, list[dict]] = {}
    if not CONTENT_DIR.is_dir():
        return out
    for mag_dir in sorted(CONTENT_DIR.iterdir()):
        issues_dir = mag_dir / "issues"
        if not mag_dir.is_dir() or not issues_dir.is_dir():
            continue
        rows: list[dict] = []
        for issue_dir in sorted(issues_dir.iterdir()):
            ij = issue_dir / "issue.json"
            if not issue_dir.is_dir() or not ij.exists():
                continue
            try:
                data = json.loads(ij.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                continue
            rows.append(
                {
                    "slug": issue_dir.name,
                    "number": data.get("number"),
                    "published": data.get("published"),
                    "status": data.get("status"),
                    "theme": data.get("issueTheme") or data.get("title") or "",
                }
            )
        if rows:
            out[mag_dir.name] = rows
    return out


def find_collisions(data: dict[str, list[dict]]) -> list[str]:
    msgs: list[str] = []
    for mag, rows in sorted(data.items()):
        by_day: dict[str, list[str]] = defaultdict(list)
        for r in rows:
            if r["status"] != "published" or not r["published"]:
                continue
            by_day[str(r["published"])].append(r["slug"])
        for day, slugs in sorted(by_day.items()):
            if len(slugs) > 1:
                msgs.append(f"{mag}: {day} used by {', '.join(slugs)}")
    return msgs


def render(data: dict[str, list[dict]]) -> str:
    lines = [
        "# Udgivelseskalender",
        "",
        "Automatisk ledger over `published`-datoer i `content/*/issues/*/issue.json`.",
        "Genopbyg: `python3 production/udgivelseskalender.py`.",
        "",
        "## Regel",
        "",
        "**Højst ét `status: published`-nummer pr. magasin pr. kalenderdag** "
        "(`YYYY-MM-DD`). Flere titler *må* udkomme samme dag (uge-batch), men "
        "DOSIS nr. 2 og nr. 3 må ikke dele `2026-08-08`.",
        "",
        "Håndhæves som **ERROR** i `production/check_issue.py` (og dermed i "
        "`npm run preflight` / Vercel-build).",
        "",
        "## Før du sætter `published`",
        "",
        "1. Kør denne fil — er dagen allerede taget for titlen?",
        "2. Eller: `python3 production/check_issue.py <slug> <issue-slug>`.",
        "3. Ny dag: typisk næste planlagte udgivelsesvindue (fx +7 dage), "
        "ikke “i dag igen” under batch-pres.",
        "",
    ]

    # Chronological index of published days
    day_index: dict[str, list[str]] = defaultdict(list)
    for mag, rows in data.items():
        for r in rows:
            if r["status"] == "published" and r["published"]:
                day_index[str(r["published"])].append(
                    f"{mag}/{r['slug']} (nr. {r['number']})"
                )

    lines += ["## Efter kalenderdag (published)", ""]
    if not day_index:
        lines.append("_Ingen publicerede numre fundet._")
        lines.append("")
    else:
        lines.append("| Dato | Udgivelser |")
        lines.append("|---|---|")
        for day in sorted(day_index.keys()):
            lines.append(f"| {day} | {'; '.join(day_index[day])} |")
        lines.append("")

    lines += ["## Efter magasin", ""]
    for mag, rows in sorted(data.items()):
        lines.append(f"### {mag}")
        lines.append("")
        lines.append("| Nummer | issue-slug | published | status | tema |")
        lines.append("|---|---|---|---|---|")
        for r in sorted(rows, key=lambda x: (x["published"] or "", x["slug"])):
            theme = (r["theme"] or "").replace("|", "/")
            lines.append(
                f"| {r['number']} | `{r['slug']}` | {r['published'] or '—'} | "
                f"{r['status'] or '—'} | {theme} |"
            )
        lines.append("")

    collisions = find_collisions(data)
    lines += ["## Kollisioner (skal være tom)", ""]
    if collisions:
        for c in collisions:
            lines.append(f"- **KOLLISION:** {c}")
    else:
        lines.append("_Ingen — godt._")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 if any same-day collisions exist (does not write the ledger)",
    )
    ap.add_argument(
        "--stdout",
        action="store_true",
        help="Print markdown to stdout instead of writing the ledger file",
    )
    args = ap.parse_args()

    data = collect()
    collisions = find_collisions(data)
    md = render(data)

    if args.check:
        if collisions:
            print("Same-day publish collisions:", file=sys.stderr)
            for c in collisions:
                print(f"  - {c}", file=sys.stderr)
            sys.exit(1)
        print("OK — no same-day collisions.")
        sys.exit(0)

    if args.stdout:
        print(md)
    else:
        LEDGER_PATH.parent.mkdir(parents=True, exist_ok=True)
        LEDGER_PATH.write_text(md, encoding="utf-8")
        print(f"Wrote {LEDGER_PATH.relative_to(REPO_ROOT)}")
        if collisions:
            print("WARNING: collisions present — check_issue will ERROR:", file=sys.stderr)
            for c in collisions:
                print(f"  - {c}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
