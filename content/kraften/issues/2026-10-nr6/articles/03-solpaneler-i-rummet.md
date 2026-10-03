---
title: "Panelerne over atmosfæren"
standfirst: Derfor er en satellits solceller ikke dem fra villataget — og hvorfor 32 procent er et stort tal.
byline: GPT-5.6 Terra (OpenAI)
section: Panelerne
order: 3
image: ../images/kraften_solpaneler.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

En satellits solpaneler ligner ved første blik dem på et dansk tag: mørke flader, der omsætter sollys til elektricitet. Fysikken er den samme — lyset frigør elektriske ladninger i halvlederlag, og cellerne kobles sammen til et panel. Men i kredsløb er kravene langt hårdere: hvert gram skal opsendes, panelet skal foldes ud uden en reparatør i nærheden, og cellerne skal levere strøm efter år i stråling og ekstreme temperaturskift.

Derfor bruger mange rumfartøjer ikke de siliciumceller, der dominerer på jorden, men flerlags-celler. Moderne triple-junction-celler af galliumarsenid-typen — galliumindiumfosfid/galliumarsenid/germanium (GaInP/GaAs/Ge) — har tre halvlederlag, som hver udnytter forskellige dele af sollyset. Spectrolabs XTE-SF-celle er opgivet til 32,2 % virkningsgrad ved **BOL** (*beginning of life*, tilstanden ved opsendelse).[^1] Det er rimeligt at omtale som omkring 32 %.

BOL-tallet er dog ikke den effekt, satellitten har til rådighed gennem hele missionen. Partikler i rummet nedbryder gradvist halvlederne, og ved **EOL** (*end of life*, tilstanden ved missionens afslutning) er virkningen lavere. Ingeniører dimensionerer derfor panelareal, batterier og strømforbrug efter den forventede EOL-effekt, ikke efter den pæne BOL-værdi på databladet.

Det ændrer betydningen af et effekttal. Et panels *nameplate*-effekt er mærkeeffekten under de betingelser, det er specificeret til ved opsendelse. Effekten i drift afhænger derimod af orientering mod Solen, skygger, temperatur, aldring og satellittens egne behov. Planlagt effekt er endelig den effekt, missionen forventer at have tilbage senere i levetiden. Tre tal kan alle være korrekte — og alligevel beskrive tre forskellige ting.

Den Internationale Rumstation (**ISS** — *International Space Station*) viser skalaen. Hvert nyt **iROSA** (*ISS Roll-Out Solar Array*, stationens udrullelige solpaneler) leverer over 20 kilowatt (**kW**). Seks iROSA-paneler giver tilsammen over 120 kW ekstra og løfter stationens tilgængelige effekt med 20-30 %.[^2]

Solceller i rummet får mere lys pr. kvadratmeter end på jorden, fordi atmosfæren ikke absorberer og spreder en del af sollyset. Cellerne arbejder under **AM0**-spektret (*Air Mass Zero*, sollys uden passage gennem Jordens atmosfære). De undgår skyer og luftforurening, men ikke natten på den side af Jorden, der vender væk fra Solen, eller skygger fra selve rumfartøjet.

Til gengæld er rumsolceller dyre pr. watt. De skal være effektive, strålingsbestandige, mekanisk robuste og grundigt testet til opsendelse og vakuum. På jorden er økonomien ofte pris og areal; i rummet er den, hvor meget pålidelig elektricitet der kan sendes op og stadig være til rådighed ved EOL. Samme sollys — en helt anden elregning.[^3]

[^1]: Spectrolab, *XTE-SF Solar Cell Data Sheet*: https://www.spectrolab.com/photovoltaics/XTE-SF_Data_Sheet.pdf. Databladet angiver 32,2 % BOL-virkningsgrad.
[^2]: NASA, *New Solar Arrays to Power NASA's International Space Station Research*: https://www.nasa.gov/missions/station/new-solar-arrays-to-power-nasas-international-space-station-research
[^3]: Spectrolab, oversigt over rumceller: https://www.spectrolab.com/
