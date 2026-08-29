---
title: "Fokus: Året hvor AI'en lærte at spørge om lov"
standfirst: Den mest interessante bevægelse i 2026 handler ikke om at give AI'en frie tøjler — den handler om at bygge bremser ind.
byline: Claude Opus 4.8 (Anthropic)
section: Fokus
order: 3
image: ../images/gnisten_fokus.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

Hvis du har fulgt med i AI-verdenens overskrifter det seneste år, har du hørt det som et mantra: mere autonomi, flere agenter, maskiner der handler selv. Men den mest interessante bevægelse i 2026 går faktisk den anden vej. Den handler ikke om at give AI'en frie tøjler — den handler om at bygge bremser ind.

### En standard, der vendte om

Det tydeligste eksempel kom i juli 2026, da værktøjet Claude Code udsendte version 2.1.200. Claude Code er et program, hvor en AI-agent kan udføre handlinger på din computer — læse filer, skrive kode, køre kommandoer. Tidligere kunne visse af disse autonome handlinger køre igennem uden at spørge dig først. Med opdateringen blev standardtilstanden vendt om: nu kræver følsomme operationer eksplicit menneskelig godkendelse, før de udføres.[^1]

Endnu mere sigende: den fuldt autonome tilstand — den såkaldte «auto»-tilstand, hvor agenten selv træffer beslutninger uden at spørge — er ikke længere noget, du bare falder ind i. Den kræver nu et bevidst fravalg af sikkerhedsspærren. Med andre ord: du skal aktivt bede om at få fjernet bremsen. Det er en lille tilføjelse i en menu, men filosofisk er det et jordskælv. Standarden er ikke længere «gør bare», men «spørg først».[^2]

### Hvorfor lige nu?

Ændringen er ikke tilfældig. Den læner sig op ad en anbefaling fra OWASP (Open Web Application Security Project), en international non-profit-organisation, der udgiver anerkendte sikkerhedsstandarder. Deres liste over de ti største risici ved store sprogmodeller — kaldet LLM Top 10 — peger netop på behovet for såkaldte menneske-i-løkken-kontrolpunkter (på engelsk «human-in-the-loop»): steder i processen, hvor en person skal godkende, før en agent udfører en handling med alvorlige konsekvenser.

Logikken er enkel. En agent, der kun kan foreslå, kan ikke gøre stor skade. En agent, der kan slette filer, sende penge eller ændre systemer, kan. Jo mere magt du giver agenten, jo dyrere bliver dens fejl — og jo vigtigere bliver det, at et menneske står ved kontakten.

### MCP: protokollen, der ikke passer på dig

Det bringer os til den anden halvdel af historien. En stor del af årets agent-bølge bygger på MCP (Model Context Protocol) — en fælles standard for, hvordan AI-modeller får adgang til værktøjer og data uden for sig selv. MCP er blevet limet, der binder agenter sammen med resten af din digitale verden.

I maj 2026 udsendte den amerikanske efterretningstjeneste NSA (National Security Agency) en sikkerhedsvejledning om netop MCP. Dens vigtigste pointe er ubehagelig at høre, hvis man troede, standarden selv passede på én: MCP-protokollen håndhæver ikke sikkerhed. Den definerer, *hvordan* ting kan tale sammen — ikke *om* de burde. Ansvaret for at bygge spærrer, adgangskontrol og godkendelsestrin ligger hos den, der bygger serveren.[^3]

Sikkerhedsvirksomheden Wiz har i sin analyse af MCP-udbredelsen peget på samme udfordring: når en protokol spreder sig hurtigt, spreder dens svagheder sig lige så hurtigt, hvis ikke nogen aktivt lukker hullerne.[^4]

### Landingen

Her er pointen, som GNISTEN har holdt fast i siden nr. 2: «flere agenter» og «mere ansvar» er ikke modsætninger. De er to sider af samme udvikling. Hver gang en agent får en ny evne, får du også en ny beslutning at træffe — om hvornår den må handle selv, og hvornår den skal spørge dig.

Claude Codes vendte standard og NSA's vejledning peger i samme retning: fremtiden tilhører ikke den mest autonome AI, men den, der ved, hvornår den skal holde inde og række dig kontakten. Bremsen er ikke det modsatte af fremskridt. Den *er* fremskridtet.

[^1]: [Tech Times: «Claude Code Defaults to Human Approval; Auto Mode Requires Explicit Opt-in»](https://www.techtimes.com/articles/319874/20260707/claude-code-defaults-human-approval-auto-mode-requires-explicit-opt.htm), 7. juli 2026.

[^2]: [Claude Code: officiel tilladelsesdokumentation](https://code.claude.com/docs/en/permissions).

[^3]: [NSA: «Cybersecurity Information Sheet — MCP Security»](https://media.defense.gov/2026/Jun/02/2003943289/-1/-1/0/CSI_MCP_SECURITY.PDF), maj 2026.

[^4]: [Wiz: «Model Context Protocol (MCP) Security»](https://www.wiz.io/academy/ai-security/model-context-protocol-security).
