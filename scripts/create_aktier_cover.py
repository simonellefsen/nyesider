#!/usr/bin/env python3
"""Create the Aktier med Grok nr. 1 cover programmatically."""

import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

# Magazine brand colors from magazine.json
NAVY = (13, 27, 42)        # #0D1B2A - primary ink
GOLD = (201, 162, 39)      # #C9A227 - accent
SAGE = (64, 130, 109)      # #40826D - highlight

# Cover dimensions (3:4 aspect ratio, high resolution)
WIDTH = 1200
HEIGHT = 1600

def create_price_line(width, height, start_y, end_y, num_points=200):
    """Create a descending jagged price line like a stock chart."""
    np.random.seed(42)  # For reproducibility
    
    x = np.linspace(0, width, num_points)
    
    # Start high, end low with realistic volatility
    base_trend = np.linspace(start_y, end_y, num_points)
    
    # Add volatility - larger swings at the start, stabilizing at end
    volatility = np.linspace(60, 15, num_points)
    noise = np.cumsum(np.random.randn(num_points) * 3)
    noise = noise / max(abs(noise.max()), abs(noise.min())) * volatility
    
    y = base_trend + noise
    
    # Ensure we don't go out of bounds
    y = np.clip(y, min(start_y, end_y) - 50, max(start_y, end_y) + 50)
    
    return list(zip(x.astype(int), y.astype(int)))

def draw_grid_lines(draw, width, height, top, bottom, color, alpha=30):
    """Draw subtle grid lines behind the chart."""
    grid_color = tuple(list(color) + [alpha]) if len(color) == 3 else color
    
    # Horizontal lines
    for y in np.linspace(top, bottom, 8):
        draw.line([(0, int(y)), (width, int(y))], fill=(*NAVY[:3], 60), width=1)
    
    # Vertical lines  
    for x in np.linspace(0, width, 12):
        draw.line([(int(x), top), (int(x), bottom)], fill=(*NAVY[:3], 60), width=1)

def main():
    # Create image with navy background
    img = Image.new('RGB', (WIDTH, HEIGHT), NAVY)
    draw = ImageDraw.Draw(img)
    
    # Add subtle texture/gradient effect
    for y in range(HEIGHT):
        alpha = int(255 * (1 - y / HEIGHT * 0.15))  # Slight gradient
        overlay_color = tuple([min(c + 8, 255) for c in NAVY])
        
    # Draw subtle grid in the chart area
    chart_top = 450
    chart_bottom = 1150
    
    # Grid lines (subtle navy variation)
    for y in np.linspace(chart_top, chart_bottom, 10):
        line_color = (20, 35, 55)
        draw.line([(80, int(y)), (WIDTH - 80, int(y))], fill=line_color, width=1)
    
    for x in np.linspace(80, WIDTH - 80, 15):
        line_color = (20, 35, 55)
        draw.line([(int(x), chart_top), (int(x), chart_bottom)], fill=line_color, width=1)
    
    # Create the price line
    points = create_price_line(WIDTH - 160, chart_bottom - chart_top - 100, 
                               50, chart_bottom - chart_top - 150, num_points=300)
    # Offset to chart area
    points = [(x + 80, y + chart_top + 50) for x, y in points]
    
    # Draw the price line (gold, thicker)
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill=GOLD, width=3)
    
    # Draw sage dot at the end
    last_point = points[-1]
    dot_radius = 12
    draw.ellipse([
        last_point[0] - dot_radius,
        last_point[1] - dot_radius,
        last_point[0] + dot_radius,
        last_point[1] + dot_radius
    ], fill=SAGE, outline=None)
    
    # Try to load a nice font, fall back to default
    try:
        # Try common system fonts
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 100)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
        tagline_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf", 36)
    except OSError:
        try:
            title_font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf", 100)
            subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 32)
            tagline_font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf", 36)
        except OSError:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            tagline_font = ImageFont.load_default()
    
    # Title: AKTIER MED GROK
    title_text = "AKTIER MED GROK"
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (WIDTH - title_width) // 2
    draw.text((title_x, 100), title_text, fill=GOLD, font=title_font)
    
    # Subtitle: NR. 1 · AUGUST 2026
    subtitle_text = "NR. 1 · AUGUST 2026"
    subtitle_bbox = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (WIDTH - subtitle_width) // 2
    draw.text((subtitle_x, 230), subtitle_text, fill=GOLD, font=subtitle_font)
    
    # Tagline at bottom
    tagline_text = "Fem kandidater i et marked uden bred nedtur."
    tagline_bbox = draw.textbbox((0, 0), tagline_text, font=tagline_font)
    tagline_width = tagline_bbox[2] - tagline_bbox[0]
    tagline_x = (WIDTH - tagline_width) // 2
    draw.text((tagline_x, 1350), tagline_text, fill=GOLD, font=tagline_font)
    
    # Add a subtle gold line under the tagline
    line_y = 1420
    draw.line([(200, line_y), (WIDTH - 200, line_y)], fill=(*GOLD, 128), width=2)
    
    # Save
    output_path = "content/aktier/issues/2026-08-nr1/images/aktier_cover.png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG", quality=95)
    print(f"Created {output_path} ({os.path.getsize(output_path) // 1024} KB)")
    return output_path

if __name__ == "__main__":
    main()
