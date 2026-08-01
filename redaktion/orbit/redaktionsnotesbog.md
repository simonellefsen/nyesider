# ORBIT – Redaktionsnotesbog

Ny titel under Nye Sider (oprettet august 2026). Endnu intet udgivet nummer.  
Modelerfaringer: [modelkartotek](../modelkartotek.md).  
OpenRouter: **kun** `.env.orbit`. Imagine: `XAI_API_KEY` i `.env.local`.

## Identitet

**ORBIT** er magasinet om **rumfart som industri, geopolitik og teknik** — ikke sci-fi-romantik alene.

### Kerne

| Søjle | Indhold |
|---|---|
| **Opsendelser** | SpaceX, Blue Origin, Rocket Lab, nationale bæreraketter; cadence, fejl, comeback |
| **Nationer & agencer** | NASA, ESA (+ medlemslande), ISRO (Indien), CNSA/Kina, Roscosmos/Rusland, kommercielle spillere |
| **Satellitter** | Starlink/OneWeb-klassen, earth observation, navigation, militær light-touch, “new space” busser |
| **Rumskrot** | Debris, conjunctions, guidelines, oprydningskoncepter — tal + politik |
| **Kalenderen** | Kommende vinduer/missioner med **omtrentlige** datoer og kilde; aldrig opdigtede præcise launches |
| **Tallet** | Opsendelser/år, masse til kredsløb, aktive satellitter, fejlrate |
| **Sådan virker det** | Diagrammer: trin, LEO/MEO/GEO, docking, genbrugelige trin, heat shield |

### Afgrænsning over for KRAFTEN

| ORBIT | KRAFTEN |
|---|---|
| Raketter, opsendelser, agencer, sats, debris, missioner | Elektrificering på Jorden + **rumkraft** (paneler, RTG, surface power) |
| “Hvem sendte hvad, hvornår, hvorhen” | “Hvor kommer watt fra — også i rummet” |

**Overlap er OK** (fx solpaneler på ISS, nuklear rumkraft): ORBIT vinkler mission/ops; KRAFTEN vinkler energi/watt. Krydshenvis gerne mellem titlerne.

Tone: nøgtern, kildetung (NASA/ESA/CASC/ISRO/company updates, Jonathan’s Space Report-agtige stats, Space-Track/offentlige debris-tal). Hardware før hype.

## Visuel linje

**Standard: xAI Imagine** (copyright).

- Pads, stack, boosters, fairings (uden mærkelogoer i AI-art hvor muligt)  
- Kredsløbs- og trin-**diagrammer** (Imagine eller rene SVG’er som GNISTEN)  
- Satellit-konstellationer som stiliserede lag — ikke forveksle med præcis katalog-plot  
- Rumskrot: illustrative skyer/fragmenter, ikke fake “NASA photo #123”  

Hvert nummer: egen forside `images/orbit_cover.png` styret af `issueTheme`.  
Kreditering: `imageCredit` + `imageSource` (Imagine / xAI → `https://x.ai/`).

## Faste formater

- **Kalenderen** — 5–8 poster, “omtrentligt / tjek live manifest”  
- **Tallet** — ét nøgletal + 3–5 sætninger  
- **Sådan virker det** — 1 diagram + kort prosa  
- **Ordbogen** — 8–12 gloser (LEO, GTO, payload, rideshare, Kessler …)  
- **Rygtebørsen** — firmaer/agencer/teknologiløfter, aldrig privatpersoner som mål  

## Udkast til nr. 1 (arbejdstitel: *"Cadence"*)

Mål **12–14 artikler**:

1. **Leder** — Velkommen til ORBIT: hvorfor cadence og debris er samme historie  
2. **Tallet** — globale opsendelser seneste fulde år (kilde + årstal)  
3. **SpaceX: fabriksrytmen** — Falcon/Starship-status uden pressemeddelelsessprog  
4. **Blue Origin** — New Glenn / New Shepard: hvor er hardware?  
5. **NASA** — flagskibsmissioner + kommercielt LEO  
6. **ESA** — Ariane/Vega/europeisk adgang til rummet  
7. **Indien (ISRO)** — cadence og cost-effekt  
8. **Kina** — opsendelser, station, måne-spor  
9. **Rusland** — kapacitet under pres  
10. **Satellitter: mega-konstellationer** — kapacitet vs. sky/astronomi/debris  
11. **Rumskrot** — hvor slemt, hvem rydder op  
12. **Sådan virker det: baner (LEO/MEO/GEO)** — diagram  
13. **Kalenderen** — næste kvartals højdepunkter (med forbehold)  
14. **Ordbogen** + **Rygtebørsen** (flow)

## Research-regler

- Opsendelser: skeln **planlagt / scrub / success / failure**; link til primær kilde.  
- Aldrig opdigtede launch-datoer — “forventet Qx / net window, tjek manifest”.  
- Nationer: adskil **civil, kommerciel, militær** når kilden tillader det.  
- Diagrammer: label på dansk i SVG hvis præcision kræves; ellers Imagine + kort figurtekst.

## Status

- [x] `magazine.json` + brand (ORBIT, mørk navy / blå accent / guld highlight)  
- [x] Redaktionsnotesbog + nr. 1-outline  
- [x] `.env.orbit` (OpenRouter — brugerens nøgle)  
- [ ] Første nummer produceret  
- [ ] Cover + PDF  
