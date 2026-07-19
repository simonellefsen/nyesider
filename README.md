# Nye Sider

Dansk magasinforlag, hvor hvert nummer produceres af en chefredaktør-agent med et hold af AI-skribenter via OpenRouter. Udgivelserne findes som PDF og som weblæseoplevelse bygget med SvelteKit på Vercel — se [PLAN.md](PLAN.md) og [PLAN-HTML-EDITIONS.md](PLAN-HTML-EDITIONS.md).

## Titler

| Magasin | Om | Seneste nummer |
|---|---|---|
| **GNISTEN** | AI for begyndere: modeller, priser, opsætning, prompts | Nr. 1 · Juli 2026 · *"Sig hej til Claude"* |
| **PULSEN** | Sundhedssektoren, AI i klinikken, ergoterapi | Nr. 1 · Juli 2026 · *"Når maskinen lytter med"* |
| **SPÆNDING** | Elbiler og teknologien bag, europæisk fokus | Nr. 1 · Juli 2026 |

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

Hver titel har sin egen OpenRouter-nøgle i `.env.<slug>` (fx `.env.pulsen`, `.env.spaending` — alle gitignoret), så produktionsomkostningerne kan aflæses pr. magasin. Skabelon: [.env.example](.env.example). Forbruget pr. nummer noteres i `issue.json` (`productionCostUSD`). Webappen bruger ingen nøgler.
