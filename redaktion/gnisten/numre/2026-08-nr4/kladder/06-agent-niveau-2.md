# Værkstedet: Byg din første niveau-2-agent

Sidste nummer viste dig din første agent-arbejdsgang: en simpel opgave, hvor du sad med fingeren på godkend-knappen for hvert eneste skridt. Det var niveau\u00a01 — trygt, men langsomt. Nu tager vi et skridt videre.

**Niveau\u00a02 betyder præcis dette: agenten får adgang til én afgrænset mappe — ikke hele dit filsystem — og ét konkret værktøj, ikke frie hænder.** Ikke ti værktøjer, ikke adgang til alt, du har liggende. Én mappe. Ét værktøj. Det er hele pointen.

## Bremsen flytter sig, den forsvinder ikke

Det vigtigste at forstå, før du går videre: menneskelig godkendelse er stadig standarden. Claude Code (Anthropics agent-værktøj til programmering og filhåndtering) kræver som udgangspunkt, at et menneske godkender handlinger — det er ikke noget, du skal slå til, det er noget, du aktivt skal fravælge, hvis du vil have en agent, der kører uden opsyn.[^1]

Det betyder, at niveau\u00a02 ikke er "mindre kontrol". Det er samme bremse — flyttet til et sted, hvor agenten kan gøre mere *pr. godkendelse*. I stedet for at du godkender hvert lille skridt (åbn fil, læs linje, skriv forslag), godkender du nu en hel arbejdsgang inden for et afgrænset rum: én mappe, ét værktøj. Du giver agenten lidt mere plads til at bevæge sig i — men rummet er stadig lille, og du står stadig i loopet.

## Syntaksen: adgang til ét værktøj, ikke en hel server

Mange AI-værktøjer forbindes til eksterne tjenester via MCP (Model Context Protocol) — en standard for, hvordan en agent kan tale med fx en søgetjeneste eller en dokumentdatabase. Problemet er, at en MCP-server (den tjeneste, du forbinder til) tit har flere værktøjer indbygget. Vil du kun åbne for søgning og ikke for fx sletning, skal du kunne pege på det ene værktøj — ikke hele serveren.

Claude Codes officielle dokumentation beskriver netop denne mekanisme: man kan give adgang til et specifikt værktøj inde i en MCP-server ved at bruge formen `mcp__servernavn__værktøjsnavn`.[^2] Har en server for eksempel værktøjerne `søg` og `gem`, kan du i din tilladelseskonfiguration angive `mcp__dokumentserver__søg` og dermed åbne for søgefunktionen alene — mens `gem` forbliver lukket, indtil du selv trykker godkend.

Det er selve niveau\u00a02-mekanikken: du navngiver præcis det ene værktøj, agenten må bruge, i stedet for at give grønt lys til en hel værktøjskasse.

## Et konkret eksempel

Forestil dig, at du har en mappe med kundehenvendelser — säg tyve dokumenter i almindeligt tekstformat. Du vil have en agent, der:

1. Kun har adgang til denne ene mappe (ikke resten af din computer)
2. Kun må bruge søgeværktøjet i din dokument-MCP-server (`mcp__dokumentserver__søg`) — ikke skriveværktøjet
3. Må finde mønstre og foreslå ændringer eller opsummeringer
4. Aldrig selv gemmer noget — hver ændring lander som et forslag, du skal godkende

Agenten kan altså søge frit i mappen, finde de tre henvendelser, der handler om samme problem, og skrive et udkast til et svar. Men den kan ikke røre originalfilerne, og den kan ikke gå ud af mappen. Det er præcis den afgrænsning, der gør niveau\u00a02 til noget andet end "agenten må gøre, hvad den vil, bare i en mindre kasse".

## Sådan gør du det selv

Åbn din tilladelseskonfiguration i Claude Code, og:

1. Angiv den ene mappe, agenten må arbejde i.
2. Find navnet på det MCP-værktøj, du vil åbne for (fx `søg`), og skriv det som `mcp__servernavn__værktøjsnavn`.
3. Lad alt andet — herunder skrive- og slettefunktioner i samme server — stå som "kræver godkendelse".
4. Test med en lille, ufarlig opgave først. Se, om agenten holder sig inden for mappen og værktøjet, før du stoler på den med noget vigtigere.

Niveau\u00a02 er ikke et spring ud i det ukendte. Det er et lille, kontrolleret skridt — hvor du stadig bestemmer, hvad der bliver gemt, og hvad der ikke gør.

---

[^1]: Tech Times, "Claude Code Defaults Human Approval, Auto Mode Requires Explicit Opt", https://www.techtimes.com/articles/319874/20260707/claude-code-defaults-human-approval-auto-mode-requires-explicit-opt.htm
[^2]: Claude Code, officiel dokumentation om tilladelser, https://code.claude.com/docs/en/permissions