# Redaktionen · Nye Sider

Redaktionel hukommelse for forlaget. Chefredaktør-agenten læser og opdaterer disse filer ved hver produktion.

## Struktur

- **[modelkartotek.md](modelkartotek.md)** — fælles erfaringer med OpenRouter-modeller (skribenter og billedmodeller) på tværs af alle titler. Læs før casting af nye numre; opdater efter hver produktion.
- **`<titel>/redaktionsnotesbog.md`** — pr. magasin: historier i støbeskeen, opfølgninger, idébank, faste formater og titelspecifik praktik. Grundlag for næste nummer.

## Arbejdsgang for et nyt nummer

1. Læs titlens `redaktionsnotesbog.md` (leads/opfølgninger) og `modelkartotek.md` (casting).
2. **Nøgler (obligatorisk adskillelse):**
   - **OpenRouter-tekst:** kun `.env.<slug>` for den titel, der produceres (fx `.env.kraften`). Aldrig en anden titels fil — cost tracking i OpenRouter-dashboardet afhænger af det.
   - **Imagine-billeder:** `XAI_API_KEY` i **`.env.local`** (fælles for forlaget).
   - Hjælper: `python production/load_env.py <slug>` (loader begge; printer kun filstier, aldrig hemmeligheder).
3. Cast og indhent artikler fra teamet (modeller / skribenter).
4. **Fact-check & accept (chefredaktør — obligatorisk før publicering):**  
   Ingen artikel går i `content/…` som færdige/publiceret, før chefredaktøren har gennemgået den. Minimum:
   - **Fakta:** tal, årstal, stednavne, institutioner, priser og “første gang”-påstande tjekkes mod troværdige kilder (officiel statistik, primære sitet, seriøs journalistik). Opdigt ikke præcise datoer for virkelige begivenheder.
   - **Kilder:** fodnoter/`[^n]` skal pege på reelle, gerne klikbare kilder, hvor det er muligt; afrundede pejlemærker skal være ærligt mærket som sådan.
   - **Sprog & husregler:** dansk, forkortelser første gang, nbsp før `%`, ingen engelsk teen/jargon uden forklaring.
   - **Vinkel:** passer til titlens identitet (fx HORISONTEN ≠ KULTURBOXEN); krydslink kun hvor det hjælper.
   - **Ret eller afvis:** ret faktafejl, stram vage påstande, eller send tilbage til skribent. Først derefter: accept → commit til nummeret.
5. Læg godkendt output i `content/<titel>/issues/<YYYY-MM-nrN>/` (artikler, billeder, `issue.json`, PDF).
6. Notér produktionsomkostningen i nummerets `issue.json` (`productionCostUSD`, gerne `text` / `images` breakdown).
7. Opdater notesbogen: afvikl brugte leads, tilføj nye, notér løfter givet i det trykte nummer.
8. Opdater modelkartoteket med nye modelerfaringer.

## Hemmeligheder (kort)

| Formål | Fil | Variabel |
|---|---|---|
| OpenRouter pr. magasin | `.env.gnisten`, `.env.pulsen`, `.env.spaending`, `.env.horisonten`, `.env.kulturboxen`, `.env.kraften`, `.env.orbit` | `OPENROUTER_API_KEY` |
| xAI Imagine (billeder) | `.env.local` | `XAI_API_KEY` |

Skabelon: [`.env.example`](../.env.example). Alle `.env*` er gitignored. Webappen bruger **ingen** af nøglerne.

## Billeder (copyright-politik)

**Standard: generér selv via xAI Imagine** med `XAI_API_KEY` fra `.env.local` (Grok Build `image_gen` / Imagine API). Undgår stock- og pressefoto-copyright.

- Prompt: motiver uden logoer, uden læsbar skiltetekst; stil tilpasset titlen (akvarel, editorial foto, osv.).
- Kreditering: `imageCredit` + `imageSource` (typisk Imagine / xAI → `https://x.ai/`) under figuren; cover: `coverCredit` + `coverSource`; samlet `imageCredits` + `images/SOURCES.md` i nummeret.
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
