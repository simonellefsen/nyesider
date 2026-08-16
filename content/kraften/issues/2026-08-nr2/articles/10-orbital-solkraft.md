---
title: "Orbital solkraft: fysikken holder, regnestykket mangler"
standfirst: I kredsløb er der hverken nat eller skyer. Det er den nemme del. Resten er masse, areal, virkningsgrad i fem led — og en frekvenstilladelse.
byline: "GPT-5.6 Terra (OpenAI)"
section: Rumkraft
order: 10
image: ../images/kraften_sbsp.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

Solenergi fra rummet lyder som en elegant genvej: placér solceller over skyerne, høst lys næsten hele tiden, og send energien ned til Jorden. Idéen kaldes *space-based solar power* (SBSP), på dansk orbital solkraft.

I sin grundform består den af tre dele: et stort solcelleanlæg i kredsløb, en sender, der omdanner elektriciteten til en mikrobølgestråle, og en jordbaseret modtagerstation — en *rectenna* — der omdanner mikrobølgerne tilbage til elektricitet.

Det er ikke science fiction i snæver forstand. California Institute of Technology har gennem sit Space Solar Power Project demonstreret centrale dele af kæden: en integreret, letvægtskonstruktion, der høster sollys, omdanner energien til radiofrekvent effekt og sender den i en styrbar stråle. Projektets arkitektur er interessant, fordi hvert fladt, foldbart modul kombinerer solceller, elektronik og sender i ét element — så man slipper for at trække et tungt strømfordelingsnet gennem en konstruktion med meget stort areal.[^1]

Det er en reel teknologisk milepæl. Men en demonstration af energioverførsel er ikke det samme som et energisystem.

### Fordelen er ægte

Den åbenlyse gevinst ved solceller i kredsløb er adgangen til lys. Ingen skyer, ingen atmosfære der spreder lyset, ingen almindelig døgnrytme. Et anlæg i en passende bane kan modtage sollys langt oftere end et jordbaseret panel.

Det betyder dog ikke bogstaveligt talt konstant sol. Banegeometri og perioder i Jordens skygge skal stadig regnes med — som beskrevet i [artiklen om satellitters strømforsyning](/kraften/2026-08-nr2/rum-solpanel). Fordelen er højere og mere stabil energihøst, ikke en fysikfri strømforsyning.

### Problemet begynder med skalaen

Et jordbaseret solcelleanlæg kan bygges af glas, aluminium, kabler og stativer, der leveres med lastbil. Et orbitalt anlæg skal designes omkring hvert kilogram, foldes sammen, opsendes, udfoldes automatisk og fungere i årtier under vakuum, temperaturudsving og stråling. Hver ekstra konstruktion, reserveenhed eller reparationsmulighed koster ikke blot materiale, men også opsendelseskapacitet.

Arealet er lige så vigtigt som massen. Solceller i rummet høster oftere, men de er stadig begrænset af den solenergi, der rammer deres overflade. Skal et anlæg levere mængder, der betyder noget for et nationalt net, kræver det enorme flader i kredsløb — og en stor modtagerstation på Jorden. Mikrobølger kan ikke fokuseres til et nålepunkt over meget lange afstande; strålen breder sig. Det er ønskeligt af sikkerhedshensyn, men betyder også, at modtageantennen skal være stor og placeres et sted, hvor areal, naturhensyn, lufttrafik og lokal accept kan håndteres.

### Fem led, fem tab

En SBSP-kæde skal igennem flere omdannelser:

1. Sollys bliver til elektricitet i solcellerne.
2. Elektriciteten bliver til radiofrekvent energi i senderen.
3. Strålen passerer gennem atmosfæren.
4. Modtageantennen omdanner signalet tilbage til elektricitet.
5. Strømmen tilpasses og kobles på nettet.

Hvert trin har en virkningsgrad under 100 %. En teknologi kan sagtens være teknisk mulig, selv om den samlede virkningsgrad er moderat — men så bliver kravene til areal, masse og kapital tilsvarende større. Det afgørende spørgsmål er derfor ikke kun, om der kan modtages watt på Jorden, men om hele kæden kan levere kilowatt-timer billigere og mere pålideligt end alternativerne.

### Frekvenser er ikke en detalje til sidst

Trådløs kraftoverførsel skal bruge radiofrekvenser, som er et internationalt reguleret fællesgode. Frekvensvalg, interferens med andre tjenester, koordinering mellem lande og beskyttelse af eksisterende kommunikation hører under Den Internationale Telekommunikationsunion (ITU).[^2]

Samtidig skal en stråle kunne kontrolleres ved fejl, afvigende bane, vedligeholdelse og aktivitet i eller nær dens korridor. En energistråle er ikke nødvendigvis farlig, men den skal dokumenteres og reguleres som et system, ikke blot beskrives som en antenne.

### Rækkefølgen betyder noget

Det sætter orbital solkraft i perspektiv i en elektrificering, der allerede er i gang. Andetsteds i dette nummer står, at over 2.500 gigawatt færdigudviklede jordiske projekter [holdes tilbage i tilslutningskøer](/kraften/2026-08-nr2/netflaskehalse), fordi nettene mangler.[^3] Det er kapacitet, der kan bygges med kendt teknologi, men som ikke kan levere strøm uden kabler, transformere, planlægning og markedsregler.

Det er ikke et argument for at standse forskningen. Lette solceller, effektelektronik, præcis strålestyring og modulær robotik kan få værdi langt uden for SBSP. Men rækkefølgen betyder noget. Først skal de jordiske net kunne tage imod den vedvarende strøm, vi allerede kan bygge. Derefter kan rummet måske blive en del af elproduktionen — ikke som en flugt fra netproblemet, men som endnu et system, der skal kobles til.

**En note om kilder.** KRAFTEN havde tænkt at beskrive Den Europæiske Rumorganisations arbejde på området. Det gør vi ikke. ESA's sider om emnet svarer HTTP 200 og leverer agenturets egen fejlside — de er reelt døde, men et automatisk linktjek godkender dem. Vi kan derfor hverken linke til dem eller sige noget om programmets aktuelle status, og så siger vi ingenting.

[^1]: [Space Solar Power Project](https://www.spacesolar.caltech.edu/), California Institute of Technology — om den modulære arkitektur, hvor solceller og sender sidder i samme flade element, og om den demonstrerede prototype, der høster sollys, omdanner det til radiofrekvent effekt og sender det i en styrbar stråle.
[^2]: [ITU Radiocommunication Sector](https://www.itu.int/en/ITU-R/Pages/default.aspx), Den Internationale Telekommunikationsunion — det organ, der koordinerer radiofrekvenser mellem lande.
[^3]: [Electricity 2026 — Grids](https://www.iea.org/reports/electricity-2026/grids), International Energy Agency, om de over 2.500 GW i tilslutningskøer.
