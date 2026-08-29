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
| 2026-08-29 | aktier/2026-08-nr1 (nr. 1); dosis/2026-08-nr4 (nr. 4); gnisten/2026-08-nr4 (nr. 4); horisonten/2026-08-nr4 (nr. 4); humanerd/2026-08-nr4 (nr. 4); indeni/2026-08-nr4 (nr. 4); kraften/2026-08-nr4 (nr. 4); kronike/2026-08-nr3 (nr. 3); kulturboxen/2026-08-nr4 (nr. 4); orbit/2026-08-nr4 (nr. 4); pulsen/2026-08-nr4 (nr. 4); spaending/2026-08-nr4 (nr. 4) |

## Efter magasin

### aktier

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-08-nr1` | 2026-08-29 | published | Fem kandidater i et marked uden bred nedtur |

### dosis

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-08-nr1` | 2026-08-01 | published | Protein-æraen |
| 2 | `2026-08-nr2` | 2026-08-08 | published | Appetitten under kontrol |
| 3 | `2026-08-nr3` | 2026-08-15 | published | Søvnen, der ikke kan stikkes |
| 4 | `2026-08-nr4` | 2026-08-29 | published | Styrke, tarm og fedtsyrer — tre skeptiske eftersyn |

### gnisten

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-07-nr1` | 2026-07-19 | published | Sig hej til Claude |
| 2 | `2026-08-nr2` | 2026-08-01 | published | Ud af browseren |
| 3 | `2026-08-nr3` | 2026-08-08 | published | Agenten og den lokale hjerne |
| 4 | `2026-08-nr4` | 2026-08-29 | published | Flere agenter, mere ansvar |

### horisonten

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-07-nr1` | 2026-07-20 | published | Mallorca uden for højsæsonen |
| 2 | `2026-08-nr2` | 2026-08-01 | published | Georgien — bjerge, by og bord |
| 3 | `2026-08-nr3` | 2026-08-08 | published | Dolomitterne i efteråret |
| 4 | `2026-08-nr4` | 2026-08-29 | published | Sicilien i efteråret |

### humanerd

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-08-nr1` | 2026-08-01 | published | Robotter på arbejde |
| 2 | `2026-08-nr2` | 2026-08-08 | published | Lagerets koreografi |
| 3 | `2026-08-nr3` | 2026-08-19 | published | Tre humanoider, tre beviser |
| 4 | `2026-08-nr4` | 2026-08-29 | published | Nathandleren og samlebåndet |

### indeni

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-08-nr1` | 2026-08-01 | published | Dåsen |
| 2 | `2026-08-nr2` | 2026-08-08 | published | Filteret |
| 3 | `2026-08-nr3` | 2026-08-15 | published | Fjernvarmen — rørene under fortovet |
| 4 | `2026-08-nr4` | 2026-08-29 | published | Kontaktlinsen |

### kraften

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-08-nr1` | 2026-08-01 | published | Hvad holder lyset tændt |
| 2 | `2026-08-nr2` | 2026-08-08 | published | Strøm overalt |
| 3 | `2026-08-nr3` | 2026-08-15 | published | Hvem får strømmen først? |
| 4 | `2026-08-nr4` | 2026-08-29 | published | Atomkraften vender tilbage — drevet af datacentre, på vej til Månen |

### kronike

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-08-nr1` | 2026-08-08 | published | Riget formes |
| 2 | `2026-08-nr2` | 2026-08-19 | published | Kvinders valgret — fire aartier, fem aarstal |
| 3 | `2026-08-nr3` | 2026-08-29 | published | Andelsbevægelsen — bønder, der ejede fabrikken |

### kulturboxen

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-08-nr1` | 2026-08-01 | published | Supra og tillid |
| 2 | `2026-08-nr2` | 2026-08-08 | published | Tre sprog, ét plateau |
| 3 | `2026-08-nr3` | 2026-08-15 | published | Landet der arbejder ude |
| 4 | `2026-08-nr4` | 2026-08-29 | published | Marokko |

### orbit

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-08-nr1` | 2026-08-01 | published | Kadence |
| 2 | `2026-08-nr2` | 2026-08-08 | published | Kataloget og kikkerten |
| 3 | `2026-08-nr3` | 2026-08-15 | published | To hastigheder i kredsløb |
| 4 | `2026-08-nr4` | 2026-08-29 | published | De fire spor nr. 3 lod stå åbne |

### pulsen

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-07-nr1` | 2026-07-19 | published | Når maskinen lytter med |
| 2 | `2026-08-nr2` | 2026-08-01 | published | Når tasterne bliver stille |
| 3 | `2026-08-nr3` | 2026-08-08 | published | Når driften taler |
| 4 | `2026-08-nr4` | 2026-08-29 | published | Tre internationale pejlinger: ambient-tal, klinisk AI og genomdrevet forebyggelse |

### spaending

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-07-nr1` | 2026-07-19 | published | SPÆNDING nr. 1 · Juli 2026 |
| 2 | `2026-08-nr2` | 2026-08-01 | published | Når watt bliver hverdag |
| 3 | `2026-08-nr3` | 2026-08-08 | published | Køen, kulden og den næste watt |
| 4 | `2026-08-nr4` | 2026-08-29 | published | Sommeren, hvor Europa fulgte med |

## Kollisioner (skal være tom)

_Ingen — godt._
