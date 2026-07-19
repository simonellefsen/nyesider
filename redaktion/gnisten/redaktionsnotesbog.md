# GNISTEN – Redaktionsnotesbog

Redaktionel backlog og noter — nr. 1 (juli 2026, "Sig hej til Claude"). Opdateres løbende af chefredaktionen. Modelerfaringer ligger i det fælles [modelkartotek](../modelkartotek.md).

## Løfter givet i nr. 1

- **Bagsiden lovede:** ChatGPT, MCP'er og "de første skridt ud af browseren" til nr. 2 (se `backCoverPromise` i issue.json).
- **Ordbogen nævnte MCP** kun kort med et løfte om uddybning i et senere nummer.
- **Læsere opfordret til at indsende deres egne varianter** af "Månedens prompt" — hold øje med eventuelle svar til nr. 2.

## Historier i støbeskeen til nr. 2

- **Fokus: ChatGPT** — samme skabelon som nr. 1's Claude-portræt, men om OpenAI/ChatGPT. Overvej at lade en OpenAI-model (fx GPT-5.6) skrive den, i tråd med nr. 1's selvironiske "Claude anmelder Claude"-greb.
- **Værkstedet: MCP'er forklaret for begyndere** — hvad er en MCP-server helt konkret, og hvordan "tilslutter" man én uden at være udvikler? Byg videre på Ordbogens korte MCP-glose.
- **Deployment/publicering for begyndere** — hvordan får en nybegynder sit Claude Code-projekt "ud i verden" (gratis hosting-muligheder)? Oplagt praktisk opfølgning på nr. 1's "Mit første projekt".
- **Fokus på Gemini eller Grok** som alternativ til Fokus-sektionens Claude-fokus, hvis nr. 2 skifter hovedmodel.
- **Læserindsendte prompts** — hvis nogen sender variationer af "Dagens Gnist", saml de bedste til en mini-side.

## Faste formater at genbruge

- **Kortet** (AI-landskabet/overblik) · **Fokus** (månedens model) · **Værkstedet** (praktisk opsætning) · **Månedens prompt** (copy/paste, altid selv-testet af redaktionen før tryk) · **Regningen** (priser, cirka-tal med forbehold) · **Ordbogen** (10 gloser) · **Sladder fra serverrummet** (satire, kun firmaer/modeller som mål, aldrig navngivne rigtige mennesker).
- **Regningen, Ordbogen og Sladder** er markeret `flow: true` i frontmatter, så de kan dele sider i PDF'en som et samlet bagsnit — brug samme greb for tilsvarende korte, letvægts-sektioner i kommende numre.

## Praktisk (til næste produktion)

- **Sidetal-budget:** nr. 1 landede på 16 sider efter en tæt redigeringsrunde — startudkastet var 27 sider ved fuld længde. For at holde 10-15 sider fremover: skriv briefs med lavere målængde fra start (600-750 ord for føljetonartikler, ikke 1000+), og brug `flow: true` aktivt på korte bagsnit-artikler.
- **Billeder:** cover + 3 artikelbilleder er nok til at give bladet visuelt liv uden at blive tungt. Heltebilleder sat til maks. 4,6 cm højde i PDF'en for at spare plads.
- **Diagrammer:** håndtegnede SVG'er (ikke AI-genereret) fungerer godt til pædagogiske figurer (se "Sådan virker en sprogmodel"s tre figurer) — hurtigere at style konsistent med magasinets palet end at prompte frem.
- Se [modelkartotek](../modelkartotek.md) for OpenRouter-specifik produktionspraksis (reasoning-parameter, fallback-modeller).
