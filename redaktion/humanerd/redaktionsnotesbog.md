# HumaNerd · redaktionsnotesbog

## Identitet

HumaNerd undersøger robotter, som skal arbejde blandt mennesker: humanoider, robotarme, mobile robotter og husholdningsrobotter. Magasinet er nysgerrigt, men ikke godtroende. Vi skelner altid mellem en prototype, en pilot, en validering, en kommerciel installation og stabil drift i et rigtigt arbejdsskift.

Vi bruger "fysisk AI" som en forklaring, ikke som en magisk etiket: en robot skal sanse, beregne, planlægge, bevæge sig og stoppe sikkert. Kinesiske, japanske, sydkoreanske, amerikanske og europæiske producenter dækkes med den samme målestok. Virksomheders egne tal navngives som virksomheders egne oplysninger; sammenlignelig markedsstatistik kommer helst fra International Federation of Robotics (IFR).

## Format

- **Fabrikken** starter med den opgave, robotten faktisk skal løse, før den beskriver kroppen.
- **Humanoiden** læser annonceringer som statusrapporter: hvad, hvor, hvem, hvor længe og med hvilken begrænsning?
- **Verdenskortet** sammenligner regioner uden at gøre nationalitet til teknologiens forklaring.
- **Hjernen** forklarer ét lag i robotstakken (gerne med diagram, når det hjælper).
- **Hjemmet** behandler privatliv, sikkerhed og vedligehold som en del af produktet — og menneskeligt arbejde i “samarbejdet”.
- **Tallet** angiver år, geografi og måleenhed i en kildebelagt tabel; skeln IFR fra virksomhedstal.
- **Påstandskontoret** afmonterer hype uden messesprog.
- **Ingen fast Ordbog-side.** AMR, WMS, SKU, 3PL, API m.fl. forklares i brødtekst (parentes) eller fodnote første gang i *hver* artikel. (Nr. 1 har historisk ordbog; fra nr. 2 er formatet droppet.)
- **Dybde før bredde:** features skal være læsbare artikler (sigt typisk **500–800 ord**, hævet fra 250–500 den 2026-08-09), ikke tre overskrifter med én sætning. Navngiv **konkrete operatører/anlæg/systemer**, når de er dokumenterbare (Amazon/Kiva-arv, Ocado-grid, AutoStore, navngivne 3PL-piloter) — og mærk selskabstal som selskabstal.
- **Undgå meta-bokse** (“HumaNerd-målestok” som tjekliste-overblik er ok, hvis den er kort; hellere indlejret i prosa end “regel”-bokse der ligner redaktionsnoter).

## Udgivne numre

### Nr. 4 — “Nathandleren og samlebåndet” — UDGIVET 2026-08-29 (nyt nummer, fra bunden)

7 artikler, **3.533 ord**. Seks artikler reelt kommissioneret på `.env.humanerd`; lederen er
chefredaktionens og har **ingen byline**. Samlet forbrug **0,1547 USD**. `check_issue.py`:
**0 fejl, 0 advarsler.** `bestilling.json` under `numre/2026-08-nr4/`.

Ejerens brief: en historie om det danske robotselskab **HIVE Robots** og **Salling Group/Føtex**.
Research (WebSearch/WebFetch) fandt et ægte, dateret partnerskab — annonceret 11. marts 2026,
pilot fra sommeren 2026, natarbejde i lukkede butikker, langsigtet mål 3-5 robotter pr. butik —
brugt som nummerets ene anker i **Humanoiden**. Det andet anker, valgt af redaktionen for at give
nummeret bredde uden at overskride budgettet på 7 artikler, er **Apptronik Apollo hos
Mercedes-Benz** (Berlin-Marienfelde + Kecskemét, Ungarn, 520 mio. USD Serie A-X februar 2026,
Jabil-partnerskab mod kommerciel skala fra 2027) — et andet, europæisk, men langt kapitaltungere
bevis. **Hjernen** bruger HIVE's egen "Heimdall"-platform til at forklare teleoperation som bro
til autonomi generelt. **Verdenskortet** sætter de to europæiske piloter op mod Tesla (internt,
udelukkende datafangst ifølge Musk selv) og Shenzhen/Leju (Kinas første pilotproduktionslinje for
humanoide robotter, men til en forsknings-/uddannelsesrobot, ikke en industriarbejder — en
skelnen, der ER historien i det afsnit).

#### Fem fejl/svagheder fanget og rettet før udgivelse

- **Faktuel fejl:** Hjernen-kladden kaldte HIVE Robots for "det amerikanske selskab" — HIVE er
  dansk (Kongens Lyngby, CVR 45531805). Rettet.
- **Domænenavne uden konkrete URL'er** (samme mønster som nr. 2's læring): Tallet-kladdens fem
  fodnoter var kun "hive-robots.com" (forkert domæne i øvrigt), "sallinggroup.com", "apptronik.com",
  "ir.tesla.com", "reuters.com" — ingen af dem pegede på en bestemt side. Erstattet med fem
  side-specifikke, verificerede URL'er.
- **Forældede/forkerte kilder til aktuelle påstande:** Verdenskortet-kladden citerede en
  Apptronik/Jabil-meddelelse og et Tesla "Q1 2024 Update" — begge dateret FØR de 2026-hændelser,
  de skulle understøtte. Erstattet med den faktiske Jabil-partnerskabsmeddelelse og Tesla's
  Q4 2025-resultatkonference (afholdt 28. januar 2026).
- **Dødt link efter redirect:** Fabrikken-kladdens `apptronik.com/news` gav 301→404. `check_links.py`
  ville have fanget en direkte 404, men ikke redirect-kæden — fundet ved manuel `curl -L`-verificering
  af hver URL før udgivelse. Erstattet med den korrekte pressemeddelelse-URL.
- **Citat i anførselstegn uden ordret dækning:** To kladder (Verdenskortet, Påstandskontoret)
  satte en parafrase af Elon Musk ("lære og indsamle data") i anførselstegn, som om det var et
  direkte citat. Den faktiske kilde (Teslas Q4 2025-resultatkonference) bekræfter kun parafrasen
  — ikke den ordrette formulering. Omskrevet til reported speech uden anførselstegn.

**Navnetjek, der IKKE endte i artiklen:** research fandt modstridende sekundære kilder om, hvorvidt
en "Jakob Sand" er medstifter/direktør hos HIVE Robots ud over CEO Charlotte Blou Sand — nogle
aggregator-sider nævner ham, det officielle CVR-udtræk gjorde det ikke entydigt. I stedet for at
gætte blev navnet simpelthen ikke brugt i den udgivne tekst.

**Driftsnotits:** `google/gemini-3.1-pro` (Hjernens planlagte skribent) svarede HTTP 400 "not a
valid model ID" på OpenRouter, selvom `modeller.json` lister den som `aktiv`. Løst med `--fallback`
til DeepSeek V3.2 — se `redaktion/modelkartotek.md`, "Produktionspraktik".

### Nr. 3 — “Tre humanoider, tre beviser” — UDGIVET 2026-08-19 (nyt nummer, fra bunden)

7 artikler, **3.656 ord**. Seks artikler reelt kommissioneret på `.env.humanerd`; lederen er
chefredaktionens og har **ingen byline**. Samlet forbrug **0,2028 USD**. `check_issue.py`:
**0 fejl, 1 advarsel** (korrekt, se nedenfor). `bestilling.json` under `numre/2026-08-nr3/`.

Idébank-emnet "Tre humanoider, tre beviser" brugt direkte: 1X NEO (forudsalgs-bevis, 10.000
forudbestillinger på fem dage), Figure 03 hos BMW Spartanburg (kontraheret drifts-bevis, 40
enheder, 25 USD/robot-time, 99 %+ nøjagtighed), og Boston Dynamics Atlas hos Hyundai
(hensigts-bevis: en 25.000-robot-plan for 2028, blokeret af Korean Metal Workers' Union siden
22. januar 2026 — bilindustriens første strejke rettet specifikt mod humanoide robotter, juli
2026). Verdenskortet-artiklen bruger samme research til at afmontere national-kapløbs-sproget:
BMW bruger både amerikansk (Figure) og schweizisk (Hexagon/AEON) teknologi på to forskellige
fabrikker; et koreansk selskab (Hyundai) ejer et amerikansk robotfirma (Boston Dynamics).

### Fire gættede/dårlige kilder fanget og rettet

- **Atlas/fagforening:** kladdens tre fodnoter (bostondynamics.com, hyundaimotorgroup.com,
  ifr.org) sourcerede intet af fagforeningens citat eller juli-strejken. Erstattet med UPI
  (26. jan. 2026) og Tech Times (20. jul. 2026), som faktisk dækker de to hændelser.
- **Verdenskortet:** to fodnoter fra 2024 (Reuters om BMW/Figure, TechCrunch om Mercedes/Apptronik)
  var forældede *og* døde — Reuters-linket gav **HTTP 401** (behandlet som dødt, ikke
  bot-tolerabelt, jf. SPÆNDING nr. 3's regel samme dag), TechCrunch-linket gav **404**. Erstattet
  med Figure AI's og PR Newswires egne 2026-meddelelser.
- **Hjemmet:** en fodnote pegede på en gættet `openai.com/index/1x/`-sti (HTTP 403, ikke
  bekræftet som en reel side). Erstattet med 1X's egen, bekræftede pressemeddelelse om den
  OpenAI-ledede finansieringsrunde.
- **Tallet:** kladdens seks fodnoter var kun prosahenvisninger til domænenavne
  ("hyundaimotorgroup.com", "sydkoreansk erhvervspresse") uden konkrete URL'er — ubrugeligt for
  en læser. Erstattet med fire konkrete, verificerede sider (1x.tech, BMW Group PressClub,
  Hyundai newsroom, Seoul Economic Daily).

### mustCite-advarslen i Tallet er korrekt, ikke en fejl

`tallet` endte med 4 citationer mod et briefet mustCite på 5 — samme mønster som ORBIT og
KRAFTEN nr. 3 samme dag. Tabellens seks rækker deler reelt kun fire distinkte kilder: række 1+2
er begge 1X, række 3+4 er begge BMW. At opfinde en femte fodnote til en allerede citeret kilde
havde været falsk præcision. Ledgerens `citations`-felt viser det faktiske, korrekte antal med
en forklarende note.

### Nr. 2 — “Lagerets koreografi” — GENOPBYGGET OG GENUDGIVET 2026-08-17

9 artikler, **5.878 ord** (var 2.279 ord — gns. 253). Otte artikler reelt kommissioneret på
`.env.humanerd`; lederen er chefredaktionens og har **ingen byline**. Samlet forbrug **0,40 USD**.
`check_issue.py`: **0 fejl, 0 advarsler.** `bestilling.json` under `numre/2026-08-nr2/`.

**Nummeret fik et rigtigt nyhedsanker undervejs.** Researchen fandt, at IERA-prisen 2026 —
uddelt af IFR og IEEE's robotselskab — gik til det schweiziske Verity for et autonomt
indendørs dronesystem (Frankfurt, 16. juni 2026). Det ændrede hovedartiklen fra en generisk
lagerfeature til en historie med dato, kilde og en pointe: **den mest værdifulde robot i et
lager er måske ikke den, der løfter noget, men den der tæller.** Verificerede tal derfra:
dronerne arbejder i måneder ad gangen med to til tre batteriskift om året, optager omkring
500.000 billeder om dagen på tværs af lagre, og er udrullet i omkring 200 lagre.

Alle tal i nummeret kommer fra IFR og er tilskrevet dem — i tråd med formatreglen om at
skelne selskabstal fra IFR-statistik. Verity-oplysningerne er desuden mærket som **IFR's
gengivelse af en prisvinders system**, ikke som uafhængigt bekræftede driftstal.

### Hvad faktatjekket fangede

- **En kilde, der svarer 200 uden at bære påstanden.** WMS-kladden henviste til
  `ifr.org/service-robots` med påstand om, at siden omtaler Veritys lagerrobotter. Siden findes,
  men det kunne ikke bekræftes. Erstattet af IERA-pressemeddelelsen, som redaktionen har læst,
  og som indeholder netop udsagnet om integration i lagerstyringssystemer.
- **To fodnoter uden link**, som blev erstattet af de konkrete pressemeddelelser.

### Metoden, der nu har virket fem gange

INDENI, HORISONTEN, PULSEN, KULTURBOXEN og HumaNerd nr. 2: **en brief, der forbyder de tal, der
ikke kan kildebelægges, får mekanismen forklaret i stedet.** Her var forbuddet plukhastigheder,
fejlprocenter, cyklustider, hastigheds- og kraftgrænser, priser og ROI — og otte kladder kom hjem
uden ét opfundet tal. Fem af otte gik ind praktisk taget uredigeret.

### Tallet: pas på nævneren

IFR's robottæthed (8. april 2026, World Robotics 2025 med 2024-tal): Vesteuropa 267 pr. 10.000
ansatte, Nordamerika 204, Asien 131, globalt 132, EU-27 231, USA 307, Kina 166. **Kinas tal bygger
på opdaterede arbejdsmarkedstal fra landets statistikbureau** — samme nævner-fænomen som nr. 1
beskrev. Bemærk også, at tætheden måler industrirobotter i fremstillingsindustrien, så et lager
ikke nødvendigvis tæller med; det gør målet dårligt egnet til netop dette nummers emne, og det
står i artiklen.

**Personskifte til fremtidige citater:** IFR fik ny præsident 2. juli 2026 — Jane Heffner
(Teradyne Robotics) efter Takayuki Ito (Fanuc). Ældre Ito-citater skal tilskrives ham som
*daværende* præsident.

- **(2026-08) Nr. 2 — “Lagerets koreografi”**: AMR’er, Amazon/Ocado/AutoStore som eksempler, pluk, WMS, sikkerhed, den menneskelige undtagelse. Uden ordbog. `bestilling.json` under `numre/2026-08-nr2/`.
- **(2026-08) Nr. 1 — “Robotter på arbejde”**: humanoider og andre robotter i fabrik, lager og hjem. Nummeret kortlægger markedet, AI-stakken og forskellen mellem feltforsøg og drift.
  **Genopbygget 2026-08-09:** 11 artikler / 6.630 ord (var 12 / 2.924). Ordbogen fjernet. Ti artikler
  reelt kommissioneret på `.env.humanerd`; lederen er chefredaktionens uden byline. Forbrug **0,42 USD**.

### Læring fra genopbygningen af nr. 1 (2026-08-09)

**Den vigtigste kilde lå i kundens eget nyhedsrum.** BMW's pressemeddelelse af 6. august 2024 om den
«vellykkede test» med Figure indeholder sætningen, at der *aktuelt ikke er nogen Figure AI-robotter på
fabrikken i Spartanburg, og at der ikke er fastlagt nogen tidsplan*. Den citeres stort set aldrig
videre. Læringen er generel: når en leverandør fejrer et forløb hos en kunde, så læs kundens egen
udmelding fra samme dag — den er ofte smallere, og forskellen er historien.

**Hold styr på, hvis tal det er.** Alle detaljerede tal fra Figure/BMW-forløbet (11 måneder,
ca. 1.250 driftstimer, 90.000 dele, 30.000 X3) kommer fra leverandøren. BMW's vicedirektør bekræftede,
at pilotforsøget gik godt, uden at angive ét eneste tal. Den asymmetri skal stå i artiklen.

**En 200 er ikke et bevis for, at siden er den rigtige.** Tre gange i denne genopbygning gættede en
kladde en adresse, som svarede 200 med et helt andet indhold — to gange hos Geostat, én gang hos
**ifr.org**, hvor `…/robot-density-by-country-2024` serverer en pressemeddelelse om FCC-restriktioner
fra august 2026. `check_links.py` godkender dem alle. Åbn siden og læs, hvad der står.

**En delvist rigtig litteraturhenvisning er farligere end en forkert.** En kladde angav «Evan Ackerman,
*How to Watch a Robot Video*, IEEE Spectrum, 2023». Forfatter, år og emne var rigtige; titel og
publikation var det ikke. Den rigtige er *How to Make a Good Robot Video [Media]*, **IEEE Robotics &
Automation Magazine**, bind 30, nr. 2, 2023, s. 127. Kontrollér altid tidsskrift, bind og side — ikke
kun at forfatteren findes.

**Pas på kategorifejl mellem tælleværker.** Amazons million robotter (juli 2025) og IFR's driftsbestand
på 4.664.000 industrirobotter tæller ikke det samme; Amazons flåde er overvejende mobile lagerrobotter.
Divisionen «Amazon står for en femtedel af verdens industrirobotter» cirkulerer alligevel.

**Kontrollér også de tal, briefen selv udleverer.** Briefen regnede 1.250 driftstimer om til fire timer
pr. arbejdsdag. Det er fem. Fejlen nåede to kladder, fordi begge stolede på briefen.

**Kvitteringer: her var DAGS-tælleren den rigtige.** `usage_daily + byok_usage_daily` = 0,424845 mod
ledgerens 0,4248. Levetidstallet lå 0,019 USD højere — tidligere, udokumenteret forbrug på nøglen,
formentlig det, der frembragte de to forældreløse kladder i `kladder/`. Modsat KULTURBOXEN, hvor
levetidstallet var det rigtige. Reglen er stadig: afstem mod begge, og forklar forskellen.

## Idébank

- **(2026-08) Robotten der kan se** — kameraer, kraftsensorer og grænserne for perception.
- **(2026-08) Håndens problem** — gribere, taktilitet og hvorfor det bløde stadig er svært.
- ~~Tre humanoider, tre beviser~~ → **brugt i nr. 3** (2026-08-19).
- **(2026-08) Dronen som robot** — inspektion, lager, landbrug og beredskab; skeln mellem fjernstyring, assisteret flyvning og autonomi.
- **(2026-08) Robotter i krig** — militære anvendelser, dual use, menneskelig kontrol, fejlrisiko og dokumentation. Må ikke behandles som gadgetstof eller produktpromovering; brug primærkilder, folkeretlige rammer og uafhængig rapportering.
- **(2026-08) Boston Dynamics efter videoen** — fra mobilitet til konkret arbejdscelle, med den samme pilot→drift-målestok som nr. 1.
- **(2026-08) Humanoiden på scenen** — robotter i koncert, teater, forlystelse, tv og brandaktivering. Skeln mellem autonom robot, teleoperation, forudprogrammeret koreografi og visuel illusion.

## Løfter til læseren

- Vi skriver "pilot", når det er en pilot.
- Vi gør regneenheden tydeligere end tallet.
- Vi viser sikkerhed, data og menneskeligt arbejde som en del af systemet.
- Vi navngiver drift, når den findes — og siger fra, når det kun er en demo.

## Log

- **2026-08-29:** Nr. 4 publiceret — "Nathandleren og samlebåndet" (HIVE Robots × Føtex, samt
  Apptronik Apollo × Mercedes-Benz). Ejerbrief-emne. Fem fejl/svagheder fanget og rettet før
  udgivelse, se læringen ovenfor.
- **2026-08-08:** Nr. 2 publiceret — lager/AMR før humanoid-hype.
- **2026-08-08 (edit):** Nr. 2 udvidet (især lager-koreografi med Amazon/Ocado/AutoStore m.fl.); Ordbogen fjernet; formatregel om dybde og inline-forklaringer.
- **2026-08-09:** Nr. 1 genopbygget og genudgivet efter afpubliceringen 2026-08-08. Se læringen ovenfor.
- **2026-08-09 (format):** Formatreglen om 250–500 ord pr. feature er hævet til **500–800**. Loftet stammede fra en periode, hvor artiklerne var for tynde; et blad, der skelner mellem pilot, validering og drift, kan ikke gøre det på 250 ord.
