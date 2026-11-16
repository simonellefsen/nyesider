# Billedkilder — Aktier med Grok nr. 13

## Forside

| Fil | Beskrivelse | Kilde |
|---|---|---|
| `aktier_cover.png` | Forside (600×800), navy baggrund, guld titel, SGO.PA €75,30, NVDA −12,7 %, 25 aktive | Programmatisk genereret (Python/Pillow) |

## Artikelbilleder

Alle dekorative SVG-motiver er redaktionelle diagrammer skabt af chefredaktionen.
Ingen AI-genererede billeder. Ingen stockfoto, ingen logoer, ingen afbildning af reelle personer.

| Fil | Artikel | Stilart |
|---|---|---|
| `aktier_leder.svg` | Leder | 6-boks grid (SGO ind, NVDA følger, RBREW bestod) |
| `aktier_markedet.svg` | Markedet | 6-boks grid (ugens indeks, STOXX rekord) |
| `aktier_sgo.svg` | Saint-Gobain feature | 6-boks grid (nøgletal + invalidation) |
| `aktier_tallet.svg` | Tallet | 4-boks grid (−12,7 %, CEO væk, fwd P/E 10) |
| `aktier_etf.svg` | ETF'erne | 4-boks grid (ETF-status, QQQ korrektion) |
| `aktier_portefoelje.svg` | Porteføljen | 6-boks grid (scorecard, SGO ind, 25 aktive) |
| `aktier_rygter.svg` | Rygtebørsen / Bagsnit | 6-boks grid (følgere + afviste, delt billede) |

## 1-års prisgrafer (Yahoo Finance data)

Alle prisgrafer er baseret på daglige lukkekurser fra Yahoo Finance.
Periode: november 2025 – november 2026. **52-ugers top markeret.** **Invalidationsniveau markeret med rød stiplet linje hvor relevant.**

| Fil | Ticker | Indhold |
|---|---|---|
| `figur-sgo-pris.svg` | SGO.PA | 1-års priskurve, 52w top €90,86 (13. feb lukke), 7. okt lav €64,76, breakout €70,40 (2. nov), invalidation €70,00, lukke €75,30 |
| `figur-nvda-pris.svg` | NVDA | 1-års priskurve, 52w top $239,24 (6. okt lukke, intradag $243,37), 12. nov intradag lav $148,80, lukke $162,85 (ny lukkebund) |
| `figur-rbrew-pris.svg` | RBREW.CO | 1-års priskurve, 52w top DKK 650,50 (23. feb lukke, intradag DKK 653,50 24. feb), vores niveau DKK 394,60, vores pris DKK 405,40, Q3-dag lukke DKK 449,00 (11. nov), lukke DKK 479,00 |

## Markedsdiagrammer

| Fil | Artikel | Indhold |
|---|---|---|
| `figur-markedet-uge.svg` | Markedet | Søjlediagram: S&P +2,51 %, Nasdaq +2,27 %, Dow +2,07 %, STOXX 600 +2,44 %, DAX +3,60 %, CAC 40 +2,82 %, OMXS30 +2,72 %, OSEBX +2,84 %, OMXC25 +0,40 % |
| `figur-portefoelje-bar.svg` | Porteføljen | 24 aktive kandidater, % siden publikation (vandret søjlediagram), sorteret fra WKL +37,1 % til YAR −9,0 % |

## Datakilder

- **Yahoo Finance:** Daglige lukkekurser, 52-ugers intervaller, nøgletal. https://finance.yahoo.com/
- Alle tal pr. **lukkekurs fredag 13. november 2026** (US fredag lukke / EU fredag lukke).
- Prisdata fra vedhæftede CSV-filer: `prices/SGO.PA.csv`, `prices/NVDA.csv`, `prices/RBREW.CO.csv`, m.fl.
- Portfolio scorecard: `portefoelje_scorecard_2026-11-13.csv`.
- Quote snapshot: `yahoo_quotes_snapshot_2026-11-13.json`.

## Nyheder og rapporter citeret

- AP News rally: https://apnews.com/article/stocks-markets-ai-us-oil-f8edd0eeb1494d4d2584715686c5e619
- Morningstar weekly: https://www.morningstar.com/markets/market-wrap-stocks-up-252-led-by-energy-industrials
- Dow Jones/Morningstar STOXX rekord: https://www.morningstar.com/news/dow-jones/202611138667/stoxx-europe-600-index-ends-the-week-244-higher-at-66414-data-talk
- Stellantis laggard: https://www.ideal-investisseur.fr/en/stock-news/stellantis-shares-the-cac-40-s-laggard-shed-12-6-in-one-week/29242.html
- CNBC CPI: https://www.cnbc.com/2026/11/10/cpi-inflation-report-october-2026.html
- BLS CPI: https://www.bls.gov/news.release/archives/cpi_11102026.htm
- Saint-Gobain Q3: https://www.investing.com/news/earnings/saintgobain-confirms-margin-outlook-as-q3-sales-rise-25-likeforlike-4976524
- Saint-Gobain pressemeddelelse: https://www.saint-gobain.com/sites/saint-gobain.com/files/media/document/CP_CA_T3_2026_VA.pdf
- Nvidia CEO Reuters/Investing.com: https://www.investing.com/news/stock-market-news/nvidia-ceo-jensen-huang-to-step-down-in-big-blow-to-ai-boom-5021980
- WSJ Nvidia: https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-11-12-2026
- NBC News Nvidia: https://www.nbcnews.com/business/markets/nvidia-stock-huang-resigns-rcna608958
- NYT Nvidia: https://www.nytimes.com/2026/11/12/business/nvidia-stock-price-jensen-huang-ceo-affair.html
- CNBC Nvidia: https://www.cnbc.com/2026/11/12/stock-market-today-live-updates.html
- Royal Unibrew Q3: https://cms.unibrew.com/media/tsjjnk4l/q3-2026-trading-statement.pdf
- Royal Unibrew Investing.com: https://www.investing.com/news/earnings/royal-unibrew-jumps-as-q3-profit-rises-margin-widens-despite-cost-inflation-5020646
