# KRØNIKE – Redaktionsnotesbog

Oprettet 2026-08-08. Modelerfaringer: [modelkartotek](../modelkartotek.md).

## Identitet

**KRØNIKE** er magasinet om **danmarkshistorie** med magasin-dybde: magt, diplomati, krig, kriser, opfindelser, industri, sociale skift, religion, migration og biografier (mænd og kvinder) fra ca. **år 700 til år 2000**.

### Tone

- Fortællende, kildetung, nøgtern — ikke romantiseret nationalisme og ikke ren skolebog.  
- Skeln **myte / tradition / belagt kilde**. Skriv årstal, aktører og usikkerhed ærligt.  
- Billeder: AI-genereret (Imagine), stil **varieret** (retro, grunge, illustreret, geometrisk …) — undgå “stock-middelalder” på alle sider.

### Afgrænsning

- **Ikke KULTURBOXEN:** nutidig hverdagskultur i andre lande.  
- **Ikke HORISONTEN:** rejseguide.  
- **Ikke PULSEN/DOSIS:** sundhedssektor/krop.  
- Nutid (efter ~2000) kun som **kort spejl**, ikke som hovedstof.

## Format

- **Artikeltal:** typisk **8–10** — hellere færre og dybere end 12 tynde.  
- **Ordmål (revideret 2026-08-08 efter nr. 1):** features **700–900**. Tallet 250–450. Leder 120–220. Bagsnit korte.  
  Nedre grænse er et **gulv, ikke et mål**: en historiefeature under 700 ord når kun at *nævne* sin sag. Nr. 1's svageste artikler (reformation 404 ord, 1864 383 ord) havde begge en god tese og derefter ingen plads til hverken menneske, scene eller dokument. De stærkeste (Hedeby 689, Ørsted 633) var de længste. Det er ikke tilfældigt.
- **Krav til en feature (ikke kun ordtal):** mindst **ét navngivet menneske**, **én konkret scene eller ét citeret/refereret dokument**, og **ét hårdt tal med kilde**. En feature, der kun består af tese + punktopstilling af konsekvenser, er en disposition, ikke en artikel.
- **Ingen Ordbog, ingen Rygtebørs.** Gloser i parentes/fodnote. Eventuelt bagsnit: *Myter & missforståelser*.  
- **Standard `mustCite`:** **3+** for features (nr. 1 lå på 2 og fik i praksis fodnoter som `danmarkshistorien.dk / lærebogstradition` uden URL — det er en pladsholder forklædt som kilde). Fodnoter skal pege på **navngivet værk/institution**, gerne klikbart. 0 for leder/myter (når bevidst).  
- OpenRouter: **kun** `.env.kronike`. Imagine: `.env.local`.

## Nr. 1 — udgivet

**Tema:** Riget formes  
**Slug:** `2026-08-nr1`  
12 artikler: leder, tallet, Hedeby/Dannevirke, kristning, Margrete 1., reformation, Øresundstold, landboreformer, 1864, udvandring, H.C. Ørsted, myter.  
`bestilling.json`: `redaktion/kronike/numre/2026-08-nr1/bestilling.json`.

## Nr. 2 — udgivet 2026-08-19

**Tema:** Kvinders valgret — fire aartier, fem aarstal
**Slug:** `2026-08-nr2`
9 artikler, **4.641 ord**. Otte artikler reelt kommissioneret på `.env.kronike`; lederen er
chefredaktionens og har **ingen byline**. Samlet forbrug **0,302 USD**. `check_issue.py`:
**0 fejl, 0 advarsler.** `check_links.py`: **0 døde links.** `bestilling.json`:
`redaktion/kronike/numre/2026-08-nr2/bestilling.json`.

Fem aarstal baerer nummeret: 1871 (Dansk Kvindesamfund stiftes), 1908 (kommunal valgret),
1915 (grundlovsaendringen), 1918 (foerste kvinder i Rigsdagen) og 1924 (Nina Bang minister).
Format-kravet fra nr. 1 (mindst ét navngivet menneske, én konkret scene, ét haardt tal med
kilde pr. feature) blev holdt i alle seks features.

### Den vigtigste laering: en model kan haandtere en myte praecist, hvis briefen kraever det

Nina Bang krediteres i loes tale ofte som "verdens foerste kvindelige minister". Det er upraecist:
Aleksandra Kollontaj var folkekommissaer i den bolsjevikiske magts Sovjetrusland allerede i
1917/1918, foer Bang. Braaftet for `nina-bang`-artiklen kraevede eksplicit denne skelnen
(parlamentarisk-demokratisk udpegelse vs. revolutionaer magtovertagelse), og kladden loeste det
korrekt paa foerste forsoeg — presist og uden at goere Bangs bedrift mindre. **Faren laa et andet
sted:** `valget-1918`-kladden, som IKKE havde faaet myte-braaftet, skrev ukritisk "Danmarks og
verdens foerste kvindelige minister" om Bang i forbifarten. Rettet til en henvisning til den
dedikerede artikel i stedet. **Laering: naar en faktuel praecisering er vigtig, skal den ind i
HVER brief, der naevner emnet — ikke kun i braaftet for hovedartiklen om det.**

### To reelle fejl fanget i faktatjekket

- **Jutta Bojsen-Møller** blev i `grundloven-1915`-kladden krediteret som "forperson for Dansk
  Kvindesamfund" i 1915. Faktuelt forkert: hun var formand 1894-1910, og i 1915 aeresformand, som
  ledte optoget til Amalienborg. Rettet til korrekt titel.
- Flere kladder brugte fodnoter, der kun henviste til domaenenavne uden URL ("kvindesamfund.dk",
  "ft.dk — historisk oversigt") — samme muster som nr. 1's laering fra 2026-08-08. Erstattet
  gennemgaaende med konkrete, verificerede sider.

### Et link, der virkede i curl med rå apostrof, men fejlede procent-kodet

`danmarkshistorien.lex.dk`'s side om "de syv F'er" findes kun med en **rå** apostrof i URL'en
(`F'er`), ikke den procent-kodede form (`F%27er`), som ellers er standard URL-encoding. Modellen
skrev selv den korrekte, rå form i kladden; en senere redigering procent-kodede den ved en fejl,
hvilket gjorde linket dødt. **Test altid den endelige URL i den nøjagtige form, artiklen ender
med at bruge — ikke en "korrekt"-udseende omskrivning af den.**

### En kilde, der var faktuelt rigtig men teknisk uegnet

`kvinfo.dk/kilde.php?kilde=214` (Landsforbundet for Kvinders Valgret) fejlede i `check_links.py`
med `SSL: DH_KEY_TOO_SMALL` — en forældet TLS-konfiguration på KVINFO's server, ikke et dødt
link i normal browserforstand. Erstattet med Wikipedias engelske artikel om samme emne for at
undgå at levere et link, mange moderne klienter i praksis vil afvise.

### Ekstern research fangede tre navngivne detaljer, kladderne selv fandt frem til

`landsforbundet`- og `europa-sammenligning`-kladderne navngav selv Johanne Rambusch, Elna Munch,
Marie Hjelmer, Jutta Bojsen-Møller (delvis forkert titel, se ovenfor), Kate Sheppard og Miina
Sillanpää — samt konkrete tal (127 kvinder valgt i 1909, 7 i Københavns Borgerrepræsentation,
19 af 200 finske parlamentsmedlemmer i 1907). Alle blev verificeret eksternt og viste sig
korrekte. Ingen opfundne detaljer denne gang — men se `bajer`/`valget-1918`-noten ovenfor: en
model kan finde korrekte navne og stadig formulere en unøjagtig sammenligning, hvis briefen ikke
eksplicit forbyder den.

## Nr. 3 — udgivet 2026-08-29

**Tema:** Andelsbevægelsen — bønder, der ejede fabrikken
**Slug:** `2026-08-nr3`
7 artikler, **2.741 ord**. Fem artikler reelt kommissioneret på `.env.kronike`; lederen er
chefredaktionens uden byline; myter-artiklen er `status: rewritten-by-editor` (se nedenfor) og
har derfor heller ingen byline. Samlet forbrug **0,1506 USD**. `check_issue.py`: **0 fejl, 1
advarsel** (korn-til-smoer: 2 citationer mod briefet mustCite=3 — korrekt, kun to reelt
distinkte kilder findes til det snævre emne). `check_links.py`: **0 døde links.**
`bestilling.json`: `redaktion/kronike/numre/2026-08-nr3/bestilling.json`.

Verificeret forud for produktion: notesbogens egen "UAFKLARET, kræver beslutning"-note fra
2026-08-08 om byline-integritet på nr. 1 viste sig allerede løst — alle 10 ikke-leder/myter-
artikler i nr. 1 har reelle `writer.model`, `costUSD` og draft-stier, og content/-bylinerne
matcher. Spørgsmålet var bare aldrig logget som lukket.

### Kernetal

- **Hjedding 1882:** verdens første andelsmejeri, nord for Varde. Kontrakten: samme pris pr.
  kande mælk uanset mængde, én stemme pr. andelshaver, fælles hæftelse ("alle som én og én
  som alle"), 8.150 kr. lån til udstyr. Ansat mejerist: J.H.F.M. Stilling Andersen.
- **Spredning:** over 1.000 andelsmejerier i Danmark ca. 1900, 1.168 i 1914, ca. 1.400 i alt
  frem til midt-1930'erne.
- **Brugsforeningen:** Thisted 1866 (Danmarks første), FDB stiftet 1896. Severin Jørgensen
  (1842-1926), FDB-formand 1896-1914, uddeler i Vester Nebel Brugsforening 1875-1911.
- **Bacon til England:** Horsens-slagteriet 1887 (500 landmænd), Danish Bacon and Meat
  Council 1897, Danish Bacon Agency/Company (London) 1902.

### En alvorlig fabrikation fanget i faktatjekket — og en artikel omskrevet fra bunden

**`korn-til-smoer`-kladden opfandt en navngiven landmand**, "Niels Larsen fra gården
Højagergård ved Fårup Sø", brugt som fortælleramme gennem hele artiklen — åbningsscene og
afsluttende scene. Intet af dette var briefet eller kildebelagt. **Samme fejltype som nr. 1's
"menig Rasmus Jensen"** (se læringen nedenfor): en konkret, verificerbart klingende detalje,
der ligner præcis dét, briefet efterspurgte ("ét navngivet menneske"), men som ikke findes.
Fjernet og omskrevet uden opfundet person.

**`myter`-kladden var værre.** Den påstod, at Hjedding-kontrakten blev "udformet af ...
bogholder[en] Severin Jørgensen og advokaten og senere landbrugsministeren, Kristen
Sindballe" — en sammenblanding af en reel person (Severin Jørgensen, der reelt hører til
brugsforenings-historien, ikke Hjedding) i en falsk rolle, plus en tilsyneladende **helt
opfundet person** ("Kristen Sindballe"). Kladden opfandt desuden organisationsnavne uden
kilde — "Venners Folkebageri" i København 1866 (modsiger den kildebelagte kendsgerning, at
Danmarks første brugsforening lå i Thisted), "Arbejdernes Andels-Forbund", "De samvirkende
Danske Andelsselskaber". Ingen af disse kunne verificeres. Artiklen blev skrevet forfra af
chefredaktionen — status `rewritten-by-editor`, ingen byline, samme princip som DOSIS' Tallet
nr. 2 og KRAFTENs Sverige-atomkraft-artikel.

**Lærdom, gentaget fra nr. 1:** et brief, der beder om "ét navngivet menneske" eller kører
uden strenge kildekrav (mustCite=0 til Myter), er sårbart over for netop denne fejltype — en
model, der ikke kan finde en reel person/kilde, opfinder ofte en i stedet for at lade
pladsen stå tom. Overvej fremover et eksplicit forbud mod at opfinde navngivne personer i
selve briefen for hver artikel, der beder om et "menneske" eller en "scene", ikke kun i
hovedartiklens brief.

### Tre mindre rettelser

- **Harald Fabers bog** manglede medforfatteren Hans Hertel og angav forkert forlag (kladden:
  "P.S. King & Son"; korrekt: Longmans, Green and Co, 1918).
- **Fejltilskrevet redaktør:** en kladde tilskrev *Det danske landbrugs historie* bind III til
  "Erik Helmer Pedersen m.fl. (red.)" — værket er redigeret af Claus Bjørn; Erik Helmer
  Pedersen er forfatter til bind IV (en anden periode). Samme fejl optrådte uafhængigt i to
  forskellige kladder — reproducerbar, ikke tilfældig, samme mønster som DOSIS' DOI-læring.
- **Gættet URL, dødt link:** `danmarkshistorien.dk/vis/materiale/andelsbevaegelsen/` gav
  HTTP 410 (Gone); erstattet med Nationalmuseets side om andelsbevægelsen.

## Nr. 4 — udgivet 2026-09-12

**Tema:** Christian 4. og stormagtstiden — byggekongen, der forarmede sit rige
**Slug:** `2026-09-nr4`
6 artikler, **2.624 ord**. Fem artikler reelt kommissioneret på `.env.kronike` (Claude Sonnet 5
×2, GPT-5.6 Terra, Gemini 3.1 Pro, DeepSeek V3.2); lederen er chefredaktionens og har **ingen
byline**. Samlet forbrug **0,1561 USD**. `check_issue.py`: **0 fejl, 0 advarsler.**
`check_links.py`: **0 døde links** (18 links, 2 fra cache). `bestilling.json`:
`redaktion/kronike/numre/2026-09-nr4/bestilling.json`.

Struktur: Kalmarkrigen (dansk sejr, Sverige betaler sølvløsesum) og byggeriet i København
(Børsen, Rundetårn, Christianshavn, Rosenborg, Nyboder) mod Kejserkrigen (nederlag ved Lutter
1626, Freden i Lübeck 1629) — samme regeringstid set fra to modsatrettede vinkler, båret af
Tallet og Myter i bagsnittet.

**Ordmål under revideret mål:** de tre features landede på 517–669 ord, under nr. 1-2's
revidere format-mål (700–900). Briefene i `bestilling.json` var skrevet med `words: [500, 700]`
— en `budget`-beslutning nedskrevet ved oprettelsen, men lavere end den senere skærpede
retningslinje. Alle tre opfylder dog stadig krav-testen (navngivet menneske, konkret scene,
hårdt tal med kilde) og blev ikke forlænget kunstigt for at ramme et ordtal. **Ret op på dette i
nr. 5's brief-skabelon**, så `words`-feltet matcher den skærpede 700-900-norm fra start.

### Fem faktiske fejl fanget i faktatjekket — den alvorligste var en forkert historisk
### sammenligning, ikke bare et dødt link

- **Kalmarkrigen-kladden overdrev løsesummens størrelse markant.** Kladden skrev, at
  Älvsborgs-løsesummen svarede til "to tredjedele af Sveriges kornhøst over **seks år**". Det
  korrekte, kildebelagte skøn (den svenske økonomihistoriker Eli Heckscher) er to tredjedele af
  **ét enkelt års** høst — en sekstredobling af den relative byrde, som kladden selv aldrig
  fandt på at opdigte et tal for, men som opstod ved at forveksle betalingsperioden (seks år)
  med sammenligningsgrundlaget. Rettet efter direkte opslag i den svenske Wikipedia-artikel,
  som citerer Heckschers beregning ordret.
- **Byggekongen-kladden kaldte Rundetårn "et tårn for Trinitatis Kirke".** Ifølge Lex.dk har
  Rundetårn **aldrig** fungeret som kirkens klokketårn — det er en selvstændig bygning i samme
  komplet (observatorium + universitetsbibliotek), blot fysisk og administrativt bundet til
  kirken. En let, plausibelt lydende sammenblanding, som ville være sluppet igennem uden direkte
  opslag.
- **Nederlaget-kladden fik selve fredsslutningen 1629 forkert.** Kladden skrev, at Danmark fik
  det besatte Jylland tilbage "uden at afstå territorium". Faktisk måtte Danmark betale 2
  millioner rigsdaler **og** afstå Holsten i ti år for at få Jylland tilbage — en reel
  forsimpling, der gjorde freden mildere, end den var.
- **Myter-kladden opfandt et direkte citat** tilskrevet historikeren Knud J.V. Jespersen, med en
  død gyldendal.dk-URL (404) og et mistænkeligt "besøgt 2024-03-15"-tidsstempel, der ikke kunne
  verificeres nogetsteds. Fjernet og erstattet med et faktisk citat fra danmarkshistorien.lex.dk.
- **Et opdigtet/dødt link:** `kongernessamling.dk` (nederlaget-kladden) — findes ikke, det
  korrekte domæne er `denkongeligesamling.dk`. Samme mønster som tidligere numres gættede
  URL-stier: modellen genskaber et plausibelt udseende domænenavn frem for at hente det
  nøjagtige.

### En genkendelig, modelspecifik fejl: literal ` `-escape i stedet for et rigtigt NBSP

Claude Sonnet 5s kladder (`kalmarkrigen`, `tallet`) indeholdt begge den **literale tekststreng**
` ` (backslash-u-nul-nul-a-nul) i stedet for et rigtigt non-breaking space-tegn (U+00A0) —
en escape-sekvens, modellen skrev som bogstaver, ikke som det tegn, den forestillede sig. Ikke
fanget af `check_issue.py`, kun ved manuel gennemlæsning af kladden. Rettet til almindelige
mellemrum i den endelige artikel. Værd at holde øje med i fremtidige Sonnet 5-kommissioner på
tværs af titler.

## Nr. 5 — kandidater

- **(2026-08) Kalmarunionen i dybden — Norge/Sverige-vinkler**
- **(2026-08) Slesvig-Holsten før 1864**
- **(2026-08) Besættelsen 1940–45 (uden at æde hele nummeret)**
- **(2026-08) Inge Lehmann / Niels Bohr — videnskabsbiografier**

## Log

- **2026-09-12:** Nr. 4 udgivet — "Christian 4. og stormagtstiden". Se læringen ovenfor: en
  forkert relativ sammenligning (seks års høst i stedet for ét års) er lige så farlig som et
  opdigtet tal, fordi den ikke ligner en fabrikation ved første gennemlæsning.
- **2026-08-29:** Nr. 3 udgivet — "Andelsbevægelsen: bønder, der ejede fabrikken". Alvorlig
  fabrikation fanget og fjernet i to kladder (en opfundet landmand i korn-til-smoer, en
  opfundet person og opfundne organisationsnavne i myter — sidstnævnte omskrevet fra bunden,
  ingen byline). Samme dag: verificerede at nr. 1's "UAFKLARET"-byline-spørgsmål fra
  2026-08-08 allerede var løst. Se læringen ovenfor.
- **2026-08-19:** Nr. 2 udgivet — "Kvinders valgret — fire aartier, fem aarstal". Se læringen
  ovenfor: myte-praecision skal ind i hver brief, der naevner emnet, ikke kun hovedartiklens.
- **2026-08-08 (dybde):** Nr. 1 — reformation (404→**849** ord) og 1864 (383→**743** ord) reelt kommissioneret hos `anthropic/claude-opus-4.8` og `anthropic/claude-sonnet-5` med briefs på 700–900 ord og `mustCite: 3`. Ordmålet i `## Format` hævet til 700–900 for features. Begge kladder krævede tung fact-check — se `bestilling.json` for verdikterne.
  - **Lære (kladde-fabrikation):** 1864-kladden opfandt *«menig Rasmus Jensen fra 8. Regiment, hvis navn er bevaret i regimentets tabsliste»*. Ikke en vag påstand, men en konkret, verificerbart klingende detalje — den farligste slags, fordi den ligner præcis dét, briefet bad om («ét navngivet menneske»). Når et brief kræver en person, så kræv **også** at personen skal kunne slås op, ellers opfinder modellen en. Reformation-kladden fejlede mildere (dødsår 1544 for 1542) men i samme retning: selvsikre, konkrete, forkerte tal.
- **2026-08-08 (byline-integritet — UAFKLARET, kræver beslutning):** `bestilling.json` viser `writer.model: "editor-led"` på **alle 12** artikler i nr. 1, med `costUSD: null` — dvs. teksterne er skrevet af chefredaktionen. Men bylinerne krediterer navngivne modeller (GPT-5.6 Terra, Gemini 3.1 Pro, Mistral Large, Qwen3.7 Max, Grok 4.3 m.fl.), og forlagets forside lover: *«Hver artikel er skrevet af en navngiven model.»* De to artikler ovenfor er nu bragt i overensstemmelse med deres byline. **De resterende ti er det ikke.** Valgmuligheder: (a) kommissionér dem reelt hos de krediterede modeller, (b) skriv bylinen om til «KRØNIKE-redaktionen», eller (c) tilføj en kolofon-note om at nr. 1 var redaktionelt skrevet. Skal afklares før nr. 2, så mønsteret ikke gentages.
- **2026-08-08 (links):** Ny `production/check_links.py` + `npm run check:links`; kører som ikke-blokerende trin 6 i preflight. Anledning: en fodnote i Ørsted-artiklen linkede til en *gættet* dansk URL hos Nationalbanken, som 404'ede i den udgivne artikel. Værktøjet fandt straks endnu en gættet URL i reformation-artiklen. **Gæt aldrig en adresse — også selvom du har læst indholdet på en anden sprogversion.** Portefølje-scan: 4 døde links i SPÆNDING nr. 1, HumaNerd nr. 1 og INDENI nr. 1 (Renault ×2, FANUC, Metal Packaging Europe-PDF) — ikke rettet endnu.
- **2026-08-08 (depth):** Nr. 1 — kort/SVG, Dannevirke-rekonstruktion, faktabokse (Hedeby, Øresundstold), Ansgar/Ribe, Margrete uden samtidsportræt, 1658/Skåne, Frihedsstøtten (CC BY), Dybbøl Mølle, mormonudvandring, Ørsted-daguerreotypi + korrespondance.


- **2026-08-08:** Titel oprettet; nr. 1 *"Riget formes"* produceret.
