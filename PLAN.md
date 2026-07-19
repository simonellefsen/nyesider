# Nye Sider · Web Reading Experience — Plan

Goal: a web-based reading experience for the Nye Sider magazines (PULSEN, SPÆNDING, and future titles) that carries over the look and feel of the PDF editions, built with **SvelteKit** and deployed on **Vercel**. The PDFs remain available as downloads; the web version becomes the primary reading surface.

## Guiding decisions

- **Markdown is the canonical content format going forward.** The existing two issues only exist as PDFs, so their articles must be extracted once (Phase 1). Every future issue is produced markdown-first, with the PDF as an export — never the other way around again.
- **One SvelteKit app, many magazines.** Each title is themed via its `magazine.json` (colors, name, sections); adding a third title requires zero code, only content.
- **Fully prerendered.** All pages are static at build time (content lives in the repo), which makes Vercel hosting trivial, fast, and free-tier friendly.

## Repo layout (Phase 0 — done)

```
nyesider/
├── content/                  # canonical published content
│   └── <slug>/               # pulsen, spaending, …
│       ├── magazine.json     # brand: name, tagline, colors, sections, audience
│       └── issues/<YYYY-MM-nrN>/
│           ├── issue.json    # issue manifest incl. articles[] reading order
│           ├── articles/     # one .md per article (Phase 1 for existing issues)
│           ├── images/       # cover + article images
│           └── <issue>.pdf   # the print edition, offered as download
├── redaktion/                # editorial memory (see redaktion/README.md)
│   ├── modelkartotek.md      # shared OpenRouter model experience, used for casting
│   └── <slug>/redaktionsnotesbog.md   # story leads, follow-ups, promises made in print
├── web/                      # SvelteKit app (Phase 2)
├── production/               # (future) issue-production scripts, e.g. build_magazine.py
├── .env.<slug>               # one OpenRouter key PER TITLE (.env.pulsen, .env.spaending) — gitignored
└── PLAN.md                   # this file
```

## Phase 1 — Extract the two existing issues from PDF

> Detailed, phone-first execution plan for converting the two current PDF editions to HTML: **[PLAN-HTML-EDITIONS.md](PLAN-HTML-EDITIONS.md)** (covers this phase and the mobile reading design of Phase 2).

The PDFs are ReportLab-generated with embedded text, so extraction is mechanical, then editorial:

1. Install a one-off extraction tool (`pip install pymupdf`) and dump text + images per page for both PDFs. PULSEN's article images exist only inside the PDF; SPÆNDING's four PNGs are already in `images/`.
2. Reassemble into one markdown file per article in `articles/`, with frontmatter:

   ```yaml
   ---
   title: "…"
   standfirst: "…"        # underrubrik
   byline: "GPT-5.6 Terra" # the model, as credited in the kolofon
   section: "Teknologi"
   order: 3
   image: "../images/spaending_faststof.png"  # optional
   ---
   ```

3. Fill `articles[]` in each `issue.json` (slug, file, order) and record PULSEN's actual brand colors in its `magazine.json` (read them off the PDF).
4. Proof against the PDF — extraction must not silently drop pull quotes, fact boxes, or the quiz/games section (model those as markdown blockquotes/fenced blocks the web app styles specially).

## Phase 2 — SvelteKit app (`web/`)

- **Stack:** SvelteKit 2 + Svelte 5, TypeScript, `@sveltejs/adapter-vercel`, `prerender = true` everywhere. Markdown compiled at build time (unified/remark or mdsvex) from `../content` via a server-only loader.
- **Routes:**
  - `/` — the kiosk: publisher front page, all titles with latest covers.
  - `/[magazine]` — magazine front: brand identity, issue archive.
  - `/[magazine]/[issue]` — cover + contents page mirroring the PDF's indholdsfortegnelse, plus PDF download.
  - `/[magazine]/[issue]/[article]` — the reading view.
- **Design — "print, but comfortable":** per-magazine theme from `magazine.json` via CSS custom properties (SPÆNDING: `#0E3A5C`/`#19B5C8`/`#F2A03D`); serif body type echoing the PDF, magazine conventions (standfirst, drop cap, pull quotes, section labels, byline with model credit); measured line length (~65ch), generous leading; sequential navigation (prev/next article, "bladre" feel).
- **Danish throughout:** UI copy, `lang="da"`, dates in Danish.

## Phase 3 — Polish

Open Graph/social cards from covers · reading-progress indicator · interactive quiz section (PULSEN) as a progressive enhancement · sitemap + RSS per magazine · Vercel Analytics.

## Phase 4 — Vercel deployment

1. Push repo to GitHub, import in Vercel, set **Root Directory = `web/`** (content is read from the repo at build time, so `../content` is available during build).
2. Preview deployments per branch; production on `main`. No runtime env vars needed (the OpenRouter key is production-side only, never used by the site).
3. Custom domain when ready (e.g. `nyesider.dk`).
4. Note: the Vercel MCP connector in this environment isn't authenticated yet — deploys can run via `vercel` CLI or the Vercel dashboard either way.

## Phase 5 — Future issue workflow

New issue = one editor-in-chief agent session: read `redaktion/` → produce articles as markdown into a new `content/<slug>/issues/…/` folder + images + `issue.json` → export PDF (recreate the ReportLab script in `production/`, it was not preserved from the original sessions) → update notesbog + modelkartotek → merge to `main` → Vercel auto-deploys. The website needs no changes for new issues or new titles.

### Cost accounting per title

Each magazine has its **own OpenRouter API key** in `.env.<slug>` so spend is separable in the OpenRouter dashboard. The workflow builds on that:

- A production session for a title loads only that title's key (`.env.pulsen` for PULSEN etc.); a new title gets a fresh key and a fresh `.env.<slug>` before its first issue.
- At the end of a production, the agent reads the session's spend (OpenRouter credits/usage per key, or summed from per-request `usage` fields) and records it in the issue's `issue.json` as `productionCostUSD`, optionally with a breakdown (`text`, `images`).
- That makes cost-per-issue and cost-per-title queryable straight from `content/` — and it could even surface in the kolofon on the web edition if you ever want to publish it.
- The web app itself never uses any key: it is fully static, so publishing costs on Vercel stay at zero/hobby tier and all OpenRouter spend is attributable to editorial production.

## Open questions (decide later, nothing blocks)

- Domain name (`nyesider.dk`?) and whether the kiosk page gets its own Nye Sider brand identity.
- Whether to render the games/quiz pages interactively or as styled static pages in v1 (recommendation: static in v1).
- Whether PDFs should be Git LFS if the repo grows (currently ~7 MB total — fine as-is).
