# KULTURBOXEN – Redaktionsnotesbog

Opdateret efter nr. 1 (august 2026, *"Supra og tillid"* — Georgien).  
OpenRouter: **kun** `.env.kulturboxen`. Imagine: `.env.local` / `XAI_API_KEY`.

## Identitet

**KULTURBOXEN** er magasinet om **hvordan mennesker lever** i andre kulturer — med dansk/europæisk læser som udgangspunkt for *sammenligning*, ikke som facit.

### vs HORISONTEN

| | HORISONTEN | KULTURBOXEN |
|---|---|---|
| Fokus | Rejse, ruter, sæson, praktisk | Hverdag, normer, systemer |
| Spørgsmål | Hvordan kommer jeg derhen? | Hvordan lever folk dér? |

Krydslink når destination og kultur overlapper.

### Synk-regel (planlægning)

**Prøv at synke numre med HORISONTEN**, når det giver mening: vælg kultur *og* foreslå en matchende rejseudgave (eller omvendt).  
- Eksempel: Georgien (KULTURBOXEN nr. 1 + HORISONTEN nr. 2).  
- **Ikke obligatorisk hver gang** — nogle kulturer egner sig dårligt til “vandring/cykling/praktisk” i samme kvartal. Notér asynk bevidst.  
- Ved synk: fælles timing hvis muligt, gensidige links, “Søster: …” i begge notesbøger.  
- Se husregel i [redaktion/README](../README.md).

## Nr. 1 — udgivet

**Tema:** Supra og tillid · **Kultur:** Georgien  
**15 artikler:** leder, fokus, supra, dagligdag, arbejde, familie, natteliv, ceremonier, penge, skat/stat, tøj, tallet, ordbog, myter, til HORISONTEN.  
Cover + 4 feature-billeder (Imagine). PDF mangler.  
**Søsterrejse:** [HORISONTEN nr. 2](../../content/horisonten/issues/2026-08-nr2/) (samme land — stier, by, praktisk).

## Nr. 2 — kandidater

- **(2026-08) Marokko** (by vs. land, Ramadan-rytme, handel, kønsrum)  
- **(2026-08) Japan uden kirsebærtræer** (arbejde, service, bolig, dating)  
- **(2026-08) Filippinerne / OFW** (familieøkonomi, remitter, diaspora i DK)  
- **(2026-08) Et overset europæisk spor** (fx Sardinien, Sámi, Syditalien som *system*)

## Format

- **Artikeltal:** typisk **12–16** (10–20 rummeligt). Faste: Leder · Fokus · Mad · Dagligdag · Arbejde · Familie · Socialt · Penge · Stat · Tallet · Ordbog · Myter · Til HORISONTEN.
- **Standard `mustCite`:** 3+ for Tallet (skal være en kildetabel, ikke en "ballpark"-liste — nr. 1's `12-tallet.md` er et negativt eksempel: 38 tal, 0 kilder, se Workstream C); 1–2 for Fokus/Arbejde/Penge/Stat med konkrete satser eller andele; 0 for Dagligdag/Familie/Myter medmindre en påstand kræver det.

## Produktion

```bash
python3 production/load_env.py kulturboxen
```

Output: `content/kulturboxen/issues/<YYYY-MM-nrN>/`  
Brand: `#2C1830` / `#C45C26` / `#D4A574`.

## Log

- **2026-08-01:** Notesbog udvidet med `## Format`; leads datostemplet (se [redaktion/README](../README.md)).
