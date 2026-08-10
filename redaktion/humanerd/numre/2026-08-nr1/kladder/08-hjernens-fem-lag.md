# Hjernen: Fra pixel til motor – robotstakkens fem skrøbelige lag

Når en skinnende humanoid samler et æble op og lægger det i en kurv på en viral video, ser det legende let ud. Det frister os til at tro, at maskinen instinktivt forstår verden på samme måde som et menneske. Men fysisk kunstig intelligens (AI) er ikke en magisk etiket, man kan klistre på et chassis for at give det liv. Det er derimod en kompliceret og strengt sekventiel kæde af matematiske processer – den såkaldte robotstak.

Forskellen på digital og fysisk AI er fundamental: Hvis en sprogmodel, for eksempel en LLM (Large Language Model), tager fejl og hallucinerer, får du et komisk eller forkert tekstsvar på en skærm. Hvis en robot tager fejl, risikerer den at flytte et tungt metalemne til det forkerte sted med enorm kraft. For at forstå, hvorfor en overbevisende demonstration på en messe sjældent kan oversættes direkte til stabil drift i et industrielt arbejdsskift, skal man forstå stakkens fem lag – og præcis hvor de har tendens til at knække.

**1. Sansning (Sensing)**
Før robotten kan foretage sig noget som helst, skal den måle sin omverden. Dette sker gennem optiske kameraer, infrarøde dybdesensorer og kraft- og momentmåling indbygget direkte i robottens led. 
*Fejlmuligheden:* Sensorer er slaver af fysikken. Et kamera blændes nemt af uventet modlys fra et vindue på lageret. En dybdesensor kan blive totalt forvirret af refleksioner fra en skinnende metaloverflade, som kaster signalet væk og får objektet til at ligne et tomt hul i rummet. Hvis dette første input er defekt, fejler resten af kæden uvægerligt, uanset hvor avanceret softwaren er.

**2. Opfattelse (Perception)**
I det næste lag skal robotten oversætte en kaotisk strøm af rå pixels og dybdedata til en konkret model af virkeligheden: "Her står en papkasse, og den er vinklet præcis sådan her."
*Fejlmuligheden:* Selvom maskinlæring er blevet formidabel til at genkende objekter, glipper den rumlige orientering ofte i praksis. Robotten genkender måske kassen med 100&nbsp;% sikkerhed og ved, hvad den er, men algoritmen gætter kassens vinkel forkert med få centimeter. Resultatet er, at gribekloen lukker sig om den tomme luft ved siden af emnet – eller endnu værre, maser sine fingre direkte ned i kassens hjørne.

**3. Planlægning (Planning)**
Når maskinen ved, hvor kassen befinder sig, skal den beregne en rute. Den skal vælge en præcis rækkefølge af bevægelser og vinkler for alle sine led, så hånden når frem til målet, uden at albuen undervejs rammer en reol eller en menneskelig kollega.
*Fejlmuligheden:* Matematikken bag kinematisk bevægelsesplanlægning er beregningstung. En hyppig fejl i udviklingsfasen er ikke nødvendigvis, at robotten vælger en forkert rute, men at planen er alt for langsom at generere. En rute, der er teknisk gyldig og undgår alle forhindringer, men som tager systemet femten sekunder at udregne, er fuldstændig ubrugelig i en produktionshal, hvor tid er penge.

**4. Styring (Control)**
Nu skal planen konverteres til fysisk handling. Motorstyringen sender den rette mængde strøm til aktuatorerne for at følge den beregnede bane, alt imens sensorerne konstant mærker efter, hvordan den fysiske verden skubber tilbage mod robotten.
*Fejlmuligheden:* Her træder en afgørende forskel frem. Hvis softwaren i en klassisk, fastboltet robotarm crasher midt i en bevægelse, stopper den blot op og står stille i luften. Hvis en gående humanoid derimod mister evnen til at beregne sin komplekse balancekontrol i et splitsekund, falder den tungt forover. Tyngdekraften holder ikke pause, mens computeren genstarter.

**5. Sikkerhed (Safety)**
Det femte og sidste lag er det absolut vigtigste for industriel implementering: Sikkerhedssystemet skal fungere fejlfrit, også (og især) når de fire foregående lag bryder sammen.
*Fejlmuligheden:* Fordi neurale netværk og indlært adfærd i sagens natur opererer med sandsynligheder, er de svære at forudsige hundrede procent. Derfor er sikkerheden typisk implementeret helt adskilt fra det lærte system. Det består ofte af hårde, ufravigelige regler – for eksempel et relæ, der fysisk afbryder strømmen, hvis en motor trækker et millivolt for meget. Blandes den lærte "fysiske AI" for tæt sammen med sikkerhedslaget, risikerer man, at en hallucination i softwaren slår nødbremsen fra.

**Når videoen snyder øjet**
Når robotproducenter frigiver PR-videoer, ser vi kun de nøje udvalgte gennemløb, hvor alle fem lag i stakken spillede perfekt sammen. Men meget af det, der ligner flydende autonomi på en skærm, er i virkeligheden noget ganske andet.[^1] 

Som kritisk seer bør man altid lede efter tre ting:
For det første: Teleoperation. Står der en ingeniør uden for billedet med et VR-headset (Virtual Reality) eller et sæt joysticks? En fjernstyret robot demonstrerer fremragende mekanisk styring, men den beviser absolut intet om autonom opfattelse eller planlægning. 
For det andet: Klipningen. Hvis videoen klipper nøjagtig i det brøkdel af et sekund, hvor robotten griber ud efter et objekt, og i næste klip har et solidt fat, er det et klassisk symptom på, at grebet har krævet mange mislykkede forsøg. 
For det tredje: Hastigheden. Er mennesker i baggrunden uskarpe, eller falder tabte genstande unaturligt hurtigt mod jorden? Så er videoen spillet hurtigere, fordi robottens planlægningslag i virkeligheden arbejder i et tempo, der ville kede seeren.

Fysisk AI er et regulært ingeniørmæssigt gennembrud, når det vel at mærke drives stabilt. Men næste gang en maskine imponerer dig på sociale medier, så stop op og overvej: Hvor mange gange knækkede kæden i et af de første lag, før kameraet rullede?

[^1]: Den tekniske publikation IEEE Spectrum har i årevis dækket misforholdet mellem PR-demoer og reel robotdrift. Evan Ackermans guide *"How to Watch a Robot Video"* (IEEE Spectrum, 2023) er en anerkendt reference til at identificere skjult teleoperation, hastighedsmanipulation og selektiv klipning i branchens markedsføringsmateriale.