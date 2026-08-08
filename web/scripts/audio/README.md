# Lyd til artikler

Lyd genereres kun lokalt. Vercel og browseren får aldrig TTS- eller R2-nøgler.

## Første opsætning

`.env.local` skal indeholde `OPENAI_API_KEY`, `XAI_API_KEY`, R2 S3 Access Key ID,
R2 S3 Secret Access Key, `CLOUDFLARE_S3_API_ENDPOINT`, `CLOUDFLARE_R2_BUCKET` og
`CLOUDFLARE_R2_PUBLIC_URL`. Endpoint må gerne være kopieret med bucket-navnet til
sidst; værktøjet normaliserer det til R2's S3-endpoint.

`CLOUDFLARE_R2_PUBLIC_URL` skal være et Cloudflare custom domain, eksempelvis
`https://audio.nyesider.dk`. Den rate-limited `r2.dev`-adresse må kun bruges til
en eksplicit prøve med `--allow-dev-url`.

## Lydprøve

```sh
npm --prefix web run audio:samples
```

Det skaber blindmærkede `A.mp3` til `D.mp3` i `artifacts/audio-samples/`. De er
ikke uploadet eller publiceret.

## En artikel eller et helt nummer

```sh
# Kun lokal preview
npm --prefix web run audio:article -- indeni 2026-08-nr1 det-usynlige-lag

# Upload til R2 og skriv versionsmetadata til issue.json
npm --prefix web run audio:article -- indeni 2026-08-nr1 det-usynlige-lag --upload --write

# Samme operation for et helt nummer. Kommandoen kan trygt genoptages og
# springer allerede færdige artikler over (brug små batches i Codex-terminalen).
npm --prefix web run audio:issue -- indeni 2026-08-nr1 --upload --write --limit 2
```

`Leder`, `Ordbogen` og `Rygtebørsen` får aldrig AI-oplæsning. Brug nedenstående kommando, hvis ældre katalogmetadata skal ryddes; de versionsstyrede R2-filer slettes med vilje ikke automatisk.

```sh
npm --prefix web run audio:prune
```

For at afvikle hele lydkataloget — både publiceringsmetadata og alle `articles/`-objekter i den dedikerede R2-bucket — er der en bevidst bekræftet kommando:

```sh
npm --prefix web run audio:purge -- --confirm
```

Standard er OpenAI `gpt-4o-mini-tts` med stemmen `coral`. Vælg en anden testet
provider/stemme med `--provider xai --voice carina`. Hver lydfil navngives med
hashen af den præcise oplæsningstekst, så en artikelændring automatisk får en ny
R2-nøgle og aldrig spiller en gammel lydfil.
