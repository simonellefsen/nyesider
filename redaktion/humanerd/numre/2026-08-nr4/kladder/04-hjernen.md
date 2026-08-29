# Teleoperation: broen mellem menneske og autonomi

Når en humanoide robot vises på video, mens den genopfylder en butikshylde, ser det ofte ud til at være ren magi. I virkeligheden kan den magi have et meget menneskeligt hjælpeånd: en operatør, der sidder flere kilometer væk med et virtuelt reality-headset (VR-headset) og styrer robottens hver eneste bevægelse i realtid. Denne praksis kaldes teleoperation, og den er ikke et nødvendigt onde, men en bevidst strategi. For mange robotudviklere er det en uundværlig bro på vejen mod fuld autonomi.

Mekanismen er ligetil, men kræver avanceret infrastruktur. Operatøren ser gennem robottens sensorer – oftest stereokameraer – i VR-udstyret. Når operatøren griber fat i en virtuel genstand eller bevæger sine egne arme, sender et lav-latens netværk disse bevægelseskommandoer til robotten, som udfører dem med det samme. Mens dette sker, logger systemet alt: hvert kamera billede, hver sensorværdi, hver motorbevægelse og hver menneskelig handling. Denne enorme datamængde bliver brændstof til at træne den kunstige intelligens (AI), som en dag skal gøre robotten selvkørende.

**Hjemmebanen for datafangsten**

Et konkret eksempel på denne platform-tilgang finder man hos det amerikanske selskab HIVE Robots. Ifølge selskabets egen beskrivelse dækker deres platform, kaldet ‘Heimdall’, hele denne proces[^1]. Platformen er opdelt i seks kategorier: teleoperation, AI-datafangst, modeltræning, sikkerhed/tilsyn, flådedrift og integration/sikkerhed. Sammen rummer disse ifølge HIVE selv 30 forskellige funktioner[^1]. Det afslørende i opdelingen er, at teleoperation og AI-træning behandles som to integrerede dele af samme system. Operatørens arbejde er ikke blot at udføre en opgave, men at producere et detaljeret undervisningssæt til maskinen.

**Hvorfor er strategien så udbredt?**

Teleoperation som datastrægi er en pragmatisk løsning på et komplekst problem. For det første er det billigere og hurtigere at installere en fysisk robot i en rigtig butik eller fabrik, hvis den kan sættes i drift med et menneske i loopet. Dette giver værdi for kunden med det samme, mens den nødvendige træningsdata indsamles på den rigtige arbejdsplads med de rigtige udfordringer.

For det andet sikrer det kvaliteten af træningsdataene. I stedet for at forsøge at simulere alverdens uforudsigelige menneskelige adfærd og fysiske miljøer i en computer, indsamles data fra de *præcise* situationer, robotten skal håndtere. Dette løser et af de største flaskehalse i fysisk AI: at få nok højkvalitets, realistisk data til at træne en robust model.

Forbrugeren af nyheder skal dog være opmærksom. Når en pressemeddelelse melder om, at “robotten nu arbejder i butik X”, er det afgørende at skelne mellem, om den arbejder autonomt, eller om den fungerer som en avanceret, fysisk drone for en menneskelig operatør. Denne forskel er sjældent tydelig i markedsføringsmateriale. Antallet af installerede robotenheder bliver dermed en misvisende statistik, hvis den bruges som et mål for teknologisk modenhed. Et højt tal kan lige så godt indikere en omfattende indsats i manuel dataindsamling som det kan indikere et gennembrud i selvstændighed.

Teleoperation viser sig altså ikke som et snyd, men som et afgørende udviklingsstadie. Det er erkendelsen af, at den vej til intelligent, fysisk handling ofte først skal kortlægges af et menneske – et skridt ad gangen.

[^1]: HIVE Robots, “Heimdall Platform”, beskrevet på selskabets hjemmeside. https://www.hiverobots.com/heimdall (Besøgt i forbindelse med research til artiklen).
[^2]: International Federation of Robotics (IFR), “World Robotics Report”, diskuterer ofte udfordringer og trends inden for implementering og autonomi i service- og industrirobotter. https://ifr.org/