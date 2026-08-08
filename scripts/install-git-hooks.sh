#!/usr/bin/env bash
# Point this clone at the repo's shared hooks (pre-push → preflight).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [[ ! -d .git ]]; then
  echo "Not a git checkout — nothing to install."
  exit 0
fi

git config core.hooksPath scripts/githooks
chmod +x scripts/githooks/pre-push scripts/preflight.sh scripts/install-git-hooks.sh

echo "Git hooksPath → scripts/githooks (pre-push runs scripts/preflight.sh)"
echo "Bypass once: SKIP_PREFLIGHT=1 git push"
