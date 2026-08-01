# ORBIT – Redaktionsnotesbog

Opdateret efter nr. 1 (august 2026, *"Kadence"*).  
OpenRouter: **kun** `.env.orbit`. Imagine: `.env.local` / `XAI_API_KEY`.

## Identitet

Rumfart som industri og geopolitik: opsendelser, agenturer, sats, skrot, kalender, statistik, how-it-works.  
vs **KRAFTEN:** de tager rum-*kraft* (watt); vi tager mission/ops/katalog. Overlap OK.

## Forside (skifter hvert nummer)

1. Sæt `issueTheme` (nr. 1: **Kadence**).  
2. Generér ny `images/orbit_cover.png` (3:4, Imagine) der fanger temaet.  
3. `issue.json`: `cover`, `coverCredit`, `coverSource`.  
4. Brand: navy `#0B1020`, blå `#5B8DEF`, guld `#E8B86D`. Ingen masthead-tekst i billedet.

## Nr. 1 — udgivet

13 artikler: leder, tallet (324), SpaceX, Blue Origin, NASA/ESA, Indien/Rusland, Kina, satellitter, skrot, LEO/MEO/GEO-diagram, kalender, ordbog, rygtebørs.  
Cover + 5 Imagine-features + SVG-diagram.

## Nr. 2 — kandidater

- **(2026-08) Starship vs. Falcon manifests i praksis**  
- **(2026-08) New Glenn return-to-flight opfølgning**  
- **(2026-08) Kuiper / kinesiske konstellationer**  
- **(2026-08) Rumsituationsoverblik (SSA) og nærpassage-statistik**
- **(2026-08) ESA launcher-politik**

## Format

- **Artikeltal:** typisk 12–14. Faste: Leder · Tallet · agentur-features (SpaceX/Blue Origin/NASA-ESA/Indien-Rusland/Kina) · satellitter · skrot · LEO/MEO/GEO-diagram · kalender · ordbog · rygtebørs.
- **Standard `mustCite`:** 2+ for Tallet og agentur-features med launch-tal/masse/dato; 0 for rygtebørs.

## Research-regler

Ingen opdigtede launch-datoer. Skeln planlagt/scrub/success/failure. Primære kilder.  
`python production/load_env.py orbit` før produktion.

## Tendensdiagrammer

Kanonisk data i `content/orbit/issues/<issue>/charts/*.json` — se [content/CHARTS.md](../../content/CHARTS.md).  
Nr. 1: `global-launches`, `active-sats`.

## Log

- **2026-08-01:** Notesbog udvidet med `## Format`; leads datostemplet (se [redaktion/README](../README.md)).
- **2026-08-01 rettelse:** `10-saadan-virker-baner.md` (chefredaktør-skrevet) angav LEO 160-2.000 km og GEO 35.786 km korrekt, men uden kilde — tilføjede ESA/NASA-kilder. Ingen faktafejl fundet, kun manglende kildehenvisning.
