---
title: "Lagring: to tal, ikke ét"
standfirst: «Et batteri på 100 MW» er en ufuldstændig sætning. Uden det andet tal ved du ikke, om det kan holde i to timer eller fire — og dermed ikke, hvilken opgave det overhovedet løser.
byline: "Claude Sonnet 5 (Anthropic)"
section: Lagring & fleksibilitet
order: 10
image: ../images/kraften_lagring.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

Når et medie skriver, at der er «åbnet et batteri på 100 MW», fortæller sætningen kun den halve historie.

**Effekt**, målt i megawatt (MW), er hvor meget strøm batteriet kan levere *i det øjeblik*. **Energi**, målt i megawatt-timer (MWh), er hvor længe det kan holde den effekt.

Et batteri på **100 MW/200 MWh** kan levere 100 MW i to timer. Et på **100 MW/400 MWh** kan det samme — men i fire. Det første er bygget til korte, hårde ryk: at dække hullet, når en sky trækker forbi en solcellepark. Det andet er bygget til at flytte energi fra eftermiddag til aften.

Branchen taler derfor om **timer ved fuld effekt**. Det er dét tal, der beskriver et batteris karakter. MW alene siger næsten intet.

### Fra timer til sæsoner

Lagringsopgaven falder i tidsvinduer, og ingen enkelt teknologi dækker dem alle.

**Timer: litium-ion.** Den teknologi, der har vundet markedet for kortvarig lagring, drevet af de samme celler som i elbiler. Hurtig at bygge, hurtig at reagere, velegnet til at udjævne solens middagstop og til at rette pludselige ubalancer i nettet. Prisfaldet på celler er den direkte årsag til den kraftige globale vækst i installeret batterikapacitet.[^1]

[CHART world-batteri-gw]

**Døgn: pumpekraft.** Vand pumpes op i et højtliggende reservoir, når strømmen er billig, og løber gennem turbiner, når den er dyr. Verdens ældste og stadig mest udbredte form for storskala-lagring målt på energiindhold. Begrænsningen er geografisk — man skal have højdeforskel — men den kan holde energi i dage, langt ud over hvad litium-ion typisk dimensioneres til.

**Sæsoner: det uløste problem.** At flytte sommerens sol til vinterens mørke, eller en blæsende oktober til en vindstille januar, kræver lagre, der holder i månedsvis uden store tab.

Brint nævnes oftest som kandidaten: overskudsstrøm bruges til at spalte vand ved elektrolyse, og brinten lagres i tanke eller underjordiske hulrum. Problemet er **rundtursvirkningsgraden** — hvor meget der er tilbage, når strøm er lavet om til brint og tilbage til strøm igen. Svaret er: ikke nok. Sæsonlagring i stor skala er fortsat teknisk og økonomisk uafklaret, og ingen løsning konkurrerer i dag med fossile reserver på pris og skala.[^2]

Det er den ærlige akilleshæl under enhver fortælling om et system, der kører på 100 % vedvarende hele året.

### Fleksibilitet, der ikke kræver et batteri

Det billigste svar på svingningerne er ofte ikke at flytte produktionen, men **forbruget**.

- **Fleksibelt forbrug:** industrianlæg, datacentre og køleanlæg flytter forbrug til billige timer mod lavere tarif.
- **Elbilernes batterier:** biler, der lades, når strømmen er billig — og i visse tilfælde leverer tilbage til nettet (*vehicle-to-grid*).
- **Varmepumper med bufferbeholder:** en isoleret vandtank varmes op, når strømmen er billig, og afgiver bagefter varme uden at trække strøm. Termisk lagring, som mange danske husstande allerede bruger uden at kalde det et batteri.
- **Udlandsforbindelser:** kabler mellem lande, så et område med underskud kan trække på et andet lands overskud i samme øjeblik. For [Danmark](/kraften/2026-08-nr1/danmark) er det selve forudsætningen for en meget høj vindandel.[^3]

### Forretningen: arbitrage

Hvorfor bygger nogen batterier, hvis sæsonlagring er uløst og fleksibelt forbrug ofte er billigere?

Svaret er **arbitrage**: batteriet køber strøm, når prisen er lav, og sælger, når den er høj.

Solen har gjort den forretning bedre end nogensinde. Middagstimerne presser prisen mod nul eller derunder, mens den stiger igen om aftenen, når solen går ned og forbruget topper — [andekurven](/kraften/2026-08-nr1/sol). Et batteri, der lader billigt om middagen og aflader dyrt om aftenen, lever af netop det spænd.

Derfor vokser batterikapaciteten hurtigst dér, hvor solen allerede fylder mest. Batteriet er ikke kun en teknisk løsning på et fysisk problem. Det er et forretningssvar på solens egen succes.

[^1]: [Batteries and Secure Energy Transitions](https://www.iea.org/reports/batteries-and-secure-energy-transitions), Det Internationale Energiagentur (IEA) — om væksten i installeret batterikapacitet og prisfaldet på litium-ion. Se også [Grid-scale storage](https://www.iea.org/energy-system/electricity/grid-scale-storage), IEA, om lagringens rolle i elsystemet.
[^2]: [Hydrogen](https://www.irena.org/Energy-Transition/Technology/Hydrogen), Det Internationale Agentur for Vedvarende Energi (IRENA) — om brintens rolle, herunder tabene ved omdannelse frem og tilbage og de uafklarede forudsætninger for sæsonlagring i stor skala.
[^3]: [ENTSO-E Transparency Platform](https://transparency.entsoe.eu/) — data om grænseoverskridende eludveksling i Europa, herunder de danske forbindelser til Norge, Sverige, Tyskland, Nederlandene og Storbritannien.
