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

## Scripts

- `npm run dev` — sync assets + dev server
- `npm run build` — production build
- `npm run preview` — preview production build
- `npm run check` — svelte-check
