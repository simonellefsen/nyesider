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
| 2026-08-31 | aktier/2026-08-nr2 (nr. 2) |
| 2026-09-05 | gnisten/2026-09-nr5 (nr. 5); kraften/2026-09-nr5 (nr. 5); orbit/2026-09-nr5 (nr. 5); pulsen/2026-09-nr5 (nr. 5); spaending/2026-09-nr5 (nr. 5) |
| 2026-09-07 | aktier/2026-09-nr3 (nr. 3) |
| 2026-09-12 | dosis/2026-09-nr5 (nr. 5); horisonten/2026-09-nr5 (nr. 5); humanerd/2026-09-nr5 (nr. 5); indeni/2026-09-nr5 (nr. 5); kronike/2026-09-nr4 (nr. 4); kulturboxen/2026-09-nr5 (nr. 5) |
| 2026-09-14 | aktier/2026-09-nr4 (nr. 4) |
| 2026-09-21 | aktier/2026-09-nr5 (nr. 5) |
| 2026-09-28 | aktier/2026-09-nr6 (nr. 6) |
| 2026-10-03 | dosis/2026-10-nr6 (nr. 6); gnisten/2026-10-nr6 (nr. 6); horisonten/2026-10-nr6 (nr. 6); humanerd/2026-10-nr6 (nr. 6); indeni/2026-10-nr6 (nr. 6); kraften/2026-10-nr6 (nr. 6); kronike/2026-10-nr5 (nr. 5); kulturboxen/2026-10-nr6 (nr. 6); orbit/2026-10-nr6 (nr. 6); pulsen/2026-10-nr6 (nr. 6); spaending/2026-10-nr6 (nr. 6) |
| 2026-10-05 | aktier/2026-10-nr7 (nr. 7) |

## Efter magasin

### aktier

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-08-nr1` | 2026-08-29 | published | Fem kandidater i et marked uden bred nedtur |
| 2 | `2026-08-nr2` | 2026-08-31 | published | Fire dips, stadig intet udsalg i indekset |
| 3 | `2026-09-nr3` | 2026-09-07 | published | LULU invalideret — fem nye dips mens indekset holder toppen |
| 4 | `2026-09-nr4` | 2026-09-14 | published | Comcast endelig med — Rockwool åbner København-siden |
| 5 | `2026-09-nr5` | 2026-09-21 | published | Efter Fed: Adobe til rabat — yield i UPS, Sanofi, Telenor og Telekom |
| 6 | `2026-09-nr6` | 2026-09-28 | published | Intuit-vask — Pepsi, Lowe's og Orkla mens Nike venter |
| 7 | `2026-10-nr7` | 2026-10-05 | published | Regnskabsdag: ni ud, tre ind — vi rydder op i porteføljen |

### dosis

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-08-nr1` | 2026-08-01 | published | Protein-æraen |
| 2 | `2026-08-nr2` | 2026-08-08 | published | Appetitten under kontrol |
| 3 | `2026-08-nr3` | 2026-08-15 | published | Søvnen, der ikke kan stikkes |
| 4 | `2026-08-nr4` | 2026-08-29 | published | Styrke, tarm og fedtsyrer — tre skeptiske eftersyn |
| 5 | `2026-09-nr5` | 2026-09-12 | published | Tre skeptiske eftersyn: magnesium, creatin og collagen |
| 6 | `2026-10-nr6` | 2026-10-03 | published | Kirkegården for glemte superfødevarer — en obduktion af, hvordan en wellness-myte dør |

### gnisten

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-07-nr1` | 2026-07-19 | published | Sig hej til Claude |
| 2 | `2026-08-nr2` | 2026-08-01 | published | Ud af browseren |
| 3 | `2026-08-nr3` | 2026-08-08 | published | Agenten og den lokale hjerne |
| 4 | `2026-08-nr4` | 2026-08-29 | published | Flere agenter, mere ansvar |
| 5 | `2026-09-nr5` | 2026-09-05 | published | Skyen som standardvalg — hvad koster det at komme i gang? |
| 6 | `2026-10-nr6` | 2026-10-03 | published | Indbakken uden at trykke send — kan AI rydde op uden at sende, slette eller love noget på dine vegne? |

### horisonten

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-07-nr1` | 2026-07-20 | published | Mallorca uden for højsæsonen |
| 2 | `2026-08-nr2` | 2026-08-01 | published | Georgien — bjerge, by og bord |
| 3 | `2026-08-nr3` | 2026-08-08 | published | Dolomitterne i efteråret |
| 4 | `2026-08-nr4` | 2026-08-29 | published | Sicilien i efteråret |
| 5 | `2026-09-nr5` | 2026-09-12 | published | Kreta — oldtidens paladser, en kløft der lukker for vinteren, og en ny fast rubrik |
| 6 | `2026-10-nr6` | 2026-10-03 | published | Storby-weekend Lissabon — syv bakker, to verdensarvsmonumenter og en kyststi mod vest |

### humanerd

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-08-nr1` | 2026-08-01 | published | Robotter på arbejde |
| 2 | `2026-08-nr2` | 2026-08-08 | published | Lagerets koreografi |
| 3 | `2026-08-nr3` | 2026-08-19 | published | Tre humanoider, tre beviser |
| 4 | `2026-08-nr4` | 2026-08-29 | published | Nathandleren og samlebåndet |
| 5 | `2026-09-nr5` | 2026-09-12 | published | Dronen som robot — tre beviser, tre autonominiveauer |
| 6 | `2026-10-nr6` | 2026-10-03 | published | Håndens problem — gribere, taktilitet, og hvorfor det bløde stadig er svært |

### indeni

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-08-nr1` | 2026-08-01 | published | Dåsen |
| 2 | `2026-08-nr2` | 2026-08-08 | published | Filteret |
| 3 | `2026-08-nr3` | 2026-08-15 | published | Fjernvarmen — rørene under fortovet |
| 4 | `2026-08-nr4` | 2026-08-29 | published | Kontaktlinsen |
| 5 | `2026-09-nr5` | 2026-09-12 | published | Asfalt — fra stenbrud og raffinaderi til vejen, der genopstår som sig selv |
| 6 | `2026-10-nr6` | 2026-10-03 | published | Køleskabet — fra stål og kølemiddel til kompressoren, der aldrig sover, og kredsløbet der tapper den tom |

### kraften

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-08-nr1` | 2026-08-01 | published | Hvad holder lyset tændt |
| 2 | `2026-08-nr2` | 2026-08-08 | published | Strøm overalt |
| 3 | `2026-08-nr3` | 2026-08-15 | published | Hvem får strømmen først? |
| 4 | `2026-08-nr4` | 2026-08-29 | published | Atomkraften vender tilbage — drevet af datacentre, på vej til Månen |
| 5 | `2026-09-nr5` | 2026-09-05 | published | Fra produktion til distribution: kablerne under havet og kobberet i dem |
| 6 | `2026-10-nr6` | 2026-10-03 | published | Gennem skyggen: solpaneler, batterier og strømstyring når lyset forsvinder |

### kronike

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-08-nr1` | 2026-08-08 | published | Riget formes |
| 2 | `2026-08-nr2` | 2026-08-19 | published | Kvinders valgret — fire aartier, fem aarstal |
| 3 | `2026-08-nr3` | 2026-08-29 | published | Andelsbevægelsen — bønder, der ejede fabrikken |
| 4 | `2026-09-nr4` | 2026-09-12 | published | Christian 4. og stormagtstiden — byggekongen, der forarmede sit rige |
| 5 | `2026-10-nr5` | 2026-10-03 | published | Slesvig-Holsten før 1864 — hertugdømmerne, helstaten og den forfatning, der blev påskud |

### kulturboxen

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-08-nr1` | 2026-08-01 | published | Supra og tillid |
| 2 | `2026-08-nr2` | 2026-08-08 | published | Tre sprog, ét plateau |
| 3 | `2026-08-nr3` | 2026-08-15 | published | Landet der arbejder ude |
| 4 | `2026-08-nr4` | 2026-08-29 | published | Marokko |
| 5 | `2026-09-nr5` | 2026-09-12 | published | Japan uden kirsebærtræer — arbejde, bolig, dating og hverdag |
| 6 | `2026-10-nr6` | 2026-10-03 | published | Portugal — hverdag, arbejde, bolig, mad, penge, normer |

### orbit

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-08-nr1` | 2026-08-01 | published | Kadence |
| 2 | `2026-08-nr2` | 2026-08-08 | published | Kataloget og kikkerten |
| 3 | `2026-08-nr3` | 2026-08-15 | published | To hastigheder i kredsløb |
| 4 | `2026-08-nr4` | 2026-08-29 | published | De fire spor nr. 3 lod stå åbne |
| 5 | `2026-09-nr5` | 2026-09-05 | published | Europæisk rumadgang — og en amerikansk kontrast i skala |
| 6 | `2026-10-nr6` | 2026-10-03 | published | Løfterne indfries: FAA siger ja til Stillehavet, Starmind venter stadig på rampen |

### pulsen

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-07-nr1` | 2026-07-19 | published | Når maskinen lytter med |
| 2 | `2026-08-nr2` | 2026-08-01 | published | Når tasterne bliver stille |
| 3 | `2026-08-nr3` | 2026-08-08 | published | Når driften taler |
| 4 | `2026-08-nr4` | 2026-08-29 | published | Tre internationale pejlinger: ambient-tal, klinisk AI og genomdrevet forebyggelse |
| 5 | `2026-09-nr5` | 2026-09-05 | published | Opfølgning: Bupa i drift, og AID_NOTE på målstregen |
| 6 | `2026-10-nr6` | 2026-10-03 | published | Mellemåret: AID_NOTE og genomik uden facit — men med pejlemærker |

### spaending

| Nummer | issue-slug | published | status | tema |
|---|---|---|---|---|
| 1 | `2026-07-nr1` | 2026-07-19 | published | SPÆNDING nr. 1 · Juli 2026 |
| 2 | `2026-08-nr2` | 2026-08-01 | published | Når watt bliver hverdag |
| 3 | `2026-08-nr3` | 2026-08-08 | published | Køen, kulden og den næste watt |
| 4 | `2026-08-nr4` | 2026-08-29 | published | Sommeren, hvor Europa fulgte med |
| 5 | `2026-09-nr5` | 2026-09-05 | published | Brugtmarkedet finder sine ben — og to robotaxi-forsøg går fra plan til drift |
| 6 | `2026-10-nr6` | 2026-10-03 | published | Europa bygger, tester og designer lavt — Szeged, London og Volvos SPA3-platform |

## Kollisioner (skal være tom)

_Ingen — godt._
