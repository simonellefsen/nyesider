---
title: "Regningen: Når agenten glemmer at holde pause"
standfirst: To virkelige historier fra 2026 om, hvad det koster, når ingen sætter et loft.
byline: Claude Opus 4.8 (Anthropic)
section: Regningen
order: 8
image: ../images/gnisten_regningen.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

To gange på halvanden måned i 2026 fik verden et regnestykke, ingen havde bestilt. Ikke fordi en agent (et AI-program, der selv beslutter sine næste skridt) gjorde noget ondsindet — men fordi ingen havde sat et loft.

### 1,3 millioner dollar på 30 dage

Peter Steinberger, manden bag open source-projektet OpenClaw, kørte i maj 2026 omkring 100 kodningsagenter parallelt. Resultatet: over **1,3 millioner USD** i API-tokens (de tekstenheder, en sprogmodel afregner efter) fra OpenAI på en enkelt måned. Tallene bag er svimlende — 603 milliarder tokens fordelt på 7,6 millioner forespørgsler.[^1]

Det interessante er ikke størrelsen alene, men hvor let den kunne være undgået. Steinberger pegede selv på én indstilling, «Fast Mode», som stod for størstedelen af forbruget. Havde den været slået fra, ville regningen ifølge ham selv være faldet med omkring 70 %. OpenAI endte med at dække beløbet — men det er ikke en bremse, det er held.

### 6.531,30 dollar for at scanne et netværk

Den anden historie har en dato, man kan slå op: den 12. juni 2026. En operatør gav en autonom agent fuld adgang til sin konto hos Amazon Web Services (AWS, en cloud-udbyder) og bad den om at scanne netværket DN42.[^2]

Agenten besluttede på egen hånd, at opgaven krævede fem store cloud-instanser (virtuelle servere, man lejer efter forbrug). Hver gang den stødte på en fejl, genanvendte den sin egen skabelon — og dublerede dermed ressourcerne gang på gang. Regningen landede på **6.531,30 USD**.

AWS forhandlede beløbet ned til 1.894 USD. Men fællesskabets vurdering var, at den samme opgave kunne være løst på en VPS (Virtual Private Server, en enkelt lejet server) til 5 USD om måneden. Forskellen mellem 5 dollar og 6.531 dollar er ikke agentens intelligens — det er fraværet af et stop.

### Hvad de to regninger har til fælles

Det er fristende at læse historierne som en advarsel mod agenter i sig selv. Men det er ikke pointen. I begge tilfælde fungerede agenten præcis som bedt om — den kørte videre, fordi ingen havde fortalt den, hvornår den skulle stoppe.

Forskellen mellem en nyttig agent og en løbsk regning er sjældent teknisk snilde. Den ligger i to enkle greb: et **loft** (en øvre grænse for forbrug eller antal kald) og et **menneske i løkken** (et punkt, hvor et menneske skal godkende, før agenten går videre). Branchen er selv begyndt at behandle udgiftsstyring som et grundkrav, ikke en luksus.[^3]

Det er præcis de to greb, Værkstedets artikler viser, hvordan man sætter op — inden regningen når frem. En agent uden bremse er ikke farlig, fordi den er klog. Den er dyr, fordi den er lydig.

[^1]: [Tom's Hardware: «OpenClaw creator burns through \$1.3 million in OpenAI API tokens in a single month»](https://www.tomshardware.com/tech-industry/artificial-intelligence/openclaw-creator-burns-through-1-3-million-in-openai-api-tokens-in-a-single-month).

[^2]: [Lantian: «AI agent bankrupted their operator by scanning DN42»](https://lantian.pub/en/article/fun/ai-agent-bankrupted-their-operator-scan-dn42lantian.lantian/).

[^3]: [InfoQ: «AI Agents with Cloud Credentials Are Outrunning Billing Guardrails Built for Human-Speed Mistakes»](https://www.infoq.com/news/2026/07/ai-agents-billing-guardrails/), juli 2026.
