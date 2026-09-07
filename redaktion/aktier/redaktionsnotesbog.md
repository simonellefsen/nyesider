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

## Nr. 4 — kandidater / opfølgning

**(2026-09-29)** Nike Q1 FY27 — margin-stabilisering?

**(2026-10-21)** Husqvarna Q3 + ex-div 19. okt.

**(2026-10-22)** Yara Q3 — nitrogen og margin.

**(2026-10-23)** Volvo Cars Q3 — Kina-stabilisering?

**(2026-10-28)** Mercedes-Benz Q3 + PayPal Q3.

**(2026-11-04)** Novo Q3 + Ahold Q3.

**Følger (ikke feature endnu):**
- FISV — aktivist JANA, debit-talks. Feature hvis deal-nyt.
- CHTR — for binær (D/E 441 %, short 52 %).
- CMCSA — near-miss, følger for evt. nr.4.

## Log

- **2026-08-29:** Nr. 1 publiceret — *"Fem kandidater i et marked uden bred nedtur"*. Editor-led, ingen bylines, `productionCostUSD: 0`. Fem kandidater: NOVO-B, LULU, ZTS, RI.PA, BMW.
- **2026-08-31:** Nr. 2 publiceret — *"Fire dips, stadig intet udsalg i indekset"*. Editor-led, ingen bylines, `productionCostUSD: 0`. Fire nye kandidater: PYPL, YAR.OL, HUSQ-B.ST, AD.AS. Porteføljen følger nr. 1's fem navne. LULU Q2 3. sep er det aktive binære.
- **2026-09-07:** Nr. 3 publiceret — *"LULU invalideret — fem nye dips mens indekset holder toppen"*. Editor-led, ingen bylines, `productionCostUSD: 0`. **LULU exit** (guide-down, −17 % tab). Fem nye kandidater: NKE, DECK, BSX, VOLCAR-B.ST, MBG.DE. Porteføljen nu 9 aktive fra nr.1+nr.2 (minus LULU).
