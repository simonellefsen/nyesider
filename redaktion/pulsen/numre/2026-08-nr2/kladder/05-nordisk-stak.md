# Fire lag, ét ord

Når en kliniker siger «journalsystem», mener hun ofte noget helt konkret: skærmbilledet hun sidder foran, felterne hun taster ind i, knapperne der virker eller ikke virker. Når en it-arkitekt siger det samme ord, tænker han måske på databasen, der ligger et helt andet sted, driftet af en helt anden aktør. De taler forbi hinanden — og det er ikke en misforståelse, der kan ryddes af vejen med bedre kommunikation. Det er fordi «journalsystem» dækker mindst fire forskellige lag, som sjældent følges ad.

**Lag 1: Registreringslaget.** Det er her, data bliver til: notatet lægen skriver under en konsultation, blodtryksmålingen sygeplejersken taster ind, ordinationen der udstedes. Dette lag er tættest på den kliniske hverdag, og det er her, brugeroplevelsen — godt eller skidt — opstår.

**Lag 2: Lagringslaget.** Data skal ligge et sted, i en database, hos en dataansvarlig. Dette lag er usynligt for de fleste klinikere, men afgørende: hvem ejer databasen, hvor står serverne, og hvem bestemmer, hvad der sker med data, når en leverandør skifter, eller en aftale udløber. Lagringslaget er det tungeste at flytte. At migrere årtiers journaldata fra én database til en anden er en teknisk og juridisk operation af en helt anden størrelsesorden end at skifte, hvad man ser på skærmen.

**Lag 3: Udvekslingslaget.** Det er de aftaler, standarder og formater, der gør, at System A kan sende en oplysning til System B, som B faktisk kan forstå og bruge — ikke bare modtage som en uigennemsigtig fil. Uden et fælles udvekslingslag er systemerne isolerede øer, uanset hvor moderne de hver især ser ud.

**Lag 4: Anvendelseslaget.** Det, klinikeren rent faktisk klikker i. Dette lag kan i princippet leveres af en helt anden aktør end de tre øvrige — en app eller en brugerflade, der «taler» med lagringslaget bagved gennem udvekslingslaget, uden selv at eje en eneste byte af de underliggende data.

## Hvorfor lag 3 er kernen i de fleste konflikter

Pointen er denne: de fleste konflikter om sundheds-it handler i virkeligheden om lag 3, uden at parterne altid ved det. Det er relativt let at skifte anvendelseslag — en ny brugerflade kan i teorien indføres uden at røre databasen. Det er stort set umuligt at skifte lagringslag, fordi det kræver at flytte selve dataene og den juridiske forpligtelse, der følger med dem. Og hvis udvekslingslaget ikke er standardiseret — hvis der ikke findes fælles formater og fælles regler for, hvad der skal deles og hvordan — så er man reelt bundet til én leverandør, uanset hvad der står i kontrakten. Fri konkurrence på anvendelseslaget hjælper ikke, hvis udvekslingslaget er lukket.

Det er netop her, EHDS (European Health Data Space, det europæiske sundhedsdataområde) kommer ind, som beskrevet andetsteds i dette nummer. EU-forordningen regulerer specifikt udvekslingslaget: den stiller krav om, at elektroniske patientjournal-systemer (EPJ) skal kunne dele bestemte data i standardiserede formater. Men de krav gælder først fra midten og slutningen af dette årti — reglerne træder i kraft i etaper frem mod 2029 og 2031. Indtil da forbliver lag 3 primært et forhandlingsspørgsmål mellem købere og leverandører snarere end et lovkrav, man kan påberåbe sig.

## Hvorfor «nordisk» dukker op

I diskussioner om dataudveksling optræder ordet «nordisk» ofte som eksempel — ikke fordi et bestemt projekt nødvendigvis er dokumenteret, men fordi de nordiske lande generelt har sammenlignelige registerstrukturer og en tradition for personnumre, der gør det teknisk enklere at forestille sig, at data i princippet kunne følge en patient på tværs af landegrænser. Det er en strukturel pointe om, hvad der gør udveksling lettere at tænke sig — ikke en påstand om, at et konkret system allerede gør det i dag.

Næste gang en diskussion om sundheds-it kører fast, kan det være værd at spørge: hvilket lag taler vi egentlig om? Ni gange ud af ti er svaret det tredje.