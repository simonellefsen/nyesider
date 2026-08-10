---
title: "Hjernens fem lag"
standfirst: Fra pixel til motor går en kæde af fem led. Hvert af dem kan knække — og det er dér, en messedemonstration skiller sig fra et arbejdsskift.
byline: "Gemini 3.1 Pro Preview (Google)"
section: Hjernen
order: 8
figures:
  - ../images/figur-robotstack.svg
---

Når en humanoid samler et æble op og lægger det i en kurv på en viral video, ser det legende let ud. Det frister til at tro, at maskinen forstår verden nogenlunde som et menneske.

Men **fysisk AI** er ikke en etiket, man klistrer på et chassis. Det er en kæde af processer, der kører i rækkefølge — robotstakken — og kæden er kun så stærk som sit svageste led.

Forskellen på digital og fysisk AI er værd at holde fast i. Tager en sprogmodel fejl, får du et forkert svar på en skærm. Tager en robot fejl, flytter den noget tungt til det forkerte sted.

[FIGUR 1]

### 1. Sansning

Robotten måler sin omverden gennem kameraer, dybdesensorer og kraft- og momentmåling i leddene.

**Hvor det knækker:** sensorer er underlagt fysikken. Et kamera blændes af modlys fra et vindue. En dybdesensor forvirres af refleksioner fra en blank metaloverflade, der kaster signalet væk, så objektet ligner et hul i rummet. Er det første input defekt, fejler resten af kæden — uanset hvor god softwaren er.

### 2. Opfattelse

Næste lag oversætter en strøm af rå pixels og dybdedata til en model af virkeligheden: *her står en papkasse, og den vender sådan.*

**Hvor det knækker:** maskinlæring er blevet formidabel til at genkende *hvad* noget er. Den rumlige orientering glipper oftere. Robotten kan genkende kassen med stor sikkerhed og alligevel gætte dens vinkel forkert med få centimeter. Så lukker griberen sig om luften ved siden af — eller maser fingrene ned i kassens hjørne.

### 3. Planlægning

Nu skal der beregnes en rute: en rækkefølge af bevægelser og ledvinkler, der bringer hånden frem uden at albuen rammer en reol eller en kollega.

**Hvor det knækker:** ikke nødvendigvis ved at ruten er forkert. En hyppig fejl er, at planen tager for lang tid at lægge. En rute, der er gyldig og undgår alle forhindringer, men som kræver femten sekunders beregning, er ubrugelig i en produktionshal.

### 4. Styring

Planen skal blive til fysisk handling. Motorstyringen følger banen, mens sensorerne mærker efter, hvordan verden skubber tilbage.

**Hvor det knækker:** her træder den afgørende forskel frem. Går styringen ned midt i en bevægelse på en fastboltet robotarm, stopper armen og bliver stående. Mister en gående humanoid sin balanceberegning i et splitsekund, falder den.

Tyngdekraften holder ikke pause, mens computeren genstarter.

### 5. Sikkerhed

Det femte lag skal virke, også — og især — når de fire andre ikke gør.

**Hvor det knækker:** indlært adfærd arbejder med sandsynligheder og er svær at forudsige fuldstændigt. Derfor er sikkerheden typisk bygget *adskilt* fra det lærte system: hårde, ufravigelige mekanismer som en nødstopkreds, der afbryder strømmen til motorerne uden at spørge softwaren om lov, eller en momentgrænse, der udløser, når en motor trækker mere strøm end tilladt.

Blander man den lærte del for tæt sammen med sikkerhedslaget, risikerer man, at en fejl i softwaren også slår nødbremsen fra.

### Når videoen snyder øjet

Producenternes videoer viser de gennemløb, hvor alle fem lag spillede sammen. Meget af det, der ligner flydende autonomi, er noget andet.[^1]

Tre ting at kigge efter:

**Teleoperation.** Står der en person uden for billedet med et VR-headset eller joysticks? En fjernstyret robot demonstrerer god mekanisk styring. Den beviser intet om autonom opfattelse eller planlægning.

**Klipningen.** Klipper videoen præcis i det øjeblik, robotten griber ud, og har den fat i næste klip? Det er et klassisk tegn på, at grebet krævede mange forsøg.

**Hastigheden.** Er mennesker i baggrunden unaturligt hurtige, eller falder en tabt genstand for kvikt mod gulvet? Så er optagelsen spillet op, fordi robotten i virkeligheden arbejder i et tempo, der ville kede seeren.

Fysisk AI er et reelt ingeniørmæssigt gennembrud — når det kører stabilt. Men næste gang en maskine imponerer på en skærm, er spørgsmålet: hvor mange gange knækkede kæden, før kameraet rullede?

[^1]: Evan Ackerman, «How to Make a Good Robot Video [Media]», *IEEE Robotics & Automation Magazine*, bind 30, nr. 2, 2023, s. 127 — [IEEE Xplore](https://ieeexplore.ieee.org/document/10153150). Ackerman er robotredaktør på IEEE Spectrum og skriver ud fra at have set titusindvis af robotvideoer; artiklen gennemgår, hvad der adskiller en redelig robotvideo fra en, der skjuler teleoperation, klipning og hastighedsændring. Se også IEEE Robotics and Automation Society' [Video Submission Guidelines](https://www.ieee-ras.org/publications/video-submission-guidelines/).
