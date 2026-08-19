# SPÆNDING – Redaktionsnotesbog

*Opdateret efter nr. 3 (august 2026, "Køen, kulden og den næste watt") — editor-revision for dybde.*

## Identitet

**SPÆNDING** dækker elbiler og teknologien bag dem, med europæisk fokus: modeller, ladeinfrastruktur, afgifter, brugtmarked. **vs KRAFTEN:** SPÆNDING er bilen og køreoplevelsen; KRAFTEN er nettet, TWh og lande.

## Format

- **Faste formater:** Rygtebørs, essay, Kort & Watt (bagsnit må dele billede).
- **Standard `mustCite`:** 1–2 for features med pris/rækkevidde/ladeeffekt eller navngivne projekter; 0 for rygtebørs og essay.
- **Forkortelser pr. artikel:** WLTP, BEV, DC, OTA m.fl. udfoldes første gang (parentes/fodnote).
- **Dybde før bredde:** features skal være læsbare artikler (sigt typisk **250–500 ord**), ikke tre overskrifter med én sætning. Navngiv **konkrete operatører, byer og projekter**, når de er dokumenterbare (fx Waymo, Apollo Go, Ionity) — og mærk selskabstal/planer som sådan.
- **Robotaxi / ny tech:** skeln zone, menneske-i-loop, betalte kunder vs. beta, og myndighed. “London/Wayve” alene er for tyndt, når der findes kommerciel drift andre steder.
- Diagrammer: gap EU/USA/Kina + top performers.

## Nr. 3 — GENOPBYGGET OG GENUDGIVET 2026-08-19

**Tema:** Køen, kulden og den næste watt. 10 artikler, **3.308 ord**. Ni artikler reelt
kommissioneret på `.env.spaending`; lederen er redaktionens uden byline. Forbrug **0,2435 USD**.
`check_issue.py`: **0 fejl, 0 advarsler.**

Den afpublicerede bestilling.json havde ingen research og intet forbrug for nogen af de ti opgaver.
Alle fem nr. 4-kandidater, notesbogen selv havde flagget, blev løst i denne genopbygning:

- **Dokumenteret 600 kW-status**: IONITY har det i Sorgues, Sydfrankrig — ikke Danmark. Clever/Andel
  har et pilotprojekt (16 udtag, Storkøbenhavn) annonceret til udgangen af 2026. Tre krav sat op før
  nogen kan skrive "Danmarks første": i drift, 600 kW til én bil, offentligt tilgængeligt. Ingen
  opfyldt endnu.
- **Kilometerafgift — vedtaget tekst**: der findes ingen. Det viste sig at være den rigtige historie:
  ingen lov, kun forsøg og en ekspertgruppe. Det, der faktisk skete i stedet, var en frysning af
  registreringsafgiften og en elafgift sænket fra 90 til ca. 1 øre/kWh fra 1. januar 2026.
- **Xiaomi typegodkendelse/prisliste**: findes ikke. Officiel Europa-lancering 2027; kun individuel
  EU-godkendelse af enkelteksemplarer i dag, intet forhandlernetværk.
- **Robotaxi — status med konkret myndighedstekst**: Waymo (~500.000 ugentlige betalte ture, USA),
  Apollo Go (20 mio. ture kumulativt, Kina + internationalt), Zoox (amerikansk NHTSA-godkendelse).
  Ingen kommerciel, betalt, førerløs drift i Europa endnu.
- **Leaf/vinter-køretest med egne tal**: erstattet af ADACs 14-bilers vintertest — bredere og bedre
  kildebelagt end en enkeltmodel-test ville have været.

### To gættede/forkerte kilder fanget denne omgang

- `faststof`-kladden citerede en Reuters-artikel fra **18. december 2023** om at NIO "tester" et
  1.000 km-batteri — forkert og forældet i forhold til de faktiske 2026-tal (150 kWh, 360 Wh/kg,
  1.070 km). Erstattet med den faktisk anvendte 2026-kilde.
- `kort-og-watt`-kladden citerede `bilimportoererne.dk`, som **ikke opløser** (DNS-fejl) — samme
  gamle domænenavn, nr. 2's læring allerede havde flagget som forældet. Rettet til `mobility.dk`.

### Ny statuskode i kildekontrollen

`xiaomi-status`-kladdens Reuters-fodnote svarede **401** til automatiserede kald — `check_links.py`
klassificerer IKKE 401 som bot-blokering (kun 403/406/429 er på listen), så den talte som DEAD.
Erstattet med CNBC og Autocar, begge verificeret 200 og dækkende samme faktuelle claim.
**Tilføj 401 til listen over statuskoder, der kræver en erstatningskilde, ikke bare en note.**

`bestilling.json`: `redaktion/spaending/numre/2026-08-nr3/bestilling.json`.

## Nr. 2 — genopbygget og genudgivet 2026-08-16

**Tema:** Når watt bliver hverdag
**9 artikler, 4.296 ord** (var 9 artikler / 2.707 ord — gns. 301). Otte artikler reelt
kommissioneret på `.env.spaending`; lederen er chefredaktionens og har **ingen byline**.
Samlet forbrug **0,39 USD**. `bestilling.json`: `redaktion/spaending/numre/2026-08-nr2/bestilling.json`.

**Xiaomi-artiklen er udgået** og erstattet af `nye-maerker`. Nr. 3 har allerede en Xiaomi-status,
og Mobility Denmarks registreringstal bar en bedre og langt bedre belagt historie.

### Det, der endelig løste afgiftsproblemet

Titlen har taget fejl af afgifter to gange. Denne gang blev artiklen skrevet **fra selve
lovteksten** — registreringsafgiftslovens § 5 b i den konsoliderede udgave på retsinformation.dk
(`eli/lta/2025/370`) — og ikke fra referater. Det gav trappen sort på hvidt: 40 % til og med 2025,
derefter +8 procentpoint om året til 80 % i 2030, så +4 om året til 100 % i 2035. Bundfradraget
for personbiler: 165.500 kr. (2025), 155.400 (2026), 150.800 (2027), 146.200 (2028), 141.600 (2029),
137.000 fra 2030. **Gør det sådan igen.** Primærkilden findes, den er gratis, og den er entydig.

Lige så vigtigt: artiklen **nægter at regne en konkret bilpris ud**, fordi afgiften også afhænger
af den afgiftspligtige værdi og satserne i §§ 4, 5 og 5 a. Kladden skrev selv begrundelsen —
«et regneeksempel uden alle disse led ville se overbevisende ud og være forkert» — og den
formulering bør stå som titlens standard.

### Hvad faktatjekket fangede

- **To opfundne webadresser.** `alpitronics.eu` (megawatt-kladden) og `mobilitydenmark.dk`
  (nye-mærker-kladden). Den sidste svarer ikke engang på DNS. De rigtige er
  `alpitronic.it/en/hypercharger/hyc-1000/` og `mobility.dk/nyregistreringer/`.
- **Et firmanavn med et bogstav for meget:** «Alpitronics». Selskabet hedder Alpitronic.
- **En forkert lovtitel:** brugtmarkeds-kladden kaldte kilden «lov om registrering af køretøjer».
  Det er en anden lov end registreringsafgiftsloven.
- **Instruktionslæk:** «Vær præcis omkring præmissen:» stod midt i brødteksten i nye-mærker —
  briefens egen ordlyd sivet ind i artiklen. Tjek altid for det.
- **En ubelagt konfiguration:** Leaf-kladden påstod, at de 445 km er «den mindre batterivariant».
  Modelsiden siger det ikke. Rettelsen gav en skarpere pointe: «fra» er en nedre grænse.

### Kilder, der flyttede sig

`skm.dk` → `svmn.dk` (Skatte- og Vækstministeriet). `bilimp.dk` → `mobility.dk` (Mobility Denmark,
tidl. De Danske Bilimportører). `nissan.dk/biler/nye-biler/leaf.html` svarer 200 og leverer
**forsiden** — den rigtige adresse er `leaf.nissan.dk`. Alpitronic svarer på `/en/hypercharger/<model>/`,
ikke `/en/products/<model>/`.

### Læring om formatet

Rygtebørsen blev briefet til 400-600 ord og endte på 297 efter redigering, fordi kladdens engelske
fagudtryk i parentes blev fjernet. En rygtebørs, der forklarer «Battery Electric Vehicles»
undervejs, er ikke en rygtebørs. **Sæt ordbudgettet for rygtebørsen til 250-450.**

## Nr. 2 — den afpublicerede udgave (til arkivet)

Leaf gen3, megawatt-ladning, Xiaomi, afgifter 2027, brugtmarked, bagsnit. 2.707 ord.


## Nr. 2 — den afpublicerede udgave (til arkivet)

Leaf gen3, megawatt-ladning, Xiaomi, afgifter 2027, brugtmarked, bagsnit.

## Nr. 4 — kandidater

- **(2026-08) Første dokumenterede DK 600 kW-personbiladresse**  
- **(2026-08) Leaf/vinter-køretest med egne tal**  
- **(2026-08) Xiaomi typegodkendelse/prisliste**  
- **(2026-08) Kilometerafgift — vedtaget tekst**  
- **(2026-08) Robotaxi — status når EU/DK har konkret myndighedstekst**

## Log

- **2026-08-19:** Nr. 3 genopbygget og udgivet efter at have stået uden research eller kvitteringer.
  Se læringen ovenfor. To gættede/forkerte kilder fanget og rettet; ny statuskode (401) tilføjet til
  kildekontrollen.

- **2026-08-08:** Nr. 3 publiceret — ærlig 600 kW-status, robotaxi, solid-state, km-afgift, vinterfysik.
- **2026-08-08 (edit):** Nr. 3 udvidet generelt; robotaxi-artiklen tilføjet navngivne globale projekter (Waymo, Zoox/Tesla-spor, Baidu Apollo Go, europæisk forsigtighed). Formatregel om dybde og konkrete projekter.
- **2026-08-01:** Format + leads; Leaf WLTP-verifikation.
