---
title: "Hjernen: Manden i maskinen"
standfirst: Når en pressemeddelelse siger, at robotten "arbejder", kan det betyde alt fra fuld autonomi til, at en operatør et andet sted styrer den gennem et VR-headset.
byline: DeepSeek V3.2 (DeepSeek)
section: Hjernen
order: 4
image: ../images/humanerd_hjernen.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

Når en humanoid robot vises på video, mens den genopfylder en butikshylde, ser det ofte ud til at være ren autonomi. I virkeligheden kan der stå en operatør bag: en person, der sidder flere kilometer væk med et virtuelt reality-headset (VR-headset, briller der viser et computergenereret billede) og styrer robottens bevægelser i realtid. Denne praksis kaldes teleoperation, og den er ikke et nødvendigt onde, men en bevidst strategi. For mange robotudviklere er den en uundværlig bro på vejen mod fuld autonomi.[^1]

Mekanismen er ligetil, men kræver avanceret infrastruktur. Operatøren ser gennem robottens sensorer — oftest stereokameraer — i VR-udstyret. Når operatøren griber fat i en virtuel genstand eller bevæger sine egne arme, sender et lav-latens netværk disse bevægelseskommandoer til robotten, som udfører dem med det samme. Mens dette sker, logger systemet alt: hvert kamerabillede, hver sensorværdi, hver motorbevægelse og hver menneskelig handling. Denne datamængde bliver brændstof til at træne den kunstige intelligens (AI), som på sigt skal gøre robotten selvkørende.

**Et konkret eksempel: HIVE's Heimdall-platform**

Det danske selskab HIVE Robots — omtalt i Humanoiden i dette nummer for sit samarbejde med Føtex — bygger sin robotplatform op omkring netop denne logik. Ifølge selskabets egen beskrivelse dækker platformen, kaldet "Heimdall", hele processen fra fjernstyring til datafangst.[^2] Platformen er opdelt i seks kategorier: teleoperation, AI-datafangst, modeltræning, sikkerhed/tilsyn, flådedrift og integration/sikkerhed — tilsammen, ifølge HIVE selv, 30 funktioner. Det er en beskrivelse fra selskabet selv og ikke uafhængigt efterprøvet i denne artikel, men opdelingen er alligevel afslørende: teleoperation og AI-træning behandles som to integrerede dele af samme system. Operatørens arbejde er ikke blot at udføre en opgave, men at producere et detaljeret undervisningssæt til maskinen.

**Hvorfor er strategien så udbredt?**

Teleoperation som datastrategi er en pragmatisk løsning på et komplekst problem. For det første er det billigere og hurtigere at sætte en fysisk robot i drift i en rigtig butik eller fabrik, hvis den kan fungere med et menneske i loopet fra dag ét. Det giver værdi for kunden med det samme, mens den nødvendige træningsdata indsamles på den rigtige arbejdsplads med de rigtige udfordringer.

For det andet sikrer det kvaliteten af træningsdataene. I stedet for at forsøge at simulere alverdens uforudsigelige menneskelige adfærd og fysiske miljøer i en computer, indsamles data fra de præcise situationer, robotten skal håndtere. Dette løser en af de største flaskehalse i fysisk AI: at få nok højkvalitets, realistisk data til at træne en robust model.

Forbrugeren af nyheder skal dog være opmærksom. Når en pressemeddelelse melder, at "robotten nu arbejder i butik X", er det afgørende at skelne mellem, om den arbejder autonomt, eller om den fungerer som en avanceret, fysisk forlængelse af en menneskelig operatør. Denne forskel er sjældent tydelig i markedsføringsmateriale. Antallet af installerede robotenheder bliver dermed en misvisende statistik, hvis den bruges som et mål for teknologisk modenhed. Et højt tal kan lige så godt indikere en omfattende indsats i manuel dataindsamling, som det kan indikere et gennembrud i selvstændighed.

Teleoperation viser sig altså ikke som et snyd, men som et afgørende udviklingsstadie. Det er erkendelsen af, at vejen til intelligent, fysisk handling ofte først skal kortlægges af et menneske — et skridt ad gangen.

[^1]: [The Humanoid: «Teleoperation»](https://thehumanoid.ai/glossary/teleoperation/) — introduktion til teleoperation i humanoid robotteknologi.
[^2]: [HIVE Robots: «Heimdall»](https://hiverobots.dk/heimdall).
