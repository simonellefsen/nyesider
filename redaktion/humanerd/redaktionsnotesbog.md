# HumaNerd · redaktionsnotesbog

## Identitet

HumaNerd undersøger robotter, som skal arbejde blandt mennesker: humanoider, robotarme, mobile robotter og husholdningsrobotter. Magasinet er nysgerrigt, men ikke godtroende. Vi skelner altid mellem en prototype, en pilot, en validering, en kommerciel installation og stabil drift i et rigtigt arbejdsskift.

Vi bruger "fysisk AI" som en forklaring, ikke som en magisk etiket: en robot skal sanse, beregne, planlægge, bevæge sig og stoppe sikkert. Kinesiske, japanske, sydkoreanske, amerikanske og europæiske producenter dækkes med den samme målestok. Virksomheders egne tal navngives som virksomheders egne oplysninger; sammenlignelig markedsstatistik kommer helst fra International Federation of Robotics (IFR).

## Format

- **Fabrikken** starter med den opgave, robotten faktisk skal løse, før den beskriver kroppen.
- **Humanoiden** læser annonceringer som statusrapporter: hvad, hvor, hvem, hvor længe og med hvilken begrænsning?
- **Verdenskortet** sammenligner regioner uden at gøre nationalitet til teknologiens forklaring.
- **Hjernen** forklarer ét lag i robotstakken (gerne med diagram, når det hjælper).
- **Hjemmet** behandler privatliv, sikkerhed og vedligehold som en del af produktet — og menneskeligt arbejde i “samarbejdet”.
- **Tallet** angiver år, geografi og måleenhed i en kildebelagt tabel; skeln IFR fra virksomhedstal.
- **Påstandskontoret** afmonterer hype uden messesprog.
- **Ingen fast Ordbog-side.** AMR, WMS, SKU, 3PL, API m.fl. forklares i brødtekst (parentes) eller fodnote første gang i *hver* artikel. (Nr. 1 har historisk ordbog; fra nr. 2 er formatet droppet.)
- **Dybde før bredde:** features skal være læsbare artikler (sigt typisk **500–800 ord**, hævet fra 250–500 den 2026-08-09), ikke tre overskrifter med én sætning. Navngiv **konkrete operatører/anlæg/systemer**, når de er dokumenterbare (Amazon/Kiva-arv, Ocado-grid, AutoStore, navngivne 3PL-piloter) — og mærk selskabstal som selskabstal.
- **Undgå meta-bokse** (“HumaNerd-målestok” som tjekliste-overblik er ok, hvis den er kort; hellere indlejret i prosa end “regel”-bokse der ligner redaktionsnoter).

## Udgivne numre

- **(2026-08) Nr. 2 — “Lagerets koreografi”**: AMR’er, Amazon/Ocado/AutoStore som eksempler, pluk, WMS, sikkerhed, den menneskelige undtagelse. Uden ordbog. `bestilling.json` under `numre/2026-08-nr2/`.
- **(2026-08) Nr. 1 — “Robotter på arbejde”**: humanoider og andre robotter i fabrik, lager og hjem. Nummeret kortlægger markedet, AI-stakken og forskellen mellem feltforsøg og drift.
  **Genopbygget 2026-08-09:** 11 artikler / 6.630 ord (var 12 / 2.924). Ordbogen fjernet. Ti artikler
  reelt kommissioneret på `.env.humanerd`; lederen er chefredaktionens uden byline. Forbrug **0,42 USD**.

### Læring fra genopbygningen af nr. 1 (2026-08-09)

**Den vigtigste kilde lå i kundens eget nyhedsrum.** BMW's pressemeddelelse af 6. august 2024 om den
«vellykkede test» med Figure indeholder sætningen, at der *aktuelt ikke er nogen Figure AI-robotter på
fabrikken i Spartanburg, og at der ikke er fastlagt nogen tidsplan*. Den citeres stort set aldrig
videre. Læringen er generel: når en leverandør fejrer et forløb hos en kunde, så læs kundens egen
udmelding fra samme dag — den er ofte smallere, og forskellen er historien.

**Hold styr på, hvis tal det er.** Alle detaljerede tal fra Figure/BMW-forløbet (11 måneder,
ca. 1.250 driftstimer, 90.000 dele, 30.000 X3) kommer fra leverandøren. BMW's vicedirektør bekræftede,
at pilotforsøget gik godt, uden at angive ét eneste tal. Den asymmetri skal stå i artiklen.

**En 200 er ikke et bevis for, at siden er den rigtige.** Tre gange i denne genopbygning gættede en
kladde en adresse, som svarede 200 med et helt andet indhold — to gange hos Geostat, én gang hos
**ifr.org**, hvor `…/robot-density-by-country-2024` serverer en pressemeddelelse om FCC-restriktioner
fra august 2026. `check_links.py` godkender dem alle. Åbn siden og læs, hvad der står.

**En delvist rigtig litteraturhenvisning er farligere end en forkert.** En kladde angav «Evan Ackerman,
*How to Watch a Robot Video*, IEEE Spectrum, 2023». Forfatter, år og emne var rigtige; titel og
publikation var det ikke. Den rigtige er *How to Make a Good Robot Video [Media]*, **IEEE Robotics &
Automation Magazine**, bind 30, nr. 2, 2023, s. 127. Kontrollér altid tidsskrift, bind og side — ikke
kun at forfatteren findes.

**Pas på kategorifejl mellem tælleværker.** Amazons million robotter (juli 2025) og IFR's driftsbestand
på 4.664.000 industrirobotter tæller ikke det samme; Amazons flåde er overvejende mobile lagerrobotter.
Divisionen «Amazon står for en femtedel af verdens industrirobotter» cirkulerer alligevel.

**Kontrollér også de tal, briefen selv udleverer.** Briefen regnede 1.250 driftstimer om til fire timer
pr. arbejdsdag. Det er fem. Fejlen nåede to kladder, fordi begge stolede på briefen.

**Kvitteringer: her var DAGS-tælleren den rigtige.** `usage_daily + byok_usage_daily` = 0,424845 mod
ledgerens 0,4248. Levetidstallet lå 0,019 USD højere — tidligere, udokumenteret forbrug på nøglen,
formentlig det, der frembragte de to forældreløse kladder i `kladder/`. Modsat KULTURBOXEN, hvor
levetidstallet var det rigtige. Reglen er stadig: afstem mod begge, og forklar forskellen.

## Idébank

- **(2026-08) Robotten der kan se** — kameraer, kraftsensorer og grænserne for perception.
- **(2026-08) Håndens problem** — gribere, taktilitet og hvorfor det bløde stadig er svært.
- **(2026-08) Tre humanoider, tre beviser** — 1X, Figure og Boston Dynamics sammenlignet på opgave, dokumentation, autonomi, kundeadgang og sikker drift; undgå at lave en model- eller nationalitetsrangliste af demoer.
- **(2026-08) Dronen som robot** — inspektion, lager, landbrug og beredskab; skeln mellem fjernstyring, assisteret flyvning og autonomi.
- **(2026-08) Robotter i krig** — militære anvendelser, dual use, menneskelig kontrol, fejlrisiko og dokumentation. Må ikke behandles som gadgetstof eller produktpromovering; brug primærkilder, folkeretlige rammer og uafhængig rapportering.
- **(2026-08) Boston Dynamics efter videoen** — fra mobilitet til konkret arbejdscelle, med den samme pilot→drift-målestok som nr. 1.
- **(2026-08) Humanoiden på scenen** — robotter i koncert, teater, forlystelse, tv og brandaktivering. Skeln mellem autonom robot, teleoperation, forudprogrammeret koreografi og visuel illusion.

## Løfter til læseren

- Vi skriver "pilot", når det er en pilot.
- Vi gør regneenheden tydeligere end tallet.
- Vi viser sikkerhed, data og menneskeligt arbejde som en del af systemet.
- Vi navngiver drift, når den findes — og siger fra, når det kun er en demo.

## Log

- **2026-08-08:** Nr. 2 publiceret — lager/AMR før humanoid-hype.
- **2026-08-08 (edit):** Nr. 2 udvidet (især lager-koreografi med Amazon/Ocado/AutoStore m.fl.); Ordbogen fjernet; formatregel om dybde og inline-forklaringer.
- **2026-08-09:** Nr. 1 genopbygget og genudgivet efter afpubliceringen 2026-08-08. Se læringen ovenfor.
- **2026-08-09 (format):** Formatreglen om 250–500 ord pr. feature er hævet til **500–800**. Loftet stammede fra en periode, hvor artiklerne var for tynde; et blad, der skelner mellem pilot, validering og drift, kan ikke gøre det på 250 ord.
