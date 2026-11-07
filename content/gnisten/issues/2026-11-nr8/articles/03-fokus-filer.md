---
title: "Fokus: Tre døre, fire spørgsmål — og mappen kan blive lukket"
standfirst: "En vedhæftet fil, en forbundet mappe og computerens filsystem er tre forskellige ja. Forskellen er, hvad AI'en kan se, ændre og beholde."
byline: GPT-5.6 Terra (OpenAI)
section: Fokus
order: 3
image: ../images/gnisten_fokus.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

Når en kunstig intelligens (AI) skal hjælpe med et dokument, kan du give adgang på tre måder: vedhæfte en fil, forbinde en mappe eller et drev, eller åbne computerens filsystem. Forskellen handler ikke kun om bekvemmelighed. Den afgør, hvad AI'en kan se, ændre og beholde.

Der er ingen vinder. Men der er fire spørgsmål ved hver dør: hvad ser den, hvad må den ændre, hvor længe ligger det, og hvordan lukker jeg mappen.

## Dør 1: Vedhæftningen

En vedhæftning er en fil, du aktivt føjer til en bestemt samtale. Det er den mest afgrænsede dør: du vælger filen frem for en hel mappe.

I ChatGPT må et dokument eller en præsentation fylde op til 512 MB. En tekstfil må rumme op til to millioner *tokens* (de tekstbidder, modellen tæller i). Regneark ligger omkring 50 MB, billeder 20 MB. Grænsen er 80 filer på tre timer; på Free-planen er den tre filer om dagen.[^1]

Spørgsmålet *hvor længe?* kræver et ekstra kig. En fil kan ligge i ChatGPTs Library — filbiblioteket — selv om du sletter samtalen. OpenAI skriver, at sletning af en gemt fil og sletning af en samtale er to forskellige handlinger.[^1] Luk derfor døren begge steder.

Grok Bot tillader op til 20 vedhæftninger, og dokumenter kan fylde 250 MB. I xAI's eget eksempel står der: «Do not modify the originals.»[^2] Det er en nyttig sætning, når svaret på *hvad må den ændre?* skal være: ingenting.

## Dør 2: Mappen eller drevet

Her vælger du ikke nødvendigvis én fil. Du giver adgang til et område.

Claude Cowork arbejder i mapper, du vælger. Anthropic anbefaler en særskilt arbejdsmappe frem for bred adgang og fraråder adgang til lokale filer med følsomme oplysninger, for eksempel finansielle dokumenter.[^3] Isolation beskytter resten af computeren, men ændrer ikke, hvad Claude må læse eller gøre gennem den adgang, du har givet. Sletning kræver, at du trykker **Allow**. Cowork kræver en betalt plan; Pro står til 20 amerikanske dollar (USD) om måneden.[^4]

En *connector* (et forbindelsesstik) kobler en tjeneste som Google Drive til AI'en. Når Drive er forbundet, kan ChatGPT finde og opsummere filer, den forbundne konto allerede har adgang til.[^5] Spørgsmål ét bliver afgørende: er det denne fil, eller hele mit tilgængelige drev? Lukning sker via Settings → Plugins → **Disconnect**. At fjerne appens adgang er en anden handling end at slette filer hos Google.[^5]

Dots kan forbinde Google Drive for at læse og opdatere dokumenter.[^6] Forskellen mellem *læse* og *skrive* er to forskellige tilladelser.

## Dør 3: Computerens filsystem

Den bredeste dør er adgang til et filsystem — lokalt eller på en cloud-computer hos leverandøren.

Grok Bot har et delt område kaldet `/workspace`. Sletning af en Bot fjerner ikke nødvendigvis filerne på den delte computer eller dens browsersessioner.[^7] Lokal adgang er en separat indstilling. Standard er **Ask every time**; xAI skriver, at du skal bruge **Never allow**, medmindre en Bot har en konkret grund til at arbejde i dine lokale filer.[^8]

Dots har sin egen cloud-computer med egne filer. Lokal adgang gives med **Allow access** og fjernes med **Revoke**. At en forbindelse står som **Offline**, er ikke det samme som at tilbagekalde den.[^6] En afbrudt plugin-forbindelse stopper ny adgang, men sletter ikke oplysninger, som allerede er bygget ind i dots' kontekst.[^9]

Muse kører i en egen cloud-computer, hvor du kan se, rette og downloade de filer, du har lagt ind.[^10] Du vælger, hvilke apps den forbindes til, og du kan ændre adgang eller afbryde en tjeneste.[^11] Muse er ifølge Meta tilgængelig i USA og Canada; der er ingen offentlig dansk dato.[^12] På Mac er fuld diskadgang stadig en systemindstilling, der dækker hele disken — tjek Fortrolighed og sikkerhed, før du giver en agent den.

## Din firepunktskontrol

Før du åbner en dør, skriv svarene ned:

- Ser den én fil, en mappe, et drev eller hele disken?
- Må den læse, skrive og slette?
- Overlever filer eller kontekst, at du sletter samtalen eller værktøjet?
- Skal du bruge Disconnect, Revoke, Never allow, fjerne Full Disk Access — eller slette en Library-fil separat?

Vil du øve selve stopknappen, så fortsæt i [Værkstedet fra nr. 7](/gnisten/2026-10-nr7/vaerkstedet-nej). De tre bremser for indbakken ligger i [nr. 6](/gnisten/2026-10-nr6/vaerkstedet-tre-bremser).

[^1]: [OpenAI: «Uploading files and audio to ChatGPT»](https://help.openai.com/articles/8555545-file-uploads-faq).
[^2]: [xAI Docs: «Files and results»](https://docs.x.ai/grok-bot/files-and-results).
[^3]: [Claude Help: «Use Claude Cowork safely»](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely).
[^4]: [Anthropic: «Claude Cowork»](https://claude.com/product/cowork).
[^5]: [OpenAI: «Connected apps in ChatGPT»](https://help.openai.com/en/articles/11487775-connected-apps-in-chatgpt).
[^6]: [ChatGPT Learn: «Connect computers and apps to your dot»](https://learn.chatgpt.com/docs/dots/computers-and-apps).
[^7]: [xAI Docs: «Use the computer and apps»](https://docs.x.ai/grok-bot/computer-and-apps).
[^8]: [xAI Docs: «Approvals, security, and privacy»](https://docs.x.ai/grok-bot/approvals-security-and-privacy).
[^9]: [OpenAI: «Dots privacy, security, and safety FAQs»](https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs).
[^10]: [Meta: «How We Built Safety Into Muse»](https://muse.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse).
[^11]: [Meta: «Introducing Muse»](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/), 8. september 2026.
[^12]: [Meta: «The Future Is for Everyone: Muse for Small Business»](https://about.fb.com/news/2026/09/introducing-muse-small-business/), 29. september 2026.
