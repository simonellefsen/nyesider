# Billedkilder — Aktier med Grok nr. 11

## Forside

| Fil | Beskrivelse | Kilde |
|---|---|---|
| `aktier_cover.png` | Forside (600×800), navy baggrund, guld titel, GOOGL −12,6 %, TMUS ind, BKNG ud | Programmatisk genereret (Python/Pillow) |

## Artikelbilleder

Alle dekorative SVG-motiver er redaktionelle diagrammer skabt af chefredaktionen.
Ingen AI-genererede billeder. Ingen stockfoto, ingen logoer, ingen afbildning af reelle personer.

| Fil | Artikel | Stilart |
|---|---|---|
| `aktier_leder.svg` | Leder | 6-boks grid (TMUS ind, BKNG ud, Alphabet) |
| `aktier_markedet.svg` | Markedet | 6-boks grid (ugens indeks) |
| `aktier_tmus.svg` | T-Mobile US feature | 6-boks grid (nøgletal + Q3) |
| `aktier_tallet.svg` | Tallet | 5-boks grid (−12,6 %, P/E, FCF) |
| `aktier_etf.svg` | ETF'erne | 4-boks grid (ETF-status) |
| `aktier_portefoelje.svg` | Porteføljen | 6-boks grid (scorecard, BKNG out, TMUS in) |
| `aktier_rygter.svg` | Rygtebørsen / Bagsnit | 6-boks grid (følgere + afviste, delt billede) |

## 1-års prisgrafer (Yahoo Finance data)

Alle prisgrafer er baseret på daglige lukkekurser fra Yahoo Finance.
Periode: november 2025 – oktober 2026. **52-ugers top markeret med guld cirkel.** **Invalidationsniveau markeret med rød stiplet linje.** **Exit/lukkebund markeret med rød cirkel.**

| Fil | Ticker | Indhold |
|---|---|---|
| `figur-tmus-pris.svg` | TMUS | 1-års priskurve, 52w top $224,75 (intradag 24. feb), lukkebund $146,54 (23. okt), 28. okt intradag lav $143,75, invalidation $143,50, lukke $156,44 |
| `figur-googl-pris.svg` | GOOGL | 1-års priskurve, 52w top $408,61 (intradag), 13. maj høj lukke $402,62, 29. okt fald −12,6 % (fra $324,89 til $283,82), lukke $279,84 |
| `figur-bkng-pris.svg` | BKNG | 1-års priskurve, 52w top $219,68 (9. jan), invalidation $154,13, publikationspris $159,02, exit 26. okt $153,14, lukke $148,13 |

## Markedsdiagrammer

| Fil | Artikel | Indhold |
|---|---|---|
| `figur-markedet-uge.svg` | Markedet | Søjlediagram: S&P −0,6 %, Nasdaq −2,0 %, Dow −0,9 %, Russell +1,3 %, Euro Stoxx +1,0 %, DAX +2,5 %, CAC +2,4 %, OMXC25 +4,9 %, OMXS30 +3,0 %, OSEBX +2,1 % |
| `figur-portefoelje-bar.svg` | Porteføljen | 22 aktive kandidater, % siden publikation (vandret søjlediagram) |

## Datakilder

- **Yahoo Finance:** Daglige lukkekurser, 52-ugers intervaller, nøgletal. https://finance.yahoo.com/
- Alle tal pr. **lukkekurs fredag 30. oktober 2026** (US fredag lukke / EU fredag lukke).
- Prisdata fra vedhæftede CSV-filer: `prices/TMUS.csv`, `prices/GOOGL.csv`, `prices/BKNG.csv`, m.fl.
- Portfolio scorecard: `portefoelje_scorecard_2026-10-30.csv`.
- Quote snapshot: `yahoo_quotes_snapshot_2026-10-30.json`.

## Nyheder og rapporter citeret

- T-Mobile Q3: https://www.t-mobile.com/news/business/t-mobile-q3-2026-earnings
- Investing.com TMUS Q3: https://www.investing.com/news/earnings/tmobile-q3-profit-jumps-27-as-revenue-tops-estimates-4980669
- MarketWatch TMUS: https://www.marketwatch.com/story/t-mobile-3q-profit-revenue-rise-on-postpaid-growth-096d4d4f
- CNBC Alphabet: https://www.cnbc.com/2026/10/29/alphabet-google-microsoft-msft-shares-today-earnings.html
- NBC News Alphabet: https://www.nbcnews.com/business/markets/alphabet-google-stock-ai-advertising-rcna606322
- Reuters/StreetInsider Alphabet: https://www.streetinsider.com/Reuters/Alphabet+stock+sinks+as+search+woes+cause+revenue+miss%2C+cash+burn+worsens/27249195.html
- MarketWatch BKNG: https://www.marketwatch.com/data-news/booking-holdings-inc-stock-outperforms-competitors-despite-losses-on-the-day-a88a67f4-f61b5cbdcc1f
- T. Rowe Price Global Markets Weekly: https://www.troweprice.com/personal-investing/resources/insights/global-markets-weekly-update.html
- The Closing Print: https://www.theclosingprint.net/2026/10/post-market-and-weekly-summary-2026-10-30/
- AP News: https://apnews.com/article/wall-street-stocks-dow-nasdaq-a01d3551e794fed1a0c317c20bc3f0a2
- Morningstar: https://www.morningstar.com/markets/weekly-market-update-stocks-flat-healthcare-rises-communication-services-fall
- Nasdaq Dorsey Wright: https://dorseywright.nasdaq.com/research/weekly-review/2026/10/30/10-30-2026/weekly-review-10-30-2026
- UPS Q3: https://www.cnbc.com/2026/10/27/ups-ups-q3-2026-earnings.html
- PayPal Q3: https://www.investing.com/news/earnings/paypal-lifts-fullyear-profit-guidance-q3-revenue-falls-short-4975030
- Sanofi Q3: https://www.sanofi.com/en/media-room/press-releases/2026/2026-10-30-06-30-00-3392028
