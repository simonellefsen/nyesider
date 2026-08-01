"""Generate article art with xAI Imagine, in a named graphic-design style.

Realistic photo-look is one option among many — not the default for every
figure. A magazine where all art is AI-realism looks monotonous, so pick a
style per article and vary it across an issue. The catalogue below follows
The Noun Project's 17 graphic design styles:
https://blog.thenounproject.com/graphic-design-styles/

Usage:

    python production/generate_image.py \
        --style flat \
        --out content/dosis/issues/2026-08-nr1/images/dosis_pulver.png \
        --prompt "a protein shaker on the left, a plate of real food on the right"

    python production/generate_image.py --list-styles

House rules baked into every prompt: no logos, no readable packaging text,
no brand marks (see redaktion/README.md, "Billeder (copyright-politik)").
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from load_env import load_imagine_env  # noqa: E402

API_URL = "https://api.x.ai/v1/images/generations"
DEFAULT_MODEL = "grok-imagine-image"

# The Noun Project's 17 styles, as prompt fragments.
STYLES: dict[str, str] = {
    "minimalism": (
        "minimalist graphic design, very limited colour palette, minimal shading, "
        "generous white space, simple geometric forms, nothing decorative"
    ),
    "maximalism": (
        "maximalist graphic design, densely layered composition filling the frame, "
        "unexpected clashing colour palette, pattern on pattern, deliberately unbalanced"
    ),
    "typographic": (
        "typographic poster design where lettering is the main visual element, "
        "bold expressive type as image, supporting shapes only"
    ),
    "retro": (
        "retro 1960s-70s poster design, vintage screen-print texture, warm faded "
        "palette, psychedelic curves, halftone grain, aged paper feel"
    ),
    "abstract": (
        "abstract graphic composition detached from literal reality, contrasting "
        "forms and tones, open to interpretation, no recognisable scene"
    ),
    "geometric": (
        "geometric graphic design built on straight lines, precise angles and exact "
        "shapes, mathematical symmetry and balance, grid-based"
    ),
    "flat": (
        "flat two-dimensional vector illustration, solid fills, no gradients, no "
        "shadows, no depth, clean icon-like shapes, limited palette"
    ),
    "three-dimensional": (
        "three-dimensional render with realistic light and shadow, volumetric depth, "
        "soft studio lighting, tactile materials"
    ),
    "organic": (
        "organic illustration with natural textures, earthy palette, fluid hand-drawn "
        "lines, botanical forms, imperfect edges"
    ),
    "modern": (
        "modern mid-century-descended graphic design, vivid palette, irregular "
        "geometric shapes, clean sans-serif sensibility, confident negative space"
    ),
    "corporate": (
        "restrained corporate graphic style, conservative professional palette, "
        "simple shapes, clean lines, uncluttered"
    ),
    "illustrated": (
        "hand-drawn editorial illustration with visible personal mark-making, "
        "ink line and wash, illustrator's touch"
    ),
    "playful": (
        "playful illustration for a young audience, vibrant palette, bouncy rounded "
        "shapes, characterful and imaginative"
    ),
    "feminine": (
        "soft feminine design language, pastel palette, delicate decorative detail, "
        "flowing cursive-like forms"
    ),
    "masculine": (
        "masculine design language, thick heavy strokes, muted palette, rugged "
        "textures, blunt forms"
    ),
    "grunge": (
        "grunge design, distressed rough textures, irregular torn lines, dark "
        "somber mood, photocopied zine feel"
    ),
    "photorealism": (
        "photorealistic editorial photograph, natural light, shallow depth of field, "
        "documentary framing"
    ),
}

# Applied to every prompt regardless of style.
HOUSE_RULES = (
    "No logos, no brand marks, no readable packaging text, no legible words or "
    "letters anywhere in the image. Editorial magazine illustration."
)


def build_prompt(subject: str, style: str, palette: str | None = None) -> str:
    if style not in STYLES:
        raise SystemExit(
            f"Unknown style {style!r}. Options: {', '.join(sorted(STYLES))}"
        )
    parts = [subject.strip().rstrip("."), STYLES[style]]
    if palette:
        parts.append(f"colour palette anchored on {palette}")
    parts.append(HOUSE_RULES)
    return ". ".join(parts) + "."


def generate(prompt: str, out: Path, model: str = DEFAULT_MODEL) -> Path:
    load_imagine_env()
    body = json.dumps(
        {
            "model": model,
            "prompt": prompt,
            "n": 1,
            "response_format": "b64_json",
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        API_URL,
        data=body,
        headers={
            "Authorization": f"Bearer {os.environ['XAI_API_KEY']}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        payload = json.load(resp)
    data = payload.get("data") or []
    if not data or not data[0].get("b64_json"):
        raise SystemExit(f"No image returned: {json.dumps(payload)[:400]}")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(base64.b64decode(data[0]["b64_json"]))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--prompt", help="What the image shows (the subject, in English)")
    ap.add_argument("--style", help=f"One of: {', '.join(sorted(STYLES))}")
    ap.add_argument("--out", type=Path, help="Output .png path")
    ap.add_argument("--palette", help="Optional colour anchor, e.g. the title's hexes")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument(
        "--list-styles", action="store_true", help="Print the style catalogue and exit"
    )
    args = ap.parse_args()

    if args.list_styles:
        for name, desc in sorted(STYLES.items()):
            print(f"{name:20} {desc}")
        return

    if not (args.prompt and args.style and args.out):
        ap.error("--prompt, --style and --out are required")

    prompt = build_prompt(args.prompt, args.style, args.palette)
    path = generate(prompt, args.out, args.model)
    print(f"{path} ({path.stat().st_size // 1024} kB) · style={args.style}")


if __name__ == "__main__":
    main()
