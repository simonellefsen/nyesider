# Din krop, deres data: Sandheden om at eksportere dit liv

For longevity-nørder og biohackere er tesen simpel: Hvis vi vil optimere vores krop, skal vi måle den. Vi spænder ure om håndleddet, tisser på teststrimler og sætter en Continuous Glucose Monitor (CGM) i overarmen. Vi får farverige grafer og daglige scores, der fortæller os, om vi er restituerede. Det føles, som om vi har kontrol. Men hvem ejer egentlig den kontrol, når vi vil have rådataene ud?

De fleste wearable-producenter bryster sig af, at du til enhver tid kan eksportere og eje din egen data. Men et kig på den praktiske eksport-vej afslører, at maskinlæsbart sjældent er det samme som brugbart for kroppens ejer. At få tallene ud af de lukkede økosystemer kræver en teknisk tålmodighed, der ligger langt over, hvad gennemsnitsbrugeren orker. 

### Apple Health: Velkommen til tekst-helvedet
Lad os starte med det mest udbredte system. Går du ind i din iPhone, scroller ned i bunden af din sundhedsprofil og trykker "Eksporter alle sundhedsdata", sker der først ingenting. Så tænker telefonen længe. Til sidst får du en ZIP-fil. Pakker du den ud på din computer, finder du en fil ved navn `export.xml`. Det er skrevet i formatet Extensible Markup Language (XML)[^1].

For en maskine er det en logisk og struktureret fil. For et menneske er det en uendelig mur af kodesprog. Har du brugt et Apple Watch i tre år, vil denne ene fil nemt fylde adskillige gigabytes. Forsøger du at åbne den i regnearksprogrammer som Microsoft Excel, vil programmet med stor sandsynlighed fryse og bryde sammen på grund af datamængden. Du har teknisk set fået udleveret din data, men du kan ikke bruge den til at krydstjekke din dybe søvn mod din nye diæt uden at skrive et computerprogram først.

### Google og Fitbit: En labyrint af mapper
Efter Googles opkøb af Fitbit er vejen til din data blevet indlemmet i Google Takeout-maskineriet. Når du anmoder om at eksportere dine Fitbit-data, modtager du et arkiv, der primært består af filer i formaterne JavaScript Object Notation (JSON) og Comma-Separated Values (CSV)[^2].

Det er marginalt nemmere at arbejde med CSV end Apples massive XML-blok, fordi data her er brudt op. Prisen er til gengæld kaos. Din data er spredt ud over snesevis af undermapper: én til puls, én til søvnstadier, én til skridt – typisk opdelt i klodsede månedsintervaller. Vil du se en helbredstrend over flere år, skal du manuelt flette hundredevis af regneark sammen.

### Garmin: Sportens lukkede standard
Garmin er hardware-favoritten blandt folk, der tager deres kredsløbstræning alvorligt. Deres eksport af specifikke træningspas sker i formatet Flexible and Interoperable Data Transfer (.FIT)[^3]. Det er en binær filstandard, som er fantastisk kompakt og præcis til at gemme GPS-koordinater, watt og pulsslag ned til millisekunder, men filerne består af ren "volapyk" for det blotte øje. 

Du er tvunget til at bruge specialiserede tredjepartsværktøjer for overhovedet at konvertere filen til et format, der kan læses af et regneark. Vælger du i stedet at anmode om et fuldt kontoudtræk via Garmins hjemmeside, får du serveret en gigantisk portion JSON-filer, der kræver samme programmeringsfærdigheder som hos Google.

### WHOOP: API'er er en illusion af frihed
Hvad så med systemer som WHOOP, der slår sig op på at være for den absolutte elite inden for restitution og data-drevet ydeevne? WHOOP tilbyder et Application Programming Interface (API)[^4]. Et API bliver ofte fremhævet i tech-verdenen som den gyldne standard for datafrihed, fordi det lader systemer tale direkte sammen.

Problemet er bare, at de fleste API'er er bygget til softwareudviklere, ikke til dig. At udnytte WHOOP's system kræver, at du forstår netværksprotokoller, kan opsætte en server med OAuth 2.0-godkendelse og kan parse maskinelle JSON-svar via kode. Det er en bro mellem to computere, ikke et dashboard til din krop. 

Konklusionen er åbenlys: Hardwaregiganterne lyver ikke, når de siger, at du kan hente din data. De har bare gjort det præcis så besværligt at udnytte den, at 99 % af os opgiver og bliver inde i deres lukkede, farverige apps. Indtil der opstår universelle standarder, der lader os samle tallene nemt på tværs af mærker, lejer vi i praksis bare vores egen kropsdata.

[^1]: [Share your health and fitness data in Health on iPhone](https://support.apple.com/guide/iphone/share-your-health-data-iph5ede58c3d/ios) (Apple Support). Dokumenterer den XML-baserede eksportfunktion.
[^2]: [How do I export my Fitbit account data?](https://help.fitbit.com/articles/en_US/Help_article/1133.htm) (Google/Fitbit Help). Specificerer at data eksporteres som JSON og CSV via Google Takeout.
[^3]: [Flexible and Interoperable Data Transfer (FIT) Protocol](https://developer.garmin.com/fit/overview/) (Garmin Developers). Dokumentation af Garmins binære filstandard for wearables.
[^4]: [WHOOP API Documentation - Getting Started](https://developer.whoop.com/docs/developing/getting-started) (WHOOP). Beskriver krav om OAuth 2.0 og API'ets JSON-struktur.