"""Derive a per-model stats table from every redaktion/*/numre/*/bestilling.json.

Replaces the hand-maintained, staleness-prone half of modelkartotek.md with
something that regenerates from what actually happened. Two fidelity
levels, both useful:

  - qualitative columns (commissions, verdict counts, words-in-range,
    citations-met) work from Phase 1 alone — every bestilling.json has them.
  - cost, latency and finish_reason columns need Phase 3 (commission.py)
    receipts and are blank ("—") until a model has real commissioned runs.

Usage:

    python production/modelstats.py            # print markdown table
    python production/modelstats.py --write     # write into modelkartotek.md
                                                  # between the AUTO markers
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
AUTO_START = "<!-- AUTO:modelstats:start -->"
AUTO_END = "<!-- AUTO:modelstats:end -->"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def find_ledgers():
    return sorted(REPO_ROOT.glob("redaktion/*/numre/*/bestilling.json"))


def in_range(n: int, lo: int, hi: int) -> bool:
    return lo <= n <= hi


def compute_stats() -> dict[str, dict]:
    stats: dict[str, dict] = {}

    for lp in find_ledgers():
        ledger = load_json(lp)
        for opgave in ledger.get("opgaver", []):
            writer = opgave.get("writer", {})
            byline = writer.get("byline", "?")
            if byline not in stats:
                stats[byline] = {
                    "commissions": 0,
                    "verdicts": {},
                    "words_in_range": 0,
                    "words_total": 0,
                    "cites_met": 0,
                    "cites_total": 0,
                    "costs": [],
                    "finish_length_count": 0,
                    "finish_total": 0,
                }
            s = stats[byline]
            s["commissions"] += 1

            verdict = opgave.get("verdict", {}).get("status", "unknown")
            s["verdicts"][verdict] = s["verdicts"].get(verdict, 0) + 1

            brief = opgave.get("brief", {})
            receipt = opgave.get("receipt", {})
            words = receipt.get("words")
            lo_hi = brief.get("words")
            if words is not None and lo_hi:
                s["words_total"] += 1
                if in_range(words, lo_hi[0], lo_hi[1]):
                    s["words_in_range"] += 1

            must_cite = brief.get("mustCite")
            citations = opgave.get("verdict", {}).get("citations")
            if must_cite is not None and citations is not None:
                s["cites_total"] += 1
                if citations >= must_cite:
                    s["cites_met"] += 1

            cost = receipt.get("costUSD")
            if cost is not None:
                s["costs"].append(cost)

    return stats


def render_table(stats: dict[str, dict]) -> str:
    rows = []
    header = (
        "| Model | Kommissioner | Godkendt | Efter redigering | Omskrevet | Afvist | "
        "Ord i mål | Kilder opfyldt | Total omkostning (USD) |"
    )
    sep = "|---|---|---|---|---|---|---|---|---|"
    rows.append(header)
    rows.append(sep)

    for byline in sorted(stats, key=lambda b: -stats[b]["commissions"]):
        s = stats[byline]
        v = s["verdicts"]
        words_col = (
            f"{s['words_in_range']}/{s['words_total']}" if s["words_total"] else "—"
        )
        cites_col = f"{s['cites_met']}/{s['cites_total']}" if s["cites_total"] else "—"
        cost_col = f"{sum(s['costs']):.4f}" if s["costs"] else "—"
        rows.append(
            f"| {byline} | {s['commissions']} | {v.get('accepted', 0)} | "
            f"{v.get('accepted-after-edit', 0)} | {v.get('rewritten-by-editor', 0)} | "
            f"{v.get('rejected', 0)} | {words_col} | {cites_col} | {cost_col} |"
        )

    return "\n".join(rows)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true", help="Write table into redaktion/modelkartotek.md")
    args = ap.parse_args()

    stats = compute_stats()
    ledgers = find_ledgers()
    table = render_table(stats)
    note = (
        f"_Afledt af {len(ledgers)} `bestilling.json`-ledger(e) — "
        f"kør `python production/modelstats.py` for at gendanne. "
        f"Kolonner uden data (—) venter på flere kommissioner via `commission.py`._"
    )
    block = f"{table}\n\n{note}"

    if not args.write:
        print(block)
        return

    mk_path = REPO_ROOT / "redaktion" / "modelkartotek.md"
    text = mk_path.read_text(encoding="utf-8")
    if AUTO_START not in text or AUTO_END not in text:
        raise SystemExit(
            f"{mk_path} has no {AUTO_START}/{AUTO_END} markers — add them where the "
            f"generated table should live, then rerun with --write."
        )
    new_text = re.sub(
        rf"{re.escape(AUTO_START)}.*?{re.escape(AUTO_END)}",
        f"{AUTO_START}\n{block}\n{AUTO_END}",
        text,
        flags=re.DOTALL,
    )
    mk_path.write_text(new_text, encoding="utf-8")
    print(f"Wrote stats table into {mk_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
