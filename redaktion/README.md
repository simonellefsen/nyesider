# Redaktionen · Nye Sider

Redaktionel hukommelse for forlaget. Chefredaktør-agenten læser og opdaterer disse filer ved hver produktion.

## ⛔ Byline-reglen (indført 2026-08-08 efter afpublicering af 17 numre)

**En byline er en påstand om, hvem der har skrevet teksten. Den skal være sand.**

Den 8. august 2026 blev **191 artikler i 17 numre** rullet tilbage til `status: draft`. De var
udgivet med byline til navngivne modeller, men `bestilling.json` havde hverken `costUSD`,
`receipt.draft` eller kladdefil for en eneste af dem — og OpenRouter-forbruget viste, at flere
af titlernes nøgler (KulturBoxen, Orbit, Kraften) **aldrig havde været kaldt**. Verdikterne
(`accepted`, `rejected`) beskrev bedømmelser af kladder, der aldrig var modtaget.

Derfor gælder nu, uden undtagelse:

| Hvem skrev teksten? | `writer.model` | Byline | `receipt` |
|---|---|---|---|
| En model via OpenRouter | modellens id, fx `anthropic/claude-sonnet-5` | modellens navn | `costUSD` + `draft` **skal** være udfyldt |
| Chefredaktionen | `"editor-led"` | **ingen byline** | `costUSD: null`, `draft: null` |

- **Ingen kladde = intet verdikt.** `verdict.status` må først skrives, når der ligger en rigtig
  kladde i `kladder/`. At skrive `rejected` om noget, der aldrig er bestilt, er ikke sjusk —
  det er et opdigtet revisionsspor.
- **Genudgivelses-standarden aftalt med ejeren er: ingen byline, *indtil* en reel forfatter kan
  dokumenteres.** Sæt hellere ingen byline end en, du håber er rigtig.

  > **Læs «indtil» som det, der står — det er en betingelse, ikke et permanent forbud.**
  > Reglen er tosidet, og begge sider er lige forpligtende. Da de fem `2026-08-nr1`-numre var
  > genopbygget med rigtige kald, kvitteringer, `generationId` og kladder, blev de alligevel
  > udgivet **uden** byline, fordi «ingen byline» var blevet læst som selve standarden.
  > Ejeren opdagede det på de udgivne sider: fire modeller stod på OpenRouter-dashboardet med
  > 0,61 USD forbrug på KulturBoxen alene, og ingen artikel krediterede nogen af dem. Rettet
  > 2026-08-09, hvor 56 artikler fik den byline, kvitteringen hele tiden havde belagt.
  >
  > At tilbageholde en dokumenteret byline er sin egen unøjagtighed: den fratager forfatteren
  > arbejdet og skjuler for læseren, hvad der faktisk producerede teksten. Den ærlige regel er
  > **byline ⇔ kvittering** — i begge retninger.

- **En byline skal navngive præcis den model, der kørte.** `google/gemini-3.1-pro-preview` er et
  andet model-id end `google/gemini-3.1-pro` og har derfor sin egen post i `modeller.json`.
  Vælg aldrig den nærmeste slægtning i kartoteket, fordi den rigtige mangler — opret posten.
- **Brug titlens egen nøgle.** `.env.<slug>` — aldrig en anden titels. Det var netop
  dashboardet med de urørte nøgler, der afslørede sagen.

## En kilde, der svarer, er ikke en kilde, der passer

Tilføjet 2026-08-09 efter genopbygningen af de syv nr. 1-numre. **Statuskoden beviser, at noget
findes på adressen. Den beviser ikke, at det er det, fodnoten påstår.** Tre gange fandt vi det samme:

- **Gættede websider svarer 200 med forkert indhold.** `geostat.ge/…/768/2024-population-census`
  serverer kriminalstatistik for juli 2022; `…/322/inbound-visitors-statistics` serverer
  migrationsdata; `ifr.org/…/robot-density-by-country-2024` serverer en pressemeddelelse om
  FCC-restriktioner. CMS-drevne sites svarer ofte på id'et og ignorerer sluggen. **Åbn siden og læs.**
- **DOI'er opløses korrekt til det forkerte arbejde.** I ét nummer var to ud af fire DOI'er forkerte
  — én anført som en klinisk ernæringsretningslinje opløste til en artikel om kystklitter i et
  geovidenskabeligt tidsskrift. `check_links.py` godkender dem alle.

  ```bash
  curl -sL -H "Accept: application/vnd.citationstyles.csl+json" https://doi.org/<DOI>
  ```

  Læs `title` og `container-title` og hold dem op mod fodnoten. Ti sekunder pr. reference.
- **Delvist rigtige referencer er farligst.** Rigtig forfatter, rigtigt år, rigtigt emne — forkert
  titel og tidsskrift. Kontrollér bind, nummer og side, ikke kun at forfatteren findes.

Modellerne leverer også *korrekte* referencer uopfordret — Hosford & Duncan, Goldstein, PROT-AGE,
VITAL og to Venedigkommission-numre var alle rigtige. Kildekontrol er ikke mistillid. Det er den
eneste måde at skelne dem fra hinanden.

De afpublicerede numre bærer hver især `unpublishedReason` i deres `issue.json`. **Sæt dem ikke
tilbage til `published` uden at have produceret dem rigtigt.**

## Struktur

- **[modelkartotek.md](modelkartotek.md)** — fælles erfaringer med OpenRouter-modeller (skribenter og billedmodeller) på tværs af alle titler. Læs før casting af nye numre; opdater efter hver produktion.
- **`<titel>/redaktionsnotesbog.md`** — pr. magasin: historier i støbeskeen, opfølgninger, idébank, faste formater og titelspecifik praktik. Grundlag for næste nummer.
- **`<titel>/numre/<issue-slug>/bestilling.json`** — pr. nummer: det skrevne brief til hver skribent og chefredaktørens verdikt på hver artikel. Se [bestilling.schema.md](bestilling.schema.md). Dette er kontraktens **anden halvdel** — uden den overlever kun det færdige resultat, aldrig hvad der blev bedt om.

## Arbejdsgang for et nyt nummer

1. Læs titlens `redaktionsnotesbog.md` (leads/opfølgninger) og `modelkartotek.md` (casting).
2. **Nøgler (obligatorisk adskillelse):**
   - **OpenRouter-tekst:** kun `.env.<slug>` for den titel, der produceres (fx `.env.kraften`). Aldrig en anden titels fil — cost tracking i OpenRouter-dashboardet afhænger af det.
   - **Imagine-billeder:** `XAI_API_KEY` i **`.env.local`** (fælles for forlaget).
   - Hjælper: `python production/load_env.py <slug>` (loader begge; printer kun filstier, aldrig hemmeligheder).
3. **Skriv briefet, så bestil.** Før du kaster en opgave til en skribentmodel, opret (eller udvid) `redaktion/<titel>/numre/<issue-slug>/bestilling.json` — se [bestilling.schema.md](bestilling.schema.md). Hver `opgave` skal som minimum have `brief.angle`, `brief.words` og `brief.mustCite`, **før** du sender prompten. `mustCite` er en bevidst beslutning, ikke en eftertanke: `0` er lovligt og almindeligt (leder, ordbog, rygtebørs, førstepersonsanekdote), men det skal skrives ned som `0`, ikke bare udelades.
   - **Sourcing hører hjemme i briefet, ikke kun i godkendelsen.** Det er den enkelte lære fra denne fil, der har haft størst konsekvens: da kildekravet kun stod i fact-check-tjeklisten (trin 4 nedenfor), var det for sent at rette, når artiklen landede — så det blev sjældent gjort. To hele titler blev udgivet med 0 % kildedækning, fordi ingen skribent nogensinde blev bedt om en kilde. Fortæl skribenten `mustCite`-tallet og eventuelle `mustNumber`-krav direkte i prompten, sammen med `words`-intervallet.
   - Skriv én artikel ad gangen (sandboxens shell-kald har typisk et loft på ~45 sek.). Brug `production/commission.py <titel> <issue-slug> <artikel-slug>` når det findes (se `production/README` eller scriptets docstring) — det virker som et rent transportlag: det henter, tæller ord/kilder og pris, og skriver kladden til `kladder/`, men **kan ikke selv skrive til `content/`**. Du læser stadig hele udkastet, og du skriver stadig selv den godkendte fil.
4. **Fact-check & accept (chefredaktør — obligatorisk før publicering):**  
   Ingen artikel går i `content/…` som færdige/publiceret, før chefredaktøren har gennemgået den. Minimum:
   - **Færdig læsertekst — ikke kladde, brief eller redaktionsnote.** Læs artiklen som en abonnent uden forudgående brief. Hvis den lyder som instruks til skribenten (“Brug X som primærkilde”, “Citér dato og status”, “Skeln konsekvent mellem…”), en punktopstilling af *hvad der mangler*, et TODO/FIXME/TBD, eller en notesbog der endnu ikke er skrevet om til magasinprosa, er den **ikke accepteret**. Omskriv eller afvis — parkér i `kladder/` eller `redaktion/<slug>/parked/`, aldrig i `content/` under `status: published`. Negativt eksempel: KRAFTEN nr. 2’s første Sverige-atom-version (intern tjekliste efter Rygtebørsen). Positivt: den omskrevne feature *før* bagsnittene.
   - **Jargon & forkortelser første gang — pr. artikel, ikke pr. nummer:** antag ikke, at læseren husker nr. 1, har læst lederen, eller arbejder i branchen. Hver artikel kan åbnes alene via URL/RSS. Første gang i *denne* artikel: fuldt navn + kort dansk forklaring (fx LEO = lav jordbane / *low Earth orbit*; NASA HLS = *Human Landing System*; FCC, FAA, Fit for 55, IRA, PJM). Hvis udfoldelsen tynger brødteksten, brug en **fodnote** — hellere en lille note end en uforklaret forkortelse. Gælder også “kendte” labels.
   - **Fakta:** tal, årstal, stednavne, institutioner, priser og “første gang”-påstande tjekkes mod troværdige kilder (officiel statistik, primære sitet, seriøs journalistik). Opdigt ikke præcise datoer for virkelige begivenheder.
   - **Hårde tal er et krav, ikke en bonus:** hvor en artikel *kan* underbygges med et konkret tal (absolut antal, procent, kr., år, g/kg osv.), skal den. Vage formuleringer som “en betydelig andel”, “mange danskere” eller “stiger markant” sendes tilbage til skribenten, medmindre chefredaktøren selv kan finde og indsætte det præcise tal med kilde. Afrundede pejlemærker er kun acceptable, når et præcist tal reelt ikke findes (mærk dem da eksplicit som ballpark) — ikke fordi ingen gad slå det op. Se DOSIS' `11-tallet.md` (august 2026) som skabelon: tabel med tal + år + fodnote pr. celle.
   - **Kilder:** fodnoter/`[^n]` skal pege på reelle, gerne klikbare kilder, hvor det er muligt; afrundede pejlemærker skal være ærligt mærket som sådan.
   - **Verificér hver URL, før den går i trykken — gæt aldrig en adresse.** Konkret fejl (KRØNIKE nr. 1, august 2026): en fodnote linkede til Nationalbankens *danske* side om historiske sedler, hvor stien var oversat fra den engelske URL i hånden. Siden fandtes ikke; fodnoten 404'ede i den udgivne artikel. At have læst indholdet på den engelske side gør ikke den danske adresse rigtig. Kør `npm run check:links` (eller `python3 production/check_links.py <slug> <issue-slug>`) før accept — den henter hver adresse og skelner mellem *død* (404/410, skal rettes) og *bot-blokeret* (403/406/429, typisk fin i en browser). Den kører også som sidste, **ikke-blokerende** trin i `npm run preflight`; at den ikke blokerer er ikke en invitation til at ignorere den.
   - **Sprog & husregler:** dansk, forkortelser første gang, nbsp før `%`, ingen engelsk teen/jargon uden forklaring.
   - **Vinkel & rækkefølge:** passer til titlens identitet (fx HORISONTEN ≠ KULTURBOXEN); krydslink kun hvor det hjælper. Features hører **før** bagsnit (Rygtebørs, Sladder, Myter) — en feature efter Rygtebørsen er et ordensfejl, der ofte signalerer “sent indsat kladde”.
   - **Ret eller afvis:** ret faktafejl, stram vage påstande, omskriv kladder, eller send tilbage til skribent. Først derefter: accept → commit til nummeret.
   - **Skriv verdikten ned:** udfyld `verdict.status` (`accepted` / `accepted-after-edit` / `rewritten-by-editor` / `rejected` / `fallback-used`), `citations` (talt fodnote-antal) og en kort `editorNote` i den tilhørende `opgave` i `bestilling.json`. Uden dette felt findes der intet sted, der viser, at en artikel faktisk blev gennemgået — kun at nummeret endte med `"status": "published"`. Ved omskrivning fra kladde: `rewritten-by-editor` + én sætning om hvorfor.
5. Læg godkendt output i `content/<titel>/issues/<YYYY-MM-nrN>/` (artikler, billeder, `issue.json`, PDF). Kør `production/check_issue.py <titel> <issue-slug>` — det er hurtigt (sekunder) og fanger det, der ellers glider stille igennem: manglende billedfiler, filnavne-præfiks der ikke matcher `order`, ubrugte/manglende fodnoter, brudt `[CHART]`-reference, **og draft-/redaktionsnote-stemme i brødteksten**. Fejl her bør rettes før udgivelse; advarsler (fx manglende `standfirst`) er redaktionelle valg, ikke blokerende.
5b. **Før push / “færdig session”:** kør `npm run preflight` fra repo-roden (eller lad git `pre-push`-hooket gøre det). Den suite er: katalog-fejl for *alle* numre → `svelte-check` → unit tests → fuld `web`-build (samme som Vercel). Et rødt Vercel-build, der kunne have været fanget her, er en procesfejl.
5c. **Udgivelsesdato — én pr. magasin pr. dag:** Sæt `published` i `issue.json` til `YYYY-MM-DD`. **Højst ét `status: published`-nummer pr. titel pr. kalenderdag.** Flere magasiner må gerne udkomme samme dag (uge-batch); to DOSIS-numre på `2026-08-08` må ikke. Før du låser datoen: kig i [udgivelseskalender.md](udgivelseskalender.md) eller kør `python3 production/udgivelseskalender.py --check`. Ved batch under tidspres: næste ledige dag for *den* titel (ofte +7 dage), ikke “i dag igen”. `check_issue.py` giver **ERROR** ved kollision.
5d. **Hold et nummer tilbage til næste uge:** Behold mappen under `content/<slug>/issues/…`, sæt `status: "scheduled"` (eller `draft`) og den planlagte `published`-dato. Websitet lister og prerenderer **kun** `status: published` — så nummeret er usynligt for læsere, men klar til at flippe til `published` når ugen kommer.
6. Notér produktionsomkostningen i nummerets `issue.json` (`productionCostUSD`). Summér `receipt.costUSD` på tværs af nummerets `opgaver` i `bestilling.json` — `production/commission.py --sum <titel> <issue-slug>` gør det for dig, når scriptet findes.
7. Opdater notesbogen: afvikl brugte leads, tilføj nye **med datostempel** (`(2026-08)`), og notér løfter givet i det trykte nummer.
8. Modelkartoteket opdaterer sig selv — `production/modelstats.py` afleder statistikken fra alle titlers `bestilling.json`-filer, når det findes. Tilføj kun kvalitative, daterede observationer med hånd (se `modelkartotek.md`'s egen struktur).

## Hemmeligheder (kort)

| Formål | Fil | Variabel |
|---|---|---|
| OpenRouter pr. magasin | `.env.gnisten`, `.env.pulsen`, `.env.dosis`, `.env.spaending`, `.env.horisonten`, `.env.kulturboxen`, `.env.kraften`, `.env.orbit`, `.env.kronike` | `OPENROUTER_API_KEY` |
| xAI Imagine (billeder) | `.env.local` | `XAI_API_KEY` |

Skabelon: [`.env.example`](../.env.example). Alle `.env*` er gitignored. Webappen bruger **ingen** af nøglerne.

## Billeder (copyright-politik)

**Standard: generér selv via xAI Imagine** med `XAI_API_KEY` fra `.env.local` (Grok Build `image_gen` / Imagine API). Undgår stock- og pressefoto-copyright. Brug `production/generate_image.py` (se `--list-styles`) — den holder styr på stilkatalog og husregler i prompten.

- **Varier stilart bevidst — fotorealisme er ét valg blandt mange, ikke standarden.** Skribenter og chefredaktør skal aktivt overveje [The Noun Project's 17 grafiske designstile](https://blog.thenounproject.com/graphic-design-styles/) (minimalisme, maksimalisme, typografisk, retro, abstrakt, geometrisk, flad vektor, 3D, organisk, moderne, corporate, illustreret, legende, feminin, maskulin, grunge, fotorealisme) og vælge den stil, der passer *emnet* i den enkelte artikel — fx flad vektor til et enkelt sammenligningsmotiv, maksimalisme til en overvældende "jungle" af valgmuligheder, geometrisk til et data-tungt "Tallet". Et helt nummer i samme fotorealistiske stil er en smagsfejl, ikke et neutralt valg.
- Prompt: motiver uden logoer, uden læsbar skiltetekst; stil tilpasset både titlen og den enkelte artikels emne (se ovenfor).
- Kreditering: `imageCredit` + `imageSource` (typisk Imagine / xAI → `https://x.ai/`) under figuren, gerne med stilnavn i parentes (fx "— retrostil"); cover: `coverCredit` + `coverSource`; samlet `imageCredits` + `images/SOURCES.md` i nummeret (inkl. stilart pr. billede).
- **Bagsnit må dele billeder.** Rygtebørsen, sladder, myter og lignende korte bagsnit behøver ikke unikke motiver — genbrug ét fælles bagsnit-billede (eller to) inden for nummeret. Features, Tallet og forsiden skal stadig have egne, emnespecifikke billeder. Skriv gerne i `images/SOURCES.md`, at bagsnit deler fil.
- **Træk ikke** billeder fra nettet, Google Images, Wikipedia eller agency feeds uden eksplicit licens og kilde-URL.
- Undtagelse: egenproducerede diagrammer/SVG (fx GNISTEN) og materiale med dokumenteret fri/egen licens.
- **Gemini/OpenRouter-billeder** kun som fallback — og så på **titlens egen** OpenRouter-nøgle (`.env.<slug>`), så billedforbrug også kan spores pr. magasin.

## Ny titel

Opret `redaktion/<slug>/redaktionsnotesbog.md` og `content/<slug>/magazine.json` (brand, farver, sektioner, målgruppe).

## Sprog & typografi (husregler)

1. **Procent:** Dansk form med mellemrum før `%`, men brug **ikke-brydende mellemrum** (U+00A0), så tal og tegn ikke skilles ved linjeskift.  
   Skriv: `30\u00a0%` → vises som «30 %».  
   Undgå almindeligt mellemrum: `30 %` (kan give `30` på én linje og `%` på næste).

2. **Forkortelser:** Antag ikke, at læseren kender dem — heller ikke at de husker dem fra et andet nummer eller en anden artikel. **Første gang i hver artikel:** fuldt navn + forkortelse (og gerne dansk gloss), derefter forkortelsen frit i *samme* artikel. Layout-flugt: forklar i **fodnote**.  
   Eksempler:  
   - lav jordbane / **LEO** (*low Earth orbit*)  
   - den europæiske rumorganisation **ESA** (*European Space Agency*)  
   - **NASA** (*National Aeronautics and Space Administration*); **HLS** (*Human Landing System*)  
   - **FAA** (*Federal Aviation Administration*); **FCC** (*Federal Communications Commission*)  
   - det Internationale Energiagentur (IEA); WLTP; LCOE  
   Meget kendte geografiske navne (EU, USA) kan stå alene. Agenturer og baneklasser (NASA, ESA, LEO, MEO, GEO) skal udfoldes mindst én gang pr. artikel (parentes eller fodnote). **Ordbogen er droppet** som bagsnit fra 2026-08-08 — forklar gloser i brødteksten, ikke i en separat ordliste. Chefredaktøren er ansvarlig — se trin 4.

3. **Diagrammer / tendenskurver:** Vis **gap mellem verdensøkonomier**. Standard er at lægge **EU, USA og Kina** side om side, plus relevante top performers (fx Norge for elbilandel). En dansk eller europæisk kurve alene fortæller for lidt — læseren skal se, hvem der fører, hvem der hænger, og hvor stort springet er. Se [content/CHARTS.md](../content/CHARTS.md).

4. **Krydsreferencer:** Når et emne overlapper et andet magasin eller et tidligere nummer (fx SPÆNDING↔KRAFTEN, ORBIT↔KRAFTEN, HORISONTEN↔KULTURBOXEN, «i nr. 1 skrev vi…»), sæt en **relativ intern link** i brødteksten: `/<slug>/<issue-slug>/<article-slug>` (fx `[KRAFTEN](/kraften/2026-08-nr1/leder)`). Ikke linkfarm — kun hvor læseren reelt har glæde af at hoppe.

5. **Fact-check før accept:** Se arbejdsgang trin 4. Chefredaktøren er ansvarlig for, at teamets artikler er faktatjekket — publicering uden den gennemgang er en procesfejl, ikke en stilpræference.

6. **HORISONTEN ↔ KULTURBOXEN — synk når det giver mening:**  
   De to titler er søskende (rejse vs. hverdag/kultur). Ved planlægning af nye numre: **prøv at matche land/region/tema**, så læseren kan hoppe mellem “hvordan kommer jeg derhen” og “hvordan lever folk dér” (som Georgien-parret i august 2026).  
   - **Ikke et krav hver gang** — nogle destinationer er rene ruter; nogle kulturer har ikke et naturligt rejseformat i samme kvartal.  
   - Når I synker: samme `published`-vindue hvis muligt, gensidige krydslinks, og en linje i begge notesbøger (*“Søster: …”*).  
   - Når I *ikke* synker: notér kort hvorfor i notesbogen, så det er et bevidst valg.
