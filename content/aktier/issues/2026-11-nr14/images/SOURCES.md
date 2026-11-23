# Billedkilder — Aktier med Grok nr. 14

## Forside

| Fil | Beskrivelse | Kilde |
|---|---|---|
| `aktier_cover.png` | Forside (600×800), navy baggrund, guld titel, S&P −8,6 %, NVDA −22,9 %, 0 nye kandidater, 25 aktive | Programmatisk genereret (Python/Pillow) |

## Artikelbilleder

Alle dekorative SVG-motiver er redaktionelle diagrammer skabt af chefredaktionen.
Ingen AI-genererede billeder. Ingen stockfoto, ingen logoer, ingen afbildning af reelle personer.

| Fil | Artikel | Stilart |
|---|---|---|
| `aktier_leder.svg` | Leder | 6-boks grid (S&P −8,6 %, NVDA −22,9 %, 0 nye, SGO tæt, INTU niveau, 25 aktive) |
| `aktier_markedet.svg` | Markedet | 6-boks grid (ugens indeks, VIX, SMH, Fed) |
| `aktier_tallet.svg` | Tallet | 4-boks grid (−22,9 %, fwd P/E 7,6, 7-ugers stime, følger) |
| `aktier_etf.svg` | ETF'erne | 4-boks grid (SPY korrektion, QQQ bjørnemarked, SMH −40 %, ingen anbefaling) |
| `aktier_portefoelje.svg` | Porteføljen | 6-boks grid (0 inv., SGO, FISV, uge −5,7 %, INTU, 25 aktive) |
| `aktier_rygter.svg` | Rygtebørsen / Bagsnit | 6-boks grid (NVDA, Vinci, GIS, GOOGL fjernet, COF fjernet, CPH ingen) — delt billede |

## 1-års prisgrafer (Yahoo Finance data)

Alle prisgrafer er baseret på daglige lukkekurser fra Yahoo Finance.
Periode: november 2025 – november 2026. **52-ugers top markeret.** **Exit-/prisniveauer markeret med rød stiplet linje hvor relevant.**

| Fil | Ticker | Indhold |
|---|---|---|
| `figur-nvda-pris.svg` | NVDA | 1-års priskurve, 52w top $243,37 (6. okt intradag) / $239,24 (højeste lukke), $162,85 (13. nov), rapport 17. nov $155,46, lukke $125,53 (20. nov, ny bund) |
| `figur-sgo-pris.svg` | SGO.PA | 1-års priskurve, 52w top €90,86 (13. feb lukke), vores €75,30, EXIT €70,00, lukke €71,22 (1,7 % over) |
| `figur-fisv-pris.svg` | FISV | 1-års priskurve, 52w top $69,85 (9. jan lukke), lav $44,36 (2. okt), vores $62,88, EXIT $54,50, lukke $55,88 (2,5 % over) |
| `figur-intu-pris.svg` | INTU | 1-års priskurve, 52w top $676,55 (26. dec 2025 lukke), vores $275,79, 25. jun lukkebund $255,07, NYT EXIT $255,00, lukke $270,44 (5,7 % over) |

## Markedsdiagrammer

| Fil | Artikel | Indhold |
|---|---|---|
| `figur-markedet-uge.svg` | Markedet | Søjlediagram: S&P −8,61 %, Nasdaq −10,02 %, Dow −8,02 %, Nasdaq-100 −10,43 %, STOXX 600 −5,80 %, Euro Stoxx 50 −6,97 %, DAX −7,28 %, CAC 40 −5,27 %, OMXS30 −5,42 %, OSEBX −3,51 %, OMXC25 −4,79 %, SMH −17,8 % |
| `figur-portefoelje-bar.svg` | Porteføljen | 25 aktive kandidater, % uge-ændring (vandret søjlediagram), kun RBREW i plus (+0,4 %), værste INTU −20,9 %, referencelinjer SPY −8,6 %, EUNL −5,9 % |

## Datakilder

- **Yahoo Finance:** Daglige lukkekurser, 52-ugers intervaller, nøgletal. https://finance.yahoo.com/
- Alle tal pr. **lukkekurs fredag 20. november 2026** (US fredag lukke / EU fredag lukke).
- Prisdata fra vedhæftede CSV-filer: `prices/NVDA.csv`, `prices/SGO.PA.csv`, `prices/FISV.csv`, `prices/INTU.csv`, m.fl.
- Portfolio scorecard: `portefoelje_scorecard_2026-11-20.csv`.
- Quote snapshot: `yahoo_quotes_snapshot_2026-11-20.json`.

## Nyheder og rapporter citeret

- Reuters/Yahoo wall st futures: https://finance.yahoo.com/markets/stocks/articles/wall-st-futures-slip-anthropic-104746137.html
- AP News stock markets: https://apnews.com/article/stock-markets-anthropic-ai-chips-boom-c4c3f4878b12989347f8a930ed813dad
- T. Rowe Price weekly update: https://www.troweprice.com/en/us/insights/global-markets-weekly-update
- Morningstar market wrap: https://www.morningstar.com/markets/market-wrap-stocks-lose-851-technology-basic-materials-fall
- Dow Jones/Morningstar STOXX: https://www.morningstar.com/news/dow-jones/202611206110/stoxx-europe-600-index-ends-the-week-580-lower-at-62565-data-talk
- Reuters/Yahoo European shares: https://finance.yahoo.com/markets/world-indices/articles/european-shares-head-steepest-weekly-082527441.html
- Nvidia Q3 pressemeddelelse: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Third-Quarter-Fiscal-2027/default.aspx
- Investing.com Nvidia beats: https://www.investing.com/news/earnings/nvidia-quarterly-results-beat-estimates-5033943
- CNBC Nvidia earnings: https://www.cnbc.com/2026/11/18/nvidia-stock-earnings.html
- Investing.com Nvidia SEC: https://www.investing.com/news/stock-market-news/nvidia-shares-fall-10-as-report-of-sec-accounting-probe-adds-to-pressure-5042464
- CNBC Nvidia 7-week streak: https://www.cnbc.com/2026/11/20/nvidias-7-week-losing-streak-is-longest-since-2008-financial-crisis.html
- Intuit Q1: https://investors.intuit.com/news-events/press-releases/detail/1331/intuit-reports-first-quarter-results-and-enters-agreement-to-sell-mailchimp-to-bending-spoons
- Yahoo Finance Intuit: https://finance.yahoo.com/markets/stocks/article/intuit-stock-falls-on-weaker-outlook-mailchimp-sale-to-bending-spoons-160641699.html
- Investing.com Intuit: https://www.investing.com/news/earnings/intuit-beats-firstquarter-estimates-agrees-to-sell-mailchimp-for-368-billion-5040049
- Lowe's SEC: https://www.sec.gov/Archives/edgar/data/60667/000006066726000126/exhibit991-10302026.htm
- CNBC Lowe's: https://www.cnbc.com/2026/11/18/lowes-low-q3-2026-earnings.html
- Yahoo Finance Fiserv: https://finance.yahoo.com/markets/stocks/articles/fisv-stock-slumps-most-5-032040440.html
- Insider Monkey GIS: https://www.insidermonkey.com/news/general-mills-gis-is-suddenly-drawing-wall-streets-attention-1868407/
- Seeking Alpha GIS: https://seekingalpha.com/news/4671353-general-mills-is-on-watch-after-piper-sandler-warns-of-a-potential-dividend-cut
