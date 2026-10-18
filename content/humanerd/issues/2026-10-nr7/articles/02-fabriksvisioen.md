# Øjet der aldrig blinker: Sådan ser BMW lakken før mennesket gør

**Fabrikken.** Hver eneste bil, der ruller ud fra BMWs fabrik i Regensburg, skal gennem en kontrol, intet menneske kan udføre i det tempo: en millimeterstor ujævnhed i lakken eller en misplaceret stud (svejse- eller monteringsknop) skal opdages, før bilen forlader samlebåndet. Opgaven er ikke at erstatte kvalitetskontrollørens øje, men at give det hjælp i en hastighed, hvor der ifølge BMWs egen pressemeddelelse fra april 2025 kommer en ny bil ca. hvert 57. sekund, og hvor Regensburg-fabrikken samlet set producerer omkring 1.400 biler om dagen.[^1]

## Et digitalt billede af karrosseriet

Løsningen hedder Automated Surface Processing og har kørt i serieproduktion i Regensburg siden marts 2022. Princippet er deflektometri: skærme projicerer geometriske mønstre ned på lakfladen, og kameraer scanner, hvordan mønstrene bøjes af bilens overflade. Ud fra det bygger systemet et digitalt 3D-billede af karrosseriet. En robot sliber og polerer de steder, billedet peger på, og til sidst markerer en laserprojektor de flader, som systemet ikke selv har kunnet kontrollere automatisk — typisk kanter og samlinger — så en menneskelig kontrollør ved præcis, hvor det sidste blik skal sættes ind.

Det er den praktiske pointe ved "fysisk AI" i en fabrikshal: systemet skal ikke bare genkende et mønster på et billede, det skal også regne ud, hvor robotarmen skal bevæge sig hen, og hvornår den skal stoppe, uden at ridse en lak, der koster tusindvis af kroner at udbedre.

## AIQX: kameraer som fælles nervesystem

Deflektometrien er én del af et større system, BMW kalder AIQX — Artificial Intelligence Quality Next. Det er BMWs egen IT-platform, bygget op omkring netværkskameraer langs samlebåndet, hovedsagligt af typen Axis P14 Bullet. Ifølge kameraleverandøren Axis er AIQX i dag rullet ud på tværs af BMW-fabrikker globalt, og platformen laver realtidsanalyse af billederne og sender straks-advarsler videre til medarbejdernes håndholdte enheder, hvis noget afviger fra normen.[^2] Det er værd at bemærke, at det er Axis' egen beskrivelse af et kundesamarbejde — altså en leverandørs fremstilling af, hvor udbredt systemet er, ikke en uafhængig optælling.

Fra den amerikanske fabrik i Spartanburg har den tidligere BMW-ledelse i et interview med CNBC beskrevet en lignende opsætning med 26 kameraer og et lukket AI-kredsløb, der ifølge BMW selv sparer virksomheden over 1 million amerikanske dollar om året.[^3] Det tal er et virksomhedstal — en besparelse, BMW selv har opgjort og offentliggjort, ikke en ekstern revision — men det giver en fornemmelse af skalaen: AOI (automatisk optisk inspektion) handler ikke om ét kamera, der kigger på én bil, men om snesevis af kameraer, der dækker en hel produktionslinje.

## Grænsen for, hvad kameraet kan se

Her er det vigtigt at skelne. AIQX og Automated Surface Processing er dokumenteret drift i Regensburg — ikke en pilot og ikke en messedemo. Men systemet kan ikke se alt. Kanter, samlinger og skjulte vinkler er notorisk svære for optisk inspektion, uanset hvor avanceret deflektometrien er, og det er netop derfor, laserprojektoren til sidst peger de steder ud, hvor et menneske stadig skal kigge efter. Kvalitetskontrol i Regensburg er med andre ord et samarbejde, ikke en automatisering, der har gjort den menneskelige kontrollør overflødig.

## Næste skridt er stadig en pilot

I april 2025 annoncerede BMW et nyt forsøg: GenAI4Q, udviklet sammen med München-opstarten Datagon AI. Formålet er at bruge generativ AI til at bygge et skræddersyet kontrolkatalog — altså automatisk at generere de referencebilleder og fejltyper, som AOI-systemet skal sammenligne med — til de omkring 1.400 biler, der dagligt går gennem Regensburgs samlelinje.[^4] Det er, ifølge BMWs egen annoncering, et pilotprojekt, og det bør læses som det: en test af, om kataloget kan gøres hurtigere og mere præcist at opdatere, ikke en bekræftelse af, at det allerede kører i fuld drift på linjen.

Forskellen mellem de to nyheder er selve pointen. Automated Surface Processing er en proces, der har kørt i over tre år på en konkret fabrik. GenAI4Q er en idé, der er annonceret — og som først bliver til drift, den dag BMW (eller en uafhængig kilde) kan vise, at kataloget faktisk bruges på hver eneste bil, der ruller forbi kameraerne.

---

[^1]: BMW Group PressClub, «Artificial intelligence as a quality booster», april 2025: [https://www.press.bmwgroup.com/global/article/detail/T0449729EN/artificial-intelligence-as-a-quality-booster?language=en](https://www.press.bmwgroup.com/global/article/detail/T0449729EN/artificial-intelligence-as-a-quality-booster?language=en)
[^2]: Axis Communications, kundecase om BMWs AIQX-platform: [https://www.axis.com/customer-story/axis-industrial-vehicle-production](https://www.axis.com/customer-story/axis-industrial-vehicle-production)
[^3]: CNBC, «How BMW uses AI to make vehicle assembly more efficient», 21. juli 2023: [https://www.cnbc.com/2023/07/21/how-bmw-uses-ai-to-make-vehicle-assembly-more-efficient.html](https://www.cnbc.com/2023/07/21/how-bmw-uses-ai-to-make-vehicle-assembly-more-efficient.html)
[^4]: BMW Group PressClub, «Automated surface processing at BMW Group Plant Regensburg – trio of digital paint shop processes», 2. maj 2023: [https://www.press.bmwgroup.com/global/article/detail/T0411621EN/automated-surface-processing-at-bmw-group-plant-regensburg-%E2%80%93-trio-of-digital-paint-shop-processes?language=en](https://www.press.bmwgroup.com/global/article/detail/T0411621EN/automated-surface-processing-at-bmw-group-plant-regensburg-%E2%80%93-trio-of-digital-paint-shop-processes?language=en)