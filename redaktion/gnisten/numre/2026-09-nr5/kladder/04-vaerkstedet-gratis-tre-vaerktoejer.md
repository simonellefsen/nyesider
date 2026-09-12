### Værkstedet: Få dit første AI-projekt på nettet — helt gratis

Du har brugt kunstig intelligens (AI) til at skabe en web-applikation. Den virker måske helt perfekt, når du tester den hjemme på din egen computer, men nu vil du gerne udgive den, så andre kan bruge den. Moderne AI-værktøjer genererer ofte kode, der kræver specialiserede platforme for at køre på internettet. Heldigvis behøver du ikke at finde betalingskortet frem for at komme i gang. Du skal blot bruge tre forskellige onlinetjenester i en trin-for-trin-rækkefølge: Opret først kode på GitHub, deploy (udgiv) derefter koden på Vercel, og tilføj til sidst en database på Supabase. Disse tre gratis niveauer er mere end nok til at lære og til at vise et projekt frem. Men hver tjeneste har sin egen specifikke faldgrube, som en begynder er nødt til at kende til, før man rammer den.

**Første skridt: Opret kode på GitHub**
Det første og vigtigste fundament er at gemme din kode sikkert på nettet. Her er platformen GitHub branchens absolutte standard. På deres gratis plan, GitHub Free, får du adgang til ubegrænsede private repositories (kodemapper) med et begrænset funktionssæt. At mapperne er private betyder, at du trygt kan eksperimentere, uden at hele internettet kan se dine fejl. Du får desuden 500 Megabyte (MB) Packages-lager (et centralt sted til softwarepakker) og 15 Gigabyte (GB) Codespaces-lager pr. måned (md). Sidstnævnte er en virtuel computer, hvor du kan rette koden direkte i din internetbrowser.

Faldgruben hos GitHub ligger i deres loft over baggrundsopgaver. Planen inkluderer nemlig præcis 2.000 minutters gratis GitHub Actions (automatiske kørsler) pr. måned[^1]. Hver gang du uploader en lille opdatering til din applikation, kan en Action køre i baggrunden for at bygge den. Hvis du lader din AI skrive scripts, der rutinemæssigt tester og opdaterer din kode adskillige gange i timen, vil du lynhurtigt udtømme dine 2.000 Actions-minutter/md, hvorefter automatiseringen låser.

**Andet skridt: Deploy på Vercel**
Når din kode er trygt placeret på GitHub, skal den forvandles til en faktisk hjemmeside. Her opretter du en konto hos Vercel og forbinder den med GitHub. Vercel henter nu din kode og lægger den på en offentlig webadresse. På deres gratis niveau, Vercel Hobby, er reglen klar: Der tillades kun ÉN udvikler pr. konto (ingen med-udviklere/team). Kapaciteten er dog enorm for en nybegynder: Du får 100 GB Fast Data Transfer/md (hurtig dataoverførsel) og hele 1 million funktionskald/md. Skulle du overskride et loft, sættes funktionen bare på pause i ca. 30 dage — der kommer absolut ingen overraskelsesregning med posten.

Den afgørende faldgrube er Vercels strenge licens: Platformen er udtrykkeligt kun til PERSONLIGT, IKKE-kommercielt brug[^2]. Hvis du indsætter reklamer, kræver betaling for adgang, eller nævner din egen virksomhed, bryder du betingelserne. Det er præcis dette kommercielle forbud, GNISTEN selv trådte i tilbage i magasinets nummer 2, fordi vi overså det med småt.

**Tredje skridt: Tilføj database på Supabase**
Din hjemmeside kører nu via Vercel, men for at brugerne kan oprette profiler eller gemme oplysninger, mangler du et system til at huske data. Dette løses ved at oprette en database på Supabase, som du forbinder til din udgivne applikation. Med Supabase Free får du en 500 MB database og 1 GB fillager til billeder. Du får også 5 GB egress/md (udgående datatrafik), op til 50.000 månedlige aktive brugere, og du må have højst 2 aktive projekter ad gangen.

Supabases største faldgrube for hobby-udvikleren er deres krav om aktivitet. Reglen er stram, idet et gratis projekt sættes på PAUSE efter 1 uges inaktivitet (data bevares, men projektet skal genstartes manuelt)[^3]. Der er altså blot 1 uges inaktivitet før pause. Hvis ingen besøger din side, mens du holder ferie, lukker dit projekt simpelthen ned, indtil du selv logger ind i kontrolpanelet og genaktiverer det.

Styrer du uden om Vercels kommercielle forbud, Supabases automatiske pause og GitHubs Actions-minutloft, står intet i vejen for, at du kan bygge dit næste AI-eventyr uden at betale en krone.

[^1]: https://docs.github.com/en/get-started/learning-about-github/githubs-plans
[^2]: https://vercel.com/pricing
[^3]: https://supabase.com/pricing