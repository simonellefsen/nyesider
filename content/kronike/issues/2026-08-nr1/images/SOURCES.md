# KRØNIKE nr. 1 · billedkilder

## AI-genereret (Imagine / xAI)

| Fil | Stil | Emne |
|---|---|---|
| `kronike_cover.png` | retro | forside |
| `kronike_leder.png` | retro | leder |
| `kronike_tallet.png` | geometric | tallet |
| `kronike_hedeby.png` | illustrated | Hedeby header |
| `kronike_kristning.png` | retro | kristning header |
| `kronike_margrete.png` | masculine | stiliseret (ikke portrætlighed) |
| `kronike_reformation.png` | grunge | reformation |
| `kronike_oresund.png` | flat | Øresund |
| `kronike_landbo.png` | organic | landboreformer header |
| `kronike_1864.png` | illustrated | 1864 header |
| `kronike_udvandring.png` | retro | udvandring |
| `kronike_oersted.png` | geometric | lab-motiv (header) |
| `kronike_myter.png` | playful | myter |
| `dannevirke-rekonstruktion.png` | illustrated | kunstnerisk rekonstruktion m. skala |
| `hedeby-bykort.png` | geometric | abstrakt byplan-idé |

Ingen logoer, ingen læsbar skiltetekst i Imagine-billeder.

## Atlaskort (AI-genereret kartografi via OpenRouter)

Erstattede de oprindelige håndlavede SVG-skitser 2026-08-08 efter en modelafprøvning
(se `map-trial/README.md`): `google/gemini-3-pro-image` gav markant mere læsbare
kortplader end skitse-SVG'erne. Kørt på **`.env.kronike`**, så billedforbruget spores
på titlens egen nøgle.

Alle tre plader er genereret med **`google/gemini-3-pro-image`** (ikke preview-varianten).

| Fil | Indhold |
|---|---|
| `kort-sydjylland-hedeby.jpg` | Slien, Hedeby, Dannevirke, Flensborg Fjord, Als, nutidens DK/DE-grænse |
| `kort-danmark-jelling-ribe.jpg` | Danmark med Ribe (rød) og Jelling, Jylland/Fyn/Sjælland |
| `kort-dybboel-1864.jpg` | Dannevirke → Dybbøl-skanserne, dansk tilbagetog feb. 1864, Als |

**Prompt-lære (til næste nummer):** modellen får geografien forkert, hvis den kun
får en liste af stednavne. Det, der virkede, var at skrive **rækkefølgen nord→syd**
eksplicit ud (Ribe → Aabenraa → Sønderborg → grænse → Flensborg → Slesvig → Hedeby
→ Dannevirke) og at angive **retning** på lineære træk (»Dannevirke løber *vest*
ind i halvøen«, »Slien åbner *øst* mod Østersøen«). Uden det bytter den rundt på
byerne og lader volden løbe den forkerte vej.

**Skematiske atlasplader — ikke geodætisk opmålte kort.** Stednavne og indbyrdes
placeringer er redaktionelt kontrolleret; kystlinjer er stiliserede.
De oprindelige SVG-skitser er bevaret i git-historikken.

## Eksterne licenser (public domain / CC)

| Fil | Kilde | Licens | Kredit |
|---|---|---|---|
| `pd_frihedsstoetten.jpg` | [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Frihedsst%C3%B8tten_-_Liberty_Column_(37179754433).jpg) (Flickr) | **CC BY 2.0** | Foto: [Jorge Láscar](https://www.flickr.com/people/8721758@N06) |
| `pd_oersted_daguerreotype.jpg` | [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Hans_Christian_%C3%98rsted_daguerreotype.jpg) | Public domain (forfatter død 1851; værk før 1851) | H.C. Ørsted daguerreotypi |
| `pd_margrete_gravmaele.jpg` | [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Margaret_of_Denmark,_Norway_%26_Sweden_(1389)_effigy_2010_(2).jpg) | Public domain (fotograf har frigivet værket) | Foto: Jacob Truedson Demitz / Ristesson — gravmæle ca. 1423 af Johannes Junge, Roskilde Domkirke |
| `cc_moent_erik_af_pommern.jpg` | [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Dansk_gros-m%C3%B8nt_af_s%C3%B8lv,_sl%C3%A5et_p%C3%A5_Gurre_Slot_under_Erik_af_Pommern.jpg) | **CC BY-SA 4.0** | Foto: Nationalmuseet — dansk sølvgros, Gurre Slot, Erik af Pommern |

## Bevidst fravalgt

| Motiv | Hvorfor ikke |
|---|---|
| 100-kronesedlen med H.C. Ørsted | Danmarks Nationalbank har **ophavsret** til seddelmotiverne, og Wikimedia Commons klassificerer danske sedler som *«Not OK»* ([Commons:Currency](https://commons.wikimedia.org/wiki/Commons:Currency)). Dertil kommer straffelovens regler om eftergørelse af penge. Sedlen omtales derfor i teksten i `11-oersted.md` med kilde til Nationalbanken, men gengives ikke. |
