# Nye Sider · Modelkartotek

Fælles erfaringer med OpenRouter-modeller på tværs af alle titler. Bruges ved casting af skribenter til nye numre.

To slags indhold i denne fil, bevidst adskilt:

1. **Statistik** (nedenfor) — *afledt*, aldrig håndskrevet. Genereres af `production/modelstats.py` fra alle titlers `bestilling.json`-ledgere. Kan ikke gå forældet, fordi den ikke er skrevet — kør scriptet igen efter en produktion, den opdaterer sig selv.
2. **Kvalitative noter** (`## Skribenter — kvalitative noter`) — håndskrevne observationer om *stemme, stil, pålidelighed*, ting tal ikke fanger. Hver note er **dateret og citerer sit nummer**, så modstridende observationer om samme model (fx Grok 4.5 nedenfor) læses som to punkter i tid, ikke en selvmodsigelse.

## Statistik (afledt)

<!-- AUTO:modelstats:start -->
| Model | Kommissioner | Godkendt | Efter redigering | Omskrevet | Afvist | Ord i mål | Kilder opfyldt | Total omkostning (USD) |
|---|---|---|---|---|---|---|---|---|
| Claude Fable 5 | 2 | 2 | 0 | 0 | 0 | 2/2 | 2/2 | — |
| GPT-5.6 Terra (OpenAI) | 2 | 2 | 0 | 0 | 0 | 2/2 | 0/2 | — |
| DeepSeek V3.2 (DeepSeek) | 2 | 0 | 1 | 1 | 0 | 2/2 | 2/2 | — |
| Qwen3.7 Max (Alibaba) | 2 | 1 | 1 | 0 | 0 | 2/2 | 2/2 | — |
| Claude Sonnet 5 (Anthropic) | 1 | 1 | 0 | 0 | 0 | 1/1 | 0/1 | — |
| Gemini 3.1 Pro (Google) | 1 | 1 | 0 | 0 | 0 | 1/1 | 1/1 | — |
| Mistral Large (Mistral AI) | 1 | 0 | 1 | 0 | 0 | 1/1 | 1/1 | — |
| GLM-5.2 (Z.ai) | 1 | 0 | 1 | 0 | 0 | 1/1 | 1/1 | — |
| Grok 4.5 (xAI) | 1 | 1 | 0 | 0 | 0 | 1/1 | 0/1 | — |
| Gemini 3.5 Flash (Google) | 1 | 1 | 0 | 0 | 0 | 1/1 | 1/1 | — |

_Afledt af 1 `bestilling.json`-ledger(e) — kør `python production/modelstats.py` for at gendanne. Kolonner uden data (—) venter på flere kommissioner via `commission.py`._
<!-- AUTO:modelstats:end -->

## Skribenter — kvalitative noter

Hver linje er dateret og navngiver sit nummer. Modstridende noter om samme model er **ikke rettet ud** — begge stod, fordi begge var sande på deres tidspunkt; datoen er hvad der adskiller dem.

| Model | Dato / nummer | Erfaring | Anbefaling |
|---|---|---|---|
| GPT-5.6 Terra | 2026-07, SPÆNDING nr. 1 | Stærk, disciplineret feature-prosa; leverede længst og renest | Genansæt til tunge features |
| Claude Sonnet 5 | 2026-07, SPÆNDING nr. 1 | Bedste scene-åbning; ren dansk | Reportage/analyse |
| Grok 4.5 | 2026-07, tidlig note | Personlighed og humor, men flest sprogfejl på dansk | Tests — kræver hård redigering |
| GLM-5.2 | 2026-07/08 | Skarp klumme-stemme, men løb tør midt i sidste sætning | Klummer — bestil kortere end ønsket længde |
| Qwen3.7 Max | 2026-07/08 | Rammer sladderformatet perfekt; enkelte anglicismer | Rygtebørsen o.l. |
| Mistral Medium 3.5 | 2026-07 | Varm essaystemme, men flest dansk/engelsk-blandingsfejl | Essays — med redigering |
| Gemini 3.5 Flash / MiniMax M3 | 2026-07 | Første drafts afbrudt ved lavt max_tokens (reasoning æder budgettet) | Giv altid 5-6.000 tokens |
| Kimi K3 | 2026-07, PULSEN/GNISTEN/HORISONTEN nr. 1 | Ustabil på tværs af numre: missede deadline i PULSEN nr. 1, leverede fint i GNISTEN nr. 1 (467 ord), men fejlede igen i HORISONTEN nr. 1 (0 ord, finish=length — brugte hele token-budgettet på reasoning uden at nå frem til svaret) | Alt for uforudsigelig til at stole på uden fallback klar. Sæt altid en fallback-model op (fx DeepSeek V3.2) og accepter, at ca. 1 ud af 3 opgaver må gå til fallback |
| DeepSeek V3.2 | 2026-07, HORISONTEN nr. 1 | Pålidelig fallback: overtog "Løberuter langs kysten", da Kimi K3 fejlede — solid, stedkonkret dansk uden ekstra redigeringsbyrde | God standard-fallback til enhver opgave |
| Mistral Large | 2026-07, HORISONTEN nr. 1 | Sanselig, stemningsfuld essayprosa til byportræt ("Palma: byens puls") — bedre disciplin end den 2026-07-note for Mistral Medium 3.5 ovenfor | Stemningsfulde by-/stedportrætter |
| GPT-5.6 Terra | 2026-07, GNISTEN nr. 1 | Stærk, informationstæt overbliksprosa til "Kortet"-sektionen (AI-landskab), god til at holde styr på mange navne uden at blive en liste | Overbliks-/landkort-artikler |
| Gemini 3.1 Pro | 2026-07, GNISTEN nr. 1 | Fremragende til pædagogisk "forklar det helt fra bunden"-stof ("Sådan virker en sprogmodel") — rammer analogier og tempo godt | Pædagogiske dybdeartikler til nybegyndere |
| Grok 4.5 | 2026-07, GNISTEN nr. 1 | Stærk førstepersons-fortælling med humor og selvironi ("Mit første projekt") — matcher tidligere note om personlighed, men fungerer fint uredigeret på dansk til narrativ non-fiktion. **Modsiger ikke** 2026-07-noten ovenfor: samme styrke (personlighed), forskellig svaghed synlig afhængig af format (test vs. førstepersonsfortælling) | Førstepersons-reportager/anekdoter |
| DOSIS' skribentkorps | 2026-08, DOSIS nr. 1 | Se `redaktion/dosis/numre/2026-08-nr1/bestilling.json` for komplet, retro-udfyldt eksempel — første nummer med skrevne briefs + verdikter, se `redaktion/bestilling.schema.md` | Skabelon for fremtidige numres kvalitative noter: citer `bestilling.json`, ikke kun hukommelse |

**Hurtige reservemodeller** (2026-07, leverede hurtigt til PULSEN nr. 1): llama-4-maverick, deepseek-v3.2, grok-4.3, mistral-large, gemini-3.5-flash.

## Billedmodeller

**Standard fra august 2026: xAI Imagine** (Grok Build `image_gen` / Imagine) til covers og artikelbilleder — primært for at **undgå copyright** på stock/pressefotos. Krediter altid med `imageCredit` + `imageSource` (fx «AI-genereret … (Imagine / xAI)» → `https://x.ai/`).

**Nøgler:**
- Imagine: `XAI_API_KEY` i **`.env.local`** (fælles).
- OpenRouter-tekst (og evt. Gemini-billed-fallback): **kun** `.env.<slug>` for den titel der produceres — se [README](README.md) og `production/load_env.py`.

- **Imagine (xAI)** — forsider + feature-billeder. Foretrukket default; load `.env.local`.
- **Gemini 3 Pro Image** (via OpenRouter) — ældre forsider; fallback på **titlens** OpenRouter-nøgle.
- **Gemini 3.1 Flash Image** — ældre artikelbilleder via OpenRouter (samme: titlens nøgle).
- Tip: skriv altid "no text" / "no logos" / "no readable signage" i prompten.
- **Ikke:** scrapte fotos fra web uden licens.

## Produktionspraktik

- Sandboxens shell-kald har 45 sek. loft: kør én artikel pr. kald; slå reasoning fra på langsomme modeller; billeder én ad gangen.
- Layout: `production/build_magazine.py` (ReportLab, genskabt juli 2026), A4, Georgia/Arial-fonte, farver fra magasinets `magazine.json`. Generisk på tværs af titler — kør som `.venv/bin/python production/build_magazine.py <slug> <issue-slug>`.
- **OpenRouter og `reasoning`-parameteren:** nogle modeller afviser et eksplicit `"reasoning": {"enabled": false}`-felt med HTTP 400. Send kaldet uden feltet overhovedet som fallback, i stedet for at sætte det til false — mere kompatibelt på tværs af modeller.
- **Sidetal-styring:** hvis et nummer skal holdes kort (fx 10-15 sider), brief artiklerne til lavere målængde fra start (450-650 ord for føljetonstof) frem for at skrive langt og klippe bagefter — redigering kan kun spare så meget. Brug frontmatter-feltet `flow: true` på korte bagsnit-artikler, så de deler sider i stedet for hver at tvinge en ny side. Bekræftet i HORISONTEN nr. 1: strammere briefs fra start (ingen efterfølgende trimning nødvendig) landede på 15 sider i første hug, mod GNISTENs 27→16 sider efter en hård eftertrimning.
- **Rejsestof kræver geografisk præcision:** brief skribenterne eksplicit til at navngive rigtige steder, ruter og landsbyer (ikke generiske beskrivelser) — det gav HORISONTEN nr. 1 sin troværdighed. Kombinér med reglen om ALDRIG at opdigte præcise datoer for virkelige, tilbagevendende begivenheder (kun "omtrentligt, med forbehold").
- **`google/gemini-3.1-pro` kan svare HTTP 400 "not a valid model ID"** på OpenRouter, selvom modellen har brugt succesfuldt før (GNISTEN nr. 1) og står som `aktiv` i `modeller.json`. Set 2026-08-29 (HumaNerd nr. 4, Hjernen). `--fallback` (til `deepseek/deepseek-v3.2` i det tilfælde) løste det med det samme og gav et fint resultat. Ukendt om det er en midlertidig OpenRouter-side-fejl eller en rebrandet model-ID — tjek `--dry-run` af den rene modelstreng, hvis det sker igen, før du antager roster-filen er forkert.
