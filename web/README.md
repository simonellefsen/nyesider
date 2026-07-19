# Nye Sider — web

SvelteKit 2 + Svelte 5, TypeScript, `@sveltejs/adapter-vercel`, fuldt prerenderet.

## Routes

| Sti | Indhold |
|---|---|
| `/` | Kiosk — alle titler med seneste forside |
| `/[magazine]` | Magasinforside + arkiv |
| `/[magazine]/[issue]` | Indholdsfortegnelse + PDF-download |
| `/[magazine]/[issue]/[article]` | Læsevisning |

Indhold læses fra `../content` ved build. Billeder og PDF kopieres til `static/content/` via `npm run sync-assets`.

## Kilder & links (fodnoter)

Artikler kan bruge GFM-fodnoter i markdown — de vises som **Kilder & links** nederst i læsevisningen:

```md
Der blev indregistreret 80.704 nye elbiler …[^1]
Renault Twingo E-Tech er et af de tydeligste tegn.[^2]

[^1]: Mobility Denmark, [nyregistreringer](https://mobility.dk/nyregistreringer/).
[^2]: [Renault Twingo E-Tech](https://www.renault.dk/elbiler/twingo-e-tech-electric) — produktlink.
```

Ekstern links i artikler åbnes i nyt faneblad.

## Scripts

- `npm run dev` — sync assets + dev server
- `npm run build` — production build
- `npm run preview` — preview production build
- `npm run check` — svelte-check
