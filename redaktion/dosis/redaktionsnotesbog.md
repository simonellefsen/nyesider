# DOSIS – Redaktionsnotesbog

*Ny titel · endnu ikke udgivet. OpenRouter: **kun** `.env.dosis`. Imagine: `.env.local` / `XAI_API_KEY`.*

## Identitet

**DOSIS** er magasinet om **levetid, generel sundhed og det, vi putter i og på kroppen** — med nysgerrighed, skepsis og kildekrav.

### Hvad vi dækker

| Spor | Eksempler |
|------|-----------|
| **Gennembrud & forskning** | Kliniske studier, lægemidler, biomarkører, “har det egentlig evidens?” |
| **Longevity** | Aldring, senolytics-hype vs. data, søvn, inflammation, livsstil der måles |
| **Ernæring & kost** | Makro/mikro, diæter (Middelhav, plantebaseret, keto m.fl.), mætheds- og blodsukker-logik |
| **Mad i praksis** | Tallerkenen, ikke kun papers — hvad man *spiser*, priser, vaner i DK |
| **Protein & træning** | Behov, pulver, timing, sarkopeni, ældre vs. atleter |
| **Vitaminer, mineraler, piller & væsker** | D, B12, omega-3, creatine, elektrolytter, “shot”-kultur — dosis, mangel, overskud |
| **Proteser, implantater, hardware** | Led, hjerte, sensorer, eksoskeletter, dental, “krop 2.0” |
| **Sikkerhed** | Interaktioner, forurening af tilskud, hvem der ikke skal tage hvad |

### Hvad vi *ikke* er

| Titel | De tager | Vi tager |
|-------|----------|----------|
| **[PULSEN](../pulsen/redaktionsnotesbog.md)** | Sundhedssektor, klinik, AI i journalen, ergoterapi, regioner | Individ/krop, forbrugerprodukter, ernæring, longevity-forskning |
| **SPÆNDING** | Elbiler | Evt. “motion som transport” kun hvis det er sundhedsvinkel |
| **KRAFTEN** | El-systemet | Evt. energiforbrug i kroppen metaforisk — undgå overlap |

Krydslink til PULSEN når emnet bliver **system/klinik/MDR**; bliv i DOSIS når det er **evidens, dosis, tallerken, hardware i kroppen**.

### Tone

- Sassy, klar, dansk — **ikke** wellness-influencer.  
- “Virker det?” før “det er trending.”  
- Skeln **mangel → tilskud** fra **rask → megadosis**.  
- Fact-check er hård her (claims, studier, interessekonflikter) — chefredaktør accepterer først efter tjek (se [redaktion/README](../README.md)).  
- Undgå diagnose- og behandlingsråd til den enkelte; vi er magasin, ikke læge.

## Nummerstruktur (ca. 10–16 artikler)

| # | Type |
|---|------|
| 1 | Leder |
| 2–3 | Gennembrud / research deep dive |
| 4–5 | Ernæring & kost (ét overblik + ét praksis- eller diæt-spor) |
| 6 | Protein / træning eller madkultur |
| 7–8 | Tilskud / vitaminer / en konkret “hot” pille eller væske |
| 9 | Proteser, implantater eller sensorer |
| 10 | Sikkerhed, bivirkninger, eller “hvad lab’et ikke viser” |
| 11 | Tallet / pejlemærker (DK vs. andre hvor relevant) |
| 12 | Ordbogen |
| 13 | Rygtebørsen (hype-stock) |
| + | Essay, case, “ugens paper” efter plads |

## Billeder

Imagine via `.env.local`. Editorial/lab/køkken/hardware — **ingen** lægemiddel-logoer, ingen læsbar emballage-tekst, ingen “før/efter”-kropsskam.  
Brand: dyb teal `#0A2E36`, mint-accent `#2BB5A0`, amber highlight `#F0B429`.  
Cover: `images/dosis_cover.png` pr. nummer fra `issueTheme`.

## Produktion

```bash
python3 production/load_env.py dosis
```

Output: `content/dosis/issues/<YYYY-MM-nrN>/`

## Nr. 1 — kandidat-temaer

1. **Protein-æraen** — hvad danskere faktisk har brug for, pulver vs. mad, ældre muskler.  
2. **D-vitamin & nordisk mørke** — mangel, megadoser, hvad evidensen siger.  
3. **GLP-1 og naboerne** — vægttabsmedicin, ernæring under behandling, hype vs. data (forsigtig, kilde-tung).  
4. **Implantater i hverdagen** — hofte, knæ, pacemaker, sensorer — livskvalitet ikke sci-fi.  
5. **Microbiom-hype** — tarm, kost, tilskud der lover for meget.

## Status

- [x] Magasin registreret (`magazine.json`, notesbog, `.env.dosis`)  
- [ ] Nr. 1 produceret  
- [ ] Cover + features  
- [ ] PDF  
