# Billedkilder — Aktier med Grok nr. 10

## Forside

| Fil | Beskrivelse | Kilde |
|---|---|---|
| `aktier_cover.png` | Forside (600×800), navy baggrund, guld titel, Volvo Car −25 % + Balder til halv NAV | Programmatisk genereret (Python/Pillow) |

## Artikelbilleder

Alle dekorative SVG-motiver er redaktionelle diagrammer skabt af chefredaktionen.
Ingen AI-genererede billeder. Ingen stockfoto, ingen logoer, ingen afbildning af reelle personer.

| Fil | Artikel | Stilart |
|---|---|---|
| `aktier_leder.svg` | Leder | to-kolonne sammenligning (Volvo Car kollaps vs. Balder NAV) |
| `aktier_markedet.svg` | Markedet | 6-boks grid (ugens nøgletal) |
| `aktier_balder.svg` | Balder feature | 6-boks grid (nøgletal + Q3) |
| `aktier_tallet.svg` | Tallet | stort tal (−24,6 %) + exit-sammenligning |
| `aktier_etf.svg` | ETF'erne | multi-boks grid (ETF-status) |
| `aktier_portefoelje.svg` | Porteføljen | scorecard + bedste/værste + BKNG binært |
| `aktier_rygter.svg` | Rygtebørsen / Bagsnit | følger-boks + afvisninger (delt billede) |

## 1-års prisgrafer (Yahoo Finance data)

Alle prisgrafer er baseret på daglige lukkekurser fra Yahoo Finance.
Periode: oktober 2025 – oktober 2026. **52-ugers top markeret med guld cirkel.** **Invalidationsniveau markeret med rød stiplet linje.** **Lukkebund markeret hvor relevant.**

| Fil | Ticker | Indhold |
|---|---|---|
| `figur-balder-pris.svg` | BALD-B.ST | 1-års priskurve, 52w top SEK 74,10 (24. okt 2025), lukkebund SEK 43,51 (12. okt 2026), invalidation SEK 43,50, lukke SEK 49,02 |
| `figur-volcar-pris.svg` | VOLCAR-B.ST | 1-års priskurve, 52w top SEK 35,75 (11. nov 2025), invalidation SEK 18,00, publikationspris SEK 18,86, lukke SEK 10,70 |

## Markedsdiagrammer

| Fil | Artikel | Indhold |
|---|---|---|
| `figur-markedet-uge.svg` | Markedet | Søjlediagram: S&P −0,5 %, Nasdaq −0,7 %, Dow +0,4 %, Euro Stoxx −2,2 %, OMXS30 −3,7 %, AT&T −10,7 %, TMUS −7,9 %, Energi +2,5 % |
| `figur-portefoelje-bar.svg` | Porteføljen | 22 aktive kandidater, % siden publikation (vandret søjlediagram) |

## Datakilder

- **Yahoo Finance:** Daglige lukkekurser, 52-ugers intervaller, nøgletal. https://finance.yahoo.com/
- Alle tal pr. **lukkekurs fredag 23. oktober 2026** (US fredag lukke / EU fredag lukke).
- Prisdata fra vedhæftede CSV-filer: `BALD-B_ST_1y_daily.csv`, `VOLCAR-B_ST_1y_daily.csv`, `SPY_1y_daily.csv`, `EUNL_DE_1y_daily.csv`.
- Portfolio scorecard: `portefoelje_scorecard_2026-10-23.csv`.
- Quote snapshot: `yahoo_quotes_snapshot_2026-10-23.json`.

## Nyheder og rapporter citeret

- Balder Q3: https://www.balder.se/om-balder/press/rapporter/10232026-0800/fastighets-ab-balders--publ--del-rsrapport-januari-september-2026
- Volvo Cars Q3: https://www.volvocars.com/se/media/press-releases/D8DC833A7EBDC85A/
- Comcast Q3: https://cmcsa.gcs-web.com/news-releases/news-release-details/comcast-reports-3rd-quarter-2026-results
- Yara Q3: https://www.yara.com/corporate-releases/yara-reports-solid-3q-amid-market-volatility/
- AT&T Q3: https://about.att.com/story/2026/3q-earnings.html
- Reuters/WSJ/Motley Fool: Se fodnoter i artikler.
