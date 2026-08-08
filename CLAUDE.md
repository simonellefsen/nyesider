# Nye Sider

Danish AI-magazine publisher. Content is `content/<slug>/`; editorial process and memory is `redaktion/`; the SvelteKit site is `web/`.

**Before producing or editing any issue, read [`redaktion/README.md`](redaktion/README.md) and the title's own `redaktion/<slug>/redaktionsnotesbog.md`.** They are the actual playbook — this file only points at them so a session can't skip straight to writing files.

Non-negotiables:

- **Never publish an article without a `bestilling.json` entry.** Every article gets a written brief (`brief.angle`, `brief.words`, `brief.mustCite`) before commissioning and a written verdict (`verdict.status`, `citations`) before it lands in `content/`. See [`redaktion/bestilling.schema.md`](redaktion/bestilling.schema.md). `mustCite: 0` is a legal, common, deliberate choice — an *unset* citation requirement is not.
- **One commission per shell call.** The sandbox has a documented ~45s ceiling per call; `production/commission.py` (when it exists) enforces one article per invocation on purpose.
- **Never batch-commission a whole issue in one pass.** Article length collapsed 30–70% across the August 2026 issues when the portfolio doubled and briefs got thinner under time pressure — that drift happened silently. Depth-vs-breadth is a decision `budget` in `bestilling.json` makes you write down, not one automation should make for you.
- **Run `production/check_issue.py <slug> <issue-slug>` before marking an issue published.** It catches what silently degrades otherwise: missing images, filename/order mismatches, broken footnotes and chart refs, and **draft/editor-note voice** in published bodies (TODOs, “Brug X som kilde”, production imperatives). A feature that still reads like a brief or checklist is not accepted — rewrite or park it; never leave it after the bagsnit as a “last page.”
- **Explain jargon on first mention.** EU packages, US statutes, grid operators, and industry labels (Fit for 55, IRA, PJM, …) get a one-line Danish gloss the first time they appear. Do not assume the reader already works in that field.
- **Per-title API keys are load-bearing, not ceremonial.** Only `.env.<slug>` for OpenRouter text on that title; only `.env.local` for the shared xAI Imagine key. Never borrow another title's key — cost attribution depends on it.

This file is intentionally short. The real editorial judgment — angle, casting, fact-checking, house style — lives in `redaktion/README.md` and is not mechanized here.
