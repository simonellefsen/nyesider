# Månedens prompt: Hjælp, hvilken gratis cloud-tjeneste skal jeg vælge?

Du har en idé til et lille projekt — måske en simpel hjemmeside til foreningens medlemsliste, en chatbot til din keramikbutik, eller en database over din pladesamling, som du gerne vil kunne tilgå fra telefonen. Du har hørt, at der findes gratis niveauer (**free tier**, det gratis trin af en betalingstjeneste) hos udbydere som Vercel, Supabase, Netlify og en håndfuld andre navne, som florerer i AI-genererede vejledninger. Problemet er ikke mangel på muligheder — det er for mange, uden at du aner, hvilken der passer til lige præcis dit projekt.

Her er en prompt, du kan give til en AI-chatbot for at få hjælp til at vælge — ikke en facitliste, men en samtale, der tvinger dig til at tænke projektet igennem, før nogen anbefaler noget.

> Jeg vil bygge [beskriv dit projekt i én-to sætninger, fx "en lille hjemmeside med et kontaktformular til min håndværksvirksomhed" eller "en database, hvor jeg kan søge i min bogsamling"].
>
> Før du anbefaler nogen konkrete værktøjer eller tjenester, vil jeg have dig til at stille mig spørgsmål om:
> 1. Hvor mange mennesker forventer jeg besøger eller bruger det — pr. dag, ikke pr. år?
> 2. Skal data gemmes permanent (som en database), eller er det bare en statisk side?
> 3. Har jeg brug for et rigtigt domænenavn, eller er en gratis underadresse (som noget.vercel.app) fint?
> 4. Er der nogen chance for, at projektet vokser markant inden for det næste år?
>
> Når du har mine svar: giv mig 2-3 konkrete forslag til gratis niveauer, der passer — og fortæl mig eksplicit, hvad der sker, hvis jeg overskrider den gratis grænse. Skjul ikke, at der er en grænse.

**Hvorfor er den formuleret sådan?**

Den vigtigste sætning i prompten er *"før du anbefaler noget, stil mig spørgsmål"*. Uden den vil de fleste AI-chatbotter straks foreslå de mest kendte navne — fordi de optræder hyppigst i træningsdata, ikke fordi de passer til dit projekt. En statisk side til ti besøgende om måneden har helt andre behov end en chatbot, der potentielt rammer tusind samtaler på en dag.

Spørgsmål 1 og 2 tvinger modellen til at skelne mellem projekter, der reelt er "bare en side" og projekter, der kræver en database — for gratis niveauer er ofte generøse med det ene og stramme med det andet. Spørgsmål 3 forhindrer, at du betaler for noget, du ikke har brug for (et domænenavn), bare fordi det lyder mere professionelt. Spørgsmål 4 er måske det vigtigste: gratis niveauer er typisk designet til at lokke dig ind — og til at blive ubehagelige at forlade, når du vokser ud af dem.

Den sidste linje — *"skjul ikke, at der er en grænse"* — er der, fordi AI-chatbotter har en tendens til at være optimistiske på udbyderens vegne. De nævner gerne de gratis fordele, men glemmer let at forklare, hvad der konkret sker den dag, dit projekt rammer loftet: bliver siden langsom, lukker den ned, eller begynder den bare at koste penge uden varsel? Det er det spørgsmål, du som ikke-programmør har mindst forudsætning for selv at gennemskue — og derfor er det den, prompten insisterer på at få besvaret.