# Tre døre til dine filer — og fire spørgsmål før du åbner

Når en kunstig intelligens (AI) skal hjælpe med et dokument, kan du give adgang på tre grundlæggende måder: vedhæfte en fil, forbinde en mappe eller et drev eller åbne computerens filsystem. Forskellen handler ikke kun om bekvemmelighed. Den afgør, hvad AI’en kan se, ændre og beholde.

Der er ingen vinder. Men der er fire spørgsmål, du bør stille ved hver dør:

1. Hvad ser den?
2. Hvad må den ændre?
3. Hvor længe ligger det der?
4. Hvordan lukker jeg igen?

## Dør 1: Vedhæftningen

En vedhæftning er en fil, du aktivt føjer til en bestemt samtale. Det er den mest afgrænsede dør: Du vælger filen frem for en hel mappe.

I ChatGPT må et dokument eller en præsentation fylde op til 512 megabyte (MB). En tekstfil må rumme op til to millioner tekstdele, såkaldte tokens. Regneark ligger omkring 50 MB, mens billeder må fylde 20 MB. Grænsen er 80 filer på tre timer; på Free-planen er den tre filer om dagen.[^1]

Men spørgsmålet *hvor længe?* kræver ekstra opmærksomhed. En fil kan ligge i ChatGPTs Library, altså det gemte filbibliotek, selv om du sletter samtalen. OpenAI skriver, at sletning af en gemt fil og sletning af en samtale er to forskellige handlinger. Luk derfor døren begge steder: slet samtalen, hvis den ikke skal bevares, og slet Library-filen separat.

Grok Bot tillader op til 20 vedhæftninger, og dokumenter kan fylde 250 MB. I xAI’s eget eksempel står der: “Do not modify the originals.”[^2] Det er en nyttig formulering, når svaret på *hvad må den ændre?* skal være: ingenting.

## Dør 2: Mappen eller drevet

Her vælger du ikke nødvendigvis én fil. Du giver adgang til et område.

Claude Cowork arbejder i mapper, du vælger. Anthropic anbefaler en særskilt arbejdsmappe frem for bred adgang og fraråder adgang til lokale filer med følsomme oplysninger, eksempelvis finansielle dokumenter.[^3] Isolation beskytter resten af computeren, men ændrer ikke, hvad Claude må læse eller gøre gennem den adgang, du faktisk har givet. Sletning kræver, at du trykker **Allow**. Claude Cowork kræver en betalt plan; Pro står til 20 amerikanske dollar (USD) om måneden.[^4]

En connector — på dansk et forbindelsesstik — kobler en tjeneste som Google Drive til AI’en. Nye ChatGPT-brugere anvender Drive-connectoren frem for den gamle filvælger. Når forbindelsen er oprettet, kan ChatGPT spørges om alt, brugeren selv har adgang til i Drive eller SharePoint.[^5]

Det gør spørgsmål ét afgørende: *Er det denne fil eller hele mit tilgængelige drev?* Lukning sker via **Settings → Connected apps → Disconnect**. Men OpenAI understreger, at frakobling ikke ændrer tjenestens regler for opbevaring af filer.

Dots kan forbinde Google Drive for at læse og opdatere dokumenter.[^6] Her er forskellen mellem *læse* og *skrive* altså ikke akademisk: Det er to forskellige tilladelser.

## Dør 3: Computerens filsystem

Den bredeste dør er adgang til et filsystem — enten lokalt eller på en cloud-computer, altså en computer, der kører hos leverandøren.

Grok Bot har et delt område kaldet `/workspace`. Sletning af en Bot fjerner ikke nødvendigvis filerne på den delte computer eller dens browsersessioner.[^7] Ved lokal adgang er det forsigtige standardvalg **Never allow**, indtil du ved præcis, hvorfor adgang er nødvendig.

Dots har sin egen cloud-computer med egne filer. Lokal adgang kan gives med **Allow access** og fjernes med **Revoke**. At en forbindelse står som **Offline**, er ikke det samme som at tilbagekalde den. Desuden stopper en afbrudt pluginforbindelse ny adgang, men sletter ikke oplysninger, som allerede er bygget ind i dots’ kontekst.[^8]

Meta Muse på Mac kan få **Full Disk Access**, fuld diskadgang, som omfatter alle filer. Sletning sender filer til papirkurven, og adgangen slås fra i macOS’ systemindstillinger.[^9] Muse er ikke tilgængelig i Det Europæiske Økonomiske Samarbejdsområde (EØS); Meta har ikke oplyst en dansk lanceringsdato.

## Din firepunktskontrol

Før du åbner en dør, skriv svarene ned:

- **Ser den én fil, en mappe, et drev eller hele disken?**
- **Må den læse, skrive og slette?**
- **Overlever filer eller kontekst, at du sletter samtalen eller værktøjet?**
- **Skal du bruge Disconnect, Revoke, Never allow, fjerne Full Disk Access eller slette en Library-fil separat?**

Vil du øve selve stopknappen, så fortsæt i [Værkstedet: Nej](/gnisten/2026-10-nr7/vaerkstedet-nej). Se også [indbakkens tre bremser](/gnisten/2026-10-nr6).

[^1]: [OpenAI: File Uploads FAQ](https://help.openai.com/articles/8555545-file-uploads-faq)
[^2]: [xAI: Grok Bot — Files and results](https://docs.x.ai/grok-bot/files-and-results)
[^3]: [Anthropic: Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)
[^4]: [Anthropic: Claude Cowork](https://claude.com/product/cowork)
[^5]: [OpenAI: Add files from connected apps in ChatGPT](https://help.openai.com/en/articles/9309188-add-files-from-connected-apps-in-chatgpt)
[^6]: [OpenAI: Dots — Computers and apps](https://learn.chatgpt.com/docs/dots/computers-and-apps)
[^7]: [xAI: Grok Bot — Computer and apps](https://docs.x.ai/grok-bot/computer-and-apps)
[^8]: [OpenAI: Dots privacy, security and safety FAQ](https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs)
[^9]: [Meta: Muse on Mac](https://www.meta.com/help/artificial-intelligence/1126304576638594/)