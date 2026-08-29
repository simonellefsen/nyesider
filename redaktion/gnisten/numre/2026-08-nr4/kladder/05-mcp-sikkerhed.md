## Værkstedet: Giv din AI færre nøgler, end du tror den behøver

En AI-assistent kan skrive, opsummere og finde mønstre i tekst helt på egen hånd. Men når den kobles til dine filer, kalender, e-mail eller andre tjenester, får den pludselig mulighed for at *gøre* noget. Det er her, **Model Context Protocol (MCP)** kommer ind i billedet.

MCP er en standard, som lader en AI-assistent forbinde sig til eksterne værktøjer og data gennem såkaldte MCP-servere. En server kan for eksempel give assistenten adgang til en mappe på din computer, et dokumentarkiv eller en online-tjeneste. Det kan være enormt nyttigt: Du kan bede assistenten finde noter, sortere bilag eller hente oplysninger fra et system, du allerede bruger.

Men forbindelsen er også en tilladelse. Og en tilladelse er i denne sammenhæng ikke bare en venlig forespørgsel. Det er en regel om, hvad AI-assistenten og det værktøj, den bruger, må gøre på dine vegne.

### Hver server er en ny dør ind

Tænk på en MCP-server som en håndværker, der får adgang til dit hus. Du kan give håndværkeren en nøgle til hoveddøren, men du kan også give adgang kun til kælderen og kun i arbejdstiden. Jo bredere adgang, desto mere kan håndværkeren hjælpe — og desto større bliver konsekvensen, hvis noget går galt.

Det samme gælder MCP. Hver ny server er en ny **tillidsgrænse**: et sted, hvor du reelt lader fremmed kode arbejde med dine data eller dine konti. Serveren kan være velment og nyttig, men den kan også have fejl, være dårligt vedligeholdt eller blive narret af skadelig tekst i et dokument. NSA peger blandt andet på, at MCP-forbindelser kræver kontrol med identitet, adgang og de data, værktøjerne får lov at behandle.[^1]

Sikkerhedsfirmaet Wiz anbefaler derfor et enkelt princip: Både MCP-serveren og den AI-agent, der bruger den, bør have de mindst mulige tilladelser, opgaven tillader. Det kaldes ofte princippet om mindst privilegium. Hvis assistenten kun skal læse tre dokumenter, behøver den ikke kunne gennemse hele din computer — og slet ikke slette filer.[^2]

### De 3 svar: allow, deny og ask

I et tilladelsessystem som det, Claude Code beskriver, findes der 3 grundlæggende niveauer:

1. **allow — tillad**  
   Handlingen må ske automatisk. Hvis reglen siger, at assistenten må læse filer i en bestemt mappe, bliver du ikke spurgt hver gang.

2. **deny — afvis**  
   Handlingen er forbudt. En regel kan for eksempel afvise sletning af filer eller adgang til en mappe med private dokumenter.

3. **ask — spørg**  
   Assistenten skal bede dig om godkendelse, før handlingen udføres. Det er den forsigtige mellemvej: Du får stadig hjælpen, men ser handlingen, før den sker.

Reglerne evalueres i rækkefølgen **deny → ask → allow**. Den første regel, der matcher handlingen, vinder.[^3] Derfor er en afvisningsregel stærkere end en tilladelsesregel: Hvis du både har sagt “AI må arbejde med filer” og “AI må aldrig åbne mappen Privat”, skal afslaget på den private mappe gælde først.

Det er værd at læse reglerne som trafikskilte. **Deny** er en lukket vej. **Ask** er et stopskilt, hvor du skal tage stilling. **Allow** er en åben vej. Sætter du den åbne vej først og uden begrænsning, risikerer du at give mere adgang, end du mente.

### Din sikre startopsætning

Start altid med **ask** for en ny MCP-server. Godkend de konkrete handlinger, og læg mærke til, hvad der faktisk bliver bedt om: Skal værktøjet kun læse en fil? Oprette et dokument? Sende noget ud af huset? Eller ændre data?

Udvid først til **allow**, når du har set den samme, ufarlige handling fungere trygt flere gange. En god kandidat kan være at læse filer i én bestemt arbejdsmappe. Undgå derimod automatisk tilladelse til at slette, sende, dele eller ændre oplysninger — især hvis handlingen ikke let kan fortrydes.

Og lav gerne en eksplicit **deny**-regel for det, der aldrig må røres: private mapper, adgangskoder, økonomiske dokumenter eller andre følsomme data.

Den mest nyttige AI-assistent er ikke den, der har alle nøglerne. Det er den, der har præcis den nøgle, opgaven kræver.

[^1]: National Security Agency, *MCP Security*, sikkerhedsvejledning: <https://media.defense.gov/2026/Jun/02/2003943289/-1/-1/0/CSI_MCP_SECURITY.PDF>  
[^2]: Wiz, *Model Context Protocol Security*: <https://www.wiz.io/academy/ai-security/model-context-protocol-security>  
[^3]: Anthropic, *Claude Code permissions*: <https://code.claude.com/docs/en/permissions>