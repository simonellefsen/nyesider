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

- **(2026-08) Fjernvarmen** — rørene under fortovet, varmeværket og den enkelte radiator.
- **(2026-08) Kontaktlinsen** — polymer, sterilisering, pasform og hvorfor den ikke må skylles ud i vasken.
- **(2026-08) Asfalt** — sten, bitumen, temperatur, genbrug og vejarbejde om natten.

## Løfter til læseren

- Vi viser processen, før vi fælder dommen.
- Vi angiver altid år og geografi ved hårde tal.
- Vi tegner selv, når diagrammet er vigtigere end et dekorativt billede.
