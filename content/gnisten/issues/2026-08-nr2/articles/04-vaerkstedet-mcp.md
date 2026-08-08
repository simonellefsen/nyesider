---
title: "Værkstedet: MCP forklart for begyndere"
standfirst: Forestil dig en universalstikkontakt til AI. Sådan tilslutter du værktøjer uden at bygge hver ledning selv — og uden at blive udvikler overnight.
section: Værkstedet
order: 4
---

I [nr. 1's ordbog](/gnisten/2026-07-nr1/ordbogen) lovede vi at vende tilbage til **MCP**. Her er den forklaring, der mangler i de fleste "det er en protokol"-artikler.

## Problemet MCP løser

Uden en fælles standard skal hver AI-app have sin egen måde at tale med hver tjeneste på. ChatGPT har sine connectors. Claude har sine. Din lille hjemmelavede assistent har ingen. Det er som om hver el-producent solgte stikkontakter med forskelligt hulmønster.

**Model Context Protocol** er en åben aftale om, hvordan en AI-klient (chatappen eller kode-assistenten) spørger en **MCP-server** (et lille program, der eksponerer værktøjer): *hvad kan du?* og *gør det her, tak*. Serveren kan give adgang til filer, en database, en kalender, et issue-system — eller bare en vejrtjeneste.

Du behøver ikke forstå netværksprotokoller. Du skal bare huske tre roller:

1. **Klienten** — det du snakker med (fx Claude Desktop, Cursor, ChatGPT med connectors).
2. **Serveren** — det lille stik, der kender ét domæne (filer, Notion, GitHub …).
3. **Modellen** — hjernen, der beslutter *hvornår* stikket skal bruges.

## Hvad betyder det for dig i praksis?

Hvis du bruger en moderne AI-klient med MCP-støtte, kan du ofte:

- pege assistenten på en mappe eller et dokument
- lade den hente data fra en tilkoblet tjeneste
- få den til at udføre en handling (oprette en note, tjekke en status), ikke kun skrive om den

I 2026 er MCP ikke længere et nørdet sideprojekt. OpenAI, Google, Microsoft og Anthropic har alle rørt ved det. Der findes tusindvis af offentlige servere — og ja, det betyder også, at **sikkerhed** er blevet vigtigt. Tilslut kun servere, du stoler på. Giv ikke en tilfældig MCP-server adgang til hele din harddisk, bare fordi nogen på nettet sagde, det var "sejt".

## Den begyndervenlige opskrift

1. Vælg en klient, der understøtter MCP (mange kode-editorer og desktop-assistenter gør det nu).
2. Start med **én** officiel eller velkendt server — fx filadgang til et projekt, du selv har oprettet.
3. Test med en lille opgave: "List filerne i mappen X" eller "Opsummér README'en".
4. Først bagefter: mere spændende stik (kalender, database, publicering).

## MCP vs. "bare en plugin"

En plugin eller en indbygget connector kan føles ens for dig som bruger. Forskellen er under motorhjelmen: MCP er en **fælles standard**, så det samme stik i princippet kan bruges af flere klienter. Det er derfor, det er værd at lære ordet — ikke for at imponere nogen til middagsbordet, men fordi det er den retning, "AI der kan noget" bevæger sig i.

Næste skridt i dette nummer: at få noget, du har bygget, *ud* på nettet. MCP er stikkontakten. Publicering er, når lampen tændes, så andre kan se den.
