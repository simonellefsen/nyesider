# Den usynlige hjerne bag rummets kraftværker

Solpaneler og batterier får ofte al opmærksomheden, når talen falder på satellitter og rumstationer. Men de store, skinnende vinger er reelt ubrugelige uden den logik, der binder dem sammen. Strømstyring er den usynlige halvdel af al rumkraft. Paneler og batterier er i sidste ende kun så gode som den computer, der prioriterer mellem dem.

Hjertet i denne styring kaldes et Electric Power System (EPS). Uden et velkalibreret elsystem ville en satellit hurtigt tømmes for strøm i mørket eller overbelaste sine kredsløb i solen.

I lavt jordkredsløb, Low Earth Orbit (LEO), er vilkårene og kravene til strømstyringen brutale. Et omløb for Den Internationale Rumstation (ISS) tager cirka 90 minutter. Ud af dette tidsrum tilbringer stationen i omegnen af 30 minutter i total formørkelse, når den bevæger sig ind i Jordens skygge. Her forsvinder solenergien på et splitsekund, og batterierne skal øjeblikkeligt levere hele den elektriske last.[^1]

Når stationen atter træder ud i sollyset, sker der et nyt, voldsomt skift. Her aktiveres rumstationens Battery Charge/Discharge Unit (BCDU). Denne laderegulator styrer overgangen, så strømforsyningen lynhurtigt skifter tilbage til solpanelerne. Samtidig sørger en indbygget pegealgoritme for, at panelerne aktivt rettes mod Solen for at maksimere den indfangede effekt. Herved kan de både drive stationens mange systemer og lade batterierne helt op til den næste formørkelse.[^1] Alt dette sker automatisk adskillige gange i døgnet.

Længere ude i rummet, i det geostationære kredsløb, Geostationary Earth Orbit (GEO), er hverdagen en anden for strømstyringen. Herude finder vi blandt andet de amerikanske GOES-vejrsatellitter. Fordi banen er markant anderledes, er satellitterne badet i sollys det meste af året. Men under de såkaldte formørkelsessæsoner om foråret og efteråret glider de dagligt ind i Jordens skygge. Her må satellitterne køre udelukkende på batterier i op til 72 minutter pr. døgn.[^2]

For at bevare strømmen til en nominel last på 1150 W under disse mørke perioder, kræves der hård prioritering. Instrumenter drosles ned eller slukkes midlertidigt efter strikse, forprogrammerede regler, så batterierne ikke drænes for hurtigt.[^3]

Denne type strømstyring bygger på sirlige tabeller for såkaldt load shedding — en planlagt afbrydelse af ikke-kritiske laster for at aflaste elnettet. EPS-computeren overvåger konstant netværket for uregelmæssigheder og har ansvaret for fejlisolering. Hvis en sensor for eksempel registrerer en kortslutning i et instrument, griber systemet ind med elektroniske afbrydere og sikringer. Den fejlramte zone isoleres fra nettet, længe før et strømsvigt kan sprede sig til resten af fartøjet.[^1]

Skulle situationen alligevel eskalere, og batterispændingen falde mod det kritiske, har elsystemet et absolut sidste værn: safe mode. Dette er en sikkerhedstilstand, hvor satellitten kynisk ofrer sin videnskabelige mission for at redde strømmen og dermed sig selv. I safe mode slukkes alle forskningsinstrumenter og sekundære systemer. Den sparsomme rest af energi bruges udelukkende på at holde hovedcomputeren i live, at pege solpanelerne mod Solen og at holde kommunikationslinjen til Jorden åben.

Ude i mørket er strømstyring ikke blot et spørgsmål om at levere watt; det er forudsætningen for overlevelse.

[^1]: [NASA Technical Reports Server: Space Station Electrical Power System](https://ntrs.nasa.gov/api/citations/20160014034/downloads/20160014034.pdf)
[^2]: [NOAA: GOES Eclipse Seasons](https://www.ospo.noaa.gov/operations/goes/eclipse.html)
[^3]: [NASA Technical Reports Server: GOES I-M Power System Limits and Operations](https://ntrs.nasa.gov/api/citations/19990004147/downloads/19990004147.pdf)