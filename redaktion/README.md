# Redaktionen · Nye Sider

Redaktionel hukommelse for forlaget. Chefredaktør-agenten læser og opdaterer disse filer ved hver produktion.

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
   - **Fakta:** tal, årstal, stednavne, institutioner, priser og “første gang”-påstande tjekkes mod troværdige kilder (officiel statistik, primære sitet, seriøs journalistik). Opdigt ikke præcise datoer for virkelige begivenheder.
   - **Hårde tal er et krav, ikke en bonus:** hvor en artikel *kan* underbygges med et konkret tal (absolut antal, procent, kr., år, g/kg osv.), skal den. Vage formuleringer som “en betydelig andel”, “mange danskere” eller “stiger markant” sendes tilbage til skribenten, medmindre chefredaktøren selv kan finde og indsætte det præcise tal med kilde. Afrundede pejlemærker er kun acceptable, når et præcist tal reelt ikke findes (mærk dem da eksplicit som ballpark) — ikke fordi ingen gad slå det op. Se DOSIS' `11-tallet.md` (august 2026) som skabelon: tabel med tal + år + fodnote pr. celle.
   - **Kilder:** fodnoter/`[^n]` skal pege på reelle, gerne klikbare kilder, hvor det er muligt; afrundede pejlemærker skal være ærligt mærket som sådan.
   - **Sprog & husregler:** dansk, forkortelser første gang, nbsp før `%`, ingen engelsk teen/jargon uden forklaring.
   - **Vinkel:** passer til titlens identitet (fx HORISONTEN ≠ KULTURBOXEN); krydslink kun hvor det hjælper.
   - **Ret eller afvis:** ret faktafejl, stram vage påstande, eller send tilbage til skribent. Først derefter: accept → commit til nummeret.
   - **Skriv verdikten ned:** udfyld `verdict.status` (`accepted` / `accepted-after-edit` / `rewritten-by-editor` / `rejected` / `fallback-used`), `citations` (talt fodnote-antal) og en kort `editorNote` i den tilhørende `opgave` i `bestilling.json`. Uden dette felt findes der intet sted, der viser, at en artikel faktisk blev gennemgået — kun at nummeret endte med `"status": "published"`.
5. Læg godkendt output i `content/<titel>/issues/<YYYY-MM-nrN>/` (artikler, billeder, `issue.json`, PDF). Kør `production/check_issue.py <titel> <issue-slug>` — det er hurtigt (sekunder) og fanger det, der ellers glider stille igennem: manglende billedfiler, filnavne-præfiks der ikke matcher `order`, ubrugte/manglende fodnoter, brudt `[CHART]`-reference. Fejl her bør rettes før udgivelse; advarsler (fx manglende `standfirst`) er redaktionelle valg, ikke blokerende.
6. Notér produktionsomkostningen i nummerets `issue.json` (`productionCostUSD`). Summér `receipt.costUSD` på tværs af nummerets `opgaver` i `bestilling.json` — `production/commission.py --sum <titel> <issue-slug>` gør det for dig, når scriptet findes.
7. Opdater notesbogen: afvikl brugte leads, tilføj nye **med datostempel** (`(2026-08)`), og notér løfter givet i det trykte nummer.
8. Modelkartoteket opdaterer sig selv — `production/modelstats.py` afleder statistikken fra alle titlers `bestilling.json`-filer, når det findes. Tilføj kun kvalitative, daterede observationer med hånd (se `modelkartotek.md`'s egen struktur).

## Hemmeligheder (kort)

| Formål | Fil | Variabel |
|---|---|---|
| OpenRouter pr. magasin | `.env.gnisten`, `.env.pulsen`, `.env.dosis`, `.env.spaending`, `.env.horisonten`, `.env.kulturboxen`, `.env.kraften`, `.env.orbit` | `OPENROUTER_API_KEY` |
| xAI Imagine (billeder) | `.env.local` | `XAI_API_KEY` |

Skabelon: [`.env.example`](../.env.example). Alle `.env*` er gitignored. Webappen bruger **ingen** af nøglerne.

## Billeder (copyright-politik)

**Standard: generér selv via xAI Imagine** med `XAI_API_KEY` fra `.env.local` (Grok Build `image_gen` / Imagine API). Undgår stock- og pressefoto-copyright. Brug `production/generate_image.py` (se `--list-styles`) — den holder styr på stilkatalog og husregler i prompten.

- **Varier stilart bevidst — fotorealisme er ét valg blandt mange, ikke standarden.** Skribenter og chefredaktør skal aktivt overveje [The Noun Project's 17 grafiske designstile](https://blog.thenounproject.com/graphic-design-styles/) (minimalisme, maksimalisme, typografisk, retro, abstrakt, geometrisk, flad vektor, 3D, organisk, moderne, corporate, illustreret, legende, feminin, maskulin, grunge, fotorealisme) og vælge den stil, der passer *emnet* i den enkelte artikel — fx flad vektor til et enkelt sammenligningsmotiv, maksimalisme til en overvældende "jungle" af valgmuligheder, geometrisk til et data-tungt "Tallet". Et helt nummer i samme fotorealistiske stil er en smagsfejl, ikke et neutralt valg.
- Prompt: motiver uden logoer, uden læsbar skiltetekst; stil tilpasset både titlen og den enkelte artikels emne (se ovenfor).
- Kreditering: `imageCredit` + `imageSource` (typisk Imagine / xAI → `https://x.ai/`) under figuren, gerne med stilnavn i parentes (fx "— retrostil"); cover: `coverCredit` + `coverSource`; samlet `imageCredits` + `images/SOURCES.md` i nummeret (inkl. stilart pr. billede).
- **Træk ikke** billeder fra nettet, Google Images, Wikipedia eller agency feeds uden eksplicit licens og kilde-URL.
- Undtagelse: egenproducerede diagrammer/SVG (fx GNISTEN) og materiale med dokumenteret fri/egen licens.
- **Gemini/OpenRouter-billeder** kun som fallback — og så på **titlens egen** OpenRouter-nøgle (`.env.<slug>`), så billedforbrug også kan spores pr. magasin.

## Ny titel

Opret `redaktion/<slug>/redaktionsnotesbog.md` og `content/<slug>/magazine.json` (brand, farver, sektioner, målgruppe).

## Sprog & typografi (husregler)

1. **Procent:** Dansk form med mellemrum før `%`, men brug **ikke-brydende mellemrum** (U+00A0), så tal og tegn ikke skilles ved linjeskift.  
   Skriv: `30\u00a0%` → vises som «30 %».  
   Undgå almindeligt mellemrum: `30 %` (kan give `30` på én linje og `%` på næste).

2. **Forkortelser:** Antag ikke, at læseren kender dem. **Første gang** i en artikel: fuldt navn + forkortelse i parentes, derefter forkortelsen frit.  
   Eksempler:  
   - det Internationale Energiagentur (IEA)  
   - den europæiske rumorganisation ESA (*European Space Agency*)  
   - WLTP (*Worldwide Harmonised Light Vehicle Test Procedure*)  
   - LCOE (*levelized cost of energy*)  
   Meget kendte navne (NASA, EU, USA) kan stå alene, men det skader ikke at udfolde dem første gang i en leder eller intro.

3. **Diagrammer / tendenskurver:** Vis **gap mellem verdensøkonomier**. Standard er at lægge **EU, USA og Kina** side om side, plus relevante top performers (fx Norge for elbilandel). En dansk eller europæisk kurve alene fortæller for lidt — læseren skal se, hvem der fører, hvem der hænger, og hvor stort springet er. Se [content/CHARTS.md](../content/CHARTS.md).

4. **Krydsreferencer:** Når et emne overlapper et andet magasin eller et tidligere nummer (fx SPÆNDING↔KRAFTEN, ORBIT↔KRAFTEN, HORISONTEN↔KULTURBOXEN, «i nr. 1 skrev vi…»), sæt en **relativ intern link** i brødteksten: `/<slug>/<issue-slug>/<article-slug>` (fx `[KRAFTEN](/kraften/2026-08-nr1/leder)`). Ikke linkfarm — kun hvor læseren reelt har glæde af at hoppe.

5. **Fact-check før accept:** Se arbejdsgang trin 4. Chefredaktøren er ansvarlig for, at teamets artikler er faktatjekket — publicering uden den gennemgang er en procesfejl, ikke en stilpræference.

6. **HORISONTEN ↔ KULTURBOXEN — synk når det giver mening:**  
   De to titler er søskende (rejse vs. hverdag/kultur). Ved planlægning af nye numre: **prøv at matche land/region/tema**, så læseren kan hoppe mellem “hvordan kommer jeg derhen” og “hvordan lever folk dér” (som Georgien-parret i august 2026).  
   - **Ikke et krav hver gang** — nogle destinationer er rene ruter; nogle kulturer har ikke et naturligt rejseformat i samme kvartal.  
   - Når I synker: samme `published`-vindue hvis muligt, gensidige krydslinks, og en linje i begge notesbøger (*“Søster: …”*).  
   - Når I *ikke* synker: notér kort hvorfor i notesbogen, så det er et bevidst valg.
