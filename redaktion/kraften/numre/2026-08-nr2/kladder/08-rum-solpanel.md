# Sådan virker det: en satellits strømforsyning

En satellit i kredsløb om Jorden har ingen stikkontakt at ty til. Alt strøm, den bruger — til radioer, computere, instrumenter og varme — skal produceres om bord, lagres om bord og bruges op om bord. Løsningen er næsten altid den samme: solpaneler, der omdanner sollys til elektricitet, og batterier, der bærer satellitten gennem de perioder, hvor solen er væk. Princippet er simpelt. Det, der gør det svært, er fire faktorer, som alle trækker i hver sin retning.

## Fire ting bestemmer watt-tallet

Den første er **arealet** af solpanelerne. Flere kvadratmeter celler giver flere watt, men areal koster masse, og masse koster plads på raketten og penge i opsendelsen. Ingen satellit har mere panel, end den absolut må have.

Den anden er **retning**: hvor godt panelerne peger mod solen. En flad plade, der står vinkelret på sollyset, høster mest; drejer den bare lidt væk, falder udbyttet. Mange satellitter har derfor motoriserede paneler, der roterer for konstant at følge solen, mens selve satellitten peger sine instrumenter et andet sted hen.

Den tredje er **stråling** (radiation) — ladede partikler fra solen og Jordens magnetfelt, der år for år nedbryder solcellernes krystalstruktur. En celle, der er ny, yder mere end den samme celle efter nogle års eksponering. Det er en gradvis, uafvendelig aldring, ikke en fejl.

Den fjerde er **varme**. Al den effekt, en satellit ikke omsætter til nyttigt arbejde, ender som spildvarme et sted i systemet — og den varme skal væk.

## Køling: den usynlige flaskehals

På Jorden leder man varme bort med luft eller vand. I vakuum findes ingen af de to. Den eneste vej ud for en satellit er **stråling** i termodynamisk forstand: overfladen udsender infrarød varmestråling ud i rummet, ligesom en rødglødende kul­gløde stråler varme uden at røre noget. Det virker, men det er langsomt i forhold til luftkøling, og det kræver dedikerede **radiatorer** — typisk flade, sortmalede paneler vendt væk fra solen.

Fordi stråling er den eneste kølingsvej, sætter radiatorernes areal en øvre grænse for, hvor meget effekt en satellit kan bruge, uden at blive for varm. Man kan ikke bare hælde flere watt ind i et system og regne med, at det klarer sig — hver ekstra watt, der skal bruges, er en ekstra watt, der skal kunne stråles ud igen. Det er derfor, kraftbudgettet på en satellit er en balance mellem produktion, forbrug og bortledning, ikke bare et spørgsmål om at have store nok solpaneler.

## Formørkelse: batteriets time

I store dele af et kredsløb ser en satellit solen. Men i en del af hver runde omkring Jorden går satellitten ind i Jordens skygge — en **formørkelse** (eclipse) — hvor planeten selv blokerer sollyset. I denne periode giver solpanelerne intet, og alt strømforbrug skal bæres af batteriet alene.

I lav bane om Jorden (low Earth orbit, LEO), hvor mange observations- og kommunikationssatellitter samt Den Internationale Rumstation (International Space Station, ISS) befinder sig, går kredsløbet så hurtigt, at satellitten kan opleve formørkelse op mod 16 gange i døgnet¹. Det betyder, at batteriet lades op og aflades igen mange gange dagligt — og over en mission på flere år bliver det til titusinder af cyklusser. Almindelige batterier, som man kender dem fra en mobiltelefon, ville være udtjente lang tid før missionen er slut. Det er grunden til, at batterilevetid på en satellit er et **designproblem** frem for et **indkøbsproblem**: man kan ikke bare købe et større batteri og forvente, det holder — cellekemi, ladestrategi og temperaturstyring skal tilpasses netop det antal cyklusser, missionen kræver.

## Design til slutningen, ikke til starten

Fordi stråling svækker solcellerne gradvist, vil en satellit, der er dimensioneret efter sin effekt ved opsendelsen, ende med for lidt strøm mod slutningen af missionen. Ingeniører designer derfor efter **end-of-life**-effekten: den mindste ydelse, panelerne forventes at kunne levere efter years i rummet, med den nedbrydning stråling har forårsaget. Det betyder, at en ny satellit i praksis har mere strøm til rådighed, end den behøver — et bevidst overskud, bygget ind for at sikre, at den stadig fungerer, når panelerne er blevet ældre og svagere.

## Ikke et elnet

Det er værd at understrege, hvad denne strømforsyning *ikke* er. En satellits solpaneler producerer strøm til satellittens egne systemer — typisk i størrelsesordenen nogle hundrede watt til nogle kilowatt, afhængigt af missionstype. Det har intet at gøre med at sende strøm ned til Jorden. Idéen om at indfange sollys i rummet og stråle det til jordbaserede modtagere — orbital solkraft — er en helt anden skala og en helt anden opgave, med sine egne udfordringer omkring overførsel og effektivitet. Den historie fortælles særskilt.

---

¹ NASA, *International Space Station*, oplysninger om ISS' kredsløbsperiode og antal solopgange/nedgange pr. døgn: https://www.nasa.gov/international-space-station/