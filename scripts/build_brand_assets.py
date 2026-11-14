#!/usr/bin/env python3
"""
NovaArc Official Brand Assets Generator
Generates SVG, PNG, and Favicon assets from the official NovaArc logo specification.
"""
import math
import os
import subprocess
from PIL import Image

REPO_ROOT = "/Users/bhargav/Nova-Arc"
IMAGES_DIR = os.path.join(REPO_ROOT, "images")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Brand Colors
CREAM = "#F4EEDD"       # Off-white / cream for outer arc, center dot, wordmark
EMERALD = "#2DD782"     # Vibrant emerald green for inner arc & brand accent
MINT = "#A5DABE"        # Soft mint / sage green for middle arc & tagline
DARK_NAVY = "#0B2545"   # Deep navy for dark text on white backgrounds
PINE_GREEN = "#043329"  # Deep pine/emerald for dark arc variants on white

def polar_to_cartesian(cx, cy, r, angle_deg):
    angle_rad = math.radians(angle_deg)
    return cx + r * math.cos(angle_rad), cy + r * math.sin(angle_rad)

def describe_arc(cx, cy, r, start_angle, end_angle):
    diff = (end_angle - start_angle) % 360
    if diff == 0:
        diff = 360
    start_x, start_y = polar_to_cartesian(cx, cy, r, start_angle)
    end_x, end_y = polar_to_cartesian(cx, cy, r, start_angle + diff)
    large_arc_flag = "1" if diff > 180 else "0"
    return f"M {start_x:.3f} {start_y:.3f} A {r:.3f} {r:.3f} 0 {large_arc_flag} 1 {end_x:.3f} {end_y:.3f}"

def generate_icon_svg(cream_color=CREAM, mint_color=MINT, emerald_color=EMERALD):
    cx, cy = 250, 250
    sw = 38
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <!-- Center Dot -->
  <circle cx="{cx}" cy="{cy}" r="22" fill="{cream_color}" />
  
  <!-- Inner Arc (Emerald Green) -->
  <path d="{describe_arc(cx, cy, 80, -165, 110)}" fill="none" stroke="{emerald_color}" stroke-width="{sw}" stroke-linecap="round" />
  
  <!-- Middle Arc (Mint Green) -->
  <path d="{describe_arc(cx, cy, 152, 95, -10)}" fill="none" stroke="{mint_color}" stroke-width="{sw}" stroke-linecap="round" />
  
  <!-- Outer Arc (Cream) -->
  <path d="{describe_arc(cx, cy, 224, -34, -135)}" fill="none" stroke="{cream_color}" stroke-width="{sw}" stroke-linecap="round" />
</svg>'''

def generate_horizontal_logo_svg(is_dark=False):
    scale = 26.0 / 224.0
    cx, cy = 34, 30
    sw = 38 * scale
    
    cream_col = PINE_GREEN if is_dark else CREAM
    mint_col = "#0D9488" if is_dark else MINT
    emerald_col = "#059669" if is_dark else EMERALD
    text_color = DARK_NAVY if is_dark else "#FFFFFF"
    accent_color = "#059669" if is_dark else EMERALD
    
    icon_markup = f'''
  <circle cx="{cx}" cy="{cy}" r="{22*scale:.2f}" fill="{cream_col}" />
  <path d="{describe_arc(cx, cy, 80*scale, -165, 110)}" fill="none" stroke="{emerald_col}" stroke-width="{sw:.2f}" stroke-linecap="round" />
  <path d="{describe_arc(cx, cy, 152*scale, 95, -10)}" fill="none" stroke="{mint_col}" stroke-width="{sw:.2f}" stroke-linecap="round" />
  <path d="{describe_arc(cx, cy, 224*scale, -34, -135)}" fill="none" stroke="{cream_col}" stroke-width="{sw:.2f}" stroke-linecap="round" />
'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 60" width="100%" height="100%">
  <defs>
    <style>
      .brand-title {{
        font-family: 'Outfit', 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-weight: 800;
        font-size: 26px;
        fill: {text_color};
        letter-spacing: 0.08em;
      }}
      .brand-accent {{
        fill: {accent_color};
      }}
    </style>
  </defs>
  {icon_markup}
  <text x="74" y="39" class="brand-title">NOVA<tspan class="brand-accent">ARC</tspan></text>
</svg>'''

def generate_stacked_logo_svg(is_dark=False):
    scale = 0.52
    cx, cy = 300, 155
    sw = 38 * scale
    
    cream_col = PINE_GREEN if is_dark else CREAM
    mint_col = "#0D9488" if is_dark else MINT
    emerald_col = "#059669" if is_dark else EMERALD
    text_color = DARK_NAVY if is_dark else CREAM
    tagline_color = "#059669" if is_dark else MINT
    
    icon_markup = f'''
  <circle cx="{cx}" cy="{cy}" r="{22*scale:.2f}" fill="{cream_col}" />
  <path d="{describe_arc(cx, cy, 80*scale, -165, 110)}" fill="none" stroke="{emerald_col}" stroke-width="{sw:.2f}" stroke-linecap="round" />
  <path d="{describe_arc(cx, cy, 152*scale, 95, -10)}" fill="none" stroke="{mint_col}" stroke-width="{sw:.2f}" stroke-linecap="round" />
  <path d="{describe_arc(cx, cy, 224*scale, -34, -135)}" fill="none" stroke="{cream_col}" stroke-width="{sw:.2f}" stroke-linecap="round" />
'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 500" width="100%" height="100%">
  <defs>
    <style>
      .wordmark {{
        font-family: 'Outfit', 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-weight: 700;
        font-size: 52px;
        fill: {text_color};
        letter-spacing: 0.28em;
      }}
      .tagline {{
        font-family: 'Outfit', 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-weight: 600;
        font-size: 20px;
        fill: {tagline_color};
        letter-spacing: 0.32em;
      }}
    </style>
  </defs>
  {icon_markup}
  <text x="300" y="360" class="wordmark" text-anchor="middle">NOVAARC</text>
  <text x="300" y="420" class="tagline" text-anchor="middle">TECHNOLOGIES SERVICES PVT LTD</text>
</svg>'''

def render_svg_to_png(svg_path, png_path, width, height, transparent=True):
    temp_html = svg_path + ".render.html"
    bg = "transparent" if transparent else "#0B2545"
    html = f'''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  html, body {{
    margin: 0;
    padding: 0;
    width: {width}px;
    height: {height}px;
    background: {bg};
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  img {{
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: block;
  }}
</style>
</head>
<body>
  <img src="{os.path.basename(svg_path)}">
</body>
</html>'''
    with open(temp_html, "w") as f:
        f.write(html)
        
    subprocess.run([
        CHROME,
        "--headless",
        "--disable-gpu",
        "--default-background-color=00000000",
        f"--window-size={width},{height}",
        f"--screenshot={png_path}",
        f"file://{temp_html}"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if os.path.exists(temp_html):
        os.remove(temp_html)
    print(f"Rendered: {png_path} ({width}x{height})")

def main():
    os.makedirs(IMAGES_DIR, exist_ok=True)
    
    # 1. Standalone circular icon SVG (Light/Standard)
    icon_svg_path = os.path.join(IMAGES_DIR, "novaarc-icon.svg")
    with open(icon_svg_path, "w") as f:
        f.write(generate_icon_svg())
    print("Wrote:", icon_svg_path)
    
    # Standalone circular icon SVG (Dark for white background)
    icon_dark_svg_path = os.path.join(IMAGES_DIR, "novaarc-icon-dark.svg")
    with open(icon_dark_svg_path, "w") as f:
        f.write(generate_icon_svg(cream_color=PINE_GREEN, mint_color="#0D9488", emerald_color="#059669"))
    print("Wrote:", icon_dark_svg_path)
    
    # 2. Horizontal logo SVG (Light text for dark navbar)
    horiz_svg_path = os.path.join(IMAGES_DIR, "novaarc-logo-horizontal.svg")
    with open(horiz_svg_path, "w") as f:
        f.write(generate_horizontal_logo_svg(is_dark=False))
    print("Wrote:", horiz_svg_path)
    
    # Horizontal logo SVG (Dark text for white mobile drawer)
    horiz_dark_svg_path = os.path.join(IMAGES_DIR, "novaarc-logo-horizontal-dark.svg")
    with open(horiz_dark_svg_path, "w") as f:
        f.write(generate_horizontal_logo_svg(is_dark=True))
    print("Wrote:", horiz_dark_svg_path)
    
    # 3. Stacked logo SVG (Light text for footer)
    stacked_svg_path = os.path.join(IMAGES_DIR, "novaarc-logo-stacked.svg")
    with open(stacked_svg_path, "w") as f:
        f.write(generate_stacked_logo_svg(is_dark=False))
    print("Wrote:", stacked_svg_path)
    
    # Stacked logo SVG (Dark text for white background)
    stacked_dark_svg_path = os.path.join(IMAGES_DIR, "novaarc-logo-stacked-dark.svg")
    with open(stacked_dark_svg_path, "w") as f:
        f.write(generate_stacked_logo_svg(is_dark=True))
    print("Wrote:", stacked_dark_svg_path)
    
    # 4. Favicon SVG
    fav_svg_path = os.path.join(IMAGES_DIR, "favicon.svg")
    with open(fav_svg_path, "w") as f:
        f.write(generate_icon_svg())
    print("Wrote:", fav_svg_path)
    
    # 5. Render PNGs
    # Standalone icon PNG (512x512)
    icon_png_path = os.path.join(IMAGES_DIR, "novaarc-icon.png")
    render_svg_to_png(icon_svg_path, icon_png_path, 512, 512)
    
    # Standalone dark icon PNG (512x512)
    icon_dark_png_path = os.path.join(IMAGES_DIR, "novaarc-icon-dark.png")
    render_svg_to_png(icon_dark_svg_path, icon_dark_png_path, 512, 512)
    
    # Horizontal logo PNG (600x120)
    horiz_png_path = os.path.join(IMAGES_DIR, "novaarc-logo-horizontal.png")
    render_svg_to_png(horiz_svg_path, horiz_png_path, 600, 120)
    
    # Horizontal dark logo PNG (600x120)
    horiz_dark_png_path = os.path.join(IMAGES_DIR, "novaarc-logo-horizontal-dark.png")
    render_svg_to_png(horiz_dark_svg_path, horiz_dark_png_path, 600, 120)
    
    # Stacked logo PNG (600x500)
    stacked_png_path = os.path.join(IMAGES_DIR, "novaarc-logo-stacked.png")
    render_svg_to_png(stacked_svg_path, stacked_png_path, 600, 500)
    
    # Stacked dark logo PNG (600x500)
    stacked_dark_png_path = os.path.join(IMAGES_DIR, "novaarc-logo-stacked-dark.png")
    render_svg_to_png(stacked_dark_svg_path, stacked_dark_png_path, 600, 500)
    
    # Update legacy file images/nova-arc-logo.png with the new 512x512 icon!
    legacy_logo_path = os.path.join(IMAGES_DIR, "nova-arc-logo.png")
    im_512 = Image.open(icon_png_path)
    im_512.save(legacy_logo_path)
    print("Updated legacy file:", legacy_logo_path)
    
    # 6. Generate Favicon variants
    # Favicon 16x16
    fav16 = im_512.resize((16, 16), Image.Resampling.LANCZOS)
    fav16_path = os.path.join(IMAGES_DIR, "favicon-16x16.png")
    fav16.save(fav16_path)
    print("Wrote:", fav16_path)
    
    # Favicon 32x32
    fav32 = im_512.resize((32, 32), Image.Resampling.LANCZOS)
    fav32_path = os.path.join(IMAGES_DIR, "favicon-32x32.png")
    fav32.save(fav32_path)
    print("Wrote:", fav32_path)
    
    # Apple Touch Icon 180x180 (with subtle rounded dark navy container for home screen)
    touch_im = Image.new("RGBA", (180, 180), (11, 37, 69, 255))
    icon_inset = im_512.resize((140, 140), Image.Resampling.LANCZOS)
    touch_im.paste(icon_inset, (20, 20), icon_inset)
    apple_touch_path = os.path.join(IMAGES_DIR, "apple-touch-icon.png")
    touch_im.save(apple_touch_path)
    print("Wrote:", apple_touch_path)
    
    # Multi-resolution favicon.ico (16, 32, 48)
    fav48 = im_512.resize((48, 48), Image.Resampling.LANCZOS)
    root_ico = os.path.join(REPO_ROOT, "favicon.ico")
    images_ico = os.path.join(IMAGES_DIR, "favicon.ico")
    legacy_ico = os.path.join(IMAGES_DIR, "nova-arc-logo.ico")
    
    fav16.save(root_ico, format="ICO", sizes=[(16, 16), (32, 32), (48, 48)], append_images=[fav32, fav48])
    fav16.save(images_ico, format="ICO", sizes=[(16, 16), (32, 32), (48, 48)], append_images=[fav32, fav48])
    fav16.save(legacy_ico, format="ICO", sizes=[(16, 16), (32, 32), (48, 48)], append_images=[fav32, fav48])
    print("Wrote:", root_ico, images_ico, legacy_ico)

if __name__ == "__main__":
    main()
