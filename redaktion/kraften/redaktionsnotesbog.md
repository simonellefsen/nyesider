# KRAFTEN – Redaktionsnotesbog

Opdateret efter nr. 5 (september 2026, *"Fra produktion til distribution"*). Modelerfaringer: [modelkartotek](../modelkartotek.md).

## Identitet

**KRAFTEN** er magasinet om **elektrificering** — hvordan strøm erstatter fossil energi i transport, varme, industri og hverdag, **på tværs af lande**, og hvordan den samme logik rækker **ud i rummet**.

### Afgrænsning

- **Ikke SPÆNDING:** bilmodeller og danske afgifter → SPÆNDING.  
- **Ikke ORBIT (fuld rumfart):** opsendelser/katalog → ORBIT. KRAFTEN tager **rumkraft** (watt).  
- Tone: nøgtern, kildetung, global.

## Format

- **Ordmål:** Features 200–400 i batch (sigt 500–750 når der er tid).  
- **Artikeltal:** 12–16. **Ingen Ordbog** — gloser i parentes/fodnote.  
- **Standard `mustCite`:** 2+ for MW/TWh/andels-tal; 0 for rygtebørs.

## Nr. 2 — genopbygget og genudgivet 2026-08-16

**Tema:** Strøm overalt
**13 artikler, 7.933 ord** (var 13 artikler / 5.237 ord — gns. 403). Tolv artikler reelt
kommissioneret på `.env.kraften`; lederen er chefredaktionens og har **ingen byline**.
Samlet forbrug **0,65 USD**. `bestilling.json`: `redaktion/kraften/numre/2026-08-nr2/bestilling.json`.

Den afpublicerede udgave havde en `bestilling.json`, men den var tom, hvor det gjaldt:
`writer.model: editor-led`, ingen `costUSD`, ingen `receipt.draft` og ingen fil i `kladder/`
for en eneste af de 13 artikler — samtidig med at nummeret bar byline til navngivne modeller.

### Hvad faktatjekket fangede denne gang

Samme mønster som nr. 1, men skarpere:

- **Rigtigt tal, forkert rapport — igen, og værre.** `lagring`-kladden tilskrev samtlige tre tal
  de forkerte IEA-rapporter (*Batteries and Secure Energy Transitions*, *Electricity 2024*, en
  tracker-side). Alle tallene står i *Electricity 2026*. Alle de forkerte rapporter findes, og
  alle URL'erne svarede 200 — hverken `check_links.py` eller en hurtig læser ville have fanget det.
- **To ubriefede påstande.** `indien-syd` skrev, at Indien som fjerdestørste kun var overgået af
  «Kina, USA og Brasilien»; den rækkefølge står ikke i kilden. `netflaskehalse` skrev, at de
  2.500 GW i kø er «mere end det dobbelte» af verdens installerede sol og vind; det er forkert.
- **Fem døde adresser**, heraf to der svarer 200: en Caltech-nyhed (404), ITU's forside på forkert
  sti (404), `iea.org/reports` uden rapportnummer (404), Unipers newsroom (svarede slet ikke) og
  Embers amerikanske landeprofil på `/united-states/` i stedet for `/united-states-of-america`.
- **En kilde med forkert indhold.** `rum-solpanel` hentede «op mod 16 formørkelser i døgnet» fra
  NASA's ISS-forside. Siden svarer 200; påstanden står der ikke.
- **En faktor to i den gamle udgave.** Nordic Baseload Powers Barsebäck-projekt stod som
  «2 × ~2.500 MWe». WNA skriver to reaktorer med **samlet** ca. 2.500 MWe.

### To modsatte lektioner om linktjek

Nummeret endte med begge fejltyper i samme udgivelse, og de er skrevet ind i artiklerne:

- **Død side, der melder sig levende.** ESA's sider om orbital solkraft svarer HTTP 200 og
  leverer agenturets egen fejlside. Derfor står der intet om ESA i nummeret.
- **Levende side, der meldes død.** NASA Glenns server sender ikke sit mellemliggende certifikat.
  Browseren henter det selv; `check_links.py` melder siden død. Siden er læst.

Dertil: NASA's egne sider om Fission Surface Power under `nasa.gov` er i en **redirect-løkke**
(`/missions/artemis/…` → `/space-technology-mission-directorate/…` → tilbage igen).

### Læring til nr. 3

**Sæt `mustCite` EFTER kildesøgningen, ikke før.** Fem artikler udløser advarsel om for få
citations. Advarslen er korrekt, men årsagen er redaktionens: `mustCite: 3` blev skrevet, før
researchen viste, at stoffet stammer fra én autoritativ side. At splitte samme side i tre
fodnoter ville give tre links til samme adresse — falsk præcision af præcis den slags, bladet
advarer imod.

## Nr. 2 — den afpublicerede udgave (til arkivet)

**Tema:** Strøm overalt  
13 artikler: leder, tallet (el-andel), Kina, Indien/syd, EU/USA, netflaskehalse, lagring, rum-solpanel, rum-kernekraft, orbital solkraft, lande-snapshot, Sverige-atom, rygtebørs. (Ordbogen fjernet 2026-08-08.)  
Cover + feature-billeder (Imagine).  
`bestilling.json`: `redaktion/kraften/numre/2026-08-nr2/bestilling.json`.  
Kryds: [ORBIT nr. 2](../../content/orbit/issues/2026-08-nr2/).

**Depth-pass (samme dag som publicering):** Features var for tynde efter batch-udgivelse. Omskrevet: Indien (fjernet meta-«Læseregler», prosa med adgang/peak/leapfrog + kilder); Sverige-atom (6 reaktorer ~7 GW, ~29 % el 2024, Nordic Baseload Power 2×~2 500 MWe Barsebäck-støtteansøgning juni 2026); øvrige features udvidet til magasinlængde.

## Nr. 1 — genopbygget og genudgivet 2026-08-09

**Tema:** Hvad holder lyset tændt
**13 artikler, 9.701 ord** (var 14 artikler / 4.165 ord — gns. 297). Ordbogen fjernet.
Tolv artikler reelt kommissioneret på `.env.kraften`; lederen er chefredaktionens og har **ingen byline**.
Samlet forbrug **0,54 USD** — ledgersummen stemmer på øren med `GET /api/v1/key`.
`bestilling.json`: `redaktion/kraften/numre/2026-08-nr1/bestilling.json`.

Den oprindelige udgave havde **ingen `bestilling.json`** — ingen brief, intet verdikt, ingen kvittering —
men bar byline til navngivne modeller.

### Hvad der virkede

**Skriv tallene ind i `brief.angle`, ikke i `researchNote`.** `researchNote` når aldrig frem til
modellen. Efter den ændring ramte `europa-mix` alle syv tal i første forsøg og leverede den første
kladde i hele genopbygningen uden en eneste gættet URL.

### Hvad faktatjekket fangede

Fejlmønstret var **ikke** sprogligt. Det var kilder og årstal:

- **Bare domænehenvisninger** i stedet for kilder («Se iea.org») i fire kladder. Ubrugeligt for læseren.
- **Rigtigt tal, forkert rapport:** sol-kladden tilskrev IEA-tal til *Renewables 2024*; de står i
  *Electricity 2026*. Gas-kladden satte 17 % gasandel til 2023; det er 2025-tallet.
- **Forældede tal:** fusionsbranchens investeringer stod til «over 6 mia. dollar» fra en rapport fra
  2023. Facit er 14,24 mia., heraf 4,48 mia. rejst alene i året frem til juli 2026.
- **Gættede URL'er:** energy.gov om andekurven, Eurostat om energiforbrug, IAEA om tritium — alle 404.

### Hvad der er værd at gentage

`lande`-kladden **nægtede at udfylde landeskemaet** med tal, den ikke kunne kildebelægge, og skrev
begrundelsen ind i artiklen: *«en falsk-præcis procent er værre end en åben beskrivelse.»* Redaktionen
har derefter fundet de tal, der kunne findes (Kina 22 %, OECD 20 %), og ladet resten stå tomt med
begrundelsen. Det er den rigtige rækkefølge.

## Nr. 3 — udgivet 2026-08-19

**Tema:** Hvem får strømmen først? **8 artikler, 2.742 ord.** Syv artikler reelt kommissioneret på
`.env.kraften`; lederen er redaktionens uden byline. Forbrug **0,2526 USD**. `check_issue.py`:
**0 fejl, 0 advarsler.** `bestilling.json`: `redaktion/kraften/numre/2026-08-nr3/bestilling.json`.

Alle fire nr. 3-kandidater brugt: data centre vs. husholdninger (globalt + Irland som case),
havne-el, det afrikanske netadgangs-spring, og svensk atom.

### Kernetal

- **Datacentre globalt:** 485 TWh i 2025 (+17 %), ventet 950 TWh i 2030 (~3 % af globalt
  elforbrug). AI-fokuserede datacentre: +50 % i 2025, tredobling ventet til 2030. Kilde: IEA,
  *Key Questions on Energy and AI*, april 2026.
- **Irland:** datacentre 23 % af elforbruget i 2025 (7.663 GWh, +10 %) mod husholdningers
  28 % (+1–2 %) — gabet lukker hurtigt. Kilde: CSO, 7. juli 2026.
- **Havne-el:** kun 20 % af de AFIR-krævede OPS-tilslutninger var installeret/kontraheret medio
  2025, 58 % af EU-havne har OPS-kapacitet overhovedet. Deadline: 31. december 2029.
- **Afrika:** 730 mio. uden elektricitet globalt (2024), 8 ud af 10 i Subsahara-Afrika. Minigrids
  drev ~90 % af nye tilslutninger i 2024.
- **Svensk atom:** Videberg Kraft (Vattenfall) valgte Rolls-Royce SMR som leverandør, offentliggjort
  15. juni 2026 — tre reaktorer à 470 MW (~1.410 MW, ~12 TWh/år), efter en fireårig proces med 70+
  oprindelige kandidater. Investeringsbeslutning ventet 2029.

### En kladde blev væsentligt opdateret før accept

`svensk-atom`-kladden skrev, at "endeligt leverandørvalg ventes i 2026", som om spørgsmålet stod
åbent. En opfølgende research fandt Vattenfalls egen pressemeddelelse af 15. juni 2026, der viser,
at valget allerede var truffet og offentliggjort — med langt mere præcise tal (470 MW × 3 = 1.410 MW,
~12 TWh/år, 70+ oprindelige kandidater over fire år) end kladdens vagere "op til 1.500 MW". Artiklen
blev omskrevet til de bekræftede tal. Verdikt: `rewritten-by-editor`.

### mustCite sat før research — igen, men denne gang håndteret rigtigt

Tre artikler (`datacentre-globalt`, `afrika-netadgang`, `svensk-atom`) endte med færre citationer
end briefet krævede — men denne gang er det IKKE en fejl. Hver historie har genuint kun ÉN
autoritativ kilde (IEA's ene rapport, Vattenfalls ene pressemeddelelse). At splitte samme side i
flere fodnoter for at ramme et tal ville have været den falske præcision, nr. 2's læring advarer
imod. Ledgerens `citations`-felt er rettet til det faktiske, korrekte antal, med en forklarende note
— ikke opjusteret med opfundne ekstra fodnoter.

## Nr. 4 — udgivet 2026-08-29

**Tema:** Atomkraften vender tilbage — drevet af datacentre, på vej til Månen (indfrier nr. 3's
bagsideløfte om SMR-ansøgninger med konkret myndigheds-/virksomhedstekst). **7 artikler, 3.494
ord.** Seks artikler reelt kommissioneret på `.env.kraften`; lederen er redaktionens uden byline.
Forbrug **0,2157 USD**. `check_issue.py`: **0 fejl, 0 advarsler.** `check_links.py`: **0 døde
links.** `bestilling.json`: `redaktion/kraften/numre/2026-08-nr4/bestilling.json`.

Fire spor: techgiganternes atomaftaler (Microsoft/Constellation, Google/Kairos, Amazon/X-energy),
SMR-kapløbet globalt (Kina/Linglong One, Canada/Darlington, USA/Kemmerer, UK/Wylfa), en ærlig
økonomisk realitetstjek (NuScale-annulleringen), og et rumspor: NASA/DOE's fissionsreaktor til
Månen.

### Lært af GNISTEN nr. 4 samme dag: skriv verificerede URL'er direkte ind i briefen

Efter at GNISTEN nr. 4 samme dag oplevede, at en model afviste at skrive en artikel, fordi den
ikke kunne bekræfte begivenheder nyere end dens træningsdata, blev alle KRAFTEN nr. 4-briefs
skrevet med en eksplicit liste af verificerede URL'er indsat direkte i `brief.angle` — ikke kun
beskrevet som fakta. Alle seks kommissioneringer lykkedes på første forsøg, med korrekte,
konkrete fodnoter. **Denne praksis bør være standard fremover, når en brief refererer til
begivenheder fra 2024-2026** — modellens egen viden rækker ikke til at bekræfte eller finde
kilder til dem.

### Fabrikeret sammenligningstal fanget i faktatjekket

`atomkraft-paa-maanen`-kladden tilføjede en ubriefet påstand om, at "tidligere rumreaktorer typisk
har opereret i intervallet 10-40 kilowatt". Research viste, at USA's eneste fissionsreaktor
nogensinde sendt i rummet (SNAP-10A, 1965) leverede omkring **500 watt** — ikke kilowatt — og at
tidligere radioisotopgeneratorer (RTG'er, en helt anden teknologi) lå i enkelte til lave hundrede
watt. Tallet var ikke bare forkert, det var en helt anden størrelsesorden. Rettet til det
korrekte, kildebelagte SNAP-10A-tal. **Samme mønster som Danmarkshistorien og HumaNerd har fundet
i andre titler denne uge: en model kan finde korrekte navne og datoer og stadig tilføje et
selvsikkert, forkert tal ved siden af, hvis briefen ikke eksplicit har stillet det til raadighed.**

### Reaktor 1 vs. reaktor 2 — en skelnen der holdt

Briefen for `techgiganternes-atomaftaler` krævede eksplicit, at Three Mile Islands reaktor 1
(genstartes af Microsoft/Constellation, lukkede 2019 af økonomiske årsager) ikke måtte blandes
sammen med reaktor 2 (stedet for 1979-ulykken, permanent lukket). Kladden holdt skelnen korrekt
uden yderligere redigering — et eksempel på, at en tydelig, eksplicit advarsel i briefen om en
oplagt forvekslingsrisiko virker.

## Nr. 5 — udgivet 2026-09-05

**Tema:** Fra produktion til distribution — undersøiske højspændingskabler og kobber som ressource
(indfrier nr. 4's bagsideløfte). **7 artikler, 2.773 ord.** Seks artikler reelt kommissioneret på
`.env.kraften`; lederen er redaktionens uden byline. Forbrug **0,1754 USD**. `check_issue.py`:
**0 fejl, 3 advarsler** (alle forklarede, se nedenfor). `check_links.py`: **0 døde links** (1
bot-blokeret, National Grid, svarer 403 men er læst manuelt). `bestilling.json`:
`redaktion/kraften/numre/2026-09-nr5/bestilling.json`.

Tre kabel-cases med tre forskellige skæbner: Viking Link (Danmark-UK, i drift siden 29. december
2023, 765 km/1.400 MW), Xlinks (Marokko-UK, 4.000 km/11,5 GW, **afvist af den britiske regering i
juni 2025** efter milliarder i privat investering), og Australia-Asia PowerLink/tidl. Sun Cable
(4.300 km/6 GW, overlevede et selskabskollaps i januar 2023, FID ventet 2027). Plus Tallet og en
kobber-feature, begge bygget på samme S&P Global/IEA-tal (42 mio. ton efterspørgsel i 2040 mod et
forsyningsgab på 10 mio. ton).

### Xlinks-fejlen der ikke blev begået: forældet træningsviden om et "kommende" projekt

Første websøgning på Xlinks fandt kun 2022-2023-materiale, der beskrev projektet som fremadskridende
("første kabel aktivt i 2027"). En opfølgende søgning specifikt efter 2025-2026-status afslørede, at
den britiske regering reelt havde **afvist** projektet i juni 2025 — en fundamentalt anden historie.
**Lektionen, værd at gentage i alle titler:** et projekt, der lød aktivt i det, modellen (eller den
første websøgning) "husker", skal altid eftertjekkes for en nyere status, før det briefes som
igangværende. Havde denne fejl ikke være fanget i research-fasen, ville en hel artikel være bygget
på en forkert præmis.

### To kladder med opdigtede/døde kilder — begge fanget og rettet

- `suncable-australien-singapore`-kladden (DeepSeek V3.2) citerede fem URL'er, hvoraf tre var
  problematiske: `sun-cable.com` opløser slet ikke (DNS-fejl, ren opdigtning — selskabets rigtige
  side er `suncable.sg`, som til gengæld ikke kan hentes automatiseret pga. en TLS-fejl), en
  Guardian-artikel på en gættet, forkert sti (404), og en australsk regeringsside, der konsekvent
  timer ud. Erstattet med Wikipedia, New Atlas, ABC News (uændret AFR-kilde beholdt) og Energy
  Storage News — samme fakta, verificerede adresser.
- `xlinks-afvist`-kladden (Gemini 3.1 Pro) citerede en 2023-artikel (NS Energy) om et projekt, der
  siden er blevet afvist — indholdsmæssigt forældet, ikke forkert i sig selv — samt `viking-link.com`,
  som timer ud og ikke kan verificeres. Begge erstattet med aktuelle 2025-kilder (Solar Power Portal,
  Morocco World News) og Wikipedia.

### Bare domænehenvisninger fanget igen — samme mønster som nr. 1 og nr. 2

`kobber-flaskehalsen`-kladden pegede på `spglobal.com/commodityinsights` og `iea.org` uden konkret
side — nøjagtig den fejltype, nr. 1 og nr. 2's læringer allerede havde navngivet. Erstattet med de
faktiske sider (samme S&P Global-pressemeddelelse som Tallet bruger, IEA's Global Critical Minerals
Outlook 2025-side). **Mønstret gentager sig på tværs af numre — det er værd at skrive direkte ind i
fremtidige briefs: "brug den konkrete side, ikke domænets forside", ikke kun i chefredaktørens
tjekliste.**

## Løfter givet i nr. 5

- **Bagsiden:** en satellit gennem Jordens skygge — hvordan solpaneler, batterier og strømstyring
  holder den i live, når lyset forsvinder.

## Research-regler

Tal med **kilde + årstal**. Skeln nameplate MW / TWh / planlagt / under byggeri / i drift.
**Tjek altid om et "kommende" projekt stadig er aktivt** — Xlinks nr. 5's lektion: et projekt kan
være afvist eller skrinlagt siden modellens træningsdata.
OpenRouter: **kun** `.env.kraften`. Imagine: `.env.local`.

## Log

- **2026-09-05:** Nr. 5 udgivet — 'Fra produktion til distribution', indfrier nr. 4's bagsideløfte.
  Se læringen ovenfor: en forældet "Xlinks er på vej"-antagelse blev fanget og rettet til den
  faktiske 2025-afvisning; to kladder havde opdigtede/døde kilder, alle erstattet.

- **2026-08-19:** Nr. 3 udgivet — 'Hvem får strømmen først?', nyt nummer produceret fra bunden.
  Se læringen ovenfor. Én kladde (svensk-atom) væsentligt opdateret før accept, da en opfølgende
  research fandt et nyere, mere præcist primærkilde-dokument end kladdens grundlag.

- **2026-08-08 (format):** Ordbogen fjernet fra nr. 2 — gloser i parentes/fodnote i features (ikke separat ordliste).


- **2026-08-08:** Nr. 2 publiceret — global elektrificering + rumkraft-pakke.
- **2026-08-01:** Notesbog udvidet med `## Format`.

- **2026-08-08 (edit):** KRAFTEN nr. 2 — forklaret *Fit for 55* og *IRA* i EU/USA-artiklen; udfoldet *PJM-agtige køer* i netflaskehalse; Sverige-atom omskrevet fra notes-kladde til færdig feature og flyttet **før** Ordbog/Rygtebørs (lå tidligere som sidste side efter bagsnit).
- **2026-08-08 (process):** Efter Sverige-kladde-uheldet: `production/check_issue.py` flagger nu **draft/production-meta** i publiceret brødtekst som ERROR; chefredaktør-tjekliste i [redaktion/README](../README.md) kræver eksplicit “færdig læsertekst” + jargon første gang + features før bagsnit.
- **2026-08-08 (depth):** Features stadig for korte efter batch. Indien: Læseregler væk → prosa. Sverige: flåde (6 reaktorer, Forsmark/Ringhals/Oskarshamn, ~50 TWh/~29 %) + Nordic Baseload Power (Barsebäck, ~2 500 MWe, 4. støtteansøgning juni 2026). Kina, lagring, rum-pakke, tallet, snapshot udvidet.

