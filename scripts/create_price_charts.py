#!/usr/bin/env python3
"""Create SVG price charts for the five Aktier med Grok candidates."""

import json
import os
from datetime import datetime

# Magazine colors
NAVY = "#0D1B2A"
GOLD = "#C9A227"
SAGE = "#40826D"
GRAY = "#888888"
LIGHT_GRAY = "#444444"

# Chart dimensions
WIDTH = 800
HEIGHT = 400
MARGIN = {"top": 60, "right": 80, "bottom": 80, "left": 80}
PLOT_WIDTH = WIDTH - MARGIN["left"] - MARGIN["right"]
PLOT_HEIGHT = HEIGHT - MARGIN["top"] - MARGIN["bottom"]

def load_price_data():
    """Load the fetched Yahoo Finance data."""
    with open("content/aktier/issues/2026-08-nr1/data/yahoo_prices.json") as f:
        return json.load(f)

def create_svg_chart(ticker: str, data: dict, title_dk: str, currency: str) -> str:
    """Create an SVG price chart for a single ticker."""
    prices = data["prices"]
    
    # Get price range
    closes = [p["close"] for p in prices if p.get("close")]
    if not closes:
        return None
    
    min_price = min(closes) * 0.95
    max_price = max(closes) * 1.05
    price_range = max_price - min_price
    
    # Get date range
    dates = [datetime.strptime(p["date"], "%Y-%m-%d") for p in prices if p.get("close")]
    min_date = min(dates)
    max_date = max(dates)
    date_range = (max_date - min_date).days
    
    # Find 52-week high and low
    high52 = data.get("high52_calc") or max(closes)
    low52 = data.get("low52_calc") or min(closes)
    
    # Current price (last available)
    current_price = closes[-1]
    current_date = dates[-1]
    
    # Find the date of the 52-week high
    high52_idx = closes.index(max(closes))
    high52_date = dates[high52_idx]
    
    def x_scale(date):
        days_from_start = (date - min_date).days
        return MARGIN["left"] + (days_from_start / date_range) * PLOT_WIDTH
    
    def y_scale(price):
        return MARGIN["top"] + PLOT_HEIGHT - ((price - min_price) / price_range) * PLOT_HEIGHT
    
    # Build path for price line
    path_points = []
    for p in prices:
        if p.get("close"):
            dt = datetime.strptime(p["date"], "%Y-%m-%d")
            x = x_scale(dt)
            y = y_scale(p["close"])
            path_points.append(f"{x:.1f},{y:.1f}")
    
    path_d = "M " + " L ".join(path_points)
    
    # Generate x-axis labels (monthly)
    x_labels = []
    current_month = None
    month_names_dk = {
        1: "jan", 2: "feb", 3: "mar", 4: "apr", 5: "maj", 6: "jun",
        7: "jul", 8: "aug", 9: "sep", 10: "okt", 11: "nov", 12: "dec"
    }
    for p in prices:
        if p.get("close"):
            dt = datetime.strptime(p["date"], "%Y-%m-%d")
            month_key = (dt.year, dt.month)
            if month_key != current_month:
                current_month = month_key
                label = f"{month_names_dk[dt.month]} {dt.year % 100}"
                x_labels.append({"date": dt, "label": label})
    
    # Take every 2nd month for cleaner display
    x_labels = x_labels[::2]
    
    # Generate y-axis labels
    y_labels = []
    step = price_range / 5
    for i in range(6):
        price = min_price + i * step
        y_labels.append({"price": price, "y": y_scale(price)})
    
    # Currency symbol
    curr_symbol = {"DKK": "kr.", "USD": "$", "EUR": "€"}.get(currency, currency)
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" style="background:{NAVY}">
  <defs>
    <style>
      .title {{ font-family: Georgia, serif; font-size: 16px; fill: {GOLD}; }}
      .subtitle {{ font-family: Arial, sans-serif; font-size: 12px; fill: {GRAY}; }}
      .axis-label {{ font-family: Arial, sans-serif; font-size: 11px; fill: {GRAY}; }}
      .price-label {{ font-family: Arial, sans-serif; font-size: 10px; fill: {GRAY}; }}
      .annotation {{ font-family: Arial, sans-serif; font-size: 10px; }}
      .source {{ font-family: Arial, sans-serif; font-size: 9px; fill: {GRAY}; }}
    </style>
  </defs>
  
  <!-- Title -->
  <text x="{MARGIN['left']}" y="25" class="title">{title_dk}</text>
  <text x="{MARGIN['left']}" y="45" class="subtitle">{ticker}, daglig lukkekurs, {min_date.strftime('%d. %b %Y').lower().replace('.', '')} – {max_date.strftime('%d. %b %Y').lower().replace('.', '')}</text>
  
  <!-- Grid lines -->
  <g stroke="{LIGHT_GRAY}" stroke-width="0.5" stroke-dasharray="2,4">
'''
    
    # Horizontal grid lines
    for yl in y_labels:
        svg += f'    <line x1="{MARGIN["left"]}" y1="{yl["y"]:.1f}" x2="{MARGIN["left"] + PLOT_WIDTH}" y2="{yl["y"]:.1f}" />\n'
    
    svg += '  </g>\n'
    
    # 52-week high line (dashed, gold)
    high52_y = y_scale(high52)
    svg += f'''
  <!-- 52-ugers top -->
  <line x1="{MARGIN["left"]}" y1="{high52_y:.1f}" x2="{MARGIN["left"] + PLOT_WIDTH}" y2="{high52_y:.1f}" 
        stroke="{GOLD}" stroke-width="1" stroke-dasharray="6,4" opacity="0.6"/>
  <text x="{MARGIN["left"] + PLOT_WIDTH + 5}" y="{high52_y + 4:.1f}" class="annotation" fill="{GOLD}">52w top</text>
  <text x="{MARGIN["left"] + PLOT_WIDTH + 5}" y="{high52_y + 16:.1f}" class="price-label">{curr_symbol} {high52:.2f}</text>
'''
    
    # 52-week low line (dashed, sage)
    low52_y = y_scale(low52)
    svg += f'''
  <!-- 52-ugers bund -->
  <line x1="{MARGIN["left"]}" y1="{low52_y:.1f}" x2="{MARGIN["left"] + PLOT_WIDTH}" y2="{low52_y:.1f}" 
        stroke="{SAGE}" stroke-width="1" stroke-dasharray="6,4" opacity="0.6"/>
  <text x="{MARGIN["left"] + PLOT_WIDTH + 5}" y="{low52_y + 4:.1f}" class="annotation" fill="{SAGE}">52w bund</text>
  <text x="{MARGIN["left"] + PLOT_WIDTH + 5}" y="{low52_y + 16:.1f}" class="price-label">{curr_symbol} {low52:.2f}</text>
'''
    
    # Price line
    svg += f'''
  <!-- Price line -->
  <path d="{path_d}" fill="none" stroke="{GOLD}" stroke-width="2" stroke-linejoin="round"/>
'''
    
    # Current price dot
    current_x = x_scale(current_date)
    current_y = y_scale(current_price)
    svg += f'''
  <!-- Current price -->
  <circle cx="{current_x:.1f}" cy="{current_y:.1f}" r="6" fill="{SAGE}" />
  <text x="{current_x - 35:.1f}" y="{current_y - 12:.1f}" class="annotation" fill="{SAGE}">{curr_symbol} {current_price:.2f}</text>
'''
    
    # X-axis labels
    svg += '\n  <!-- X-axis -->\n'
    for xl in x_labels:
        x = x_scale(xl["date"])
        svg += f'  <text x="{x:.1f}" y="{HEIGHT - MARGIN["bottom"] + 20}" class="axis-label" text-anchor="middle">{xl["label"]}</text>\n'
    
    # Y-axis labels
    svg += '\n  <!-- Y-axis -->\n'
    for yl in y_labels[1:-1]:  # Skip first and last
        svg += f'  <text x="{MARGIN["left"] - 10}" y="{yl["y"] + 4:.1f}" class="price-label" text-anchor="end">{curr_symbol} {yl["price"]:.0f}</text>\n'
    
    # Calculate drawdown
    drawdown_pct = (high52 - current_price) / high52 * 100
    
    # Source line
    svg += f'''
  <!-- Source -->
  <text x="{MARGIN["left"]}" y="{HEIGHT - 15}" class="source">Kilde: Yahoo Finance. Stiplet linje: 52-ugers top ({curr_symbol} {high52:.2f}). Aktuel pris: {curr_symbol} {current_price:.2f} (−{drawdown_pct:.1f} % fra top).</text>
</svg>'''
    
    return svg

def create_comparison_chart(data: dict, title: str) -> str:
    """Create a comparison bar chart showing % from 52w high for all candidates."""
    # Calculate drawdowns for stocks
    stocks = [
        ("NOVO-B", "NOVO-B.CO", GOLD),
        ("LULU", "LULU", "#E8B4B8"),  # Light pink
        ("ZTS", "ZTS", "#A3C9A8"),     # Light green  
        ("RI.PA", "RI.PA", "#B8D4E3"), # Light blue
        ("BMW", "BMW.DE", "#D4B8E3"),  # Light purple
    ]
    
    drawdowns = []
    for label, ticker, color in stocks:
        if ticker in data:
            d = data[ticker]
            high52 = d.get("high52_calc") or d.get("expected", {}).get("high52", 100)
            current = d["prices"][-1]["close"] if d.get("prices") else d.get("expected", {}).get("close_28aug", 100)
            pct = (high52 - current) / high52 * 100
            drawdowns.append({"label": label, "pct": pct, "color": color})
    
    # Chart dimensions
    bar_height = 35
    bar_spacing = 15
    chart_height = len(drawdowns) * (bar_height + bar_spacing) + 120
    max_pct = 55  # Max percentage for scale
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {chart_height}" style="background:{NAVY}">
  <defs>
    <style>
      .title {{ font-family: Georgia, serif; font-size: 16px; fill: {GOLD}; }}
      .subtitle {{ font-family: Arial, sans-serif; font-size: 12px; fill: {GRAY}; }}
      .bar-label {{ font-family: Arial, sans-serif; font-size: 12px; fill: white; }}
      .pct-label {{ font-family: Arial, sans-serif; font-size: 11px; fill: {GOLD}; font-weight: bold; }}
      .source {{ font-family: Arial, sans-serif; font-size: 9px; fill: {GRAY}; }}
    </style>
  </defs>
  
  <text x="{MARGIN['left']}" y="25" class="title">{title}</text>
  <text x="{MARGIN['left']}" y="45" class="subtitle">Afstand fra 52-ugers top, pr. 28. aug 2026</text>
'''
    
    y_start = 70
    bar_width_max = PLOT_WIDTH - 80
    
    for i, d in enumerate(drawdowns):
        y = y_start + i * (bar_height + bar_spacing)
        bar_width = (d["pct"] / max_pct) * bar_width_max
        
        svg += f'''
  <rect x="{MARGIN['left']}" y="{y}" width="{bar_width:.1f}" height="{bar_height}" fill="{d['color']}" rx="4"/>
  <text x="{MARGIN['left'] + 10}" y="{y + bar_height/2 + 5}" class="bar-label">{d['label']}</text>
  <text x="{MARGIN['left'] + bar_width + 10:.1f}" y="{y + bar_height/2 + 5}" class="pct-label">−{d['pct']:.1f} %</text>
'''
    
    svg += f'''
  <text x="{MARGIN['left']}" y="{chart_height - 15}" class="source">Kilde: Yahoo Finance. Alle tal pr. 28. august 2026 lukke.</text>
</svg>'''
    
    return svg

def create_index_comparison_chart(data: dict) -> str:
    """Create chart comparing indices at highs vs stocks washed out."""
    # Indices
    indices = [
        ("S&P 500", "^GSPC"),
        ("DAX", "^GDAXI"),
        ("OMXC25", "^OMXC25"),
    ]
    
    # Stocks
    stocks = [
        ("NOVO-B", "NOVO-B.CO"),
        ("LULU", "LULU"),
        ("ZTS", "ZTS"),
        ("RI.PA", "RI.PA"),
        ("BMW", "BMW.DE"),
    ]
    
    items = []
    
    # Calculate index drawdowns
    for label, ticker in indices:
        if ticker in data:
            d = data[ticker]
            closes = [p["close"] for p in d.get("prices", []) if p.get("close")]
            if closes:
                high52 = max(closes)
                current = closes[-1]
                pct = (high52 - current) / high52 * 100
                items.append({"label": label, "pct": pct, "color": SAGE, "type": "index"})
    
    # Calculate stock drawdowns
    for label, ticker in stocks:
        if ticker in data:
            d = data[ticker]
            closes = [p["close"] for p in d.get("prices", []) if p.get("close")]
            if closes:
                high52 = max(closes)
                current = closes[-1]
                pct = (high52 - current) / high52 * 100
                items.append({"label": label, "pct": pct, "color": GOLD, "type": "stock"})
    
    # Sort by drawdown (smallest first)
    items.sort(key=lambda x: x["pct"])
    
    # Chart dimensions
    bar_height = 28
    bar_spacing = 10
    chart_height = len(items) * (bar_height + bar_spacing) + 130
    max_pct = 55
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {chart_height}" style="background:{NAVY}">
  <defs>
    <style>
      .title {{ font-family: Georgia, serif; font-size: 16px; fill: {GOLD}; }}
      .subtitle {{ font-family: Arial, sans-serif; font-size: 12px; fill: {GRAY}; }}
      .bar-label {{ font-family: Arial, sans-serif; font-size: 11px; fill: white; }}
      .pct-label {{ font-family: Arial, sans-serif; font-size: 10px; fill: {GOLD}; font-weight: bold; }}
      .legend {{ font-family: Arial, sans-serif; font-size: 10px; fill: {GRAY}; }}
      .source {{ font-family: Arial, sans-serif; font-size: 9px; fill: {GRAY}; }}
    </style>
  </defs>
  
  <text x="{MARGIN['left']}" y="25" class="title">Indeks ved toppen, kandidater solgt fra</text>
  <text x="{MARGIN['left']}" y="45" class="subtitle">Afstand fra 52-ugers top — indeks vs. nummerets fem kandidater</text>
  
  <!-- Legend -->
  <rect x="{WIDTH - 180}" y="15" width="12" height="12" fill="{SAGE}" rx="2"/>
  <text x="{WIDTH - 163}" y="25" class="legend">Indeks</text>
  <rect x="{WIDTH - 100}" y="15" width="12" height="12" fill="{GOLD}" rx="2"/>
  <text x="{WIDTH - 83}" y="25" class="legend">Kandidat</text>
'''
    
    y_start = 70
    bar_width_max = PLOT_WIDTH - 80
    
    for i, item in enumerate(items):
        y = y_start + i * (bar_height + bar_spacing)
        bar_width = (item["pct"] / max_pct) * bar_width_max
        
        svg += f'''
  <rect x="{MARGIN['left']}" y="{y}" width="{bar_width:.1f}" height="{bar_height}" fill="{item['color']}" rx="3" opacity="0.85"/>
  <text x="{MARGIN['left'] + 8}" y="{y + bar_height/2 + 4}" class="bar-label">{item['label']}</text>
  <text x="{MARGIN['left'] + bar_width + 8:.1f}" y="{y + bar_height/2 + 4}" class="pct-label">−{item['pct']:.1f} %</text>
'''
    
    svg += f'''
  <text x="{MARGIN['left']}" y="{chart_height - 15}" class="source">Kilde: Yahoo Finance, 28. august 2026. Grøn = indeks (S&P, DAX, OMXC25). Guld = nummerets kandidater.</text>
</svg>'''
    
    return svg


def main():
    data = load_price_data()
    output_dir = "content/aktier/issues/2026-08-nr1/images"
    
    # Create individual stock charts
    charts = [
        ("NOVO-B.CO", "Novo Nordisk (NOVO-B.CO) — 1 år", "DKK", "figur-novo-pris.svg"),
        ("LULU", "Lululemon (LULU) — 1 år", "USD", "figur-lulu-pris.svg"),
        ("ZTS", "Zoetis (ZTS) — 1 år", "USD", "figur-zts-pris.svg"),
        ("RI.PA", "Pernod Ricard (RI.PA) — 1 år", "EUR", "figur-ripa-pris.svg"),
        ("BMW.DE", "BMW (BMW.DE) — 1 år", "EUR", "figur-bmw-pris.svg"),
    ]
    
    for ticker, title, currency, filename in charts:
        if ticker in data:
            svg = create_svg_chart(ticker, data[ticker], title, currency)
            if svg:
                path = os.path.join(output_dir, filename)
                with open(path, "w") as f:
                    f.write(svg)
                print(f"Created {path}")
    
    # Create comparison chart for Tallet
    svg = create_comparison_chart(data, "Fem kandidater: afstand fra 52-ugers top")
    path = os.path.join(output_dir, "figur-tallet-sammenligning.svg")
    with open(path, "w") as f:
        f.write(svg)
    print(f"Created {path}")
    
    # Create index comparison chart for Markedet
    svg = create_index_comparison_chart(data)
    path = os.path.join(output_dir, "figur-markedet-sammenligning.svg")
    with open(path, "w") as f:
        f.write(svg)
    print(f"Created {path}")
    
    print("\nAll charts created!")

if __name__ == "__main__":
    main()
