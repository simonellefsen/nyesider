# Sådan virker det: at holde øje med rummet

Et satellitkatalog ser bedragerisk præcist ud. Ud for hvert objekt står et nummer, en bane, en position. Men bag hver af de linjer gemmer sig en sandhed, som er værd at forstå, hvis man vil forstå debatten om rumskrot: en position i et katalog er aldrig en position. Den er et estimat med en usikkerhed omkring sig.

## Tre instrumenter, tre afstande

Arbejdet med at vide, hvad der er i kredsløb, og hvor det er på vej hen, kaldes space situational awareness (SSA), på dansk rumsituationsbillede. Det hviler på tre grundlæggende typer sensorer, og valget mellem dem handler først og fremmest om afstand.

**Radar** bruges til lav kredsløbsbane (Low Earth Orbit, LEO), typisk under omkring 2.000 km. En radar sender selv sin energi ud og lytter efter ekkoet. Fordi den udsendte styrke falder dramatisk med afstanden — energien spredes over en stadig større kugleflade på vej ud *og* på vej tilbage — bliver radar hurtigt for svag langt væk. Til gengæld virker den døgnet rundt, uanset om objektet er belyst, fordi den leverer sit eget lys.

**Optiske teleskoper** bruges til de høje baner, herunder geostationær bane (Geostationary Orbit, GEO) i cirka 36.000 km højde. Her ser teleskopet ikke objektet selv, men det sollys, objektet reflekterer. Det giver en afgørende begrænsning: en optisk observation kan kun foretages i det korte tidsrum, hvor objektet er solbelyst, mens observatøren nede på jorden står i mørke. Det sker i skumringstimerne efter solnedgang og før solopgang. Er observatøren i dagslys, drukner objektet i himmelbaggrunden; er objektet selv i Jordens skygge, reflekterer det intet.

**Laserafstandsmåling** (Satellite Laser Ranging, SLR) er den mest præcise metode, men den kan kun bruges på de objekter, der bærer retroreflektorer — særlige spejle, der sender laserlyset præcist tilbage mod afsenderen. Man måler, hvor lang tid lyset er om at rejse frem og tilbage, og får afstanden på centimeterniveau. Det er derfor mest et redskab til udvalgte, samarbejdende satellitter, ikke til tilfældigt skrot.

## Hvorfor kataloget altid er et skøn

Her er kernen. Et objekt observeres kun få gange i døgnet — en radar eller et teleskop får det i syne, når banen fører det hen over sensoren. Mellem observationerne *beregnes* banen frem ved hjælp af fysiske modeller. Og fra det øjeblik den sidste observation er lavet, begynder usikkerheden at vokse.

Den vokser hurtigst i lav bane. Her rager den øverste, tynde atmosfære stadig op og bremser objektet — men bremsningen afhænger af, hvor tæt atmosfæren er netop dér, og det svinger med soltiden. Når Solen opvarmer den øvre atmosfære, udvider den sig, og modstanden ændrer sig. Da man ikke kender den fremtidige soltid præcist, kan man ikke forudsige bremsningen præcist. Resultatet er, at det beregnede punkt bliver til en langstrakt "sky" af mulige positioner — størst langs banen.

Derfor angives risiko for et sammenstød aldrig som et ja eller nej, men som en sandsynlighed. To usikkerhedsskyer, der overlapper, giver en kollisionssandsynlighed — et tal, en operatør må afveje, før beslutningen om at bruge brændstof på en undvigelsesmanøvre tages.

## Hvad tallene siger

ESA's Space Debris Office opgør billedet sådan (opdateret 31. juli 2026): cirka **46.230 objekter** følges regelmæssigt og står i kataloget. Men modeller anslår langt flere. Der skønnes at være omkring **54.000 objekter over 10 cm**, cirka **1,2 millioner mellem 1 cm og 10 cm** og i størrelsesordenen 140 millioner mellem 1 mm og 1 cm.[^1][^2]

Pointen med de tal er ubehagelig, men vigtig: kun den første kategori — det, der faktisk er katalogiseret — kan man undvige. Man kan ikke manøvrere uden om noget, ingen kan se. Og selv en flage på få centimeter rammer i kredsløbshastighed med en energi, der kan ødelægge en satellit. Mod de små, usynlige partikler er svaret derfor ikke undvigelse, men afskærmning (skjolde, der optager anslaget) og redundans (dobbelte systemer, så ét gennemslag ikke slår hele satellitten ud).

## Hvorfor opgaven bliver sværere

Til sidst en matematisk grund til bekymring. Antallet af mulige sammenstød afhænger ikke af antallet af objekter, men af antallet af *par* af objekter. Fordobler man antallet af satellitter i lav bane, firdobler man groft sagt antallet af mulige møder. Med de mange nye konstellationer i LEO vokser antallet af par — og dermed arbejdsbyrden for dem, der overvåger — hurtigere end antallet af objekter selv.

Det er derfor SSA ikke bare handler om at bygge flere radarer. Det handler om at leve med usikkerhed, sætte tal på den og træffe beslutninger, før skyerne overlapper.

[^1]: ESA Space Debris Office, "Space debris by the numbers" (opdateret 31. juli 2026). Tilgængelig via ESA's websted, esa.int.
[^2]: ESA Annual Space Environment Report, European Space Agency — Space Debris Office. Publiceres årligt af ESA.