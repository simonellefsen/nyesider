# ORBIT – Redaktionsnotesbog

Opdateret efter nr. 2 (august 2026, *"Kataloget og kikkerten"*).  
OpenRouter: **kun** `.env.orbit`. Imagine: `.env.local` / `XAI_API_KEY`.

## Identitet

Rumfart som industri og geopolitik: opsendelser, agenturer, sats, skrot, kalender, statistik, how-it-works.  
vs **KRAFTEN:** de tager rum-*kraft* (watt); vi tager mission/ops/katalog. Overlap OK.

## Forside (skifter hvert nummer)

1. Sæt `issueTheme` (nr. 2: **Kataloget og kikkerten**).  
2. Generér ny `images/orbit_cover.png` (3:4, Imagine) der fanger temaet.  
3. `issue.json`: `cover`, `coverCredit`, `coverSource`.  
4. Brand: navy `#0B1020`, blå `#5B8DEF`, guld `#E8B86D`. Ingen masthead-tekst i billedet.

## Nr. 2 — udgivet

**Tema:** Kataloget og kikkerten  
10 artikler: leder, tallet (nærpassager), Starship vs Falcon, New Glenn RTF, SSA, Kuiper/konstellationer, ESA launcher, nærpassage uden panik, kalender, rygtebørs. (Ordbogen fjernet 2026-08-08.)  
Cover + 4 feature-billeder (Imagine).  
`bestilling.json`: `redaktion/orbit/numre/2026-08-nr2/bestilling.json`.  
Kryds: [KRAFTEN nr. 2](../../content/kraften/issues/2026-08-nr2/) (watt i rummet).

## Nr. 1 — udgivet

13 artikler: leder, tallet (324), SpaceX, Blue Origin, NASA/ESA, Indien/Rusland, Kina, satellitter, skrot, LEO/MEO/GEO-diagram, kalender, ordbog, rygtebørs.  
Cover + 5 Imagine-features + SVG-diagram.

## Nr. 3 — kandidater

- **(2026-08) Starship flight-by-flight / post-13** — genbrug, næste V3, om V3 går i Falcon-manifest  
- **(2026-08) Starbase** — site, pads, FAA, Texas-politik (ikke kun livestream)  
- **(2026-08) Launch pads & raketter verden rundt** — sammenlign klasse, alder, kadence, genbrug (Falcon, Long March, Ariane, Soyuz, Electron, New Glenn, …)  
- **(2026-08) Starmind** — research lead (afklar hvad læser/redaktion mener; produkt/projekt/firma)  
- **(2026-08) Kommerciel SSA-marked**  
- **(2026-08) Kinesiske LEO-konstellationer — opsendte vs. plan**  
- **(2026-08) Ariane 6 flight rate**  
- **(2026-08) Liability i praksis** — forsikring, forlig, nationale love oven på 1972-konventionen  

## Format

- **Artikeltal:** typisk 10–14. Faste: Leder · Tallet · opsendelser · agenturer · konstellationer · SSA/skrot · kalender · rygtebørs. **Ingen Ordbog** — gloser i parentes/fodnote.
- **Standard `mustCite`:** 2+ for Tallet og agentur-features med launch-tal; 0 for rygtebørs.

## Research-regler

Ingen opdigtede launch-datoer. Skeln planlagt/scrub/success/failure. Primære kilder.  
`python production/load_env.py orbit` før produktion.

## Log

- **2026-08-08 (depth):** Nr. 2 — nærpassage/Tallet udvidet (kollisioner, CDM, Liability Convention); Starship flight 13 (V3, Starlink V3-test, Indiske Ocean); SSA/leder/kalender synket.


- **2026-08-08 (format):** Ordbogen fjernet fra nr. 2 — LEO/SSA/HLS/FAA/FCC/Georeturn m.fl. i brødtekst/fodnote.


- **2026-08-08:** Nr. 2 publiceret — SSA, konstellationer, Starship/Falcon, New Glenn, ESA launcher.
- **2026-08-01:** Notesbog udvidet med `## Format`; leads datostemplet.

- **2026-08-08 (edit):** ORBIT nr. 2 — LEO, NASA HLS, FAA, FCC, ESA, CNSA, SSA udfoldet **pr. artikel** (læser lander ofte på én URL); ordbog udvidet. Husregel: chefredaktør ejer first-mention; fodnote OK hvis layout knækker.

