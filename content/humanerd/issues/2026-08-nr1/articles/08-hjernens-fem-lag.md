---
title: "Hjernens fem lag"
standfirst: "Robot-AI er ikke én hjerne. Det er et forløb fra blik til bremse."
section: "Hjernen"
order: 8
figures:
  - images/figur-robotstack.svg
---

Når en robot ser en kasse og flytter den, er det sjældent én model, der gør alt. Det er en stak af beslutninger med meget forskellige krav til tid og sikkerhed.

**1. Perception.** Kameraer, dybdesensorer, taktile og kraftsensorer oversætter lys og berøring til en arbejdshypotese: Hvor er kassen? Er hånden fri? Er noget i vejen?

**2. Verdensmodel og simulation.** Her kan systemet øve variationer uden at tabe rigtige emner. NVIDIA beskriver Isaac Sim og Isaac Lab som dele af et simulerings- og læringsflow; formålet er blandt andet at lukke afstanden mellem en virtuel opgave og den virkelige robot.[^1]

**3. Opgaveplan.** Et højere lag vælger rækkefølgen: hent, orientér, læg, kontrollér. Sprog kan være en del af dette lag, men det er ikke motorstyring.

**4. Bevægelsespolitik.** Her omsættes hensigten til konkrete led, kræfter og greb. NVIDIA lancerede Isaac GR00T N1 som en åben, tilpasningsbar grundmodel for humanoiders ræsonnement og færdigheder; de beskrev samtidig et åbent datasæt med **24.000** humanoide bevægelsesforløb.[^2]

**5. Sikkerhed og kontrol.** Grænser for kraft, fart, kollisionsafstand og nødstop må ikke være en eftertanke fra sprogmodellen. Det er de sidste lag, der afgør, om robotten standser, når verden afviger fra planen.

[FIGUR 1]

"Fysisk AI" er et praktisk navn for hele kæden. Et godt svar i tekst er ikke nok; robotten skal også se rigtigt, vælge rigtigt, bevæge sig rigtigt og kunne lade være.

[^1]: [NVIDIA Physical AI Learning](https://docs.nvidia.com/learning/physical-ai/index.html) — platformens undervisningsoversigt over simulation, læring og deployment.
[^2]: [NVIDIA: Isaac GR00T N1](https://nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks) — produktannoncen og dens beskrivelse af åben model og datasæt.
