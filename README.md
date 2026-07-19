# Nye Sider

Dansk magasinforlag, hvor hvert nummer produceres af en chefredaktør-agent med et hold af AI-skribenter via OpenRouter. Udgivelserne findes som PDF og som weblæseoplevelse bygget med SvelteKit på Vercel — se [PLAN.md](PLAN.md) og [PLAN-HTML-EDITIONS.md](PLAN-HTML-EDITIONS.md).

## Titler

| Magasin | Om | Seneste nummer |
|---|---|---|
| **PULSEN** | Sundhedssektoren, AI i klinikken, ergoterapi | Nr. 2 · Juli 2026 · *"Når maskinen lytter med"* |
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

## Hemmeligheder & omkostninger

Hver titel har sin egen OpenRouter-nøgle i `.env.<slug>` (fx `.env.pulsen`, `.env.spaending` — alle gitignoret), så produktionsomkostningerne kan aflæses pr. magasin. Skabelon: [.env.example](.env.example). Forbruget pr. nummer noteres i `issue.json` (`productionCostUSD`). Webappen bruger ingen nøgler.
