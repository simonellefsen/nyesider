# HORISONTEN – Redaktionsnotesbog

Opdateret efter nr. 3 (august 2026) **Dolomitterne i efteråret** — genoplivet fra parked.

## Identitet

**HORISONTEN** er magasinet om at rejse i Europa: ruter, sæson, praktisk planlægning. **vs KULTURBOXEN:** HORISONTEN svarer "hvordan kommer jeg derhen?"; KULTURBOXEN svarer "hvordan lever folk dér?" — se [søstertitel-note](#søstertitel-kulturboxen) nedenfor.

## Afviklet i nr. 3 (publiceret 2026-08)

- **Dolomitterne i efteråret:** overblik, vandring, cykling, løb, byliv (Bolzano/Cortina), søer/udsigter, kalender, mad & vin, praktisk.  
- Leder broer fra [nr. 2 Georgien](../../content/horisonten/issues/2026-08-nr2/) og [KULTURBOXEN Georgien](../../content/kulturboxen/issues/2026-08-nr1/).  
- Kilde: parked-pakke i `redaktion/horisonten/parked/dolomitterne-efteraar/` (beholdes som arkiv/kopi-kilde).

## Afviklet i nr. 2 — GENOPBYGGET OG GENUDGIVET 2026-08-17

- **Georgien — bjerge, by og bord.** 10 artikler, **5.835 ord** (var 1.720 ord — gns. 172,
  det tyndeste nummer i hele porteføljen). Ni artikler reelt kommissioneret på `.env.horisonten`;
  lederen er chefredaktionens og har **ingen byline**. Samlet forbrug **0,34 USD**.
  `check_issue.py`: **0 fejl, 0 advarsler.** Krydslink til [KULTURBOXEN nr. 1](../../content/kulturboxen/issues/2026-08-nr1/).

### To formatbeslutninger, der bør gentages

**Kalenderen indeholder ingen måneder.** For et bjergland er en sæson ikke en dato: passene
åbner, når sneen tillader det. Briefen forbød måneder, datoer, temperaturer og festivalnavne, og
kladden skrev i stedet, hvordan man *læser* en sæson — med sin egen formulering «sneen bestemmer,
ikke datoen». Det er nummerets bedste artikel.

**Praktisk indeholder ingen svar.** Kun hvad læseren selv skal slå op, og hvor, med den
begrundelse at rejsepraktik ældes hurtigere, end et magasin udkommer. En visumregel eller pris,
der ændrer sig tre uger efter udgivelsen, er en bjørnetjeneste.

Begge dele kom af, at briefen **forbød** det, der ikke kunne kildebelægges — samme metode som
INDENI nr. 2 samme dag. Ni kladder, ikke ét opfundet tal: ingen højdemeter, gåtider, temperaturer,
priser, valutakurser eller visumregler.

### Kilder

Rygraden er UNESCO's verdensarvsliste, som er kildebelagt og fordeler sig over landet: Gelati
(1994, ændret 2017), Mtskheta (1994), Øvre Svaneti (1996) og Colchic Rainforests and Wetlands
(2021, landets eneste naturarv). 14 steder på den vejledende liste, de fleste fra 2007.
**Modellerne ramte samtlige UNESCO-ID'er korrekt** (708 Mtskheta, 709 Svaneti, 710 Gelati,
1616 Colchic, 5221 Alaverdi) — kontrolleret mod UNESCO's egen landeside.

**Kilde, der ikke kunne bruges:** `ich.unesco.org` (immateriel kulturarv) er beskyttet af en
CAPTCHA. Qvevri-metoden står efter alt at dømme på den liste, men det kunne ikke verificeres, og
nummeret skriver derfor metoden uden årstal eller listestatus. **Bemærk også:** whc.unesco.org
svarer 403 på automatiserede kald, men åbner fint i en browser — endnu et eksempel på, at en
statuskode ikke er en dom over en side.

### Hvad faktatjekket fangede

- **To gættede kilder:** Encyclopaedia Britannicas Tbilisi-opslag (byliv) og den georgiske
  ortodokse kirkes officielle side (udsigter). Ingen af dem var briefet eller kontrolleret. Fjernet.
- **En markdown-fejl** i vandringsartiklens fodnote, hvor URL'en stod både som linktekst og mål.

## Historier i støbeskeen til nr. 4+

1. **(2026-08) Kreta, Sicilien, eller storby-weekend** (Lissabon / Ljubljana).  
2. **(2026-08) Læsersendte ruter** (Mallorca + senere Georgien/Dolomit).  
3. **(2026-08) Postkort-vignet** som fast bagsnit.  
4. ~~Bevidst asynk~~ → **synket 2026-08-08:** [KULTURBOXEN nr. 2](../../content/kulturboxen/issues/2026-08-nr2/) (Sydtyrol / tre sprog).

## Format

- **Faste formater:** Vandring · Cykling · Løb · Byliv · (Strande/søer/udsigter efter destination) · Kalenderen · Mad & Vin · Praktisk.
- **Standard `mustCite`:** 1–2 for praktik-artikler med priser/afstande/temperaturer; 0 for stemningsartikler uden konkrete tal.
- Aldrig opdigtede præcise datoer for virkelige begivenheder.  
- **Fact-check** af stednavne og sæson før accept (chefredaktør — se [redaktion/README](../README.md)).

## Søstertitel: KULTURBOXEN

[KULTURBOXEN](../kulturboxen/redaktionsnotesbog.md) = livet i kulturen. HORISONTEN = rejsen til stedet.

### Synk-regel (planlægning)

**Prøv at synke numre**, når det giver mening: samme land/region i samme sæson (fx Georgien nr. 2 her + KULTURBOXEN nr. 1).  
- Før I låser destination: tjek KULTURBOXENs notesbog — er der en kultur i støbeskeen, der matcher?  
- Ikke altid muligt (rene storby-weekender, rene “oversete folk” uden rejsevinkel). Så notér *bevidst asynk*.  
- Ved synk: krydslinks begge veje + “Søster: …” i notesbogen.

## Praktisk

- PDF mangler for nr. 2–3.  
- Geografisk præcision er kernen.  
- OpenRouter: **kun** `.env.horisonten`. Imagine: `.env.local`.

## Log

- **2026-08-08:** Nr. 3 publiceret — Dolomitterne genoplivet fra parked; byline DeepSeek rettet; `bestilling.json` oprettet.
- **2026-08-08 (senere):** Søster synket — KULTURBOXEN nr. 2 *Tre sprog, ét plateau* (Sydtyrol).
- **2026-08-01:** Notesbog udvidet med `## Identitet` og `## Format`; leads datostemplet (se [redaktion/README](../README.md)).
- **2026-08-01 rettelse:** `03-vandring-tramuntana.md` — GR221 var angivet til "90-100 km"; nuværende kilder angiver hovedruten til ca. 140 km (op til ~170 km med varianter). Rettet + kilde tilføjet. Puig de Massanellas højde (1.364 m, næsthøjeste) var korrekt — tilføjede kun kilde. `07-strande-skjulte-bugter.md` — tilføjede "cirka-tal, tjek på stedet"-forbehold til parkeringsprisen, samme mønster som `10-praktisk-planlaeg-turen.md`. **Ikke rettet i denne omgang:** priserne i `10-praktisk-planlaeg-turen.md` (hotel/middag/lejebil) har allerede et tilsvarende forbehold i teksten og er ikke ændret; HORISONTEN nr. 1 og nr. 2 har fortsat 0 % fodnote-dækning generelt, hvilket er en separat, større opgave end denne sessions afgrænsede rettelse af konkrete faktafejl.
