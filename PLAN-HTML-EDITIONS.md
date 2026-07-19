# Plan: HTML editions of the two current PDFs (phone-first)

Detailed execution plan for turning **PULSEN nr. 1** and **SPÆNDING nr. 1** into HTML that reads comfortably on a phone. This is the concrete version of Phases 1–2 in [PLAN.md](PLAN.md), applied to the two existing issues.

## Principle: reflow, don't reproduce

An A4 print spread cannot be shrunk onto a 375-px screen. The HTML edition keeps the magazine's **identity** — colors, typography feel, section structure, covers, bylines with model credits — but reflows every article into a single readable column. The PDF stays available as the "print edition" download; the HTML is the phone edition.

## Step 1 — Extract content from the PDFs

One-time, per issue. The PDFs are ReportLab-generated with embedded text, so this is scripted + an editorial proofing pass.

1. **Tooling:** `production/extract_pdf.py` using PyMuPDF (`pip install pymupdf` in a venv). Dump per-page text blocks (with font size/style metadata — that's how headlines, standfirsts, body, and captions are told apart) and export all embedded images. PULSEN's cover and article images exist *only* inside its PDF; SPÆNDING's four PNGs are already in `images/` but its PDF may contain more.
2. **Reassemble into articles:** one markdown file per article in `content/<slug>/issues/<issue>/articles/NN-<slug>.md` with the frontmatter defined in PLAN.md (title, standfirst, byline/model, section, order, image). Number files in reading order.
3. **Model the special formats** so the web can style them:
   - Pull quotes → blockquote with a marker (`> !citat …`).
   - Fact boxes / "Rygtebørsen" items / kolofon → fenced blocks (```` ```faktaboks ````, ```` ```rygte ````) or sections with headings — decide once, use in both issues.
   - PULSEN's quiz + logic puzzle → structured list; answers separated so the web can hide them behind a tap (`<details>`).
4. **Clean the artifacts:** strip running headers/footers and page numbers; join hard line breaks and de-hyphenate words split at line ends; verify æ/ø/å survived everywhere.
5. **Proof against the PDF:** compare per-article word counts script-dump vs. final markdown; read every article once side-by-side. Nothing may silently disappear — this is the only copy of the content.
6. **Record metadata:** fill `articles[]` in both `issue.json` files; read PULSEN's brand colors off the extracted pages/images and complete `content/pulsen/magazine.json`.

## Step 2 — Optimize images for mobile

The current PNGs are 0.7–1.1 MB each — too heavy for a phone edition.

- Convert to WebP (or AVIF) at 2 widths (~800 px and ~1600 px) targeting 100–250 KB each; keep originals in `images/`, derivatives generated at build time (e.g. `vite-imagetools`) so `content/` stays clean.
- Covers get a small blurred placeholder for instant paint.

## Step 3 — Render as the SvelteKit reading experience

No throwaway interim site: the two extracted issues become the first content of the `web/` app (PLAN.md Phase 2), whose issue/article pages **are** the HTML editions. Phone-first design rules:

- **Reading column:** single column, `max-width: 65ch`, 17–18 px base size, line-height ~1.65, `hyphens: auto` with `lang="da"` (Danish words are long — hyphenation matters on narrow screens).
- **Typography:** serif body + sans headings echoing the print edition; self-hosted subset fonts or a system stack (zero external requests). Drop caps on feature openers, styled pull quotes, section label in the magazine's accent color.
- **Issue page = contents page:** cover on top, then a tappable card per article (section, title, standfirst, byline) mirroring the PDF's indholdsfortegnelse, plus the PDF download link.
- **Article navigation:** sticky mini-header (magazine name, section, progress bar); footer with forrige/næste artikel and "til indholdet" — the "leafing through" feel.
- **No JS required to read:** everything prerendered; quiz answers via `<details>`, progress bar as progressive enhancement.
- **Budget:** each article page under ~300 KB transferred, Lighthouse mobile ≥ 95.

## Step 4 — Verify on a phone

- Browser preview at 375×812 (and 320 px width worst case): check hyphenation, table/fact-box overflow (`overflow-x` inside the box, never the page), image weights, dark mode.
- Read both issues end-to-end on an actual phone before calling it done.

## Order of work

1. Extraction script + SPÆNDING nr. 1 (easier: images already exported) → proof.
2. PULSEN nr. 1 (incl. image extraction + brand colors) → proof.
3. Scaffold `web/`, build kiosk → magazine → issue → article routes with the two issues.
4. Image pipeline + mobile polish + phone QA.
5. Deploy preview to Vercel and read on a phone.

Steps 1–2 are the careful part (the PDFs are the only source); 3–5 is ordinary SvelteKit work with the design rules above.
