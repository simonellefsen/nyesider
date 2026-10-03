---
title: "Den usynlige hjerne bag rummets kraftværker"
standfirst: Paneler og batterier er kun så gode som den computer, der prioriterer mellem dem.
byline: Gemini 3.1 Pro Preview (Google)
section: Styringen
order: 5
image: ../images/kraften_styring.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

Solpaneler og batterier får al opmærksomheden, når talen falder på satellitter. Men de store, skinnende vinger er ubrugelige uden den logik, der binder dem sammen. Strømstyring er den usynlige halvdel af al rumkraft.

Hjertet i styringen kaldes **EPS** (*electric power system*, satellittens elsystem). Uden et velkalibreret elsystem ville en satellit hurtigt tømmes for strøm i mørket eller overbelaste sine kredsløb i sollyset.

I **lav jordbane (LEO — *low Earth orbit*)** er vilkårene brutale. Et omløb for Den Internationale Rumstation (**ISS** — *International Space Station*) tager cirka 90 minutter, og heraf ligger stationen omkring 30 minutter i formørkelse. Her forsvinder solenergien på et splitsekund, og batterierne skal øjeblikkeligt levere hele den elektriske last.[^1]

Når stationen atter træder ud i sollyset, sker et nyt, voldsomt skift. Rumstationens **BCDU** (*battery charge/discharge unit*, laderegulatoren) styrer overgangen, så forsyningen lynhurtigt skifter tilbage til solpanelerne. Samtidig sørger en pegealgoritme for, at panelerne aktivt rettes mod Solen for at maksimere effekten — så de både driver stationens systemer og lader batterierne op til næste formørkelse.[^1] Det sker automatisk adskillige gange i døgnet.

Længere ude, i **geostationær bane (GEO — *geostationary orbit*)**, er hverdagen en anden. Her ligger blandt andet de amerikanske GOES-vejrsatellitter (*Geostationary Operational Environmental Satellites*). Det meste af året er de badet i sollys, men i formørkelsessæsonerne forår og efterår glider de dagligt ind i Jordens skygge og må køre udelukkende på batterier i op til 72 minutter pr. døgn.[^2]

For at holde en nominel last på 1.150 watt (**W**) i de mørke perioder kræves hård prioritering: instrumenter drosles ned eller slukkes midlertidigt efter faste, forprogrammerede regler, så batterierne ikke drænes for hurtigt.[^3]

Denne styring bygger på tabeller for såkaldt *load shedding* — planlagt afbrydelse af ikke-kritiske laster. EPS-computeren overvåger hele tiden nettet og står for fejlisolering: registrerer en sensor f.eks. en kortslutning i et instrument, griber systemet ind med elektroniske afbrydere, og den fejlramte zone isoleres, før et svigt spreder sig.[^1]

Skulle batterispændingen alligevel falde mod det kritiske, har elsystemet et sidste værn: *safe mode* (sikkerhedstilstand, hvor satellitten ofrer missionen for at redde sig selv). Alle forskningsinstrumenter slukkes, og den sparsomme restenergi bruges kun på at holde hovedcomputeren i live, pege panelerne mod Solen og holde forbindelsen til Jorden åben.

I mørket er strømstyring ikke blot et spørgsmål om at levere watt; det er forudsætningen for overlevelse.

[^1]: NASA Technical Reports Server, *Space Station Electrical Power System*: https://ntrs.nasa.gov/api/citations/20160014034/downloads/20160014034.pdf
[^2]: NOAA, GOES Eclipse Seasons: https://www.ospo.noaa.gov/operations/goes/eclipse.html
[^3]: NASA Technical Reports Server, GOES I-M Power System Limits and Operations: https://ntrs.nasa.gov/api/citations/19990004147/downloads/19990004147.pdf
