# Multi-year charts (online)

Interactive trend charts for the web edition. PDF/print stays text-only for these blocks.

## Long-term layout (preferred)

```
content/<magazine>/issues/<issue>/charts/
  <chart-id>.json
```

Article body:

```markdown
[CHART chart-id]
```

The loader reads **all** `charts/*.json` for the issue, then resolves markers.  
Optional: article frontmatter `charts: [...]` still works and **overrides** the same id from the library.

## Chart JSON shape

```json
{
  "id": "eu-elmix",
  "title": "EU: andel af elproduktion (ca.)",
  "unit": "%",
  "note": "Afrundede serier; se kilde for facit.",
  "source": "Ember",
  "sourceUrl": "https://ember-energy.org/",
  "years": [2015, 2016, 2025],
  "series": [
    { "name": "Vind + sol", "color": "#4EC9B0", "values": [8, 10, 30] }
  ]
}
```

Rules:

- `years.length` must match each `series[].values.length`
- Percentages in prose still use non-breaking space before `%` (`30\u00a0%`)
- Prefer rounded public series + honest `note` over false precision
- Web UI: `TrendChart.svelte` (hover tooltips)
- **Vis gap mellem verdensøkonomier:** Når et diagram handler om adoption, salg, produktion eller tempo, skal det som standard sammenligne store blokke (typisk **EU / USA / Kina**) og — hvor det er relevant — **top performers** (fx Norge for elbiler, eller andre forreste lande). En enkelt national kurve er sjældent nok; læseren skal se *forskellen* mellem markeder. Hold definitioner ærlige i `note` (BEV vs. plug-in, TWh vs. GW, osv.).

## When to use

| Magasin | Typiske serier |
|---|---|
| **KRAFTEN** | Elmix, sol TWh, vind/gas-andele, landeandele (EU/USA/Kina) |
| **ORBIT** | Opsendelser/år, aktive satellitter (lande/aktører side om side) |
| **SPÆNDING** | Elbilandel af nyregistreringer (DK + NO + EU + Kina + USA), volumen-gaps |
| **KULTURBOXEN** | Sammenlignende pejlemærker (DK/EU vs. den behandlede kultur: arbejdstid, skat, priser …) |
| **DOSIS** | Ernæring/tilskud/longevity-tal med gap (DK vs. andre, før/efter evidens — ærlig note) |
| Andre | Kun hvis det styrker artiklen — ikke diagram for diagrammets skyld |
