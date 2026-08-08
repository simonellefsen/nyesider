---
title: "Lagerets koreografi: hvem fører dansen?"
standfirst: Mennesker, mobile robotter og reoler i samme gulvplan. Rytmen er software, sikkerhedsregler — og en række navngivne lagre, der allerede har sat hjulene i gang.
section: Fabrikken
order: 2
image: ../images/humanerd_lager.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

Et moderne lager er en **koreografi**: varer ind, varer ud, undtagelser midt i det hele. **AMR**’er (*autonomous mobile robots* — mobile robotter, der navigerer på et digitalt kort med sensorer og en flåde-manager) kører ruter, henter hylder eller bringer ordrer hen til en plukstation. Mennesker plukker, pakker og håndterer det, robotten ikke må eller kan. Rytmen er ikke “robotten har overtaget”. Rytmen er **hvem der har lov til at indtage gulvet, og hvornår**.

### Hvad “autonom” betyder her

Ikke “ingen mennesker i bygningen”. Oftest: **assisteret autonomi** i zoner med hastighedsgrænser, nødstop og enten indhegning eller “bløde” sikkerhedslag, der sænker farten, når nogen kommer for tæt på. Se [nr. 1 om pilot til drift](/humanerd/2026-08-nr1/naar-robotten-faar-ben).

### Hvem bruger allerede mobile systemer?

**Amazon** er det største, offentligt synlige eksempel. Efter opkøbet af **Kiva Systems** i 2012 (i dag **Amazon Robotics**) har selskabet rullende hylder og mobile “drives” i sine **fulfillment centers** — lagre, hvor ordrer plukkes og pakkes til kunder. Amazon selv har fortalt om hundrede tusinder og senere **over en million robotter** på tværs af sit operationsnetværk siden 2012; det er **selskabets egne tal**, ikke en IFR-tælling, men skalaen er uomtvistelig i branchen.[^1] Et nyere showcase er det stærkt robotiserede center i **Shreveport, Louisiana** (åbnet midt i 2020’erne ifølge Amazons egen omtale), hvor flere robotsystemer arbejder sammen med mennesker — stadig ikke “uden folk”, men med en tættere koreografi.[^1]

**Ocado** i Storbritannien har bygget en anden slags koreografi: et **gitter af robotter**, der kører oven på kasser med dagligvarer (ofte kaldet en “hive” eller grid). Det er tættere på et automatiseret lagersystem end en frikørende AMR i en gammel hal, men pointen er den samme: **software + mekanik i drift**, ikke en engangsdemo. Flere detailkæder har licenseret eller kopieret lignende grid-tænkning.

**AutoStore** (norsk oprindelse, global udrulning) er et **kube-lager**: robotter kører oven på et aluminiumsgitter og henter kasser op til en port, hvor et menneske eller en arm plukker. Systemet er installeret hos mange 3PL-lagre (*third-party logistics* — eksterne logistikpartnere) og detailvirksomheder i Europa, Nordamerika og Asien. Igen: tjek den konkrete kunde og årstal, før du citerer “alle bruger det” — men listen over offentlige AutoStore-referencer er lang nok til, at det ikke er science fiction.

Blandt leverandører af frikørende AMR’er til eksisterende lagre (uden at bygge hele huset om) nævnes ofte selskaber som **Locus Robotics**, **Geek+** og **Hai Robotics** i kundehistorier fra e-handel og 3PL. **DHL**, **DB Schenker** og andre store speditører har i årevis kørt **piloter og delvise udrulninger** af mobile robotter i udvalgte centre — typisk som “goods-to-person” eller assisteret pluk, ikke som total erstatning af nattevagten. Offentlige casestudier skifter; HumaNerd’s point er mønsteret: **navngivne operatører, begrænset zone, målt opgave**.

### Hvad du skal spørge om — også når navnet er kendt

1. Hvilken **opgave** er erstattet eller hjulpet (transport, pluk, sortering)?  
2. Hvor længe har systemet kørt **uden demo-mode** — uger, måneder, skift?  
3. Hvem **stopper** robotten, og hvor hurtigt?  
4. Er tallet fra **kunden**, **leverandøren** eller en **uafhængig** kilde?

Amazon, Ocado og AutoStore viser, at mobile lagere er **industrielle**. De viser ikke, at din lokale terminal automatisk kan kopiere dem i morgen — gulv, **WMS** (*warehouse management system*) og arbejdsmiljø skal stadig passe.

[^1]: Amazon / Amazon Robotics offentlige omtaler af Kiva-opkøbet (2012), robotflådens vækst og Shreveport-anlægget — virksomhedstal; se aboutamazon.com operations/robotics-omtale. Tæl ikke Amazons “1 million robots” som IFR-industrirobotstatistik.
