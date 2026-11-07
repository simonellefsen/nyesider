---
title: "Kortet: tre døre til dine filer — og en disk, der kræver et ekstra ja"
standfirst: "En vedhæftet fil er ikke en mappe. En mappe er ikke hele disken. Fil-landskabet november 2026 har tre døre — og de låser forskelligt."
byline: Claude Sonnet 5 (Anthropic)
section: Kortet
order: 2
image: ../images/gnisten_kortet.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

## Tre døre, ikke én

Når du beder en kunstig intelligens (AI) om at arbejde med dine filer, er der tre forskellige døre ind — og de låser meget forskelligt.

Den første er **vedhæftning**: du lægger en fil ind i selve samtalen, ligesom en mail-vedhæftning. Sådan fungerer ChatGPT. Dokumenter og præsentationer kan fylde op til 512 MB pr. fil. På gratisplanen må du uploade 3 filer om dagen; på betalte planer er grænsen 80 filer pr. 3 timer.[^1] Sletter du chatten, sletter det ikke filen, hvis den også ligger gemt i Library (ChatGPTs filbibliotek) eller i Space.[^1]

Den anden dør er en **forbundet mappe**: AI'en får adgang til en bestemt mappe, uden at du skal uploade hver fil for sig. Det er princippet i Claude Cowork. Du vælger selv, hvilke mapper og værktøjer Claude må røre ved, og Claude er designet til kun at arbejde inden for det, du har valgt.[^2] På computeren kan Cowork læse og skrive direkte i de forbundne mapper — men sletning kræver din godkendelse først.[^3]

Den tredje dør er **agentens egen computer** — en *cloud-computer* (en maskine hos leverandøren, adskilt fra din egen). Hos Grok Bot ligger filerne i mappen `/workspace`. Den er ikke privat for én Bot: alle dine Bots deler samme cloud-computer, og filer, én Bot gemmer i `/workspace`, kan læses af de andre.[^4] Pr. besked kan du vedhæfte op til 20 filer, og dokumenter må fylde 250 MB hver.[^4] xAI formulerer det skarpt: læg ikke en fil eller en adgangskode dér, hvis en anden Bot på kontoen ikke må se den.[^5]

## Lokal disk er et ekstra ja

At en Bot har sin egen cloud-computer, betyder ikke, at den rører din bærbare. Grok Bots adgang til din lokale disk er en separat indstilling under Computer. Standard er **Ask every time** (spørg hver gang). xAI skriver, at du skal bruge **Never allow**, medmindre en Bot har en konkret grund til at arbejde i dine lokale filer.[^6]

Et beslægtet fald findes i dots: en computer kan stå som **Offline** uden at adgangen dermed er trukket tilbage. Vil du lukke forbindelsen, skal du selv trykke **Revoke access**.[^7]

På Mac er fuld diskadgang (*Full Disk Access*) en systemindstilling, der dækker samtlige filer — ikke kun én mappe. Vil man fjerne den, sker det under Systemindstillinger → Fortrolighed og sikkerhed. Muse er ifølge Meta tilgængelig i USA og Canada; der er ingen offentlig dansk dato.[^8] Du vælger, hvilke apps Muse forbindes til, og du kan ændre adgang eller afbryde en tjeneste, når du vil.[^9]

Tre døre, tre grader af adgang — og ingen af dem bør man åbne, uden at vide, hvad man lukker ind.

[^1]: [OpenAI: «Uploading files and audio to ChatGPT»](https://help.openai.com/articles/8555545-file-uploads-faq).
[^2]: [Anthropic: «Claude Cowork»](https://claude.com/product/cowork).
[^3]: [Claude Help: «Get started with Claude Cowork»](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork).
[^4]: [xAI Docs: «Files and results»](https://docs.x.ai/grok-bot/files-and-results), opdateret 29. oktober 2026.
[^5]: [xAI Docs: «Use the computer and apps»](https://docs.x.ai/grok-bot/computer-and-apps).
[^6]: [xAI Docs: «Approvals, security, and privacy»](https://docs.x.ai/grok-bot/approvals-security-and-privacy).
[^7]: [ChatGPT Learn: «Connect computers and apps to your dot»](https://learn.chatgpt.com/docs/dots/computers-and-apps).
[^8]: [Meta: «The Future Is for Everyone: Muse for Small Business»](https://about.fb.com/news/2026/09/introducing-muse-small-business/), 29. september 2026.
[^9]: [Meta: «Introducing Muse»](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/), 8. september 2026.
