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

## Nr. 1 — udgivet

**Tema:** Supra og tillid · **Kultur:** Georgien  
**15 artikler:** leder, fokus, supra, dagligdag, arbejde, familie, natteliv, ceremonier, penge, skat/stat, tøj, tallet, ordbog, myter, til HORISONTEN.  
Cover + 4 feature-billeder (Imagine). PDF mangler.  
**Søsterrejse:** [HORISONTEN nr. 2](../../content/horisonten/issues/2026-08-nr2/) (samme land — stier, by, praktisk).

## Nr. 2 — kandidater

- **Marokko** (by vs. land, Ramadan-rytme, handel, kønsrum)  
- **Japan uden kirsebærtræer** (arbejde, service, bolig, dating)  
- **Filippinerne / OFW** (familieøkonomi, remitter, diaspora i DK)  
- **Et overset europæisk spor** (fx Sardinien, Sámi, Syditalien som *system*)

## Nummerstruktur (10–20)

Typisk **12–16**. Faste: Leder · Fokus · Mad · Dagligdag · Arbejde · Familie · Socialt · Penge · Stat · Tallet · Ordbog · Myter · Til HORISONTEN.

## Produktion

```bash
python3 production/load_env.py kulturboxen
```

Output: `content/kulturboxen/issues/<YYYY-MM-nrN>/`  
Brand: `#2C1830` / `#C45C26` / `#D4A574`.
