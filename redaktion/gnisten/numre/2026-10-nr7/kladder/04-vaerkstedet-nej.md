**Værkstedet**

## Du behøver ikke stole på den – du skal bare vide, hvor den stopper

I nummer 6 lovede vi dig forsiden: «sådan siger du nej til din AI». Her er løftet indfriet – men kun det halve. Hvad der faktisk sker, når sådan en assistent kigger i dine filer, gemmer vi til nummer 8. I dag handler det om noget mere grundlæggende: en always-on-agent – en kunstig intelligens (AI), der kører i baggrunden og selv tager initiativer, i modsætning til en chatbot du selv skal spørge hver gang – og hvordan du giver den opgaver uden at give den nøglerne til din konto.

Tre bremser, skrevet som handlinger, ikke som løfter:

**A. Send aldrig automatisk.** Et udkast til en mail, en besked eller et opslag skal altid ligge og vente på dit tryk, før det forlader skærmen.

**B. Køb/betal aldrig automatisk.** Ingen agent skal have lov at gennemføre en betaling, bestille noget eller indtaste et betalingskort, uden at du selv trykker bekræft.

**C. Giv aldrig adgang til din egen computers filer, før du har set stop-knappen.** Find og afprøv stopfunktionen, mens opgaven er triviel – ikke første gang det haster.

## Spor 1: Du har endnu ikke adgang

De fleste danske privatbrugere har endnu ikke adgang til nogen af de tre produkter nedenfor. Metas Muse er – ifølge Metas egne sider – ikke udrullet i Det Europæiske Økonomiske Samarbejdsområde (EEA), og OpenAIs dots på Pro-abonnement er uden for EEA, Schweiz (CH) og Storbritannien (UK). Gør derfor det eneste fornuftige: kopiér aldrig adgangskoder eller nøgler ind i en chatboks, uanset hvor overbevisende den beder om det.

Til gengæld kan du øve selve nej-sætningen i en almindelig chatbot allerede i dag:

> «Foreslå aldrig at sende, købe eller slette. Skriv [TJEK] dér, hvor der ellers ville stå et løfte. Spørg, før du anbefaler at forbinde en app.»

Det koster intet, kræver ingen konto hos de tre nævnte produkter, og det er den sikre måde at opbygge vanen på, før du nogensinde giver en agent adgang til noget som helst.

## Spor 2: Du HAR adgang

Har du Grok Bot via X' Premium-abonnement, dots via OpenAIs Business Premium i en understøttet region, eller Muse i USA/Canada, gælder en anden regel: første opgave skal være en, der ikke kræver login til mail, betaling eller din lokale disk.

**Grok Bot.** xAI's eget første-eksempel er at vedhæfte et dokument og bede om fem punkter – med instruktionen «Do not change the source file»¹. Når den opgave er løst, sætter du bremserne, før du giver den mere: skriv «Stop now» for at standse det igangværende (det fortryder ikke det, der allerede er gjort), og slå «Auto Review» til, så den spørger først («Ask first»), før den sender ekstern mail². Husk: Grok Bots deler én computer indbyrdes – logins og filer på den maskine er tilgængelige for alle dine bots³.

**dots.** Sæt Pause i profilens •••-menu, før du går videre. Under Custom rules vælger du «Ask before taking action» og «Hand off to you», og tjek at adgang til din lokale computer står slået fra som standard. Vil du fortryde helt, bruger du Revoke access⁴. OpenAI beskriver dots' proaktive baggrunds-research som read-only – men det gælder kun den research, ikke de opgaver du selv beder om.

**Muse.** Gå i Settings → Permissions og slå «Always ask» til, så intet sker uden dit godkendende tryk. Du kan altid køre Disconnect Connectors for at fjerne adgang til eksterne tjenester. Vær opmærksom på, at Reset sletter alt og ikke kan fortrydes⁵.

Fælles for alle tre: den første opgave er en test af bremsen, ikke af agenten. Virker «stop», «pause» og «ask» ikke, før du har givet adgang til noget vigtigt, har du lært det billigt. Næste gang – i nummer 8 – ser vi på, hvad en agent faktisk kan se, når den først er inde i dine filer.

---

¹ xAI, *Grok Bot – Get started*: https://docs.x.ai/grok-bot/get-started
² xAI, *Grok Bot – Approvals, security and privacy*: https://docs.x.ai/grok-bot/approvals-security-and-privacy
³ xAI, *Grok Bot – Overview*: https://docs.x.ai/grok-bot/overview
⁴ OpenAI Help Center, *Getting started with your dot*: https://help.openai.com/en/articles/20001530-getting-started-with-your-dot
⁵ Meta, *Help – kunstig intelligens og tilladelser*: https://www.meta.com/help/artificial-intelligence/1385290430137537/