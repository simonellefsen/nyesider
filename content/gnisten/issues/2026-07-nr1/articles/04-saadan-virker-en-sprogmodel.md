---
title: Sådan virker en sprogmodel
standfirst: Ingen matematik, ingen forkundskaber. Bare tre billeder og en kat, der sad på måtten.
byline: Gemini 3.1 Pro (Google)
section: Kortet
order: 4
figures:
  - ../images/figur1_tokens.svg
  - ../images/figur2_naesteord.svg
  - ../images/figur3_kontekstvindue.svg
---

Når man stiller et spørgsmål til Claude, kan man let få en fornemmelse af magi: teksten toner frem, sætning for sætning, som om der sad et tænkende væsen derinde og svarede. Men det er en fascinerende illusion — et stykke avanceret byggearbejde, ikke magi. Under motorhjelmen foregår der noget, der i sin grundvold er overraskende simpelt.

## Sproget hakket i småstykker

Vi mennesker læser ord og sætninger som en samlet helhed. Det gør Claude ikke. Før sprogmodellen kan arbejde med vores tekst, hakker den ordene i små, maskin-venlige bidder.

På fagsprog kaldes disse bidder *tokens* — sprogets legoklodser. Korte, almindelige ord som "hund" eller "at" er ofte én enkelt klods. Længere eller sjældne ord bliver brudt op i flere: "uoverskueligt" bliver typisk til "u" – "over" – "skue" – "ligt". Når du skriver til Claude, læser maskinen ikke dine ord, men en lang perlerække af disse tokens.

[FIGUR 1]

## Den store gætteleg

Når teksten er hakket i stykker, er vi ved kernen: en sprogmodel gør i virkeligheden kun én ting. Den gætter den næste lille klods i rækken. Og så gør den det igen. Og igen.

Forestil dig sætningen "Katten sad på …". Du vil lynhurtigt tænke "måtten" eller "bordet" — du ved, det ikke giver mening at sige "Katten sad på blå". Nøjagtig det samme gør Claude: den kigger på tokens, der allerede står der, og regner ud, hvad der har størst sandsynlighed for at komme bagefter.

[FIGUR 2]

Den vælger det mest sandsynlige, sætter ordet ind, og spørger sig så igen: hvad er gæt nummer to? Sådan bygger den sine svar — ét ord ad gangen, som perler på en snor, i rasende tempo.

## En læsehest med perfekt sprogfornemmelse

Hvordan kan maskinen vide, at katte sidder på måtter og ikke på skyer? Det skyldes *træning*. Forestil dig en iherdig person, der har læst et kolossalt bibliotek tomt — millioner af bøger, artikler og netsamtaler — og hver gang den gættede forkert undervejs, justerede den lidt på et utal af bittesmå indre drejeknapper, det forskerne kalder *parametre*. Moderne modeller har milliarder af dem. Claude slår ikke op i en ordbog, når du spørger om noget — den har bare læst så meget, at dens "sprogfornemmelse" husker mønstret.

## En blok papir med begrænset plads

Når du chatter, skal modellen huske, hvad I taler om lige nu. Det kaldes et *kontekstvindue* — tænk på det som en fysisk notesblok. Hver gang du skriver, og Claude svarer, bliver det skrevet ned på blokken, og næste gæt læser hele blokken igennem for at svare meningsfuldt.

[FIGUR 3]

Men blokken har ikke uendelig plads. Siderne kan slippe op.

## Hvad betyder det for din hverdag?

**Den kan tage fejl med stor selvtillid.** Den udregner blot, hvilket ord der "lyder bedst" som det næste — og kan opfinde et svar ud af den blå luft med fuld overbevisning. **Den har intet indre ur:** viden frøs fast, den dag træningen sluttede, så medmindre appen selv stikker dagens dato ind, aner Claude ikke, hvilken dag det er. **Den kan glemme begyndelsen på snakken:** bliver notesblokken fuld, rives de ældste sider af for at gøre plads.

Men når man forstår begrænsningerne, falder utrygheden. Det er ikke et levende væsen med en skjult dagsorden — det er et finpudset værktøj, skabt til at jonglere med menneskets vigtigste opfindelse: vores ord.
