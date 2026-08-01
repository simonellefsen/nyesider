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

## When to use

| Magasin | Typiske serier |
|---|---|
| **KRAFTEN** | Elmix, sol TWh, vind/gas-andele, landeandele |
| **ORBIT** | Opsendelser/år, aktive satellitter |
| **SPÆNDING** | Elbilandel af nyregistreringer, BEV-salg |
| Andre | Kun hvis det styrker artiklen — ikke diagram for diagrammets skyld |
