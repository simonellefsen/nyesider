"""Commission one article's draft from a writer model — the wire, not a factory.

This script is deliberately a thin transport layer, not a replacement for the
editor. It:

  - refuses to run without a written brief already in `bestilling.json`
    (angle, words, mustCite, writer.model) — see redaktion/bestilling.schema.md
  - calls OpenRouter via `load_title_env(slug)`, so cost is attributable to
    the right title's key (never falls back to another title's .env file)
  - prints the full draft to stdout, so the editor reads it in-band in the
    session exactly as before — the kladde file is only the durable copy
  - CANNOT write to content/. It writes only to
    redaktion/<slug>/numre/<issue-slug>/kladder/. The editor still hand-writes
    the accepted article. Typing is not judgement; this script owns only the
    clerical, unobservable part (HTTP, token/cost accounting, retries).
  - is one article per invocation, on purpose — matches the sandbox's
    documented ~45s per-shell-call ceiling. Never batch-commissions a whole
    issue; that is how article length quietly collapsed 30-70% in August
    2026 when briefs got thinner under time pressure and nobody had to look
    at it happening.

Usage:

    python production/commission.py <slug> <issue-slug> <article-slug> [--dry-run] [--fallback]
    python production/commission.py <slug> <issue-slug> --sum

--dry-run prints the assembled prompt without calling the API. Expect this
to be the most-used flag — use it to check the brief reads the way you
intended before spending anything.

--fallback uses writer.fallback from the ledger instead of writer.model
(for when the primary model is known-flaky, e.g. Kimi K3 — see
redaktion/modelkartotek.md).

--sum reads every opgave's receipt.costUSD in the issue's ledger and prints
the total, formatted for pasting into issue.json's productionCostUSD.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from load_env import load_title_env  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
API_URL = "https://openrouter.ai/api/v1/chat/completions"

HOUSE_RULES = """\
Skriv på dansk. Første gang en forkortelse bruges: fuldt navn + forkortelse i \
parentes. Brug ikke-brydende mellemrum (\\u00a0) før %. Opdigt aldrig \
præcise datoer for virkelige begivenheder. Ingen engelsk teen-jargon uden \
forklaring.

OPDIGT ALDRIG EN KILDE. Dette er den vigtigste regel, og den brydes typisk \
i den mest overbevisende form: en konkret, verificerbart klingende detalje. \
Et faktisk eksempel fra denne redaktion — en kladde skrev «menig Rasmus \
Jensen fra 8. Regiment, hvis navn er bevaret i regimentets tabsliste». \
Personen fandtes ikke. Derfor:

- Nævn kun personer, steder, dokumenter og institutioner, som en læser kan \
slå op. Er du i tvivl, om noget findes, så lad være med at nævne det.
- Skriv ALDRIG et citat i anførselstegn, medmindre du er sikker på ordlyden \
OG kan navngive kilden. Ingen citater tilskrevet «en historiker», «en \
samtidig iagttager» eller lignende.
- Opfind ikke arkivreferencer, sagsnumre, tabslister eller sidetal.
- Er du usikker på et tal, så skriv det som en ordenstørrelse med forbehold \
(«i størrelsesordenen», «skøn varierer») — det er altid bedre end et \
falsk-præcist tal.
- Fodnoter skal pege på et navngivet værk eller en navngiven institution. \
Er du ikke sikker på en URL, så skriv værkets titel i stedet for at gætte \
en adresse. En gættet URL er en opdigtet kilde.

Det er bedre at aflevere kortere og rigtigt end længere og opdigtet. \
Chefredaktionen faktatjekker hver kladde og sender fabrikationer retur."""


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def ledger_path(slug: str, issue_slug: str) -> Path:
    return REPO_ROOT / "redaktion" / slug / "numre" / issue_slug / "bestilling.json"


def notebook_excerpt(slug: str) -> str:
    """Pull ## Identitet and ## Format sections out of the title's notebook, if present."""
    nb = REPO_ROOT / "redaktion" / slug / "redaktionsnotesbog.md"
    if not nb.exists():
        return ""
    text = nb.read_text(encoding="utf-8")
    parts = []
    for heading in ("## Identitet", "## Format"):
        m = re.search(rf"^{re.escape(heading)}\n(.*?)(?=\n## |\Z)", text, re.MULTILINE | re.DOTALL)
        if m:
            parts.append(f"{heading}\n{m.group(1).strip()}")
    return "\n\n".join(parts)


def magazine_identity(slug: str) -> str:
    mag_path = REPO_ROOT / "content" / slug / "magazine.json"
    if not mag_path.exists():
        return ""
    mag = load_json(mag_path)
    return f"{mag.get('name', slug)} — {mag.get('tagline', '')}\nMålgruppe: {mag.get('audience', '')}"


def build_prompt(slug: str, opgave: dict) -> str:
    brief = opgave["brief"]
    must_number = brief.get("mustNumber") or []
    lines = [
        magazine_identity(slug),
        notebook_excerpt(slug),
        f"Sektion: {opgave['section']}",
        f"Vinkel: {brief['angle']}",
        f"Ordmål: {brief['words'][0]}-{brief['words'][1]} ord.",
        f"Kildekrav: mindst {brief['mustCite']} fodnote(r) med reelle, klikbare kilder."
        if brief["mustCite"] > 0
        else "Kildekrav: ingen (mustCite=0) — dette er bevidst, ikke en tilladelse til at gætte tal.",
    ]
    if must_number:
        lines.append("Skal indeholde konkrete tal for: " + "; ".join(must_number) + ".")
    lines.append(HOUSE_RULES)
    lines.append("Returnér kun selve artiklen i markdown (ingen frontmatter, ingen forklaring før/efter).")
    return "\n\n".join(p for p in lines if p)


def call_openrouter(model: str, prompt: str) -> dict:
    # Deliberately no "reasoning" field: some models return HTTP 400 on an
    # explicit reasoning:{enabled:false} (redaktion/modelkartotek.md's known
    # gotcha). Omitting it entirely is the documented fallback, so that's
    # the only mode this sends — no retry branch needed for a field we
    # never include.
    body = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "usage": {"include": True},
    }
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {__import__('os').environ['OPENROUTER_API_KEY']}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        payload = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"OpenRouter HTTP {e.code}: {payload[:500]}")


def cmd_sum(slug: str, issue_slug: str) -> None:
    ledger = load_json(ledger_path(slug, issue_slug))
    total = 0.0
    n = 0
    for opgave in ledger["opgaver"]:
        cost = opgave.get("receipt", {}).get("costUSD")
        if cost is not None:
            total += cost
            n += 1
    print(f"productionCostUSD: {round(total, 4)}  ({n}/{len(ledger['opgaver'])} opgaver has cost recorded)")


def cmd_commission(slug: str, issue_slug: str, article_slug: str, dry_run: bool, use_fallback: bool) -> None:
    lp = ledger_path(slug, issue_slug)
    if not lp.exists():
        raise SystemExit(
            f"No bestilling.json at {lp} — write the brief first. See redaktion/bestilling.schema.md."
        )
    ledger = load_json(lp)
    opgave = next((o for o in ledger["opgaver"] if o["slug"] == article_slug), None)
    if opgave is None:
        raise SystemExit(f"No opgave with slug={article_slug!r} in {lp}")

    brief = opgave.get("brief", {})
    missing = [k for k in ("angle", "words", "mustCite") if k not in brief]
    if missing:
        raise SystemExit(f"opgave {article_slug!r} brief is missing required field(s): {missing}")

    writer = opgave.get("writer", {})
    model = writer.get("fallback") if use_fallback else writer.get("model")
    if not model:
        raise SystemExit(f"opgave {article_slug!r} has no writer.{'fallback' if use_fallback else 'model'}")
    if model == "chefredaktør":
        raise SystemExit("This opgave is editor-written (writer.model=chefredaktør) — nothing to commission.")

    prompt = build_prompt(slug, opgave)

    if dry_run:
        print("--- PROMPT (dry run, not sent) ---")
        print(prompt)
        print(f"\n--- would call model: {model} ---")
        return

    load_title_env(slug)
    result = call_openrouter(model, prompt)
    draft = result["choices"][0]["message"]["content"]
    usage = result.get("usage", {})
    cost = usage.get("cost")
    finish_reason = result["choices"][0].get("finish_reason")
    word_count = len(re.findall(r"\S+", draft))

    kladder_dir = lp.parent / "kladder"
    kladder_dir.mkdir(parents=True, exist_ok=True)
    kladde_path = kladder_dir / f"{opgave['order']:02d}-{article_slug}.md"
    kladde_path.write_text(draft, encoding="utf-8")

    opgave["receipt"] = {
        "words": word_count,
        "costUSD": cost,
        "draft": f"kladder/{kladde_path.name}",
    }
    opgave.setdefault("writer", {})["model"] = model
    save_json(lp, ledger)

    print(f"--- DRAFT ({model}, {word_count} words, cost=${cost}, finish={finish_reason}) ---\n")
    print(draft)
    print(f"\n--- saved: {kladde_path.relative_to(REPO_ROOT)} ---")
    if finish_reason == "length":
        print("WARNING: finish_reason=length — model likely ran out of budget mid-answer. Consider --fallback.")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug")
    ap.add_argument("issue_slug")
    ap.add_argument("article_slug", nargs="?")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--fallback", action="store_true")
    ap.add_argument("--sum", action="store_true")
    args = ap.parse_args()

    if args.sum:
        cmd_sum(args.slug, args.issue_slug)
        return
    if not args.article_slug:
        ap.error("article_slug is required unless --sum")
    cmd_commission(args.slug, args.issue_slug, args.article_slug, args.dry_run, args.fallback)


if __name__ == "__main__":
    main()
