# KRAFTEN – Redaktionsnotesbog

Opdateret efter nr. 1 (august 2026, *"Hvad holder lyset tændt"*). Modelerfaringer: [modelkartotek](../modelkartotek.md).

## Identitet

**KRAFTEN** dækker hele energisystemet: atom (fission, thorium, fusion), fossilt, vedvarende, lagring, landeudbygning, planer og anlæg. Nøgtern, kildetung. Ikke SPÆNDING (elbiler).

## Visuel linje (bindende fra nr. 1)

Prioritér **anlæg, maskiner og byggeri** — ikke stock "grønt blad på panel":

- Kraner, jack-up-skibe, monopæle  
- Reaktor-/containment-byggeri, armering  
- Solfarm under montering  
- BESS-containere, transformere  
- LNG-tanke, rør, lastearme  
- Net/master hvor det er relevant  

Stil: dokumentarisk/editorial foto (AI-genereret OK, **ingen logoer, ingen læsbar skiltetekst**). Cover + 4–6 artikelbilleder pr. nummer.

**Billedkilde er obligatorisk:** `imageCredit` + `imageSource` (URL) under hvert artikelbillede; cover: `coverCredit` + `coverSource`. Samlet liste i `images/SOURCES.md` og `imageCredits` i issue-kolofonen.

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

- `.env.kraften` ved OpenRouter-produktion.  
- Features 500–750 ord; bagsnit `flow: true`.  
- PDF: `build_magazine.py kraften 2026-08-nr1` når layout ønskes.
