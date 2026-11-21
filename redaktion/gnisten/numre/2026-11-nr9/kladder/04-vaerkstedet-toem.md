# Værkstedet: Tre bremser mod en hukommelse, der husker for meget

Nr. 8 lovede en opskrift på bagsiden: sådan tømmer du hukommelsen — eller holder bare én samtale ude af den. Her er den, uden kode og uden omveje om MCP (Model Context Protocol). Tre bremser, tre handlinger.

## Bremse A: Hold samtalen ude, FØR den første besked

Det vigtigste tidspunkt er før du skriver noget som helst.

I **ChatGPT** vælger du midlertidig chat. Inden du starter, skal du vælge «Unpersonalized», hvis den ikke må trække på eksisterende minder. Valget kan ikke ændres, efter samtalen er i gang. Midlertidige chats opretter eller opdaterer ikke minder — men gemmer du chatten alligevel, bliver den en almindelig chat med det samme regelsæt som resten[^1].

I **Claude** åbner du en ny chat, klikker på plus-menuen og slår Memory fra — og sender først derefter den første besked. Det kan ikke ændres bagefter. Chatten ligger stadig i historikken, så vil du have, at den heller ikke dukker op der, skal du bruge spøgelsesikonet og starte en incognito-chat i stedet[^2][^3].

## Bremse B: Slet linjen et andet sted end chatten

Når skaden er sket, ligger oplysningen typisk to steder: i selve chatten og i en separat hukommelse. Du skal begge steder.

I **ChatGPT**: gå til Settings → Personalization → Memory. Slet i oversigten eller inde i saved memories. Slet også selve chatten, inklusive arkiverede, hvis oplysningen stammer derfra. Sletning af chatten alene sletter ikke en separat saved memory — og «Delete and turn off memory» sletter ikke selve chatten[^1].

I **Claude**: Settings → Your Claude → Manage → Topics → Delete på det enkelte emne. Pause beholder det, der allerede ligger, og stopper kun ny brug og nye minder. Reset sletter alle minder — også projektets — og **kan ikke fortrydes**. Sletter du bare chatten, forsvinder memory-posterne ikke[^2].

I **Gemini** ser Danmark anderledes ud: Memory summary findes ikke i Det Europæiske Økonomiske Samarbejdsområde (EØS), og det inkluderer en dansk konto[^4]. Opfind ikke en knap, der ikke findes her. Den vej, der faktisk virker fra Danmark, er: slet alle chats med oplysningen under Gemini Apps Activity — og husk, at Keep Activity skal stå til, for at hukommelse fra chats overhovedet fungerer[^5].

## Bremse C: Slet agenten, når der ikke er en liste

Nogle værktøjer viser dig ikke, hvad de har lært. Så er «glem det» ikke det samme som sletning.

**Grok Bot** har ingen liste. Skriv «What do you remember about me?», ret det forkerte, og skriv «Forget that …». Et reset af selve samtalen **beholder hukommelsen** — den rører den slet ikke. Vil du af med bottens hukommelse helt, skal du slette botten selv: højreklik → Delete. Det **kan ikke fortrydes**, og det sletter samtaler, rutiner og vedhæftninger med det samme[^6]. At skjule botten i sidebaren er ikke sletning.

**Dots** lader dig ikke slette ét enkelt minde. At slå ChatGPT Memory fra i Dots stopper kun ny deling fremover. Sletter du selve dotten, starter sletning af dens egen kontekst — men filer og ChatGPT-samtaler, den har lavet, bliver liggende, og andre ChatGPT-minder styres fortsat inde i ChatGPT. Pause sletter intet[^7].

**Muse** kan bedes glemme et emne — «to the best of its ability» — eller du åbner Assistant → Identity → Memory og retter direkte i Memory.md. En slettet besked kan stadig efterlade det, Muse lærte af den. Reset under Settings → Data controls sletter det hele og **kan ikke fortrydes**. Meta har lanceret Muse i USA (8. september 2026) og i Australien (17. november 2026) uden at nævne Danmark på nogen af siderne[^8].

## Den fælles test

Før du overhovedet giver en ny AI noget personligt, så spørg den, hvad den husker om dig. Svaret afslører, om bremsen virker — og om du har valgt den rigtige, inden samtalen var i gang.

Vil du have mere struktur efter oprydningen, se Værkstedet i nr. 8 om mapper. Vil du først forstå, hvornår du bør sige nej til at dele noget overhovedet, se Værkstedet i nr. 7.

[^1]: OpenAI, «Memory in ChatGPT», https://help.openai.com/en/articles/8590148-memory-in-chatgpt
[^2]: Claude Support, «Use Claude's chat search and memory to build on previous context», https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context
[^3]: Claude Support, «Use incognito chats», https://support.claude.com/en/articles/12260368-use-incognito-chats
[^4]: Google, Gemini Apps hjælp, https://support.google.com/gemini/answer/18617127
[^5]: Google, Gemini Apps hjælp, https://support.google.com/gemini/answer/16598469
[^6]: xAI, «Grok Bot», https://docs.x.ai/grok-bot/bots
[^7]: OpenAI, «Dots: Privacy, Security and Safety FAQs», https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs
[^8]: Meta, hjælpeside om kunstig intelligens, https://www.meta.com/help/artificial-intelligence/2225571704857152/