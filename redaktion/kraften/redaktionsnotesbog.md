# KRAFTEN – Redaktionsnotesbog

Opdateret efter nr. 1 (august 2026, *"Hvad holder lyset tændt"*). Modelerfaringer: [modelkartotek](../modelkartotek.md).

## Identitet

**KRAFTEN** dækker hele energisystemet: atom (fission, thorium, fusion), fossilt, vedvarende, lagring, landeudbygning, planer og anlæg. Nøgtern, kildetung. Ikke SPÆNDING (elbiler).

## Visuel linje (bindende fra nr. 1)

**Kun xAI Imagine** til fotos/illustrationer (ingen scrapede presse-/stockfotos) — se [redaktion/README.md](../README.md) copyright-politik.

Prioritér **anlæg, maskiner og byggeri** — ikke stock "grønt blad på panel":

- Kraner, jack-up-skibe, monopæle  
- Reaktor-/containment-byggeri, armering  
- Solfarm under montering  
- BESS-containere, transformere  
- LNG-tanke, rør, lastearme  
- Net/master hvor det er relevant  

Stil: dokumentarisk/editorial (Imagine), **ingen logoer, ingen læsbar skiltetekst**. 4–6 artikelbilleder pr. nummer.

### Forside (skifter hvert nummer)

Hvert nummer har **egen cool forside** — ikke et fast logo-cover:

1. Sæt `issueTheme` (fx «Hvad holder lyset tændt»).  
2. Generér **ny** `images/kraften_cover.png` (3:4, Imagine) der *fortolker temaet* — system/net, anlæg, brændsel, havvind, lagring …  
3. Peg `issue.json` → `"cover": "images/kraften_cover.png"` + `coverCredit` / `coverSource`.  
4. Brandfarver i billedet: mørk grøn-sort, amber `#E3A008`, teal-highlight.  
5. Ingen masthead-tekst i billedet (web/PDF lægger titel ovenpå / ved siden af).

Nr. 1-forside: dramatisk nattescene med master, lysbue, køletårn og vind — «systemet der holder lyset tændt».

**Billedkilde er obligatorisk:** `imageCredit` + `imageSource` under hvert artikelbillede (Imagine / xAI → `https://x.ai/`); cover: `coverCredit` + `coverSource`. Samlet liste i `images/SOURCES.md` og `imageCredits` i issue-kolofonen.

## Nr. 1 — udgivet

14 artikler, cover + 5 feature-billeder (atom, vind, sol, lagring, gas). Kilder primært Ember EER 2026, IEA Electricity 2026, ENS/IEA DK.

## Løfter / nr. 2

- Bagside: netflaskehalse, uranmarked, anlæg der får tilladelse.  
- Dybde i ét land (fx DE net nord–syd eller FR EPR-status).  
- Geotermi / varme.  
- Kul i Asien som global balance.  

## Research-regler

Tal med kilde + årstal. Skeln nameplate MW / TWh / planlagt / under byggeri / i drift. Ingen opdigtede projektnavne.

## Praktisk

- OpenRouter: **kun** `.env.kraften` (aldrig andre titlers nøgler).  
- Imagine: `XAI_API_KEY` i `.env.local`.  
- `python production/load_env.py kraften` før scriptet kørsel.  
- Features 500–750 ord; bagsnit `flow: true`.  
- PDF: `build_magazine.py kraften 2026-08-nr1` når layout ønskes.
