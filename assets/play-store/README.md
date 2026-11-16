# Play Store assets

Graphics for the Google Play listing. Both are generated from the launcher icon
artwork (`app/src/main/res/drawable/ic_launcher_foreground.xml`) on the
`#0F1419` background.

| File | Size | Used for |
| --- | --- | --- |
| `icon-512.png` | 512x512 | Play app icon |
| `feature-graphic-1024x500.png` | 1024x500 | Play feature graphic |

Regenerate with `python3 make_assets.py` (needs Playwright and Chromium).

Phone screenshots go in `screenshots/` (PNG or JPEG, at least 2, 1080 px or larger per side).
