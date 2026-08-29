# Kortet

## Claude Code kræver nu et menneske i løkken

Fra juli 2026 vendte Anthropic standardopførslen i sit kodningsværktøj Claude Code på hovedet. Med version 2.1.200 kræver følsomme handlinger — filskrivning, kørsel af bash-kommandoer (et kommandolinje-sprog til styresystemer) — som udgangspunkt et menneskeligt godkend-klik. Tidligere skulle brugeren aktivt slå kontrollen fra; nu skal man aktivt vælge fuld autonomi ("auto"-tilstand) fra.

Ændringen er ikke tilfældig. Anthropic henviser eksplicit til OWASP's (Open Worldwide Application Security Project) anbefaling om "human-in-the-loop" — menneske-i-løkken — for konsekvente agent-handlinger, altså handlinger en AI-agent udfører på egen hånd med reelle følger.[^1] Pointen for den nysgerrige hobby-bruger: hvis dit AI-værktøj pludselig beder om et "ja tak" før det sletter en fil eller kører en kommando, er det ikke en fejl — det er en sikkerhedsdesignbeslutning, der er blevet standard i branchen.

## NSA: protokollen sikrer ikke sig selv

I maj 2026 udgav USA's sikkerheds- og efterretningsmyndighed NSA (National Security Agency) en formel sikkerhedsvejledning om MCP (Model Context Protocol) — den protokol, der lader AI-assistenter tilgå eksterne værktøjer og data, for eksempel din kalender eller et firmas database.[^2] Kernebudskabet er ubehageligt enkelt: MCP håndhæver ikke sikkerhed i sig selv. Det gør implementeringen — altså hvordan den enkelte udvikler eller virksomhed sætter det op.

Det betyder i praksis, at en MCP-forbindelse kan være lige så sikker eller usikker, som den, der byggede den, har gjort den. For den, der bare vil "koble sin AI til sine ting", er det en vigtig påmindelse: bekvemmelighed og sikkerhed følges ikke automatisk ad.

## 80\u00a0% af cloud-miljøer har allerede MCP

Hvor hurtigt er det gået? Ifølge sikkerhedsfirmaet Wiz kørte MCP-servere i mindst 80\u00a0% af de cloud-miljøer, firmaet observerede primo 2026.[^3] Endnu mere påfaldende: 5\u00a0% af de servere var vendt direkte ud mod internettet — tilgængelige udefra, uden det ekstra lag af beskyttelse et internt netværk giver.

Tallene tegner et billede af en teknologi, der er blevet allestedsnærværende hurtigere, end sikkerhedspraksis har kunnet følge med til. Det er præcis den kombination — udbredelse før modning — som både NSA's vejledning og Anthropics nye standardindstilling forsøger at svare på. For dig, der eksperimenterer derhjemme, er den praktiske lære enkel: spørg altid, om et MCP-værktøj eller en AI-agent er sat sikkert op, før du kobler det til noget, du ikke har lyst til at miste.

[^1]: OWASP GenAI Security Project, "OWASP Top 10 for Large Language Model Applications", genai.owasp.org
[^2]: National Security Agency, Cybersecurity Information Sheet om Model Context Protocol (MCP), nsa.gov
[^3]: Wiz Research, blogindlæg om udbredelsen af MCP-servere i cloud-miljøer, wiz.io/blog
[^4]: Anthropic, "Claude Code — Release Notes / Changelog", docs.claude.com