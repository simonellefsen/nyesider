# Billedkilder — Aktier med Grok nr. 9

## Forside

| Fil | Beskrivelse | Kilde |
|---|---|---|
| `aktier_cover.png` | Forside (600×800), navy baggrund, guld titel, chip-crash + ingen nye køb | Programmatisk genereret (Python/Pillow) |

## Artikelbilleder

Alle dekorative SVG-motiver er redaktionelle diagrammer skabt af chefredaktionen.
Ingen AI-genererede billeder. Ingen stockfoto, ingen logoer, ingen afbildning af reelle personer.

| Fil | Artikel | Stilart |
|---|---|---|
| `aktier_leder.svg` | Leder | to-kolonne sammenligning (chip-crash vs. portefølje) |
| `aktier_markedet.svg` | Markedet | søjlediagram (ugens ændringer) |
| `aktier_folgelisten.svg` | Følgelisten | 6-boks grid (følgere med nøgletal) |
| `aktier_tallet.svg` | Tallet | exit-tabel (10 af 10 steget) |
| `aktier_etf.svg` | ETF'erne | 4-boks grid (US/verden, Europa, Norden, chips) |
| `aktier_portefoelje.svg` | Porteføljen | scorecard + per-issue + bedste/værste |
| `aktier_rygter.svg` | Rygtebørsen / Bagsnit | afvisnings-grid (chips, banker, EU-banker) (delt billede) |

## 1-års prisgrafer (Yahoo Finance data)

Alle prisgrafer er baseret på daglige lukkekurser fra Yahoo Finance.
Periode: oktober 2025 – oktober 2026. **52-ugers top markeret med guld cirkel.** **Invalidationsniveau markeret med rød stiplet linje hvor relevant.** **Særlige datoer markeret.**

| Fil | Ticker | Indhold |
|---|---|---|
| `figur-tmus-pris.svg` | TMUS | 1-års priskurve, 52w top $230,54 (20. okt 2025) markeret, 9. okt shock $148,58 markeret, trigger: bekræftet bund |
| `figur-ripa-pris.svg` | RI.PA | 1-års priskurve, invalidation €58,60 linje, 5. okt €58,04 (eneste under niveau), nu €68,22 (+17,5 % fra bund) |

## Markedsdiagrammer

| Fil | Artikel | Indhold |
|---|---|---|
| `figur-markedet-chip.svg` | Markedet | SMH vs SPY vs EUNL uge-ændring (søjler) |
| `figur-portefoelje-bar.svg` | Porteføljen | 22 aktive kandidater, % siden publikation (vandret søjlediagram) |

## Datakilder

- **Yahoo Finance:** Daglige lukkekurser, 52-ugers intervaller, nøgletal. https://finance.yahoo.com/
- Alle tal pr. **lukkekurs fredag 16. oktober 2026** (US fredag lukke / Europa fredag lukke).
- Prisdata fra vedhæftede CSV-filer: `TMUS_1y_daily.csv`, `RI_PA_1y_daily.csv`, `SMH_1y_daily.csv`, `SPY_1y_daily.csv`, `EUNL_DE_1y_daily.csv`.
- Portfolio scorecard: `portefoelje_scorecard_2026-10-16.csv`.
- Exits: `exits_siden_salg_2026-10-16.csv`.
- Quote snapshot: `yahoo_quotes_snapshot_2026-10-16.json`.

## Rettelser i dette nummer

Nr. 8 bragte tre forkerte kalenderdatoer:
- Booking Holdings Q3: ~27. oktober → **3. november** (kilde: Booking IR)
- PayPal Q3: 28. oktober → **27. oktober** (kilde: PayPal IR)
- Rockwool Q3: 6. november → **25. november** (kilde: Rockwool financial calendar)
