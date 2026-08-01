# KRAFTEN – Redaktionsnotesbog

Ny titel under Nye Sider (oprettet august 2026). Endnu intet udgivet nummer. Modelerfaringer: [modelkartotek](../modelkartotek.md).

## Identitet

**KRAFTEN** er magasinet om *hele* energisystemet — ikke kun grøn PR, ikke kun oliepessimisme. Vi dækker:

- **Atom:** klassisk fission (LWR/PWR/BWR), SMR, thorium-spor, fusionsprojekter (ITER, private demos)
- **Fossilt:** olie, gas (inkl. LNG), kul — produktion, handel, udfasning *og* realitet i forsyningssikkerhed
- **Vedvarende:** sol, vind (on-/offshore), vand, geotermi, biomasse hvor det er energimæssigt relevant
- **Lagring & net:** batterier, pumpelagring, brint/PtX, varme, transmission, flaskehalse
- **Geografi:** udbygning land for land med **tal** (GW, TWh, kapacitetsfaktorer, CAPEX-ordrer) — altid med kilde og årstal
- **Planer & byggeri:** nationale strategier, tilladelser, anlægsstatus (under konstruktion / forsinket / i drift)

**Tone:** nøgtern, datatung nok til at være nyttig, forklaret så en interesseret lægmand kan følge med. Vi er ikke en partsindlæg for én teknologi. Vi er imod slappe påstande uden tal.

**Afgrænsning over for SPÆNDING:** SPÆNDING = elbiler og ladeinfrastruktur. KRAFTEN = elproduktion, brændsler, system og storskala. Overlap (fx megawatt-ladning som *elforbrug*) kan nævnes, men biltesten hører hjemme i SPÆNDING.

**Længde pr. nummer:** 10–20 artikler. Mål ~12–16 i første numre (sidetal-disciplin: features 500–800 ord, bagsnit kortere + `flow: true`).

## Faste formater

| Format | Indhold |
|---|---|
| **Leder** | Chefredaktionens vinkel på måneden |
| **Tallet** | Ét nøgletal + 3–5 sætninger kontekst (GW, TWh, €/MWh, lagringstimer) |
| **Lande & udbygning** | Kort/tabel-agtig oversigt — 3–6 lande, samme nøgletal for sammenligning |
| **Byggeri & anlæg** | Status på konkrete projekter (hvem, hvor, MW, tidslinje, forsinkelse) |
| **Ordbogen** | 8–12 gloser (SMR, baseload, LCOE, curtailment, capacity factor …) |
| **Rygtebørsen** | Satire/rygter om selskaber, ministerier og teknologiløfter — aldrig navngivne privatpersoner |
| **Marked & priser** | Spot, forward, brændselspriser, subsidy-landskab — med forbehold |

## Udkast til nr. 1 (arbejdstitel: *"Hvad holder lyset tændt"*)

Mål: **14 artikler** (kan skæres til 12). Research-first; ingen opdigtede statistik-årstal.

1. **Leder** — Velkommen til KRAFTEN: system, ikke slagord  
2. **Overblik: Europas energimix 2025/26** — elproduktion fordelt (atom/gas/kul/vind/sol/vand) med kilder (Ember, Eurostat, IEA)  
3. **Atom: fission i 2026** — levetidsforlængelser, nybyggeri (Frankrig, UK, Tjekkiet, Polen …), SMR-status uden hype  
4. **Thorium: hype vs. hardware** — hvad der faktisk bygges/forskes, og hvad der stadig er PowerPoint  
5. **Fusion: ITER og de private** — tidslinjer, hvad "net energy" betyder, realistiske årstal  
6. **Gas: bro eller afhængighed** — LNG, europæiske terminaler, prischok-lektioner  
7. **Olie: stadig verdens blod** — transport, petrokemisk, peak-demand-debatten med tal  
8. **Vind: offshore-ordrebogen** — Nordsøen, auktioner, forsyningskæde (turbiner, kabler, skibe)  
9. **Sol: billig strøm, dyr integration** — LCOE vs. systemomkostninger, curtailment  
10. **Lagring: batterier, pumpelagring, brint** — hvad der skalerer nu vs. senere  
11. **Danmarksvinkel: forbrug, import, PtX-planer** — nøgletal fra Energistyrelsen / Dansk Energi  
12. **Lande & udbygning** — 5-lande-snapshot (fx DK, DE, FR, CN, US) samme indikatorer  
13. **Ordbogen** — 10 gloser  
14. **Rygtebørsen** — SMR-løfter, auktioner, "fusion om fem år (igen)"  

**Reserve / nr. 2-kandidater:** geotermisk i Europa · kul i Asien · netudbygning og flaskehalse · uranmarked · CCS på gasværker · varme (fjernvarme + industri).

## Research-regler (bindende)

- **Tal skal have kilde** (IEA, Ember, ENTSO-E, IRENA, Energistyrelsen, company filings, peer-reviewed).  
- **Årstal på al statistik** — aldrig "nu er X GW" uden periode.  
- **Skeln** nameplate GW vs. produktion TWh; planlagt vs. under konstruktion vs. i drift.  
- **Ingen opdigtede projektnavne** — hvis usikker, skriv "ifølge [kilde]" eller drop.  
- **Dansk først**, europæisk primært, global når det forklarer priser/forsyning.

## Praktisk til første produktion

1. Opret `.env.kraften` med egen OpenRouter-nøgle (gitignored).  
2. Brief features til 550–750 ord; bagsnit 200–400 + `flow: true`.  
3. Cover: mørk, industriel, amber accent — undgå stock "grøn blad på solpanel"-kliché; gerne net, reaktor-silhouette, turbiner *eller* blandet system.  
4. `content/kraften/issues/YYYY-MM-nr1/` med `issue.json` + artikler.  
5. PDF via `production/build_magazine.py kraften <issue-slug>`.  
6. Webappen opdager titlen automatisk via `magazine.json` (ingen route-kode).

## Status

- [x] `magazine.json` + brand  
- [x] Redaktionsnotesbog + nr. 1-outline  
- [ ] Første nummer produceret  
- [ ] Cover + PDF  
- [ ] OpenRouter-nøgle / cost tracking  
