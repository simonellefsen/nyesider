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

## Nr. 2 — kandidater

- **(2026-08) Kalmarunionen i dybden — Norge/Sverige-vinkler**  
- **(2026-08) Christian 4. og stormagtstiden**  
- **(2026-08) Slesvig-Holsten før 1864**  
- **(2026-08) Kvinders stemmeret og den lange vej**  
- **(2026-08) Andelsbevægelsen**  
- **(2026-08) Besættelsen 1940–45 (uden at æde hele nummeret)**  
- **(2026-08) Inge Lehmann / Niels Bohr — videnskabsbiografier**

## Log

- **2026-08-08 (dybde):** Nr. 1 — reformation (404→**849** ord) og 1864 (383→**743** ord) reelt kommissioneret hos `anthropic/claude-opus-4.8` og `anthropic/claude-sonnet-5` med briefs på 700–900 ord og `mustCite: 3`. Ordmålet i `## Format` hævet til 700–900 for features. Begge kladder krævede tung fact-check — se `bestilling.json` for verdikterne.
  - **Lære (kladde-fabrikation):** 1864-kladden opfandt *«menig Rasmus Jensen fra 8. Regiment, hvis navn er bevaret i regimentets tabsliste»*. Ikke en vag påstand, men en konkret, verificerbart klingende detalje — den farligste slags, fordi den ligner præcis dét, briefet bad om («ét navngivet menneske»). Når et brief kræver en person, så kræv **også** at personen skal kunne slås op, ellers opfinder modellen en. Reformation-kladden fejlede mildere (dødsår 1544 for 1542) men i samme retning: selvsikre, konkrete, forkerte tal.
- **2026-08-08 (byline-integritet — UAFKLARET, kræver beslutning):** `bestilling.json` viser `writer.model: "editor-led"` på **alle 12** artikler i nr. 1, med `costUSD: null` — dvs. teksterne er skrevet af chefredaktionen. Men bylinerne krediterer navngivne modeller (GPT-5.6 Terra, Gemini 3.1 Pro, Mistral Large, Qwen3.7 Max, Grok 4.3 m.fl.), og forlagets forside lover: *«Hver artikel er skrevet af en navngiven model.»* De to artikler ovenfor er nu bragt i overensstemmelse med deres byline. **De resterende ti er det ikke.** Valgmuligheder: (a) kommissionér dem reelt hos de krediterede modeller, (b) skriv bylinen om til «KRØNIKE-redaktionen», eller (c) tilføj en kolofon-note om at nr. 1 var redaktionelt skrevet. Skal afklares før nr. 2, så mønsteret ikke gentages.
- **2026-08-08 (links):** Ny `production/check_links.py` + `npm run check:links`; kører som ikke-blokerende trin 6 i preflight. Anledning: en fodnote i Ørsted-artiklen linkede til en *gættet* dansk URL hos Nationalbanken, som 404'ede i den udgivne artikel. Værktøjet fandt straks endnu en gættet URL i reformation-artiklen. **Gæt aldrig en adresse — også selvom du har læst indholdet på en anden sprogversion.** Portefølje-scan: 4 døde links i SPÆNDING nr. 1, HumaNerd nr. 1 og INDENI nr. 1 (Renault ×2, FANUC, Metal Packaging Europe-PDF) — ikke rettet endnu.
- **2026-08-08 (depth):** Nr. 1 — kort/SVG, Dannevirke-rekonstruktion, faktabokse (Hedeby, Øresundstold), Ansgar/Ribe, Margrete uden samtidsportræt, 1658/Skåne, Frihedsstøtten (CC BY), Dybbøl Mølle, mormonudvandring, Ørsted-daguerreotypi + korrespondance.


- **2026-08-08:** Titel oprettet; nr. 1 *"Riget formes"* produceret.
