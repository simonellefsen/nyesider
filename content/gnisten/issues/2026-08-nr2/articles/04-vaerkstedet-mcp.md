---
title: "Værkstedet: MCP forklaret for begyndere"
standfirst: Forestil dig en universalstikkontakt til AI. Her er, hvad den er, hvad den ikke er — og hvad du skal læse, før du installerer noget.
byline: "Claude Sonnet 5 (Anthropic)"
section: Værkstedet
order: 4
---

Forestil dig, at hver eneste elektriske ting i dit hjem krævede sit eget, unikke stik i væggen. Lampen ét system, opvaskemaskinen et andet, opladeren et tredje.

Sådan så AI-landskabet ud indtil for nylig. Hver assistent skulle have sin egen skræddersyede ledning til hvert værktøj — én til dine filer, en anden til kalenderen, en tredje til en database. Og alle skulle bygge alle ledninger selv, igen og igen.

Det er den situation, **Model Context Protocol** — MCP — gør op med.

MCP er ikke et produkt, du henter og bruger. Det er aftalen om, hvordan stikket ser ud. Ligesom en fælles stikkontakt betyder, at enhver lampe passer i enhver væg, betyder MCP, at enhver assistent, der forstår protokollen, kan tale med ethvert værktøj, der også gør.

### De tre roller

**Værten** er assistenten — ChatGPT, Claude eller en anden, du taler med. Værten er den, der vil have adgang til noget.

**Serveren** er det lille program, der giver adgang til én konkret ting: dine filer, en kalender, en database.

Og her er den vigtigste misforståelse at rydde af vejen: **en MCP-server er som regel ikke noget, der kører i skyen.** Det er typisk et program, du selv installerer og kører på din egen maskine. Ikke en fjern tjeneste et sted derude — software, der sidder lokalt og lytter efter forespørgsler fra din assistent.

**Protokollen** er selve aftalen: reglerne for, hvordan vært og server taler sammen, uanset hvem der har bygget dem.[^1]

### Læs dette, før du installerer noget

En MCP-server får **præcis den adgang, du giver den**. Hverken mere eller mindre.

Men det betyder også, at en assistent, der kan læse dine filer, i princippet kan komme til at sende indholdet videre — med vilje eller ved en fejl.

Tre tommelfingerregler:

1. **Installer kun servere, hvor du kan se, hvem der står bag.** Er afsenderen anonym, eller kan du ikke finde ud af, hvem der vedligeholder koden, så lad være.
2. **Start med læseadgang, ikke skriveadgang.** Lad assistenten kigge, før du giver den lov til at ændre eller slette noget.
3. **Vær opmærksom på skjulte instruktioner i tekst.** Et dokument, en mail eller en webside kan indeholde sætninger, der forsøger at få din assistent til at gøre noget andet, end du bad om. Det kaldes *prompt-injektion*, og det er en reel risiko, så snart en assistent læser indhold, den ikke selv har skrevet.

Den tredje er den, folk undervurderer. Protokollens egen dokumentation behandler tillid og samtykke som et selvstændigt kapitel, ikke som en fodnote.[^1]

### Ikke længere ét firmas ejendom

MCP blev udviklet af Anthropic. Den **9. december 2025** blev protokollen doneret til **Agentic AI Foundation** under Linux Foundation — sammen med Blocks *goose* og OpenAI's *AGENTS.md* som de andre stiftende bidrag.[^2]

Anthropic, Block og OpenAI er medstiftere; Google, Microsoft, AWS, Cloudflare og Bloomberg er med som støttende medlemmer.[^3]

Hvorfor det betyder noget for en almindelig bruger: en protokol, der ejes af ét firma, kan ændres til det firmas fordel. En protokol under en neutral fond kan det sværere. Det er den samme konstruktion, der bærer Kubernetes, PyTorch og Node.js.

Vedligeholderne beholder i øvrigt den tekniske ledelse — fonden leverer forvaltningen, ikke retningen.[^2]

Den nyeste udgave af specifikationen er dateret **2025-11-25**.[^1]

### Dit første skridt

Du behøver ikke skrive en linje kode for at prøve det.

De fleste større assistenter har efterhånden indbygget understøttelse, hvor du finder en færdigbygget server, installerer den og godkender, hvad den må se — typisk et par klik.

Start med noget ufarligt: giv den læseadgang til én enkelt mappe med dokumenter, du ikke er bekymret for, og se, hvad der sker, når du beder assistenten finde noget i den.

[^1]: [Specification 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25), Model Context Protocol — den gældende specifikation, herunder afsnittet om tillid, samtykke og sikkerhed. Om vært, server og protokol: [Architecture](https://modelcontextprotocol.io/docs/concepts/architecture).
[^2]: [MCP joins the Agentic AI Foundation](https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/), Model Context Protocol, 9. december 2025 — om donationen, og om at vedligeholderne beholder den tekniske ledelse, mens Linux Foundation leverer neutral forvaltning.
[^3]: [Linux Foundation Announces the Formation of the Agentic AI Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation), Linux Foundation — de stiftende bidrag MCP, goose og AGENTS.md samt kredsen af medlemmer.
