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

## Nr. 3 — kandidater

- **(2026-08) Marokko** (by vs. land, Ramadan-rytme, handel, kønsrum)  
- **(2026-08) Japan uden kirsebærtræer** (arbejde, service, bolig, dating)  
- **(2026-08) Filippinerne / OFW** (familieøkonomi, remitter, diaspora i DK)

## Format

- **Artikeltal:** typisk **12–16**.  
- **Standard `mustCite`:** 2+ for Tallet; 1–2 for Penge/Stat; 0 for Myter. **Ingen Ordbog** — gloser i parentes/fodnote.

## Log

- **2026-08-08 (format):** Ordbogen fjernet fra nr. 2 — gloser i parentes/fodnote i features.


- **2026-08-08:** Nr. 2 publiceret — Sydtyrol, synket med HORISONTEN Dolomit.
- **2026-08-01:** Notesbog udvidet med `## Format`.
- **2026-08-09:** Nr. 1 genopbygget og genudgivet efter afpubliceringen 2026-08-08. Se læringen ovenfor.
