# SPÆNDING – Redaktionsnotesbog

*Opdateret efter nr. 5 (2026-09-05, "Brugtmarkedet finder sine ben").*

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

## Nr. 4 — udgivet 2026-08-29

**Tema:** Sommeren, hvor Europa fulgte med. **7 artikler, 2.435 ord.** Seks artikler reelt
kommissioneret på `.env.spaending`; lederen er redaktionens uden byline. Forbrug **0,1862 USD**.
`check_issue.py`: **0 fejl, 0 advarsler.** `check_links.py`: **0 døde links.** `bestilling.json`:
`redaktion/spaending/numre/2026-08-nr4/bestilling.json`.

**Rettelse til dette dokument:** de fem "Nr. 4-kandidater", der stod listet her tidligere (600 kW,
Leaf-vintertest, Xiaomi, kilometerafgift, robotaxi-myndighedstekst), var allerede løst og brugt i
selve nr. 3's genopbygning — listen var aldrig ryddet op efter brug. Nr. 4 er i stedet bygget på
tre helt nye, friske spor: BYD overhaler Tesla i europæiske nyregistreringer (174.144 mod
170.351) samtidig med at EU skifter fra told til et pris-gulv; London får sit første
robotaxi-forsøg (Wayve/Uber, TfL-godkendt, men superviseret — ikke førerløs); og Danmarks
offentlige ladenetværk vokser til 51.090 punkter, +35 % siden udgangen af 2024, hurtigere end
elbilflåden selv.

### Formatreglens skelnen holdt igen: superviseret ≠ førerløs

`london-robotaxi`-briefen krævede eksplicit, at Wayve/Uber-forsøget i London IKKE blev fremstillet
som førerløs drift — der er fortsat en TfL-godkendt sikkerhedsfører om bord på hver tur. Kladden
fulgte instruksen præcist og satte London eksplicit i forhold til Waymo/Apollo Go's reelle,
betalte, førerløse drift uden for Europa. Samme skelnen blev gentaget i Kort & Watt for at
understrege pointen på tværs af nummeret.

### En navnefejl fanget: Dansk e-Mobilitet, ikke "Danske Mobilitet"

`danmark-ladenetvaerk`-kladden skrev organisationsnavnet forkert. Rettet til det korrekte navn,
Dansk e-Mobilitet, før accept.

### Et unødvendigt præcist tal fjernet fra en fremadrettet teaser

`rygteboersen`-kladden lovede i sit bagsideløfte til nr. 5 et konkret "10 % batteritab" for
brugte elbiler — et tal, der hverken var briefet eller kildebelagt, i en sætning der kun skulle
være en åben teaser. Rettet til en generisk formulering. **Regel værd at huske: selv et
bagsideløfte kan indeholde en faktapåstand, der kræver kilde, hvis det er formuleret som et
konkret tal.**

## Nr. 5 — udgivet 2026-09-05

**Tema:** Brugtmarkedet finder sine ben — og to robotaxi-forsøg går fra plan til drift (indfrier
nr. 4's bagsideløfte). **5 artikler, 1.691 ord.** Tre artikler reelt kommissioneret på
`.env.spaending`; lederen er redaktionens uden byline, og Cybercab-artiklen er redaktionens efter
to mislykkede kommissioneringsforsøg (se nedenfor). Forbrug **0,1571 USD**. `check_issue.py`:
**0 fejl, 2 advarsler** (begge forklarede, se nedenfor). `check_links.py`: **0 døde links** (4
bot-blokerede: Wayve, Engadget, electrive.com, Tesla — alle svarer 403 men er læst manuelt).
`bestilling.json`: `redaktion/spaending/numre/2026-09-nr5/bestilling.json`.

### Vigtigt nyt fund: at indsætte en URL i briefen giver IKKE modellen levende browsing

`cybercab-lancering` blev forsøgt kommissioneret to gange. Første forsøg (uden URL i briefen)
afviste korrekt at skrive artiklen, fordi eventet (3. september 2026) ligger efter modellens
træningsdata — samme sunde reaktion som GNISTEN nr. 4's `fokus-ansvar`. Efter GNISTEN/KRAFTEN/
ORBITs etablerede fix — sæt en verificeret URL direkte ind i `brief.angle` — blev anden
kommissionering forsøgt med `https://en.wikipedia.org/wiki/Tesla_Cybercab` indsat eksplicit.
Modellen skrev denne gang en hel artikel, der HÆVDEDE, at kilden ikke dokumenterede eventet — men
det gør den, hvilket redaktionen selv bekræftede ved en direkte `WebFetch` af samme URL. Modellen
havde altså ikke rent faktisk læst siden; den ræsonnerede ud fra sin egen (forældede) viden om
Cybercabs 2024-fremvisning, konkluderede fejlagtigt, at intet nyere var dokumenteret, og opfandt
oven i købet fire ekstra, ubriefede fodnoter (Tesla, NHTSA, Waymo) til støtte for sin forkerte
skepsis. Det er værre end en ærlig afvisning, fordi det ligner en velbegrundet, kildekritisk
artikel. **Rettelse til hele porteføljens URL-i-brief-praksis: en indsat URL er en instruktion om,
hvad artiklen SKAL siges at bygge på — den er ikke en garanti for, at modellen selv har læst
indholdet. Chefredaktøren skal stadig selv verificere kildens indhold uafhængigt (fx via egen
WebFetch) og være parat til at skrive artiklen selv, hvis modellen enten afviser ELLER — værre —
skriver selvsikkert forkert om en kilde, den ikke reelt har adgang til.** Artiklen blev skrevet
færdig af redaktionen (status: `rewritten-by-editor`, ingen byline). Begge kaldte regninger
(0,008301 + 0,0253035 USD) er reelle, betalte API-kald og talt med i nummerets samlede forbrug.

### En kladde brugte forældede kilder til en aktuel begivenhed

`kort-og-watt`-kladden (Gemini 3.1 Pro) citerede en Uber-investor-pressemeddelelse fra 2024 og en
Reuters-artikel om en kapitalrejsning fra maj 2024 som "dokumentation" for Londons robotaxi-
lancering i september 2026 — samme mønster som Cybercab-fejlen: plausible, ægte kilder, der bare
ikke handler om den begivenhed, de skal dokumentere. Erstattet med Wayves egen 2026-pressemeddelelse
og Engadget. Samme kladde citerede også en forældet EU-toldsats for BYD (17 %), uden at vide, at EU
erstattede tolden med en mindstepris-ordning fra januar 2026 — rettet til den aktuelle beskrivelse.

## Løfter givet i nr. 5

- **Bagsiden:** Volvos næste generations elektriske platform, ventet i en sedan-/stationcar-udgave
  af EX30.

## Nr. 6 — kandidater

- ~~Teslas Cybercab-lanceringsevent~~ → **brugt i nr. 5** (2026-09-05, som et lukket, afdæmpet
  event — ikke den store demonstration, der var ventet).
- ~~Brugtmarkedet for elbiler~~ → **brugt i nr. 5** (2026-09-05).
- **(2026-09) Volvos næste generations EV-platform** — lovet som bagsideløfte til nr. 6.
- **(2026-08) BYD's Ungarn-fabrik — opfølgning** — produktionsstart har flyttet sig fra Q2 til Q4
  2026; stadig ubekræftet.
- **(2026-09) Londons robotaxi-forsøg — opfølgning** — konkrete køretal/hændelser, når data
  foreligger efter opstarten 3. september 2026.

## Nr. 5 — kandidater (arkiv, brugt)

- **(2026-09-03) Teslas Cybercab-lanceringsevent** — ejerens forslag. Tesla afholder et
  invitation-only lanceringsevent i Austin, Texas, 3. september 2026, for topscorere i
  virksomhedens "Robotaxi rider"-lodtrækning; livestreamet for alle andre. Ventet indhold: den
  endelige produktionsdesign af Cybercab (tosædet, ingen rat eller pedaler, bygget udelukkende til
  førerløs drift på Tesla's AI4-computer), live-demonstrationer af Full Self-Driving, og detaljer
  om udrulningsplanen for Teslas robotaxi-netværk. Cybercab blev første gang vist frem ved "We,
  Robot"-eventet i oktober 2024; siden er den blevet testet på offentlig vej, og ansatte fik
  prøveture på private veje nær Austin-hovedkvarteret i juli 2026. Kilder:
  [Teslarati](https://www.teslarati.com/tesla-cybercab-launch-official-date-austin/),
  [Motor1](https://www.motor1.com/news/805874/tesla-cybercab-robotaxi-launch-austin/). Datoen
  ligger EFTER nr. 4's udgivelse (29. aug.) — til nr. 5 bør research opdateres med, hvad eventet
  faktisk viste, ikke kun hvad der var annonceret på forhånd. God krydsreference til nr. 4's
  London-robotaxi-artikel (superviseret vs. reelt førerløs — Cybercab er designet til sidstnævnte
  fra start).
- **(2026-08) Brugtmarkedet for elbiler** — batterikapacitet efter de første år, konkrete
  tjeklister (lovet som bagsideløfte).
- **(2026-08) BYD's Ungarn-fabrik** — opfølgning når produktionen af Dolphin Surf reelt starter
  (planlagt 4. kvartal 2026).
- **(2026-08) Londons robotaxi-forsøg** — opfølgning på faktiske køretal/hændelser, hvis der
  kommer data efter opstarten.

## Log

- **2026-09-05:** Nr. 5 udgivet — 'Brugtmarkedet finder sine ben', indfrier nr. 4's bagsideløfte.
  Vigtigt metodefund: en URL indsat i `brief.angle` beviser ikke, at modellen har læst dens
  indhold — den kan stadig skrive selvsikkert forkert om en kilde, den reelt ikke har adgang til.
  Se læringen ovenfor. Cybercab-artiklen skrevet af redaktionen efter to mislykkede forsøg.

- **2026-08-19:** Nr. 3 genopbygget og udgivet efter at have stået uden research eller kvitteringer.
  Se læringen ovenfor. To gættede/forkerte kilder fanget og rettet; ny statuskode (401) tilføjet til
  kildekontrollen.

- **2026-08-08:** Nr. 3 publiceret — ærlig 600 kW-status, robotaxi, solid-state, km-afgift, vinterfysik.
- **2026-08-08 (edit):** Nr. 3 udvidet generelt; robotaxi-artiklen tilføjet navngivne globale projekter (Waymo, Zoox/Tesla-spor, Baidu Apollo Go, europæisk forsigtighed). Formatregel om dybde og konkrete projekter.
- **2026-08-01:** Format + leads; Leaf WLTP-verifikation.
