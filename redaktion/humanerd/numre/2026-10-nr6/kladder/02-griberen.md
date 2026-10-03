# Fabrikken: Robotarmen der skal lære at gribe forskel

Opgaven lyder enkel, indtil man prøver den selv: tag én vare op af en kasse fyldt med rod — en paperback, en plastikflaske shampoo, en blød pose med tørrede nødder — og læg den et nyt sted uden at tabe den, mase den eller flå emballagen. For en menneskehånd er det rutine. For en robotarm er det et af de sværeste problemer i lagerautomatisering, fordi hver vare har sin egen form, vægt, overflade og skrøbelighed, og fordi varerne i en Amazon-kasse aldrig ligger pænt sorteret.

Det er den opgave, Amazons robotarm Sparrow er bygget til at løse. Amazon præsenterede Sparrow i november\u00a02022 og beskrev den som virksomhedens første system, der kan detektere, udvælge og håndtere enkeltvarer i et usorteret miks — ikke bare flytte hele kasser eller paller, som ældre robotgenerationer gør.[^1]

## Øje, hjerne og sugekop

Sparrow kombinerer computervision (kameraer der genkender objekter) og kunstig intelligens (AI) med en specialbygget griber med flere sugekopper. Systemet skal først "se" hvad der ligger i kassen, beregne hvor en vare kan gribes uden at glide eller knuses, og derefter udføre grebet — alt sammen inden for få sekunder, og med en skrøbelig badebold lige så ofte i kassen som en hård bogryg. Ifølge Amazons egne oplysninger kan Sparrow håndtere omkring 65\u00a0% af det varesortiment, systemet er trænet på — et tal, der afspejler netop variationen i størrelse og materiale, snarere end en teoretisk grænse for teknologien.[^1]

Det tal er vigtigt at læse rigtigt: det er en virksomhedsoplyst dækningsgrad, ikke en uafhængigt målt succesrate for enkeltgreb, og det siger ikke noget om de resterende varer, som stadig kræver menneskehænder eller andre løsninger.

## Fra Texas-pilot til Louisiana-drift

Sparrow blev først afprøvet i et lager i Richmond, Texas, i 2023 — en pilotfase, hvor systemet blev testet på rigtige ordrer, men i begrænset omfang. Siden er teknologien flyttet videre til det, Amazon selv kalder sit mest avancerede lager, i Shreveport, Louisiana. Her indgår Sparrow-arme i dag i kommerciel drift, hvor de konsoliderer varer mellem kasser — altså flytter enkeltvarer fra én beholder til en anden som led i sorteringsprocessen.[^2]

Det er værd at holde to ting adskilt. Konsolidering mellem kasser er i kommerciel brug i Shreveport. Det fulde enkeltvare-pluk direkte til kundeordrer — hvor Sparrow selv udvælger den præcise vare en kunde har bestilt, og sender den videre i emballeringskæden — er stadig under udrulning og ikke dokumenteret som stabil drift i hele Amazons netværk. Forskellen mellem en robot, der konsoliderer i ét lager, og en robot, der plukker kundeordrer i hele flåden, er netop den slags distinktion, der ofte drukner i pressemeddelelser.

## Søskende, ikke tvillinger

Sparrow er ikke alene i Amazons robotfamilie, og det er en hyppig kilde til forveksling. Robin, som blev taget i brug i et lager i Lakeland, Florida, i 2022, sorterer pakker efter de er pakket — en helt anden delopgave end Sparrows enkeltvare-pluk før pakning. Cardinal, introduceret i Nashville samme år, stabler kasser i vogne klar til forsendelse. De tre systemer løser hver sin del af kæden fra lagerhylde til leveringsbil, og ingen af dem kan erstatte de andres funktion.[^1]

Det samlede billede af automatisering hos Amazon er stort: i februar\u00a02025 oplyste virksomheden selv, at den havde over 750.000 robotter i sin flåde — langt hovedparten mobile drive-enheder, der kører reoler og kasser rundt på lagergulvet, en arv fra opkøbet af Kiva Systems i 2012.[^3] Det tal dækker altså primært transport, ikke de mere komplekse grib-og-plukopgaver, som Sparrow, Robin og Cardinal repræsenterer. Fysisk AI i et lager handler sjældent om én magisk robot, der kan det hele — det handler om mange specialiserede systemer, der løser hver deres smalle, veldefinerede opgave, og hvor den egentlige nyhedsværdi ofte ligger i, hvor langt den enkelte opgave er flyttet fra pilot til drift.

---

[^1]: Amazon, "Introducing Sparrow, a robotic system that handles a variety of items in Amazon's warehouses", Amazon.com (pressemeddelelse/blogindlæg), november 2022.
[^2]: Amazon, om lageret i Shreveport, Louisiana og brugen af Sparrow-arme til konsolidering — Amazon.com, virksomhedsomtale af lagerets robotteknologi.
[^3]: Amazon, pressemeddelelse om robotflådens størrelse, februar 2025, Amazon.com.