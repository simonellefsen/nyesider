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
3. Producér nummeret; læg output i `content/<titel>/issues/<YYYY-MM-nrN>/` (artikler som markdown, billeder, `issue.json`, PDF).
4. Notér produktionsomkostningen i nummerets `issue.json` (`productionCostUSD`, gerne `text` / `images` breakdown). OpenRouter-forbrug = den titels nøgle; Imagine = xAI-dashboard.
5. Opdater notesbogen: afvikl brugte leads, tilføj nye, notér løfter givet i det trykte nummer.
6. Opdater modelkartoteket med nye modelerfaringer.

## Hemmeligheder (kort)

| Formål | Fil | Variabel |
|---|---|---|
| OpenRouter pr. magasin | `.env.gnisten`, `.env.pulsen`, `.env.spaending`, `.env.horisonten`, `.env.kraften` | `OPENROUTER_API_KEY` |
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
