# HORISONTEN – Redaktionsnotesbog

Opdateret efter nr. 3 (august 2026) **Dolomitterne i efteråret** — genopbygget 2026-08-19 fra en tom "parked"-skal.

## Identitet

**HORISONTEN** er magasinet om at rejse i Europa: ruter, sæson, praktisk planlægning. **vs KULTURBOXEN:** HORISONTEN svarer "hvordan kommer jeg derhen?"; KULTURBOXEN svarer "hvordan lever folk dér?" — se [søstertitel-note](#søstertitel-kulturboxen) nedenfor.

## Afviklet i nr. 3 — GENOPBYGGET OG GENUDGIVET 2026-08-19

**Dolomitterne i efteråret.** 10 artikler, **2.607 ord**. Ni artikler reelt kommissioneret på
`.env.horisonten`; lederen er redaktionens uden byline. Forbrug **0,1488 USD**. `check_issue.py`:
**0 fejl, 0 advarsler.**

Den forrige "parked"-pakke havde `receipt.words` talt fra allerede publiceret tekst og `costUSD:
null` på alle ti opgaver — en genoplivning uden reel kommissionering, ikke en løgn i samme forstand
som byline-sagerne, men uden reelt indhold bag. Bygget forfra med research forud for hver brief:
Sellarondaens tal (51,5–53 km, fire passer), Alpe di Siusis og Lago di Braies' faktiske
sæsondatoer, og Törggelen-traditionen (Nuier/Suser/Sauser, Keschtnweg, Eisacktal).

### Krydslink til KULTURBOXEN nr. 2 fuldført

KULTURBOXEN nr. 2 (*Tre sprog, ét plateau*, samme destination — Sydtyrol) var allerede udgivet
2026-08-08 og havde et bagsnit ("Til HORISONTEN") skrevet UDEN levende link, fordi dette nummer
endnu ikke var udgivet — "behold ordene, drop parentesen", jf. husreglen om cross-title-links til
ikke-udgivne søskende. Nu hvor nr. 3 er udgivet, er linket tilføjet begge veje: HORISONTEN linker
til KULTURBOXEN nr. 2 i lederen, overbliksartiklen og bylivsartiklen; KULTURBOXEN nr. 2's bagsnit
har fået en redaktionel eftertekst med det levende link.

### Formatvalg, der afviger bevidst fra nr. 2's Georgien-mønster

Nr. 2's Kalenderen og Praktisk indeholdt **ingen** datoer/svar, fordi intet kunne kildebelægges
dengang. Nr. 3's research gav faktisk konkrete, kildebelagte datoer (kabinebane, trafikforbud,
Törggelen-sæson), så Kalenderen og Praktisk her indeholder måneds-niveau-datoer MED et eksplicit
forbehold om årlig variation, plus én fodnote til suedtirol.info i Praktisk (mustCite: 1). Begge
tilgange er rigtige — forskellen er, hvad researchen faktisk fandt, ikke et skift i husregel.

### .env.horisonten ramte samme kreditgrænse som .env.gnisten

Tre af de ni Opus-kald (`cykling`, `mad-og-vin`, `praktisk`) fik OpenRouter 402 (for lav
kreditgrænse til `max_tokens`-budgettet). Løst med `commission.py --fallback` — byline på de tre
artikler navngiver derfor Claude Sonnet 5, den model der faktisk skrev dem, ikke Opus 4.8.

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

## Nr. 4 — udgivet 2026-08-29

**Tema:** Sicilien i efteråret. **10 artikler, 3.719 ord.** Ni artikler reelt kommissioneret på
`.env.horisonten`; lederen er redaktionens uden byline. Forbrug **0,2422 USD**. `check_issue.py`:
**0 fejl, 0 advarsler.** `check_links.py`: **0 døde links.** `bestilling.json`:
`redaktion/horisonten/numre/2026-08-nr4/bestilling.json`.

Valgt fra idébankens "Kreta, Sicilien, eller storby-weekend". **Bevidst asynk med KULTURBOXEN
nr. 4** (Marokko) — prøvet først, jf. synk-reglen, men HORISONTENs egen identitet og nr. 3's
bagsideløfte afgrænser titlen til Europa, og Marokko passer derfor ikke. Noteret åbent her,
ikke stiltiende sprunget over.

### To fabrikerede kilder fanget i faktatjekket

- `cykling`-kladden tilføjede en ubriefet, ukildebelagt hældningsprocent ("over 10%") for
  Madonie-stigningerne — fjernet, kladden havde intet belæg for det præcise tal.
- `kalenderen`-kladden citerede selv en fodnote til "www.etnadoc.com" — domænet svarer slet ikke
  (ingen DNS-opløsning). Ren fabrikation, ikke i briefens kildeliste. Erstattet med den allerede
  verificerede Following the Riviera-kilde. **Samme mønster som KRAFTEN nr. 4's SNAP-10A-fejl
  samme uge: en model kan føje en overbevisende, præcis detalje til, som slet ikke står i
  briefen — verificér altid tilføjelser, ikke kun de tal, briefen selv gav.**

### En race, der ikke fandtes

`løb`-briefen forbød på forhånd at opfinde et navngivet løb med dato, efter en indledende
søgning fandt en tilsyneladende lovende kilde ("finishers.com/en/event/etna-trail"), som ved
verifikation gav **404**. Kladden fulgte forbuddet og skrev i stedet om ruter og sæson uden en
konkret konkurrence. God demonstration af, at en advarsel i researchNote/brief.angle om en
allerede-forsøgt-og-forkastet kilde forhindrer, at modellen selv falder i samme fælde.

## Historier i støbeskeen til nr. 5+

1. **(2026-08) Kreta eller storby-weekend** (Lissabon / Ljubljana) — Sicilien brugt i nr. 4.
2. **(2026-08) Læsersendte ruter** (Mallorca + senere Georgien/Dolomit).  
3. **(2026-08) Postkort-vignet** som fast bagsnit.  
4. ~~Bevidst asynk~~ → **synket 2026-08-08:** [KULTURBOXEN nr. 2](../../content/kulturboxen/issues/2026-08-nr2/) (Sydtyrol / tre sprog).

## Format

- **Faste formater:** Vandring · Cykling · Løb · Byliv · (Strande/søer/udsigter efter destination) · Kalenderen · Mad & Vin · Praktisk · **Rejsevejledning** (ny fast rubrik, se nedenfor).
- **Standard `mustCite`:** 1–2 for praktik-artikler med priser/afstande/temperaturer; 0 for stemningsartikler uden konkrete tal.
- Aldrig opdigtede præcise datoer for virkelige begivenheder.  
- **Fact-check** af stednavne og sæson før accept (chefredaktør — se [redaktion/README](../README.md)).

### Ny fast rubrik (tilføjet 2026-08-29): Rejsevejledning

**Fra nr. 5 og frem** skal hvert nummer have en **Rejsevejledning**-artikel ved siden af (ikke i
stedet for) den eksisterende Praktisk-artikel. Praktisk handler om *denne rejses* logistik
(indfaldsveje, baser, ZTL-zoner osv.); Rejsevejledning er den generiske, destinations-tilpassede
tjekliste, en dansk rejsende altid har brug for. Ejerens brief, 2026-08-29:

- **Officielle retningslinjer** fra Udenrigsministeriet, hvis en rejsevejledning findes for landet
  (`um.dk/rejse-og-ophold/rejsevejledninger`) — link direkte til den, gengiv ikke selve teksten (den
  ændrer sig og skal læses i original). Findes ingen UM-vejledning (fx det meste af Vesteuropa), sig
  det eksplicit i stedet for at opdigte en.
- **Forberedelse:** rejseforsikring, det blå EU-sygesikringskort (uden for EU: hvad det ikke dækker),
  vacciner/sundhedsråd hvis relevant.
- **Kriminalitet & sikkerhed:** lommetyveri, turistfælder, områder at være opmærksom i — kun med
  kilde (UM, lokalt politi, anerkendt rejseguide), aldrig baseret på formodning.
- **Hotelregler:** har hotellet reelt krav om at se/kopiere pas eller ID ved indtjekning i det
  pågældende land (varierer — er lovkrav visse steder, ikke andre)? Depositum, udtjekningstider.
- **Pas/ID:** gyldighedskrav (nogle lande kræver 6 mdr. tilbageværende gyldighed), om dansk kørekort
  duer, om ID skal bæres på sig.
- **Transport til/fra og i landet:** fly/tog/færge/bil fra Danmark — realistiske rejsetider og
  typiske udbydere, ikke priser der forældes (brug "tjek aktuelle priser" fremfor faste kroner der
  bliver forkerte om et år, medmindre en kilde giver et dateret spænd).
- **Prisniveau** (spænd, ikke faste tal — med kilde eller tydeligt mærket "grov tommelfingerregel"):
  hotel 3/4/5-stjernet, restaurant billig/dyr, supermarked, drikkevarer (øl/vin/kaffe ude), frisør,
  massage, **drikkepenge-norm** i landet (nogle steder forventet, andre steder ikke — det er ofte det,
  danske rejsende famler mest med).
- Samme `mustCite`-logik som Praktisk: konkrete tal og påstande om lov/regler kræver kilde.

Ikke tilføjet retroaktivt til nr. 1–4 — det er en fremadrettet standard, ikke en genudgivelses-opgave.

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

- **2026-08-29 (senere):** Ny fast rubrik besluttet: **Rejsevejledning**, fra nr. 5 og frem. Se
  `## Format` for det fulde brief (UM-vejledning hvis den findes, forberedelse, kriminalitet,
  hotel-ID-regler, pas/ID-krav, transport fra DK, prisniveau inkl. drikkepenge-norm). Ikke
  retroaktivt for nr. 1-4.
- **2026-08-29:** Nr. 4 (Sicilien) fik to rigtige kort tilføjet post-udgivelse:
  `kort-sicilien-syv-lag.svg` i `02-sicilien-overblik.md` (markerer Palermo, Etna, Noto, Agrigento,
  Siracusa — de fem stednavne, artiklens "syv lag" faktisk knytter til geografi) og `kort-baser.svg`
  i `06-byliv.md` (Palermo/Catania/Noto, de tre baser artiklen sammenligner). Genereret med det nye,
  generelle `production/generate_map.py` (Natural Earth, public domain — ikke AI-genereret, så
  kystlinjer/grænser er korrekte). Se `redaktion/README.md` → "Kort (maps)".
- **2026-08-08:** Nr. 3 publiceret — Dolomitterne genoplivet fra parked; byline DeepSeek rettet; `bestilling.json` oprettet.
- **2026-08-08 (senere):** Søster synket — KULTURBOXEN nr. 2 *Tre sprog, ét plateau* (Sydtyrol).
- **2026-08-01:** Notesbog udvidet med `## Identitet` og `## Format`; leads datostemplet (se [redaktion/README](../README.md)).
- **2026-08-01 rettelse:** `03-vandring-tramuntana.md` — GR221 var angivet til "90-100 km"; nuværende kilder angiver hovedruten til ca. 140 km (op til ~170 km med varianter). Rettet + kilde tilføjet. Puig de Massanellas højde (1.364 m, næsthøjeste) var korrekt — tilføjede kun kilde. `07-strande-skjulte-bugter.md` — tilføjede "cirka-tal, tjek på stedet"-forbehold til parkeringsprisen, samme mønster som `10-praktisk-planlaeg-turen.md`. **Ikke rettet i denne omgang:** priserne i `10-praktisk-planlaeg-turen.md` (hotel/middag/lejebil) har allerede et tilsvarende forbehold i teksten og er ikke ændret; HORISONTEN nr. 1 og nr. 2 har fortsat 0 % fodnote-dækning generelt, hvilket er en separat, større opgave end denne sessions afgrænsede rettelse af konkrete faktafejl.
- **2026-08-19:** Nr. 3 genopbygget og udgivet efter at have staaet som en tom "parked"-skal uden
  reel kommissionering. Se læringen ovenfor. Krydslink til KULTURBOXEN nr. 2 fuldført begge veje.
  Ny fast note: `.env.horisonten` har samme snævre kreditgrænse som `.env.gnisten` — brug
  `--fallback` fremfor at presse Opus-kald igennem ved 402.
