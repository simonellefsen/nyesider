---
title: "To slags kernekraft i rummet"
standfirst: Den ene har fløjet i årtier og leverer nogle få hundrede watt. Den anden findes på tegnebrættet og skal levere 40 kilowatt. De forveksles konstant.
byline: "Claude Opus 4.8 (Anthropic)"
section: Rumkraft
order: 9
image: ../images/kraften_rtg.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

Når overskrifter lover «atomkraft på Månen», dækker de ofte over to teknologier, der stort set ikke har andet til fælles end ordet *nuklear*. Den ene har fløjet i årtier. Den anden findes endnu kun på tegnebrættet.

At holde dem adskilt er første skridt til at forstå, hvad rumkraft egentlig kan i dag.

### Radioisotop-generatoren: varme, ikke kædereaktion

Den teknologi, der faktisk har rejst ud i solsystemet, hedder radioisotop-termoelektrisk generator (RTG). Der er ingen reaktor og ingen kædereaktion. En RTG udnytter simpelthen den varme, der opstår, når plutonium-238 henfalder radioaktivt. Varmen ledes gennem termoelektriske elementer — materialer, der laver en temperaturforskel om til elektrisk spænding — og resultatet er nogle få hundrede watt.

Det lyder af lidt, og det er lidt. Til gengæld er pålideligheden ekstrem. Der er ingen bevægelige dele, der kan slides, og effekten falder kun langsomt, i takt med at plutoniet henfalder. Det er teknologien bag Voyager-sonderne og Mars-roveren Curiosity.[^1] I det ydre solsystem, hvor sollyset er for svagt til at bære en mission på solpaneler, er RTG i praksis den eneste realistiske løsning.

### Fission surface power: en rigtig reaktor på overfladen

Den anden teknologi er noget helt andet. *Fission surface power* betyder en egentlig fissionsreaktor — med kædereaktion — der skal stå på Månens eller Mars' overflade og forsyne en base. Her taler man ikke om hundreder af watt, men om kilowatt.

NASA's Glenn Research Center beskriver designmålet direkte: at udvikle et fissionsanlæg, der kan levere 40 kilowatt — nok til at forsyne 30 husstande i ti år.[^2]

Oversat: 40 kilowatt er ikke et kraftværk. Det svarer omtrent til forbruget i en mindre boligblok. Pointen er heller ikke effekten i sig selv. Det er, at den kommer uafbrudt.

### Hvorfor solpaneler taber — ikke på effekt, men på udholdenhed

Og netop dér ligger sagen. Et solpanel på Månen kan sagtens levere pæn effekt, når solen står på. Problemet er natten.

En månenat varer omkring 14 jorddøgn. To uger i træk uden sollys er dødeligt for et solbaseret anlæg, medmindre man slæber enorme batterier med — og batterier har masse, og masse skal opsendes. En reaktor er ligeglad med, om solen er oppe. Den kører videre gennem hele den lange skygge.

Det er ikke effekt, men udholdenhed, der afgør spørgsmålet.

### Køling er igen den svære del

Som så ofte i rummet er varmen ikke problemet at skabe — den er problemet at komme af med. På Jorden køler man en reaktor med luft eller vand. I vakuum findes ingen af delene. Den eneste vej er at stråle varmen ud, og det kræver store radiatorflader.

En reaktor, der producerer masser af varme, skal derfor bære et køleanlæg med, der fysisk kan være stort i forhold til selve reaktoren. Køling bliver en af de tungeste designudfordringer, ikke en eftertanke.

Dertil kommer levetiden. Målet om ti års drift betyder ti år **uden serviceteknikere**. Ingen vagthold, ingen udskiftning af slidte pumper, ingen inspektion. Det stiller helt andre krav til robusthed end en jordisk reaktor, hvor personale hele tiden kan gribe ind. Alt skal kunne køre selv, fejltolerant, i et årti. Til sammenligning bygges der [i Sverige](/kraften/2026-08-nr2/sverige-atom) i disse år et helt lovkompleks op om reaktorer, der har både vagthold og tilsynsmyndigheder inden for rækkevidde.

### Status: designarbejde, ikke hardware på Månen

Det er vigtigt at være nøgtern. Fission surface power er på nuværende tidspunkt udviklings- og designarbejde. Der står ingen reaktor på Månen, og de årstal, der nævnes i forbindelse med projektet, er planlagte mål — ikke kendsgerninger. Der findes flyvefærdig hardware for RTG'er, men ikke for overfladereaktorer.

Forskellen mellem de to teknologier er altså ikke akademisk. Den ene er et modent lav-effekt-system, der allerede sender data hjem fra solsystemets udkant. Den anden er et forsøg på at give en fremtidig base den uafbrudte forsyning, ingen solcelle kan garantere gennem fjorten døgns mørke.

De forveksles konstant. De burde ikke gøre det.

[^1]: [Radioisotope Power Systems](https://rps.nasa.gov/), NASA — om RTG'er, plutonium-238 og de missioner, teknologien har båret.
[^2]: [Fission Surface Power](https://www1.grc.nasa.gov/space/fission-surface-power/), NASA Glenn Research Center: «Designing a fission power system capable of generating 40 kilowatts of energy – enough to run 30 houses for 10 years.» To forbehold, som vi noterer, fordi de kan forvirre en læser, der selv tjekker efter: NASA's øvrige sider om projektet under nasa.gov var i en redirect-løkke og kunne ikke hentes, da vi tjekkede (16. august 2026). Og serveren bag Glenn-siden sender ikke sit mellemliggende certifikat, så et automatisk linktjek melder den død, mens en browser åbner den uden problemer. Vi har læst siden.
