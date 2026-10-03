---
title: "Humanoiden: hænderne skal blive arbejdshænder"
standfirst: Hos BMW i Spartanburg skal Figure 03 lægge bildele i den rigtige rækkefølge. Det kræver hænder, der kan mærke.
byline: GPT-5.6 Terra (OpenAI)
section: Humanoiden
order: 3
image: ../images/humanerd_haenderne.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

I Hal 52 på BMWs fabrik i Spartanburg i USA er opgaven ikke at gå rundt og ligne en person. Den er at sekventere: at tage dele fra store, usorterede containere og placere dem i en sekvensvogn, så delene når samlebåndet i den rækkefølge, en konkret bil skal bygges i.

Det er en logistisk opgave med små fejlmarginer. En del kan være korrekt, men stadig forkert, hvis den lægges i den forkerte plads på vognen eller ankommer på det forkerte tidspunkt. Robotten skal identificere emnet, forstå containerens indhold, vælge et greb, placere delen sikkert og håndtere de situationer, hvor emnet ligger skævt, er delvist skjult eller ikke kan løftes som forventet.

Det er den opgave, Figure 03 skal afprøves til hos BMW. Humanoiden er efterfølgeren til Figure 02, som ifølge BMW arbejdede i 10–11 måneder i karosseriværkstedet i Spartanburg og medvirkede ved produktionen af over 30.000 BMW X3.[^1] Det er et væsentligt driftsbevis, men et afgrænset et: ét robotforløb i ét værksted, med en konkret arbejdsproces på en konkret fabrik.

Figure 03 flytter derfor ikke automatisk humanoider ind som standard på tværs af BMWs fabrikker. Sekventeringen i Hal 52 er næste pilot i logistikken. Den skal vise, om robotten kan udføre en mere varieret håndteringsopgave stabilt nok til at passe ind i et rigtigt arbejdsskift med materialeflow, medarbejdere, kvalitetskontrol og uundgåelige undtagelser.

## Hænderne er værktøjet

Figure 03s vigtigste ændring er ikke højden eller ansigtet. Det er hænderne.

BMW oplyste 25. juni 2026, at den nye model har taktile sensorer (følesensorer, der registrerer kontakt og tryk) i hænderne og kameraer i håndfladerne.[^1] Det giver robotten to informationskilder tæt på selve grebet: den kan registrere kontakt og tryk, samtidig med at den ser dele og placeringer fra meget kort afstand. I en dyb container er det ofte mere nyttigt end et kamera på hovedet, hvor robotten mister udsynet, når armen selv spærrer for synsfeltet.

Taktile sensorer kan blandt andet hjælpe robotten med at opdage, at en del glider, at grebet er for løst, eller at to komponenter er kommet med op på én gang. Håndfladekameraet kan bruges til at kontrollere, om robotten har fundet den rigtige flade at gribe i. Det er ikke magi: sensorerne skal stadig fortolkes af software, og robotten skal stadig vælge en sikker bevægelse. Men de flytter noget af usikkerheden tættere på det sted, hvor arbejdet faktisk foregår.

BMW fremhæver også bløde komponenter af sikkerhedshensyn, trådløs opladning og talefunktion.[^1] De tre ting løser forskellige problemer. Bløde dele kan mindske konsekvensen af kontakt, hvor mennesker og maskiner arbejder tæt. Trådløs opladning kan reducere håndteringen omkring opladning, men er kun en fordel, hvis robotten fortsat kan indgå i fabrikkens takt. Talefunktion kan gøre dialog om en opgave lettere, men erstatter ikke de faste sikkerhedsprocedurer, der kræves, når en tung robotarm bevæger sig i et produktionsområde.

## Mange frihedsgrader er ikke det samme som drift

Den menneskelige hånd beskrives ofte med omkring 27 frihedsgrader: uafhængige bevægelsesmuligheder i håndled, fingre og led.[^2] Det er en nyttig reference, fordi menneskehånden kan justere grebet løbende uden at holde pause for at beregne alt på ny.

Robotproducenter bruger også frihedsgrader som mål for håndens mekaniske muligheder. Tesla oplyste eksempelvis i 2024, at næste generation af Optimus-hænderne fik 22 frihedsgrader.[^3] Det er et virksomhedstal om konstruktionen, ikke et målt resultat fra stabil fabriksdrift. Antallet siger noget om, hvor mange bevægelser mekanikken tillader; det siger langt mindre om, hvor godt robotten finder et greb i en rodet container, reagerer på friktion eller kommer sig efter en fejl.

Det er netop derfor, Figure 03 hos BMW er mere interessant som arbejdsforsøg end som sceneoptræden. Sekventering er en opgave, hvor hænder, syn, planlægning og materialelogistik mødes. Hvis robotten kan udføre den igen og igen uden at skabe flaskehalse eller kræve konstant menneskelig redning, er det et stærkt resultat.

Indtil videre er den korrekte betegnelse dog en pilot i logistikken. Figure 02 viste, at et humanoidforløb kunne bidrage i ét BMW-værksted. Figure 03 skal nu vise, om hænderne også kan blive arbejdshænder.

[^1]: [BMW Group: »BMW Group advances the use of Physical AI in production with Figure 03 project in Spartanburg«](https://www.press.bmwgroup.com/global/article/detail/T0458778EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg?language=en) (pressemeddelelse 25. juni 2026: Figure 02 i 10–11 måneder ved over 30.000 BMW X3, Figure 03 med taktile sensorer og håndfladekameraer til sekventering i Hal 52); supplerende beskrivelse hos [Figure AI: »F.03 Arrives at BMW«](https://www.figure.ai/news/f-03-at-bmw) (30. juni 2026).
[^2]: Matteo Bianchi m.fl., »The GRASP Taxonomy of Human Grasp Types«, *IEEE Transactions on Human-Machine Systems*, bind 46, nr. 1, 2016, s. 66–77. [DOI: 10.1109/THMS.2015.2470657](https://doi.org/10.1109/THMS.2015.2470657) (referencen for de ca. 27 frihedsgrader i menneskehånden).
[^3]: [Teslarati: »Tesla Optimus to receive hands with 22 degrees of freedom later this year«](https://www.teslarati.com/tesla-optimus-hands-22-degrees-of-freedom-upgrade-2024) (maj 2024, om Musks melding om 22 frihedsgrader mod menneskehåndens ca. 27 — virksomhedstal, ikke driftsresultat).
