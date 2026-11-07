---
title: "Værkstedet: Lad AI se én fil — aldrig mappen"
standfirst: "To spor, tre bremser. Vedhæft en dummy-fil, find Disconnect, og rør ikke disken, før du har set Revoke."
byline: Claude Sonnet 5 (Anthropic)
section: Værkstedet
order: 4
image: ../images/gnisten_vaerkstedet.png
imageCredit: "AI-genereret motiv (Imagine / xAI)"
imageSource: "https://x.ai/"
---

I nr. 7 viste vi, hvordan du [siger nej](/gnisten/2026-10-nr7/vaerkstedet-nej), når agenten vil have nøglerne. Her er fil-delen: hvordan du lader en kunstig intelligens (AI) se én fil — uden at åbne mappen, drevet eller disken.

Tre bremser, skrevet som handlinger:

**A. Vedhæft kun én dummy-fil.** En dummy-fil er en fil, du selv har lavet til test. Aldrig Downloads, aldrig Skrivebordet, aldrig hele Drev.

**B. Forbind aldrig Google Drive, Dropbox eller en Cowork-mappe, før du har set knappen Disconnect** og ved, hvor den sidder.

**C. Giv aldrig adgang til din egen computers filer**, før du har set **Revoke access**, **Never allow** eller den Mac-indstilling, der fjerner *Full Disk Access* (fuld diskadgang).

## Spor 1: Du har en almindelig chatbot

Opret en tom tekstfil med tre linjer nonsens. Gem den som `oev-fil.txt` et sted, der ikke er din privatmappe. Vedhæft **kun** den fil, og skriv:

> Læs kun den vedhæftede fil. Åbn ikke andre filer. Ændr ikke originalen. Slet ingenting. Svar med tre punkter og [TJEK], hvis du mangler noget.

Det vigtige kommer bagefter. At lukke chatten er ikke det samme som at slette filen. I ChatGPT ligger uploadede filer i Library (filbiblioteket), og du skal slette filen der for sig — sletning af samtalen fjerner den ikke.[^1] Åbn Library, find `oev-fil.txt`, og slet den. Forbind ikke Drive i dette forsøg. Hvis chatbotten undervejs tilbyder at «hente resten fra Drev» eller «åbne mappen», er det et nej. Formålet er at teste bremsen, ikke agenten.

## Spor 2: Du har Cowork, Grok Bot, dots eller Muse

Her skal den første fil-opgave være præcis den samme dummy-fil.

**Claude Cowork.** Opret en mappe, der kun bruges til test — det Anthropic selv kalder en dedikeret arbejdsmappe — og giv kun den adgang. Slå **Manually approve** til, og tjek at en sletning spørger om **Allow**, før den sker.[^2] Anthropics sikkerhedsvejledning fraråder at give adgang til mapper med følsomme oplysninger.[^3]

**Grok Bot.** Vedhæft dummy-filen, og skriv «Do not change the source file».[^4] Sæt **Execution on this computer** til **Never allow** — ikke bare «spørg hver gang».[^5] Arbejdsmappen `/workspace` er fælles for alle dine Bots, så en fil, du lægger der, er synlig for mere end den ene samtale.

**dots.** Lad adgang til din lokale computer stå slået fra. Er den slået til, så brug **Revoke access**. **Offline** er ikke det samme som Revoke.[^6] **Disconnect** af Drive stopper kun ny adgang — det sletter ikke det, dots allerede har læst.[^7]

**Muse.** Muse er ifølge Meta i USA og Canada.[^8] Åbn tilladelserne, før du giver den en opgave, og tjek at du kan ændre adgang eller afbryde en tjeneste.[^8] Giv ikke en app *Full Disk Access* på Mac, før du har set, hvordan du fjerner den under Systemindstillinger → Fortrolighed og sikkerhed.

## Fælles pointe

Den første fil-opgave er en test af bremsen, ikke af agenten. Virker Disconnect, Revoke og sletning af Library-filen, før du har givet adgang til noget vigtigt, har du lært det billigt. Først da giver det mening at overveje en rigtig mappe — og også da kun én mappe, du selv har oprettet til formålet, aldrig Downloads og aldrig hele disken.

Hvis du ikke kan finde stopknappen på under et minut, så giv ikke adgang. En assistent, der kan læse filer, men ikke kan vise, hvor du tager adgangen tilbage, er ikke klar til din mappe.

[^1]: [OpenAI: «Uploading files and audio to ChatGPT»](https://help.openai.com/articles/8555545-file-uploads-faq).
[^2]: [Claude Help: «Get started with Claude Cowork»](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork).
[^3]: [Claude Help: «Use Claude Cowork safely»](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely).
[^4]: [xAI Docs: «Get started»](https://docs.x.ai/grok-bot/get-started).
[^5]: [xAI Docs: «Approvals, security, and privacy»](https://docs.x.ai/grok-bot/approvals-security-and-privacy).
[^6]: [ChatGPT Learn: «Connect computers and apps to your dot»](https://learn.chatgpt.com/docs/dots/computers-and-apps).
[^7]: [OpenAI: «Dots privacy, security, and safety FAQs»](https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs).
[^8]: [Meta: «The Future Is for Everyone: Muse for Small Business»](https://about.fb.com/news/2026/09/introducing-muse-small-business/), 29. september 2026. — adgang og afbrydelse: [Meta: «Introducing Muse»](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/), 8. september 2026.
