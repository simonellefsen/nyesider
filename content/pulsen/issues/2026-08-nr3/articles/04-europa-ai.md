---
title: "Tre kontinenter, tre problemer"
standfirst: AI-sundhed uden for Danmark bliver ofte fortalt som ét globalt kapløb. Europa, USA og Asien løser slet ikke den samme opgave.
byline: Claude Sonnet 5 (Anthropic)
section: Analyse · Marked
order: 4
image: ../images/pulsen_europa-ai.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

Når AI i sundhedssektoren diskuteres uden for Danmark, er der en tendens til at tale om "reguleringen" og "godkendelsen" i ental — som om Europa, USA og Asien løser den samme opgave med forskellig hastighed. Det gør de ikke. De regulerer forskellige ting, og især fortællingen om asiatisk tempo bør læses med en solid dosis skepsis.

### Europa: risikoklasser, ikke tempo

I EU er udgangspunktet forordning (EU) 2017/745 om medicinsk udstyr (Medical Device Regulation, MDR), konsolideret udgave 02017R0745-20250110. Regel 11 i bilag VIII handler specifikt om software, og den afgørende sætning er ikke kompliceret: software der leverer information, som bruges til at træffe beslutninger med diagnostisk eller terapeutisk formål, klassificeres som klasse IIa. Klassen skærpes til III, hvis en fejlagtig beslutning kan medføre død eller uoprettelig forværring af helbredstilstanden, og til IIb ved risiko for alvorlig forværring eller kirurgisk indgreb. Men reglen slutter med en sætning, der ofte overses, fordi den ikke er dramatisk: "All other software is classified as class I." Al anden software er klasse I. Det er ikke en bagatel — det er hele historien i regel 11: de fleste sundheds-apps og administrative AI-værktøjer falder formentlig i den kedelige, uregulerede klasse I, mens de færreste når klasse III.[^1]

Dertil kommer European Health Data Space (EHDS), forordning (EU) 2025/327, som ofte omtales, som om den "træder i kraft" på én dato. Det gør den ikke. Artikel 105 lægger op til et tæppe af datoer: forordningen finder generel anvendelse fra 26. marts 2027, mens artikel 3-15 og en række andre bestemmelser først gælder fra 26. marts 2029 eller 2031, afhængigt af datakategori. Kapitel III gælder fra 2031, kapitel IV fra 2029, og artikel 75, stk. 5, først fra 26. marts 2035. At sige "EHDS træder i kraft i 2027" er derfor en forenkling, der kan være direkte misvisende for en klinik eller en sundheds-it-afdeling, der planlægger implementering.[^2]

Endnu et kildekritisk punkt: slår man selv op på EUR-Lex, kan et automatiseret kald mod siden returnere HTTP-statuskode 202. Det betyder blot, at serveren har accepteret forespørgslen — det beviser ikke, at man har fundet den rigtige konsoliderede udgave. Man skal åbne siden i en almindelig browser og læse indholdet.

### USA: godkendelse af produktet, ikke af data

Den amerikanske fødevare- og lægemiddelstyrelse (FDA) arbejder efter et andet princip end EU. Her er sporet software som medicinsk udstyr (Software as a Medical Device, SaMD), hvor FDA vurderer det enkelte produkt op mod sikkerheds- og effektivitetskrav forud for markedsføring.[^3] Det er en produktgodkendelse, ikke en regulering af, hvordan sundhedsdata må dele sig på tværs af systemer og lande — det sidste er netop EHDS' ærinde i EU. De to systemer kan derfor ikke sammenlignes direkte i "hvem er hurtigst": de svarer på forskellige spørgsmål.

### Asien: tempo-fortællingen kræver skepsis

I dele af Asien beskrives godkendelsescyklusser for sundheds-AI ofte som markant hurtigere end i Europa og USA. Det er en udbredt fortælling — men den bør læses med forbehold, fordi mange af de rapporter, der cirkulerer om asiatiske AI-sundhedsgodkendelser, er sekundære, ofte oversat eller refereret gennem flere led, og svære at verificere uafhængigt op mod primære, offentligt tilgængelige myndighedskilder. Hvor MDR og EHDS kan læses direkte på EUR-Lex, og FDA's rammer kan slås op på myndighedens egen hjemmeside, mangler der ofte en tilsvarende, let tilgængelig primærkilde for de asiatiske eksempler, der citeres i internationale medier.

### Konklusion: ikke ét kapløb

Billedet af et globalt AI-sundhedskapløb holder ikke. EU bygger et system af risikoklasser og datoer for datadeling. USA godkender produkter enkeltvis. Og tempo-fortællingen om Asien er den, der kræver mest kildekritisk arbejde, før den kan bruges til noget som helst i en dansk sundhedsfaglig sammenhæng.

[^1]: Europa-Parlamentets og Rådets forordning (EU) 2017/745 af 5. april 2017 om medicinsk udstyr, [konsolideret udgave (CELEX 02017R0745)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02017R0745), EUR-Lex.

[^2]: Europa-Parlamentets og Rådets forordning (EU) 2025/327 om det europæiske sundhedsdataområde (EHDS), [EUR-Lex (CELEX 32025R0327)](https://eur-lex.europa.eu/legal-content/DA/TXT/?uri=CELEX:32025R0327).

[^3]: U.S. Food and Drug Administration: [«Software as a Medical Device (SaMD)»](https://www.fda.gov/medical-devices/digital-health-center-excellence/software-medical-device-samd), FDA.gov.
