# Aktier med Grok – Redaktionsnotesbog

Opdateret efter nr. 2 (august 2026, *"Fire dips, stadig intet udsalg i indekset"*).  
OpenRouter: **kun** `.env.aktier` (nøgle endnu ikke oprettet). Imagine: `.env.local`.

## Identitet

**Aktier der er faldet for langt, ser for billige ud, og har et argument for de næste 3–6 måneder.**

- Konkrete, kildedækkede købskandidater på NYSE, Nasdaq, Euronext, Nasdaq Copenhagen, Oslo Børs og Nasdaq Stockholm.
- Ikke gururåd, ikke "tips", ikke daytrading.
- Hård dokumentation: pris, 52-ugers interval, P/E (trailing og forward), P/B, EV/EBITDA, udbytte, og en præcis invalidation.
- Disclaimeren er ikke pynt — magasinet giver ikke personlig investeringsrådgivning.

**vs andre titler:** KRAFTEN dækker energiaktier som sektor; Aktier med Grok dækker værdiansættelse på tværs af sektorer. DOSIS dækker sundhed; vi dækker NOVO-B som aktie, ikke som medicin.

## Format

- **Artikeltal:** ~10–12 (inkl. Leder, Markedet, features, Tallet, ETF'erne, Porteføljen, Rygtebørsen, Bagsnit).
- **Ordmål:** 400–700 for features (kandidat-artikler), 150–250 for Leder, 400–600 for Markedet, 500–700 for Tallet (kildetabel).
- **Standard `mustCite`:** 2–3 for kandidat-features (Yahoo Finance + virksomhedskilde), 3+ for Markedet, 0 for Leder/Rygtebørsen.
- **Hårde tal i hver kandidat-artikel:** ticker, børs, pris, 52w interval, % fra top, P/E (trail/fwd), P/B, invalidation.
- **Jargon-forklaring:** P/E (*price-to-earnings*, kurs/indtjening), P/B (*price-to-book*, kurs/bogført værdi), EV/EBITDA, drawdown (fald fra toppen), forward P/E (forventet), trailing P/E (bagudrettet).
- **Sleeves:** CORE (stor position, høj overbevisning), SATELLITE (mindre position), BINARY (binært udfald, fx omkring regnskab), YIELD (udbyttefokus).

## Nr. 1 — udgivet (2026-08-29)

**Tema:** Fem kandidater i et marked uden bred nedtur  
**Editor-led:** Alle artikler skrevet af chefredaktionen uden byline. Ingen OpenRouter-kald. `productionCostUSD: 0`.

**Fem kandidater:**
1. **NOVO-B.CO** (Novo Nordisk, København) — DKK 295,50, −27,9 % fra top, trail P/E 11,25, CORE.
2. **LULU** (Lululemon, Nasdaq) — $120,81, −46,5 % fra top, trail P/E 9,31, SATELLITE/BINARY.
3. **ZTS** (Zoetis, NYSE) — $77,34, −50,2 % fra top, trail P/E 12,24, SATELLITE.
4. **RI.PA** (Pernod Ricard, Euronext Paris) — €63,20, −37,1 % fra top, yield 7,29 %, YIELD.
5. **BMW.DE** (BMW, Xetra) — €62,64, −36,0 % fra top, P/B 0,38, CYCLICAL.

## Nr. 2 — udgivet (2026-08-31)

**Tema:** Fire dips, stadig intet udsalg i indekset  
**Editor-led:** Alle artikler skrevet af chefredaktionen uden byline. Ingen OpenRouter-kald (`.env.aktier` endnu ikke oprettet). `productionCostUSD: 0`.

**Fire nye kandidater (pris 28. aug 2026 lukke):**
1. **PYPL** (PayPal, NasdaqGS) — $53,66 (−12,71 % fredag), −32,3 % fra top, trail P/E 11,62, SATELLITE. Deal-break washout.
2. **YAR.OL** (Yara International, Oslo Børs) — NOK 446,40, −25,5 % fra top, trail P/E 7,82, yield 4,93 %, YIELD.
3. **HUSQ-B.ST** (Husqvarna, Nasdaq Stockholm) — SEK 37,98, −29,7 % fra top, P/B 0,83 (under bog), SATELLITE.
4. **AD.AS** (Ahold Delhaize, Euronext Amsterdam) — €30,57, −28,1 % fra top, +0,8 % over 52w bund, yield 4,06 %, YIELD.

**Porteføljen (fra nr. 1):** NOVO-B, LULU, ZTS, RI.PA, BMW — alle uændret. LULU aflægger Q2 3. sep.

**Rygtebørsen (afviste):** FISV (følger, ikke feature), CHTR (D/E 441 %, short 51,6 %), ELUX-B.ST (dilution-fælde), STLAP.PA, ORCL, CMCSA, ERIC-B.ST, Ørsted.

**ETF-vurdering:** Ingen ETF anbefales. SPY/VOO −1,3 %, QQQ −4,3 %, EUNL −1,2 %, EXS1 −0,2 % (på top). Rabat kun i enkeltnavn.


## Produktion

```bash
python3 production/load_env.py aktier   # når .env.aktier oprettes
```

**Nøgle mangler:** `.env.aktier` er endnu ikke oprettet. Nr. 1 og nr. 2 er editor-led. Før kommissionerede artikler kan produceres, skal ejeren oprette en dedikeret OpenRouter-nøgle.

## Nr. 3 — udgivet (2026-09-07)

**Tema:** LULU invalideret — fem nye dips mens indekset holder toppen  
**Editor-led:** Alle artikler skrevet af chefredaktionen uden byline. Ingen OpenRouter-kald (`.env.aktier` endnu ikke oprettet). `productionCostUSD: 0`.

**LULU invalideret:**
- Q2 regnskab 3. sep 2026: omsætning −4 %, comps −10 %, FY-guide skåret til $10,35–10,50 mia.
- Aktien faldt 17,4 % til $100,61 (nu ~55 % under 52w top).
- Per notesbog-regel: guide-down = invalideret, ud af porteføljen.
- Tab fra nr.1: ~$120,81 → $100,61 = ~17 %.

**Fem nye kandidater (pris 4. sep 2026 lukke):**
1. **NKE** (Nike, NYSE) — $38,40, −50,1 % fra top, trail P/E 18,30, P/B 3,83, yield 4,3 %, SATELLITE.
2. **DECK** (Deckers/HOKA/UGG, NYSE) — $85,81, −31,3 % fra top, trail P/E ~12, P/B ~5, SATELLITE.
3. **BSX** (Boston Scientific, NYSE) — $47,80, −56,3 % fra top, trail P/E ~19, P/B ~2,7, SATELLITE.
4. **VOLCAR-B.ST** (Volvo Cars, Stockholm) — SEK 18,86, −48,4 % fra top, P/E 5,94, P/B 0,37, SATELLITE.
5. **MBG.DE** (Mercedes-Benz, Xetra) — €47,69, −23,5 % fra top, P/E 8,93, P/B ~0,49, yield 7,3 %, YIELD.

**Porteføljen (efter LULU exit):**
- Fra nr.1: NOVO-B (hold), ZTS (hold), RI.PA (hold), BMW.DE (hold).
- Fra nr.2: PYPL (+1 %), YAR.OL (+2 %), HUSQ-B.ST (+3 %), AD.AS (+4 %).
- 9 kandidater aktive fra nr.1+nr.2.

**Rygtebørsen (afviste):** CMCSA (−19 %, ikke nok rabat), BALD-B.ST (for illikvid), RNO.PA (foretrækker MBG), LULU som re-pick (nej).

**ETF-vurdering:** Ingen ETF anbefales. SPY −1,2 %, QQQ −3,9 %, EUNL −1,0 %. P/E ~25 på S&P 500. Rabat kun i enkeltnavn.

## Nr. 4 — udgivet (2026-09-14)

**Tema:** Comcast endelig med — Rockwool åbner København-siden  
**Editor-led:** Alle artikler skrevet af chefredaktionen uden byline. Ingen OpenRouter-kald (`.env.aktier` endnu ikke oprettet). `productionCostUSD: 0`.

**Fem nye kandidater (pris 11. sep 2026 lukke):**
1. **CMCSA** (Comcast, NasdaqGS) — $25,20, −23,3 % fra top, trail P/E 8,08, yield 5,24 %, CORE/YIELD.
2. **STZ** (Constellation Brands, NYSE) — $122,45, −27,4 % fra top, trail P/E 11,67, yield 3,36 %, CORE.
3. **CAP.PA** (Capgemini, Euronext Paris) — €102,9, −32,8 % fra top, trail P/E 13,1, fwd 7,5, CORE.
4. **WKL.AS** (Wolters Kluwer, Euronext Amsterdam) — €66,24, −43,6 % fra top, trail P/E 11,3, yield 3,9 %, CORE.
5. **ROCK-B.CO** (Rockwool, Nasdaq Copenhagen) — DKK 190,4, −22,2 % fra top, fwd P/E 12,6, yield 2,2 %, CORE.

**Porteføljen (fra nr.1+nr.2+nr.3):**
- Fra nr.1: NOVO-B (hold), ZTS (hold), RI.PA (hold), BMW.DE (hold).
- Fra nr.2: PYPL (+2 %), YAR.OL (+2 %), HUSQ-B.ST (+3 %), AD.AS (+1 %).
- Fra nr.3: NKE (−1 %), DECK (0 %), BSX (0 %), VOLCAR-B.ST (+1 %), MBG.DE (−1 %).
- 14 kandidater aktive fra nr.1+nr.2+nr.3, ingen invalidationer.

**Rygtebørsen (afviste):** FISV (−62 %, falling knife), UPS (−18 %, under screen), DG (P/E ~16), BALD-B (illikvid), CHTR (leverage veto), CPB/CAG/GIS (value-trap), STLAP/ELUX (traps), ERIC (ikke billig), ORSTED (ingen trail P/E), RNO/VOW3 (auto-overlap), COLO/AMBU/GN (dyre).

**ETF-vurdering:** Ingen ETF anbefales. SPY −1,9 %, QQQ −4,5 %, OMXS30 −0,4 %. P/E ~24,7 på S&P 500. Rabat kun i enkeltnavn.

## Nr. 5 — udgivet (2026-09-21)

**Tema:** Efter Fed: Adobe til rabat — yield i UPS, Sanofi, Telenor og Telekom  
**Editor-led:** Alle artikler skrevet af chefredaktionen uden byline. Ingen OpenRouter-kald (`.env.aktier` endnu ikke oprettet). `productionCostUSD: 0`.

**Fem nye kandidater (pris 18. sep 2026 lukke):**
1. **ADBE** (Adobe, NasdaqGS) — $248,92 (−32,8% fra 52w top $370,31). Trail P/E 15,0, fwd 10,0, P/B 8,9 (asset-light), ingen udbytte. CORE. GenAI-frygt vs. 90% recurring.
2. **UPS** (United Parcel Service, NYSE) — $99,06 (−19,1% fra 52w top $122,41). Trail P/E 15,1, fwd 12,5, yield 6,6%. CORE/YIELD. Near-miss i nr.4, nu klar.
3. **SAN.PA** (Sanofi, Euronext Paris) — €74,05 (−18,8% fra 52w top €91,15). Trail P/E 19,3, **fwd 8,7**, P/B 1,33, yield 5,4%. CORE/YIELD. Dupixent-pipeline.
4. **TEL.OL** (Telenor, Oslo Børs) — NOK 132,00 (−26,1% fra 52w top NOK 178,70). Trail P/E 11,3, yield 7,2%. YIELD. Defensiv nordisk cash.
5. **DTE.DE** (Deutsche Telekom, Xetra) — €27,11 (−21,1% fra 52w top €34,36). Trail P/E 15,8, fwd 11,8, yield 3,5%. CORE/YIELD. ~50% T-Mobile US.

**Porteføljen (fra nr.1+nr.2+nr.3+nr.4):**
- Fra nr.1: NOVO-B (hold), ZTS (hold, nær low), RI.PA (hold), BMW.DE (hold).
- Fra nr.2: PYPL (hold), YAR.OL (hold), HUSQ-B.ST (hold), AD.AS (hold).
- Fra nr.3: NKE (**BINÆRT** Q1 29. sep), DECK (hold), BSX (hold, nær low), VOLCAR-B.ST (hold, nær low), MBG.DE (hold).
- Fra nr.4: CMCSA (hold), STZ (hold), CAP.PA (hold), WKL.AS (hold), ROCK-B.CO (hold).
- 19 kandidater aktive fra nr.1–4 + 5 nye = **24 i alt**.

**Rygtebørsen (afviste):** FISV (falling knife), DSV.CO (P/E 40+), KER.PA (earnings stress), IFX.DE (ekstrem P/E), MC.PA (luxury derating), DG (value trap), ADS.DE/PUM (NKE overlap), ORSTED.CO (ingen P/E), ERIC-B (ikke billig), F/VOW3 (auto overlap), BN.PA (P/E 20+), INTC (AI-kompleks).

**ETF-vurdering:** Ingen ETF anbefales. SPY −2,3%, QQQ −3,6%, EUNL −2,2%. Rabat kun i enkeltnavn.

## Nr. 6 — udgivet (2026-09-28)

**Tema:** Intuit-vask — Pepsi, Lowe's og Orkla mens Nike venter  
**Editor-led:** Alle artikler skrevet af chefredaktionen uden byline. Ingen OpenRouter-kald (`.env.aktier` endnu ikke oprettet). `productionCostUSD: 0`.

**Fem nye kandidater (pris 25. sep 2026 lukke):**
1. **INTU** (Intuit, NasdaqGS) — $275,79 (−60,8% fra 52w top $703,96). Trail P/E 16,8, fwd 10,2, P/B 3,90, yield 1,7%. CORE. GenAI + Free File frygt vs. 90% recurring.
2. **PEP** (PepsiCo, NasdaqGS) — $128,63 (−25,0% fra 52w top $171,51). Trail P/E 16,9, fwd 14,4, P/B 7,95, yield 4,5%. CORE/YIELD. Volumen-frygt vs. Dividend King.
3. **LOW** (Lowe's, NYSE) — $189,28 (−35,4% fra 52w top $293,02). Trail P/E 16,0, fwd 14,5, yield 2,6%. CORE. Billigere end HD.
4. **ORK.OL** (Orkla, Oslo Børs) — NOK 93,35 (−28,8% fra 52w top NOK 131,11). Trail P/E 14,2, fwd 13,6, P/B 1,92, yield 4,3%. YIELD. Nordisk staples.
5. **PHIA.AS** (Philips, Euronext Amsterdam) — €21,87 (−21,0% fra 52w top €27,68). Trail P/E 19,2, fwd 13,0, P/B 1,87, yield 4,0%. CORE/YIELD. Health-tech recovery.

**Porteføljen (fra nr.1+nr.2+nr.3+nr.4+nr.5):**
- Fra nr.1: NOVO-B (hold), ZTS (hold, nær low), RI.PA (hold), BMW.DE (hold).
- Fra nr.2: PYPL (hold), YAR.OL (hold), HUSQ-B.ST (hold, nær low), AD.AS (hold).
- Fra nr.3: NKE (**BINÆRT Q1 29. sep — I MORGEN!**), DECK (hold), BSX (hold, nær low), VOLCAR-B.ST (hold, nær low), MBG.DE (hold).
- Fra nr.4: CMCSA (hold, nær low), STZ (hold), CAP.PA (hold), WKL.AS (hold), ROCK-B.CO (hold).
- Fra nr.5: ADBE (hold), UPS (hold), SAN.PA (hold), TEL.OL (hold), DTE.DE (hold).
- 24 kandidater aktive fra nr.1–5 + 5 nye = **29 i alt**.

**Rygtebørsen (afviste):** FISV (−64%, falling knife), NOW (P/E ~85), ORCL (AI-kompleks), EL (absurd P/E), BA (ingen earnings), SHOP/CMG (rig), DG (value-trap), FDX (UPS overlap), HD (richer end LOW), TOM.OL (cyklisk), COLO-B (dyr), MC/KER (luxury), EQT.ST (P/B ekstrem), SAP (P/E 28), UNA (mild dip), WMT (P/E 39), LULU (ingen re-pick).

**ETF-vurdering:** Ingen ETF anbefales. SPY −1,0%, QQQ −0,6%, EUNL −0,7%. Indekserne ved toppen. Rabat kun i enkeltnavn.

## Nr. 7 — udgivet (2026-10-05)

**Tema:** Regnskabsdag: ni ud, tre ind — vi rydder op i porteføljen  
**Editor-led:** Alle artikler skrevet af chefredaktionen uden byline. Ingen OpenRouter-kald (`.env.aktier` endnu ikke oprettet). `productionCostUSD: 0`.

**RETTELSE:** Nr. 4, 5 og 6 skrev fejlagtigt "ingen invalidationer" — ni kandidater var allerede invalideret på pris. Korrekt antal var 28, ikke 29. Nike Q1 FY27 blev aflagt 1. okt, ikke 29. sep.

**Ni invaliderede (pris-baseret):**
1. **ZTS** (nr. 1) — niveau $71, brud 24. sep, lukke $69,69, −9,9 %
2. **BMW.DE** (nr. 1) — niveau €56,40, brud 25. sep, lukke €54,32, −13,3 %
3. **HUSQ-B.ST** (nr. 2) — niveau SEK 34,19, brud 24. sep, lukke SEK 34,74, −8,5 %
4. **NKE** (nr. 3) — niveau $38, brud 9. sep, lukke $33,87, −11,8 %
5. **BSX** (nr. 3) — niveau $45, brud 8. sep, lukke $42,60, −10,9 %
6. **DECK** (nr. 3) — niveau $78,91, brud 15. sep, lukke $79,12, −7,8 %
7. **VOLCAR-B.ST** (nr. 3) — niveau SEK 18, brud 18. sep, lukke SEK 14,18, −24,8 %
8. **MBG.DE** (nr. 3) — niveau €42, brud 24. sep, lukke €39,72, −16,7 %
9. **STZ** (nr. 4) — niveau $120,25, brud 18. sep, lukke $112,87, −7,8 %

**Tre nye kandidater (pris 2. okt 2026 lukke):**
1. **ACN** (Accenture, NYSE) — $198,90, −31,7 % fra top, trail P/E 15,9, fwd 12,5, yield 3,4 %, CORE. Q4 FY26 beat.
2. **BKNG** (Booking Holdings, NasdaqGS) — $159,02, −29,3 % fra top, trail P/E 17,6, fwd 12,9, yield 1,1 %, SATELLITE. AI-agent-frygt.
3. **RBREW.CO** (Royal Unibrew, København) — DKK 405,40, −38,0 % fra top, trail P/E 12,4, fwd 10,7, yield 4,0 %, CORE/YIELD. Første nye CPH-kandidat siden Rockwool.

**Porteføljen (efter oprydning):**
- **19 aktive fra nr. 1–6:** NOVO-B, RI.PA, PYPL, YAR.OL, AD.AS, CMCSA, CAP.PA, WKL.AS, ROCK-B, ADBE, UPS, SAN.PA, TEL.OL, DTE.DE, INTU, PEP, LOW, ORK.OL, PHIA.AS.
- **3 nye i nr. 7:** ACN, BKNG, RBREW.CO.
- **22 aktive i alt.**

**Track record (ærligt):**
- Snit alle 28 kandidater: **−6,3 %**
- SPY i samme periode: **~0 %**
- EUNL i samme periode: **~+1,8 %**
- Indekset slog vores kandidater.

**Lærdom:** At købe navne *på* 52-ugers bund uden bundformation producerede for mange faldende knive. Fra nr. 7: krav om bekræftet højere bund eller indtruffet katalysator, invalidation stramt under synlig støtte, færre navne.

## Nr. 8 — udgivet (2026-10-12)

**Tema:** SpaceX-chokket: telekom i frit fald — vi køber ikke kniven  
**Editor-led:** Alle artikler skrevet af chefredaktionen uden byline. Ingen OpenRouter-kald (`.env.aktier` endnu ikke oprettet). `productionCostUSD: 0`.

**RI.PA INVALIDERET:**
- Pernod Ricard lukkede €58,04 mandag 5. oktober 2026 — under invalidationsniveauet €58,60.
- Nr. 7 flagede den ved €58,62 den 2. oktober.
- Ved brud: −8,2 % fra entry (€63,20). Ved 9. okt (€61,60): −2,5 %.
- Exit bekræftet. Ingen re-entry (samme regel som LULU/HUSQ/DECK).

**SpaceX telekomchok (8.–9. oktober 2026):**
- SpaceX aftalte køb af 800 MHz lavbånds-spektrum fra Grain Management (~$8 mia.).
- TMUS −13,3 %, VZ −8,8 %, T −9,8 % på fredag 9. oktober.
- Samlet tab: ~$58 mia. markedsværdi.
- DTE.DE (vores nr. 5) faldt −7,9 % til €24,70 (−8,9 % fra entry).
- CMCSA (vores nr. 4) ramte 52w bund $20,66 (−18,0 % fra entry).
- Vi køber IKKE TMUS/VZ/T — følger, venter på bekræftet bund.

**Én ny kandidat:**
1. **CCL** (Carnival, NYSE) — $26,35, −22,6 % fra top, +20,9 % over bund (24. sep $21,79), trail P/E 11,6, fwd 10,3, yield 1,7 %, SATELLITE. Q3 beat-and-raise 29. sep. Invalidation lukke < $22,14.

**Ærligt scorecard (31 kandidater, nr. 1–7):**
- Snit: **−3,8 %**
- I plus: **8 af 31**
- Indekset slog os igen.
- Kun nr. 7 foran SPY/EUNL — én uge, for tidligt at konkludere.

**Rettelse:** Nr. 7 skrev "Comcast Q3 24. oktober". Korrekt: **22. oktober** (24. okt er lørdag).

**Porteføljen nu:** 21 aktive fra nr. 1–7 (efter RI.PA exit) + 1 ny = **22 aktive kandidater**.

## Nr. 9 — udgivet (2026-10-19)

**Tema:** Chipkrakket: Nasdaq −4,5 %, vores kandidater +3,7 % — og vi køber intet  
**Editor-led:** Alle artikler skrevet af chefredaktionen uden byline. Ingen OpenRouter-kald (`.env.aktier` endnu ikke oprettet). `productionCostUSD: 0`.

**INGEN NYE KANDIDATER** — dette er en bevidst, ærlig beslutning:
- Screen-resultat: navne der faldt mest har ingen bund; navne med bund er enten i porteføljen eller har regnskab inden for dage.
- Et ærligt "ingen nye køb" er systemet der virker, ikke en mangel.
- Følgelisten-feature erstatter kandidat-feature: TMUS, VZ, T, CTSH, COF, BOL.ST — alle følges, ingen købes.

**Chip-crash (uge 12–16. okt):**
- SMH −10 % på ugen (største ugefald siden april 2025).
- Nasdaq Composite −4,5 %, S&P 500 −2,0 %.
- ASML/TSMC rapporterede stærke tal → faldende priser (markedet prissætter cyklen).

**Ærligt scorecard (lukkekurs 16. okt 2026):**
- Alle 32 kandidater (nr. 1–8): **+0,4 %** (16 af 32 i plus) — første positive snit.
- 22 aktive: **+2,7 %** siden publikation (13 af 22 i plus).
- Sidste uge (9.–16. okt): 22 aktive **+3,7 %**, 20 af 22 i plus. SPY −2,0 %, EUNL −0,8 %.
- Nr. 4, 6 og 7 nu foran både SPY og EUNL over deres respektive perioder.
- Foran SPY (−0,6 % pick-matchet), bagud af EUNL (+2,0 % pick-matchet).

**Bedste aktive:** WKL.AS +23,1 %, CAP.PA +17,9 %, INTU +17,9 %, ACN +15,5 % (+9,9 % sidste uge).  
**Værste aktive:** CMCSA −13,1 %, NOVO-B −12,1 %, YAR.OL −7,7 %.

**Alle 10 exits steget siden salg (Tallet):**
- STZ +16,4 %, ZTS +13,9 %, RI.PA +10,7 %, NKE +9,6 %, DECK +8,3 %, BMW.DE +5,0 %, BSX +4,2 %, MBG.DE +3,4 %, HUSQ-B.ST +2,8 %, VOLCAR-B.ST +0,1 %.
- RI.PA: én lukke under niveau (€58,04 den 5. okt), nu €68,22 (+17,5 % fra bund, +7,9 % over entry).
- **Åbent spørgsmål:** er single-close-reglen for stram? Evalueres før nr. 10 (ikke ny regel).

**RETTELSER fra nr. 8:**
- Booking Holdings Q3: ~27. okt → **3. november** efter US-lukke
- PayPal Q3: 28. okt → **27. oktober** før US-åbning
- Rockwool Q3: 6. nov → **25. november**

**Invalidationer denne uge: INGEN.** Alle prisniveauer holdt.

**Porteføljen efter nr. 9:** 22 aktive (samme som nr. 8 — ingen exits, ingen nye).

## Nr. 10 — udgivet (2026-10-26)

**Tema:** Volvo Car −25 % på en uge: exitten holdt — og vi køber Balder til halv substans  
**Editor-led:** Alle artikler skrevet af chefredaktionen uden byline. Ingen OpenRouter-kald (`.env.aktier` endnu ikke oprettet). `productionCostUSD: 0`.

**VOLVO CAR Q3 (23. oktober 2026):**
- Driftstab SEK 5,6 mia. (mod overskud SEK 6,4 mia. året før)
- Omsætning SEK 66,9 mia.
- Trak forward-looking statements, annoncerede SEK 5 mia. besparelser, ~2.500 stillinger
- Aktien faldt ~28–30 % den dag, lukkede ugen −24,6 % til SEK 10,70
- Vores nr. 7-exit (18. sep < SEK 18,00) undgik −43 % vs entry (kun −11 % ved exit)
- **Single-close-reglen holdt.** Beslutning: vi holder reglen uændret.

**ÉN NY KANDIDAT:**
1. **BALD-B.ST** (Balder, Nasdaq Stockholm) — SEK 49,02 (lukke 23. okt), **SATELLITE**
   - ~50 % af langsigtede NAV (EPRA NRV SEK 97,03)
   - P/B 0,60, trail P/E 10,6, fwd P/E 9,4
   - Q3 i linje med konsensus: lejeindtægter +5,7 %, driftsoverskud +5,9 %
   - Bekræftet bund: SEK 43,51 (12. okt), derefter +12,7 % før Q3
   - Risici: LTV 50,2 %, rentefølsomhed, EPS faldt
   - **Invalidation:** lukke < SEK 43,50

**Scorecard (lukkekurs 23. okt):**
- Alle 32 kandidater: **+1,4 %**, 17 af 32 i plus
- 22 aktive: **+5,1 %** siden publikation, 14 af 22 i plus
- Sidste uge: **+2,2 %**, 18 af 22 i plus (SPY −0,4 %, EUNL −0,5 %)

**Invalidationer denne uge: INGEN.** BKNG lukker kun 1,1 % over niveau — Q3 3. nov er binært.

**Porteføljen efter nr. 10:** **23 aktive** (22 fra nr. 1–8 + BALD-B.ST).

## Nr. 11 — kandidater / opfølgning

**(2026-10-26)** Verizon Q3 (følger).

**(2026-10-27)** **PayPal Q3**. UPS Q3.

**(2026-10-27–28)** FOMC.

**(2026-10-28)** T-Mobile US Q3 (følger); Telenor Q3 (følger); Alphabet Q3.

**(2026-10-29)** Cognizant Q3 + Boliden Q3 (følgere).

**(2026-10-30)** Sanofi Q3; Capgemini Q3; Wolters Kluwer Q3 (forventet).

**(2026-11-03)** **Booking Holdings Q3 — BINÆRT** (1,1 % over niveau!). Fiserv Q3 (kandidat?). Philips Q3. US midtermsvalg.

**(2026-11-04)** Novo Nordisk Q3 + Ahold Delhaize Q3 + FIS Q3.

**(2026-11-05)** Deutsche Telekom Q3.

**(2026-11-06)** Orkla Q3 + Charter Q3.

**(2026-11-10)** US oktober-CPI.

**(2026-11-11)** **Royal Unibrew Q3 — BINÆRT**.

**(2026-11-18)** Lowe's Q3.

**(2026-11-19)** Intuit Q3 (forventet).

**(2026-11-25)** **Rockwool Q3**.

**(2026-12-09)** Adobe Q4.

**(2026-12-17)** ACN Q1 FY27.

**(2026-12-18)** CCL Q4 (forventet, ubekræftet).

**Følger (ikke feature endnu):**
- TMUS/VZ/T — telekom. TMUS nyt 52w closing low ($146,54). Ingen bekræftet bund endnu.
- FISV/FIS — højere lav, Q3 3.–4. nov, kandidater for nr. 11–12.
- BOL.ST (Boliden) — −33,6 %, P/E 10,9, −9,4 % før Q3 29. okt. Metals-cyklisk.
- CTSH (Cognizant) — −19 %, fwd 11, IT-koncentration. Q3 29. okt.
- COF (Capital One) — −22,5 %, fwd 8,4. Q3 aflagt 20. okt, finanssektoren faldt fredag.
- EPAM — samme logik som CTSH.
- CHTR — leverage veto (D/E >400 %, short >50 %).
- NHY.OL — på 52w lav (−44 %), ingen bund.
- Europæiske banker (BNP.PA, GLE.PA, ACA.PA) — RSI <30, ingen bund.
- PRX.AS, MC.PA — stadig på 52w lavpunkter.

**Afviste:**
- MKC — trail P/E 8,7 men fwd P/E 14,9 (engangseffekt).
- CPB — value-trap (36 % udbyttenedsættelse, leverage).
- LULU/NKE/RI.PA — ingen re-entry (magasinregel).

## Log

- **2026-08-29:** Nr. 1 publiceret — *"Fem kandidater i et marked uden bred nedtur"*. Editor-led, ingen bylines, `productionCostUSD: 0`. Fem kandidater: NOVO-B, LULU, ZTS, RI.PA, BMW.
- **2026-08-31:** Nr. 2 publiceret — *"Fire dips, stadig intet udsalg i indekset"*. Editor-led, ingen bylines, `productionCostUSD: 0`. Fire nye kandidater: PYPL, YAR.OL, HUSQ-B.ST, AD.AS. Porteføljen følger nr. 1's fem navne. LULU Q2 3. sep er det aktive binære.
- **2026-09-07:** Nr. 3 publiceret — *"LULU invalideret — fem nye dips mens indekset holder toppen"*. Editor-led, ingen bylines, `productionCostUSD: 0`. **LULU exit** (guide-down, −17 % tab). Fem nye kandidater: NKE, DECK, BSX, VOLCAR-B.ST, MBG.DE. Porteføljen nu 9 aktive fra nr.1+nr.2 (minus LULU).
- **2026-09-14:** Nr. 4 publiceret — *"Comcast endelig med — Rockwool åbner København-siden"*. Editor-led, ingen bylines, `productionCostUSD: 0`. Fem nye kandidater: CMCSA, STZ, CAP.PA, WKL.AS, ROCK-B.CO. **Rockwool** er første rene CPH-kandidat udover Novo. Porteføljen nu 19 aktive (14 fra nr.1–3 + 5 nye). Ingen invalidationer.
- **2026-09-21:** Nr. 5 publiceret — *"Efter Fed: Adobe til rabat — yield i UPS, Sanofi, Telenor og Telekom"*. Editor-led, ingen bylines, `productionCostUSD: 0`. Fem nye kandidater: ADBE, UPS, SAN.PA, TEL.OL, DTE.DE. **Adobe** er første software-kandidat. Fire yield-navne (UPS 6,6%, SAN 5,4%, TEL 7,2%, DTE 3,5%). Porteføljen nu **24 aktive** (19 fra nr.1–4 + 5 nye). **NKE Q1 29. sep er binært** — hold uden exit før regnskab.
- **2026-09-28:** Nr. 6 publiceret — *"Intuit-vask — Pepsi, Lowe's og Orkla mens Nike venter"*. Editor-led, ingen bylines, `productionCostUSD: 0`. Fem nye kandidater: INTU, PEP, LOW, ORK.OL, PHIA.AS. **Intuit** er største drawdown (−61%). Fire yield-navne (PEP 4,5%, ORK 4,3%, PHIA 4,0%, LOW 2,6%). Porteføljen nu **29 aktive** (24 fra nr.1–5 + 5 nye). **NKE Q1 29. sep er i morgen** — binært.
- **2026-10-05:** Nr. 7 publiceret — *"Regnskabsdag: ni ud, tre ind — vi rydder op i porteføljen"*. Editor-led, ingen bylines, `productionCostUSD: 0`. **RETTELSE** af nr. 4–6's fejl om invalidationer. **Ni invalideret** (ZTS, BMW, HUSQ, NKE, BSX, DECK, VOLCAR, MBG, STZ). Tre nye kandidater: ACN, BKNG, RBREW.CO. **ACN** er første +60%-over-bund kandidat (bekræftet vending). **RBREW** er anden CPH-kandidat efter Rockwool. Track record −6,3 % vs. SPY ~0 % — indekset slog os. Porteføljen nu **22 aktive** (19 fra nr.1–6 + 3 nye).
- **2026-10-05 (post-merge rettelse):** SVG-filer rettet for UTF-8-kodningsfejl (cp1252 → UTF-8) og XML-well-formedness. Artikler 02–05, 07 og 10 rettet: fjernet usourcerede tal (ACN-medarbejdere, 65 %→57 %, Booking 90 % hotel, targets $230–250/$180–200/DKK 450–480), DAX-niveau korrigeret (21.918→25.231), falsk Reuters-fodnote erstattet med Boursier/TrustFinance, CAC 40/Vinci-kausalitet præciseret, udgivelsesdag søndag→mandag.
- **2026-10-12:** Nr. 8 publiceret — *"SpaceX-chokket: telekom i frit fald — vi køber ikke kniven"*. Editor-led, ingen bylines, `productionCostUSD: 0`. **RI.PA exit** (€58,04 < €58,60 den 5. okt). **SpaceX telekomchok** (TMUS −13%, VZ −9%, T −10%). DTE.DE −7,9%, CMCSA −18% (holder, fundamental inv.). **Én ny kandidat: CCL** (Carnival, SATELLITE, Q3 beat-and-raise). Vi køber ikke TMUS/VZ/T — shock-day lav er præcis hvad vi stoppede med at købe. **Rettelse:** Comcast Q3 er 22. okt, ikke 24. okt (lørdag). **Ærligt scorecard:** 31 kandidater snit −3,8%, 8 i plus. Indekset slog os igen. Porteføljen nu **22 aktive** (21 fra nr.1–7 + 1 ny).
- **2026-10-19:** Nr. 9 publiceret — *"Chipkrakket: Nasdaq −4,5 %, vores kandidater +3,7 % — og vi køber intet"*. Editor-led, ingen bylines, `productionCostUSD: 0`. **INGEN NYE KANDIDATER** — ærlig beslutning: faldende navne har ingen bund, bundnavne har regnskab inden for dage. **Chip-crash:** SMH −10 % uge (største siden apr 2025), Nasdaq −4,5 %. **Portefølje:** +3,7 % uge, 20 af 22 i plus. **Alle-picks snit +0,4 %** — første positive. **10 af 10 exits steget**: STZ +16,4 % til RI.PA +10,7 %. RI.PA +17,5 % fra single-close-bund — åbent spørgsmål om reglen. **Tre rettelser**: Booking Q3 = 3. nov, PayPal Q3 = 27. okt, Rockwool Q3 = 25. nov. Porteføljen stadig **22 aktive**.
- **2026-10-26:** Nr. 10 publiceret — *"Volvo Car −25 % på en uge: exitten holdt — og vi køber Balder til halv substans"*. Editor-led, ingen bylines, `productionCostUSD: 0`. **VOLVO CAR Q3**: driftstab SEK 5,6 mia., aktien −24,6 % på ugen. Vores nr. 7-exit (18. sep) undgik −43 % vs entry. **Single-close-reglen holdt** — beslutning: vi holder reglen uændret. **Én ny kandidat: BALD-B.ST** (Balder, SATELLITE, ~50 % af NAV, invalidation < SEK 43,50). Scorecard: 32 kandidater +1,4 % (17 i plus), 22 aktive +5,1 % siden pub, +2,2 % uge (18 af 22 i plus). **BKNG 1,1 % over niveau — Q3 3. nov er BINÆRT.** Ingen invalidationer. Porteføljen nu **23 aktive** (22 + Balder).
