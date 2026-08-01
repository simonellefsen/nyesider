# ORBIT – Redaktionsnotesbog

Opdateret efter nr. 1 (august 2026, *"Cadence"*).  
OpenRouter: **kun** `.env.orbit`. Imagine: `.env.local` / `XAI_API_KEY`.

## Identitet

Rumfart som industri og geopolitik: opsendelser, agencer, sats, skrot, kalender, statistik, how-it-works.  
vs **KRAFTEN:** de tager rum-*kraft* (watt); vi tager mission/ops/katalog. Overlap OK.

## Forside (skifter hvert nummer)

1. Sæt `issueTheme` (nr. 1: **Cadence**).  
2. Generér ny `images/orbit_cover.png` (3:4, Imagine) der fanger temaet.  
3. `issue.json`: `cover`, `coverCredit`, `coverSource`.  
4. Brand: navy `#0B1020`, blå `#5B8DEF`, guld `#E8B86D`. Ingen masthead-tekst i billedet.

## Nr. 1 — udgivet

13 artikler: leder, tallet (324), SpaceX, Blue Origin, NASA/ESA, Indien/Rusland, Kina, satellitter, skrot, LEO/MEO/GEO-diagram, kalender, ordbog, rygtebørs.  
Cover + 5 Imagine-features + SVG-diagram.

## Nr. 2 — kandidater

- Starship vs. Falcon manifests i praksis  
- New Glenn return-to-flight opfølgning  
- Kuiper / kinesiske konstellationer  
- SSA og conjunction-statistik  
- ESA launcher-politik  

## Research-regler

Ingen opdigtede launch-datoer. Skeln planlagt/scrub/success/failure. Primære kilder.  
`python production/load_env.py orbit` før produktion.

## Tendensdiagrammer

Kanonisk data i `content/orbit/issues/<issue>/charts/*.json` — se [content/CHARTS.md](../../content/CHARTS.md).  
Nr. 1: `global-launches`, `active-sats`.
