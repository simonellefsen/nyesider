# Nye Sider

Dansk magasinforlag, hvor hvert nummer produceres af en chefredaktør-agent med et hold af AI-skribenter via OpenRouter. Udgivelserne findes som PDF og som weblæseoplevelse bygget med SvelteKit på Vercel — se [PLAN.md](PLAN.md) og [PLAN-HTML-EDITIONS.md](PLAN-HTML-EDITIONS.md).

## Titler

| Magasin | Om | Seneste nummer |
|---|---|---|
| **GNISTEN** | AI for begyndere: modeller, priser, opsætning, prompts | Nr. 3 · August 2026 · *"Agenten og den lokale hjerne"* |
| **PULSEN** | Sundhedssektoren, AI i klinikken, ergoterapi | Nr. 3 · August 2026 · *"Når driften taler"* |
| **DOSIS** | Longevity, ernæring, tilskud, proteser/implantater, forskning | Nr. 2 · August 2026 · *"Appetitten under kontrol"* |
| **SPÆNDING** | Elbiler og teknologien bag, europæisk fokus | Nr. 3 · August 2026 · *"Køen, kulden og den næste watt"* |
| **HORISONTEN** | Rejser i Europa — vandring, cykling, løb | Nr. 3 · August 2026 · *"Dolomitterne i efteråret"* |
| **KULTURBOXEN** | Kulturer i hverdagen — set fra Danmark (også oversete) | Nr. 2 · August 2026 · *"Tre sprog, ét plateau"* (Sydtyrol) |
| **KRAFTEN** | Elektrificering globalt + rumkraft (net, el, space) | Nr. 2 · August 2026 · *"Strøm overalt"* |
| **ORBIT** | Rumfart: opsendelser, satellitter, agenturer, skrot, kalender | Nr. 2 · August 2026 · *"Kataloget og kikkerten"* |
| **HumaNerd** | Robotter blandt mennesker — fabrik, lager, hjem | Nr. 2 · August 2026 · *"Lagerets koreografi"* |
| **INDENI** | Hverdagsgenstande indefra — materialer, maskiner, kredsløb | Nr. 2 · August 2026 · *"Filteret"* |
| **Aktier med Grok** | Aktier der er faldet for langt, ser for billige ud, har et 3–6 mdr. argument | Nr. 1 · August 2026 · *"Fem kandidater i et marked uden bred nedtur"* |

## Struktur

- [`content/`](content/) — udgivet indhold: `magazine.json` (brand), numre med `issue.json`, markdown-artikler, billeder og PDF.
- [`redaktion/`](redaktion/README.md) — redaktionel hukommelse: notesbøger og [modelkartotek](redaktion/modelkartotek.md).
- [`web/`](web/) — SvelteKit-app (prerenderet, adapter-vercel).
- [`production/`](production/) — PDF-udtræk og (senere) produktionsscripts.

## Kør websitet lokalt

```bash
cd web
npm install
npm run dev
```

Byg (synkroniserer også billeder/PDF til `static/content/`):

```bash
cd web
npm run build
npm run preview
```

## Preflight før push (undgå Vercel-røde builds)

Vercel kører `npm --prefix web run build`, som blandt andet kører `production/check_issue.py --all --errors-only`. Fejl der skal fanges **lokalt**, før koden forlader maskinen.

```bash
# Fra repo-roden (anbefalet)
npm install          # installerer git pre-push-hook (core.hooksPath → scripts/githooks)
npm run preflight    # content-errors + svelte-check + tests + fuld web-build
```

| Kommando | Hvad den gør |
|---|---|
| `npm run preflight` | Samme porte som Vercel **plus** typecheck og unit tests |
| `npm run lint` | `svelte-check` i `web/` |
| `npm run test` | Node unit tests (`web` audio m.fl.) |
| `npm run build` | Production build som Vercel |
| `npm run check:content:errors` | Kun katalog-fejl (hurtig) |
| `python3 production/udgivelseskalender.py` | Genopbyg [udgivelseskalender.md](redaktion/udgivelseskalender.md); fejl ved to numre samme dag pr. magasin |

**Git pre-push:** efter `npm install` i roden kører `git push` automatisk `scripts/preflight.sh`. Bypass kun bevidst: `SKIP_PREFLIGHT=1 git push`.

**GitHub Actions:** [`.github/workflows/preflight.yml`](.github/workflows/preflight.yml) kører den samme suite på `push`/`pull_request` til `main`.

## Deploy på Vercel

1. Importér repoet i Vercel.
2. Root Directory: repo-roden (se [`vercel.json`](vercel.json) — `installCommand` / `buildCommand` bruger `web/`).
3. Build command kommer fra `vercel.json` (inkl. `npm --prefix web run build`).
4. Ingen runtime-miljøvariabler — sitet er fuldt statisk.

Produktion kan pege på `nyesider.vercel.app` (eller custom domain senere).

## PDF → markdown (eksisterende numre)

```bash
python3 -m venv .venv
.venv/bin/pip install -r production/requirements.txt
.venv/bin/python production/extract_pdf.py content/<slug>/issues/<issue>/<fil>.pdf
.venv/bin/python production/reassemble_articles.py   # genbygger artikler fra _extract/
.venv/bin/python production/cleanup_articles.py      # redaktionel oprydning
```

## Markdown → PDF (nye numre)

```bash
.venv/bin/python production/build_magazine.py <slug> <issue-slug>
# fx: .venv/bin/python production/build_magazine.py gnisten 2026-07-nr1
```

Genererer print-PDF'en (`production/build_magazine.py`, ReportLab, A4) ud fra markdown-artiklerne, `issue.json` og magasinets farver i `magazine.json`. Generisk på tværs af titler. Frontmatter-feltet `flow: true` lader en artikel dele side med den foregående (til korte bagsnit-sektioner); `figures:` i frontmatter erstatter `[FIGUR N]`-markører i brødteksten med billeder.

## Hemmeligheder & omkostninger

To lag (alle gitignored — se [.env.example](.env.example)):

| Formål | Fil | Variabel |
|---|---|---|
| **OpenRouter** (tekst pr. magasin — cost tracking) | `.env.gnisten`, `.env.pulsen`, `.env.dosis`, `.env.spaending`, `.env.horisonten`, `.env.kulturboxen`, `.env.kraften`, `.env.orbit` | `OPENROUTER_API_KEY` |
| **xAI Imagine** (billeder, forlagsfælles) | `.env.local` | `XAI_API_KEY` |

- Under produktion af en titel: load **kun** den titels `.env.<slug>` til OpenRouter — aldrig en andens nøgle.
- Imagine: `.env.local` / `XAI_API_KEY`.
- Hjælper: `python production/load_env.py <slug>` (bekræfter filer uden at printe hemmeligheder).
- Forbrug pr. nummer noteres i `issue.json` (`productionCostUSD`). Webappen bruger ingen nøgler.
