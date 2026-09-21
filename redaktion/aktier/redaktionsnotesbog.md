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

## Nr. 6 — kandidater / opfølgning

**(2026-09-29)** Nike Q1 FY27 — **BINÆRT**. Margin-stabilisering eller guide-down?

**(2026-10-03)** Constellation Brands Q2 FY27.

**(2026-10-15)** Pernod Ricard Q1 FY27-salgstal. Telenor ex-udbytte NOK 4,70.

**(2026-10-19)** Husqvarna ex-udbytte SEK 1,50.

**(2026-10-21)** Husqvarna Q3.

**(2026-10-22)** Yara Q3 — nitrogen og margin.

**(2026-10-23)** Volvo Cars Q3 — Kina-stabilisering?

**(2026-10-24)** Comcast Q3.

**(2026-10-27)** UPS Q3, Telenor udbyttebetaling.

**(2026-10-28)** Mercedes-Benz Q3 + PayPal Q3.

**(2026-10-30)** Capgemini Q3 + Wolters Kluwer Q3.

**(2026-11-04)** Novo Q3 + Ahold Q3.

**(2026-11-05)** Deutsche Telekom Q3.

**(2026-11-06)** Rockwool Q3.

**Følger (ikke feature endnu):**
- FISV — aktivist JANA, debit-talks. Feature hvis deal-nyt eller stabilisering.
- CHTR — for binær (D/E 441%, short 52%).
- NHY.OL — aluminium-cyklisk, optional follower.

## Log

- **2026-08-29:** Nr. 1 publiceret — *"Fem kandidater i et marked uden bred nedtur"*. Editor-led, ingen bylines, `productionCostUSD: 0`. Fem kandidater: NOVO-B, LULU, ZTS, RI.PA, BMW.
- **2026-08-31:** Nr. 2 publiceret — *"Fire dips, stadig intet udsalg i indekset"*. Editor-led, ingen bylines, `productionCostUSD: 0`. Fire nye kandidater: PYPL, YAR.OL, HUSQ-B.ST, AD.AS. Porteføljen følger nr. 1's fem navne. LULU Q2 3. sep er det aktive binære.
- **2026-09-07:** Nr. 3 publiceret — *"LULU invalideret — fem nye dips mens indekset holder toppen"*. Editor-led, ingen bylines, `productionCostUSD: 0`. **LULU exit** (guide-down, −17 % tab). Fem nye kandidater: NKE, DECK, BSX, VOLCAR-B.ST, MBG.DE. Porteføljen nu 9 aktive fra nr.1+nr.2 (minus LULU).
- **2026-09-14:** Nr. 4 publiceret — *"Comcast endelig med — Rockwool åbner København-siden"*. Editor-led, ingen bylines, `productionCostUSD: 0`. Fem nye kandidater: CMCSA, STZ, CAP.PA, WKL.AS, ROCK-B.CO. **Rockwool** er første rene CPH-kandidat udover Novo. Porteføljen nu 19 aktive (14 fra nr.1–3 + 5 nye). Ingen invalidationer.
- **2026-09-21:** Nr. 5 publiceret — *"Efter Fed: Adobe til rabat — yield i UPS, Sanofi, Telenor og Telekom"*. Editor-led, ingen bylines, `productionCostUSD: 0`. Fem nye kandidater: ADBE, UPS, SAN.PA, TEL.OL, DTE.DE. **Adobe** er første software-kandidat. Fire yield-navne (UPS 6,6%, SAN 5,4%, TEL 7,2%, DTE 3,5%). Porteføljen nu **24 aktive** (19 fra nr.1–4 + 5 nye). **NKE Q1 29. sep er binært** — hold uden exit før regnskab.
