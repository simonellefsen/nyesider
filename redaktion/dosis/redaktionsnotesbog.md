# DOSIS – Redaktionsnotesbog

Opdateret efter nr. 2 (august 2026, *"Appetitten under kontrol"*).  
OpenRouter: **kun** `.env.dosis`. Imagine: `.env.local`.

## Identitet

Longevity, ernæring/kost, tilskud, proteser/implantater, **wearables & hjemmetests** (blod/urin/CGM), forskning — sassy skepsis, ikke wellness-guru.  
**vs PULSEN:** de = sektor/klinik; vi = krop, tallerken, dosis, hardware.

## Format

- **Artikeltal:** 14 (nr. 1), 10 (nr. 2 efter Ordbogen droppet). Faste: Leder · features · Tallet · Rygtebørsen · Til PULSEN. **Ingen Ordbog** — gloser i parentes/fodnote.
- **Ordmål:** sigt **500–800 for features** (hævet fra 200–350 den 2026-08-09; det gamle loft er
  grunden til, at flere artikler blev til råd uden forbehold). Tallet 500–800.
- **Standard `mustCite`:** 1–2 for enhver artikel med et sundheds-/ernæringstal; 4+ for Tallet (kildetabel); 0 for Rygtebørsen.

## Nr. 2 — udgivet

**Tema:** Appetitten under kontrol (GLP-1)  
**Genopbygget 2026-08-09:** 10 artikler / 5.460 ord (var 10 / 1.821 — gennemsnit 182). Ni artikler
reelt kommissioneret på `.env.dosis`; lederen er chefredaktionens uden byline. Forbrug **0,51 USD**.
Cover + features (Imagine). PDF mangler.
`bestilling.json`: `redaktion/dosis/numre/2026-08-nr2/bestilling.json`.

### Læring fra genopbygningen af nr. 2 (2026-08-09)

**Den samme forkerte DOI dukkede op i to uafhængige kladder.** `10.1210/jendso/bvab048.031`, anført
som STEP 1's kropssammensætningsabstract, opløses til et **naboabstract om insulinresistens hos unge**
i samme supplement af samme tidsskrift. To forskellige modeller gættede den samme forkerte
identifikator. Fejlen er altså **reproducerbar, ikke tilfældig** — og en redaktion, der kun tjekker én
artikel, vil tro, den er en engangsfejl. Kør DOI-tjekket på **hver** reference, hver gang.

**Relativ og absolut risiko er nummerets vigtigste lektion.** Et dansk registerstudie af 424.152
personer (Grauslund m.fl., *Int J Retina Vitreous*, 2024) har titlen «semaglutide **doubles** the
five-year risk» af NAION — hazard ratio 2,19. Myndigheden klassificerer samtidig NAION som **meget
sjælden**, altså færre end 1 ud af 10.000. Begge dele er rigtige. Fordobler man noget meget lille,
får man stadig noget lille. Skriv altid *fordoblet fra hvad?*

**Hyppighedskategorier er definerede intervaller, ikke stemningsord.** Meget almindelig ≥ 1/10 ·
almindelig 1/100–1/10 · ikke almindelig 1/1.000–1/100 · sjælden 1/10.000–1/1.000 · **meget sjælden
< 1/10.000**. En overskrift om «ny alvorlig bivirkning» siger intet om hyppighed. Bemærk at WHO's
formulering («up to 1 in 10,000») og SmPC-kategorien (< 1/10.000) ikke er ordret ens — brug
kategorien i brødtekst og WHO's ordlyd i noten.

**Lægemiddelstyrelsen og Sundhedsstyrelsen forveksles systematisk.** To kladder tilskrev linjen om,
at «medicin ikke skal være førstevalg», til Sundhedsstyrelsen. Den står hos **Lægemiddelstyrelsen**,
på siden om vægttabs- og diabetesmedicin (senest opdateret 31. marts 2025) — samme sted som den
godkendte indikation og tilskudsspørgsmålet.

**Bløde tilskrivninger er også fabrikation.** En kladde skrev, at «Sundhedsstyrelsen og Dansk Selskab
for Klinisk Ernæring har begge peget på» diætistinddragelse. Påstanden kunne ikke efterprøves, og
selskabets domæne svarer ikke. Fjernet — pointen står nu som redaktionens egen vurdering, udtrykkeligt
mærket som sådan. Lånt autoritet er værre end ingen.

**Der findes ingen dansk myndighedsanbefaling om kost eller protein specifikt under GLP-1-behandling.**
De skemaer, der cirkulerer, er kommercielt materiale. Skriv fraværet frem i stedet for at gengive et
tal, læseren så tror er officielt.

## Nr. 1 — udgivet

**Tema:** Protein-æraen  
**Genopbygget 2026-08-09:** 13 artikler / 6.647 ord (var 14 / 3.680). Ordbogen fjernet. Tolv artikler
reelt kommissioneret på `.env.dosis`; lederen er chefredaktionens uden byline. Forbrug **0,53 USD**.
Cover + features (Imagine). PDF mangler.

### Læring fra genopbygningen af nr. 1 (2026-08-09)

**En DOI kan opløse korrekt og pege på det forkerte arbejde.** Fire DOI'er i én kladde: alle fire
opløste, og **to var forkerte**. Én anført som ESPEN's kliniske ernæringsretningslinje opløste til
*«Terrestrial LiDAR monitoring of coastal foredune evolution»* i **Earth Surface Processes and
Landforms** — kystmorfologi. En anden, anført som NNR2023, opløste til niacin-kapitlets scoping
review. I `wearables` var en tredje anført som AASM's positionsudtalelse, men opløste til et
randomiseret forsøg i samme tidsskrift. `check_links.py` godkender dem alle, fordi de svarer 200.

> **Metoden, der fanger det, og som skal bruges hver gang:**
> ```
> curl -sL -H "Accept: application/vnd.citationstyles.csl+json" https://doi.org/<DOI>
> ```
> Læs `title` og `container-title`, og hold dem op mod det, fodnoten påstår. Det tager ti sekunder.
> Det er samme lærdom som «200 er ikke bevis for den rigtige side», flyttet over på litteratur.

**Sundhedsstyrelsens D-vitaminanbefaling er opdateret 4. november 2025** — og notesbogens egen log
citerede den forældede. Det gælder nu **10 µg** dagligt fra oktober til april til børn over 4 år og
voksne (ikke «5–10 µg»), 10 µg året rundt til risikogrupperne, 20 µg med 800–1000 mg calcium til
voksne over 70, og en **øvre sikker grænse på 100 µg** (ikke 50). Begge forældede tal cirkulerer
stadig, og begge får folk til at regne forkert.

**Den farligste fejl i sundhedsstof er en ombyttet målgruppe.** En kladde skrev, at
vinteranbefalingen om D-vitamin kun gjaldt «grupper med særlig risiko». Den gælder børn over 4 år
og voksne generelt; risikogrupperne får den *året rundt*. En læser, der tror det modsatte, undlader
at følge anbefalingen. Målgruppe er ikke pynt — det er halvdelen af oplysningen.

**Registreret ≠ godkendt.** To kladder skrev, at kosttilskud er uden forudgående kontrol. Kosttilskud
skal **anmeldes til Fødevarestyrelsen**, og nye stoffer kræver tilladelse før markedsføring — men
myndigheden registrerer, at produktet findes, og tester ikke, om det virker. Den præcise formulering
er skarpere end den upræcise.

**Tal uden kilde skal ud, også de sandsynlige.** En kladde angav, at over 90 % af ledimplantater
holder mere end ti år. Kilden (sundhed.dk) var nede, så tallet blev fjernet og erstattet af en
henvisning til alloplastikregistrenes årsrapporter — hvilket passer bedre til artiklens eget
argument om, at netop de tal er offentlige.

**Modellerne leverede to helt korrekte referencer uopfordret:** VITAL-forsøget (Manson m.fl., NEJM
2019, 380:33–44) og PROT-AGE (Bauer m.fl., JAMDA 2013, 14:542–559). Begge kontrolleret via
DOI-metadata. Kildekontrol er ikke mistillid — det er den eneste måde at skelne de gode fra de dårlige.

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

- **2026-08-09:** Nr. 1 genopbygget og genudgivet efter afpubliceringen 2026-08-08. Se læringen ovenfor.
- **2026-08-09 (kilder):** Ny fast rutine — enhver DOI i en kladde slås op via CSL-JSON og
  sammenholdes med det, fodnoten påstår. To ud af fire var forkerte i første forsøg.

- **2026-08-09:** Nr. 2 genopbygget og genudgivet efter afpubliceringen 2026-08-08. Se læringen ovenfor.
