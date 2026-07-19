#!/usr/bin/env python3
"""Extract text blocks (with font metadata) and images from a ReportLab PDF issue.

Usage:
  .venv/bin/python production/extract_pdf.py content/<slug>/issues/<issue>/<file>.pdf
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

import fitz


def classify_span(size: float, flags: int, body: float) -> str:
    s = round(size, 1)
    is_bold = bool(flags & 2**4)
    if s >= body + 8:
        return "headline"
    if s >= body + 4:
        return "subhead"
    if s >= body + 1.5:
        return "standfirst" if not is_bold else "section"
    if s <= body - 1.5:
        return "caption" if not is_bold else "label"
    if is_bold and s >= body:
        return "emphasis"
    return "body"


def page_blocks_raw(page: fitz.Page) -> list[dict]:
    d = page.get_text("dict", flags=fitz.TEXT_PRESERVE_WHITESPACE)
    raw = []
    for b in d.get("blocks", []):
        if b.get("type") != 0:
            continue
        lines = []
        sizes = []
        for line in b.get("lines", []):
            spans = line.get("spans", [])
            if not spans:
                continue
            text = "".join(s.get("text", "") for s in spans)
            if not text.strip():
                continue
            main = max(
                spans,
                key=lambda s: abs(s.get("bbox", [0, 0, 0, 0])[2] - s.get("bbox", [0, 0, 0, 0])[0]),
            )
            size = float(main.get("size", 0))
            sizes.append(size)
            lines.append(
                {
                    "text": text,
                    "size": round(size, 2),
                    "font": main.get("font", ""),
                    "flags": main.get("flags", 0),
                    "color": main.get("color", 0),
                    "bbox": [round(x, 1) for x in line.get("bbox", (0, 0, 0, 0))],
                }
            )
        if not lines:
            continue
        bb = b.get("bbox", (0, 0, 0, 0))
        raw.append(
            {
                "bbox": [round(x, 1) for x in bb],
                "x0": round(bb[0], 1),
                "y0": round(bb[1], 1),
                "x1": round(bb[2], 1),
                "y1": round(bb[3], 1),
                "lines": lines,
                "avg_size": sum(sizes) / len(sizes) if sizes else 0,
            }
        )
    return raw


def assign_columns(blocks: list[dict], page_width: float) -> list[dict]:
    """Detect 1 or 2 columns from x0 clustering; assign col index; sort reading order."""
    if not blocks:
        return blocks
    # Mid-page gap heuristic: two columns if many blocks start past page mid
    mid = page_width * 0.45
    left = [b for b in blocks if b["x0"] < mid]
    right = [b for b in blocks if b["x0"] >= mid]
    # full-width blocks (span across)
    full = [b for b in blocks if (b["x1"] - b["x0"]) > page_width * 0.55]

    two_col = len(right) >= 3 and len(left) >= 3
    if not two_col:
        for b in blocks:
            b["col"] = 0
        blocks.sort(key=lambda b: (b["y0"], b["x0"]))
        return blocks

    # full-width first (headers), then left column top-to-bottom, then right
    for b in blocks:
        if b in full or (b["x1"] - b["x0"]) > page_width * 0.55:
            b["col"] = -1  # full width
        elif b["x0"] < mid:
            b["col"] = 0
        else:
            b["col"] = 1
    blocks.sort(key=lambda b: (0 if b["col"] < 0 else 1, b["col"], b["y0"], b["x0"]))
    return blocks


def extract_page(page: fitz.Page, page_no: int) -> dict:
    raw = page_blocks_raw(page)
    all_sizes = [ln["size"] for b in raw for ln in b["lines"]]
    body = Counter(round(s, 1) for s in all_sizes).most_common(1)[0][0] if all_sizes else 10.0
    raw = assign_columns(raw, page.rect.width)

    flat_lines = []
    for b in raw:
        for ln in b["lines"]:
            role = classify_span(ln["size"], ln["flags"], body)
            flat_lines.append(
                {
                    "text": ln["text"],
                    "size": ln["size"],
                    "font": ln["font"],
                    "flags": ln["flags"],
                    "color": ln["color"],
                    "bbox": ln["bbox"],
                    "origin_y": ln["bbox"][1],
                    "col": b["col"],
                    "role": role,
                    "body_size": body,
                }
            )
    return {
        "page": page_no,
        "width": page.rect.width,
        "height": page.rect.height,
        "body_size": body,
        "blocks": flat_lines,
    }


def extract_images(doc: fitz.Document, out_dir: Path) -> list[dict]:
    img_dir = out_dir / "images"
    img_dir.mkdir(parents=True, exist_ok=True)
    seen: set[int] = set()
    catalog: list[dict] = []
    for page_no, page in enumerate(doc, start=1):
        for img_i, img in enumerate(page.get_images(full=True), start=1):
            xref = img[0]
            if xref in seen:
                continue
            seen.add(xref)
            try:
                pix = fitz.Pixmap(doc, xref)
                if pix.n - pix.alpha > 3:
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                if pix.width < 80 or pix.height < 80:
                    continue
                name = f"p{page_no:02d}_img{img_i:02d}_{pix.width}x{pix.height}.png"
                path = img_dir / name
                pix.save(path.as_posix())
                catalog.append(
                    {
                        "page": page_no,
                        "file": f"images/{name}",
                        "width": pix.width,
                        "height": pix.height,
                        "xref": xref,
                    }
                )
            except Exception as e:
                catalog.append({"page": page_no, "error": str(e), "xref": xref})
    return catalog


def page_text_dump(page_data: dict) -> str:
    lines = [f"===== PAGE {page_data['page']} (body≈{page_data['body_size']}) ====="]
    prev_col = None
    for b in page_data["blocks"]:
        if prev_col is not None and b["col"] != prev_col:
            lines.append(f"--- col {b['col']} ---")
        prev_col = b["col"]
        t = b["text"].rstrip()
        lines.append(f"[{b['role']}|{b['size']}|c{b['col']}] {t}")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pdf", type=Path)
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args()
    pdf = args.pdf.resolve()
    if not pdf.exists():
        print(f"PDF not found: {pdf}", file=sys.stderr)
        return 1
    out = (args.out or (pdf.parent / "_extract")).resolve()
    out.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(pdf)
    pages = []
    text_parts = []
    for i, page in enumerate(doc, start=1):
        pdata = extract_page(page, i)
        pages.append(pdata)
        text_parts.append(page_text_dump(pdata))

    images = extract_images(doc, out)

    # color samples: sample top bar pixels more densely for brand color
    page0 = doc[0]
    pix = page0.get_pixmap(matrix=fitz.Matrix(0.5, 0.5), alpha=False)
    samples = []
    w, h = pix.width, pix.height
    for x, y in [
        (5, 5),
        (w // 4, 5),
        (w // 2, 5),
        (3 * w // 4, 5),
        (w // 2, h // 10),
        (w // 2, h // 3),
        (w // 4, h // 2),
    ]:
        r, g, b = pix.pixel(min(x, w - 1), min(y, h - 1))
        samples.append({"x": x, "y": y, "rgb": f"#{r:02x}{g:02x}{b:02x}"})

    meta = {
        "pdf": pdf.name,
        "page_count": doc.page_count,
        "images": images,
        "color_samples": samples,
    }
    (out / "meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out / "pages.json").write_text(json.dumps(pages, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out / "pages.txt").write_text("\n\n".join(text_parts) + "\n", encoding="utf-8")
    print(f"Extracted {doc.page_count} pages → {out}")
    print(f"  images: {len(images)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
