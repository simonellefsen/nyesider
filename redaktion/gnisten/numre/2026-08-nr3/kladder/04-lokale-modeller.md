# Værkstedet: Din egen private AI med Ollama

Når vi arbejder med systemer baseret på Artificial Intelligence (AI) – for eksempel ChatGPT – sender vi vores tekster og data afsted til store, eksterne servere. For mange nysgerrige skabere rejser det et naturligt spørgsmål: Hvad nu, hvis du vil eksperimentere på din egen maskine, helt uden at dele dine ufærdige idéer med resten af verden? Det er netop her, Ollama kommer ind i billedet.

I tekniske kredse bliver Ollama ofte beskrevet med analogien "Docker for AI-modeller". Docker er et populært værktøj, der pakker kompliceret software ind i små lukkede kasser, så det er nemt at starte på enhver computer. På fuldstændig samme måde gør Ollama det let at hente og køre sprogmodeller uden at skulle indstille alting manuelt fra bunden.

På deres egen hjemmeside beskriver projektet sig selv med ordene: "Build with open models, on your computer and in the cloud". Som du kan læse af det citat, er det vigtigt at bemærke, at Ollama ikke længere udelukkende er et rent lokalt værktøj. De tilbyder nu også cloud-kørsel som et direkte valg oveni den lokale funktion. Når vi her i magasinet alligevel vælger at kalde det for det private valg, skyldes det, at programmet fortsat er bygget til at kunne køre "entirely offline for mission critical work". Valget mellem at køre lokalt på skrivebordet eller i skyen er fuldstændig dit.

**Sådan kommer du i gang med installationen**
Ollama understøtter de tre store styresystemer: macOS, Linux og Windows. For at installere det på din maskine, skal du blot besøge deres dedikerede download-side[^1], hvor du finder de direkte installationsfiler. Bruger du en Apple-computer med macOS, skal du dog være opmærksom på én vigtig detalje: Det kræver styresystemet Sonoma 14 eller en nyere version.

Hvis du foretrækker at bruge kommandolinjen, kan selve installationen for Linux og macOS klares lynhurtigt med denne kodelinje i terminalen: `curl -fsSL https://ollama.com/install.sh | sh`. Projektet opdateres løbende, og den seneste version på deres åbne kildekodelager, GitHub, er i skrivende stund version v0.32.14, som udkom den 15. august 2026[^2].

Når installationen er veloverstået, åbner du din terminal og skriver din allerførste kommando: `ollama run <navn-paa-model>`. Dokumentationen bruger sprogmodellen `gemma4` som deres gennemgående eksempel. Første gang du kører den kommando, sørger Ollama helt automatisk for at hente de nødvendige filer ned på din computer, hvis de ikke allerede findes lokalt.

**Taler samme sprog som de store**
En af Ollamas helt store forcer er den måde, den kommunikerer med andre programmer på. Under motorhjelmen kører den en såkaldt Representational State Transfer Application Programming Interface (REST-API) på port 11434. I praksis betyder det blot, at den lyttende dør på din computer kører i et format, som er direkte OpenAI-kompatibelt. Hvis du har fundet et spændende, nyt stykke værktøj, der egentlig er bygget til at tale med OpenAIs systemer, vil det derfor ofte virke med Ollama med meget få ændringer.

I GNISTEN handler det om at prøve ting af uden forhåndskrav. Du behøver slet ikke at forstå tekniske koncepter som kvantisering (en metode til at komprimere filstørrelser) eller tænke over mængden af hukommelse på din computers Graphics Processing Unit (GPU) for at eksperimentere med systemet. Du skal bare være forberedt på, at Ollama vil være langsommere end en enorm cloud-model på samme opgave, men at det til gengæld giver dig 100 % kontrol over dine egne data i bytte.

[^1]: Ollamas officielle download-side med installationsfiler: https://ollama.com/download
[^2]: Udgivelsesnoter fra Ollamas officielle GitHub-arkiv: https://github.com/ollama/ollama/releases/tag/v0.32.14