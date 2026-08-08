---
title: "Sådan virker det: LEO, MEO og GEO"
standfirst: Tre etager over Jorden, tre jobbeskrivelser. Hvorfor ligger GPS ikke tættere på? Hvorfor kræver Starlink tusinder af satellitter, når tre kan dække kloden? Og hvorfor forsvinder skrot i lav bane af sig selv?
section: Sådan virker det
order: 10
figures:
  - ../images/figur_baner.svg
---

Satellitter omtales, som om de svæver «deroppe» i én stor, udifferentieret sky.

De gør de ikke. Rummet omkring Jorden har tre etager, og hvilken etage en satellit bor på, afgør stort set alt ved dens arbejde: hvor meget den kan se, hvor hurtigt signalet når frem, og hvor længe skrottet efter den bliver liggende.

[FIGUR 1]

*Skitse — ikke i skala.*

### LEO: den travle etage

**LEO**, Low Earth Orbit, regnes normalt fra omkring **160 til 2.000 kilometer**, men langt hovedparten af trafikken ligger under 1.000.[^1]

Det er tæt på. Til sammenligning måler Danmark cirka 360 kilometer fra Skagen til Gedser. En satellit i LEO befinder sig altså ofte i en afstand, der svarer til landets egen længde.

I den højde er omløbstiden **90–120 minutter**. En LEO-satellit runder hele kloden 15–16 gange i døgnet.

Hvorfor betyder lavere bane hurtigere omløb? Fordi tyngdekraften er stærkere tættere på. En satellit falder hele tiden mod Jorden — den rammer bare aldrig, fordi den samtidig bevæger sig sidelæns hurtigt nok til, at Jorden krummer væk under den. Jo stærkere træk, jo hurtigere skal den bevæge sig for at ramme forbi. Månen, 384.000 kilometer ude, mærker et så svagt træk, at den kan nøjes med knap en måned per omgang.

Nærheden er både styrken og svagheden.

**Styrken** er lav forsinkelse: signalet har kort vej. Det er hele forudsætningen for internetkonstellationer.

**Svagheden** er udsyn. En LEO-satellit ser kun et lille stykke af Jorden ad gangen — og haster videre. Et globalt dækkende system kræver derfor tusinder af satellitter i et konstant relæløb, hvor den næste tager over, når den forrige er ude af syne. Det er derfor [Starlink](/orbit/2026-08-nr1/satellitter) tælles i titusinder og ikke i dusiner.

Og så en detalje, der får konsekvenser i [rumskrot](/orbit/2026-08-nr1/rumskrot): der er stadig atmosfære i disse højder. Meget tynd, men nok til at bremse. Det atmosfæriske træk trækker langsomt satellitter og fragmenter ned, indtil de brænder op. LEO er med andre ord den eneste etage, der rydder op efter sig selv — over år eller årtier, afhængigt af højden.

### MEO: navigationens kompromis

**MEO**, Medium Earth Orbit, er hjemsted for navigationssystemerne: amerikanske **GPS**, europæiske **Galileo**, russiske **GLONASS** og kinesiske **BeiDou**. GPS-satellitterne ligger omkring **20.200 kilometer** oppe med en omløbstid på cirka 12 timer.[^2]

Hvorfor lige dér? Fordi navigation stiller et bestemt krav: en modtager på jorden skal kunne se **mindst fire satellitter samtidig** for at beregne sin position. Ikke tre — fire, fordi den fjerde bruges til at korrigere modtagerens eget ur.

Ligger satellitterne for lavt, ser man for få ad gangen, og systemet kræver tusinder. Ligger de for højt, bliver signalet svagt og geometrien dårlig. MEO er kompromiset, der gør global navigation mulig med nogle få dusin satellitter i stedet for tusindvis.

### GEO: satellitten der står stille

Den tredje etage er **GEO**, den geostationære bane, i **35.786 kilometers** højde — og kun over Ækvator.[^1]

Her er omløbstiden præcis lige så lang som Jordens egen rotation. Bemærk: det er **23 timer, 56 minutter og 4 sekunder** — et *stjernedøgn* — og ikke de 24 timer, vi går efter i hverdagen. Forskellen på de knap fire minutter skyldes, at Jorden samtidig flytter sig i sin bane om Solen.[^3]

Resultatet er, at satellitten hænger fast over det samme punkt på jordoverfladen. Derfor kan en parabol pege ét fast sted op på himlen og blive der.

Stilstanden koster afstand. Et signal op og ned igen tilbagelægger over **71.000 kilometer** og bruger derfor omkring **et kvart sekund** frem og tilbage — mærkbart i et telefonopkald eller et videomøde, og præcis det problem, LEO-konstellationerne er bygget for at omgå.

Til gengæld er udsynet enormt: fra GEO ser en satellit omkring en tredjedel af kloden. Tre rigtigt placerede satellitter dækker næsten hele den beboede verden. Det er grunden til, at vejr- og tv-satellitter traditionelt sidder her.

Men der er ingen atmosfære til at bremse noget som helst. Skrot i GEO bliver liggende **i praksis for altid**, medmindre det aktivt flyttes op i en såkaldt kirkegårdsbane, når det pensioneres.

### De tre kompromiser

| | Højde | Omløbstid | Betaler med |
|---|---|---|---|
| **LEO** | 160–2.000 km | 90–120 min | Kræver tusinder af satellitter |
| **MEO** | ca. 20.200 km (GPS) | ca. 12 timer | Svagere signal, færre opgaver |
| **GEO** | 35.786 km | et stjernedøgn | Kvart sekunds forsinkelse — og evigt skrot |

Kadencen i 2025 var først og fremmest en LEO-historie. Det er også dér, regningen samler sig.

[^1]: [Types of orbits](https://www.esa.int/Enabling_Support/Space_Transportation/Types_of_orbits), ESA — LEO, MEO og GEO med højder og omløbstider, herunder den geostationære bane i 35.786 km over Ækvator. Se også [Orbits](https://www.earthdata.nasa.gov/learn/earth-observation-data-basics/orbits), NASA Earthdata.
[^2]: GPS-satellitternes banehøjde på ca. 20.200 km og omløbstid på ca. 12 timer: [GPS.gov](https://www.gps.gov/), det amerikanske nationale koordinationskontor for satellitnavigation, og [Global Positioning System](https://en.wikipedia.org/wiki/Global_Positioning_System). Kravet om mindst fire synlige satellitter følger af, at modtagerens egen urfejl er den fjerde ubekendte ved siden af de tre rumkoordinater.
[^3]: [Sidereal time](https://en.wikipedia.org/wiki/Sidereal_time) — stjernedøgnet på 23 t 56 min 4 sek er Jordens rotationstid i forhold til stjernerne; det er den, en geostationær satellit skal matche.
