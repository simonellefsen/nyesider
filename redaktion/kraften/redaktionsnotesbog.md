# KRAFTEN – Redaktionsnotesbog

Opdateret efter genopbygningen af nr. 2 (august 2026, *"Strøm overalt"*). Modelerfaringer: [modelkartotek](../modelkartotek.md).

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

## Research-regler

Tal med **kilde + årstal**. Skeln nameplate MW / TWh / planlagt / under byggeri / i drift.  
OpenRouter: **kun** `.env.kraften`. Imagine: `.env.local`.

## Log

- **2026-08-19:** Nr. 3 udgivet — 'Hvem får strømmen først?', nyt nummer produceret fra bunden.
  Se læringen ovenfor. Én kladde (svensk-atom) væsentligt opdateret før accept, da en opfølgende
  research fandt et nyere, mere præcist primærkilde-dokument end kladdens grundlag.

- **2026-08-08 (format):** Ordbogen fjernet fra nr. 2 — gloser i parentes/fodnote i features (ikke separat ordliste).


- **2026-08-08:** Nr. 2 publiceret — global elektrificering + rumkraft-pakke.
- **2026-08-01:** Notesbog udvidet med `## Format`.

- **2026-08-08 (edit):** KRAFTEN nr. 2 — forklaret *Fit for 55* og *IRA* i EU/USA-artiklen; udfoldet *PJM-agtige køer* i netflaskehalse; Sverige-atom omskrevet fra notes-kladde til færdig feature og flyttet **før** Ordbog/Rygtebørs (lå tidligere som sidste side efter bagsnit).
- **2026-08-08 (process):** Efter Sverige-kladde-uheldet: `production/check_issue.py` flagger nu **draft/production-meta** i publiceret brødtekst som ERROR; chefredaktør-tjekliste i [redaktion/README](../README.md) kræver eksplicit “færdig læsertekst” + jargon første gang + features før bagsnit.
- **2026-08-08 (depth):** Features stadig for korte efter batch. Indien: Læseregler væk → prosa. Sverige: flåde (6 reaktorer, Forsmark/Ringhals/Oskarshamn, ~50 TWh/~29 %) + Nordic Baseload Power (Barsebäck, ~2 500 MWe, 4. støtteansøgning juni 2026). Kina, lagring, rum-pakke, tallet, snapshot udvidet.

