# PULSEN – Redaktionsnotesbog

Opdateret efter genopbygningen af nr. 2 (august 2026, "Når driften taler") — depth/format-pass samme dag. Modelerfaringer: [modelkartotek](../modelkartotek.md).

## Identitet

**PULSEN** dækker sundhedssektoren som system: klinik, teknologi, journalen, regulering, AI i drift. **vs DOSIS:** de = krop/ernæring; vi = system/klinik.

## Format

- **Faste formater:** vandrehistorier, quiz (deler bagsnit-billede). **Ingen Rygtebørs** (droppet 2026-08-08 — permanent). **Ingen pligt-Corti** hvert nummer: kun ved ny evidens, filing eller kontrakt.
- **Standard `mustCite`:** 0–2 (3+ for internationale pejlinger med tal/love); jargon (MDR, EHDS, EPJ, AI Act, ambient) udfoldes pr. artikel i parentes/fodnote.
- Features **før** bagsnit. Features sigt **300–550** ord (ikke 120-ords stubs).

## Nr. 3 — udgivet

**Tema:** Når driften taler  
**8 artikler:** leder, ambient i drift, region-fusion/AI, **AI i sundhed uden for DK (EU/USA/Asien)**, farmakogenomik, ergoterapi efter OK, vandrehistorier, quiz.  
Corti-IPO-gentagelse **erstattet**. Rygtebørsen **fjernet**.  
`bestilling.json`: `redaktion/pulsen/numre/2026-08-nr3/bestilling.json`.  
Kryds: [DOSIS nr. 2](../../content/dosis/issues/2026-08-nr2/).

## Nr. 2 — genopbygget og genudgivet 2026-08-17

**Tema:** Når tasterne bliver stille
**8 artikler, 4.408 ord** (var 9 artikler / 2.447 ord — gns. 272, altså præcis de
«120-ords stubs», formatreglen advarer mod). Syv artikler reelt kommissioneret på
`.env.pulsen`; lederen er chefredaktionens og har **ingen byline**.
Samlet forbrug **0,22 USD** — portefølgens billigste nummer.
`bestilling.json`: `redaktion/pulsen/numre/2026-08-nr2/bestilling.json`.
**Rygtebørsen er fjernet**, jf. formatreglen af 2026-08-08. Derfor 9 → 8 artikler.

Nummeret gik igennem `check_issue.py` med **0 fejl og 0 advarsler** — det første i
genopbygningen, der gør det.

### Hvad der virkede: skriv fra lovteksten

To af nummerets tre tunge artikler er bygget direkte på primærkilden i EUR-Lex, og
det er grunden til, at der ikke var en eneste faktafejl at rette i dem:

- **MDR regel 11** (bilag VIII til forordning (EU) 2017/745, konsolideret udgave
  02017R0745-20250110). Software, der leverer information til diagnostiske eller
  terapeutiske beslutninger, er klasse IIa; klasse III ved risiko for død eller
  uoprettelig forværring; IIb ved alvorlig forværring eller kirurgi. Og så sætningen,
  der er hele historien: «All other software is classified as class I.»
- **EHDS artikel 105** (forordning (EU) 2025/327). Gælder fra 26. marts 2027; artikel
  3-15 m.fl. fra 26. marts 2029 for den første gruppe datakategorier og 26. marts 2031
  for den næste; kapitel III fra 2031; kapitel IV fra 2029 — og artikel 75(5) først fra
  **26. marts 2035**.

**Gør det sådan igen.** Når stoffet er en EU-forordning, findes den fulde tekst gratis
og entydigt. En brief bygget på den giver kladder uden gættede tal.

### Kildeteknisk fund

**EUR-Lex svarer HTTP 202 på automatiserede kald.** Statuskoden alene siger derfor
hverken at siden findes eller at den er den rigtige — indholdet skal kontrolleres i en
browser. Det er den tredje variant af samme problem, porteføljen har mødt på tre dage:
ESA svarer 200 med sin egen fejlside, NASA Glenn meldes død på grund af et manglende
certifikat, og EUR-Lex svarer 202 på noget, der findes.

### Formatnote

Quizzen lander på 254 ord mod de briefede 300-500. Det er formatets natur — spørgsmål
og svar, uden udfyldning. **Sæt quizzens ordbudget til 200-350.**

## Nr. 2 — den afpublicerede udgave (til arkivet)

Ambient pilot→drift, MDR, EHDS, nordisk stak, ergoterapi 2035, bagsnit (inkl. daværende rygtebørs).

## Nr. 4 — kandidater

- **(2026-08) Offentlige ambient-evalueringer med tal**  
- **(2026-08) NHS/tysk/fransk ambient eller billed-AI — case med kilde**  
- **(2026-08) Aiforia/Dedalus kliniske resultater**  
- **(2026-08) Bupa Prevention Pathways tal**  
- **(2026-08) Corti — kun hvis filing/signaler er nye**

## Log

- **2026-08-08 (edit):** Nr. 3 depth — Corti no-story → international AI-sundhed; features udvidet; Rygtebørsen droppet permanent.
- **2026-08-08:** Nr. 3 publiceret — drift, fusion, farmakogenomik, ergo.
- **2026-08-01:** Format + leads.
