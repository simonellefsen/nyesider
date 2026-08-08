# Nye Sider

Danish AI-magazine publisher. Content is `content/<slug>/`; editorial process and memory is `redaktion/`; the SvelteKit site is `web/`.

**Before producing or editing any issue, read [`redaktion/README.md`](redaktion/README.md) and the title's own `redaktion/<slug>/redaktionsnotesbog.md`.** They are the actual playbook — this file only points at them so a session can't skip straight to writing files.

> ## ⛔ READ FIRST — 2026-08-08: 17 issues were unpublished for fabricated authorship
>
> On 2026-08-08, **191 articles across 17 issues** were rolled back to `status: draft`.
> They had been published crediting named models (GPT-5.6 Terra, Gemini 3.1 Pro, Mistral
> Large, Qwen3.7 Max …) in the byline, while `bestilling.json` showed **no `costUSD`, no
> `receipt.draft`, and no file in `kladder/`** for a single one of them — and the
> OpenRouter dashboard confirmed several of those titles' keys (KulturBoxen, Orbit,
> Kraften) had **never been called at all**. The verdicts (`accepted`, `rejected`) described
> judgements of drafts that were never requested. In other words: both the byline and the
> audit trail were invented.
>
> **If you are a new agent picking this repo up, the three rules that follow are not
> style preferences. They are why that happened.**
>
> 1. **A byline is a factual claim.** Never put a model's name on an article that model did
>    not write. If you wrote it, there is no byline — the rebuild standard agreed with the
>    owner on 2026-08-08 is *no byline* until a real author can be documented.
> 2. **A verdict without a receipt is fabrication.** `verdict.status` may only be written
>    after a real draft exists at `receipt.draft` with a real `receipt.costUSD`. If you did
>    not call the API, the honest value is `writer.model: "editor-led"` and **no** model byline.
> 3. **Use the title's own key.** `.env.<slug>`, never another title's. Spend on the wrong
>    key is how this became invisible — the owner spotted it because the dashboard showed
>    the other keys untouched.
>
> Unpublished and awaiting genuine production: `kronike/2026-08-nr1`, plus the
> `2026-08-08` issues of dosis, gnisten, horisonten, humanerd, indeni, kraften,
> kulturboxen, orbit, pulsen, spaending — and the `2026-08-01` **first** issues of
> dosis, humanerd, indeni, kraften, kulturboxen, orbit. Do **not** flip any of these back
> to `published` without doing the work. Each carries `unpublishedReason` in its `issue.json`.

Non-negotiables:

- **The byline must name whoever actually wrote the text.** Model byline ⇔ a real API call
  on that title's key, with cost and draft recorded. No call → no model byline. This is the
  one rule whose breach invalidates everything else in the publication.
- **Never publish an article without a `bestilling.json` entry.** Every article gets a written brief (`brief.angle`, `brief.words`, `brief.mustCite`) before commissioning and a written verdict (`verdict.status`, `citations`) before it lands in `content/`. See [`redaktion/bestilling.schema.md`](redaktion/bestilling.schema.md). `mustCite: 0` is a legal, common, deliberate choice — an *unset* citation requirement is not.
- **One commission per shell call.** The sandbox has a documented ~45s ceiling per call; `production/commission.py` (when it exists) enforces one article per invocation on purpose.
- **Never batch-commission a whole issue in one pass.** Article length collapsed 30–70% across the August 2026 issues when the portfolio doubled and briefs got thinner under time pressure — that drift happened silently. Depth-vs-breadth is a decision `budget` in `bestilling.json` makes you write down, not one automation should make for you.
- **Run `production/check_issue.py <slug> <issue-slug>` before marking an issue published.** It catches what silently degrades otherwise: missing images, filename/order mismatches, broken footnotes and chart refs, and **draft/editor-note voice** in published bodies (TODOs, “Brug X som kilde”, production imperatives). A feature that still reads like a brief or checklist is not accepted — rewrite or park it; never leave it after the bagsnit as a “last page.”
- **Explain jargon on first mention — per article.** EU packages, US statutes, grid operators, orbit classes, and industry labels (Fit for 55, IRA, PJM, LEO, NASA HLS, FCC, FAA, …) get a one-line Danish gloss the first time they appear *in that article*. Do not assume the reader remembers nr. 1 or works in the field. Use a footnote if the expansion would break the sentence.
- **Preflight before push / before calling the work done.** From repo root run `npm run preflight` (or rely on the git `pre-push` hook). That runs content-errors (`check_issue.py --all --errors-only`), `svelte-check`, unit tests, and the full `web` production build — the same path Vercel uses, plus lint/tests. Do **not** push content or web changes that fail preflight; Vercel failing is a process bug, not an acceptable feedback loop. Bypass only with explicit `SKIP_PREFLIGHT=1` when the user asks.
- **At most one published issue per magazine per calendar day.** `issue.json` `published` is a `YYYY-MM-DD` day stamp. Never stamp a second DOSIS (or any title) with the same day as an existing `status: published` issue of that title — even in a “weekly batch.” Check [`redaktion/udgivelseskalender.md`](redaktion/udgivelseskalender.md) or run `python3 production/udgivelseskalender.py --check` before setting the date; `check_issue.py` errors on collisions. Multiple *different* magazines may share a day.
- **Per-title API keys are load-bearing, not ceremonial.** Only `.env.<slug>` for OpenRouter text on that title; only `.env.local` for the shared xAI Imagine key. Never borrow another title's key — cost attribution depends on it. The key files that exist today: `.env.dosis`, `.env.gnisten`, `.env.horisonten`, `.env.humanerd`, `.env.indeni`, `.env.kraften`, `.env.kronike`, `.env.kulturboxen`, `.env.orbit`, `.env.pulsen`, `.env.spaending` (all gitignored). A **new title needs its own key before its first commission** — ask the owner; do not fall back to another title's. `production/commission.py` loads via `load_title_env(slug)` precisely so this cannot be fudged.
- **Verify every URL before it ships — never guess an address.** A footnote once linked to a Danish Nationalbank page whose path had been translated by hand from the English URL; it 404'd in the published article. Run `npm run check:links` (or `python3 production/check_links.py <slug> <issue-slug>`). It separates *dead* (404/410 — fix) from *bot-blocked* (403/406 — usually fine in a browser). It also runs as a non-blocking step in `npm run preflight`; non-blocking is not permission to ignore it.
- **Cross-title links break the build when the sister issue is unpublished.** Prerendering fails hard on a dead internal link (that is correct behaviour — it is a 404 for a real reader). If you unpublish an issue, de-link any references to it from still-published articles; keep the words, drop the `](/…)`.

This file is intentionally short. The real editorial judgment — angle, casting, fact-checking, house style — lives in `redaktion/README.md` and is not mechanized here.
