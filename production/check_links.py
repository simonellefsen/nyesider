#!/usr/bin/env python3
"""Verify that every external link in published content actually resolves.

Born from a real miss: a footnote in KRØNIKE nr. 1 linked to a Danmarks
Nationalbank page whose Danish URL had been *guessed* by translating the
English path. It 404'd in the published issue. `check_issue.py` never looks
outside the repo, so nothing caught it.

Usage:
    python production/check_links.py                 # every published issue
    python production/check_links.py kronike         # one title
    python production/check_links.py kronike 2026-08-nr1
    python production/check_links.py --json          # machine-readable

Exit code is 1 if any link is broken, so it can gate a push.
Results are cached in .linkcache.json (7 days) to keep reruns cheap and to
avoid hammering other people's servers.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENT = REPO_ROOT / "content"
CACHE_FILE = REPO_ROOT / ".linkcache.json"
CACHE_TTL = 7 * 24 * 3600
UA = "Mozilla/5.0 (compatible; NyeSider-linkcheck/1.0; +editorial link validation)"

# Markdown inline links first — the URL inside (...) is delimited, so URLs that
# themselves contain parentheses (very common for Wikimedia file names) survive
# intact. Bare URLs in prose are picked up by the second pattern.
MD_LINK_RE = re.compile(r"\]\(\s*(https?://[^\s()]*(?:\([^\s()]*\)[^\s()]*)*)\s*\)")
BARE_URL_RE = re.compile(r"(?<![(\]])\bhttps?://[^\s<>\"'`\])]+")

# Hosts that block automated HEAD/GET but are stable, well-known destinations.
# Skipped deliberately rather than reported as false failures.
SKIP_HOSTS = {"x.ai"}


def find_links(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    out: set[str] = set()
    spans: list[tuple[int, int]] = []
    for m in MD_LINK_RE.finditer(text):
        # No rstrip here: inside ](...) the URL is already delimited, and Danish
        # lex.dk slugs for regnal names genuinely end in a period
        # (…/Margrete_1., …/Christian_3.). Stripping it invents a 404.
        out.add(m.group(1))
        spans.append(m.span())
    for m in BARE_URL_RE.finditer(text):
        if any(s <= m.start() < e for s, e in spans):
            continue
        out.add(m.group(0).rstrip(".,;:"))
    return out


def check(url: str) -> tuple[str, int, str]:
    host = urllib.parse.urlparse(url).netloc.lower().removeprefix("www.")
    if host in SKIP_HOSTS:
        return url, 0, "skipped (blocks bots)"
    req = urllib.request.Request(url, headers={"User-Agent": UA}, method="GET")
    last = ""
    # Transient resets are common when several requests hit one host at once;
    # a genuine 404 never becomes a 200 on retry, so this only filters noise.
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return url, r.status, ""
        except urllib.error.HTTPError as e:
            # 5xx and 429 are the server having a moment, not a missing page.
            # Retry those; 404/410 never become 200, so return immediately.
            if e.code >= 500 or e.code == 429:
                last = f"{e.code} {e.reason or ''}".strip()
                time.sleep(1.5 * (attempt + 1))
                continue
            return url, e.code, e.reason or ""
        except Exception as e:  # noqa: BLE001 - network errors are the point
            last = str(e)[:120]
            time.sleep(1.5 * (attempt + 1))
    m = re.match(r"^(\d{3})", last)
    return (url, int(m.group(1)), last) if m else (url, 0, last)


def load_cache() -> dict:
    if not CACHE_FILE.exists():
        return {}
    try:
        raw = json.loads(CACHE_FILE.read_text())
    except json.JSONDecodeError:
        return {}
    now = time.time()
    return {k: v for k, v in raw.items() if now - v.get("at", 0) < CACHE_TTL}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("magazine", nargs="?")
    ap.add_argument("issue", nargs="?")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-cache", action="store_true")
    ap.add_argument("--include-drafts", action="store_true",
                    help="also check issues with status != published — needed when\nvalidating an issue before (re)publishing it")
    args = ap.parse_args()

    import urllib.parse  # noqa: PLC0415 - used inside check()
    globals()["urllib"].parse = urllib.parse

    roots = [CONTENT / args.magazine] if args.magazine else sorted(
        p for p in CONTENT.iterdir() if p.is_dir()
    )

    targets: list[tuple[str, Path]] = []
    for mag in roots:
        issues_dir = mag / "issues"
        if not issues_dir.exists():
            continue
        for issue_dir in sorted(issues_dir.iterdir()):
            if args.issue and issue_dir.name != args.issue:
                continue
            meta = issue_dir / "issue.json"
            if not meta.exists():
                continue
            if (not args.include_drafts
                    and json.loads(meta.read_text()).get("status") != "published"):
                continue
            for f in sorted(issue_dir.rglob("*.md")):
                targets.append((f"{mag.name}/{issue_dir.name}", f))

    links: dict[str, set[str]] = {}
    for label, f in targets:
        for url in find_links(f):
            links.setdefault(url, set()).add(f"{label}:{f.name}")

    cache = {} if args.no_cache else load_cache()
    todo = [u for u in links if u not in cache]

    results: dict[str, dict] = {u: dict(cache[u]) for u in links if u in cache}
    if todo:
        with ThreadPoolExecutor(max_workers=8) as pool:
            for url, status, note in pool.map(check, todo):
                results[url] = {"status": status, "note": note, "at": time.time()}

    if not args.no_cache:
        CACHE_FILE.write_text(json.dumps(results, indent=0))

    # 403/406/429 are overwhelmingly bot-blocking (Tesla, Uber, some press sites)
    # rather than a dead page. Reporting them as failures trains people to ignore
    # the tool, so they are warnings — only 4xx/5xx that mean "gone" fail the run.
    SOFT = {403, 406, 429}
    broken, blocked = {}, {}
    for u, r in results.items():
        st, note = r["status"], r.get("note", "")
        # Any 2xx is a success, not just 200. IEEE Xplore answers 202 as part of
        # its bot mitigation, and reporting a live page as dead is exactly the
        # kind of false alarm that trains people to stop reading the output.
        if (st is not None and 200 <= st < 300) or "skipped" in note:
            continue
        # A 5xx is the origin having a bad minute, not a missing page — the
        # fetch helper above already says so and retries. Calling it DEAD sends
        # the editor to re-source a URL that is fine an hour later.
        (blocked if (st in SOFT or (st is not None and st >= 500)) else broken)[u] = r

    if args.json:
        print(json.dumps({
            "dead": {u: {**r, "usedIn": sorted(links[u])} for u, r in broken.items()},
            "blocked": {u: {**r, "usedIn": sorted(links[u])} for u, r in blocked.items()},
        }, ensure_ascii=False, indent=2))
    else:
        for u in sorted(broken):
            r = broken[u]
            print(f"[DEAD {r['status'] or 'ERR'}] {u}")
            for where in sorted(links[u]):
                print(f"         used in {where}")
            if r["note"]:
                print(f"         {r['note']}")
        if blocked:
            print(f"\n{len(blocked)} link(s) did not answer an automated request "
                  f"(403/406/429 bot-blocking, or a 5xx server hiccup) — usually "
                  f"fine in a browser, verify by hand if you doubt one:")
            for u in sorted(blocked):
                print(f"  [{blocked[u]['status']}] {u}")
        cached = len(links) - len(todo)
        print(f"\n{len(links)} link(s) checked ({cached} from cache), "
              f"{len(broken)} dead, {len(blocked)} unverifiable.")

    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
