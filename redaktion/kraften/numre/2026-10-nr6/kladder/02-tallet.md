# Tallet: 72 minutter

To gange om året forsvinder solen bag Jordens skygge for de satellitter, der kredser i **geostationær bane (GEO)** — den bane ca. 35.786\u00a0km over ækvator, hvor en satellit følger Jordens rotation og derfor "står stille" over et fast punkt. I disse perioder — kaldet formørkelsessæsonerne — oplever satellitterne dagligt en mørk periode, der ved jævndøgn topper på **72 minutter**.[^1]

Formørkelsessæsonerne optræder omkring forårs- og efterårsjævndøgn: ca. sidst i februar til midt i april, og igen sidst i august til midt i oktober — hver sæson varer omkring **45 dage**.[^1] Uden for disse vinduer rammer Jordens skygge slet ikke satellitten, fordi geometrien mellem sol, Jord og satellit ikke flugter.

Billedet er et helt andet i **lav jordbane (LEO = low Earth orbit)**, hvor f.eks. Den Internationale Rumstation (ISS) kredser i ca. 400\u00a0km højde. Her tager et helt omløb om Jorden kun ca. 90 minutter — og af dem ligger satellitten i skygge i omkring **30 minutter**.[^2] Det betyder, at ISS oplever solopgang og solnedgang omkring 16 gange i døgnet, mens en GEO-satellit kun formørkes i afgrænsede sæsoner.

| | GEO | LEO (eksempel: ISS) |
|---|---|---|
| Højde | ca. 35.786\u00a0km | ca. 400\u00a0km |
| Omløbstid | ca. 24 timer | ca. 90 minutter |
| Maks. formørkelse | op til 72 minutter/døgn | ca. 30 minutter/omløb |
| Sæson/hyppighed | 2 sæsoner à ca. 45 dage/år | hvert omløb, året rundt |

Den afgørende konsekvens er strømforsyningen. Når solpanelerne ikke rammes af sollys, må satellitten leve af batteri. NOAA's GOES-satellitter (Geostationary Operational Environmental Satellites) er udstyret med batteripakker på 28 celler à 12 amperetimer (**Ah** — et mål for, hvor meget strøm et batteri kan levere over tid), og de er designet til at blive afladet til **60\u00a0% DOD** (depth of discharge, afladningsdybde — hvor stor en andel af batteriets kapacitet der bruges) netop for at klare de 72 minutters mørke uden at nedslide batteriet for hurtigt.[^3]

Forskellen i banehøjde er altså ikke kun et spørgsmål om udsigt — den dikterer, hvor stort et batteri en satellit skal bære med sig, og hvor ofte det skal holde til en fuld afladningscyklus i hele satellittens levetid.

[^1]: NOAA NESDIS, "GOES Eclipse Schedule": https://www.nesdis.noaa.gov/our-satellites/currently-flying/goes-east-west/goes-eclipse-schedule
[^2]: NASA Technical Reports Server, "ISS Electrical Power System" (overview), s. 4-5: https://ntrs.nasa.gov/api/citations/20160014034/downloads/20160014034.pdf
[^3]: NASA Technical Reports Server, rapport om GOES-batterisystem: https://ntrs.nasa.gov/api/citations/19990004147/downloads/19990004147.pdf