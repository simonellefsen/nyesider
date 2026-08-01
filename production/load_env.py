"""Load Nye Sider production secrets with correct cost-tracking boundaries.

Usage (from repo root or production/):

    from load_env import load_title_env, load_imagine_env

    load_title_env("kraften")   # OpenRouter key for that magazine only
    load_imagine_env()          # XAI_API_KEY from .env.local for Imagine

Or CLI:

    python production/load_env.py kraften   # prints which files would load (no secrets)
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def _parse_env_file(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    if not path.is_file():
        return out
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if key:
            out[key] = val
    return out


def load_env_file(path: Path, *, override: bool = True) -> Path | None:
    """Load KEY=VAL pairs into os.environ. Returns path if file existed."""
    if not path.is_file():
        return None
    for k, v in _parse_env_file(path).items():
        if override or k not in os.environ:
            os.environ[k] = v
    return path


def load_imagine_env(*, override: bool = True) -> Path:
    """Load shared xAI Imagine key from .env.local (XAI_API_KEY)."""
    path = REPO_ROOT / ".env.local"
    loaded = load_env_file(path, override=override)
    if not loaded:
        raise FileNotFoundError(
            f"Missing {path} — create it with XAI_API_KEY=... for Imagine images."
        )
    if not os.environ.get("XAI_API_KEY"):
        raise RuntimeError(f"{path} has no XAI_API_KEY")
    return path


def load_title_env(slug: str, *, override: bool = True) -> Path:
    """Load that magazine's OpenRouter key from .env.<slug> only.

    Never falls back to another title's file — cost accounting depends on it.
    """
    slug = slug.strip().lower()
    if not slug or "/" in slug or ".." in slug:
        raise ValueError(f"Invalid magazine slug: {slug!r}")
    path = REPO_ROOT / f".env.{slug}"
    loaded = load_env_file(path, override=override)
    if not loaded:
        raise FileNotFoundError(
            f"Missing {path} — copy .env.example to .env.{slug} "
            f"with a dedicated OPENROUTER_API_KEY for this title."
        )
    if not os.environ.get("OPENROUTER_API_KEY"):
        raise RuntimeError(f"{path} has no OPENROUTER_API_KEY")
    return path


def load_production_env(slug: str) -> dict[str, Path]:
    """Load both Imagine (shared) and title OpenRouter keys for a production run."""
    return {
        "imagine": load_imagine_env(),
        "openrouter": load_title_env(slug),
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python production/load_env.py <magazine-slug>", file=sys.stderr)
        sys.exit(2)
    slug = sys.argv[1]
    paths = load_production_env(slug)
    # Never print secret values — only which files loaded and which keys are set.
    print(f"title={slug}")
    print(f"imagine_env={paths['imagine']}")
    print(f"openrouter_env={paths['openrouter']}")
    print(f"XAI_API_KEY_set={'yes' if os.environ.get('XAI_API_KEY') else 'no'}")
    print(
        f"OPENROUTER_API_KEY_set="
        f"{'yes' if os.environ.get('OPENROUTER_API_KEY') else 'no'}"
    )
