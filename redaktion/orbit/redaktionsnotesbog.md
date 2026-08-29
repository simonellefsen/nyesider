# ORBIT – Redaktionsnotesbog

Opdateret efter genopbygningen af nr. 2 (august 2026, *"Kataloget og kikkerten"*).  
OpenRouter: **kun** `.env.orbit`. Imagine: `.env.local` / `XAI_API_KEY`.

## Identitet

Rumfart som industri og geopolitik: opsendelser, agenturer, sats, skrot, kalender, statistik, how-it-works.  
vs **KRAFTEN:** de tager rum-*kraft* (watt); vi tager mission/ops/katalog. Overlap OK.

## Forside (skifter hvert nummer)

1. Sæt `issueTheme` (nr. 2: **Kataloget og kikkerten**).  
2. Generér ny `images/orbit_cover.png` (3:4, Imagine) der fanger temaet.  
3. `issue.json`: `cover`, `coverCredit`, `coverSource`.  
4. Brand: navy `#0B1020`, blå `#5B8DEF`, guld `#E8B86D`. Ingen masthead-tekst i billedet.

## Nr. 2 — genopbygget og genudgivet 2026-08-16

**Tema:** Kataloget og kikkerten
**10 artikler, 5.683 ord** (var 10 artikler / 3.437 ord — gns. 344). Ni artikler reelt
kommissioneret på `.env.orbit`; lederen er chefredaktionens og har **ingen byline**.
Samlet forbrug **0,39 USD**. `bestilling.json`: `redaktion/orbit/numre/2026-08-nr2/bestilling.json`.

Temaet blev holdt: forskellen mellem det talte og det anslåede bærer Tallet, SSA-artiklen,
nærpassage-artiklen og rygtebørsen. Alle opsendelsestal er redaktionens egen optælling af
**unikke** orbitale opsendelser i GCAT's `launchlog.tsv` (opgjort 15. august 2026) — bemærk
at rå rækkeoptælling i den fil giver nyttelaster, ikke opsendelser, og derfor tal der er
ti gange for høje. Det er en fælde, næste nummer skal huske.

### Hvad faktatjekket fangede

- **Forkert år på et rigtigt tal.** Kalender-artiklen skrev «Falcon 9 gennemførte 162
  opsendelser i 2024». De 162 er 2025-tallet. Ironien er noteret: netop artiklen om forkerte
  årstal satte selv et tal på det forkerte år.
- **Samme tastefejl fra to forskellige modeller.** «Blue 0rigin» med nul i stedet for O
  optrådte uafhængigt i både `new-glenn` (Sonnet 5) og `esa-launcher` (Sonnet 5).
- **Et tal uden belæg.** Nærpassage-kladden angav en konkret manøvretærskel (0,01 %) — ubriefet,
  ukildebelagt, og i modstrid med artiklens egen pointe om, at tærsklen er et valg.
- **Et dødt link og et halvdødt.** NASA's `lowearthorbit.html` er en 404. ESA's
  `sdo.esoc.esa.int/environment_report/` svarer 200, men lander på portalens forside.
- **Bare domænehenvisninger** igen: `arianespace.com`, `nasa.gov/artemis`, «SpaceX' officielle
  opsendelsesoversigt» — alle uden den konkrete side, oplysningen står på.

### Læring til nr. 3

Samme som KRAFTEN nr. 2 samme dag: **sæt `mustCite` efter kildesøgningen, ikke før.** Fire
artikler udløser advarsel om for få citations, fordi briefen krævede 2, mens stoffet stammer
fra én kilde. To links til samme adresse er ikke to kilder.

## Nr. 2 — den afpublicerede udgave (til arkivet)

**Tema:** Kataloget og kikkerten  
10 artikler: leder, tallet (nærpassager), Starship vs Falcon, New Glenn RTF, SSA, Kuiper/konstellationer, ESA launcher, nærpassage uden panik, kalender, rygtebørs. (Ordbogen fjernet 2026-08-08.)  
Cover + 4 feature-billeder (Imagine).  
`bestilling.json`: `redaktion/orbit/numre/2026-08-nr2/bestilling.json`.  
Kryds: [KRAFTEN nr. 2](../../content/kraften/issues/2026-08-nr2/) (watt i rummet).

## Nr. 1 — genopbygget og genudgivet 2026-08-09

**Tema:** Kadence  
**12 artikler, 9.561 ord** (var 13 artikler / 2.420 ord — gns. 186). Ordbogen fjernet, jf. formatreglen nedenfor.  
Elleve artikler reelt kommissioneret på `.env.orbit`; lederen er chefredaktionens og har **ingen byline**.  
Samlet forbrug **0,53 USD**. `bestilling.json`: `redaktion/orbit/numre/2026-08-nr1/bestilling.json`.

Den oprindelige udgave havde **ingen `bestilling.json` overhovedet** — ingen brief, intet verdikt, ingen
kvittering — men bar byline til navngivne modeller. Hele nummeret er produceret forfra.

### Hvad faktatjekket fangede (læs dette før nr. 3)

Kladderne var gennemgående velskrevne. Fejlene lå næsten alle i **tidsfølsomme fakta**, hvor modellen
regnede videre på et forældet udgangspunkt — ikke i sproget:

- **Kalenderen** havde Artemis III som «NET september 2026» med første månelanding siden 1972, bygget på
  en NASA-melding fra januar 2024. NASA reviderede missionen i februar 2026: Artemis III lander **ikke**,
  men er en bemandet demonstration i **lav jordbane**, tidligst 2027; første landing er Artemis IV i 2028.
- **Rygtebørsen** troede, seneste New Glenn-flyvning var NG-1 i januar 2025. Der var sket tre ting siden.
- **Indien/Rusland** skrev, at OneWebs satellitter blev hentet hjem fra Baikonur. De ligger der stadig.
- **Blue Origin**-kladden fulgte briefens tese om at «andettrinnet bider» — og modsagde sig selv, fordi
  undersøgelsen af pad-eksplosionen peger mod *førstetrinnets* agterende. Artiklen argumenterer nu imod
  sin egen brief.

**Læring til briefs:** `researchNote` på issue-niveau kommer **ikke** med i prompten — kun `brief.angle`.
Tidslinjer og nøgletal skal skrives ind i den enkelte artikels `angle`, ellers regner modellen på sin
træningsviden. Det var direkte årsag til rygtebørsens fejl.

**Læring til kvitteringer:** BYOK-rutede kald (Anthropic, Gemini) rapporterer `cost=0` i svaret, fordi de
afregnes på vores egen upstream-nøgle. `commission.py` er rettet, så den tager `cost_details.
upstream_inference_cost` — men **aldrig lægger de to sammen**; det dobbelttæller et normalt kald.
Facit aflæses på `GET /api/v1/key`: `usage` skal matche de rutede kald, `byok_usage` de øvrige.

## Nr. 3 — udgivet 2026-08-19

**Tema:** To hastigheder i kredsløb. **7 artikler, 2.456 ord.** Seks artikler reelt kommissioneret på
`.env.orbit`; lederen er redaktionens uden byline. Forbrug **0,1627 USD**. `check_issue.py`:
**0 fejl, 1 advarsel** (korrekt, se nedenfor). `bestilling.json`:
`redaktion/orbit/numre/2026-08-nr3/bestilling.json`.

Fire kandidater brugt: launch pads/raketter verden rundt (som en global rekord-status), Starship
post-13, kinesiske LEO-konstellationer opsendt vs. plan, og Ariane 6 flight rate. Fire står stadig
åbne til nr. 4: Starbase (site/FAA/Texas-politik), Starmind, kommerciel SSA-marked, liability i
praksis.

### Trackerusikkerhed skrevet åbent frem — første gang i porteføljen

Global-rekord-artiklen og Tallet holder bevidst TO tal i luften på samme tid: SpaceNews' 324 globale
opsendelsesforsøg for 2025 mod Payload Space's 329. I stedet for at vælge ét som facit, skriver
begge artikler forskellen frem som pointen — trackere tæller Falcon Heavy, suborbitale forsøg og
årsafskæring forskelligt, og det er ikke et tegn på, at nogen tager fejl. **Denne tilgang bør
gentages, når to seriøse kilder reelt er uenige** — vælg ikke ét tal for at virke skarpere, end
kilderne selv er.

### To gættede/forkerte kilder fanget

- `kinesiske-konstellationer`-kladden citerede en SpaceNews-artikel fra **6. august 2024** om
  Qianfans FØRSTE opsendelser — irrelevant for 2026-status. Erstattet med to konstellationssporings-
  kilder (KeepTrack, China in Space), der faktisk dækker 2026-tallene.
- `ariane6-tempo`-kladden citerede to URL'er, der begge svarede **404** (aboutamazon.com,
  esa.int/Enabling_Support/Space_Transportation/Ariane_6 — en ældre, flyttet sti). Erstattet med
  Arianespaces egen pressemeddelelse og ESA's faktiske programoversigt.

### mustCite-lektionen fra nr. 2 anvendt korrekt denne gang

`tallet` endte med 5 citationer mod et briefet mustCite på 6 — men det er korrekt, ikke en fejl:
række 1 og 2 deler bevidst de samme to kilder (SpaceNews + Payload Space), fordi begge tal reelt
står i de samme to rapporter. At opfinde separate fodnoter til samme kilder havde været den falske
præcision, nr. 2's egen læring advarer imod.  

## Nr. 4 — udgivet 2026-08-29

**Tema:** De fire spor, nr. 3 lod stå åbne. **7 artikler, 2.910 ord.** Seks artikler reelt
kommissioneret på `.env.orbit`; lederen er redaktionens uden byline. Forbrug **0,1952 USD**.
`check_issue.py`: **0 fejl, 0 advarsler.** `check_links.py`: **0 døde links.** `bestilling.json`:
`redaktion/orbit/numre/2026-08-nr4/bestilling.json`.

Alle fire kandidater fra nr. 3 brugt: Starbase (FAA's godkendelse af 25 årlige
Starship-opsendelser, holdt eksplicit adskilt fra byens egen indlemmelse maj 2025), Starmind
(SpaceX' officielt navngivne orbitale AI-konstellation — endnu kun en FCC-ansøgning, intet
fartøj i kredsløb), det kommercielle SSA-marked (Andurils opkøb af ExoAnalytic Solutions som
konkret anker for markedstal), og liability i praksis (FN's Liability Convention, aldrig brugt
til at afgøre en satellitkollision, heller ikke efter Iridium-Cosmos 2009).

### Endnu et eksempel på reglen fra GNISTEN/KRAFTEN samme dag: skriv verificerede URL'er direkte i briefen

Ligesom GNISTEN og KRAFTEN nr. 4 samme dag blev alle briefs skrevet med eksplicitte, verificerede
kilde-URL'er indsat direkte i `brief.angle`. Alle seks kommissioneringer lykkedes på første
forsøg med korrekte fodnoter — ingen afviste forsøg denne gang.

### En tilføjet dato blev efterprøvet og holdt stik — ikke alle tilføjelser er fabrikationer

`liability-i-praksis`-kladden tilføjede selv en præcis dato (10. februar 2009) for
Iridium-Cosmos-kollisionen, som ikke stod i briefen. I modsætning til KRAFTEN nr. 4's SNAP-10A-
fejl samme dag var dette tal korrekt ved ekstern verifikation. **Lektionen er ikke "stol aldrig
på en tilføjet detalje" — det er "verificér den altid", uanset om den viser sig rigtig eller
forkert.**

### En for præcis hastighedsangivelse fjernet fra en spekulativ sætning

`rygteboersen`-kladden skrev "27.000 kilometer i timen" om en hypotetisk fremtidig kollision —
et konkret, ukildebelagt tal i en sætning, der kun skulle være spekulation. Fjernet før accept.

## Nr. 5 — kandidater

- **(2026-08-25) SpaceX' "Louisiana Purchase"** — ejerens forslag. SpaceX har annonceret en
  100 mia. USD-investering i et fjerde og hidtil største opsendelsesanlæg, "Starbase, Louisiana",
  i Vermilion Parish ved Pecan Island — 125.000-130.000 acres kystland konverteret fra en tidligere
  Exxon-grund. Ved fuld udbygning ventes fem opsendelseskomplekser, hver med to ramper og en
  drivmiddelfarm, plus produktionsfaciliteter og boliger til ansatte. Byggeri ventes at starte
  2027, første opsendelse tidligst 2029. Lokalaftale: SpaceX betaler Vermilion Parish 25 mio. USD
  om året i 25 år (med eskalatorklausul) plus 20 mio. USD i forudbetaling — over 820 mio. USD i
  direkte lokale betalinger over aftalens levetid — samt et krævet velgørenhedsbidrag på 25 mio.
  USD til Community Foundation of Acadiana. Kilder: [Payload Space](https://payloadspace.com/spacex-announces-new-starbase-louisiana-spaceport/),
  [New Atlas](https://newatlas.com/space-systems/spacex-build-worlds-largest-spaceport-louisiana/).
  God parallel til nr. 4's Starbase-artikel (Texas-byen) — denne gang er det delstaten Louisiana,
  ikke kun en lokal folkeafstemning. **Oplagt kandidat til skala-greb (se `## Format` nedenfor):**
  125.000-130.000 acres og 820+ mio. USD i lokale betalinger er tal, der beder om et
  areal-sammenligningsdiagram og helst et kort over Vermilion Parish/Pecan Island.
- **(2026-08) Europæisk rumadgang** — uafhængighed, opsendelseskapacitet, Ariane-programmets
  næste skridt (lovet som bagsideløfte).
- **(2026-08) Starmind-opfølgning** — når AI1-prototyperne rent faktisk sendes op (planlagt
  tidligt 2027, muligvis for tidligt til nr. 5).
- **(2026-08) Første Starbase-miljøvurdering (Stillehavs-genindtræden)** — opfølgning når FAA's
  afgørelse efter høringsperioden (lukkede 3. august 2026) foreligger.

## Format

- **Artikeltal:** typisk 10–14. Faste: Leder · Tallet · opsendelser · agenturer · konstellationer · SSA/skrot · kalender · rygtebørs. **Ingen Ordbog** — gloser i parentes/fodnote.
- **Standard `mustCite`:** 2+ for Tallet og agentur-features med launch-tal; 0 for rygtebørs.

### Ejerens greb (tilføjet 2026-08-29): skala, kort og deep dives

Fire stående instrukser fra ejeren, gældende fra nr. 5 og fremad:

1. **Vis skalaen på de virkelig store projekter.** Når en artikel handler om noget i milliard-
   eller mia.-USD-klassen (Starbase Louisiana, Starship-produktion, Terafab-typer anlæg), suppler
   teksten med et diagram eller en figur, der gør størrelsen konkret — areal sammenlignet med noget
   kendt, kapitalinvestering over tid, antal ansatte/lokationer. Brug `[CHART chart-id]` (se
   [content/CHARTS.md](../../content/CHARTS.md)) til tal-serier; brug en hånd-tegnet SVG (som
   INDENI/GNISTENs `figur-*.svg`-mønster) til strukturelle/geografiske forklaringer.
2. **Nævn europæisk teknologi, hvor det er relevant.** Artikler må ikke implicit fremstille
   rumfart som et rent USA/Kina-anliggende — nævn Ariane, ESA-programmer eller andre europæiske
   aktører, når historien har en naturlig plads til dem (jf. husreglens EU/USA/Kina-graf-standard
   i CHARTS.md, som allerede gælder for ORBIT).
3. **Deep dives:** overvej dedikerede dybdegående features om enkeltprogrammer — SpaceX Starship,
   Blue Origin, SpaceX Starbase (Texas og evt. Louisiana) — frem for kun korte statusopdateringer.
   Disse kan bære et helt nummer eller stå som en fast tilbagevendende sektion.
4. **Public domain-kortdata til lokationer.** Ejeren ønsker rigtige kort (fx Natural Earth/
   OpenStreetMap-afledt data, ikke AI-genererede fantasikort) til artikler, hvor en lokation er
   central (Starbase Texas vs. Louisiana, lanceringsbaser verden rundt). **Ingen eksisterende
   pipeline for dette i repoet endnu** — `production/generate_image.py` laver AI-kunst, ikke
   faktakort. Skal enten (a) løses med en ny let SVG-kort-komponent bygget på fri geodata, eller
   (b) en hånd-konstrueret SVG pr. artikel efter samme mønster som diagram-figurerne. Afklar
   værktøjsvalg, før det loves i en brief.

Generelt: læg vægt på at data/kort/diagrammer er *indlejret i artiklen*, ikke en pligtøvelse —
kun når det rent faktisk gør en stor ting mere begribelig.

## Research-regler

Ingen opdigtede launch-datoer. Skeln planlagt/scrub/success/failure. Primære kilder.  
`python production/load_env.py orbit` før produktion.

## Log

- **2026-08-29 (format):** Ejerens fire stående instrukser til skala/kort/deep dives/europæisk
  teknologi tilføjet under `## Format`. Gælder fra nr. 5. Kort-pipeline (public domain-geodata)
  mangler stadig og skal afklares, før den loves i en brief.

- **2026-08-19:** Nr. 3 udgivet — 'To hastigheder i kredsløb', nyt nummer produceret fra bunden.
  Se læringen ovenfor. To gættede/forkerte kilder fanget og rettet; trackerusikkerhed skrevet
  åbent frem i stedet for et falsk facit-tal.

- **2026-08-08 (depth):** Nr. 2 — nærpassage/Tallet udvidet (kollisioner, CDM, Liability Convention); Starship flight 13 (V3, Starlink V3-test, Indiske Ocean); SSA/leder/kalender synket.


- **2026-08-08 (format):** Ordbogen fjernet fra nr. 2 — LEO/SSA/HLS/FAA/FCC/Georeturn m.fl. i brødtekst/fodnote.


- **2026-08-08:** Nr. 2 publiceret — SSA, konstellationer, Starship/Falcon, New Glenn, ESA launcher.
- **2026-08-01:** Notesbog udvidet med `## Format`; leads datostemplet.

- **2026-08-08 (edit):** ORBIT nr. 2 — LEO, NASA HLS, FAA, FCC, ESA, CNSA, SSA udfoldet **pr. artikel** (læser lander ofte på én URL); ordbog udvidet. Husregel: chefredaktør ejer first-mention; fodnote OK hvis layout knækker.

