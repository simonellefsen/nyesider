---
title: "Lokale modeller: Ollama for begyndere"
standfirst: Privat, langsommere, dit ansvar — og det er præcis derfor det er interessant.
byline: Claude Sonnet 5 (Anthropic)
section: Værkstedet
order: 4
image: ../images/gnisten_lokal.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

En **lokal model** (*on-device*) kører på *din* computer. Teksten forlader ikke maskinen, medmindre *du* sender den videre. Det er den primære grund til at prøve det — ikke “gratis uendelig GPT-5 derhjemme”.

### Hvad du får

- **Privatliv som default:** dagbogsnoter, klientkladde, familieplan — uden cloud-log.  
- **Ingen abonnementsmåler pr. token** (du betaler i strøm, disk og tålmodighed).  
- **Kontrol:** du vælger modelstørrelse, og du kan slukke.

### Hvad du *ikke* får

- Samme rå styrke som de største cloud-modeller — især på lange, komplekse opgaver.  
- Altid-opdateret viden om “i går”.  
- Magisk “det bare virker”-installation på en gammel laptop med 8 GB RAM.

### Ollama i tre skridt (macOS/Linux/Windows)

[Ollama](https://ollama.com) er den mest begyndervenlige vej lige nu: ét program, simple kommandoer, modeller hentes med navn.

1. Installér Ollama fra den officielle side.  
2. Åbn terminalen og kør fx `ollama run llama3.2` (eller en anden model, Ollama foreslår — navne skifter; se deres katalog).  
3. Skriv en sætning. Vent. Læs svaret. Ret forventningen: det er *dit* hardwarebudget, der sætter tempoet.

**Tip:** Start med en **lille** model. Hellere hurtige, korte svar end en kæmpe model, der får blæseren til at græde.

### Hvornår det giver mening for en begynder

| Situation | Cloud | Lokalt |
|---|---|---|
| “Skriv tre emner til et nyhedsbrev” | Ofte bedst | Fint, hvis privat |
| Følsomme noter / arbejdskladder | Kun med bevidst politik | Ofte bedst |
| Kode-hjælp på stor codebase | Ofte bedst | Afhænger af RAM/GPU |
| Offline i toget | Nej | Ja |

### Tre fejl, alle laver

1. **For stor model først.** Download er gigabytes; inference er langsom.  
2. **Tror “lokalt = sandt”.** **Hallucinationer** (overbevist opdigt) findes stadig — privatliv ændrer ikke sandhedskravet.  

3. **Glemmer opdateringer.** Ollama og modeller opdateres — kør `ollama pull …` når du vil have nyere vægte.

### Bro til resten af nummeret

Når den lokale model kan svare på én fil, er næste skridt **ikke** “giv den hele harddisken”. Næste skridt er en lille [agent-arbejdsgang](/gnisten/2026-08-nr3/agent) med output til en *ny* fil — og dig som bremse.

Lokalt er ikke det modsatte af cloud. Det er et **ekstra gear**, når privatliv eller offline vejer tungere end rå top-model-kvalitet.
