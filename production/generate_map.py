"""Generate locator/region maps from public-domain Natural Earth vector data.

Public-domain alternative to `generate_image.py` for the one kind of figure
AI image generation can't produce honestly: "where is this place". Natural
Earth (https://www.naturalearthdata.com/) is explicit public domain — no
attribution required, but we print a small credit line into the figure
anyway since that's how `figur-*.svg` diagrams already credit their source.

Data is cached locally in `production/.mapcache/` (gitignored, ~35 MB) and
downloaded on first use — nothing is committed to the repo.

Usage — locator map (country highlighted within its region):

    python production/generate_map.py \\
        --out content/kulturboxen/issues/2026-08-nr4/images/kort-marokko.svg \\
        --title "Marokko" \\
        --note "Fire byer, fire forskellige historier i dette nummer" \\
        --bbox -14,26.5,0,36.5 \\
        --highlight-country Morocco \\
        --marker "Rabat:34.020:-6.841" \\
        --marker "Casablanca:33.573:-7.589" \\
        --marker "Marrakech:31.629:-7.981" \\
        --marker "Fes:34.020:-5.004"

Usage — sub-country region map (admin-1 provinces dissolved into one
highlight, for places like Sicily that aren't their own admin-0 country):

    python production/generate_map.py \\
        --out content/horisonten/issues/2026-08-nr4/images/kort-sicilien.svg \\
        --title "Sicilien" \\
        --bbox 11.8,36.4,15.8,38.6 \\
        --highlight-admin1-country Italy \\
        --highlight-admin1 "Trapani,Palermo,Messina,Agrigento,Caltanissetta,Enna,Catania,Ragusa,Siracusa" \\
        --marker "Palermo:38.116:13.362" \\
        --marker "Catania:37.502:15.087" \\
        --marker "Messina:38.193:15.554"

Then in the article frontmatter:

    figures:
      - ../images/kort-marokko.svg

And a `[FIGUR]` marker line, positionally matched, in the body — see
`redaktion/README.md`, "Kort (maps)".
"""

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path
from urllib.request import urlretrieve

REPO_ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = Path(__file__).resolve().parent / ".mapcache"
NE_BASE = "https://naturalearth.s3.amazonaws.com"

DATASETS = {
    "admin_0": ("10m_cultural/ne_10m_admin_0_countries.zip", "ne_10m_admin_0_countries"),
    "admin_1": (
        "10m_cultural/ne_10m_admin_1_states_provinces.zip",
        "ne_10m_admin_1_states_provinces",
    ),
    "places": ("10m_cultural/ne_10m_populated_places.zip", "ne_10m_populated_places"),
    "land": ("10m_physical/ne_10m_land.zip", "ne_10m_land"),
    "ocean": ("10m_physical/ne_10m_ocean.zip", "ne_10m_ocean"),
}

STYLES = {
    "light": dict(
        ocean="#dce8ea",
        land="#f7f4ef",
        border="#c9c2b4",
        highlight="#c9842f",
        highlight_edge="#8f5c1c",
        marker="#1a1a1a",
        text="#1a1a1a",
        text_muted="#5c5c5c",
        bg="#fffcf7",
    ),
    "dark": dict(
        ocean="#071c2c",
        land="#102c3e",
        border="#2f5060",
        highlight="#e88d45",
        highlight_edge="#f5c99a",
        marker="#f5f5ef",
        text="#f5f5ef",
        text_muted="#d7e8e4",
        bg="#071c2c",
    ),
}


def _ensure_dataset(key: str) -> Path:
    """Download + unzip a Natural Earth 10m dataset into CACHE_DIR on first use."""
    rel_zip, dirname = DATASETS[key]
    out_dir = CACHE_DIR / dirname
    shp = out_dir / f"{dirname}.shp"
    if shp.is_file():
        return shp
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    zip_path = CACHE_DIR / Path(rel_zip).name
    url = f"{NE_BASE}/{rel_zip}"
    print(f"downloading {url}", file=sys.stderr)
    urlretrieve(url, zip_path)
    with zipfile.ZipFile(zip_path) as zf:
        zf.extractall(out_dir)
    zip_path.unlink()
    if not shp.is_file():
        raise SystemExit(f"expected {shp} after extracting {url}")
    return shp


def _parse_bbox(raw: str) -> tuple[float, float, float, float]:
    parts = [float(x) for x in raw.split(",")]
    if len(parts) != 4:
        raise SystemExit("--bbox needs lonmin,latmin,lonmax,latmax")
    return parts[0], parts[1], parts[2], parts[3]


def _parse_marker(raw: str) -> tuple[str, float, float]:
    label, lat, lon = raw.split(":")
    return label.strip(), float(lat), float(lon)


def build(args: argparse.Namespace) -> Path:
    import geopandas as gpd
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patheffects import withStroke

    palette = STYLES[args.style]
    lonmin, latmin, lonmax, latmax = _parse_bbox(args.bbox)
    aspect = (lonmax - lonmin) / max(latmax - latmin, 0.01)

    # Clip to the map extent (+ margin) before plotting — otherwise matplotlib
    # embeds full-resolution 10m global coastline/border vertices into the
    # output file even for geometry entirely off-screen, ballooning SVG size.
    margin = max(lonmax - lonmin, latmax - latmin) * 0.15
    clip_box = (lonmin - margin, latmin - margin, lonmax + margin, latmax + margin)

    land = gpd.clip(gpd.read_file(_ensure_dataset("land"), bbox=clip_box), clip_box)
    ocean = gpd.clip(gpd.read_file(_ensure_dataset("ocean"), bbox=clip_box), clip_box)
    admin0 = gpd.clip(gpd.read_file(_ensure_dataset("admin_0"), bbox=clip_box), clip_box)

    fig_w = 10.0
    fig_h = max(fig_w / max(aspect, 0.3), 5.0)
    fig, ax = plt.subplots(figsize=(fig_w, fig_h))
    fig.patch.set_facecolor(palette["bg"])
    ax.set_facecolor(palette["ocean"])

    ocean.plot(ax=ax, color=palette["ocean"], zorder=0)
    land.plot(ax=ax, color=palette["land"], zorder=1)
    admin0.boundary.plot(ax=ax, color=palette["border"], linewidth=0.6, zorder=2)

    if args.highlight_country:
        for name in args.highlight_country:
            sel = admin0[admin0["NAME"].str.lower() == name.lower()]
            if sel.empty:
                sel = admin0[admin0["NAME_LONG"].str.lower() == name.lower()]
            if sel.empty:
                raise SystemExit(f"country not found in Natural Earth admin_0: {name!r}")
            sel.plot(
                ax=ax,
                color=palette["highlight"],
                edgecolor=palette["highlight_edge"],
                linewidth=1.0,
                zorder=3,
            )

    if args.highlight_admin1:
        admin1 = gpd.read_file(_ensure_dataset("admin_1"))
        names = [n.strip() for n in args.highlight_admin1.split(",")]
        sel = admin1[
            (admin1["admin"].str.lower() == args.highlight_admin1_country.lower())
            & (admin1["name"].isin(names))
        ]
        found = set(sel["name"])
        missing = set(names) - found
        if missing:
            raise SystemExit(f"admin-1 names not found under {args.highlight_admin1_country!r}: {missing}")
        sel.plot(
            ax=ax,
            color=palette["highlight"],
            edgecolor=palette["highlight_edge"],
            linewidth=1.0,
            zorder=3,
        )

    for raw in args.marker or []:
        label, lat, lon = _parse_marker(raw)
        ax.scatter([lon], [lat], s=46, color=palette["marker"], edgecolor=palette["bg"], linewidth=1.2, zorder=5)
        txt = ax.text(
            lon + (lonmax - lonmin) * 0.012,
            lat,
            label,
            fontsize=12,
            color=palette["text"],
            va="center",
            zorder=6,
            fontfamily="sans-serif",
        )
        txt.set_path_effects([withStroke(linewidth=3, foreground=palette["bg"])])

    ax.set_xlim(lonmin, lonmax)
    ax.set_ylim(latmin, latmax)
    ax.set_aspect(1.0 / max(0.15, __import__("math").cos(__import__("math").radians((latmin + latmax) / 2))))
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.text(
        0.02, 0.965, args.title, transform=ax.transAxes,
        fontsize=22, fontweight="bold", color=palette["text"], va="top", fontfamily="sans-serif",
    )
    if args.note:
        ax.text(
            0.02, 0.90, args.note, transform=ax.transAxes,
            fontsize=12, color=palette["text_muted"], va="top", fontfamily="sans-serif",
        )
    credit = args.credit or "Kilde: Natural Earth (public domain)"
    ax.text(
        0.02, 0.02, credit, transform=ax.transAxes,
        fontsize=9.5, color=palette["text_muted"], va="bottom", fontfamily="sans-serif",
    )

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout(pad=0.4)
    fig.savefig(out, facecolor=palette["bg"])
    plt.close(fig)
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True, type=Path, help="Output .svg or .png path")
    ap.add_argument("--title", required=True)
    ap.add_argument("--note", help="Optional subtitle line")
    ap.add_argument("--credit", help="Override the default Natural Earth credit line")
    ap.add_argument("--bbox", required=True, help="lonmin,latmin,lonmax,latmax")
    ap.add_argument(
        "--highlight-country", action="append",
        help="Admin-0 country name to fill (Natural Earth NAME field); repeatable",
    )
    ap.add_argument(
        "--highlight-admin1",
        help="Comma-separated admin-1 (province/state) names to dissolve into one highlight, e.g. Sicilian provinces",
    )
    ap.add_argument(
        "--highlight-admin1-country",
        help="Country the --highlight-admin1 provinces belong to (Natural Earth 'admin' field)",
    )
    ap.add_argument(
        "--marker", action="append",
        help='"Label:lat:lon", repeatable, e.g. "Rabat:34.020:-6.841"',
    )
    ap.add_argument("--style", choices=sorted(STYLES), default="light")
    args = ap.parse_args()

    if args.highlight_admin1 and not args.highlight_admin1_country:
        ap.error("--highlight-admin1 requires --highlight-admin1-country")

    path = build(args)
    print(f"{path} ({path.stat().st_size // 1024} kB)")


if __name__ == "__main__":
    main()
