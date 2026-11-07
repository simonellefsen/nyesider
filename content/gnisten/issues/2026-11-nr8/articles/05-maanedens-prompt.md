---
title: "Månedens prompt: Sig ja til filen — ikke til drevet"
standfirst: "En kopiér-og-brug instruks, du giver chatbotten, før du vedhæfter noget. En fil er et ja. Et drev er et andet."
byline: Claude Sonnet 5 (Anthropic)
section: Månedens prompt
order: 5
image: ../images/gnisten_prompt.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

Du har en rapport, du vil have en chatbot til at kigge på. Eller du bruger en *always-on-agent* (en kunstig intelligens, der kan køre videre og få adgang til mapper, uden at du starter hver samtale). Før du vedhæfter filen, er der ét skridt, de fleste springer over: at fortælle botten, hvad den **ikke** må.

En vedhæftet fil er et ja til dén fil. Et forbundet drev — Google Drive, Dropbox, OneDrive — eller adgang til din lokale computer via *Full Disk Access* (fuld diskadgang) er et ja til meget mere. Og tryk på Disconnect bagefter sletter ikke det, agenten allerede har læst. Derfor: giv denne instruks, **før** du vedhæfter noget.

## Prompten

> Læs kun den fil, jeg selv vedhæfter i denne besked. Åbn ikke andre filer, mapper eller drev — hverken lokalt eller i skyen. Ændr ikke originalen. Slet aldrig filer. Foreslå aldrig at forbinde Google Drive, Dropbox, OneDrive eller min lokale computer til denne samtale.
>
> Hvis du på noget tidspunkt ville skrive, at du har læst eller gennemgået en hel mappe eller et helt drev, skal du i stedet skrive [TJEK] og stoppe der.
>
> Svar først med præcis tre ting:
> 1. Hvilken fil du har modtaget (navn og format).
> 2. Hvad du har tænkt dig at gøre med den.
> 3. Hvad du venter på mit ja til, før du går videre.
>
> Gør ikke andet, før jeg har svaret ja.

## Hvorfor denne rækkefølge

Sætninger som «jeg har gennemgået dine filer» dækker ofte over, at agenten har fået adgang, den ikke behøvede. Ved at bede om [TJEK] i stedet for et løfte om fuldstændighed tvinger du botten til at vise, hvor grænsen for dens adgang går.

Det samme gælder for always-on-agenter, der kører i baggrunden — uanset om det er en almindelig chat eller en mere specialiseret agent som dots. Jo mere en tjeneste er bygget til at huske og handle uden at spørge hver gang, jo vigtigere er det at sætte grænsen, før den første fil lander i samtalen.

Tre-trins-svaret (fil, plan, ventepunkt) er din kvittering for, at botten har forstået opgaven som «læs denne ene fil» og ikke som «gør dig hjemme». Får du i stedet et svar, der nævner en mappe, et drev eller et tilbud om at forbinde en tjeneste, du ikke bad om, så start forfra, før du går videre.

Har du ikke en agent endnu, kan du øve den samme prompt i en almindelig chat. Vedhæft kun dummy-filen. Det koster intet, og det er den sikre måde at opbygge vanen på, før nogen beder om mappen.
