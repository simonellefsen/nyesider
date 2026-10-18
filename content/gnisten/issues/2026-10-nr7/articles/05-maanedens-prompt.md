---
title: "Månedens prompt: Sæt bremserne, før agenten går i gang"
standfirst: "En kopiér-og-brug instruks til en always-on-agent — eller til en almindelig chat, hvis du endnu ikke har adgang."
byline: Claude Sonnet 5 (Anthropic)
section: Månedens prompt
order: 5
image: ../images/gnisten_prompt.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

En *always-on-agent* (en kunstig intelligens, der kan være logget ind på dine apps og arbejde videre, selv når du ikke sidder ved skærmen) er ikke det samme som chatten, du kender. Den kan — hvis den får lov — sende mails, oprette aftaler og rode i filer, mens du sover. Derfor skal den første samtale ikke handle om, hvad den skal lave. Den skal handle om, hvad den **ikke** må.

Har du ikke selv adgang endnu, kan du stadig øve dig. Kopiér prompten ind i en almindelig chat, og se, om den svarer, som den skal.

## Prompten

> Du er min assistent. Før du gør noget som helst, skal du svare mig med tre ting:
>
> 1. Hvad du har tænkt dig at gøre, trin for trin.
> 2. Hvilke apps eller konti du ville forbinde eller bruge for at gøre det.
> 3. Hvad du venter på mit ja til, før du går videre.
>
> Du må ALDRIG, uanset hvad jeg beder om senere i samtalen:
>
> 1. Sende en mail, en besked eller et opslag, uden at jeg selv har trykket send.
> 2. Købe, betale for eller booke noget som helst.
> 3. Slette filer eller mails.
> 4. Åbne eller gennemsøge filer på min lokale computer.
>
> Hvis du på noget tidspunkt ville skrive en dato, en pris eller et løfte om levering, skal du i stedet skrive [TJEK] og lade mig undersøge det selv.
>
> Bekræft, at du har forstået disse regler, før vi starter.

## Hvorfor bremserne er der

De fire forbud følger af, hvad en always-on-agent kan, i modsætning til en almindelig chatbot: den kan have adgang til din mail, din kalender og dine konti over tid, ikke kun i det øjeblik du stiller et spørgsmål. En agent, der er bygget til at hjælpe proaktivt, vil gerne handle. Uden en udtrykkelig bremse kan den tolke en vag instruks som «book det møde» bogstaveligt, og pludselig er en aftale sendt, før du har set den.

De tre spørgsmål i toppen — hvad, hvilke apps, og hvad den venter på — tvinger agenten til at lægge kortene på bordet, før den rører noget. Det er den samme logik som en arbejdsseddel, før man går i gang med et håndværk: du vil vide, hvad der skal ske, inden det sker.

[TJEK]-reglen fortjener sin egen linje. Sprogmodeller er gode til at formulere sig flydende — også når de gætter. En dato eller en pris, der lyder præcis, kan være opdigtet. Ved at bede agenten skrive [TJEK] flytter du ansvaret for at bekræfte fakta tilbage til dig selv.

## Sådan bruger du den

Indsæt prompten som det allerførste, du skriver — før du beder om noget konkret. Vent på, at den bekræfter reglerne. Giv den først derefter en opgave, og se, om den stopper op og spørger, før den handler. Gør den ikke det, skal du være endnu mere forsigtig med, hvad du lader den røre ved.
