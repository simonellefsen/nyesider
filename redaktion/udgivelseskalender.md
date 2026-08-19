# Udgivelseskalender

Automatisk ledger over `published`-datoer i `content/*/issues/*/issue.json`.
Genopbyg: `python3 production/udgivelseskalender.py`.

## Regel

**Højst ét `status: published`-nummer pr. magasin pr. kalenderdag** (`YYYY-MM-DD`). Flere titler *må* udkomme samme dag (uge-batch), men DOSIS nr. 2 og nr. 3 må ikke dele `2026-08-08`.

Håndhæves som **ERROR** i `production/check_issue.py` (og dermed i `npm run preflight` / Vercel-build).

## Før du sætter `published`

1. Kør denne fil — er dagen allerede taget for titlen?
2. Eller: `python3 production/check_issue.py <slug> <issue-slug>`.
3. Ny dag: typisk næste planlagte udgivelsesvindue (fx +7 dage), ikke “i dag igen” under batch-pres.

## Efter kalenderdag (published)

| Dato | Udgivelser |
|---|---|
| 2026-07-19 | gnisten/2026-07-nr1 (nr. 1); pulsen/2026-07-nr1 (nr. 1); spaending/2026-07-nr1 (nr. 1) |
| 2026-07-20 | horisonten/2026-07-nr1 (nr. 1) |
| 2026-08-01 | dosis/2026-08-nr1 (nr. 1); gnisten/2026-08-nr2 (nr. 2); horisonten/2026-08-nr2 (nr. 2); humanerd/2026-08-nr1 (nr. 1); indeni/2026-08-nr1 (nr. 1); kraften/2026-08-nr1 (nr. 1); kulturboxen/2026-08-nr1 (nr. 1); orbit/2026-08-nr1 (nr. 1); pulsen/2026-08-nr2 (nr. 2); spaending/2026-08-nr2 (nr. 2) |
| 2026-08-08 | dosis/2026-08-nr2 (nr. 2); gnisten/2026-08-nr3 (nr. 3); horisonten/2026-08-nr3 (nr. 3); humanerd/2026-08-nr2 (nr. 2); indeni/2026-08-nr2 (nr. 2); kraften/2026-08-nr2 (nr. 2); kronike/2026-08-nr1 (nr. 1); kulturboxen/2026-08-nr2 (nr. 2); orbit/2026-08-nr2 (nr. 2); pulsen/2026-08-nr3 (nr. 3); spaending/2026-08-nr3 (nr. 3) |
| 2026-08-15 | dosis/2026-08-nr3 (nr. 3); indeni/2026-08-nr3 (nr. 3); kraften/2026-08-nr3 (nr. 3); kulturboxen/2026-08-nr3 (nr. 3); orbit/2026-08-nr3 (nr. 3) |
| 2026-08-19 | humanerd/2026-08-nr3 (nr. 3); kronike/2026-08-nr2 (nr. 2) |

## Efter magasin

### dosis

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-08-nr1` | 2026-08-01 | published | Protein-æraen |
| 2 | `2026-08-nr2` | 2026-08-08 | published | Appetitten under kontrol |
| 3 | `2026-08-nr3` | 2026-08-15 | published | Søvnen, der ikke kan stikkes |

### gnisten

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-07-nr1` | 2026-07-19 | published | Sig hej til Claude |
| 2 | `2026-08-nr2` | 2026-08-01 | published | Ud af browseren |
| 3 | `2026-08-nr3` | 2026-08-08 | published | Agenten og den lokale hjerne |

### horisonten

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-07-nr1` | 2026-07-20 | published | Mallorca uden for højsæsonen |
| 2 | `2026-08-nr2` | 2026-08-01 | published | Georgien — bjerge, by og bord |
| 3 | `2026-08-nr3` | 2026-08-08 | published | Dolomitterne i efteråret |

### humanerd

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-08-nr1` | 2026-08-01 | published | Robotter på arbejde |
| 2 | `2026-08-nr2` | 2026-08-08 | published | Lagerets koreografi |
| 3 | `2026-08-nr3` | 2026-08-19 | published | Tre humanoider, tre beviser |

### indeni

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-08-nr1` | 2026-08-01 | published | Dåsen |
| 2 | `2026-08-nr2` | 2026-08-08 | published | Filteret |
| 3 | `2026-08-nr3` | 2026-08-15 | published | Fjernvarmen — rørene under fortovet |

### kraften

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-08-nr1` | 2026-08-01 | published | Hvad holder lyset tændt |
| 2 | `2026-08-nr2` | 2026-08-08 | published | Strøm overalt |
| 3 | `2026-08-nr3` | 2026-08-15 | published | Hvem får strømmen først? |

### kronike

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-08-nr1` | 2026-08-08 | published | Riget formes |
| 2 | `2026-08-nr2` | 2026-08-19 | published | Kvinders valgret — fire aartier, fem aarstal |

### kulturboxen

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-08-nr1` | 2026-08-01 | published | Supra og tillid |
| 2 | `2026-08-nr2` | 2026-08-08 | published | Tre sprog, ét plateau |
| 3 | `2026-08-nr3` | 2026-08-15 | published | Landet der arbejder ude |

### orbit

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-08-nr1` | 2026-08-01 | published | Kadence |
| 2 | `2026-08-nr2` | 2026-08-08 | published | Kataloget og kikkerten |
| 3 | `2026-08-nr3` | 2026-08-15 | published | To hastigheder i kredsløb |

### pulsen

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-07-nr1` | 2026-07-19 | published | Når maskinen lytter med |
| 2 | `2026-08-nr2` | 2026-08-01 | published | Når tasterne bliver stille |
| 3 | `2026-08-nr3` | 2026-08-08 | published | Når driften taler |

### spaending

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-07-nr1` | 2026-07-19 | published | SPÆNDING nr. 1 · Juli 2026 |
| 2 | `2026-08-nr2` | 2026-08-01 | published | Når watt bliver hverdag |
| 3 | `2026-08-nr3` | 2026-08-08 | published | Køen, kulden og den næste watt |

## Kollisioner (skal være tom)

_Ingen — godt._
