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

echo "==> [1/4] content catalogue errors (same as Vercel build gate)"
python3 production/check_issue.py --all --errors-only

echo "==> [2/4] web typecheck (svelte-check)"
npm --prefix web run check

echo "==> [3/4] web unit tests"
npm --prefix web run test:audio

echo "==> [4/4] web production build (sync-assets + content errors + vite)"
npm --prefix web run build

echo ""
echo "Preflight OK — safe to push."
