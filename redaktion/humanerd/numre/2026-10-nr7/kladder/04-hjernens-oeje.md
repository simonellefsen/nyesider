# Hjernen: Fra pixel til pakke – perceptionsstakken i Figure Helix

At udstyre en robot med et kamera er den lette del. Den svære del er at få kameraets pixels til at blive til en fysisk bevægelse, der ikke knuser en papkasse eller taber et skrøbeligt objekt. I robotteknologiens perceptionsstak er synet nemlig aldrig færdigt, før det er oversat til motoriske kommandoer. Det er i dette oversættelsesled, at kompromisserne ligger, og det er her, den amerikanske robotproducent Figure AI forsøger at stramme grebet med deres model Helix.

Den 20. februar 2025 introducerede Figure AI Helix som en såkaldt Vision-Language-Action-model (VLA).[^1] En VLA-model forsøger at løse et grundlæggende problem i moderne robotteknologi: kløften mellem højniveau-sprogforståelse og lavniveau-motorstyring. I stedet for at lade en sprogmodel uddele abstrakte ordrer til et separat synssystem, kobler Helix stereo-kameraer, sprogforståelse og direkte kontrol af leddene i ét samlet system.

Kæden fra sansning til handling følger en streng logik. Det starter med stereo-kameraer, der optager billedpar. Disse billeder danner grundlaget for en 3D-forståelse af omgivelserne. Herefter følger grebsplanlægningen: Hvor skal fingrene placeres for at undgå kartonens svage punkter? Til sidst kommer korrektionerne i millisekunder, mens armen bevæger sig, og objektet måske glider eller ændrer tyngdepunkt.

For at håndtere denne kæde i realtid opererer Helix med det, Figure AI kalder System 1 – det hurtige, reaktive lag i modellen. System 1 udsender såkaldte *action chunks* (forudberegnede sekvenser af motoriske kommandoer) med en frekvens på 200\u00a0Hz.[^2] Det betyder, at robotten justerer sin bane 200 gange i sekundet, hvilket er nødvendigt, når en pakke skal tages fra et transportbånd i bevægelse.

Netop transportbåndet er omdrejningspunktet for den opdatering, Figure AI offentliggjorde den 26. februar 2025 under titlen 'Helix Accelerating Real-World Logistics'.[^3] Her demonstreres en klassisk lageropgave: Robotten skal tage tilfældige pakker fra et bånd og dreje dem, så forsendelsesetiketten vender præcist mod en stregkodescanner. Det lyder simpelt, men det kræver, at perceptionen forstår, at en krøllet plastikpose og en firkantet papkasse kræver vidt forskellige fysiske tilgange.

Her afsløres også, hvor meget menneskelig indgriben der stadig kræves for at få fysisk kunstig intelligens til at fungere i drift. Ifølge Figures egne oplysninger gav 8 timers velkurateret demonstrationsdata en 40\u00a0% bedre *throughput* (gennemstrømning) end en markant større, men mere rodet og ukureret datamængde.[^3] Det er en vigtig påmindelse om, at robotter i dag ikke bare "lærer sig selv" i et hjørne af lageret; de fodres med omhyggeligt udvalgte succeser. Figure AI hævder desuden, at deres 'Sport Mode' kan accelerere udførelsen med op til 50\u00a0%, og at Helix generelt kan "pick up anything" – altså gribe tusindvis af aldrig før sete genstande udelukkende baseret på en naturlig sproglig instruktion.[^1]

Som læser og indkøber skal man her huske at skelne mellem demo og drift. At rotere en pakke til en scanner under kontrollerede lysforhold er en validering. At gøre det i 12 timer i træk med støv på kameralinsen, reflekser fra plastik og paller, der skifter placering, er stabil drift. 

Perceptionsstakken i Helix viser, hvor langt vi er kommet med at koble sprog og syn direkte til muskler. Men den viser også, at fysisk AI ikke er magi. Det er statistik, stereo-kameraer og 8 timers perfekt træningsdata, der møder virkelighedens rod – milisekund for milisekund.

***

[^1]: Figure AI: «Helix: A Vision-Language-Action Model for Generalist Humanoid Control», 20. februar 2025: [https://www.figure.ai/news/helix](https://www.figure.ai/news/helix).
[^2]: Figure AI: teknisk beskrivelse af Helix-arkitekturen (System 1/System 2), se [https://www.figure.ai/news/helix](https://www.figure.ai/news/helix).
[^3]: Figure AI: «Helix Accelerating Real-World Logistics», 26. februar 2025: [https://www.figure.ai/news/helix-logistics](https://www.figure.ai/news/helix-logistics).