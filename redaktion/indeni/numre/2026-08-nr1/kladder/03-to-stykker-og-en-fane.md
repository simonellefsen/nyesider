# Maskinen: Dåsen, der bliver til under træk

En tom sodavandsdåse vejer omkring 13-14 gram og er sat sammen af to dele: en krop med bund i ét stykke aluminium, og et separat låg med oplukkerfanen. Det er derfor den kaldes en **to-delt dåse** (two-piece can) — i modsætning til ældre dåsetyper, hvor krop, bund og låg var tre separate stykker, der skulle svejses eller loddes sammen. Nutidens dåsekrop er hverken støbt eller svejst. Den er formet — presset og trukket ud af en flad plade, indtil metallet sidder, hvor det skal, uden en eneste søm nedad langs siden.

Rejsen fra plade til dåse foregår i to maskiner, der arbejder lige efter hinanden på samme produktionslinje.

## Fra plade til kop

Aluminiumspladen, der ankommer på coils til dåsefabrikken, er omkring 250 mikrometer tyk — en mikrometer er en tusindedel af en millimeter, så pladen svarer nogenlunde til tykkelsen af to-tre stykker almindeligt printerpapir oven på hinanden. Den første maskine, **cupperen**, er i bund og grund en udstansepresse: et stempel skærer en rund, flad skive ud af pladen og trykker den samtidig ned i en formhulning, så skiven bliver til en lav, bred kop — lidt som en dyb underkop. På dette stadie er koppens vægge stadig næsten lige så tykke som den oprindelige plade.

## Bodymakeren: tre træk gennem ringe

Koppen sendes videre til **bodymakeren**, den maskine, der reelt skaber dåsens endelige form. Her sker to ting efter hinanden. Først genudtrækkes koppen (redraw) — den bliver smallere og lidt højere, så diameteren passer til den færdige dåse. Derefter presses koppen gennem en serie stramme metalringe i tre trin. Hvert ringpassage strækker og forlænger sidevæggen, samtidig med at den bliver tyndere — processen kaldes ironing, fordi metallet i praksis "stryges" tyndt, ligesom en strygejern-lignende bevægelse, men her drevet af mekanisk kraft i stedet for varme. Efter de tre strækketrin er sidevæggen nede på cirka 0,094-0,100 millimeter på det tyndeste sted — tyndere end to menneskehår lagt ved siden af hinanden. Bunden af dåsen forbliver derimod tykkere, fordi den skal holde til at blive presset op i den hvælvede form (dome), der giver dåsen stabilitet, når den står på en flad overflade under indre tryk.

Hele forløbet — cupning, genudtrækning og tre strækketrin — sker på under et sekund per dåse, og en moderne linje kan producere flere hundrede dåser i minuttet.¹

## Hvorfor låget er en anden legering

Låget bliver ikke lavet i bodymakeren. Det stanses separat ud af en anden, hårdere aluminiumslegering end kroppen — typisk en legering med et højere indhold af magnesium, mens kropslegeringen har mere mangan.² Grunden er belastningen: låget skal holde til det indre tryk fra den kulsyreholdige drik, det skal danne den bøjede fold, der senere krympes fast på kroppen, og det skal bære oplukkerfanen (tab), som brugeren trækker op. Kroppens legering er valgt til at kunne trækkes og strækkes ekstremt tyndt uden at revne undervejs i bodymakeren — en egenskab, der ikke nødvendigvis går hånd i hånd med den styrke, låget har brug for. Derfor er det to forskellige materialer, selv om begge dele ser ens ud og begge er aluminium.

## Hvor kredsløbet knækker

Det tyndeste punkt i hele dåsen er sidevæggen lige der, hvor det tredje strækketrin slutter. Er legeringens sammensætning, pladens oprindelige tykkelse eller ringenes justering en anelse forkert, opstår der ikke en jævn udtynding, men lokale svage punkter — og resultatet er en revne, ofte usynlig for øjet ved produktionen, som først viser sig som en utæt eller bulet dåse efter fyldning, når det indre tryk fra kulsyren presser på metallet. Producenter tester derfor løbende vægtykkelsen med ultralyd eller vekselstrømsmålinger under produktionen, fordi en fejl her ikke kan rettes bagefter — dåsen er allerede formet.³

---

¹ Can Manufacturers Institute (CMI), "How a Can is Made", cancentral.com

² The Aluminum Association, aluminum.org — materiale om legeringstyper til dåsekroppe (typisk 3xxx-serien) og dåselåg (typisk 5xxx-serien)

³ European Aluminium, european-aluminium.eu — brancheoplysninger om kvalitetskontrol og materialeforbrug i aluminiumsemballage

<svg viewBox="0 0 900 320" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <!-- baseline -->
  <line x1="20" y1="280" x2="880" y2="280" stroke="#999" stroke-width="1"/>

  <!-- 1: blank -->
  <ellipse cx="90" cy="240" rx="45" ry="10" fill="#c9d6e3" stroke="#333"/>
  <text x="90" y="270" font-size="13" text-anchor="middle">Udstanset skive</text>
  <text x="90" y="286" font-size="11" text-anchor="middle" fill="#555">~250 μm</text>

  <!-- arrow -->
  <line x1="150" y1="240" x2="200" y2="240" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- 2: cup -->
  <path d="M 220 240 L 220 200 L 250 190 L 280 200 L 280 240 Z" fill="#c9d6e3" stroke="#333"/>
  <text x="250" y="270" font-size="13" text-anchor="middle">Kop (cupper)</text>
  <text x="250" y="286" font-size="11" text-anchor="middle" fill="#555">væg ≈ plade</text>

  <line x1="300" y1="220" x2="350" y2="220" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- 3: redraw -->
  <path d="M 370 240 L 370 180 L 395 165 L 420 180 L 420 240 Z" fill="#b7c9dc" stroke="#333"/>
  <text x="395" y="270" font-size="13" text-anchor="middle">Genudtrukket</text>
  <text x="395" y="286" font-size="11" text-anchor="middle" fill="#555">smallere, højere</text>

  <line x1="440" y1="200" x2="480" y2="200" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- ironing rings 1-3 -->
  <g>
    <path d="M 500 240 L 500 150 L 515 140 L 530 150 L 530 240 Z" fill="#a5bcd4" stroke="#333"/>
    <rect x="495" y="150" width="40" height="6" fill="#333"/>
    <text x="515" y="270" font-size="12" text-anchor="middle">Ring 1</text>
  </g>

  <line x1="545" y1="190" x2="575" y2="190" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>

  <g>
    <path d="M 590 240 L 590 120 L 601 112 L 612 120 L 612 240 Z" fill="#94b0cc" stroke="#333"/>
    <rect x="586" y="120" width="30" height="5" fill="#333"/>
    <text x="601" y="270" font-size="12" text-anchor="middle">Ring 2</text>
  </g>

  <line x1="625" y1="170" x2="655" y2="170" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>

  <g>
    <path d="M 670 240 L 670 90 L 679 84 L 688 90 L 688 240 Z" fill="#7f9fc0" stroke="#333"/>
    <rect x="666" y="90" width="26" height="4" fill="#333"/>
    <text x="679" y="270" font-size="12" text-anchor="middle">Ring 3</text>
    <text x="679" y="286" font-size="11" text-anchor="middle" fill="#555">0,094-0,100 mm</text>
  </g>

  <line x1="700" y1="150" x2="740" y2="150" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- final can with lid -->
  <g>
    <path d="M 760 240 L 760 90 L 769 84 L 778 90 L 778 240 Z" fill="#6f90b3" stroke="#333"/>
    <ellipse cx="769" cy="84" rx="12" ry="4" fill="#d9c98a" stroke="#333"/>
    <text x="769" y="270" font-size="12" text-anchor="middle">Færdig krop</text>
    <text x="769" y="286" font-size="11" text-anchor="middle" fill="#555">+ separat låg</text>
  </g>

  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="#333"/>
    </marker>
  </defs>
</svg>