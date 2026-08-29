# Aktier med Grok – Redaktionsnotesbog

Opdateret efter nr. 1 (august 2026, *"Fem kandidater i et marked uden bred nedtur"*).  
OpenRouter: **kun** `.env.aktier` (nøgle endnu ikke oprettet). Imagine: `.env.local`.

## Identitet

**Aktier der er faldet for langt, ser for billige ud, og har et argument for de næste 3–6 måneder.**

- Konkrete, kildedækkede købskandidater på NYSE, Nasdaq, Euronext, Nasdaq Copenhagen, Oslo Børs og Nasdaq Stockholm.
- Ikke gururåd, ikke "tips", ikke daytrading.
- Hård dokumentation: pris, 52-ugers interval, P/E (trailing og forward), P/B, EV/EBITDA, udbytte, og en præcis invalidation.
- Disclaimeren er ikke pynt — magasinet giver ikke personlig investeringsrådgivning.

**vs andre titler:** KRAFTEN dækker energiaktier som sektor; Aktier med Grok dækker værdiansættelse på tværs af sektorer. DOSIS dækker sundhed; vi dækker NOVO-B som aktie, ikke som medicin.

## Format

- **Artikeltal:** ~10–12 (inkl. Leder, Markedet, features, Tallet, ETF'erne, Rygtebørsen, Bagsnit).
- **Ordmål:** 400–700 for features (kandidat-artikler), 150–250 for Leder, 400–600 for Markedet, 500–700 for Tallet (kildetabel).
- **Standard `mustCite`:** 2–3 for kandidat-features (Yahoo Finance + virksomhedskilde), 3+ for Markedet, 0 for Leder/Rygtebørsen.
- **Hårde tal i hver kandidat-artikel:** ticker, børs, pris, 52w interval, % fra top, P/E (trail/fwd), P/B, invalidation.
- **Jargon-forklaring:** P/E (*price-to-earnings*, kurs/indtjening), P/B (*price-to-book*, kurs/bogført værdi), EV/EBITDA, drawdown (fald fra toppen), forward P/E (forventet), trailing P/E (bagudrettet).
- **Sleeves:** CORE (stor position, høj overbevisning), SATELLITE (mindre position), BINARY (binært udfald, fx omkring regnskab).

## Nr. 1 — udgivet (2026-08-29)

**Tema:** Fem kandidater i et marked uden bred nedtur  
**Editor-led:** Alle artikler skrevet af chefredaktionen uden byline. Ingen OpenRouter-kald (`.env.aktier` endnu ikke oprettet). `productionCostUSD: 0`.

**Research-baggrund (pris 28. aug 2026 lukke):**

Markedet er ikke i udsalg. S&P 500 er kun −1,3 % fra 52-ugers top, DAX er −0,2 %, OMXC25 er −1,1 %. Muligheden ligger i enkeltnavn, ikke brede indekser.

**Fem kandidater:**

1. **NOVO-B.CO** (Novo Nordisk, København) — DKK 295,50, −27,9 % fra top, trail P/E 11,25, fwd 13,48, P/B 5,90. CORE. Invalidation: DKK 224.
2. **LULU** (Lululemon, Nasdaq) — $120,81, −46,5 % fra top, trail P/E 9,31, fwd 10,32, P/B 2,71. SATELLITE, BINARY (Q2 3. sep). Invalidation: $104,44.
3. **ZTS** (Zoetis, NYSE) — $77,34, −50,2 % fra top, trail P/E 12,24, fwd 12,11, P/B 9,85 (ikke billig på bog). SATELLITE. Invalidation: $71.
4. **RI.PA** (Pernod Ricard, Euronext Paris) — €63,20, −37,1 % fra top, trail P/E 11,53, fwd 10,16, P/B 1,05, udbytte 7,29 %. SATELLITE/YIELD. Invalidation: €58,60 eller udbyttenedsættelse.
5. **BMW.DE** (BMW, Xetra) — €62,64, −36,0 % fra top, trail P/E 5,77, fwd 9,02, P/B 0,38 (BVPS €159), udbytte 7,34 %. SATELLITE/CYCLICAL. Invalidation: €56,40 eller udbyttenedsættelse.

**ETF-vurdering:** Ingen ETF er bedre end enkeltaktierne. SPY, VOO, QQQ, EUNL, EXS1, XACTC25 og XACT-OMXS30 ligger alle tæt på 52-ugers top. XACTC25 har ~16 % Novo og fortynder dermed dippen.

**Afviste navne (Rygtebørsen):** NKE, DKS, ORSTED, VWS, STLA, KER, LVMH, EQNR, COLO-B m.fl.

## Nr. 2 — kandidater

- **(2026-09)** Opfølgning på LULU efter Q2 (3. sep) — guide-down = invalideret, guide-up = CORE.
- **(2026-09)** Novo Q3 (4. nov kommende) — forbered update til oktober/november.
- **(2026-09)** BMW og RI.PA: hold øje med kinesisk efterspørgsel, tariffer, udbyttepolitik.
- **(2026-09)** Screen for nye kandidater: farmakoncerner efter patentudløb, nordiske small-caps, japanske eksportører (yen svag?).

## Produktion

```bash
python3 production/load_env.py aktier   # når .env.aktier oprettes
```

**Nøgle mangler:** `.env.aktier` er endnu ikke oprettet. Første nummer er editor-led. Før kommissionerede artikler kan produceres, skal ejeren oprette en dedikeret OpenRouter-nøgle.

## Log

- **2026-08-29:** Nr. 1 publiceret — *"Fem kandidater i et marked uden bred nedtur"*. Editor-led, ingen bylines, `productionCostUSD: 0`. Fem kandidater: NOVO-B, LULU, ZTS, RI.PA, BMW. Alle priser verificeret mod Yahoo Finance 28. aug lukke. Ingen ETF anbefales — alle ligger tæt på 52w top.
