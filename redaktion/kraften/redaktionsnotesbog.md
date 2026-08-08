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
- **Artikeltal:** 12–16.  
- **Standard `mustCite`:** 2+ for MW/TWh/andels-tal; 0 for rygtebørs.

## Nr. 2 — udgivet

**Tema:** Strøm overalt  
14 artikler: leder, tallet (el-andel), Kina, Indien/syd, EU/USA, netflaskehalse, lagring, rum-solpanel, rum-kernekraft, orbital solkraft, lande-snapshot, ordbog, rygtebørs, Sverige-atom.  
Cover + 4 features (Imagine).  
`bestilling.json`: `redaktion/kraften/numre/2026-08-nr2/bestilling.json`.  
Kryds: [ORBIT nr. 2](../../content/orbit/issues/2026-08-nr2/).

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

- **2026-08-08:** Nr. 2 publiceret — global elektrificering + rumkraft-pakke.
- **2026-08-01:** Notesbog udvidet med `## Format`.

- **2026-08-08 (edit):** KRAFTEN nr. 2 — forklaret *Fit for 55* og *IRA* i EU/USA-artiklen; udfoldet *PJM-agtige køer* i netflaskehalse; Sverige-atom omskrevet fra notes-kladde til færdig feature og flyttet **før** Ordbog/Rygtebørs (lå tidligere som sidste side efter bagsnit).

