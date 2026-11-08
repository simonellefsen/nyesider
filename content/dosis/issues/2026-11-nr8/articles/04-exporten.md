---
title: "Din krop, deres data: sandheden om at eksportere dit liv"
standfirst: "Apple giver dig XML i gigabytes, Google giver dig et arkiv i et takelag af mapper, Garmin giver dig binære .FIT-filer — og WHOOP giver udviklere et API. Maskinlæsbart er ikke det samme som brugbart."
section: Wearables & data
order: 4
image: ../images/dosis_n8_export.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
byline: "Gemini 3.1 Pro Preview (Google)"
---

For longevity-nørder og biohackere er tesen simpel: Hvis vi vil optimere vores krop, skal vi måle den. Vi spænder ure om håndleddet og sætter en kontinuerlig glukosemåler (CGM, *continuous glucose monitoring*) i overarmen. Vi får farverige grafer og daglige scores, der fortæller os, om vi er restituerede. Det føles, som om vi har kontrol. Men hvem ejer egentlig den kontrol, når vi vil have rådataene ud?

De fleste wearable-producenter bryster sig af, at du til enhver tid kan eksportere og eje din egen data. Men et kig på den praktiske eksport-vej afslører, at maskinlæsbart sjældent er det samme som brugbart for kroppens ejer. At få tallene ud af de lukkede økosystemer kræver en teknisk tålmodighed, der ligger langt over, hvad gennemsnitsbrugeren orker.

### Apple Health: velkommen til tekst-helvedet

Lad os starte med det mest udbredte system. Går du ind i din iPhone, scroller ned i bunden af din sundhedsprofil og trykker «Eksporter alle sundhedsdata», sker der først ingenting. Så tænker telefonen længe. Til sidst får du en ZIP-fil. Pakker du den ud på din computer, finder du en fil ved navn `export.xml`. Det er skrevet i formatet Extensible Markup Language (XML).[^1]

For en maskine er det en logisk og struktureret fil. For et menneske er det en uendelig mur af kodesprog. Har du brugt et Apple Watch i tre år, vil denne ene fil nemt fylde adskillige gigabytes. Forsøger du at åbne den i regnearksprogrammer som Microsoft Excel, vil programmet med stor sandsynlighed fryse og bryde sammen på grund af datamængden. Du har teknisk set fået udleveret din data, men du kan ikke bruge den til at krydstjekke din dybe søvn mod din nye diæt, uden at skrive et computerprogram først.

### Google og Fitbit: en labyrint af mapper

Efter Googles opkøb af Fitbit er vejen til din data blevet indlemmet i Google-maskineriet. Logger du ind med en Google-konto, anmoder du om dataudtræk via Googles download-side med «Google Health» markeret; er du stadig tilbage i det gamle Fitbit-login, bestiller du et fuldstændigt kontoudtræksarkiv fra Fitbits indstillingsside, og GPS-træningspas kan eksporteres enkeltvis i TCX-formatet fra appen.[^2]

Arkivet består af maskinlæsbare filer — men data er spredt ud over snesevis af undermapper: én til puls, én til søvn, én til skridt — typisk opdelt i klodsede intervaller. Vil du se en helbredstrend over flere år, skal du manuelt flette hundredvis af filer sammen.

### Garmin: sportens lukkede standard

Garmin er hardware-favoritten blandt folk, der tager deres kredsløbstræning alvorligt. Deres eksport af specifikke træningspas sker i formatet Flexible and Interoperable Data Transfer (.FIT).[^3] Det er en binær filstandard, som er fantastisk kompakt og præcis til at gemme GPS-koordinater, watt og pulsslag ned til millisekunder, men filerne består af ren «volapyk» for det blotte øje.

Du er tvunget til at bruge specialiserede tredjepartsværktøjer for overhovedet at konvertere filen til et format, der kan læses af et regneark. Vælger du i stedet at anmode om et fuldt kontoudtræk, får du serveret en gigantisk portion maskinlæsbare filer, der kræver samme programmeringsfærdigheder som hos Google.

### WHOOP: API'er er en illusion af frihed

Hvad så med systemer som WHOOP, der slår sig op på at være for den absolutte elite inden for restitution og data-drevet ydeevne? WHOOP tilbyder et Application Programming Interface (API).[^4] Et API bliver ofte fremhævet i tech-verdenen som den gyldne standard for datafrihed, fordi det lader systemer tale direkte sammen.

Problemet er bare, at de fleste API'er er bygget til softwareudviklere, ikke til dig. At udnytte WHOOP's system kræver, at du forstår netværksprotokoller, kan opsætte en server med OAuth 2.0-godkendelse og kan parse maskinelle JSON-svar via kode. Det er en bro mellem to computere, ikke et dashboard til din krop.

Konklusionen er åbenlys: Hardwaregiganterne lyver ikke, når de siger, at du kan hente din data. De har bare gjort det præcis så besværligt at udnytte den, at langt de fleste opgiver og bliver inde i deres lukkede, farverige apps. Indtil der opstår universelle standarder, der lader os samle tallene nemt på tværs af mærker, lejer vi i praksis bare vores egen kropsdata.

[^1]: [Del dine sundheds- og fitnessdata i Sundhed på iPhone](https://support.apple.com/da-dk/guide/iphone/iph5ede58c3d/ios) (Apple Support). Dokumenterer den XML-baserede eksportfunktion.
[^2]: [How do I export my Google Health data?](https://help.fitbit.com/articles/en_US/Help_article/1133.htm) (Google Health Help Center). Dækker Google-konto-udtræk, Fitbits Data Export-archive og TCX-eksport af GPS-træningspas.
[^3]: [Flexible and Interoperable Data Transfer (FIT) Protocol](https://developer.garmin.com/fit/overview/) (Garmin Developers). Dokumentation af Garmins binære filstandard for wearables.
[^4]: [WHOOP API Documentation — Getting Started](https://developer.whoop.com/docs/developing/getting-started) (WHOOP). Beskriver krav om OAuth 2.0 og API'ets JSON-struktur.
