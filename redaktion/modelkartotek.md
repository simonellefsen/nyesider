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
| Kimi K3 | Missede deadline i PULSEN nr. 1 | Fortjener en revanche-opgave i nr. 2 |

**Hurtige reservemodeller** (leverede hurtigt til PULSEN nr. 1): llama-4-maverick, deepseek-v3.2, grok-4.3, mistral-large, gemini-3.5-flash.

## Billedmodeller

- **Gemini 3 Pro Image** — forsider; gode resultater.
- **Gemini 3.1 Flash Image** — artikelbilleder.
- Tip: skriv altid "no text" i prompten.

## Produktionspraktik

- Sandboxens shell-kald har 45 sek. loft: kør én artikel pr. kald; slå reasoning fra på langsomme modeller; billeder én ad gangen.
- Layout hidtil: ReportLab-script (`build_magazine.py`), A4, DejaVu-fonte.
