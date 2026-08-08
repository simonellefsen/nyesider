#!/usr/bin/env bash
# Local gate that mirrors (and exceeds) the Vercel build path.
# Vercel runs: npm --prefix web run build
#   → sync-assets + check_issue --all --errors-only + vite build
# This script also runs typecheck (svelte-check) and unit tests first so
# failures show up before a full production build.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [[ "${SKIP_PREFLIGHT:-}" == "1" ]]; then
  echo "SKIP_PREFLIGHT=1 — skipping preflight."
  exit 0
fi

echo "==> [1/5] publish calendar (one issue per magazine per day)"
python3 production/udgivelseskalender.py --check
# Keep the human ledger in sync when preflight is run from a dirty tree.
python3 production/udgivelseskalender.py >/dev/null

echo "==> [2/5] content catalogue errors (same as Vercel build gate)"
python3 production/check_issue.py --all --errors-only

echo "==> [3/5] web typecheck (svelte-check)"
npm --prefix web run check

echo "==> [4/5] web unit tests"
npm --prefix web run test:audio

echo "==> [5/5] web production build (sync-assets + content errors + vite)"
npm --prefix web run build

echo ""
echo "Preflight OK — safe to push."
