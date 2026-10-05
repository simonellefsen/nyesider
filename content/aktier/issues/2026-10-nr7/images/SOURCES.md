# Billedkilder — Aktier med Grok nr. 7

## Forside

| Fil | Beskrivelse | Kilde |
|---|---|---|
| `aktier_cover.png` | Forside (600×800), navy baggrund, guld titel, tre dip-pile (ACN, BKNG, RBREW) | Programmatisk genereret (Python/Pillow) |

## Artikelbilleder

Alle dekorative SVG-motiver er redaktionelle diagrammer skabt af chefredaktionen.
Ingen AI-genererede billeder. Ingen stockfoto, ingen logoer, ingen afbildning af reelle personer.

| Fil | Artikel | Stilart |
|---|---|---|
| `aktier_leder.svg` | Leder | abstrakt ni-ud-tre-ind diagram |
| `aktier_markedet.svg` | Markedet | søjlediagram (indeks vs. enkeltnavn) |
| `aktier_accenture.svg` | Accenture | stiliseret nøgletal + Q4-beat info |
| `aktier_booking.svg` | Booking | stiliseret nøgletal + fald-info |
| `aktier_unibrew.svg` | Royal Unibrew | stiliseret nøgletal + PepsiCo-info |
| `aktier_tallet.svg` | Tallet | tre kandidater i rækkediagram |
| `aktier_etf.svg` | ETF'erne | grid af ETF-bokse med vurdering |
| `aktier_portefoelje.svg` | Porteføljen | invaliderede vs. nye kandidater |
| `aktier_rygter.svg` | Rygtebørsen / Bagsnit | afvisnings-kryds + kriterier (delt billede) |

## 1-års prisgrafer (Yahoo Finance data)

Alle prisgrafer er baseret på daglige lukkekurser fra Yahoo Finance.
Periode: oktober 2025 – oktober 2026. **52-ugers top markeret med guld cirkel.** **Invalidationsniveau markeret med rød stiplet linje.**

| Fil | Ticker | Indhold |
|---|---|---|
| `figur-acn-pris.svg` | ACN | 1-års priskurve, 52w top $291,09 markeret, invalidation $174,47 |
| `figur-bkng-pris.svg` | BKNG | 1-års priskurve (split-justeret), 52w top $224,99 markeret, invalidation $154,13 |
| `figur-rbrew-pris.svg` | RBREW.CO | 1-års priskurve, 52w top DKK 653,50 markeret, invalidation DKK 394,60 |

## Sammenligningsdiagrammer

| Fil | Artikel | Indhold |
|---|---|---|
| `figur-tallet-sammenligning.svg` | Tallet | Tre kandidater: P/E vs. drawdown scatter |
| `figur-markedet-sammenligning.svg` | Markedet | Performance siden nr. 1: vores kandidater vs. indeks |

## Datakilder

- **Yahoo Finance:** Daglige lukkekurser, 52-ugers intervaller, nøgletal. https://finance.yahoo.com/
- Alle tal pr. **lukkekurs fredag 2. oktober 2026** (US fredag lukke / Europa fredag lukke).
- Prisdata fra vedhæftede CSV-filer: `ACN_1y_daily.csv`, `BKNG_1y_daily.csv`, `RBREW_CO_1y_daily.csv`.
