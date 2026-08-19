# GNISTEN – Redaktionsnotesbog

Redaktionel backlog og noter — opdateret efter nr. 3 (august 2026, "Agenten og den lokale hjerne"). Modelerfaringer ligger i det fælles [modelkartotek](../modelkartotek.md).

## Identitet

**GNISTEN** er magasinet for nysgerrige, der vil skabe med AI **uden at være programmør** — praktisk, prøv-selv-vinklet, ingen forudsætninger. Ikke en teknologi-nyhedstjeneste og ikke en udvikler-publikation; hvis en artikel kræver at læseren allerede kan kode, er den ikke GNISTEN.

## Format

- **Faste formater:** Kortet · Fokus · Værkstedet · Månedens prompt · Regningen · Sladder (`flow: true` på bagsnit). **Ingen Ordbog** — gloser i parentes/fodnote.
- **Ordmål:** **500–750 på de tre kernefeatures** (Fokus, Værkstedet, det praktiske), 400–600 på
  Kortet, Regningen og Sladder. Hævet fra 350–500 den 2026-08-09: en forklaring på MCP, der skal
  holde uden forudsætninger, kan ikke leveres på 350 ord.
- **Standard `mustCite`:** **2+ for Fokus, Værkstedet og alle features med datoer, versionstal eller
  produktpåstande**; 0 for Månedens prompt og Sladder. Hævet 2026-08-09 — titlen havde 0 %
  kildedækning, og det var den alvorligste svaghed i formatet.
- **Kilder skal pege på den konkrete side**, ikke på leverandørens forside. En adresse, der virker,
  er ikke det samme som en adresse, der dokumenterer påstanden.

## Afviklet i nr. 3 — genopbygget 2026-08-19

**Genopbygget:** 8 artikler / 2.620 ord. Syv artikler reelt kommissioneret på `.env.gnisten`;
lederen er redaktionens uden byline. Forbrug **0,2156 USD**. Fire nye motiver (Imagine).

Den afpublicerede bestilling.json var det reneste tomme skelet fundet i hele oprydningen: otte
opgaver, alle `writer.model: "editor-led"`, ingen `researchNote`, ikke ét `mustNumber` — og alligevel
udgivet med byline til navngivne modeller. Nummeret er nu bygget forfra med reel research forud for
hver brief.

### Læring fra genopbygningen af nr. 3 (2026-08-19)

**`.env.gnisten` ramte en kreditgrænse midt i produktionen.** Opus 4.8's `max_tokens`-budget kunne
ikke dækkes af nøglens resterende kredit (OpenRouter HTTP 402). Løsning: `--fallback`-flaget i
`commission.py`, som brugte `writer.fallback` (Claude Sonnet 5) i stedet — en sanktioneret vej, ikke
en omgåelse. Bylinen på `agent`-artiklen navngiver derfor Sonnet, ikke Opus, fordi bylinereglen er
byline ⇔ den model, der faktisk kørte.

**Google-kilder om Gemini skal holdes adskilt.** «Personal Intelligence» (blog.google, 14. januar
2026) forbinder Gemini til præcis fire apps — Gmail, Google Photos, YouTube, Search — IKKE alle
Workspace-apps. Flere sekundære kilder (SEO-blogs, som GNISTENs egen nr. 2-læring advarede mod)
overdriver dette til at være hele økosystemet. Adskilt fra «Gmail is entering the Gemini era», som
beskriver fem konkrete Gmail-funktioner med et klart gratis/abonnement-skel.

**Ollama er ikke længere rent lokalt.** Ollama.com beskriver sig selv som «on your computer and in
the cloud» — en cloud-mulighed er kommet oveni det lokale spor. GNISTEN kalder det stadig «det
private valg», fordi offline-kørsel stadig findes, men skrev skiftet eksplicit frem i tre artikler
(Kortet, Værkstedet, Regningen), fordi det ændrer selve præmissen for, hvorfor man vælger værktøjet.

**GitHub Copilot CLI's autopilot-dokumentation er en klar, citerbar kilde til «bremse og
tillidsniveau».** Man behøver ikke opfinde et sikkerhedsprincip for agenter — det er allerede skrevet
ned i et udbredt værktøjs egen dokumentation, med en eksplicit advarsel om at fulde tilladelser
"gives the CLI permission to make any changes it deems necessary to complete the task, including
altering and deleting files".

`bestilling.json`: `redaktion/gnisten/numre/2026-08-nr3/bestilling.json`.

## Afviklet i nr. 2

- Fokus: ChatGPT (som lovet på bagsiden af nr. 1).
- Værkstedet: MCP for begyndere.
- Første skridt ud af browseren / publicering (Vercel, Cloudflare Pages, GitHub Pages).
- Opdateret Kortet, Regningen, Sladder. Ordbogen droppet.

**Genopbygget 2026-08-09:** 8 artikler / 4.034 ord (var 9 / 3.281). Syv artikler reelt
kommissioneret på `.env.gnisten`; lederen er chefredaktionens uden byline. Forbrug **0,25 USD**.
`bestilling.json` oprettet — der fandtes ingen før.

### Læring fra genopbygningen af nr. 2 (2026-08-09)

**Nummeret havde slet ingen `bestilling.json`.** Ikke en nulstillet — ingen overhovedet, for nogen af
de ni artikler, samtidig med at de bar byline til navngivne modeller. Det er det reneste brud på
forlagets første non-negotiable, der er fundet i hele oprydningen.

**GNISTENs 0 %-kildedækning er rettet i dette nummer.** Titlen har historisk ikke haft en eneste kilde
på tværs af alle numre. Nu har hvert versionstal, hver dato og hver produktpåstand en adresse, og
adressen går til leverandørens eller standardens egen dokumentation. Det er skrevet ud i lederen,
fordi et blad, der beder læseren være kritisk, skal kunne tåle sit eget krav.

**Modellerne pegede stadig på forsider frem for sider.** Fire ud af syv kladder afsluttede med
`linuxfoundation.org`, `modelcontextprotocol.io` eller `vercel.com` — adresser der virker, men som
ikke dokumenterer den konkrete påstand. Regn med at skulle finde den præcise side hver gang.

**Den ene faktafælde, der skal blive stående i titlen:** Vercels gratis Hobby-plan må ifølge Vercels
egen dokumentation kun bruges til *ikke-kommercielle, personlige* formål. Det er den slags, en
begynder opdager for sent, og det er præcis GNISTENs opgave at sige det først.

**Kontinuitet: bagsideløfter er bindende.** Kladden til Sladder opfandt et nyt løfte om næste nummer
(oprydning i mapper og feriebilleder). Nummerets `backCoverPromise` — og det, nr. 3 faktisk leverede —
var Gemini, lokale modeller og den første agent-arbejdsgang. Et forkert løfte her ville have gjort
bladets egen historik usand bagud. Tjek altid `backCoverPromise` mod det, næste nummer gjorde.

**`check_issue.py`s nye YAML-tjek fangede en 404 før build.** `fokus-chatgpt` havde et ucitéret
standfirst med kolon i. Uden tjekket ville det først være dukket op som en prerender-fejl til sidst
i en fuld build.

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

- **2026-08-08 (format):** Ordbogen fjernet fra nr. 3 — gloser i parentes/fodnote i features.


- **2026-08-08:** Nr. 3 publiceret — indfrier bagsideløfte (Gemini / lokalt / agent). Kerne-features udvidet ved accept for at undgå length-collapse; `bestilling.json` oprettet.
- **2026-08-01:** Notesbog udvidet med `## Identitet` og `## Format` (fælles skabelon på tværs af titler, se [redaktion/README](../README.md)).
- **2026-08-01 rettelse:** `08-regningen.md` påstod nr. 1 var produceret for "under 10 dollars" — det faktiske tal i `issue.json` er **0,11 dollars**, en faktor 90 forkert. Rettet til det reelle tal. Ellers udgivet uden kilder (2 titler — GNISTEN og HORISONTEN — har 0 % kildedækning på tværs af alle numre); resten af GNISTENs artikler er ikke gennemgået i denne omgang (kapacitet brugt på det konkrete faktafejl, ikke en fuld retrofit — se Workstream C-princippet i [redaktion/README](../README.md)).

- **2026-08-09:** Nr. 2 genopbygget og genudgivet efter afpubliceringen 2026-08-08. `bestilling.json`
  oprettet fra bunden — der fandtes ingen. Kildedækningen gik fra 0 til 13 fodnoter. Se læringen ovenfor.

- **2026-08-19:** Nr. 3 genopbygget og udgivet efter at have ligget som et tomt brief-skelet med
  byline til navngivne modeller. Se læringen ovenfor. Ny fast note: `.env.gnisten` har en snæver
  kreditgrænse — brug `--fallback` frem for at presse Opus-kald igennem, hvis 402 opstår.
