---
title: "Første skridt ud af browseren"
standfirst: Du har bygget noget. Nu skal det have en adresse. Her er den korteste ærlige vej — og den ene fælde, der fanger flest.
byline: "Gemini 3.1 Pro Preview (Google)"
section: Værkstedet
order: 5
image: ../images/gn2_udgivelse.png
imageCredit: "AI-genereret motiv (Imagine / xAI) — illustreret"
imageSource: "https://x.ai/"
---

Du har gjort det. Gennem en stædig samtale med en assistent har du bygget en side. Knapperne virker, farverne sidder.

Men lige nu lever den kun i en mappe på din egen harddisk. Skal en ven, en kollega eller en kunde se den, mangler der ét skridt: den skal ud på internettet.

At få filer fra din maskine ud på en server kaldes **hosting**. Vi tager den korteste vej uden om fnidderet.

### Den forskel, der afgør alt

Først skal du forstå én skelnen, for den bestemmer, hvilke gratis muligheder der overhovedet gælder for dit projekt.

**En statisk side** består kun af færdige filer — tekst i HTML, design i CSS. Tænk på den som en stak trykte flyers. Når en gæst besøger adressen, skal computeren i den anden ende ikke tænke sig om. Den rækker bare en færdigtrykt flyer over disken.

**Noget, der kræver en server**, fungerer anderledes. Skal siden gemme data, lade brugere logge ind eller ændre sig efter, hvem der kigger, er det ikke en flyer længere. Det er en kok, der tilbereder retten fra bunden, hver gang nogen bestiller.

Kokken kræver strøm, regnekraft og vedligehold. Derfor er statiske sider ofte gratis at lægge ud, mens serverkode hurtigt koster penge.

### De tre almindelige veje

**GitHub Pages** er indbygget i kodeplatformen GitHub, driftssikker og skræddersyet til statiske sider.[^1]

**Cloudflare Pages** kører på et globalt netværk, hvor dine filer kopieres ud og kan hentes hurtigt fra hele verden.[^2]

**Vercel** er kendt for at gøre det nemt at få også lidt mere komplicerede projekter online med få klik.[^3]

### De fire spørgsmål

Mange guider kaster om sig med tal for båndbredde, byggeminutter og gigabytes. Ignorer dem. De ændrer sig, og dette blad har brændt sig på forældede tal før.

Stil i stedet fire spørgsmål til enhver udbyder:

1. **Kan den overhovedet køre det, jeg har bygget?**
2. **Hvad koster det i virkeligheden**, når fremmede begynder at besøge siden?
3. **Må jeg bruge tjenesten til lige præcis det, jeg har i sinde?**
4. **Hvordan får jeg mine filer væk igen?**

### Fælden, der fanger flest

Særligt det tredje spørgsmål. Her lurer en helt konkret fælde.

Vercel tilbyder en gratis **Hobby**-plan. Men i Vercels egen dokumentation står der, at Hobby-planen «restricts users to non-commercial, personal use only» — altså udelukkende personlige, ikke-kommercielle formål.[^4]

Hvad betyder det i praksis? Vil du sælge et produkt, tage imod betaling eller bruge siden som visitkort for en virksomhed, er gratisplanen ikke beregnet til det.

Det er ikke en kritik af Vercel. Det står i deres vilkår. Men det er præcis den slags, man opdager for sent — og Vercel beskriver selv, at konti og deployments kan sættes på pause ved brud på retningslinjerne.[^5]

### Køb et domænenavn

Afslut med at købe et domæne — for eksempel *mit-projekt.dk*.

Domænet er dit permanente skilt. Peger du det hen på udbyderen, har du altid en flugtvej: viser det sig, at du bryder en regel, eller bliver det for dyrt, kan du tage dine filer, finde en ny udbyder og pege domænet det nye sted hen.

Ingen besøgende opdager flytningen. Og du beholder kontrollen.

[^1]: [GitHub Pages](https://pages.github.com) — produktsiden. Dokumentationen findes under [About GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages).
[^2]: [Cloudflare Pages](https://pages.cloudflare.com) — produktsiden; den tekniske dokumentation ligger hos [Cloudflare Developers](https://developers.cloudflare.com/pages/).
[^3]: [Vercel](https://vercel.com) — produktsiden.
[^4]: [Vercel Hobby Plan](https://vercel.com/docs/plans/hobby), Vercel — «As stated in the fair use guidelines, the Hobby plan restricts users to non-commercial, personal use only.» De bagvedliggende retningslinjer: [Fair use guidelines](https://vercel.com/docs/limits/fair-use-guidelines).
[^5]: [Limits](https://vercel.com/docs/limits), Vercel — om kontogrænser og om, hvornår en konto eller et deployment kan sættes på pause.
