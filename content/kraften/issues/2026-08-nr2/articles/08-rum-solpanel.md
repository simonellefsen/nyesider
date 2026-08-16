---
title: "Sådan virker det: en satellits strømforsyning"
standfirst: Areal, retning, stråling og varme. Fire ting afgør, hvor mange watt en satellit har — og den sværeste af dem er at komme af med varmen.
byline: "Claude Sonnet 5 (Anthropic)"
section: Rumkraft
order: 8
image: ../images/kraften_rumsol.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

En satellit i kredsløb om Jorden har ingen stikkontakt at ty til. Al strøm, den bruger — til radioer, computere, instrumenter og varme — skal produceres om bord, lagres om bord og bruges om bord. Løsningen er næsten altid den samme: solpaneler, der omdanner sollys til elektricitet, og batterier, der bærer satellitten gennem de perioder, hvor solen er væk.

Princippet er simpelt. Det, der gør det svært, er fire faktorer, som alle trækker i hver sin retning.

### Fire ting bestemmer watt-tallet

Den første er **arealet** af solpanelerne. Flere kvadratmeter celler giver flere watt, men areal koster masse, og masse koster plads på raketten og penge i opsendelsen. Ingen satellit har mere panel, end den absolut må have.

Den anden er **retningen**: hvor godt panelerne peger mod solen. En plade vinkelret på sollyset høster mest; drejer den bare lidt væk, falder udbyttet. Mange satellitter har derfor motoriserede paneler, der roterer for konstant at følge solen, mens selve satellitten peger sine instrumenter et andet sted hen.

Den tredje er **stråling** — ladede partikler fra solen og Jordens magnetfelt, der år for år nedbryder solcellernes krystalstruktur. En ny celle yder mere end den samme celle efter nogle års eksponering. Det er en gradvis, uafvendelig aldring, ikke en fejl.

Den fjerde er **varme**. Al den effekt, en satellit ikke omsætter til nyttigt arbejde, ender som spildvarme — og den varme skal væk.

### Køling: den usynlige flaskehals

På Jorden leder man varme bort med luft eller vand. I vakuum findes ingen af delene. Den eneste vej ud er varmestråling: overfladen udsender infrarød stråling ud i rummet, ligesom en glødende kulgløde afgiver varme uden at røre noget. Det virker, men det er langsomt sammenlignet med luftkøling, og det kræver dedikerede **radiatorer** — typisk flade paneler vendt væk fra solen.

Fordi stråling er den eneste kølevej, sætter radiatorernes areal en øvre grænse for, hvor meget effekt en satellit kan bruge uden at blive for varm. Man kan ikke bare hælde flere watt ind i systemet og regne med, at det klarer sig: hver ekstra watt, der bruges, er en ekstra watt, der skal kunne stråles ud igen. Kraftbudgettet på en satellit er derfor en balance mellem produktion, forbrug og bortledning — ikke bare et spørgsmål om at have store nok paneler.

### Formørkelse: batteriets time

I store dele af et kredsløb ser en satellit solen. Men i en del af hver runde går den ind i Jordens skygge — en **formørkelse** (eclipse) — hvor planeten blokerer sollyset. I den periode giver panelerne intet, og alt forbrug skal bæres af batteriet alene.

I lav kredsløbsbane (low Earth orbit, LEO) går det hurtigt. Den Internationale Rumstation kredser om Jorden cirka hvert 90. minut,[^1] hvilket giver i omegnen af 16 kredsløb i døgnet — og dermed op mod 16 formørkelser. Batteriet lades op og aflades igen mange gange dagligt, og over en mission på flere år bliver det til titusinder af cyklusser.

Et almindeligt batteri, som man kender det fra en mobiltelefon, ville være udtjent længe før missionen. Det er grunden til, at batterilevetid i rummet er et **designproblem** snarere end et **indkøbsproblem**: cellekemi, ladestrategi og temperaturstyring skal tilpasses præcis det antal cyklusser, missionen kræver.

### Design til slutningen, ikke til starten

Fordi stråling svækker cellerne gradvist, vil en satellit, der er dimensioneret efter sin effekt ved opsendelsen, ende med for lidt strøm mod slutningen af missionen. Ingeniører designer derfor efter effekten ved missionens *slutning* — den mindste ydelse, panelerne forventes at kunne levere efter år i rummet.

Det betyder, at en ny satellit i praksis har mere strøm til rådighed, end den behøver. Overskuddet er bevidst, bygget ind for at sikre, at den stadig fungerer, når panelerne er blevet ældre og svagere.

### Ikke et elnet

Det er værd at understrege, hvad denne strømforsyning *ikke* er. En satellits solpaneler producerer strøm til satellittens egne systemer. Det har intet at gøre med at sende strøm ned til Jorden.

Idéen om at indfange sollys i kredsløb og stråle det til jordbaserede modtagere er en helt anden skala og en helt anden opgave. Den historie står i [artiklen om orbital solkraft](/kraften/2026-08-nr2/orbital-solkraft).

[^1]: [Space Station Facts and Figures](https://www.nasa.gov/international-space-station/space-station-facts-and-figures/), NASA — om at rumstationen kredser om Jorden cirka hvert 90. minut. Antallet af kredsløb pr. døgn følger af omløbstiden; nøjagtigt hvor mange formørkelser en given satellit oplever, afhænger af dens bane og hældning.
