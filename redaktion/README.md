# Redaktionen · Nye Sider

Redaktionel hukommelse for forlaget. Chefredaktør-agenten læser og opdaterer disse filer ved hver produktion.

## Struktur

- **[modelkartotek.md](modelkartotek.md)** — fælles erfaringer med OpenRouter-modeller (skribenter og billedmodeller) på tværs af alle titler. Læs før casting af nye numre; opdater efter hver produktion.
- **`<titel>/redaktionsnotesbog.md`** — pr. magasin: historier i støbeskeen, opfølgninger, idébank, faste formater og titelspecifik praktik. Grundlag for næste nummer.

## Arbejdsgang for et nyt nummer

1. Læs titlens `redaktionsnotesbog.md` (leads/opfølgninger) og `modelkartotek.md` (casting).
2. Brug **titlens egen nøgle** fra `.env.<titel>` — aldrig en anden titels nøgle, da forbruget aflæses pr. nøgle.
3. Producér nummeret; læg output i `content/<titel>/issues/<YYYY-MM-nrN>/` (artikler som markdown, billeder, `issue.json`, PDF).
4. Notér produktionsomkostningen i nummerets `issue.json` (`productionCostUSD`).
5. Opdater notesbogen: afvikl brugte leads, tilføj nye, notér løfter givet i det trykte nummer.
6. Opdater modelkartoteket med nye modelerfaringer.

## Billeder (copyright-politik)

**Standard: generér selv via xAI Imagine** (Grok Build `image_gen` / Imagine API). Det er forlagets standardvej for covers og artikelbilleder — undgår stock- og pressefoto-copyright.

- Prompt: motiver uden logoer, uden læsbar skiltetekst; stil tilpasset titlen (akvarel, editorial foto, osv.).
- Kreditering: `imageCredit` + `imageSource` (typisk Imagine / xAI → `https://x.ai/`) under figuren; cover: `coverCredit` + `coverSource`; samlet `imageCredits` + `images/SOURCES.md` i nummeret.
- **Træk ikke** billeder fra nettet, Google Images, Wikipedia eller agency feeds uden eksplicit licens og kilde-URL.
- Undtagelse: egenproducerede diagrammer/SVG (fx GNISTEN) og materiale med dokumenteret fri/egen licens.

## Ny titel

Opret `redaktion/<slug>/redaktionsnotesbog.md` og `content/<slug>/magazine.json` (brand, farver, sektioner, målgruppe).
