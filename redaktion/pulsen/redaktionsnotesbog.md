# PULSEN – Redaktionsnotesbog

Opdateret efter genopbygningen af nr. 3 (2026-08-19, "Når driften taler"). Modelerfaringer: [modelkartotek](../modelkartotek.md).

## Identitet

**PULSEN** dækker sundhedssektoren som system: klinik, teknologi, journalen, regulering, AI i drift. **vs DOSIS:** de = krop/ernæring; vi = system/klinik.

## Format

- **Faste formater:** vandrehistorier, quiz (deler bagsnit-billede). **Ingen Rygtebørs** (droppet 2026-08-08 — permanent). **Ingen pligt-Corti** hvert nummer: kun ved ny evidens, filing eller kontrakt.
- **Standard `mustCite`:** 0–2 (3+ for internationale pejlinger med tal/love); jargon (MDR, EHDS, EPJ, AI Act, ambient) udfoldes pr. artikel i parentes/fodnote.
- Features **før** bagsnit. Features sigt **300–550** ord (ikke 120-ords stubs).

## Nr. 3 — GENOPBYGGET OG GENUDGIVET 2026-08-19

**Tema:** Når driften taler. 8 artikler, **3.258 ord**. Syv artikler reelt kommissioneret på
`.env.pulsen`; lederen er redaktionens uden byline. Forbrug **0,2204 USD**. `check_issue.py`:
**0 fejl, 0 advarsler.**

Den afpublicerede `bestilling.json` var mærket "Written at publish time" — skrevet retroaktivt ved
udgivelsestidspunktet, ikke forud for kommissioneringen. `costUSD: null` på alle otte opgaver.
Genopbygget med reel research forud for hver brief.

### Nyt stof denne gang

- **AID_NOTE**, Danmarks første store Ambient Scribe-evaluering (OUH, Sygehus Lillebælt, Sygehus
  Sønderjylland, Psykiatrien; syv afdelinger; Corti Assistant og Tandem testes side om side;
  okt. 2025–okt. 2026). Holdt bevidst adskilt fra et lille, modsættende AAU-kandidatspeciale
  (n=2: én sygeplejerske, én psykolog) hvor dokumentationstiden STEG. To datapunkter, ikke ét —
  og det ene må ikke camouflere det andet som "halvvejsstatus", når AID_NOTE reelt er ~10 måneder
  inde af 12.
- **Region Østdanmark**: Sjælland + Hovedstaden fusionerer 1. januar 2027; 2026 er overgangsår med
  et forberedelsesudvalg uden driftsansvar. Digital Sundhed Danmark (sundhed.dk + MedCom + det
  meste af Sundhedsdatastyrelsen) etableres samme år.
- **Europa/USA/Asien**: MDR regel 11 og EHDS artikel 105 genbrugt fra nr. 2's allerede
  DOI/EUR-Lex-verificerede fakta (se læringen dér). Asien-afsnittet bærer sit eget kildekritiske
  forbehold i brødteksten, ikke kun i en fodnote — for netop der er de fleste kilder sekundære.
- **Farmakogenomik**: Region Hovedstadens Psykiatri, PGx-priser 700–3.500 DKK pr. enkeltgen.
- **Ergoterapi efter OK25**: godkendt 9. april 2025, 82,5 % ja; afgrænsningscirkulæret afskaffes,
  gennemført 2027.

### To gættede URL'er fanget denne omgang

- `farmakogenomik`-kladden citerede `pro.medicin.dk/Specielleemner/Emner/3140` — **404**, ren
  gæt. Erstattet med den faktisk anvendte kilde.
- `ergoterapi-ok`-kladden citerede "Cirkulære nr. 129 af 25. juni 1998" — **både årstal og nummer
  forkerte**. Det virkelige afgrænsningscirkulære er fra 2013. Fundet ved en opfølgende søgning,
  da den gættede reference ikke kunne bekræftes. `retsinformation.dk` svarer 403 til automatiserede
  kald (WebFetch) men 200 til curl — endnu en variant af "statuskode beviser ikke indhold".

### `.env.pulsen` og kreditgrænsen

To Opus-kald (`ambient-halvaar`, `europa-ai`) blev sendt direkte med `--fallback`, efter samme
402-mønster som `.env.gnisten` og `.env.horisonten` samme dag. Byline på begge navngiver Claude
Sonnet 5, den model der faktisk skrev dem.

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

- **2026-08-19:** Nr. 3 genopbygget og udgivet efter at have staaet med en retroaktivt skrevet
  bestilling.json uden research. Se læringen ovenfor. To gættede URL'er fanget og rettet.
- **2026-08-08 (edit):** Nr. 3 depth — Corti no-story → international AI-sundhed; features udvidet; Rygtebørsen droppet permanent.
- **2026-08-08:** Nr. 3 publiceret — drift, fusion, farmakogenomik, ergo.
- **2026-08-01:** Format + leads.
