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

## Nr. 1 — udgivet

*"Hvad holder lyset tændt"* — 14 artikler om EU-mix, atom, gas, vind, sol, lagring, DK.

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

