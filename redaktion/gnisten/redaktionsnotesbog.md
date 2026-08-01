# GNISTEN – Redaktionsnotesbog

Redaktionel backlog og noter — opdateret efter nr. 2 (august 2026, "Ud af browseren"). Modelerfaringer ligger i det fælles [modelkartotek](../modelkartotek.md).

## Identitet

**GNISTEN** er magasinet for nysgerrige, der vil skabe med AI **uden at være programmør** — praktisk, prøv-selv-vinklet, ingen forudsætninger. Ikke en teknologi-nyhedstjeneste og ikke en udvikler-publikation; hvis en artikel kræver at læseren allerede kan kode, er den ikke GNISTEN.

## Format

- **Faste formater:** Kortet · Fokus · Værkstedet · Månedens prompt · Regningen · Ordbogen · Sladder (`flow: true` på bagsnit).
- **Ordmål:** 450–750 ord på features (bekræftet af erfaring: strammere briefs fra start slår at skrive langt og klippe bagefter — se [modelkartotek.md](../modelkartotek.md)).
- **Standard `mustCite`:** 1–2 for Fokus/Værkstedet-features med konkrete påstande (priser, modelnavne, versionstal); 0 for Månedens prompt, Ordbogen, Sladder.

## Afviklet i nr. 2

- Fokus: ChatGPT (som lovet på bagsiden af nr. 1).
- Værkstedet: MCP for begyndere.
- Første skridt ud af browseren / publicering (Vercel, Cloudflare Pages, GitHub Pages).
- Opdateret Kortet, Regningen, Ordbog, Sladder.

## Løfter givet i nr. 2

- **Bagsiden lovede:** Gemini, lokale modeller og den første rigtige agent-arbejdsgang til nr. 3 (`backCoverPromise` i issue.json).

## Historier i støbeskeen til nr. 3

- **(2026-08) Fokus: Gemini** — Google-økosystemet, Android/Workspace-vinklen.
- **(2026-08) Lokale modeller** — Ollama m.fl.: hvornår giver det mening for en begynder?
- **(2026-08) Agent-arbejdsgange** — fra chat til multi-step uden at miste kontrollen.
- **(2026-08) Sikkerhed for MCP** — dybere end nr. 2's advarsel; tillid og tilladelser.
- **(2026-08) Læserindsendte prompts** — saml, hvis der kommer svar på "Stikket og skiltet".

## Praktisk

- Nr. 2 er markdown-first; PDF og cover-illustrationer mangler stadig (generér via `build_magazine.py` + billedmodeller).

## Log

- **2026-08-01:** Notesbog udvidet med `## Identitet` og `## Format` (fælles skabelon på tværs af titler, se [redaktion/README](../README.md)).
- **2026-08-01 rettelse:** `08-regningen.md` påstod nr. 1 var produceret for "under 10 dollars" — det faktiske tal i `issue.json` er **0,11 dollars**, en faktor 90 forkert. Rettet til det reelle tal. Ellers udgivet uden kilder (2 titler — GNISTEN og HORISONTEN — har 0 % kildedækning på tværs af alle numre); resten af GNISTENs artikler er ikke gennemgået i denne omgang (kapacitet brugt på det konkrete faktafejl, ikke en fuld retrofit — se Workstream C-princippet i [redaktion/README](../README.md)).
