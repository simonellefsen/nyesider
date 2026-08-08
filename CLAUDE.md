# Nye Sider

Danish AI-magazine publisher. Content is `content/<slug>/`; editorial process and memory is `redaktion/`; the SvelteKit site is `web/`.

**Before producing or editing any issue, read [`redaktion/README.md`](redaktion/README.md) and the title's own `redaktion/<slug>/redaktionsnotesbog.md`.** They are the actual playbook — this file only points at them so a session can't skip straight to writing files.

Non-negotiables:

- **Never publish an article without a `bestilling.json` entry.** Every article gets a written brief (`brief.angle`, `brief.words`, `brief.mustCite`) before commissioning and a written verdict (`verdict.status`, `citations`) before it lands in `content/`. See [`redaktion/bestilling.schema.md`](redaktion/bestilling.schema.md). `mustCite: 0` is a legal, common, deliberate choice — an *unset* citation requirement is not.
- **One commission per shell call.** The sandbox has a documented ~45s ceiling per call; `production/commission.py` (when it exists) enforces one article per invocation on purpose.
- **Never batch-commission a whole issue in one pass.** Article length collapsed 30–70% across the August 2026 issues when the portfolio doubled and briefs got thinner under time pressure — that drift happened silently. Depth-vs-breadth is a decision `budget` in `bestilling.json` makes you write down, not one automation should make for you.
- **Run `production/check_issue.py <slug> <issue-slug>` before marking an issue published.** It catches what silently degrades otherwise: missing images, filename/order mismatches, broken footnotes and chart refs, and **draft/editor-note voice** in published bodies (TODOs, “Brug X som kilde”, production imperatives). A feature that still reads like a brief or checklist is not accepted — rewrite or park it; never leave it after the bagsnit as a “last page.”
- **Explain jargon on first mention — per article.** EU packages, US statutes, grid operators, orbit classes, and industry labels (Fit for 55, IRA, PJM, LEO, NASA HLS, FCC, FAA, …) get a one-line Danish gloss the first time they appear *in that article*. Do not assume the reader remembers nr. 1 or works in the field. Use a footnote if the expansion would break the sentence.
- **Preflight before push / before calling the work done.** From repo root run `npm run preflight` (or rely on the git `pre-push` hook). That runs content-errors (`check_issue.py --all --errors-only`), `svelte-check`, unit tests, and the full `web` production build — the same path Vercel uses, plus lint/tests. Do **not** push content or web changes that fail preflight; Vercel failing is a process bug, not an acceptable feedback loop. Bypass only with explicit `SKIP_PREFLIGHT=1` when the user asks.
- **Per-title API keys are load-bearing, not ceremonial.** Only `.env.<slug>` for OpenRouter text on that title; only `.env.local` for the shared xAI Imagine key. Never borrow another title's key — cost attribution depends on it.

This file is intentionally short. The real editorial judgment — angle, casting, fact-checking, house style — lives in `redaktion/README.md` and is not mechanized here.
