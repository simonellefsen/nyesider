# Sådan virker det: Tre etager i rummet

Når vi taler om satellitter, lyder det ofte, som om de alle sammen svæver "deroppe" i én stor, udifferentieret sky. Men rummet omkring Jorden har i praksis tre distinkte "etager", og hvilken etage en satellit bor på, bestemmer stort set alt ved dens job: hvor meget den kan se, hvor hurtigt et signal når frem, og hvor længe skrottet efter den bliver hængende.

## LEO: den travle etage tæt på

**Low Earth Orbit (LEO)**, lav Jordbane, ligger typisk i en højde af omkring 300–2.000 kilometer over jordoverfladen[^1]. Det er tæt på — til sammenligning er Danmarks længste udstrækning nord-syd omkring 450 kilometer. På den højde bevæger en satellit sig meget hurtigt for at undgå at falde ned, og det giver en omløbstid på typisk 90–120 minutter. En satellit i LEO kredser altså om hele kloden op mod 15-16 gange i døgnet.

Det korte svar på, hvorfor lavere bane betyder hurtigere omløb, er tyngdekraften: jo tættere på Jorden, jo stærkere trækker planeten, og jo hurtigere skal satellitten bevæge sig for at holde sig "fritfaldende" i en stabil cirkel i stedet for at styrte ned. Det er samme princip, som gør, at Månen — langt ude i omkring 384.000 kilometers afstand — kun behøver at bruge knap en måned på en omgang.

Den korte afstand til Jorden er også LEO's styrke og svaghed på samme tid. Styrken: lav signalforsinkelse, hvilket er afgørende for internetkonstellationer som Starlink. Svagheden: en enkelt LEO-satellit kan kun "se" et lille stykke af Jorden ad gangen, fordi den er tæt på og hele tiden farer videre. Derfor kræver et globalt dækkende system i LEO tusindvis af satellitter, der afløser hinanden i et konstant relæløb — modsat de tre satellitter, der i princippet kan dække det meste af den beboede klode fra langt højere oppe (se GEO nedenfor).

Endelig er der en praktisk detalje, som gør LEO til den "selvrensende" etage: der er stadig — omend meget tyndt — atmosfære i disse højder. Den skaber atmosfærisk træk, som langsomt bremser satellitter og skrot, så de over år eller årtier taber højde og til sidst brænder op i atmosfæren. Det er derfor, gammelt skrot i lav bane med tiden forsvinder af sig selv, mens intet tilsvarende sker længere ude.

## MEO: GPS' foretrukne højde

**Medium Earth Orbit (MEO)**, mellemhøj Jordbane, er hjemsted for navigationssatellitter som det amerikanske Global Positioning System (GPS), det europæiske Galileo og det russiske GLONASS. GPS-satellitterne kredser i omkring 20.200 kilometers højde[^2], med en omløbstid på omkring 12 timer.

Hvorfor netop denne højde? Navigationssystemer har brug for en balance: satellitten skal være højt nok til, at få satellitter kan dække store dele af kloden samtidig (så en modtager på jorden altid har mindst fire synlige satellitter — et minimumskrav for at beregne position præcist), men ikke så højt, at signalforsinkelsen bliver et problem, og ikke så lavt, at det kræver et LEO-agtigt antal satellitter. MEO er kompromisset, der gør et globalt navigationssystem muligt med nogle få dusin satellitter i stedet for tusindvis.

## GEO: satellitten der står stille

Den tredje etage er **Geostationary Orbit (GEO)**, geostationær bane, i præcis 35.786 kilometers højde over Ækvator[^1]. Her er omløbstiden nøjagtig 24 timer — samme tid, som det tager Jorden at rotere én gang om sin egen akse. Resultatet er, at satellitten "hænger" fast over det samme punkt på Jorden, set fra jordoverfladen. Det er derfor tv-antenner og mange kommunikationsantenner bare kan pege ét fast sted op mod himlen og aldrig behøver at bevæge sig.

Denne stilstand koster noget: afstanden. Et signal, der skal op til en GEO-satellit og ned igen, tilbagelægger over 70.000 kilometer og bruger dermed et kvart sekund eller mere — mærkbart som forsinkelse i for eksempel telefonopkald eller videomøder, og et af de problemer, som LEO-baserede internetsystemer netop forsøger at omgå.

Til gengæld er dækningen enorm: fra GEO kan en satellit se omkring en tredjedel af jordoverfladen, så tre satellitter placeret rigtigt i GEO-bæltet kan tilsammen dække næsten hele den beboede klode — det er hovedårsagen til, at vejrsatellitter og store tv-/kommunikationssatellitter traditionelt sidder her.

I GEO er der stort set ingen atmosfære at tale om, så der er intet atmosfærisk træk til at bremse udtjente satellitter. Skrot herude bliver derfor liggende i praksis for altid, medmindre det aktivt flyttes til en såkaldt "kirkegårdsbane" et stykke længere ude, når det pensioneres.

---

Tre etager, tre kompromiser: LEO giver hastighed og lav forsinkelse på bekostning af antal; MEO giver global navigation med et håndterbart antal satellitter; GEO giver konstant dækning af samme sted på bekostning af signalforsinkelse — og en evighed som skrot, hvis ingen rydder op.

[^1]: European Space Agency (ESA), "Types of orbits" — ESA's forklaring af LEO, MEO og GEO med højdeangivelser.
[^2]: National Coordination Office for Space-Based Positioning, Navigation, and Timing (GPS.gov), "GPS Space Segment" — officiel amerikansk kilde til GPS-satellitternes banehøjde.