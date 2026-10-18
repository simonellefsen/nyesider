---
title: "Værkstedet: Prøv agenten — uden at give den nøglerne"
standfirst: "To spor, tre bremser. Find stop-knappen, før du åbner mail, betaling eller din egen disks filer."
byline: Claude Sonnet 5 (Anthropic)
section: Værkstedet
order: 4
image: ../images/gnisten_vaerkstedet.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

I nr. 6 lovede vi at vise, hvordan du siger nej, når AI vil have nøglerne. Her er den del indfriet. Hvad der sker, når assistenten kigger i dine filer, gemmer vi til nr. 8. I dag: en *always-on-agent* (en kunstig intelligens, der kører i baggrunden og kan tage initiativer, i modsætning til en chatbot du selv skal spørge hver gang) — og hvordan du giver den en opgave uden at give den nøglerne til din konto.

Tre bremser, skrevet som handlinger, ikke som løfter:

**A. Send aldrig automatisk.** Et udkast til en mail, en besked eller et opslag skal vente på dit tryk, før det forlader skærmen.

**B. Køb eller betal aldrig automatisk.** Ingen agent skal gennemføre en betaling, en bestilling eller et kortkøb, uden at du selv bekræfter.

**C. Giv aldrig adgang til din egen computers filer, før du har set stop-knappen.** Find og afprøv stopfunktionen, mens opgaven er triviel — ikke første gang det haster.

## Spor 1: Du har endnu ikke adgang

De fleste danske privatbrugere har endnu ikke adgang til nogen af de tre produkter. Metas Muse er ifølge Metas egne sider ikke udrullet overalt og beskrives som tilgængelig i USA og Canada.[^1] OpenAIs dots på Pro-abonnementet er uden for Det Europæiske Økonomiske Samarbejdsområde (EØS), Schweiz og Storbritannien.[^2] Gør derfor det eneste fornuftige: kopiér aldrig adgangskoder ind i en chatboks, uanset hvor overbevisende den beder om det.

Til gengæld kan du øve selve nej-sætningen i en almindelig chatbot allerede i dag:

> Foreslå aldrig at sende, købe eller slette. Skriv [TJEK] dér, hvor der ellers ville stå et løfte. Spørg, før du anbefaler at forbinde en app.

Det koster intet, kræver ingen konto hos de tre produkter, og det er den sikre måde at opbygge vanen på, før du giver en agent adgang til noget som helst.

## Spor 2: Du har adgang

Har du Grok Bot via The X Subscription Premium, dots via OpenAIs Business Premium i en understøttet region, eller Muse i USA eller Canada, gælder en anden regel: første opgave skal være en, der ikke kræver login til mail, betaling eller din lokale disk.

**Grok Bot.** xAI's eget første-eksempel er at vedhæfte et dokument og bede om fem punkter — med instruktionen «Do not change the source file».[^3] Når den opgave er løst, sætter du bremserne, før du giver den mere: skriv **Stop now** for at standse det igangværende (det fortryder ikke det, der allerede er gjort),[^4] og brug Auto Review med **Ask first**, før den sender ekstern mail.[^5] Husk: dine Grok Bots deler én computer — logins og filer på den maskine er tilgængelige for alle dine Bots.[^6]

**dots.** Sæt **Pause** i profilens •••-menu, før du går videre. Under Custom rules vælger du **Ask before taking action** og **Hand off to you**, og tjek at adgang til din lokale computer står slået fra. Vil du tage adgangen tilbage, bruger du **Revoke access**.[^2] OpenAI beskriver dots' proaktive baggrunds-research som skrivebeskyttet — men det gælder kun den research, ikke de opgaver du selv beder om.

**Muse.** Åbn Settings og tilladelserne, før du giver den en opgave. Muse spørger ved handlinger, der er svære at fortryde — som at sende mail eller købe — og du kan skrue standarden mere forsigtig.[^7] Intet offentliggøres, sendes eller betales uden godkendelse, ifølge Meta.[^1]

Fælles for alle tre: den første opgave er en test af bremsen, ikke af agenten. Virker stop, pause og ask, før du har givet adgang til noget vigtigt, har du lært det billigt. Næste gang — i nr. 8 — ser vi på, hvad en agent kan se, når den først er inde i dine filer.

[^1]: [Meta: «The Future Is for Everyone: Muse for Small Business»](https://about.fb.com/news/2026/09/introducing-muse-small-business/), 29. september 2026.
[^2]: [OpenAI Help: «Getting started with your dot»](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot).
[^3]: [xAI Docs: «Get started»](https://docs.x.ai/grok-bot/get-started).
[^4]: [xAI Docs: «Message and collaborate»](https://docs.x.ai/grok-bot/chat-and-collaboration).
[^5]: [xAI Docs: «Approvals, security, and privacy»](https://docs.x.ai/grok-bot/approvals-security-and-privacy).
[^6]: [xAI Docs: «Grok Bot»](https://docs.x.ai/grok-bot/overview).
[^7]: [Meta: «How We Designed Muse»](https://introducing.muse.ai/).
