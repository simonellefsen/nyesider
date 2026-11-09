# Billedkilder — Aktier med Grok nr. 12

## Forside

| Fil | Beskrivelse | Kilde |
|---|---|---|
| `aktier_cover.png` | Forside (600×800), navy baggrund, guld titel, FISV +26 %, FIS −25 %, 24 aktive | Programmatisk genereret (Python/Pillow) |

## Artikelbilleder

Alle dekorative SVG-motiver er redaktionelle diagrammer skabt af chefredaktionen.
Ingen AI-genererede billeder. Ingen stockfoto, ingen logoer, ingen afbildning af reelle personer.

| Fil | Artikel | Stilart |
|---|---|---|
| `aktier_leder.svg` | Leder | 6-boks grid (FISV ind, FIS afvist, BKNG steg) |
| `aktier_markedet.svg` | Markedet | 6-boks grid (ugens indeks, midtermsdag) |
| `aktier_fisv.svg` | Fiserv feature | 6-boks grid (nøgletal + Q3 + invalidation) |
| `aktier_tallet.svg` | Tallet | 4-boks grid (−25,5 %, P/E 4,3, afvist) |
| `aktier_etf.svg` | ETF'erne | 4-boks grid (ETF-status, QQQ korrektion) |
| `aktier_portefoelje.svg` | Porteføljen | 6-boks grid (scorecard, FISV ind, 24 aktive) |
| `aktier_rygter.svg` | Rygtebørsen / Bagsnit | 6-boks grid (følgere + afviste, delt billede) |

## 1-års prisgrafer (Yahoo Finance data)

Alle prisgrafer er baseret på daglige lukkekurser fra Yahoo Finance.
Periode: november 2025 – november 2026. **52-ugers top markeret med guld cirkel.** **Invalidationsniveau markeret med rød stiplet linje.**

| Fil | Ticker | Indhold |
|---|---|---|
| `figur-fisv-pris.svg` | FISV | 1-års priskurve, 52w top $69,85 (9. jan lukke), 2. okt lav $44,36, 3. nov rapport-gap +12,5 %, invalidation $54,50, lukke $62,88 |
| `figur-fis-fisv-pris.svg` | FIS | 1-års priskurve, 52w top $67,54 (8. jan lukke), 4. nov crash −23,7 %, ny 52w lav $28,73, sammenligning med FISV |
| `figur-bkng-exit.svg` | BKNG | Kort periode (26. okt – 6. nov): exit $153,14, Q3-hop til $170,97, lukke $160,67, +4,9 % over exit |

## Markedsdiagrammer

| Fil | Artikel | Indhold |
|---|---|---|
| `figur-markedet-uge.svg` | Markedet | Søjlediagram: S&P −2,7 %, Nasdaq −3,4 %, Dow −0,9 %, SMH −11,2 %, EuroStoxx +0,6 %, DAX 0 %, CAC +2,1 %, OMXC25 +1,8 %, OMXS30 −0,1 %, OSEBX −4,3 % |
| `figur-portefoelje-bar.svg` | Porteføljen | 23 aktive kandidater, % siden publikation (vandret søjlediagram), sorteret fra WKL +36 % til YAR −10,2 % |

## Datakilder

- **Yahoo Finance:** Daglige lukkekurser, 52-ugers intervaller, nøgletal. https://finance.yahoo.com/
- Alle tal pr. **lukkekurs fredag 6. november 2026** (US fredag lukke / EU fredag lukke).
- Prisdata fra vedhæftede CSV-filer: `prices/FISV.csv`, `prices/FIS.csv`, `prices/BKNG.csv`, m.fl.
- Portfolio scorecard: `portefoelje_scorecard_2026-11-06.csv`.
- Quote snapshot: `yahoo_quotes_snapshot_2026-11-06.json`.

## Nyheder og rapporter citeret

- Fiserv Q3: https://finance.yahoo.com/markets/stocks/articles/fisv-stock-surges-earnings-beat-173900579.html
- MarketWatch Fiserv Q3: https://www.marketwatch.com/story/fiserv-shares-up-as-3q-adj-profit-rev-top-views-eb989a8c
- Investing.com Fiserv: https://www.investing.com/news/stock-market-news/why-is-fiserv-stock-surging-today-93CH-4994955
- FIS Q3: https://fisglobal.gcs-web.com/news-releases/news-release-details/fis-reports-third-quarter-2026-results/
- Motley Fool FIS: https://www.fool.com/investing/2026/11/04/why-fidelity-national-information-services-plunged-today/
- Investing.com FIS Q3: https://www.investing.com/news/transcripts/earnings-call-transcript-fis-slips-after-q3-2026-beat-and-softer-outlook-93CH-5000544
- Seeking Alpha FIS: https://seekingalpha.com/news/4664941-fis-downgraded-at-j-p-morgan-over-financial-guidance-cfo-exit-stock-sinks
- CNBC Midterms: https://www.cnbc.com/2026/11/05/stock-market-today-live-updates.html
- Reuters/StreetInsider chip rebound: https://www.streetinsider.com/General+News/Nasdaq+rebounds+as+chip+stocks+recover+from+steep+losses/27302782.html
- AP Midterms: https://apnews.com/article/markets-japan-nikkei-oil-ai-bba6f0bf9035a6e6b1c4fef3e8230b89
- Morningstar weekly: https://www.morningstar.com/markets/weekly-market-update-stocks-down-after-big-losses-energy-tech
- Novo Nordisk Q3: https://www.sec.gov/Archives/edgar/data/353278/000162828026069805/caq32026.htm
- CNBC Novo: https://www.cnbc.com/2026/11/04/novo-q3-earnings-wegovy-sales.html
- Deutsche Telekom Q3: https://www.telekom.com/en/newsroom/latest-updates/media-information/2026/11/more-growth-raised-guidance-record-dividend
- Investing.com DTE: https://www.investing.com/news/earnings/deutsche-telekom-lifts-2026-targets-in-q3-buyback-below-forecasts-5002353
- Ahold Delhaize Q3: https://newsroom.aholddelhaize.com/ahold-delhaize-reports-resilient-q3-2026-results-and-updates-2026-guidance-to-reflect-business-disruption-caused-by-recent-cybersecurity-incident/
- Philips Q3: https://www.philips.com/a-w/about/news/archive/corpcomms/news/press/2026/philips-third-quarter-results-2026.html
- AP Booking: https://apsmorningbrief.com/news/2026/11/04/booking-holdings-rises-travel-stocks-rally-softer-holiday-quarter-outlook/
