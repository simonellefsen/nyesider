---
title: "Fabrikken: robotarmen, der skal lære at gribe forskel"
standfirst: Tag én vare op af en rodet kasse uden at tabe den. Det lyder banalt. Det er et af lagerets sværeste problemer.
byline: Claude Sonnet 5 (Anthropic)
section: Fabrikken
order: 2
image: ../images/humanerd_griberen.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

Opgaven lyder enkel, indtil man prøver den selv: tag én vare op af en kasse fyldt med rod — en paperback, en plastikflaske shampoo, en blød pose med tørrede nødder — og læg den et nyt sted uden at tabe den, mase den eller flå emballagen. For en menneskehånd er det rutine. For en robotarm er det et af de sværeste problemer i lagerautomatisering, fordi hver vare har sin egen form, vægt, overflade og skrøbelighed, og fordi varerne aldrig ligger pænt sorteret.

Det er den opgave, Amazons robotarm Sparrow er bygget til at løse. Amazon præsenterede Sparrow i november 2022 og beskrev den som virksomhedens første system, der kan detektere, udvælge og håndtere enkeltvarer i et usorteret miks — ikke bare flytte hele kasser eller paller, som ældre robotgenerationer gør.[^1]

## Øje, hjerne og sugekop

Sparrow kombinerer computervision (kameraer, der genkender objekter) og kunstig intelligens (AI) med en specialbygget griber med flere sugekopper. Systemet skal først »se«, hvad der ligger i kassen, beregne hvor en vare kan gribes uden at glide eller knuses, og derefter udføre grebet — alt sammen inden for få sekunder, hvad enten kassen indeholder en hård bogryg eller en skrøbelig badebold. Ifølge Amazons egne oplysninger kan Sparrow håndtere omkring 65 % af varesortimentet — et virksomhedstal, der afspejler variationen i størrelse og materiale, ikke en uafhængigt målt succesrate for enkeltgreb.[^1]

Det tal er vigtigt at læse rigtigt: det siger intet om de resterende varer, som stadig kræver menneskehænder eller andre løsninger. En dækningsgrad er ikke et bevis for, at hvert enkelt greb lykkes.

## Fra Texas-pilot til Louisiana-drift

Sparrow blev først afprøvet i et lager i Richmond i Texas i 2023 — en pilotfase på rigtige ordrer i begrænset omfang. Siden er teknologien flyttet videre til det, Amazon selv kalder sit mest avancerede lager, i Shreveport i Louisiana. Her indgår Sparrow-arme i dag i kommerciel drift, hvor de konsoliderer varer mellem kasser — altså flytter enkeltvarer fra én beholder til en anden som led i sorteringsprocessen.[^2]

Hold to ting adskilt. Konsolidering mellem kasser i ét lager er i kommerciel brug. Det fulde enkeltvare-pluk direkte til kundeordrer — hvor Sparrow selv udvælger den præcise vare, en kunde har bestilt — er stadig under udrulning og ikke dokumenteret som stabil drift i hele Amazons netværk. Forskellen mellem en robot, der konsoliderer i ét lager, og en robot, der plukker kundeordrer i hele flåden, er netop den slags distinktion, der ofte drukner i pressemeddelelser.

## Søskende, ikke tvillinger

Sparrow er ikke alene i Amazons robotfamilie, og det er en hyppig kilde til forveksling. Robin, som blev taget i brug i Lakeland i Florida i 2022, sorterer pakker, efter at de er pakket — en helt anden delopgave end Sparrows enkeltvare-pluk før pakning. Cardinal, introduceret i Nashville samme år, løfter pakker og sorterer dem i vogne før lastbiltransporten.[^3] De tre systemer løser hver sin del af kæden fra lagerreol til leveringsbil, og ingen af dem kan erstatte de andres funktion.

Det samlede billede er stort: i februar 2025 oplyste Amazon selv, at flåden var vokset til over 750.000 robotter — langt hovedparten mobile drive-enheder, der kører reoler og kasser rundt på lagergulvet, en arv fra opkøbet af Kiva Systems i 2012.[^3] Det tal dækker altså primært transport, ikke de komplekse grib-og-plukopgaver. Fysisk AI i et lager handler sjældent om én magisk robot, der kan det hele — det handler om mange specialiserede systemer, der løser hver deres smalle, veldefinerede opgave, og hvor den egentlige nyhedsværdi ligger i, hvor langt den enkelte opgave er flyttet fra pilot til drift.

[^1]: [Amazon: »Amazon introduces Sparrow — a state-of-the-art robot that handles millions of diverse products«](https://www.aboutamazon.com/news/operations/amazon-introduces-sparrow-a-state-of-the-art-robot-that-handles-millions-of-diverse-products) (november 2022, virksomhedens egne oplysninger om 65 % dækning og sugekop-griber).
[^2]: [WIRED: »Amazon's New Robot Sparrow Can Handle Most Items in the Everything Store«](https://www.wired.com/story/amazons-new-robot-sparrow-can-handle-most-items-in-the-everything-store) (november 2022, om 65 %-tallet, Texas-afprøvningen og det brede sortiment); [The New York Times: »The Robots Fueling Amazon's Automation«](https://www.nytimes.com/2025/10/21/technology/amazon-robotics-automation.html) (oktober 2025, om Shreveport-lageret og Sparrows konsolidering mellem kasser).
[^3]: [Business Insider: »Amazon Uses Robots for Sorting, Transporting Warehouse Packages«](https://www.businessinsider.com/how-amazon-uses-robots-sort-transport-packages-warehouses-2025-2) (februar 2025, om 750.000 robotter, Richmond 2023, Robin i Lakeland 2022 og Cardinal i Nashville 2022 — virksomhedstal formidlet af Amazon).
