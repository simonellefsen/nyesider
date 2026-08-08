# GNISTEN – Redaktionsnotesbog

Redaktionel backlog og noter — opdateret efter nr. 3 (august 2026, "Agenten og den lokale hjerne"). Modelerfaringer ligger i det fælles [modelkartotek](../modelkartotek.md).

## Identitet

**GNISTEN** er magasinet for nysgerrige, der vil skabe med AI **uden at være programmør** — praktisk, prøv-selv-vinklet, ingen forudsætninger. Ikke en teknologi-nyhedstjeneste og ikke en udvikler-publikation; hvis en artikel kræver at læseren allerede kan kode, er den ikke GNISTEN.

## Format

- **Faste formater:** Kortet · Fokus · Værkstedet · Månedens prompt · Regningen · Ordbogen · Sladder (`flow: true` på bagsnit).
- **Ordmål:** 350–500 ord på features (nr. 3: tre kerne-features ~360–380 efter editor-udvidelse; bagsnit korte).
- **Standard `mustCite`:** 1–2 for Fokus/Værkstedet-features med konkrete priser/versionstal når de låses; 0 for Månedens prompt, Ordbogen, Sladder — og for pejlemærke-features der bevidst undgår forældelige prisskilte.

## Afviklet i nr. 3

- **Løfte indfriet** fra nr. 2-bagside: Fokus Gemini · lokale modeller (Ollama) · første agent-arbejdsgang med bremse.  
- Kortet, Månedens prompt, Regningen, Ordbog, sladder.  
- `bestilling.json`: `redaktion/gnisten/numre/2026-08-nr3/bestilling.json`.

## Afviklet i nr. 2

- Fokus: ChatGPT (som lovet på bagsiden af nr. 1).
- Værkstedet: MCP for begyndere.
- Første skridt ud af browseren / publicering (Vercel, Cloudflare Pages, GitHub Pages).
- Opdateret Kortet, Regningen, Ordbog, Sladder.

## Løfter givet i nr. 3

- **Bagsiden:** flere agenter, mere ansvar (`backCoverPromise`).

## Historier i støbeskeen til nr. 4+

- **(2026-08) Sikkerhed for MCP** — dybere end nr. 2's advarsel; tillid og tilladelser.  
- **(2026-08) Læserindsendte prompts** — saml, hvis der kommer svar.  
- **(2026-08) Agent niveau 2** — smal mappe + én tool, stadig med menneske-stop.  
- **(2026-08) Sammenligningstabel** cloud-planer uden at love faste priser (link til leverandør).

## Praktisk

- Nr. 2–3 er markdown-first; PDF mangler.  
- OpenRouter: **kun** `.env.gnisten`. Imagine: `.env.local`.

## Log

- **2026-08-08:** Nr. 3 publiceret — indfrier bagsideløfte (Gemini / lokalt / agent). Kerne-features udvidet ved accept for at undgå length-collapse; `bestilling.json` oprettet.
- **2026-08-01:** Notesbog udvidet med `## Identitet` og `## Format` (fælles skabelon på tværs af titler, se [redaktion/README](../README.md)).
- **2026-08-01 rettelse:** `08-regningen.md` påstod nr. 1 var produceret for "under 10 dollars" — det faktiske tal i `issue.json` er **0,11 dollars**, en faktor 90 forkert. Rettet til det reelle tal. Ellers udgivet uden kilder (2 titler — GNISTEN og HORISONTEN — har 0 % kildedækning på tværs af alle numre); resten af GNISTENs artikler er ikke gennemgået i denne omgang (kapacitet brugt på det konkrete faktafejl, ikke en fuld retrofit — se Workstream C-princippet i [redaktion/README](../README.md)).
