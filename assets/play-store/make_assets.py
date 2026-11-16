"""Render Stride's Play Store graphics from the repo's ic_launcher_foreground vector.

Source: app/src/main/res/drawable/ic_launcher_foreground.xml
Usage: python3 make_assets.py [output_dir]   (needs playwright + Chromium, Inter font)
Background: #0F1419 (ic_launcher_background). Paths are copied unchanged.
"""
import os
import sys
from playwright.sync_api import sync_playwright

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))

ART = """
<path fill="#3FB950" d="M24,66 L84,66 A6,6 0 0 1 84,78 L24,78 A6,6 0 0 1 24,66 Z"/>
<path fill="#0F1419" d="M30,72 m-3,0 a3,3 0 1 0 6,0 a3,3 0 1 0 -6,0"/>
<path fill="#0F1419" d="M78,72 m-3,0 a3,3 0 1 0 6,0 a3,3 0 1 0 -6,0"/>
<path fill="#3FB950" d="M36,56 L50,56 A3,3 0 0 1 50,62 L36,62 A3,3 0 0 1 36,56 Z"/>
<path fill="#3FB950" d="M46,44 L66,44 A3,3 0 0 1 66,50 L46,50 A3,3 0 0 1 46,44 Z"/>
<path fill="#3FB950" d="M56,32 L80,32 A3,3 0 0 1 80,38 L56,38 A3,3 0 0 1 56,32 Z"/>
"""

ICON_HTML = f"""<!doctype html><html><body style="margin:0;background:#0F1419">
<svg width="512" height="512" viewBox="0 0 108 108" xmlns="http://www.w3.org/2000/svg" style="display:block">
<rect width="108" height="108" fill="#0F1419"/>{ART}</svg></body></html>"""

FEATURE_HTML = f"""<!doctype html><html><head><style>
html,body{{margin:0;padding:0}}
body{{width:1024px;height:500px;background:#0F1419;position:relative;overflow:hidden;
font-family:'Inter',sans-serif}}
.art{{position:absolute;left:84px;top:147px;width:300px;height:205px}}
.txt{{position:absolute;left:424px;top:0;height:500px;display:flex;flex-direction:column;justify-content:center}}
h1{{margin:0;font-size:120px;line-height:1;font-weight:800;letter-spacing:-3px;color:#F0F6FC}}
.tag{{margin-top:18px;font-size:32px;font-weight:500;color:#9DA7B3}}
.pill{{margin-top:22px;font-size:26px;font-weight:600;color:#3FB950;letter-spacing:.2px}}
</style></head><body>
<svg class="art" viewBox="16 29 76 52" xmlns="http://www.w3.org/2000/svg">{ART}</svg>
<div class="txt"><h1>Stride</h1>
<div class="tag">Your walking pad, one screen.</div>
<div class="pill">No account. No internet. No ads.</div></div>
</body></html>"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 512, "height": 512}, device_scale_factor=1)
    pg.set_content(ICON_HTML)
    pg.screenshot(path=f"{OUT}/icon-512.png", omit_background=False)
    pg = b.new_page(viewport={"width": 1024, "height": 500}, device_scale_factor=1)
    pg.set_content(FEATURE_HTML)
    pg.wait_for_timeout(300)
    pg.screenshot(path=f"{OUT}/feature-graphic-1024x500.png", omit_background=False)
    b.close()
print("done")
