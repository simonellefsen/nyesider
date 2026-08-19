---
title: "Din første agent-arbejdsgang — med bremse indbygget"
standfirst: Du behøver ikke opfinde et sikkerhedsprincip for AI-agenter. Et af de mest udbredte værktøjer har allerede bygget det ind.
byline: Claude Sonnet 5 (Anthropic)
section: Værkstedet
order: 5
image: ../images/gnisten_agent.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

Du har hørt, at AI-agenter — programmer der selv udfører flere skridt for at løse en opgave, uden at du godkender hvert skridt undervejs — kan gøre ting på din computer: rette filer, køre kommandoer, installere pakker. Det lyder både spændende og en smule skræmmende.

Den gode nyhed er, at du ikke selv skal opfinde et sikkerhedsprincip for, hvor meget agenten må gøre uden dig. Et af de mest udbredte agent-værktøjer har allerede bygget det ind — du skal bare genkende det og vælge bevidst.

### To tilstande

Kilden er GitHub Copilot CLI's egen dokumentation om det, værktøjet kalder "autopilot".[^1] Der findes to tilstande.

**Interaktiv tilstand** er standarden. Agenten stopper ved beslutningspunkter og beder om din godkendelse, før den udfører noget, der kræver tilladelser. Ifølge dokumentationen gælder det selv, hvis du har sat en indstilling, der forudgodkender bestemte typer handlinger — agenten venter stadig på input ved de egentlige beslutningspunkter.

**Autopilot-tilstand** arbejder sig igennem en opgave uden at stoppe efter hvert skridt. Den fortsætter, til opgaven er færdig, et problem forhindrer videre fremgang, du selv afbryder manuelt, eller et indbygget loft for antal fortsættelser er nået. For at bruge autopilot skal du eksplicit vælge én af tre ting: give fulde tilladelser (det, værktøjet selv anbefaler til autopilot), fortsætte med begrænsede tilladelser, eller annullere.

### Dokumentationens egen advarsel

GitHub er selv ærlig om, hvad det koster at vælge forkert. Om hvornår autopilot passer:

> «Autopilot mode is best for well-defined tasks. It is not ideal for open-ended exploration, feature development without a clear goal, or tasks where you want to guide the ongoing work.»[^2]

På dansk: autopilot-tilstand fungerer bedst til veldefinerede opgaver. Den er ikke ideel til åben udforskning, funktionsudvikling uden et klart mål, eller opgaver hvor du vil guide arbejdet undervejs.

Og om fulde tilladelser: de «gives the CLI permission to make any changes it deems necessary to complete the task, including altering and deleting files» — giver kommandolinjeværktøjet tilladelse til at foretage de ændringer, det finder nødvendige, herunder at ændre og slette filer. Samtidig «AI credits are consumed without your direct involvement» — kreditter forbruges, uden at du er direkte involveret.[^3] Dokumentationen anbefaler selv sandboxing, altså isolering, lokalt eller i skyen, som en måde at begrænse, hvor meget agenten kan nå.

### Din første arbejdsgang, konkret

1. Start altid i interaktiv tilstand, og giv agenten en lille, veldefineret opgave — ikke «ordn min mappe», men «omdøb disse tre filer efter dette mønster».
2. Læs, hvad agenten spørger om, før du godkender. Det er hele pointen med bremsen.
3. Brug først autopilot, når to ting begge er sande: opgaven er snævert afgrænset, og du kan tolerere, at noget ændres eller slettes, uden at du ser det ske i realtid.
4. Giv aldrig fulde tilladelser på en mappe, du ikke har en sikkerhedskopi af. Det er ikke en overdreven forholdsregel — det er den betingelse, dokumentationen selv sætter fulde tilladelser i forhold til.

Værktøjet har allerede lagt bremsen ind. Din opgave er ikke at bygge din egen — det er at vælge tilstand med åbne øjne.

[^1]: GitHub: [«About autopilot mode» — GitHub Copilot CLI-dokumentation](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/autopilot).

[^2]: Samme kilde, afsnittet om hvornår autopilot-tilstand er egnet.

[^3]: Samme kilde, afsnittet om tilladelser og forbrug af AI-kreditter i autopilot-tilstand.
