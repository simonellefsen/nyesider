# Månedens prompt

## Ryd din indbakke uden at give en chatbot adgang til den

Du behøver ikke forbinde noget som helst for at få hjælp til at overskue en fyldt indbakke. Du kan nøjes med at markere nogle mails, kopiere teksten ind i en almindelig AI-chat — altså en kunstig intelligens (AI), du taler med gennem en tekstboks, uden at den er koblet til dit Gmail eller Outlook — og bede den sortere. Denne måneds prompt er bygget til præcis det.

Pointen er ikke, at AI'en skal gøre noget ved din post. Den skal kun læse den og foreslå. Derfor har prompten tre indbyggede bremser, som du ikke må fjerne:

**Boks — kopiér denne prompt:**

```
Du får indsat uddrag af nogle mails. For hver mail skal du lave en
tabelrække med: Afsender · Hvad mailen vil · Forslag (svar i dag /
parkér / reklame) · Kladde-svar (hvis relevant).

Regler, som du ALTID skal følge:
1. Foreslå aldrig at sende noget. Du skriver kun kladder — jeg
   trykker selv send, hvis jeg vil.
2. Foreslå aldrig at slette eller arkivere en mail. Det er altid
   mit valg.
3. Lov aldrig en dato, et afslag, en pris eller en leverance på
   mine vegne. Hvis en mail kræver et konkret tilsagn (f.eks. "kan
   du levere fredag?" eller "giver I rabat?"), skal kladden indeholde
   [TJEK] i stedet for et bud, og du skal nævne hvad jeg skal tjekke.

Her er mail-uddragene:
[indsæt dine mail-uddrag her]
```

Hvorfor netop disse tre bremser? Fordi de fleste chatbotter, hvis man ikke spærrer for det, gør noget hjælpsomt, der i virkeligheden er farligt. Bed man bare om "hjælp med indbakken", vil mange modeller tilbyde at formulere og "sende et svar nu" — og nogle brugerflader har knapper, der gør afsendelse til ét klik for let. Første bremse forhindrer, at en kladde ender i verden, før du har læst den igennem.

Anden bremse handler om noget mindre åbenlyst: en chatbot, der skal "rydde op", vil ofte foreslå at arkivere eller slette, fordi det ligner oprydning. Men en mail, der ser ud som reklame, kan vise sig at være en kvittering, du får brug for om et år. Det er din beslutning, ikke modellens.

Tredje bremse er den vigtigste, og den hvor chatbotter typisk fejler mest selvsikkert. Beder man om et kladde-svar til en kunde, der spørger "kan I levere torsdag?", vil mange modeller skrive noget i stil med "jeg sørger for, at det er klar torsdag" — fordi det lyder imødekommende. Problemet er, at modellen ikke aner, om det er sandt. Den kender ikke din lagerstatus, din kalender eller din prispolitik. Et løfte om dato, pris, levering eller et afslag, som AI'en digter frem, kan du komme til at stå med ansvaret for. Derfor beder prompten specifikt om [TJEK] i stedet — en markering af, at netop dét punkt skal du selv bekræfte, før kladden sendes.

Afsenderen, emnet og "svar i dag / parkér / reklame"-kolonnen er bevidst holdt simpelt: det er en triage, ikke en automatisering. Du sidder stadig med fingrene på tastaturet. Teknikken bag selve chatten — om den er bygget på en stor sprogmodel (large language model, LLM) eller noget andet — er ligegyldig for, om prompten virker; den afhænger kun af, at du følger de tre regler, hver gang du bruger den.