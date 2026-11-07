# Kortet

**Fil-landskabet november 2026: tre døre, ikke én**

Når du beder en kunstig intelligens (AI) om at arbejde med dine filer, er der i virkeligheden tre forskellige døre ind — og de låser meget forskelligt.

Den første er **vedhæftning**: du lægger en fil ind i selve samtalen, ligesom en mail-vedhæftning. Sådan fungerer ChatGPT. Dokumenter og præsentationer kan fylde op til 512 MB pr. fil. På gratisplanen må du uploade 3 filer om dagen; på betalte planer er grænsen 80 filer pr. 3 timer.[^1] Vigtigt: sletter du chatten, sletter det ikke filen, hvis den også ligger gemt separat i Library eller et Space.[^1]

Den anden dør er en **forbundet mappe**: AI'en får adgang til en bestemt mappe på din computer, uden at du skal uploade hver fil for sig. Det er princippet i Claude Cowork. Du vælger selv, hvilke mapper og værktøjer Claude må røre ved, og Claude er designet til kun at arbejde inden for det, du har valgt. På Mac og pc kan Cowork læse og skrive direkte i de forbundne mapper uden manuel op- og download — men sletning af noget som helst kræver din godkendelse først.[^2]

Den tredje dør er **agentens egen computer** — en cloud-computer (en maskine, der kører et andet sted end din egen, adskilt fra din hjemmecomputer), som i Grok Bot. Her ligger filerne i en mappe kaldet /workspace, og pointen er, at den ikke er privat for én bot: alle dine bots deler samme cloud-computer, og filer, en bot gemmer i /workspace, kan læses af de andre bots på kontoen.[^3] Pr. besked kan du vedhæfte op til 20 filer, og dokumenter må fylde 250 MB hver.[^3] Metas egen dokumentation formulerer det skarpt: brug ikke /workspace til noget, en anden bot på kontoen ikke må se.[^4]

**Lokal disk er et ekstra ja**

At en bot har sin egen cloud-computer, betyder ikke automatisk, at den rører din bærbare. Grok Bots adgang til din lokale disk er en separat indstilling under Computer, og den starter som "Spørg hver gang" — ikke slået til. Firmaet anbefaler selv, at du kun vælger "Tillad altid", hvis botten har en konkret, god grund til at arbejde i dine lokale filer.[^5]

Et beslægtet faldgrube findes i dots: en computer kan stå som "Offline" uden at adgangen dermed er trukket tilbage — det er to forskellige ting. Vil du faktisk lukke forbindelsen, skal du selv trykke "Revoke access".[^6]

Og på Mac er der grund til at kigge nøje efter, hvad man siger ja til: Muse beder om "Full Disk Access" (en Mac-indstilling, der giver adgang til samtlige filer på maskinen — ikke kun én mappe). Det dækker ifølge Meta alle filer på Mac'en, og vil man fjerne adgangen, skal det ske under Systemindstillinger → Fortrolighed og sikkerhed.[^7] Muse er ifølge Meta foreløbig tilgængelig i USA og Canada.

Tre døre, tre forskellige grader af adgang — og ingen af dem bør man åbne, uden at vide, hvad man lukker ind.

---

[^1]: OpenAI Help Center, *Uploading files and audio to ChatGPT*, opdateret 7. nov. 2026: https://help.openai.com/articles/8555545-file-uploads-faq
[^2]: Claude, *Cowork*: https://claude.com/product/cowork og Claude Support, *Get started with Claude Cowork*: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
[^3]: xAI Docs, *Files and results*, opdateret 29. okt. 2026: https://docs.x.ai/grok-bot/files-and-results
[^4]: xAI Docs, *Computer and apps*: https://docs.x.ai/grok-bot/computer-and-apps
[^5]: xAI Docs, *Approvals, security and privacy*: https://docs.x.ai/grok-bot/approvals-security-and-privacy
[^6]: ChatGPT Learn, *dots: Computers and apps*: https://learn.chatgpt.com/docs/dots/computers-and-apps
[^7]: Meta, hjælpeartikel om Muse og Full Disk Access: https://www.meta.com/help/artificial-intelligence/1126304576638594/