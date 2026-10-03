---
title: "Værkstedet: Lad AI læse din indbakke — men aldrig sende for dig"
standfirst: To spor, tre bremser. Ingen af dem kræver kode, og det sikre begynderspor forbinder slet ikke din postkasse.
byline: Claude Sonnet 5 (Anthropic)
section: Værkstedet
order: 4
image: ../images/gnisten_vaerkstedet.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

Du behøver ikke kunne kode for at få kunstig intelligens (AI) til at hjælpe med en fyldt indbakke. Du skal sætte tre faste bremser op, før du begynder: **send aldrig** automatisk, **slet aldrig** automatisk, og lad AI **aldrig love** en dato, en refus eller en levering på dine vegne. Alt det er dit at skrive. AI'en må kun foreslå.

Der er to spor, afhængigt af hvad du bruger i forvejen.

## Spor 1: Du bruger Gmail

Åbn en af de lange tråde, du har udsat at svare på. Gmail viser i mange tilfælde en gratis AI-sammenfatning (*AI Overview*) øverst i tråden, som samler, hvad der egentlig blev sagt. Brug den til at forstå tråden hurtigt — ikke til at handle på den blindt.

Brug derefter funktionen Help Me Write til at generere et svar. Pointen er: det er en **kladde**, ikke en afsendt mail. Læs den igennem, ret tonen, fjern eventuelle løfter om datoer eller penge, du ikke selv har godkendt, og tryk selv på send. Google har beskrevet, hvordan AI-funktionerne bygges ind i Gmail, i forbindelse med det, de kalder Gemini-æraen for Gmail.[^1]

Her ligger den første bremse indbygget i selve arbejdsgangen: så længe du aldrig slår automatisk afsendelse til, er send stadig din knap.

## Spor 2: Du vil ikke have AI inde i selve mailprogrammet

Kopiér én mail — eller et uddrag af en lang tråd — ind i en almindelig AI-chat. Brug en fast instruks hver gang, for eksempel:

> Klassificér denne mail som «svar i dag», «parkér» eller «reklame». Skriv derefter et udkast til svar. Hvor der ellers ville stå et løfte om dato, refus eller levering, skal du i stedet skrive [TJEK].

Udkastet bliver stående i chatten. Du kopierer det selv tilbage i mailprogrammet, retter [TJEK]-markeringerne til noget, du kan stå inde for, og trykker send. Sletning sker også kun af dig, inde i mailprogrammet — aldrig i chatten.

## Hvorfor spor 2 er det forsigtige begynderspor

Når AI-chatbotten ChatGPT kobles direkte til en Google-konto gennem den indbyggede Google-app, beder forbindelsen ifølge OpenAIs egen hjælpeside om adgangsrettigheden (scopet) `gmail.modify`.[^2] *Modify* betyder ikke kun læse; det betyder, at forbindelsen i princippet kan ændre i din mail, hvis den tildeles rettigheden i godkendelsesprocessen (Open Authorization, OAuth).

ChatGPTs tilsvarende app til Outlook kan ifølge OpenAI sende almindelig tekst-mail, når brugeren har givet rettigheden Mail.Send.[^3] Og hos Microsoft nævner den officielle FAQ om Copilot i Outlook sletning som en del af det, værktøjet kan gøre under oprydning — altså en reel slet-funktion, ikke kun et forslag til, hvad du selv skal slette.[^4]

Det er ikke farligt i sig selv at give den slags rettigheder. Men det kræver, at man bevidst har læst, hvad man siger ja til — og det er netop den opmærksomhed, en nybegynder sjældent har overskud til midt i en overfyldt indbakke. Derfor: indtil du har siddet med rettighedslisten og forstået den, er kopiér-ind-i-chat det sikre spor. Der er ingen forbindelse, der kan sende eller slette noget. Kun du.

## De tre bremser, skrevet ned et sted du kan se dem

Hæng en seddel op, eller sæt en note øverst i din AI-chat: *Jeg sender selv. Jeg sletter selv. AI'en lover intet på mine vegne — den skriver [TJEK].* Ingen af de to spor kræver programmering, et Model Context Protocol (MCP) eller en API-nøgle (*application programming interface*). Det kræver, at du læser kladden, før du trykker på knappen.

[^1]: [Google: «Gmail is entering the Gemini era»](https://blog.google/products-and-platforms/products/gmail/gmail-is-entering-the-gemini-era/).
[^2]: [OpenAI Help Center: «Google app for ChatGPT – Data & Controls FAQ»](https://help.openai.com/articles/10408842-google-app-for-chatgpt-data-controls-faq).
[^3]: [OpenAI Help Center: «Outlook Email and Calendar app for ChatGPT»](https://help.openai.com/articles/12512241-outlook-email-and-calendar-app-for-chatgpt).
[^4]: [Microsoft Support: «Frequently asked questions about Copilot in Outlook»](https://support.microsoft.com/en-us/outlook/frequently-asked-questions-about-copilot-in-outlook).
