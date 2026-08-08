# DOSIS – Redaktionsnotesbog

Opdateret efter nr. 2 (august 2026, *"Appetitten under kontrol"*).  
OpenRouter: **kun** `.env.dosis`. Imagine: `.env.local`.

## Identitet

Longevity, ernæring/kost, tilskud, proteser/implantater, **wearables & hjemmetests** (blod/urin/CGM), forskning — sassy skepsis, ikke wellness-guru.  
**vs PULSEN:** de = sektor/klinik; vi = krop, tallerken, dosis, hardware.

## Format

- **Artikeltal:** 14 (nr. 1), 10 (nr. 2 efter Ordbogen droppet). Faste: Leder · features · Tallet · Rygtebørsen · Til PULSEN. **Ingen Ordbog** — gloser i parentes/fodnote.
- **Ordmål:** sigt 200–350 for features, 300–500 for Tallet (nr. 2 landede kortere på flere features under batch — notér til næste).
- **Standard `mustCite`:** 1–2 for enhver artikel med et sundheds-/ernæringstal; 4+ for Tallet (kildetabel); 0 for Rygtebørsen.

## Nr. 2 — udgivet

**Tema:** Appetitten under kontrol (GLP-1)  
**10 artikler:** leder, hvad er GLP-1, ernæring under behandling, bivirkninger, hype/adgang, protein+styrke, wearables, tallet, rygtebørs, til PULSEN. (Ordbogen fjernet 2026-08-08.)  
Cover + features (Imagine). PDF mangler.  
`bestilling.json`: `redaktion/dosis/numre/2026-08-nr2/bestilling.json`.

## Nr. 1 — udgivet

**Tema:** Protein-æraen  
**14 artikler:** leder, protein-æra, gram-behov, tallerken, pulver vs mad, D-vitamin, tilskudsjungle, implantater, **wearables/hjemmetests**, longevity-hype, tallet, ordbog, rygtebørs, til PULSEN.  
Cover + features (Imagine). PDF mangler.

## Nr. 3 — udgivet

**Tema:** Søvnen, der ikke kan stikkes  
11 artikler: leder, søvn-som-tilskud, timer, melatonin, hygiejne, tracker, søvn+GLP-1, tallet, ordbog, rygtebørs, til PULSEN.  
`bestilling.json`: `redaktion/dosis/numre/2026-08-nr3/bestilling.json`.

## Nr. 4 — kandidater

- **(2026-08) Søvn som "tilskud" der virker** (lovet i bagside-tone på nr. 2)  
- **(2026-08) Microbiom-hype**  
- **(2026-08) Styrketræning efter 60**  
- **(2026-08) Omega-3: evidens vs. hylde**

## Produktion

```bash
python3 production/load_env.py dosis
```

Fact-check obligatorisk før accept (se [redaktion/README](../README.md)). Medicin = indikation, forbehold, ingen dosisråd til læseren.

## Log

- **2026-08-08 (format):** Ordbogen fjernet fra nr. 2 — gloser i parentes/fodnote i features.


- **2026-08-08:** Nr. 2 publiceret (GLP-1). Tallet genopbygget med hårdere pejlemærker + fodnoter. Flere features bevidst korte under ugentlig batch — næste nummer: færre artikler eller hårdere words-brief.
- **2026-08-01:** 4 artikler manglede billede (pulver-vs-mad, tilskudsjunglen, longevity-hype, tallet) — tilføjet, hver i sin egen stilart (flad vektor / maksimalisme / retro / geometrisk) i stedet for endnu et fotorealistisk motiv, jf. ny stilregel i [redaktion/README](../README.md). Samtidig tilføjet hårde tal med kilde i pulver-vs-mad (NNR2023 protein g/kg), tilskudsjunglen (FDA/JAMA 776 forurenede produkter; DTU 60 % bruger tilskud), D-vitamin (SST's 5–10/20 µg), og longevity-hype (Newman/Ig Nobel 2024 blå zone-data), samt genopbygget "Tallet" med en kildetabel (levetid, overvægt, fysisk aktivitet, tilskud, D-vitamin, hofte-/knæalloplastik) i stedet for vage "ballpark"-rækker. Filnavne-præfikser i `articles/` rettet til at matche `issue.json`'s rækkefølge (var 09/09/10/11/12/13, nu 09–14 fortløbende).
- **2026-08-01:** Notesbog udvidet med `## Format`; nr. 1 retro-udfyldt som `bestilling.json`-skabelon (se `redaktion/dosis/numre/2026-08-nr1/bestilling.json` og [redaktion/bestilling.schema.md](../bestilling.schema.md)).
- **2026-08-01 rettelse:** `03-hvor-meget-protein.md` gav ingen konkret g/kg-tal, kun "tjek Fødevarestyrelsen" — tilføjede NNR2023's faktiske tal (0,66/0,83 g/kg voksne; 1,2-1,5 g/kg 70+) med kilde. Del af tværgående oprydning i 24 artikler med utilskrevne taltpåstande (se Workstream C, session 2026-08-01) — DOSIS' `13-rygteboersen.md` (spekulativ sladderkolonne) blev bevidst **ikke** rettet, samme begrundelse som PULSEN/DOSIS' øvrige rygtebørs-formater: `mustCite: 0` er et bevidst formatvalg der.

- **2026-08-08:** Nr. 3 publiceret — søvn-pakke (hygiejne, melatonin, tracker, GLP-1-kobling).

- **2026-08-08 (rettelse):** Nr. 3 fik `published: 2026-08-15` (ikke samme dag som nr. 2's 2026-08-08). Regel: højst ét publiceret nummer pr. magasin pr. kalenderdag — se `redaktion/udgivelseskalender.md` og `check_issue.py`.

- **2026-08-08 (holdt tilbage):** Nr. 3 *Søvnen, der ikke kan stikkes* ligger i `content/dosis/issues/2026-08-nr3/` med `status: scheduled` og `published: 2026-08-15`. Ikke på websitet før status sættes til `published` (mål: næste uge). Indhold og billeder er bevaret.

