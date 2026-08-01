# KRAFTEN – Redaktionsnotesbog

Opdateret august 2026 — **fokus skærpet:** global elektrificering + rumkraft. Modelerfaringer: [modelkartotek](../modelkartotek.md).

## Identitet

**KRAFTEN** er magasinet om **elektrificering** — hvordan strøm erstatter fossil energi i transport, varme, industri og hverdag, **på tværs af lande**, og hvordan den samme logik rækker **ud i rummet**.

### Kerne

| Søjle | Indhold |
|---|---|
| **Elektrificering globalt** | El-andelen af endeligt energiforbrug; EV- og varmepumpe-udrulning; industri-el; byer og havne; hvem går hurtigst (Kina, EU, US, Indien, Afrika, Golf …) med **tal** |
| **Systemet bag stikket** | Net, baseload, vedvarende, atom, lagring, gas som flex — altid set som *input til elektrificering*, ikke som isoleret energifetish |
| **Rumkraft / Space** | Solpaneler på satellitter og stationer; kernekraft til dybe missioner (RTG, fission surface power); orbital solkraft-koncepter; strøm til måne-/Mars-baser; data centre / downlink-energi-vinkler hvor det er reelt |

### Afgrænsning

- **Ikke SPÆNDING:** bilmodeller, køretest og danske afgifter på personbiler hører primært i SPÆNDING. KRAFTEN kan nævne EV-salg som *elektrificeringsindikator*, men dykker i net, TWh og lande — ikke i Twin go vs. Leaf.
- **Ikke ORBIT (fuld rumfart):** opsendelser, agenturer, satellit-konstellationer, debris og launch-kalender hører i **ORBIT**. KRAFTEN tager **rumkraft** (watt på satellitter, RTG, surface power). Overlap er OK — vinkel forskellig; krydshenvis.
- **Fossilt** dækkes, når det forklarer tempo, flaskehalse eller backup — ikke som olie-/gas-magasin i sig selv.
- Tone: nøgtern, kildetung, global. Ingen hype uden hardware.

## Format

- **Ordmål:** Features 500–750 ord; bagsnit `flow: true`.
- **Artikeltal:** typisk 12–16.
- **Standard `mustCite`:** 2+ for enhver artikel med MW/TWh/andels-tal (se Research-regler nedenfor — kilde + årstal er allerede påkrævet, dette gør det eksplicit pr. artikel før bestilling); 0 for rygtebørs.

## Visuel linje

**Kun xAI Imagine** (`.env.local` → `XAI_API_KEY`). Se [redaktion/README.md](../README.md).

Prioritér:

- Anlæg og maskiner (kraner, turbiner, BESS, master)  
- **Globale scener:** bynet, havne-el, toglinjer, fabrikker under el-omstilling  
- **Rum:** satellitter med paneler, landere, habitat-koncepter, jordstationer — dokumentarisk/editorial, ikke ren sci-fi-plakat uden kontekst  

### Forside (skifter hvert nummer)

Egen `images/kraften_cover.png` pr. issue, styret af `issueTheme`. Brand: mørk grøn-sort, amber `#E3A008`, teal. Ingen masthead-tekst i billedet. `coverCredit` + `coverSource` påkrævet.

Nr. 1-forside: net/lys/køletårn/vind — «systemet der holder lyset tændt».

## Nr. 1 — udgivet (fundament)

Thorium-artiklen opdateret med **Copenhagen Atomics** (MSR, tidslinje, PSI-demo ~2028, kommerciel tidligt 2030'erne — selskabets pejlinger).


*"Hvad holder lyset tændt"* — 14 artikler om EU-mix, atom, gas, vind, sol, lagring, DK. God base for **systemet**. Mindre eksplicit om global elektrificerings-kurve og rum (det kommer i nr. 2+).

## Nr. 2 — i støbeskeen (*arbejdstitel: "Strøm overalt"*)

Mål 12–16 artikler. Forslag:

1. **Leder** — Elektrificering som århundredets infrastrukturprojekt (jord + rum)  
2. **Tallet** — el-andel af global endelig energi / stigningstakt (IEA)  
3. **Kina** — verdens største elektrificeringsmaskine (EV, HSR, industri, sol/vind-GW)  
4. **Indien & det globale syd** — netadgang, peak demand, spring over fossil?  
5. **EU** — Fit for 55 i praksis: varmepumper, industri, netkøer  
6. **USA** — IRA-efterspil, data centre vs. husholdninger  
7. **Netflaskehalse** — hvor elektrificering møder tilladelse og stål  
8. **Lagring til et elektrisk samfund** — timer vs. sæson  
9. **Rum: satellittens solpanel** — hvordan missioner får watt i dag  
10. **Rum: kernekraft til dybe missioner** — RTG vs. fission surface power (NASA/ESA-spor)  
11. **Orbital solkraft** — hype vs. demonstrationsplaner  
12. **Lande-snapshot-tabel** — 6 lande, samme elektrificerings-indikatorer  
13. **Ordbogen** — electrification rate, final energy, RTG, ISP, curtailment …  
14. **Rygtebørsen**  
15. **Sverige: atomudbygningens lange vej** — regeringens mål, mulig ny kapacitet, finansiering, elnet og lokalsamfund. Skeln konsekvent mellem politisk ramme, ansøgning, myndighedsgodkendelse, investeringsbeslutning, anlæg under byggeri og MW i faktisk drift; sammenlign med Sverige, Danmark og EU uden at gøre mål til megawatt.

## Research-regler

- Tal med **kilde + årstal** (IEA, Ember, IRENA, nationale agenturer, NASA/ESA pressemeddelelser for rum).  
- Skeln nameplate MW / TWh / planlagt / under byggeri / i drift.  
- Rum: skeln **operationel hardware** fra PowerPoint-koncepter.  
- Svensk atomkraft: brug svenske myndigheder og systemoperatør, reaktoroperatører samt lov-/budgetmateriale som primærkilder; angiv altid dato og status for hver reaktor eller udvidelse.  
- OpenRouter: **kun** `.env.kraften`. Imagine: `.env.local`.

## Tendensdiagrammer (online)

Se [content/CHARTS.md](../../content/CHARTS.md).

- **Kanonisk data:** `content/kraften/issues/<issue>/charts/<id>.json`  
- **I artiklen:** `[CHART id]`  
- Web: `TrendChart.svelte` (hover). Frontmatter-`charts` kun som undtagelse/override.

## Praktisk

- `python production/load_env.py kraften`  
- PDF: `build_magazine.py kraften <issue-slug>`

## Log

- **2026-08-01:** Notesbog udvidet med `## Format` (fælles skabelon, se [redaktion/README](../README.md)); ordmål/mustCite konsolideret her fra `## Praktisk`.  
