#!/usr/bin/env python3
"""Editorial cleanup pass on assembled markdown articles."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Trailing next-section labels that leaked past article boundaries
TRAILING_LABELS = re.compile(
    r"\s*(?:"
    r"TEMA:\s*GENNEMBRUDDET|"
    r"KØRETEST|"
    r"ESSAY|"
    r"RYGTEBØRSEN|"
    r"A\s*N\s*A\s*L\s*Y\s*S\s*E\s*·.*|"
    r"B\s*R\s*A\s*N\s*C\s*H\s*E\s*N\s*Y\s*T\s*·.*|"
    r"F\s*E\s*A\s*T\s*U\s*R\s*E\s*·.*|"
    r"N\s*Y\s*T\s*F\s*R\s*A.*|"
    r"V\s*A\s*N\s*D\s*R\s*E.*"
    r")\s*$",
    re.I,
)

HYPHENS = [
    (r"\bDNAdrevet\b", "DNA-drevet"),
    (r"\bher-ognu\b", "her-og-nu"),
    (r"\bher-ognu-tilstande\b", "her-og-nu-tilstande"),
    (r"\bkr\./ md\.", "kr./md."),
    (r"til højre\.", "i kolofonen."),
]


def split_fm(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    end = text.find("\n---", 3)
    if end < 0:
        return "", text
    return text[: end + 4], text[end + 4 :].lstrip("\n")


def clean_body(body: str) -> str:
    body = body.rstrip() + "\n"
    # remove trailing leaked labels (may be mid-paragraph at end)
    body = TRAILING_LABELS.sub("", body)
    # also if label stuck to previous sentence without newline
    body = re.sub(
        r"([.!?»])\s+(TEMA: GENNEMBRUDDET|KØRETEST|ESSAY|RYGTEBØRSEN)\s*$",
        r"\1\n",
        body,
        flags=re.M,
    )
    body = re.sub(
        r"([.!?»])\s+([A-ZÆØÅ] ){3,}[A-ZÆØÅ].*$",
        r"\1\n",
        body,
        flags=re.M,
    )
    for pat, rep in HYPHENS:
        body = re.sub(pat, rep, body)
    # collapse 3+ newlines
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip() + "\n"


def fix_spaending_leader(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    fm, body = split_fm(text)
    fm = fm.replace("byline: chefredaktøren", "byline: Claude Fable 5")
    body = body.replace("i kolofonen til højre", "i kolofonen")
    path.write_text(fm + "\n\n" + clean_body(body), encoding="utf-8")


def fix_pulsen_leader(path: Path) -> None:
    content = """---
title: Lyt engang
byline: Claude Fable 5
section: Leder
order: 1
---

Der sker noget bemærkelsesværdigt i det danske sundhedsvæsen netop nu. Efter årtier, hvor hver ny teknologi føltes som endnu et skærmbillede mellem behandler og patient, er den nyeste generation af værktøjer bygget til det modsatte: at trække sig tilbage. Journalen, der skriver sig selv, mens lægen holder øjenkontakt. Røntgenalgoritmen, der sender folk hjem, før ventetiden æder aftenen. En dansk sprogmodel, der forstår, hvad en overlæge faktisk mumler ind i diktafonen.

Dette nummer af PULSEN handler om den bevægelse — fra København over Zürich til regionsgangene — og om de fag, der skal få teknologien til at lande hos rigtige mennesker. Ikke mindst ergoterapeuterne, der står foran noget nær et gyldent årti.

En bekendelse hører med: Dette magasin er selv skrevet af maskiner. Hver artikel er bestilt hos en navngiven AI-model og derefter redigeret af undertegnede — se kolofonen. Hvor indholdet er opdigtet, siger vi det højt og tydeligt. Resten står vi ved. God læselyst.

— Claude Fable 5, chefredaktør
"""
    path.write_text(content, encoding="utf-8")


def fix_pulsen_quiz(path: Path) -> None:
    content = """---
title: Skarpe hjerner, skarpere blyanter
byline: DeepSeek V3.2 (DeepSeek)
section: Sjov & Spil
order: 9
---

## Den store PULSEN-quiz

Test din viden fra dette nummer. Vælg a, b eller c.

1. Hvor stor en andel af danske sundhedsprofessionelle bruger ifølge en YouGov-undersøgelse AI-værktøjer regelmæssigt?
   - a) 15 %
   - b) 25 %
   - c) 35 %

2. Hvilket dansk AI-selskab slog OpenAI på et klinisk benchmark?
   - a) Corti
   - b) Bupa
   - c) Voicepoint

3. Hvor mange patienter betjener Cortis teknologi årligt?
   - a) Over 10 mio.
   - b) Over 50 mio.
   - c) Over 100 mio.

4. Hvad er den typiske startløn for en nyuddannet ergoterapeut?
   - a) Ca. 29.000 kr./md.
   - b) Ca. 33.000 kr./md.
   - c) Ca. 37.000 kr./md.

5. Hvilket selskab er først ude med DNA-drevet forebyggelse, før symptomer viser sig?
   - a) Dedalus
   - b) Bupa
   - c) Voicepoint

6. Hvad koster en EU MDR-certificering typisk?
   - a) 50–100.000 EUR
   - b) 200–600.000 EUR
   - c) 1–2 mio. EUR

<details>
<summary>Se facit til quizzen</summary>

1b · 2a · 3c · 4a · 5b · 6b

</details>

## Latinsk lynkursus

Match det medicinske udtryk med den mere jordnære betydning.

1. Gluteus maximus
2. Septum nasi deviatum
3. Oculus dexter
4. Tonsilla palatina

- a) Skæv næseskillevæg
- b) Den højre kikkert
- c) Ballen
- d) Halsmandlen

<details>
<summary>Se facit til latinsk lynkursus</summary>

1c · 2a · 3b · 4d

</details>

## Vagtplanens logikgåde

Sygeplejerskerne Anne, Bente og Cecilie skal dække vagterne Morgen, Dag og Aften. Hvem har hvilken vagt?

- Cecilie har ikke Dag-vagten.
- Anne har hverken Morgen- eller Aften-vagten.
- Bente har ikke Aften-vagten.

<details>
<summary>Se løsningen</summary>

Anne = Dag, Bente = Morgen, Cecilie = Aften

</details>
"""
    path.write_text(content, encoding="utf-8")


def fix_rygte_trovaerdighed(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    fm, body = split_fm(text)
    # demote "Troværdighed: x/5 ladestik" from h3 to italic line
    body = re.sub(
        r"### (Troværdighed: .+)",
        r"*\1*",
        body,
    )
    path.write_text(fm + "\n\n" + clean_body(body), encoding="utf-8")


def main() -> None:
    for issue in [
        ROOT / "content/spaending/issues/2026-07-nr1/articles",
        ROOT / "content/pulsen/issues/2026-07-nr1/articles",
    ]:
        for md in sorted(issue.glob("*.md")):
            if md.name.startswith("01-leder") and "spaending" in str(md):
                fix_spaending_leader(md)
                print("fixed", md.relative_to(ROOT))
                continue
            if md.name.startswith("01-leder") and "pulsen" in str(md):
                fix_pulsen_leader(md)
                print("fixed", md.relative_to(ROOT))
                continue
            if md.name.startswith("09-sjov"):
                fix_pulsen_quiz(md)
                print("fixed", md.relative_to(ROOT))
                continue
            if "rygteboersen" in md.name:
                fix_rygte_trovaerdighed(md)
                print("fixed", md.relative_to(ROOT))
                continue
            text = md.read_text(encoding="utf-8")
            fm, body = split_fm(text)
            cleaned = clean_body(body)
            if cleaned != body:
                md.write_text(fm + "\n\n" + cleaned, encoding="utf-8")
                print("cleaned", md.relative_to(ROOT))
            else:
                print("ok", md.relative_to(ROOT))

    # also strip trailing **KØRETEST** / ESSAY artifacts specifically
    folk = ROOT / "content/spaending/issues/2026-07-nr1/articles/02-folkebilen-er-tilbage.md"
    t = folk.read_text(encoding="utf-8")
    t = re.sub(r"\n\*\*KØRETEST\*\*\s*$", "\n", t)
    t = t.replace("kunne. TEMA: GENNEMBRUDDET Der", "kunne.\n\nDer")
    folk.write_text(t, encoding="utf-8")
    print("extra fix folkebilen")

    # corti trailing label
    corti = ROOT / "content/pulsen/issues/2026-07-nr1/articles/02-corti-maskinen-der-laerte-at-lytte.md"
    t = corti.read_text(encoding="utf-8")
    t = re.sub(r" taler\.\s+A N A L Y S E.*$", " taler.\n", t, flags=re.M)
    corti.write_text(t, encoding="utf-8")

    bupa = ROOT / "content/pulsen/issues/2026-07-nr1/articles/03-bupa-digitale-tvilling.md"
    t = bupa.read_text(encoding="utf-8")
    t = re.sub(r" gavner\.\s+B R A N C H E.*$", " gavner.\n", t, flags=re.M)
    t = t.replace("DNAdrevet", "DNA-drevet").replace("her-ognu", "her-og-nu")
    bupa.write_text(t, encoding="utf-8")

    # spaending rygte trailing ESSAY
    ryg = ROOT / "content/spaending/issues/2026-07-nr1/articles/07-rygteboersen.md"
    t = ryg.read_text(encoding="utf-8")
    t = re.sub(r"\nESSAY\s*$", "\n", t)
    ryg.write_text(t, encoding="utf-8")

    # sync issue.json bylines for leaders
    import json
    for issue_path, fixes in [
        (
            ROOT / "content/spaending/issues/2026-07-nr1/issue.json",
            {"leder-strom-til-folket": {"byline": "Claude Fable 5"}},
        ),
        (
            ROOT / "content/pulsen/issues/2026-07-nr1/issue.json",
            {
                "leder-lyt-engang": {
                    "byline": "Claude Fable 5",
                    "title": "Lyt engang",
                    "standfirst": None,
                }
            },
        ),
    ]:
        data = json.loads(issue_path.read_text(encoding="utf-8"))
        for art in data["articles"]:
            if art["slug"] in fixes:
                for k, v in fixes[art["slug"]].items():
                    if v is None:
                        art.pop(k, None)
                    else:
                        art[k] = v
        if "cover" not in data and "pulsen" in str(issue_path):
            data["cover"] = "images/pulsen_cover.png"
        issue_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print("synced", issue_path.relative_to(ROOT))


if __name__ == "__main__":
    main()
