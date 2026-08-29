# INDENI · redaktionsnotesbog

## Identitet

INDENI forklarer hverdagen indefra. Hvert nummer tager udgangspunkt i én genstand eller et system, som læseren allerede bruger, og følger den gennem materialer, maskiner, brug og efterliv. Tonen er rolig, konkret og visuelt tænkende: ikke “teknologi er magi”, men “her er delene, her er afvejningen, og her er det sted, hvor kredsløbet kan knække”.

Målgruppen er den almindeligt nysgerrige danske læser. Forklar fagord første gang, vis strømmen med diagrammer, og vær ærlig om både effektivitet, affald, energi og usikkerhed. Industrivirksomheder må bruges som konkrete eksempler, aldrig som ukritiske reklamer.

## Format

- **Turen** følger én genstand fra råstof til hverdag.
- **Maskinen** zoomer ind på ét trin og har altid et egenproduceret SVG-diagram.
- **Kredsløbet** forklarer sortering, reparation eller genanvendelse som en virkelig logistisk kæde.
- **Europa** kortlægger mindst to faktiske europæiske anlæg eller industriled, med kilde og tydelig forskel på annonceret og eksisterende kapacitet.
- **Tallet** er en lille, kildebelagt tabel: år, geografisk afgrænsning og hvad tallet faktisk måler.
- **Påstandskontoret** afmonterer hverdagspåstande uden at lade som om, alle emballagevalg har ét facit.
- **Ingen fast Ordbog-side.** Fagord og forkortelser forklares i brødtekst (parentes) eller fodnote første gang — ikke som separat bagsnit. (Nr. 1 har historisk en ordbog; fra nr. 2 er formatet droppet.)
- **Færdig artikel, ikke kladde:** undgå meta-bokse som “INDENI-regel” / “INDENI-vane”. Skriv pointen ind i artiklen som læserprosa. Hellere ét udfoldet afsnit end tre overskrifter med én sætning.

## Udgivne numre

- **(2026-08) Nr. 4 — “Kontaktlinsen” — UDGIVET 2026-08-29 (nyt nummer, fra bunden).**
  7 artikler, **3.113 ord**. Seks artikler reelt kommissioneret på `.env.indeni`; lederen er
  chefredaktionens og har **ingen byline**. Samlet forbrug **0,1672 USD**. `check_issue.py`:
  **0 fejl, 1 advarsel** (kredsløbet: 2 citationer mod briefet mustCite=3 — korrekt, kun to
  reelt distinkte kilder findes for de amerikanske spildevandstal). `bestilling.json` under
  `numre/2026-08-nr4/`. Idébank-emnet kontaktlinsen valgt over asfalt; asfalt står stadig som
  kandidat. Nummeret har et egenproduceret SVG-diagram
  (`figur-kontaktlinse-stobning.svg`, de fire trin i cast molding-processen).

  ### Kernetal

  - **Fremstilling:** op til 34 timers hærdningstid for silikonehydrogel-linser under støbning
    (cast molding).
  - **Europa:** Johnson & Johnson Vision Care, Limerick (grundlagt 1996, ca. 1.600 ansatte, 7+
    mia. linser/år) og Bausch + Lomb, Waterford (grundlagt 1980, ca. 1.500 ansatte) — begge i
    Irland, ingen tredje europæisk fabrik fundet i denne research.
  - **Bortskaffelse (amerikanske tal, IKKE danske):** en undersøgelse ledet af Rolf Halden,
    Arizona State University (først præsenteret 2018, publiceret i *Environmental Science &
    Technology*, 1. september 2020), fandt at 15-20 % af amerikanske linsebrugere skyller
    brugte linser ud — anslået 1,8-3,36 mia. linser/år, 20-23 tons plastik/år i USA.

  ### Tre fejl fanget og rettet før udgivelse

  - **Opfundet, ubriefet statistik:** `europa`-kladden påstod, at "over 99 % af processen
    forløber i lukkede, sterile maskinkredsløb" på Limerick-fabrikken — et tal, der ikke findes
    i nogen kilde og ikke var briefet. Fjernet helt, ikke blot omformuleret.
  - **Byttet forfatterrækkefølge:** `maskinen`-kladden citerede "Fang, F. & Musgrave, C.S.A." —
    den korrekte rækkefølge (verificeret) er Musgrave, C.S.A. & Fang, F. En lille detalje, men
    samme klasse fejl som notesbogens egen læring om præcise litteraturhenvisninger.
  - **Egenproduceret SVG skrevet direkte i brødteksten:** `maskinen`-kladden byggede sit eget
    SVG-diagram som en fenced kodeblok midt i artikelteksten i stedet for at følge titlens
    faste mønster (selvstændig fil + `figures:`/`[FIGUR]`-markør). Diagrammet var faktisk godt —
    flyttet til `figur-kontaktlinse-stobning.svg` uden indholdsændring.

- **(2026-08) Nr. 3 — “Fjernvarmen” — UDGIVET 2026-08-19 (nyt nummer, fra bunden).**
  8 artikler, **3.082 ord**. Syv artikler reelt kommissioneret på `.env.indeni`; lederen er
  chefredaktionens og har **ingen byline**. Samlet forbrug **0,1960 USD**. `check_issue.py`:
  **0 fejl, 3 advarsler** (alle tre er korrekte enkelt-kilde-vurderinger, se nedenfor).
  `bestilling.json` under `numre/2026-08-nr3/`.

  Første idébank-emne valgt: fjernvarmen (rørene under fortovet). Kontaktlinsen og asfalt står
  stadig som kandidater. Nummeret har et egenproduceret SVG-diagram
  (`figur-fjernvarme-kredslob.svg`) i samme stil som nr. 2's filterdiagram.

  ### Kernetal

  - **Dansk fjernvarme:** 1.982.623 boliger tilsluttet pr. 1. januar 2025 (op fra 1.933.141),
    +49.482 boliger i 2024. Men konverteringstempoet bremser: 27.000 husstande fik
    konverteringsforslag i 2024, mod ca. 50.000/år i hvert af de to foregående år.
  - **Amager Bakke (København):** 400.000+ tons affald/år, 157–247 MW fjernvarme, 0–63 MW el,
    2,7 MWh varme + 0,8 MWh el pr. ton affald, varme til 160.000 husstande.
  - **Spittelau (Wien):** 460 MW installeret kapacitet, men kun ca. 60 MW typisk grundlast —
    resten er spidslast fra gaskedler. En 16 MW varmepumpe har siden løftet den termiske
    kapacitet til ca. 76 MW.

  ### To gættede/forkerte kilder fanget

  - `maskinen`-kladden citerede to URL'er (en ARC-sti og en Ramboll-projektside), der begge
    svarede **404**. Erstattet med ARC's faktiske "From Waste to Energy"-side.
  - `kredsloebet`-kladden citerede `dansk-fjernvarme.dk` (med bindestreg) — en variant, der ikke
    findes. Den rigtige adresse er `danskfjernvarme.dk` uden bindestreg.

  ### Tre "for få citationer"-advarsler er alle korrekte, ikke fejl

  `turen`, `maskinen` og `tallet` endte alle under det briefede mustCite — samme mønster som
  KRAFTEN og ORBIT nr. 3 samme dag. Hver historie har genuint kun én eller få kilder (Dansk
  Fjernvarme/DST for de danske tal, ARC for Amager Bakke, Wien Energie for Spittelau). At opfinde
  ekstra fodnoter til samme kilde ville have været falsk præcision. Ledgerens `citations`-felt
  viser det faktiske, korrekte antal med en forklarende note.

- **(2026-08) Nr. 2 — “Filteret” — GENOPBYGGET OG GENUDGIVET 2026-08-17.**
  9 artikler, **5.678 ord** (var 2.005 ord — gns. 223, altså præcis det notesbogen kalder
  “tre overskrifter med én sætning”). Otte artikler reelt kommissioneret på `.env.indeni`;
  lederen er chefredaktionens og har **ingen byline**. Samlet forbrug **0,30 USD**.
  `check_issue.py`: **0 fejl, 0 advarsler.** `bestilling.json` under `numre/2026-08-nr2/`.

  ### Det, der virkede: forbyd tal, når der ikke er kilder

  Nummeret har meget få kildebelagte tal — kun Melittas egen historieside og Cepis nøgletal.
  I stedet for at lade modellerne fylde hullerne **forbød hver enkelt brief eksplicit** de tal,
  der manglede kilde: gramvægt, porestørrelse, fiberlængde, bryggetemperatur, bryggeforhold,
  nedbrydningstid, CO₂. Resultatet: ikke ét opfundet tal i otte kladder, og fire af dem gik ind
  praktisk taget uredigeret. **Gør det sådan igen.** En brief, der tier om tal, inviterer til gæt;
  en brief, der forbyder dem, får mekanismen forklaret i stedet.

  Bryg-kladden gjorde noget, ingen anden kladde i genopbygningen har gjort: den skrev sin egen
  kildebegrænsning ind i brødteksten — at SCA's grænseværdier ligger bag medlemslogin, og at
  redaktionen ikke har læst dem. Bedre formuleret, end briefen selv gjorde det.

  ### Hvad faktatjekket fangede

  - **En velkendt fortælling gengivet som kendsgerning:** at Melittas første filter var trækpapir.
    Det står ikke på selskabets historieside, som er artiklens kilde. Nu gengivet som det, det er.
  - **En detalje for meget:** «bag et betalingsmur og et lukket medlemslogin» om SCA. Vi ved, at
    der kræves medlemslogin. Vi ved ikke, at der er en betalingsmur.
  - **Bare domænehenvisninger** igen: `melitta-group.com` og `cepi.org` uden side. Cepis tal står
    i **pressemeddelelsen**, ikke på forsiden, og PDF'en med nøgletallene ligger bag et downloadlink.

  ### Kildekritik, der skal med i artiklen

  Cepi er brancheorganisation for producenterne, og meddelelsen argumenterer for politiske tiltag.
  Det står nu åbent i både Europa-artiklen og Tallet. Tallet «6,6 billioner euro i 2030» fra samme
  meddelelse er en **fremskrivning af markedspotentiale** — brug det kun mærket som estimat.
- **(2026-08) Nr. 1 — “Dåsen”**: aluminiumsdrikkedås fra materiale og formning til dansk pant og europæisk omsmeltning. Originale SVG-diagrammer viser formning, pantstrøm og lukket kredsløb.
  **Genopbygget 2026-08-09:** 11 artikler / 6.936 ord (var 12 / 3.427). Ordbogen fjernet. Ti artikler
  reelt kommissioneret på `.env.indeni`; lederen er chefredaktionens uden byline. Forbrug **0,50 USD**.

## Redaktionslog

- **2026-08-29:** Nr. 4 udgivet — "Kontaktlinsen", nyt nummer produceret fra bunden med
  egenproduceret SVG-diagram af cast molding-processen. Tre fejl fanget og rettet, inkl. en
  opfundet, ubriefet statistik ("99 % af processen") i Europa-artiklen. Se læringen ovenfor.
- **2026-08-19:** Nr. 3 udgivet — "Fjernvarmen", nyt nummer produceret fra bunden med egenproduceret
  SVG-diagram. Se læringen ovenfor. To gættede/forkerte kilder fanget og rettet.
- **2026-08-01:** “Det usynlige lag” udvidet efter læserspørgsmål med polymertyper, drikspecifik coating-validering og EU/EFSA's BPA-spor. Læringen: skriv aldrig “dåselak” som én universel kemisk opskrift.
- **2026-08-08:** Nr. 2 publiceret — kaffefilteret med procesdiagram.
- **2026-08-08 (edit):** Nr. 2 udvidet (især bryg + Europa); fjernet Ordbogen; meta-snippets skrevet ind i brødtekst.

### Læring fra genopbygningen af nr. 1 (2026-08-09)

**Skriv tal ind i `brief.angle`, ikke i `researchNote`.** Kun `brief.angle` når frem til modellen.

**Kildefejlen var gennemgående og forudsigelig:** næsten hver kladde afsluttede med *bare
domænehenvisninger* — «Se aluminum.org», «danskretursystem.dk» — i stedet for konkrete sider. Det er
ubrugeligt for læseren og skal rettes hver gang. Regn med det.

**Det største fund var et forældet regelspor.** Kladden om den indvendige lak byggede på EFSA's
revurdering fra 2023 og konkluderede, at branchen frivilligt bevægede sig væk fra BPA. Virkeligheden:
forordning (EU) 2024/3190 forbyder BPA i fødevarekontaktmaterialer **inklusive dåselakker**, i kraft
20. januar 2025, med frist for engangsemballage der udløb **20. juli 2026**. Tjek altid, om et
«branchen er på vej»-spor i mellemtiden er blevet til lov.

**Kvitteringer: brug DAGS-tællerne.** `.env.indeni` havde ca. 0,10 USD forbrug fra tidligere i august,
som ikke står i nogen `bestilling.json`. `usage_daily` + `byok_usage_daily` matchede ledgeren præcist;
levetidstallet ville have pålagt nummeret 0,10 USD, det ikke har brugt.

**Modellerne kan levere præcise referencer.** `hvorfor-33-cl` angav uopfordret Hosford & Duncan,
*Scientific American* 271(3), september 1994, s. 48–53 — bind, nummer, måned og sidetal alle korrekte.

## Idébank

- ~~Fjernvarmen~~ → **brugt i nr. 3** (2026-08-19).
- ~~Kontaktlinsen~~ → **brugt i nr. 4** (2026-08-29).
- **(2026-08) Asfalt** — sten, bitumen, temperatur, genbrug og vejarbejde om natten.

## Løfter til læseren

- Vi viser processen, før vi fælder dommen.
- Vi angiver altid år og geografi ved hårde tal.
- Vi tegner selv, når diagrammet er vigtigere end et dekorativt billede.
