# KULTURBOXEN – Redaktionsnotesbog

Opdateret efter nr. 2 (august 2026, *"Tre sprog, ét plateau"* — Sydtyrol).  
OpenRouter: **kun** `.env.kulturboxen`. Imagine: `.env.local` / `XAI_API_KEY`.

## Identitet

**KULTURBOXEN** er magasinet om **hvordan mennesker lever** i andre kulturer — med dansk/europæisk læser som udgangspunkt for *sammenligning*, ikke som facit.

### vs HORISONTEN

| | HORISONTEN | KULTURBOXEN |
|---|---|---|
| Fokus | Rejse, ruter, sæson, praktisk | Hverdag, normer, systemer |
| Spørgsmål | Hvordan kommer jeg derhen? | Hvordan lever folk dér? |

## Nr. 2 — GENOPBYGGET OG GENUDGIVET 2026-08-17

**Tema:** Tre sprog, ét plateau · **Kultur:** Sydtyrol / Alto Adige
**12 artikler, 6.472 ord** (var 1.877 ord — gns. 156). Elleve artikler reelt kommissioneret
på `.env.kulturboxen`; lederen er chefredaktionens og har **ingen byline**.
Samlet forbrug **0,38 USD**. `check_issue.py`: **0 fejl, 0 advarsler.**
`bestilling.json`: `redaktion/kulturboxen/numre/2026-08-nr2/bestilling.json`.

### Nummeret indeholder ikke ét tal — og det står i lederen hvorfor

Ingen befolkningstal, ingen sproggruppeprocenter, ingen turisme- eller indkomsttal.
Det er ikke et stilvalg. **ASTAT**, provinsens eget statistikinstitut, leverer en tom side
uanset hvilken underside der kaldes — samme 2.536 bytes hver gang, både via browser og curl.
`provinz.bz.it` svarer 403. Europarådets mindretalsside ligger bag Cloudflare.

Tallene kunne være hentet fra en sekundær kilde. Men **et mindretalstal uden ophav er en
politisk påstand og ikke en afrunding**, og i et nummer om netop mindretalsordninger ville
det have været det modsatte af ærindet. Rubrikken **Tallet** handler derfor om selve
optællingen: at en tælling, der fordeler goder, ikke er en måling af virkeligheden, men en
handling i den. Det er rubrikkens bedste udgave hidtil.

### Metoden, der nu har virket fire gange på én dag

INDENI nr. 2, HORISONTEN nr. 2, PULSEN nr. 2 og dette nummer: **en brief, der forbyder de tal,
der ikke kan kildebelægges, får mekanismen forklaret i stedet.** Elleve kladder her — ikke ét
opfundet tal, ikke én gættet URL, ikke ét årstal. Det er den mest effektive enkeltregel, der er
kommet ud af hele genopbygningen.

### To fælder, der blev undgået

**Krydslink til en upubliceret udgivelse.** Den afpublicerede udgave linkede fem steder til
HORISONTEN nr. 3 (Dolomitterne), som stadig er `draft`. Prerenderingen brækker på et dødt
internt link. Briefen forbød det, og ingen kladde forsøgte.

**YAML-fælden.** `autonomi` fik en standfirst med kolon i — «staten til to ting på én gang: en
fjern instans …» — som gør frontmatter ugyldig og siden til en 404. `check_issue.py`s
frontmatter-vagt fangede den før build. Den vagt tjener sig ind.

## Nr. 1 — udgivet

**Tema:** Supra og tillid · **Kultur:** Georgien  
**Genopbygget 2026-08-09:** 14 artikler / 8.325 ord (var 15 / 4.223). Ordbogen fjernet.
Tretten artikler reelt kommissioneret på `.env.kulturboxen`; lederen er chefredaktionens uden
byline. Forbrug **0,61 USD**. `bestilling.json` under `numre/2026-08-nr1/`.
**Søsterrejse:** HORISONTEN nr. 2 — *afpubliceret, så krydslinket er fjernet fra leder og
til-horisonten. Genindsæt når nr. 2 er genopbygget.*

### Læring fra genopbygningen af nr. 1 (2026-08-09)

**Den farligste linktype er ikke 404 — den er 200 med forkert indhold.** To kladder gættede
Geostat-adresser af formen `geostat.ge/en/modules/categories/<id>/<slug>`. Ingen af dem var døde.
`/768/2024-population-census` serverer Geostats **kriminalstatistik for juli 2022**;
`/322/inbound-visitors-statistics` serverer **migrationsstatistik**. Geostat ignorerer sluggen og
svarer på id'et, så en gættet Geostat-adresse giver aldrig 404. `check_links.py` godkender dem alle.
**Åbn hver Geostat-adresse og læs, hvad der står på siden** — statuskoden beviser ingenting her.

**«3,7 mio.» er 2014-tallet.** Folketællingen 14. november 2024 gav **3.929.581** — 215.777 flere end
2014-tællingens 3.713.804. De endelige resultater kom først 22. juni 2026, og fremskrivningen imellem
havde ligget for lavt. Tallet 3,7 mio. stod i vores egen `researchNote`, og to briefs var skrevet på
det, før det blev fanget. Det blev nummerets bærende pointe i stedet: et tal har en metode.

**En opfundet kilde ser mest troværdig ud, når institutionen er rigtig.** To kladder fra samme model
omregnede lari til kroner med henvisning til «Danmarks Nationalbanks kursoversigt». Nationalbanken
noterer ikke lari. Kursniveauet var tilfældigvis nogenlunde rigtigt, hvilket gjorde det værre.
Omregning går nu åbent gennem Georgiens Nationalbanks eurokurs og den danske fastkurspolitik.

**Kontrollér også de tal, briefen selv giver modellen.** Briefen udleverede 2.466 GEL som
gennemsnitsløn. Det er 4. kvartal 2025 — årets højeste. Årsgennemsnittet er 2.282,7 GEL, og
kvartalstallet alene overdriver niveauet med ca. 8 %. Fejlen var redaktionens, ikke modellens, og den
nåede tre artikler, før kildekontrollen fangede den.

**Kvitteringer: levetid mod dag afhænger af, hvornår arbejdet lå.** Her matchede **levetidstallet**
ledgeren præcist (0,6058), mens dagstallet manglede 0,06769 — nøjagtig prisen på den ene artikel, der
blev bestilt dagen før. Modsat INDENI, hvor levetidstallet indeholdt 0,10 USD fremmed forbrug.
Reglen er ikke «brug dagstallet», men: **afstem mod begge, og forklar forskellen.**

**Modellerne siger fra, når de ikke kan kildebelægge.** `myter` skrev det ind i den færdige artikel:
at der ikke findes grundlag for at udtale sig om kriminalitetsniveauet, og at det ikke skal opfindes.
`tallet` skrev «omkring seks millioner» om Danmark frem for at gætte præcist. Begge dele var bestilt
i briefen — det virker, når man beder om det.

**Og de finder rigtige ting, ingen har bedt om.** `ceremonier` valgte selv Svetitskhovloba den
14. oktober som helligdag uden dansk pendant; den står på turistadministrationens officielle liste.
`supra-og-bordet` angav Darra Goldstein, *The Georgian Feast*, UC Press 1999 — korrekt forlag, år og
førsteudgave. `familie-og-forhold` og `skat-og-stat` angav hver sit korrekte Venedigkommission-nummer.

## Nr. 3 — udgivet 2026-08-19

**Tema:** Landet der arbejder ude · **Kultur:** Filippinerne, set gennem migrationen
**10 artikler, 3.979 ord.** Ni artikler reelt kommissioneret på `.env.kulturboxen`; lederen er
redaktionens uden byline. Forbrug **0,2414 USD**. `check_issue.py`: **0 fejl, 0 advarsler.**
`bestilling.json`: `redaktion/kulturboxen/numre/2026-08-nr3/bestilling.json`.

Første af de tre nr. 3-kandidater valgt. De to øvrige (Marokko, Japan uden kirsebærtræer) står
stadig som kandidater til nr. 4.

**Bevidst asynk med HORISONTEN.** Ingen samtidig rejseudgave om Filippinerne denne gang —
researchen gik mod migrationen og den danske au pair-forbindelse, ikke mod ruten. Notér det
åbent i bagsnittet «Til HORISONTEN» i stedet for at tvinge en syntetisk synk, jf. husreglens
egen anvisning om, at synk ikke altid er muligt.

### Kernetal

- **OFW-remittancer:** 35,634 mia. USD i 2025 (+3,3 % fra 2024), 7,3 % af BNP. 56,0 % af
  alle OFW'er er kvinder.
- **Au pair i Danmark:** filippinske statsborgere har udgjort 80–83 % af alle au pair-tilladelser
  i over et årti (2013: 1.646/1.989; 2023: 431/533; 2024: 483/591) — stabil andel, styrtdykkende
  volumen. Kilde: Kristeligt Dagblad 6. maj 2024, med tal fra DST/SIRI.
- **BPO/IT-BPM:** 1,89 mio. ansatte i 2025 (+3,7 %), over 40 mia. USD i eksport — den anden
  eksportøkonomi for arbejdskraft, hvor opgaven rejser i stedet for mennesket.
- **Børnene, der bliver tilbage:** Dominguez & Hall (2022), *Lancet Regional Health — Western
  Pacific*, scoping review, 4.440 poster gennemgået, 50 studier inkluderet.

### To kilde-fælder fanget

- **En opdigtet DST-tabelreference.** En kladde citerede `statistikbanken.dk/VAN22` som specifik
  kilde til au pair-tal — ved kontrol viser adressen kun en generisk søgeside, intet konkret
  indhold. Erstattet med den faktisk verificerede Kristeligt Dagblad-artikel.
- **En uendelig redirect-loop.** Tre kladder linkede til `thelancet.com/journals/lanwpc/home`
  (tidsskriftets forside) i stedet for den konkrete artikel — `check_links.py` rapporterede
  **DEAD 302** med en redirect-loop-fejl. Fundet den rigtige artikel (Dominguez & Hall 2022,
  bind 28, artikel 100566) og skiftet til PMC-spejlet, som svarer 200 til automatiserede kald,
  hvor selve Lancet-siden svarer 403.

### Ny artikeltype: en dansk migrationsforbindelse uden rejsevinkel

Dette er første KULTURBOXEN-nummer, hvor den konkrete danske forbindelse til kulturen ikke er
turisme, men arbejdsmigration (au pair). Det gav en ekstra sektion (`Dagligdag & tempo`) en
markant mere Danmarks-nær vinkel end i Georgien- og Sydtyrol-numrene — værd at overveje som fast
greb, når et lands diaspora i Danmark er dokumenterbar.

## Nr. 4 — kandidater

- **(2026-08) Marokko** (by vs. land, Ramadan-rytme, handel, kønsrum)  
- **(2026-08) Japan uden kirsebærtræer** (arbejde, service, bolig, dating)

## Format

- **Artikeltal:** typisk **12–16**.  
- **Standard `mustCite`:** 2+ for Tallet; 1–2 for Penge/Stat; 0 for Myter. **Ingen Ordbog** — gloser i parentes/fodnote.

## Log

- **2026-08-19:** Nr. 3 udgivet — Filippinerne/OFW, nyt nummer produceret fra bunden. Se
  læringen ovenfor. To kildefælder fanget (opdigtet DST-tabelreference, uendelig redirect-loop).

- **2026-08-08 (format):** Ordbogen fjernet fra nr. 2 — gloser i parentes/fodnote i features.


- **2026-08-08:** Nr. 2 publiceret — Sydtyrol, synket med HORISONTEN Dolomit.
- **2026-08-01:** Notesbog udvidet med `## Format`.
- **2026-08-09:** Nr. 1 genopbygget og genudgivet efter afpubliceringen 2026-08-08. Se læringen ovenfor.
