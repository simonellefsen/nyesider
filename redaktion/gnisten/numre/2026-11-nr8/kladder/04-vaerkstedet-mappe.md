# Værkstedet: Lad AI se én fil — aldrig din mappe, dit drev eller din disk

Du har hørt, at du kan lade kunstig intelligens (AI) kigge i dine filer og hjælpe dig med at rydde op, skrive et resumé eller finde en gammel kvittering. Det lyder praktisk — og det er det, hvis du starter rigtigt. Problemet opstår, når den første fil-opgave bliver "se i hele min Downloads-mappe" i stedet for "se i denne ene fil, jeg selv har lavet til formålet."

Der findes tre bremser, du skal kende, før du rører ved noget. De er ikke tekniske finurligheder — de er knapper, du skal have set, inden du klikker "ja" til noget som helst.

**Bremse A:** Vedhæft kun én dummy-fil (en fil du selv har lavet til test), aldrig hele din Downloads-mappe, aldrig Skrivebordet, aldrig et helt drev.

**Bremse B:** Forbind aldrig Google Drive, Dropbox eller en delt arbejdsmappe, før du har set knappen Disconnect og ved, hvor den sidder.

**Bremse C:** Giv aldrig adgang til din egen computers filer — Allow access, Full Disk Access, Execution on this computer — før du har set Revoke eller Never allow og ved, hvordan du fjerner tilladelsen igen.

## Spor 1: Du har en almindelig chatbot

Opret en tom tekstfil med tre linjer nonsens. Gem den som "oev-fil.txt" et sted, der ikke er din privatmappe. Vedhæft **kun** den fil og skriv: "Læs kun den vedhæftede fil. Åbn ikke andre filer. Ændr ikke originalen. Slet ingenting. Svar med tre punkter og [TJEK] hvis du mangler noget."

Det vigtige kommer bagefter: at lukke chatten er ikke det samme som at slette filen. I ChatGPT ligger uploadede filer i et separat bibliotek (Library), og du skal ind og slette filen der for sig — sletning af selve samtalen fjerner den ikke[^1]. Forbind ikke Drive i dette forsøg. Formålet er at teste bremsen, ikke agenten.

## Spor 2: Du har Cowork, Grok Bot, dots eller Muse

Her skal den første fil-opgave være præcis den samme dummy-fil — uanset hvor fristende det er at springe testen over.

**Claude Cowork:** Opret en mappe, der kun bruges til test — det Anthropic selv kalder en dedikeret arbejdsmappe — og giv kun den adgang. Slå "manually approve" til, og tjek, at en sletning rent faktisk spørger dig om lov (Allow), før den sker[^2]. Anthropics egen sikkerhedsvejledning fraråder udtrykkeligt at give adgang til mapper med følsomme oplysninger[^3].

**Grok Bot:** Vedhæft dummy-filen og skriv "Do not change the source file"[^4]. Sæt "Execution on this computer" til **Never allow** — ikke bare "spørg hver gang"[^5]. Husk desuden, at arbejdsmappen /workspace er fælles for alle dine Bots, så en fil, du lægger der, er synlig for mere end den ene samtale.

**dots:** Lad lokal computer-adgang stå slået fra, medmindre du aktivt har brug for den — og hvis den er slået til, så brug Revoke access. Vær opmærksom på, at "Offline" ikke er det samme som Revoke[^6]. Og vigtigt: Disconnect af Drive stopper kun ny adgang fremover — det stopper ikke det, dots allerede har læst, før du trykkede Disconnect[^7].

**Muse:** Giv ikke Full Disk Access til at starte med. Er den allerede givet, fjerner du den under System Settings → Privacy & Security[^8].

## Fælles pointe

Den første fil-opgave, du giver en AI-agent, er ikke en test af, hvor god den er til at læse din fil. Den er en test af, om bremsen virker — om du kan se Disconnect, finde Revoke, og slette en vedhæftet fil uden at røre originalen. Først når den test er bestået, giver det mening at overveje en rigtig mappe.

Ingen kode, ingen installation i en terminal, ingen protokoller at sætte op — kun en tom tekstfil og et par klik, du selv har set virke.

*Fortsættes i nr.\u00a07's Værkstedet: /gnisten/2026-10-nr7/vaerkstedet-nej — om de situationer, hvor svaret rettelig er "nej, ikke den mappe."*

---

[^1]: OpenAI, "File uploads FAQ": https://help.openai.com/articles/8555545-file-uploads-faq
[^2]: Anthropic, "Get started with Claude Cowork": https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
[^3]: Anthropic, "Use Claude Cowork safely": https://support.claude.com/en/articles/13364135-use-claude-cowork-safely
[^4]: xAI, "Grok Bot — Get started": https://docs.x.ai/grok-bot/get-started
[^5]: xAI, "Grok Bot — Approvals, security and privacy": https://docs.x.ai/grok-bot/approvals-security-and-privacy
[^6]: OpenAI Learn, "dots — Computers and apps": https://learn.chatgpt.com/docs/dots/computers-and-apps
[^7]: OpenAI, "dots — Privacy, security and safety FAQs": https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs
[^8]: Meta, hjælpeartikel om kunstig intelligens og Full Disk Access: https://www.meta.com/help/artificial-intelligence/1126304576638594/