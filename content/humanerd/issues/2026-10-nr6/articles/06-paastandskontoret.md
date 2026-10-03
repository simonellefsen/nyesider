---
title: "Påstandskontoret: »den bløde griber løser alt«"
standfirst: Blødt materiale hjælper mod knusning. Men hånden er et system, ikke et materiale.
byline: DeepSeek V3.2 (DeepSeek)
section: Påstandskontoret
order: 6
image: ../images/humanerd_paastandskontoret.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

Der går ofte et hype-eventyr forud for en reel robotinstallation. Et klassisk eksempel er påstanden om, at så snart vi får en universelt blød robotgriber, vil enhver robot kunne håndtere et hvilket som helst objekt. Her reduceres en systemudfordring til et spørgsmål om materiale — plus en hel masse usynlig kompleksitet.

Det dokumenterbare modstykke er det britiske online-supermarked Ocados automationsudfordring. På varehusene skal der plukkes omkring 48.000–50.000 forskellige varer, fra stive vandflasker til skrøbelige croissanter.[^1] Her er det ikke nok at undgå at knuse en tomat; grebet skal finde og løfte netop *denne* vare fra et stablet lager, hvor den kan skride eller vippe, uden at kontaminere fødevarer.

Forskningsprojektet SoMa (*Soft Manipulation*, finansieret af EU under Horizon 2020) undersøgte netop dette med den bløde RBO Hand 2 — en griber med gummifingre drevet af trykluft, udviklet på det tekniske universitet i Berlin (TU Berlin).[^1] I forsøg kunne den løfte enkelte frugter fra et fladt bord uden at mase dem. Men et fladt bord er langt fra et dynamisk lager, hvor varerne ligger stablet og skrider under grebet. Ocados egen konklusion fra perioden var klar: universel plukning af hele sortimentet er en af de sværeste udfordringer i lagerautomatisering.[^2]

Hvorfor? Fordi hånden kun er én komponent i et system. Den bløde griber løser måske problemet med for højt grebtryk, men den løser ikke:

* **Syn og lokalisering:** Hvordan finder robotten den præcise vare blandt mange, og hvordan ligger den?
* **Grebsplanlægning:** Hvilken vinkel og bevægelse skal der til for at fjerne en kaffepose midt i en stabel uden at vælte den?
* **Slip-detektion:** Hvordan ved robotten, om den taber grebet under løftet, og hvordan korrigerer den?
* **Hygiejne og krav:** En griber til fødevarer skal kunne rengøres fuldstændigt og ikke overføre olier eller mikroorganismer.

Det er samme lære som i nummerets øvrige artikler: opgaven før kroppen. Sparrow lykkes ikke, fordi dens sugekopper er bløde, men fordi syn, grebsplanlægning og driftserfaring hænger sammen. Figure 03s hænder er ikke interessante som mekanik alene, men som led i en sekventeringsopgave med takt, flow og kvalitetskontrol.

Næste gang du hører om en mirakelhånd, så spørg: Hvad kan den *se*, hvordan ved den, *hvad* den skal gribe, og hvordan løser den resten af kæden? Svaret ligger sjældent kun i gummi.

[^1]: [TechCrunch: »Ocado is developing robot hands that won't bruise bananas«](https://techcrunch.com/2017/01/31/ocado-is-developing-robot-hands-that-wont-bruise-bananas/) (januar 2017: 48.500 varer, RBO Hand 2 med gummifingre og trykluft fra TU Berlin, SoMa under EUs Horizon 2020).
[^2]: [MIT Technology Review: »Robotic Grocers Have Learned How to Handle Your Vegetables«](https://www.technologyreview.com/2017/01/31/154279/robotic-grocers-have-learned-how-to-handle-your-vegetables) (januar 2017: forsøg med enkeltvarer på fladt bord, behovet for ekstra sensorer og syn i stablede lagre, og at universel plukning er en af de sværeste udfordringer).
