---
title: "Din første agent-arbejdsgang (uden at miste kontrollen)"
standfirst: En agent er bare en assistent med flere skridt og flere tilladelser. Giv den små opgaver.
section: Værkstedet
order: 5
image: ../images/gnisten_agent.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

### Definition

En **agent** er et AI-system, der planlægger og udfører flere trin: læs fil → foreslå rettelse → skriv udkast → (måske) kør kommando. Det er kraftfuldt. Det er også der, ting kan gå galt. Under motorhjelmen ligger ofte **tool use** / *function calling*: modellen må kalde værktøjer (filer, terminal, API’er) i stedet for kun at returnere tekst.

Chat er “spørg og få svar”. Agent er “få lov til at *gøre* noget”. Forskellen er **tilladelser**.

### Mini-workflow du kan kopiere

1. **Mål:** “Lav en punktopstilling af denne mødenote.”  
2. **Input:** én fil / én tekst.  
3. **Output:** ny fil `referat-udkast.md` — **ikke** overwrite af originalen.  
4. **Stop:** du læser, retter, godkender.  
5. Først derefter: send, publicér, commit.

Skriv målet ind i prompten som en checkliste. Agenter elsker at “hjælpe videre” — din opgave er at sige, hvornår de er færdige.

### Tre niveauer af tillid

| Niveau | Agenten må | Du gør |
|---|---|---|
| 0 — Chat | Læse det, du limer ind | Alt andet |
| 1 — Udkast | Skrive til en *ny* fil | Godkende før brug |
| 2 — Handling | Køre afgrænsede kommandoer / tools | Overvåge log; smal mappe |

De fleste begyndere skal bo på **niveau 1** i uger. Niveau 2 kræver, at du forstår, hvilke tools der er tændt — se [**MCP** (*Model Context Protocol*) i nr. 2](/gnisten/2026-08-nr2/vaerkstedet-mcp): en fælles “stik”-standard, så værktøjer kan kobles til modeller på tværs af produkter.

### Sikkerhedsregler (print dem ud)

- Ingen agenter med adgang til **hele** harddisken “fordi det er nemt”.  
- Ingen API-nøgler i chats, du deler eller logger.  
- Ingen “slet / force-push / send mail” uden eksplicit menneske-godkendelse.  
- Hold et **sandbox-mappe**-trick: agenten må kun skrive i `~/tmp/agent-leg/`.  
- Log hvad den gjorde. Hvis du ikke kan genfortælle det, var tillid for høj.

### Hvad “den første rigtige agent” betyder i GNISTEN

Ikke en autonom kollega. En **kæde med bremse**:

1. Læs `noter.txt`.  
2. Skriv `udkast.md` med tre bullet-afsnit.  
3. Stop.  
4. Du retter to sætninger.  
5. (Valgfrit) bed om en anden version — stadig ny fil.

Når det mønster er kedeligt sikkert, kan du udvide. Kedeligt er godt.

### Bro til Gemini og lokalt

- Cloud-agent (ChatGPT/Gemini/Cursor-agtige flows): hurtig, men data- og tool-politik er leverandørens.  
- [Lokal model](/gnisten/2026-08-nr3/lokale-modeller) + agent: mere privat, mere friktion.  
- [Gemini i økosystemet](/gnisten/2026-08-nr3/fokus-gemini): integration er magten — og risikoen, hvis du limer det forkerte ind.

Kontrol er en feature. Hastværk er en bug.
