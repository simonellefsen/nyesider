# `bestilling.json` — commissioning ledger spec

One file per issue, at `redaktion/<slug>/numre/<issue-slug>/bestilling.json`, plus a sibling `kladder/` directory holding each writer's raw, unedited draft (`kladder/NN-<slug>.md`).

This lives in `redaktion/` (editorial memory), not `content/` (the clean publishable surface `web/scripts/sync-content-assets.mjs` walks blindly) — same reasoning as `redaktion/<slug>/parked/`.

**Why this file exists:** the editorial contract used to be verbal — the ask (brief) was never written down, only the result (the article). That asymmetry is why 60% of published articles ended up with zero citations: sourcing was an editor's *acceptance criterion*, never a writer's *deliverable*. This file moves the ask upstream, in writing, per article.

## Shape

```json
{
  "magazine": "<slug>",
  "issue": "<YYYY-MM-nrN>",
  "issueTheme": "<string, optional>",
  "budget": {
    "articles": 14,
    "wordsPerArticle": [450, 650],
    "targetPages": 16,
    "note": "<optional prose — why this budget>"
  },
  "opgaver": [
    {
      "slug": "<article-slug, matches issue.json>",
      "order": 3,
      "section": "<section name>",
      "brief": {
        "angle": "<one or two sentences — the actual ask>",
        "words": [450, 650],
        "mustCite": 3,
        "mustNumber": ["<specific figures the piece must include>"],
        "format": "leder | feature | essay | ordbog | rygteboersen | tallet | krydslink | ..."
      },
      "writer": {
        "byline": "<canonical display name, see redaktion/modeller.json>",
        "model": "<OpenRouter id, or \"chefredaktør\" if editor-written>",
        "fallback": "<OpenRouter id or null>"
      },
      "receipt": {
        "words": 612,
        "costUSD": null,
        "draft": "kladder/03-<slug>.md"
      },
      "verdict": {
        "status": "accepted | accepted-after-edit | rewritten-by-editor | rejected | fallback-used",
        "checkedAt": "YYYY-MM-DD",
        "citations": 4,
        "editorNote": "<what happened, in one sentence>"
      }
    }
  ]
}
```

## Field rules

- **`brief.mustCite` is required on every `opgave`, and `0` is a legal, common value.** A leder, an ordbog, en rygtebørs-klumme, or a first-person anecdote genuinely needs no footnotes. The point is forcing the editor to write `0` *deliberately* — the machine ([`check_issue.py`](../production/check_issue.py)) only checks that the declared number was met; a human decides what the number should be.
- **`brief.words` and `brief.mustCite` get pasted verbatim into the writer's prompt** — see `redaktion/README.md` step 3. This is what makes the length-drift lesson in `modelkartotek.md` ("brief shorter from the start, don't over-write then trim") actually enforceable instead of folklore.
- **`budget`** makes the depth-vs-breadth trade for the whole issue a written, defended decision — not something that drifts silently across a busy production week.
- **`verdict.status`** is the sign-off that used to not exist anywhere. Closed vocabulary, five values only (see above). `rewritten-by-editor` covers cases like DOSIS's "Tallet", which was rebuilt from scratch by the chefredaktør rather than lightly edited.
- **`receipt.costUSD`** is populated by `production/commission.py` (Phase 3) via `"usage": {"include": true}` on the OpenRouter call. Hand-entered `null` is acceptable for editor-written pieces (`writer.model: "chefredaktør"`), which have no API cost.
- **`kladder/NN-<slug>.md`** holds the writer's raw response, unedited. `git diff` between the kladde and the published `content/**/articles/NN-<slug>.md` *is* the editor↔writer relationship rendered as a diff — it's the input to `production/modelstats.py` (Phase 4)'s "editorial intervention rate" per model.

## What this is not

Not a gate that blocks anything by itself — `production/check_issue.py` reads it and reports mismatches (declared `mustCite` vs. actual footnote count, `words` range vs. actual) as warnings, never hard errors. A missing or wrong ledger should never be able to break a deploy; a missing *image* should. See `redaktion/README.md` and `production/check_issue.py`'s own docstring for the full errors/warnings split.

## Example

See [`redaktion/dosis/numre/2026-08-nr1/bestilling.json`](dosis/numre/2026-08-nr1/bestilling.json) — retro-filled from the published issue as the first worked example. Its `retrofitNote` field explains which parts are exact (word counts, citation counts — counted directly from the shipped text) and which are reconstructed best-guesses (the original brief wording, since it predates this file format and was never recorded).
