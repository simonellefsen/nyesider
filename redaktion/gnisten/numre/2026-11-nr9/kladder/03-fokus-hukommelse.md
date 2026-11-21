# Din AI har tre slags hukommelse — og ingen sletteknap tager dem alle

Når kunstig intelligens (AI) husker noget om dig, er det fristende at forestille sig én skuffe med én stor sletteknap. Så enkelt er det ikke. Hukommelse betyder her oplysninger, som tjenesten kan genbruge på tværs af samtaler. De kan ligge i **tre lag**: det, du kan åbne, samtalehistorikken og agentens egne noter.

For hvert lag bør du stille **fire spørgsmål**: Hvad husker den? Kan jeg se det? Sletter sletning af chatten det? Hvordan tømmer jeg det?

## Lag 1: Det, du kan åbne

I ChatGPT finder du Memory under **Settings → Personalization → Memory**. Oversigten er kun et overblik, ikke nødvendigvis alt. Funktionen **Delete and turn off memory** sletter det, oversigten viser, og slår Memory fra, men sletter ikke tidligere chats. Vælger du **Don’t mention this again**, stopper fremtidige henvisninger; kilden bliver ikke slettet.[^1]

Saved memories ligger adskilt fra samtalerne. Derfor sletter det ikke automatisk en saved memory at slette den oprindelige chat. Omvendt fjerner sletning af en memory ikke omtaler i gamle samtaler. Vil du fjerne en oplysning grundigt, skal du både slette memoryen og chatten, hvor du gav oplysningen. Tjek også memory summary, saved memories, almindelige og arkiverede chats samt relevante filer i Library eller Space. Kom oplysningen fra en forbundet app — en **connector**, altså en forbindelse til eksempelvis en mail- eller filtjeneste — skal forbindelsen også afbrydes. OpenAI kan beholde logs over slettede saved memories i op til **30 dage**. Kontrollerne varierer efter abonnement, land og platform.[^1]

Claude organiserer sin synlige hukommelse som emner, der opdateres løbende. På Free, Pro, Max og Ultra er hukommelse slået til som udgangspunkt. Emnerne findes under **Settings → Your Claude → Manage** ved Your memory; ældre udgaver kan vise **Settings → Memory**. Retter du ét emne, gælder rettelsen fremover. Men sletning af samtalen fjerner ikke de memory-poster, den har skabt.[^2]

## Lag 2: Samtalehistorikken

Dette lag bruger tidligere chats uden nødvendigvis at gøre dem til en synlig note.

I ChatGPT kan **Reference chat history** slås fra. Oplysninger hentet fra tidligere chats er da planlagt slettet inden **30 dage**, men selve chattene bliver liggende, indtil du sletter dem. Saved memories slettes heller ikke. Slår du Reference saved memories fra, slås Reference chat history samtidig fra.[^1]

Claude har en separat kontakt til **Search and reference chats** på betalte planer. Den kan slås fra under **Settings → Your Claude**. En incognito-chat — en midlertidig chat, der ikke gemmes i historik eller hukommelse — åbnes med spøgelsesikonet.[^3] Slår du blot Memory fra i en chats plusmenu, bliver samtalen stadig i historikken og kan findes fra andre chats.

Gemini har to beslægtede ordninger. **Memory summary** kræver blandt andet personlig konto, en bruger på mindst 18 år samt History og Memory slået til. Funktionen er ikke tilgængelig i Det Europæiske Økonomiske Samarbejdsområde (**EØS**), som Danmark er en del af.[^4] En anden funktion, hukommelse fra tidligere chats, kræver Keep Activity og bruges ikke i Gems eller Live-chats. For at fjerne en oplysning skal alle chats med den slettes i Gemini Apps Activity. Det kan tage et øjeblik, før Gemini holder op med at bruge dem. Kom oplysningerne fra en forbundet app, skal både chattene slettes og appen afbrydes.[^5]

## Lag 3: Agentens egne noter

Agenter kan føre deres egne noter ved siden af kontoens almindelige hukommelse.

Grok Bot har ingen hukommelsesskærm. Du kan spørge, hvad den husker, rette ved at give den den nye version eller bede den glemme noget. Hver Bot har sin egen hukommelse, mens navn og tidszone deles. Et **reset af samtalen beholder hukommelsen**; sletning af selve botten sletter dens hukommelse.[^6]

En ChatGPT-dot bruger samtalen, relevant ChatGPT-hukommelse og egne noter. Noterne er ikke en afskrift og ligger adskilt fra saved memory. Du kan **ikke se, rette eller slette enkelte dot-minder**. At slå ChatGPT Memory fra stopper ny deling, men sletter ikke det, dotten allerede har fået. Sletning af dotten starter sletning af dens egen kontekst, mens dens filer, Codex-tråde og oprettede ChatGPT-samtaler ligger for sig.[^7] Det ligner pointen fra [nr. 8 om filer](/gnisten/2026-11-nr8/fokus-filer): Disconnect tømmer ikke det allerede læste. En pause er heller ikke en sletning — samme skel som [stopknappen i nr. 7](/gnisten/2026-10-nr7/vaerkstedet-nej).

Der er altså ingen vinder og ingen universel knap. Brug de fire spørgsmål på hvert lag — og kontrollér alle tre, før du regner noget for glemt.

[^1]: [OpenAI: “Memory FAQ”](https://help.openai.com/en/articles/8590148-memory-in-chatgpt)
[^2]: [Anthropic: “Use Claude’s chat search and memory to build on previous context”](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)
[^3]: [Anthropic: “Use incognito chats”](https://support.claude.com/en/articles/12260368-use-incognito-chats)
[^4]: [Google: “Manage your Gemini Apps memory summary”](https://support.google.com/gemini/answer/18617127)
[^5]: [Google: “Manage Gemini’s memory from past chats”](https://support.google.com/gemini/answer/16598469)
[^6]: [xAI: “Grok Bot”](https://docs.x.ai/grok-bot/bots)
[^7]: [OpenAI: “Dots privacy, security, and safety FAQs”](https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs)