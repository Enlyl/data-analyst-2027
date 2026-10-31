# -*- coding: utf-8 -*-
import re

for path in [r"d:\vibe_app\main_data_analytics\index.html", r"d:\vibe_app\main_data_analytics\course\index.html"]:
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # Make .brand div and topbar-title clickable to return to hero page
    html = html.replace('<div class="brand">', '<div class="brand" onclick="showHero()" style="cursor: pointer;" title="На главную">', 1)
    html = html.replace('<div class="topbar-title" id="topbarTitle">Data Analyst 2027</div>', '<div class="topbar-title" id="topbarTitle" onclick="showHero()" style="cursor: pointer;" title="На главную">Data Analyst 2027</div>', 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

print("Updated brand and title click handlers to return to home page.")
