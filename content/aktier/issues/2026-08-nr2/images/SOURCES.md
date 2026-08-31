# Billedkilder — Aktier med Grok nr. 2

## Forside

| Fil | Beskrivelse | Kilde |
|---|---|---|
| `aktier_cover.png` | Forside (3:4), navy baggrund, guld titel, faldende priskurve | Programmatisk genereret (Python/Pillow) |

## Artikelbilleder

Alle dekorative SVG-motiver er redaktionelle diagrammer skabt af chefredaktionen.
Ingen AI-genererede billeder. Ingen stockfoto, ingen logoer, ingen afbildning af reelle personer.

| Fil | Artikel | Stilart |
|---|---|---|
| `aktier_leder.svg` | Leder | abstrakt kompas med fire dip-markører |
| `aktier_markedet.svg` | Markedet | søjlediagram (indekser ved toppen) |
| `aktier_paypal.svg` | PayPal | priskurve med 12,7 % fald + 3× volumen |
| `aktier_yara.svg` | Yara | P/E-ring med yield-bue |
| `aktier_husqvarna.svg` | Husqvarna | P/B-sammenligning (bog vs. pris) |
| `aktier_ahold.svg` | Ahold Delhaize | 52-ugers range med bund-markør |
| `aktier_tallet.svg` | Tallet | horisontalt søjlediagram (% fra top) |
| `aktier_etf.svg` | ETF'erne | grid af ETF-bokse |
| `aktier_portefoelje.svg` | Porteføljen | fem cirkler (LULU markeret binær) |
| `aktier_rygter.svg` | Rygtebørsen / Bagsnit | tre afvisnings-kryds + FISV spørgsmålstegn (delt billede) |

## 1-års prisgrafer (Yahoo Finance data)

Alle prisgrafer er genereret fra daglige lukkekurser hentet fra Yahoo Finance.
Periode: 28. august 2025 – 28. august 2026.

| Fil | Ticker | Indhold |
|---|---|---|
| `figur-pypl-pris.svg` | PYPL | 1-års priskurve, 52-ugers top/bund markeret |
| `figur-yar-pris.svg` | YAR.OL | 1-års priskurve, 52-ugers top/bund markeret |
| `figur-husq-pris.svg` | HUSQ-B.ST | 1-års priskurve, 52-ugers top/bund markeret |
| `figur-ad-pris.svg` | AD.AS | 1-års priskurve, 52-ugers top/bund markeret |

## Sammenligningsdiagrammer

| Fil | Artikel | Indhold |
|---|---|---|
| `figur-tallet-sammenligning.svg` | Tallet | Fire kandidater: nøgletal-sammenligning |
| `figur-markedet-sammenligning.svg` | Markedet | Indeks ved toppen vs. kandidater solgt fra |

## Datakilder

- **Yahoo Finance:** Daglige lukkekurser, 52-ugers intervaller, nøgletal. https://finance.yahoo.com/
- Alle tal pr. 28. august 2026 lukke.
- Prisdata gemt i `data/yahoo_prices.json`.
