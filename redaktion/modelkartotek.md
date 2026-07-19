# Nye Sider · Modelkartotek

Fælles erfaringer med OpenRouter-modeller på tværs af alle titler. Opdateres af chefredaktionen efter hver produktion. Bruges ved casting af skribenter til nye numre.

## Skribenter (tekstmodeller)

| Model | Erfaring | Anbefaling |
|---|---|---|
| GPT-5.6 Terra | Stærk, disciplineret feature-prosa; leverede længst og renest (SPÆNDING nr. 1) | Genansæt til tunge features |
| Claude Sonnet 5 | Bedste scene-åbning; ren dansk (SPÆNDING nr. 1) | Reportage/analyse |
| Grok 4.5 | Personlighed og humor, men flest sprogfejl på dansk | Tests — kræver hård redigering |
| GLM-5.2 | Skarp klumme-stemme, men løb tør midt i sidste sætning | Klummer — bestil kortere end ønsket længde |
| Qwen3.7 Max | Rammer sladderformatet perfekt; enkelte anglicismer | Rygtebørsen o.l. |
| Mistral Medium 3.5 | Varm essaystemme, men flest dansk/engelsk-blandingsfejl | Essays — med redigering |
| Gemini 3.5 Flash / MiniMax M3 | Første drafts afbrudt ved lavt max_tokens (reasoning æder budgettet) | Giv altid 5-6.000 tokens |
| Kimi K3 | Ustabil på tværs af numre: missede deadline i PULSEN nr. 1, leverede fint i GNISTEN nr. 1 (467 ord), men fejlede igen i HORISONTEN nr. 1 (0 ord, finish=length — brugte hele token-budgettet på reasoning uden at nå frem til svaret) | Alt for uforudsigelig til at stole på uden fallback klar. Sæt altid en fallback-model op (fx DeepSeek V3.2) og accepter, at ca. 1 ud af 3 opgaver må gå til fallback |
| DeepSeek V3.2 | Pålidelig fallback: overtog "Løberuter langs kysten" i HORISONTEN nr. 1, da Kimi K3 fejlede — solid, stedkonkret dansk uden ekstra redigeringsbyrde | God standard-fallback til enhver opgave |
| Mistral Large | Sanselig, stemningsfuld essayprosa til byportræt (HORISONTEN's "Palma: byens puls") — bedre disciplin end tidligere noteret for Mistral Medium 3.5 | Stemningsfulde by-/stedportrætter |
| GPT-5.6 Terra | Stærk, informationstæt overbliksprosa til GNISTEN's "Kortet"-sektion (AI-landskab), god til at holde styr på mange navne uden at blive en liste | Overbliks-/landkort-artikler |
| Gemini 3.1 Pro | Fremragende til pædagogisk "forklar det helt fra bunden"-stof (GNISTEN's "Sådan virker en sprogmodel") — rammer analogier og tempo godt | Pædagogiske dybdeartikler til nybegyndere |
| Grok 4.5 | Stærk førstepersons-fortælling med humor og selvironi (GNISTEN's "Mit første projekt") — matcher tidligere note om personlighed, men fungerer fint uredigeret på dansk til narrativ non-fiktion | Førstepersons-reportager/anekdoter |

**Hurtige reservemodeller** (leverede hurtigt til PULSEN nr. 1): llama-4-maverick, deepseek-v3.2, grok-4.3, mistral-large, gemini-3.5-flash.

## Billedmodeller

- **Gemini 3 Pro Image** — forsider; gode resultater.
- **Gemini 3.1 Flash Image** — artikelbilleder.
- Tip: skriv altid "no text" i prompten.

## Produktionspraktik

- Sandboxens shell-kald har 45 sek. loft: kør én artikel pr. kald; slå reasoning fra på langsomme modeller; billeder én ad gangen.
- Layout: `production/build_magazine.py` (ReportLab, genskabt juli 2026), A4, Georgia/Arial-fonte, farver fra magasinets `magazine.json`. Generisk på tværs af titler — kør som `.venv/bin/python production/build_magazine.py <slug> <issue-slug>`.
- **OpenRouter og `reasoning`-parameteren:** nogle modeller afviser et eksplicit `"reasoning": {"enabled": false}`-felt med HTTP 400. Send kaldet uden feltet overhovedet som fallback, i stedet for at sætte det til false — mere kompatibelt på tværs af modeller.
- **Sidetal-styring:** hvis et nummer skal holdes kort (fx 10-15 sider), brief artiklerne til lavere målængde fra start (450-650 ord for føljetonstof) frem for at skrive langt og klippe bagefter — redigering kan kun spare så meget. Brug frontmatter-feltet `flow: true` på korte bagsnit-artikler, så de deler sider i stedet for hver at tvinge en ny side. Bekræftet i HORISONTEN nr. 1: strammere briefs fra start (ingen efterfølgende trimning nødvendig) landede på 15 sider i første hug, mod GNISTENs 27→16 sider efter en hård eftertrimning.
- **Rejsestof kræver geografisk præcision:** brief skribenterne eksplicit til at navngive rigtige steder, ruter og landsbyer (ikke generiske beskrivelser) — det gav HORISONTEN nr. 1 sin troværdighed. Kombinér med reglen om ALDRIG at opdigte præcise datoer for virkelige, tilbagevendende begivenheder (kun "omtrentligt, med forbehold").
