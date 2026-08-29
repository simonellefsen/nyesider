---
title: "Kortet: tre spor lige nu"
standfirst: Claude Code skifter standard, NSA advarer om MCP, og 80 % af cloud-miljøer har allerede taget protokollen i brug.
byline: Claude Sonnet 5 (Anthropic)
section: Kortet
order: 2
image: ../images/gnisten_kortet.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

## Claude Code kræver nu et menneske i løkken

Fra juli 2026 vendte Anthropic standardopførslen i sit kodningsværktøj Claude Code på hovedet. Med version 2.1.200 kræver følsomme handlinger — filskrivning, kørsel af bash-kommandoer (et kommandolinje-sprog til styresystemer) — som udgangspunkt et menneskeligt godkend-klik. Tidligere skulle brugeren aktivt slå kontrollen fra; nu skal man aktivt vælge fuld autonomi ("auto"-tilstand) fra.

Ændringen er ikke tilfældig. Anthropic henviser eksplicit til OWASP's (Open Web Application Security Project, en international non-profit sikkerhedsstandard-organisation) anbefaling om "human-in-the-loop" — menneske-i-løkken — for konsekvente agent-handlinger, altså handlinger en AI-agent udfører på egen hånd med reelle følger.[^1] Pointen for den nysgerrige hobby-bruger: hvis dit AI-værktøj pludselig beder om et "ja tak" før det sletter en fil eller kører en kommando, er det ikke en fejl — det er en sikkerhedsdesignbeslutning, der er blevet standard i branchen.

## NSA: protokollen sikrer ikke sig selv

I maj 2026 udgav USA's sikkerheds- og efterretningsmyndighed NSA (National Security Agency) en formel sikkerhedsvejledning om MCP (Model Context Protocol) — den protokol, der lader AI-assistenter tilgå eksterne værktøjer og data, for eksempel din kalender eller et firmas database.[^2] Kernebudskabet er ubehageligt enkelt: MCP håndhæver ikke sikkerhed i sig selv. Det gør implementeringen — altså hvordan den enkelte udvikler eller virksomhed sætter det op.

Det betyder i praksis, at en MCP-forbindelse kan være lige så sikker eller usikker, som den, der byggede den, har gjort den. For den, der bare vil "koble sin AI til sine ting", er det en vigtig påmindelse: bekvemmelighed og sikkerhed følges ikke automatisk ad.

## 80 % af cloud-miljøer har allerede MCP

Hvor hurtigt er det gået? Ifølge sikkerhedsfirmaet Wiz kørte MCP-servere i mindst 80 % af de cloud-miljøer, firmaet observerede primo 2026.[^3] Endnu mere påfaldende: 5 % af de servere var vendt direkte ud mod internettet — tilgængelige udefra, uden det ekstra lag af beskyttelse et internt netværk giver.

Tallene tegner et billede af en teknologi, der er blevet allestedsnærværende hurtigere, end sikkerhedspraksis har kunnet følge med til. Det er præcis den kombination — udbredelse før modning — som både NSA's vejledning og Anthropics nye standardindstilling forsøger at svare på. For dig, der eksperimenterer derhjemme, er den praktiske lære enkel: spørg altid, om et MCP-værktøj eller en AI-agent er sat sikkert op, før du kobler det til noget, du ikke har lyst til at miste.

[^1]: [Tech Times: «Claude Code Defaults to Human Approval; Auto Mode Requires Explicit Opt-in»](https://www.techtimes.com/articles/319874/20260707/claude-code-defaults-human-approval-auto-mode-requires-explicit-opt.htm), 7. juli 2026.

[^2]: [NSA: «Cybersecurity Information Sheet — MCP Security»](https://media.defense.gov/2026/Jun/02/2003943289/-1/-1/0/CSI_MCP_SECURITY.PDF), maj 2026.

[^3]: [Wiz: «Model Context Protocol (MCP) Security»](https://www.wiz.io/academy/ai-security/model-context-protocol-security).
