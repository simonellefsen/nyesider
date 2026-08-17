# Robotten, der ikke løfter noget — den tæller

**FABRIKKEN**

Den 16. juni 2026 uddelte International Federation of Robotics (IFR) sammen med IEEE's robotselskab (IEEE Robotics and Automation Society) prisen IERA — «Award for Innovation and Entrepreneurship in Robotics & Automation» — til det schweiziske selskab Verity.[^1] Begrundelsen handlede ikke om en robot, der bygger biler eller flytter paller. Den handlede om droner, der flyver rundt inde i lagerhaller og tæller, hvad der står på hylderne.

Det er et godt sted at begynde, fordi det tvinger os til at stille HumaNerds faste første spørgsmål: Hvad er egentlig opgaven?

## Opgaven er ikke at flytte — det er at vide

Når man forestiller sig en lagerrobot, tænker man på noget, der løfter. Men ifølge IFR er det største problem i et moderne lager ikke at flytte varer. Det er at vide, hvor de befinder sig. IFR beskriver situationen sådan: i et lager kan varerne være fordelt på tusindvis af lagerpladser og blive flyttet rundt hele dagen. Branchen har høj personaleomsætning og stramme omkostninger, og en løbende, manuel optælling ville i praksis ikke være mulig.[^1]

Konsekvensen er, at varer bliver forlagt. En palle stilles det forkerte sted, registreres ikke — og forsvinder reelt fra systemet, selv om den fysisk står få meter væk. Ifølge IFR er netop dét, Verity-systemet er bygget til at fange: ved at genfinde en forlagt vare — for eksempel en fuldt lastet palle — sparer systemet penge, der ellers skulle afskrives.[^1]

Med andre ord: den mest værdifulde robot i et lager i 2026 er måske ikke den, der løfter noget. Det er den, der ved, hvor tingene er.

## Hvorfor en drone — og ikke en gaffeltruck?

Her bliver geometrien interessant. Et lager bruger højden til opbevaring: reoler i mange etager, ofte flere meter op. Men gulvet — den ene dimension, hvor en gaffeltruck kan bevæge sig — er kun en brøkdel af rummet. En drone kan flyve derop, hvor trucken ikke kan køre, og læse stregkoder på de øverste hylder uden lift eller stige.

Ifølge IFR navigerer dronerne selv gennem reolgangene, scanner stregkoder og vender tilbage til deres ladestationer. Det sker uden GPS (satellitpositionering, som ikke virker indendørs) og uden menneskelig indgriben.[^1]

At systemet er **autonomt** betyder her, at hver enkelt drone selv håndterer det, der ellers ville kræve en pilot: den opfatter sine omgivelser (perception), planlægger sin bevægelse og undviger forhindringer — og al den beregning foregår om bord i realtid. En **flåde** er den samlede gruppe droner, der arbejder i samme lager eller på tværs af flere lagre. Ifølge IFR knytter en central, skybaseret platform flåderne sammen og sørger for løbende læring på tværs af dem. Stregkodedataene sendes direkte ind i lagerstyringssystemet (WMS, Warehouse Management System), og uoverensstemmelser bliver identificeret og rapporteret.[^1]

## Tallene — som IFR opgiver dem

Det er værd at understrege, at følgende tal stammer fra IFR's pressemeddelelse om prisvinderen og altså er gengivet fra IFR's beskrivelse af Verity:

- Dronerne arbejder autonomt i **måneder ad gangen** og kræver kun **to til tre batteriskift om året**.[^1]
- På tværs af lagre optager de omkring **500.000 billeder om dagen**.[^1]
- Systemet er ifølge IFR udrullet i **omkring 200 lagre** på verdensplan.[^1]

De tal siger noget om, hvad HumaNerd forstår ved et modent produkt frem for en demo. To til tre batteriskift om året er ikke en flyvetid, man imponeres af på en messe — det er en driftsrytme, der passer ind i et rigtigt arbejdsår. Og 500.000 billeder om dagen er ikke en enkelt smart flyvetur; det er en optællingsmaskine, der kører kontinuerligt.

Priskomitéens formand, Jim Ostrowski, formulerede det sådan: «With its aerial robotics technology, Verity has managed to develop a mature product that has been successfully launched to support its customers.»[^1]

## Hvad annonceringen faktisk er

En pris er ikke en uafhængig måling af drift. IERA hædrer, at et produkt er bragt fra idé til marked — «innovation og iværksætteri» — ikke en revisorgodkendt fejlprocent. Vi kender fra denne kilde ikke Verity-systemets nøjagtighed, hvor mange droner en flåde tæller, eller hvad kunderne betaler. Det er tal, IFR-meddelelsen ikke oplyser, og som vi derfor lader stå åbne.

Men pointen holder: lageret er som robotproblem betragtet mindst lige så meget et *informationsproblem* som et *muskelproblem*. Og den robot, der løser det bedst, er lige nu en, der ikke løfter et gram — den flyver, kigger og tæller.

[^1]: International Federation of Robotics (IFR), pressemeddelelse: «IERA Award 2026 goes to Verity», Frankfurt, 16. juni 2026. Se ifr.org (International Federation of Robotics). Alle tal og citater i denne artikel er gengivet fra denne meddelelse og er IFR's beskrivelse af prisvinderen.