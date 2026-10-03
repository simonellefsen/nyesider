---
title: "Hjernen: hvorfor robotten skal mærke varen, før den kan løfte den"
standfirst: Kameraer giver robotten syn. Men uden følesans ender den som en blind klo, der enten knuser eller taber.
byline: Qwen3.7 Max (Alibaba)
section: Hjernen
order: 4
image: ../images/humanerd_foelesansen.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

Kameraer og laserscannere (LiDAR — *Light Detection and Ranging*, afstandsmåling med laserlys) har givet robotterne syn. Men i et rigtigt plukkeskift på et lager er syn sjældent nok. Hvis en robotarm udelukkende styres af 3D-punktsskyer og billedgenkendelse, ender den som en blind klo, der enten klemmer, til den knuser emnet, eller taber det, når friktionen ændrer sig. Fysisk kunstig intelligens (AI) kræver en sans, der ofte overses i de polerede demovideoer: følesansen. For at en robot kan sanse, beregne, planlægge, bevæge sig og stoppe sikkert, skal den kunne mærke kontakt, tryk, slip og vibration.

I den kommercielle robotstak følger en fast kæde, når en vare skal flyttes: syn → grebsplanlægning → føling → slip-detektion → gen-greb. Det er her, de taktile sensorer træder ind. Når en robot forsøger at løfte en uigennemsigtig flaske, kan kameraet ikke se, om væsken indeni skvulper eller står stille. Vægtfordelingen afsløres først i det øjeblik, griberen løfter. Her fungerer de taktile sensorer som robottens perifere nervesystem og oversætter fysisk kontakt til elektriske signaler, så styresystemet kan reagere i millisekunder.

Et af de mest udbredte kommercielle eksempler er Robotiqs 2F-85-griber. Ifølge producentens egne oplysninger har den en slaglængde på 85 millimeter, en griberkraft på 20–235 N (newton, enheden for kraft) og en nyttelast på op til 5 kilo.[^1] Men metallet alene føler ingenting. Derfor monteres der i stigende grad taktile fingerspidser som Robotiq TSF-85: et kapacitivt sensorarray, der måler tryk, slip og vibration, og som ifølge Robotiq sampler med 1.000 Hz — altså tusind målinger i sekundet.[^2] Virksomheden oplyser selv at have leveret over 23.000 gribere globalt — et virksomhedstal, der placerer teknikken i kategorien kommerciel installation frem for laboratorieforsøg.[^1]

Sensorerne er kun halvdelen af hjernen. Datastrømmen skal fortolkes af en model, der forstår konteksten. Her er Covariant Brain et af de mest dokumenterede eksempler: en AI-platform, der ifølge Covariant selv er trænet på millioner af greb fra lagre verden over og kører hos kunder i 15 lande på tværs af 4 kontinenter.[^3] Hos den tyske detailkoncern Otto Group rulles Covariant-styrede robotter ud til ordrepluk, blandt andet på anlægget i Haldensleben, med et erklæret mål om over 100 AI-robotter i koncernens lagre — virksomhedstal, der beskriver en kommerciel udrulning, ikke et afsluttet resultat.[^3] Pointen i denne sammenhæng: kameraet foreslår et greb, følesansen korrigerer det undervejs, og flåden deler læringen, så næste robot ikke begår den samme fejl.

Skeln samtidig skarpt til de humanoide fingre, der fylder i techmediernes spalter. Når virksomheder viser videoer af humanoide hænder med tætte taktile arrays, er der typisk tale om pilot- eller forskningsstadiet: hudlignende overflader, der i laboratoriet kan mærke tekstur og temperatur, men som endnu ikke er valideret til tusindvis af cyklusser i et støvet tredjepartslogistikmiljø (3PL — *third-party logistics*, ekstern lageroperatør), hvor vedligehold af en beskadiget sensorspids kan stoppe et helt skift. En overbevisende demo i kontrolleret lys er ikke det samme som drift i et rigtigt arbejdsskift.

Følesansen er ikke magi; det er en lukket kontrolsløjfe. Uden den er fysisk AI blot en forprogrammeret bevægelse. Med den kan robotten møde virkelighedens uforudsigelighed — en skæv karton, en glat overflade, en uventet vægtfordeling — og reagere som en erfaren lagerarbejder.

[^1]: [Robotiq: »Your Physical AI Enabler« produktark](https://robotiq.com/hubfs/Physical%20AI/Physical-AI_Product_Sheet_Lettre_01.2026_EN_WEB.pdf) (2026: over 23.000 leverede gribere, 2F-85 med 85 mm slaglængde, 20–235 N griberkraft og op til 5 kg nyttelast — virksomhedens egne oplysninger).
[^2]: [Robotiq: »Tactile Sensor Fingertips«](https://robotiq.com/tactile-sensor-fingertips) (kapacitivt sensorarray til tryk-, slip- og vibrationsdata, 1.000 Hz — virksomhedens egne oplysninger).
[^3]: [Covariant: forsiden med Brain-platformen](https://covariant.ai/) (trænet på millioner af greb, kunder i 15 lande på 4 kontinenter — virksomhedens egne oplysninger); [IEEE Spectrum: »Covariant Uses Simple Robot and Gigantic Neural Net to Automate Warehouse Picking«](https://spectrum.ieee.org/covariant-ai-gigantic-neural-network-to-automate-warehouse-picking) (januar 2020, om den første dokumenterede drift hos Obeta/KNAPP i Tyskland og pointen om greb pr. time frem for fejlfri enkeltgreb).
