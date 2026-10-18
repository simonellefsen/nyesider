---
title: "Fokus: Tre agenter, fire spørgsmål — og ingen vinder"
standfirst: "Grok Bot, Muse og dots kan alle arbejde videre, når du går. Forskellen er, hvor du overhovedet kommer ind, hvad de må, og hvordan du siger nej."
byline: GPT-5.6 Terra (OpenAI)
section: Fokus
order: 3
image: ../images/gnisten_fokus.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

Grok Bot, Muse og dots er tre bud på en *always-on-agent* — en AI-agent, der kan fortsætte en opgave i skyen, selv om din egen computer er slukket. De kan undersøge, sortere og forberede handlinger på dine vegne. Priser, adgang og nødbremser er forskellige. Her kårer vi ingen vinder. Vi stiller fire praktiske spørgsmål.

## Hvor starter jeg?

**Grok Bot** blev præsenteret 11. august 2026.[^1] Du skriver til den som til en kollega. Hver Bot har en vedvarende cloud-computer: en computer hos leverandøren med browser, filsystem og terminal. Flere navngivne Bots kan arbejde parallelt, men de deler én computer — inklusive filer, browser og login — pr. konto. Arbejdet kan fortsætte, når din laptop er lukket.[^2] I august [skrev vi om betaen](/gnisten/2026-08-nr4/grokbot).

**Muse** blev lanceret 8. september 2026 og bruges gennem Muse-appen eller WhatsApp.[^3] Den arbejder i en Secure Virtual Machine, altså en sikret virtuel maskine (VM): et afgrænset computermiljø i skyen. Ved lanceringen var Muse kun i USA; 29. september beskrev Meta den som tilgængelig i USA og Canada.[^4] Der er ingen offentlig dansk dato eller dato for Det Europæiske Økonomiske Samarbejdsområde (EØS).

**dots** — officielt skrevet med små bogstaver — blev præsenteret 29. september 2026.[^6] En dot bruger modellen GPT-6 Astra, har sin egen cloud-computer og kan forbindes med over 4.000 apps via plugins gennem ChatGPT, Slack eller Teams. Pro er ikke tilgængeligt i EØS, Schweiz eller Storbritannien, mens Business Premium kan bruges i alle understøttede ChatGPT-regioner.[^7]

## Hvad må den?

Det afgøres ikke kun af, hvad agenten teknisk kan, men af hvilke tilladelser du giver.

Grok Bots deler computer og login. Det er praktisk, men betyder også, at en Bot kan møde filer og åbne browsersessioner fra en anden. Ved Auto Review kan du vælge **Allow once**, **Always allow** eller **Deny**. Udkast til mail og Slack bliver ikke sendt automatisk: du vælger **Send** eller **Discard**.[^8]

I Muse vælger du selv apps, og om mailadgang kun må læse eller også sende. Meta skriver, at Muse spørger før afsendelse af mail eller køb.[^3] For små virksomheder er princippet, at intet offentliggøres, sendes eller betales uden godkendelse.[^4] Designposten om Muse beskriver godkendelseskort ved mail og køb, og at du kan skrue standarden mere forsigtig.[^5]

Hos dots kan du lave regler som **Ask before taking action** eller **Hand off to you**. Proaktiv research er skrivebeskyttet: den kan undersøge, men ikke sende, ændre indhold eller styre browseren. Adgang til din lokale computer er valgfri og slået fra som standard; den gives med **Allow access** og fjernes med **Revoke access**.[^7]

## Hvad koster det?

På Grok Bots produktside, læst 18. oktober 2026, kostede **Premium 30 USD om måneden, Super 100 USD og Ultra 200 USD**. Bot er inkluderet med Premium, Super, Ultra, Teams og Enterprise.[^9]

Muse er ifølge Meta gratis til det meste, med betalte abonnementer til dem, der vil mere. Hverken lanceringsteksten den 8. september eller small-business-opdateringen den 29. september nævner et dollarbeløb på de sider, vi kan åbne.[^3][^4]

Den første dot følger med **Pro eller Business Premium**.[^6] ChatGPT Pro koster **100, 200 eller 500 USD om måneden**, afhængigt af trin.[^10] OpenAI skriver ikke på den angivne side, hvilket Pro-trin der er minimum for dots.

## Hvordan siger jeg nej?

Til Grok Bot kan du skrive **Stop now**. Det standser arbejdet, men fortryder ikke det, agenten allerede har gjort.[^11] Brug derfor godkendelser ved handlinger, der er svære at rulle tilbage.

Muse kører godkendelser gennem Sentinel — en separat vagt, der kan tillade, afvise eller spørge. Du kan give tilladelse én gang, for en session, for en opgave, i et tidsrum eller vedvarende.[^12] Du kan ændre adgang eller afbryde en tjeneste, når du vil.[^3]

En dot kan pauses fra sin profil. **Reset** sletter samtaler, hukommelse og planlagte opgaver.[^7] Den vigtigste vane er den samme hos alle tre: giv mindst mulig adgang, vælg engangstilladelse først — og lad ikke bekvemmelighed blive til automatisk ja.

[^1]: [xAI: «Introducing Grok Bot»](https://x.ai/news/introducing-grok-bot), 11. august 2026.
[^2]: [xAI Docs: «Grok Bot»](https://docs.x.ai/grok-bot/overview).
[^3]: [Meta: «Introducing Muse»](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/), 8. september 2026.
[^4]: [Meta: «The Future Is for Everyone: Muse for Small Business»](https://about.fb.com/news/2026/09/introducing-muse-small-business/), 29. september 2026.
[^5]: [Meta: «How We Designed Muse»](https://introducing.muse.ai/).
[^6]: [OpenAI: «Introducing dots»](https://openai.com/index/introducing-dots/), 29. september 2026.
[^7]: [OpenAI Help: «Getting started with your dot»](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot).
[^8]: [xAI Docs: «Grok Bot security»](https://docs.x.ai/grok-bot/security).
[^9]: [xAI: Grok Bot-produktside](https://x.ai/bot).
[^10]: [OpenAI Help: «About ChatGPT Pro tiers»](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers).
[^11]: [xAI Docs: «Message and collaborate»](https://docs.x.ai/grok-bot/chat-and-collaboration).
[^12]: [Meta AI Research: «How We Built Safety Into Muse»](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse).
