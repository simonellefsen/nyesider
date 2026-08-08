# KRAFTEN – Redaktionsnotesbog

Opdateret efter nr. 2 (august 2026, *"Strøm overalt"*). Modelerfaringer: [modelkartotek](../modelkartotek.md).

## Identitet

**KRAFTEN** er magasinet om **elektrificering** — hvordan strøm erstatter fossil energi i transport, varme, industri og hverdag, **på tværs af lande**, og hvordan den samme logik rækker **ud i rummet**.

### Afgrænsning

- **Ikke SPÆNDING:** bilmodeller og danske afgifter → SPÆNDING.  
- **Ikke ORBIT (fuld rumfart):** opsendelser/katalog → ORBIT. KRAFTEN tager **rumkraft** (watt).  
- Tone: nøgtern, kildetung, global.

## Format

- **Ordmål:** Features 200–400 i batch (sigt 500–750 når der er tid).  
- **Artikeltal:** 12–16. **Ingen Ordbog** — gloser i parentes/fodnote.  
- **Standard `mustCite`:** 2+ for MW/TWh/andels-tal; 0 for rygtebørs.

## Nr. 2 — udgivet

**Tema:** Strøm overalt  
13 artikler: leder, tallet (el-andel), Kina, Indien/syd, EU/USA, netflaskehalse, lagring, rum-solpanel, rum-kernekraft, orbital solkraft, lande-snapshot, Sverige-atom, rygtebørs. (Ordbogen fjernet 2026-08-08.)  
Cover + feature-billeder (Imagine).  
`bestilling.json`: `redaktion/kraften/numre/2026-08-nr2/bestilling.json`.  
Kryds: [ORBIT nr. 2](../../content/orbit/issues/2026-08-nr2/).

**Depth-pass (samme dag som publicering):** Features var for tynde efter batch-udgivelse. Omskrevet: Indien (fjernet meta-«Læseregler», prosa med adgang/peak/leapfrog + kilder); Sverige-atom (6 reaktorer ~7 GW, ~29 % el 2024, Nordic Baseload Power 2×~2 500 MWe Barsebäck-støtteansøgning juni 2026); øvrige features udvidet til magasinlængde.

## Nr. 1 — genopbygget og genudgivet 2026-08-09

**Tema:** Hvad holder lyset tændt
**13 artikler, 9.701 ord** (var 14 artikler / 4.165 ord — gns. 297). Ordbogen fjernet.
Tolv artikler reelt kommissioneret på `.env.kraften`; lederen er chefredaktionens og har **ingen byline**.
Samlet forbrug **0,54 USD** — ledgersummen stemmer på øren med `GET /api/v1/key`.
`bestilling.json`: `redaktion/kraften/numre/2026-08-nr1/bestilling.json`.

Den oprindelige udgave havde **ingen `bestilling.json`** — ingen brief, intet verdikt, ingen kvittering —
men bar byline til navngivne modeller.

### Hvad der virkede

**Skriv tallene ind i `brief.angle`, ikke i `researchNote`.** `researchNote` når aldrig frem til
modellen. Efter den ændring ramte `europa-mix` alle syv tal i første forsøg og leverede den første
kladde i hele genopbygningen uden en eneste gættet URL.

### Hvad faktatjekket fangede

Fejlmønstret var **ikke** sprogligt. Det var kilder og årstal:

- **Bare domænehenvisninger** i stedet for kilder («Se iea.org») i fire kladder. Ubrugeligt for læseren.
- **Rigtigt tal, forkert rapport:** sol-kladden tilskrev IEA-tal til *Renewables 2024*; de står i
  *Electricity 2026*. Gas-kladden satte 17 % gasandel til 2023; det er 2025-tallet.
- **Forældede tal:** fusionsbranchens investeringer stod til «over 6 mia. dollar» fra en rapport fra
  2023. Facit er 14,24 mia., heraf 4,48 mia. rejst alene i året frem til juli 2026.
- **Gættede URL'er:** energy.gov om andekurven, Eurostat om energiforbrug, IAEA om tritium — alle 404.

### Hvad der er værd at gentage

`lande`-kladden **nægtede at udfylde landeskemaet** med tal, den ikke kunne kildebelægge, og skrev
begrundelsen ind i artiklen: *«en falsk-præcis procent er værre end en åben beskrivelse.»* Redaktionen
har derefter fundet de tal, der kunne findes (Kina 22 %, OECD 20 %), og ladet resten stå tomt med
begrundelsen. Det er den rigtige rækkefølge.

## Nr. 3 — kandidater

- **(2026-08) Data centre vs. husholdninger — regionale case**  
- **(2026-08) Havne-el / shore power**  
- **(2026-08) Afrikanske netadgangs-spring**  
- **(2026-08) Svensk atom — status når ansøgninger lander**

## Research-regler

Tal med **kilde + årstal**. Skeln nameplate MW / TWh / planlagt / under byggeri / i drift.  
OpenRouter: **kun** `.env.kraften`. Imagine: `.env.local`.

## Log

- **2026-08-08 (format):** Ordbogen fjernet fra nr. 2 — gloser i parentes/fodnote i features (ikke separat ordliste).


- **2026-08-08:** Nr. 2 publiceret — global elektrificering + rumkraft-pakke.
- **2026-08-01:** Notesbog udvidet med `## Format`.

- **2026-08-08 (edit):** KRAFTEN nr. 2 — forklaret *Fit for 55* og *IRA* i EU/USA-artiklen; udfoldet *PJM-agtige køer* i netflaskehalse; Sverige-atom omskrevet fra notes-kladde til færdig feature og flyttet **før** Ordbog/Rygtebørs (lå tidligere som sidste side efter bagsnit).
- **2026-08-08 (process):** Efter Sverige-kladde-uheldet: `production/check_issue.py` flagger nu **draft/production-meta** i publiceret brødtekst som ERROR; chefredaktør-tjekliste i [redaktion/README](../README.md) kræver eksplicit “færdig læsertekst” + jargon første gang + features før bagsnit.
- **2026-08-08 (depth):** Features stadig for korte efter batch. Indien: Læseregler væk → prosa. Sverige: flåde (6 reaktorer, Forsmark/Ringhals/Oskarshamn, ~50 TWh/~29 %) + Nordic Baseload Power (Barsebäck, ~2 500 MWe, 4. støtteansøgning juni 2026). Kina, lagring, rum-pakke, tallet, snapshot udvidet.

