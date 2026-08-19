---
title: "Din egen private AI med Ollama"
standfirst: Langsommere end en cloud-model, men den er din. Og den er ikke længere kun lokal.
byline: Gemini 3.1 Pro Preview (Google)
section: Værkstedet
order: 4
image: ../images/gnisten_lokal.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

Når vi arbejder med kunstig intelligens — for eksempel ChatGPT — sender vi vores tekster og data afsted til store, eksterne servere. For mange nysgerrige skabere rejser det et naturligt spørgsmål: hvad nu, hvis du vil eksperimentere på din egen maskine, uden at dele dine ufærdige idéer med resten af verden? Det er her, Ollama kommer ind i billedet.

I tekniske kredse bliver Ollama ofte beskrevet med analogien "Docker for AI-modeller" — Docker er et populært værktøj, der pakker kompliceret software ind i lukkede kasser, så det er nemt at starte på enhver computer. Det er en analogi, ikke et faktuelt navn på produktet, men den giver et hurtigt billede: Ollama gør det let at hente og køre sprogmodeller uden at skulle indstille alting manuelt.

### Ikke længere kun lokalt

På sin egen hjemmeside beskriver projektet sig selv med ordene: "Build with open models, on your computer and in the cloud."[^1] Det er værd at bemærke: Ollama er ikke længere udelukkende et rent lokalt værktøj. Der er nu også en cloud-mulighed som et direkte valg oveni den lokale funktion.

Når vi her i magasinet alligevel kalder det det private valg, skyldes det, at programmet fortsat kan køres "entirely offline for mission critical work". Valget mellem at køre lokalt på skrivebordet eller i skyen er dit.

### Sådan kommer du i gang

Ollama understøtter macOS, Linux og Windows. Du finder installationsfilerne på den officielle download-side.[^2] Bruger du macOS, kræver det Sonoma 14 eller nyere.

Foretrækker du kommandolinjen, klares installationen på macOS og Linux med: `curl -fsSL https://ollama.com/install.sh | sh`. Projektet opdateres løbende — seneste version på GitHub er v0.32.14, udgivet 15. august 2026.[^3]

Når installationen er overstået, åbner du terminalen og skriver din første kommando: `ollama run <navn-paa-model>`. Projektets egen dokumentation bruger sprogmodellen `gemma4` som gennemgående eksempel. Første gang du kører kommandoen, henter Ollama automatisk de nødvendige filer, hvis de ikke allerede findes lokalt.

### Taler samme sprog som de store

En af Ollamas styrker er, hvordan den kommunikerer med andre programmer. Den kører en REST-API (*Representational State Transfer*, en almindelig måde at lade programmer tale sammen over internettet) på port 11434, i et OpenAI-kompatibelt format. Har du fundet et værktøj, der egentlig er bygget til at tale med OpenAIs systemer, vil det derfor ofte virke med Ollama med få ændringer.

I GNISTEN handler det om at prøve ting af uden forhåndskrav. Du behøver ikke forstå kvantisering (en metode til at komprimere filstørrelser) eller tænke over hukommelsen på din computers grafikkort for at eksperimentere. Du skal bare være forberedt på, at Ollama vil være langsommere end en stor cloud-model på samme opgave — og at det til gengæld holder dine forespørgsler på din egen maskine, når du vælger den lokale kørsel.

[^1]: Ollamas hjemmeside: [ollama.com](https://ollama.com/).

[^2]: Ollamas officielle download-side: [ollama.com/download](https://ollama.com/download).

[^3]: Udgivelsesnoter fra Ollamas GitHub-arkiv: [github.com/ollama/ollama/releases](https://github.com/ollama/ollama/releases/tag/v0.32.14).
