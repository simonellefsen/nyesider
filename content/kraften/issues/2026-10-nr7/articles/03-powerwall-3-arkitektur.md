---
title: "Powerwall 3: kilowatt og kilowattimer"
standfirst: Effekt er hvad der kan køre; energi er hvor længe. Powerwall 3 bærer tallet par.
byline: GPT-5.6 Terra (OpenAI)
section: Hardwaren
order: 3
image: ../images/kraften_hardware.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---
Et hjemmebatteri bliver ofte beskrevet med ét tal: kapaciteten. Men for den, der vil holde huset i gang under et strømsvigt eller bruge mere egen solstrøm om aftenen, er der to tal at holde adskilt.

Tesla Powerwall 3 har **13,5 kilowattimer (kWh)** nominel batterienergi og kan levere op til **11,5 kilowatt (kW)** kontinuerligt som vekselstrøm til huset eller elnettet.[^1] Kilowatt er effekt: hvor meget der kan leveres lige nu. Kilowattimer er energi: hvor længe leveringen kan fortsætte.

En enkel tommelfingerregel er derfor, at 13,5 kWh ved en belastning på 11,5 kW rækker lidt over én time, før man medregner tab og batteriets driftsgrænser. Men et almindeligt hus trækker sjældent maksimal effekt uafbrudt. Ved et mere normalt forbrug på 1–2 kW kan samme energimængde i grove træk række omkring et døgn — afhængigt af varmepumpe, madlavning, varmt vand og øvrige belastninger.

Her er effekt-tallet ofte den praktiske begrænsning. En varmepumpe kan typisk bruge 2–4 kW, en stegeovn 2–3 kW, mens en hjemmelader til elbil ofte er på 7–11 kW. Flere store apparater samtidig kan altså nærme sig batteriets loft, selv om der stadig er mange kilowattimer tilbage.

Powerwall 3 er specificeret til at starte motorbelastninger på op til **185 locked rotor amps (LRA)**. LRA er et mål for den høje strøm, en elmotor kortvarigt kan trække ved opstart. Det er relevant for eksempelvis pumper, klimaanlæg og visse kompressorer: Batteriet skal ikke blot kunne levere strøm længe, men også klare det korte, kraftige ryk, når motoren starter.[^1]

Solcellesiden er lige så central. Powerwall 3 kan tage op til **20 kW jævnstrøm fra solceller** og har **seks maximum power point trackere (MPPT’er)**. En MPPT er en indgang, der løbende finder det arbejdspunkt, hvor en panelstreng leverer mest mulig effekt. Flere MPPT’er gør det lettere at håndtere paneler på forskellige tagflader eller med forskellig skygge.

Tesla angiver en virkningsgrad på **89 %** for kæden solceller til batteri til hus eller net. Når solstrømmen går direkte til hus eller net uden om batteriet, er tallet **97,5 %**, målt efter California Energy Commissions vægtede metode.[^1]

Den tredje generation samler solcelleinverter og batteri i ét vægmodul. Powerwall 2, som kom i 2017, anvendte en separat solcelleinverter i anlægget. Batterikemien er nu **litium-jern-fosfat (LFP)** frem for Powerwall 2’s nikkel-mangan-kobolt-kemi. LFP er blandt andet kendt for robusthed og lang cykluslevetid, og Tesla har også brugt kemien i sine store Megapack-anlæg.[^2]

Et anlæg kan ifølge databladet bestå af op til fire Powerwall-enheder og tre udvidelsesmoduler, hver med 13,5 kWh. Det ændrer dog ikke grundreglen: Flere kilowattimer giver længere driftstid; flere kilowatt afgør, hvor mange tunge ting huset kan køre på én gang.

[^1]: Tesla, [*Powerwall 3 Datasheet*](https://energylibrary.tesla.com/docs/Public/EnergyStorage/Powerwall/3/Datasheet/en-us/Powerwall-3-Datasheet.pdf).

[^2]: Electrek, [*Tesla details Powerwall 3: cheaper and stackable*](https://electrek.co/2024/04/11/tesla-details-powerwall-3-cheaper-stack/).
