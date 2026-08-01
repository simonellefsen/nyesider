# DOSIS – Redaktionsnotesbog

Opdateret efter nr. 1 (august 2026, *"Protein-æraen"*).  
OpenRouter: **kun** `.env.dosis`. Imagine: `.env.local`.

## Identitet

Longevity, ernæring/kost, tilskud, proteser/implantater, **wearables & hjemmetests** (blod/urin/CGM), forskning — sassy skepsis, ikke wellness-guru.  
**vs PULSEN:** de = sektor/klinik; vi = krop, tallerken, dosis, hardware.

## Nr. 1 — udgivet

**Tema:** Protein-æraen  
**14 artikler:** leder, protein-æra, gram-behov, tallerken, pulver vs mad, D-vitamin, tilskudsjungle, implantater, **wearables/hjemmetests**, longevity-hype, tallet, ordbog, rygtebørs, til PULSEN.  
Cover + features (Imagine). PDF mangler.  
**2026-08-01 rettelse:** 4 artikler manglede billede (pulver-vs-mad, tilskudsjunglen, longevity-hype, tallet) — tilføjet, hver i sin egen stilart (flad vektor / maksimalisme / retro / geometrisk) i stedet for endnu et fotorealistisk motiv, jf. ny stilregel i [redaktion/README](../README.md). Samtidig tilføjet hårde tal med kilde i pulver-vs-mad (NNR2023 protein g/kg), tilskudsjunglen (FDA/JAMA 776 forurenede produkter; DTU 60 % bruger tilskud), D-vitamin (SST's 5–10/20 µg), og longevity-hype (Newman/Ig Nobel 2024 blå zone-data), samt genopbygget "Tallet" med en kildetabel (levetid, overvægt, fysisk aktivitet, tilskud, D-vitamin, hofte-/knæalloplastik) i stedet for vage "ballpark"-rækker. Filnavne-præfikser i `articles/` rettet til at matche `issue.json`'s rækkefølge (var 09/09/10/11/12/13, nu 09–14 fortløbende).

## Nr. 2 — kandidater

- GLP-1 og ernæring under behandling (forsigtig, kilde-tung)  
- Søvn som “tilskud” der virker  
- Microbiom-hype  
- Styrketræning efter 60  
- Omega-3: evidens vs. hylde

## Produktion

```bash
python3 production/load_env.py dosis
```

Fact-check obligatorisk før accept (se [redaktion/README](../README.md)).
