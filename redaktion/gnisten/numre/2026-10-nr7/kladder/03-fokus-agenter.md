# Tre AI-agenter, der arbejder videre, når du går hjem

Grok Bot, Muse og dots er tre bud på en *always-on-agent* — en AI-agent, der kan fortsætte en opgave i skyen, selv om din egen computer er slukket. De kan undersøge, sortere og forberede handlinger på dine vegne. Men deres priser, adgang og nødbremser er forskellige. Her kårer vi ingen vinder; vi stiller i stedet fire praktiske spørgsmål.

## Hvor starter jeg?

**Grok Bot** blev præsenteret 11. august 2026.[^1] Du skriver til den som til en kollega. Hver Bot har en vedvarende cloud-computer: en computer hos leverandøren med browser, filsystem og terminal, som husker sit arbejdsmiljø. Flere navngivne Bots kan arbejde parallelt, men de deler én computer — inklusive filer, browser og login — pr. konto. Arbejdet kan fortsætte, når din laptop er lukket.[^2] I august [skrev vi om betaen](/gnisten/2026-08-nr4/grokbot).

**Muse** blev lanceret 8. september 2026 og bruges gennem Muse-appen eller WhatsApp.[^3] Den arbejder i en Secure Virtual Machine, altså en sikret virtuel maskine (VM): et afgrænset computer­miljø i skyen. Ved lanceringen var Muse kun i USA; 29. september blev adgangen udvidet til USA og Canada.[^4] Meta skriver samtidig, at tjenesten er under begrænset afprøvning og ikke findes overalt. Der er ingen offentlig dansk dato eller dato for Det Europæiske Økonomiske Samarbejdsområde (EØS).

**dots** — officielt skrevet med små bogstaver — blev præsenteret 29. september 2026.[^5] En dot bruger modellen GPT-6 Astra, har sin egen cloud-computer og kan forbindes med over 4.000 apps via plugins, altså tilføjelser, gennem ChatGPT, Slack eller Teams. Pro er ikke tilgængeligt i EØS, Schweiz eller Storbritannien, mens Business Premium kan bruges i alle understøttede ChatGPT-regioner.[^6]

## Hvad må den?

Det afgøres ikke kun af, hvad agenten teknisk kan, men af hvilke tilladelser du giver.

Grok Bots deler computer og login. Det er praktisk, men betyder også, at en Bot kan møde filer og åbne browsersessioner fra en anden. Ved Auto Review kan du vælge **Allow once**, **Always allow** eller **Deny**. Udkast til mail og Slack bliver ikke sendt automatisk: Du vælger **Send** eller **Discard**.[^7]

I Muse vælger du selv apps, og om mailadgang kun må læse eller også sende. Meta oplyser, at Muse spørger før afsendelse af mail eller køb. For små virksomheder er princippet, at intet offentliggøres, sendes eller betales uden godkendelse.

Hos dots kan du lave regler som **Ask before taking action** eller **Hand off to you**. Proaktiv research er skrivebeskyttet: Den kan undersøge, men ikke sende, ændre indhold eller styre browseren. Adgang til din lokale computer er valgfri og slået fra som standard; den gives med **Allow access** og fjernes med **Revoke access**.

## Hvad koster det?

Grok Bot-priserne på produktsiden 18. oktober 2026 var **Premium 30 USD om måneden, Super 100 USD og Ultra 200 USD**. Bot er inkluderet med Premium, Super, Ultra, Teams og Enterprise. Free til 0 USD og Plus til 8 USD er andre abonnementstrin, men produktsiden placerer Bot fra Premium.[^8]

Muse har en gratis mulighed med forbrugsloft. **Power koster 20 USD om måneden** og giver 500 millioner Muse-tokens om ugen; **Max koster 100 USD** og giver tre milliarder. Tokens er små tekst- og dataenheder, som AI-systemet bruger til at måle forbruget.[^9]

Den første dot følger med **Pro eller Business Premium**. ChatGPT Pro koster **100, 200 eller 500 USD om måneden**, afhængigt af trin. OpenAI oplyser ikke på den angivne side, hvilket Pro-trin der eventuelt er minimum for dots.[^10]

## Hvordan siger jeg nej?

Til Grok Bot kan du skrive **Stop now**. Det standser arbejdet, men fortryder ikke det, agenten allerede har gjort. Brug derfor godkendelser ved handlinger, der er svære at rulle tilbage.

Muse tilbyder **Allow once**, **Deny** og **Always allow**. Du kan ændre appadgang, afbryde agenten eller bruge **Reset**, som sletter alt.[^11]

En dot kan pauses fra sin profil. **Reset** sletter samtaler, hukommelse og planlagte opgaver. Den vigtigste vane er derfor den samme hos alle tre: Giv mindst mulig adgang, vælg engangstilladelse først — og lad ikke bekvemmelighed blive til automatisk samtykke.

[^1]: xAI, [Introducing Grok Bot](https://x.ai/news/introducing-grok-bot).
[^2]: xAI Docs, [Grok Bot overview](https://docs.x.ai/grok-bot/overview).
[^3]: Meta, [Introducing Muse, a personal AI agent](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/).
[^4]: Meta, [Introducing Muse for small business](https://about.fb.com/news/2026/09/introducing-muse-small-business/).
[^5]: OpenAI, [Introducing dots](https://openai.com/index/introducing-dots/).
[^6]: OpenAI Help, [Getting started with your dot](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot).
[^7]: xAI Docs, [Grok Bot security](https://docs.x.ai/grok-bot/security).
[^8]: xAI, [Grok Bot](https://x.ai/bot).
[^9]: Meta Help, [Muse subscription plans](https://www.meta.com/help/subscriptions/1021145227643680/).
[^10]: OpenAI Help, [About ChatGPT Pro tiers](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers).
[^11]: Meta Help, [Manage Muse permissions and reset](https://www.meta.com/help/artificial-intelligence/1385290430137537/).