# Billedkilder — Aktier med Grok nr. 8

## Forside

| Fil | Beskrivelse | Kilde |
|---|---|---|
| `aktier_cover.png` | Forside (600×800), navy baggrund, guld titel, telekomchok + CCL-kandidat | Programmatisk genereret (Python/Pillow) |

## Artikelbilleder

Alle dekorative SVG-motiver er redaktionelle diagrammer skabt af chefredaktionen.
Ingen AI-genererede billeder. Ingen stockfoto, ingen logoer, ingen afbildning af reelle personer.

| Fil | Artikel | Stilart |
|---|---|---|
| `aktier_leder.svg` | Leder | abstrakt telekom-ned + CCL-op diagram |
| `aktier_markedet.svg` | Markedet | søjlediagram (telekomchok) |
| `aktier_ccl.svg` | Carnival (CCL) | stiliseret nøgletal + Q3-beat info |
| `aktier_tallet.svg` | Tallet | én kandidat i rækkediagram |
| `aktier_etf.svg` | ETF'erne | grid af ETF-bokse med vurdering |
| `aktier_portefoelje.svg` | Porteføljen | RI.PA exit, telekomchok, ny kandidat, scorecard |
| `aktier_rygter.svg` | Rygtebørsen / Bagsnit | telekom følgere + afvisninger (delt billede) |

## 1-års prisgrafer (Yahoo Finance data)

Alle prisgrafer er baseret på daglige lukkekurser fra Yahoo Finance.
Periode: oktober 2025 – oktober 2026. **52-ugers top markeret med guld cirkel.** **Invalidationsniveau markeret med rød stiplet linje.** **24. sep bund og Q3-rapportdag markeret.**

| Fil | Ticker | Indhold |
|---|---|---|
| `figur-ccl-pris.svg` | CCL | 1-års priskurve, 52w top $34,03 (6. feb) markeret, bund $21,79 (24. sep), invalidation $22,14 |

## Telekomchok-diagram

| Fil | Artikel | Indhold |
|---|---|---|
| `figur-markedet-telecom.svg` | Markedet | SpaceX-spektrum, TMUS/VZ/T fald, tower stocks stigning |

## Datakilder

- **Yahoo Finance:** Daglige lukkekurser, 52-ugers intervaller, nøgletal. https://finance.yahoo.com/
- Alle tal pr. **lukkekurs fredag 9. oktober 2026** (US fredag lukke / Europa fredag lukke).
- Prisdata fra vedhæftede CSV-filer: `CCL_1y_daily.csv`, `RI_PA_1y_daily.csv`, `TMUS_1y_daily.csv`, `DTE_DE_1y_daily.csv`, `SPY_1y_daily.csv`.
- Portfolio scorecard: `portefoelje_scorecard_2026-10-09.csv`.
- Quote snapshot: `yahoo_quotes_snapshot_2026-10-09.json`.
