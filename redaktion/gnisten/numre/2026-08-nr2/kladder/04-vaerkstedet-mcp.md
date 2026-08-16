# Stikkontakten, der samler AI-verdenen

Forestil dig, at hver eneste elektriske ting i dit hjem krævede sit eget, unikke stik i væggen. Din lampe ét system, din opvaskemaskine et andet, din telefonoplader et tredje. Sådan så det digitale AI-landskab faktisk ud indtil for nylig: Hver AI-assistent skulle have sin egen skræddersyede "ledning" til hvert eneste værktøj — én forbindelse til dine filer, en anden til din kalender, en tredje til en database. Og alle skulle bygge alle ledninger selv, igen og igen.

Det er den situation, **Model Context Protocol** (forkortet **MCP**) gør op med. MCP er ikke et produkt, du downloader og bruger direkte — det er selve aftalen om, hvordan stikket ser ud. Ligesom en universalstikkontakt betyder, at enhver lampe passer i enhver væg, betyder MCP, at enhver AI-assistent, der forstår protokollen, kan tale med ethvert værktøj, der også forstår den.

## De tre roller

For at forstå MCP skal du kende tre begreber:

**Værten** er selve assistenten — det kan være ChatGPT, Claude eller en anden AI-chatbot, du taler med. Værten er den, der ønsker adgang til noget: dine dokumenter, din mail, en database.

**Serveren** er det lille program, der giver adgang til en konkret ting. En MCP-server kan give adgang til dine filer på computeren, til en kalender, eller til en virksomheds interne database. Vigtigt: **en MCP-server er som regel ikke noget, der kører i skyen** — det er typisk et lille program, du selv installerer og kører på din egen maskine. Det er ikke en fjern tjeneste et sted derude; det er software, der sidder lokalt og lytter efter forespørgsler fra din assistent.

**Protokollen** er selve aftalen — reglerne for, hvordan vært og server taler sammen, uanset hvem der har bygget dem.

## Sikkerhed — læs dette, før du installerer noget

En MCP-server får **præcis den adgang, du giver den** — hverken mere eller mindre. Men det betyder også, at en assistent, der kan læse dine filer, i princippet kan komme til at sende indholdet af dem videre et sted hen, hvis den bliver instrueret til det — med vilje eller ved en fejl.

Tre tommelfingerregler, før du går videre:

1. **Installer kun servere, du kan se hvem der står bag.** Er afsenderen anonym, eller kan du ikke finde ud af, hvem der vedligeholder koden, så lad være.
2. **Start med læseadgang, ikke skriveadgang.** Lad assistenten kigge, før du giver den lov til at ændre eller slette noget.
3. **Vær opmærksom på skjulte instruktioner i tekst.** Et dokument, en mail eller en webside kan indeholde sætninger, der forsøger at få din assistent til at gøre noget andet, end du bad om — det kaldes ofte "prompt-injektion". Det er ikke science fiction; det er en reel risiko, når en assistent læser indhold, den ikke selv har skrevet.

## Ikke længere ét firmas ejendom

MCP blev oprindeligt udviklet af Anthropic, men den 9. december 2025 blev protokollen doneret til **Agentic AI Foundation** under **Linux Foundation** — den non-profit-organisation, der også huster projekter som Linux-kernen selv.[^1] Det betyder, at MCP nu forvaltes åbent, på tværs af virksomheder, i stedet for at være styret af én enkelt aktør. Den nyeste udgave af selve specifikationen er dateret **2025-11-25** og beskriver i detaljer, hvordan vært, server og protokol skal spille sammen.[^2]

## Dit første skridt

Du behøver ikke skrive en eneste linje kode for at prøve MCP. De fleste populære assistenter (blandt andet Claude Desktop) har efterhånden indbygget understøttelse, hvor du blot skal finde en færdigbygget MCP-server i en officiel oversigt, downloade den, og følge en kort installationsvejledning — typisk et par klik og en godkendelse af, hvilken mappe eller kalender assistenten må se. Start med noget ufarligt: giv den læseadgang til én enkelt mappe med dokumenter, du ikke er bekymret for at dele, og se, hvad der sker, når du beder assistenten finde noget i den.

[^1]: Linux Foundation, pressemeddelelser og nyheder om Agentic AI Foundation: linuxfoundation.org
[^2]: Model Context Protocol — officiel specifikation og dokumentation: modelcontextprotocol.io