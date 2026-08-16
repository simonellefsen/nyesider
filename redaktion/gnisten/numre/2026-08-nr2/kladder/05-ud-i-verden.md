# Fra 'det virker på min computer' til 'her er linket'

Du har gjort det. Gennem en stædig samtale med en kunstig intelligens har du bygget en hjemmeside. Den ser fantastisk ud, knapperne virker, og farverne sidder lige i skabet. Men lige nu lever dit værk kun i en mappe på din egen harddisk. Hvis du vil vise den til en ven, en kollega eller en potentiel kunde, står du over for et uundgåeligt skridt: Siden skal lægges ud på internettet.

At få filer fra din egen maskine ud på en server kaldes for "hosting". For en nysgerrig nybegynder kan det hurtigt virke som en jungle af mærkelige fagbegreber. Men vi tager den korteste og mest ærlige vej uden om alt det tekniske fnidder.

Først skal du forstå en helt afgørende forskel, for den afgør, hvilke gratis muligheder der overhovedet gælder for dit projekt. Forskellen ligger i, om din side er en statisk side eller kræver en rigtig server.

En statisk side består kun af færdige filer — for eksempel tekst kodet i HyperText Markup Language (HTML) og design i Cascading Style Sheets (CSS). Tænk på en statisk side som en stak trykte flyers. Når en gæst besøger din adresse, skal computeren i den anden ende ikke tænke sig om; den rækker bare en færdigtrykt flyer over disken.

Noget, der derimod kræver en server, der aktivt kører kode, fungerer helt anderledes. Hvis din side skal gemme data, lade brugere logge ind eller ændre sig baseret på, hvem der kigger på den, er det ikke længere en flyer. Det er en kok, der står i et køkken og tilbereder en ret fra bunden, hver gang nogen beder om den. Kokken kræver strøm, regnekraft og vedligehold. Derfor er statiske sider ofte helt gratis at lægge på nettet, mens serverkode lynhurtigt koster penge.

Når du skal vælge, hvor din side skal bo, vil AI-værktøjer ofte foreslå dig en af disse tre almindelige veje:

**GitHub Pages:** Dette er en klassisk, indbygget tjeneste i kodeplatformen GitHub.[^1] Den er utroligt driftssikker og er skræddersyet til at udstille statiske sider. 

**Cloudflare Pages:** Kører på et massivt, globalt netværk. Tjenesten lader dig uploade dine statiske filer, hvorefter de kopieres og lynhurtigt kan tilgås fra hele verden.[^2]

**Vercel:** En enormt populær platform, der især er kendt for at gøre det nemt at få lidt mere komplicerede projekter online med meget få klik.[^3]

Mange guider på nettet vil her begynde at kaste om sig med konkrete tal for båndbredde, tilladte byggeminutter og gigabytes. Dem skal du ignorere. De ændrer sig alligevel konstant, og redaktionen har brændt sig på forældede prisskilte før. I stedet skal du altid stille fire grundlæggende spørgsmål til enhver udbyder:

1. Kan den overhovedet køre det, jeg har bygget?
2. Hvad koster det i virkeligheden, når fremmede mennesker faktisk begynder at besøge siden?
3. Må jeg bruge tjenesten til lige præcis det formål, jeg har i sinde?
4. Hvordan får jeg mine filer flyttet væk igen?

Særligt det tredje spørgsmål er vigtigt, for her lurer der en helt konkret fælde, som fanger mange begejstrede begyndere. Vercel tilbyder en enormt attraktiv og gratis "Hobby"-plan. Men ifølge Vercels egen officielle dokumentation må denne gratisplan udelukkende bruges til personlige, ikke-kommercielle formål.[^4] 

Hvad betyder det i praksis? Hvis du vil sælge et produkt, tage imod betaling eller blot bruge siden som et professionelt visitkort for en virksomhed, er gratisplanen ikke lovlig til det. Det er absolut ikke en kritik af Vercel — det står sort på hvidt i deres vilkår — men det er præcis den slags begrænsninger, man oftest opdager for sent. Bliver du grebet i at drive forretning på Hobby-planen, risikerer du at siden lukkes.

For at sikre dig selv bør du altid afslutte dit projekt med at købe et domænenavn (for eksempel *mit-projekt.dk*). Domænenavnet er dit permanente skilt. Hvis du peger dit eget domæne hen på udbyderen, har du altid en flugtvej åben. Viser det sig, at du bryder en regel, eller bliver det pludselig for dyrt, kan du blot tage dine filer, finde en ny udbyder og pege dit domænenavn det nye sted hen. Ingen besøgende vil opdage flytningen, og du bevarer 100\u00a0% kontrollen.

[^1]: GitHub Pages officiel platform og dokumentation: https://pages.github.com
[^2]: Cloudflare Pages produktbeskrivelse: https://pages.cloudflare.com
[^3]: Vercel officiel forside for frontend-hosting: https://vercel.com
[^4]: Vercels dokumentation for priser og vilkår for Hobby-abonnementet: https://vercel.com/docs/pricing