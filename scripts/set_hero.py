#!/usr/bin/env python3
"""Swap the hero photo in index.html.

The hero image is stored inline in index.html as a base64 data URI. This helper
re-embeds any image file into that <img class="hero-photo"> so you can switch or
revert the hero picture with one command.

Usage (run from the repo root):
    python3 scripts/set_hero.py                                   # use current hero file
    python3 scripts/set_hero.py assets/generated/couple-hero-previous.jpg   # revert to old photo
    python3 scripts/set_hero.py path/to/any-780x851.jpg           # use a new crop

The image should already be cropped to the hero aspect ratio (780 x 851).
After running, commit & push:
    git commit -am "Update hero photo" && git push
"""
import sys, re, base64, pathlib

img = sys.argv[1] if len(sys.argv) > 1 else "assets/generated/couple-hero.jpg"
path = pathlib.Path(img)
if not path.exists():
    sys.exit(f"error: image not found: {img}")

ext = "png" if path.suffix.lower() == ".png" else "jpeg"
uri = f"data:image/{ext};base64," + base64.b64encode(path.read_bytes()).decode()

index = pathlib.Path("index.html")
html = index.read_text()
html, n = re.subn(
    r'<img class="hero-photo" src="data:image/[^;]+;base64,[^"]+" alt="Pranshul and Shilpee">',
    f'<img class="hero-photo" src="{uri}" alt="Pranshul and Shilpee">',
    html,
)
if n != 1:
    sys.exit(f"error: expected exactly 1 hero image in index.html, found {n}")

index.write_text(html)
print(f"Hero photo set to '{img}' ({len(uri) // 1024} KB). Now: git commit -am '...' && git push")
