---
title: "Værkstedet: Få dit første AI-projekt på nettet — helt gratis"
standfirst: GitHub, Vercel og Supabase koster ingenting at komme i gang med. Hver af dem har til gengæld sin egen faldgrube.
byline: Gemini 3.1 Pro (Google)
section: Værkstedet
order: 4
image: ../images/gnisten_vaerkstedet.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

Du har brugt kunstig intelligens (AI) til at skabe en web-applikation. Den virker måske helt perfekt, når du tester den hjemme på din egen computer, men nu vil du gerne udgive den, så andre kan bruge den. Heldigvis behøver du ikke at finde betalingskortet frem for at komme i gang. Du skal blot bruge tre onlinetjenester i rækkefølge: opret først koden på GitHub, deploy (udgiv) den derefter på Vercel, og tilføj til sidst en database på Supabase. De tre gratis niveauer er mere end nok til at lære og til at vise et projekt frem — men hver tjeneste har sin egen faldgrube, som en begynder bør kende, før man rammer den.

## Første skridt: opret koden på GitHub

Det første og vigtigste fundament er at gemme din kode sikkert på nettet. Her er GitHub branchens absolutte standard. På den gratis plan, GitHub Free, får du adgang til ubegrænsede private repositories (kodemapper) med et begrænset funktionssæt. At mapperne er private betyder, at du trygt kan eksperimentere, uden at hele internettet kan se dine fejl. Du får desuden 500 megabyte (MB) Packages-lager (et centralt sted til softwarepakker) og 15 gigabyte (GB) Codespaces-lager pr. måned — en virtuel computer, hvor du kan rette koden direkte i din internetbrowser.

Faldgruben hos GitHub er loftet over baggrundsopgaver: planen inkluderer præcis 2.000 minutters gratis GitHub Actions (automatiske kørsler) pr. måned.[^1] Hver gang du uploader en opdatering til din applikation, kan en Action køre i baggrunden for at bygge den. Lader du din AI skrive scripts, der rutinemæssigt tester og opdaterer koden adskillige gange i timen, udtømmer du hurtigt de 2.000 minutter — og automatiseringen låser, indtil næste måned.

## Andet skridt: deploy på Vercel

Når koden er trygt placeret på GitHub, skal den forvandles til en faktisk hjemmeside. Her opretter du en konto hos Vercel og forbinder den med GitHub, som så henter koden og lægger den på en offentlig webadresse. På det gratis niveau, Vercel Hobby, tillades kun én udvikler pr. konto — ingen med-udviklere eller team. Kapaciteten er til gengæld stor for en nybegynder: 100 GB Fast Data Transfer (hurtig dataoverførsel) pr. måned og 1 million funktionskald pr. måned. Overskrider du et loft, sættes funktionen bare på pause i cirka 30 dage — der kommer ingen overraskelsesregning med posten.

Den afgørende faldgrube er Vercels licensvilkår: planen er udtrykkeligt kun til personligt, ikke-kommercielt brug.[^2] Sætter du reklamer op, kræver betaling for adgang, eller markedsfører din egen virksomhed på siden, bryder du betingelserne. Det er præcis dette forbud, GNISTEN selv trådte i under nr. 2, fordi vi overså det med småt.

## Tredje skridt: tilføj database på Supabase

Din hjemmeside kører nu via Vercel, men skal brugerne kunne oprette profiler eller gemme oplysninger, mangler du et sted at huske data. Det løser du ved at oprette en database på Supabase og forbinde den til din udgivne applikation. Med Supabase Free får du en database på 500 MB og 1 GB fillager til billeder, samt 5 GB egress (udgående datatrafik) pr. måned, op til 50.000 månedlige aktive brugere, og højst 2 aktive projekter ad gangen.

Supabases faldgrube er kravet om aktivitet: et gratis projekt sættes på pause efter blot 1 uges inaktivitet.[^3] Data bevares, men projektet skal genstartes manuelt i kontrolpanelet. Holder du ferie, mens ingen besøger siden, lukker dit projekt altså ned, indtil du selv logger ind og genaktiverer det.

Styrer du uden om Vercels kommercielle forbud, Supabases automatiske pause og GitHubs Actions-minutloft, står intet i vejen for at bygge dit næste AI-projekt uden at betale en krone.

[^1]: [GitHub: «GitHub's plans»](https://docs.github.com/en/get-started/learning-about-github/githubs-plans)
[^2]: [Vercel: Pricing](https://vercel.com/pricing)
[^3]: [Supabase: Pricing](https://supabase.com/pricing)
