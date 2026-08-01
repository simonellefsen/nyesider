# Nye Sider

Dansk magasinforlag, hvor hvert nummer produceres af en chefredaktør-agent med et hold af AI-skribenter via OpenRouter. Udgivelserne findes som PDF og som weblæseoplevelse bygget med SvelteKit på Vercel — se [PLAN.md](PLAN.md) og [PLAN-HTML-EDITIONS.md](PLAN-HTML-EDITIONS.md).

## Titler

| Magasin | Om | Seneste nummer |
|---|---|---|
| **GNISTEN** | AI for begyndere: modeller, priser, opsætning, prompts | Nr. 2 · August 2026 · *"Ud af browseren"* |
| **PULSEN** | Sundhedssektoren, AI i klinikken, ergoterapi | Nr. 2 · August 2026 · *"Når tasterne bliver stille"* |
| **SPÆNDING** | Elbiler og teknologien bag, europæisk fokus | Nr. 2 · August 2026 · *"Når watt bliver hverdag"* |
| **HORISONTEN** | Rejser i Europa — vandring, cykling, løb | Nr. 2 · August 2026 · *"Dolomitterne i efteråret"* |
| **KRAFTEN** | Elektrificering globalt + rumkraft (net, el, space) | Nr. 1 · August 2026 · *"Hvad holder lyset tændt"* |
| **ORBIT** | Rumfart: opsendelser, satellitter, agencer, skrot, kalender | Nr. 1 · August 2026 · *"Cadence"* |

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

## Deploy på Vercel

1. Importér repoet i Vercel.
2. Sæt **Root Directory** til `web/`.
3. Build command: `npm run build` (default).
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
| **OpenRouter** (tekst pr. magasin — cost tracking) | `.env.gnisten`, `.env.pulsen`, `.env.spaending`, `.env.horisonten`, `.env.kraften`, `.env.orbit` | `OPENROUTER_API_KEY` |
| **xAI Imagine** (billeder, forlagsfælles) | `.env.local` | `XAI_API_KEY` |

- Under produktion af en titel: load **kun** den titels `.env.<slug>` til OpenRouter — aldrig en andens nøgle.
- Imagine: `.env.local` / `XAI_API_KEY`.
- Hjælper: `python production/load_env.py <slug>` (bekræfter filer uden at printe hemmeligheder).
- Forbrug pr. nummer noteres i `issue.json` (`productionCostUSD`). Webappen bruger ingen nøgler.
