# Logo rules for Claude Daycare

For the Logo section of the style guide. Claude Daycare is the team's own product; this is its mark, its lockup and the rules for using them. Every file named here is in this folder. `matrix.html` shows all of them on white and on ink.

## 1. What the mark is

Three horizontal bars of different lengths that all stop short of one solid vertical wall. Read it as usage under a hard cap: the bars are what has been used, the wall is the allowance limit, and the bars never touch it. This is the "10 Capped bars" finalist from logo round 3, unchanged.

- It says allowance, not daycare. The word "Daycare" in the name carries that half. Round 3 recorded this as a known weakness and it still holds.
- It is plain rectangles, so it can also be read as a text-align or list icon at small sizes. The wall is what stops that reading, so never crop or hide the wall.
- It is not a letter, not an A, and has no starburst, asterisk or radiating shape. It uses no Anthropic or Claude logo.

Geometry (the files keep it exactly; do not redraw it). The artwork is filled rectangles on a lattice of 16 cells of 6.25 units inside a 100-unit box, and the ink spans cells 1 to 15, so the ink is 14 cells (87.5 units) tall and wide:

| Part | Length | Thickness |
|---|---|---|
| Top bar | 6 cells (37.5 units) | 2 cells (12.5 units) |
| Middle bar | 10 cells (62.5 units) | 2 cells |
| Bottom bar | 4 cells (25 units) | 2 cells |
| Wall | 14 cells (87.5 units), full height | 2 cells |

Between bars: 3 cells. Between the longest bar and the wall: 2 cells. The unit used below, "cell", is 1/14 of the mark's visible height.

## 2. The lockup: mark beside the name

1. The mark is as tall as the capital letters of the name. Measure on the mark's ink (the wall, top to bottom), not on the 100-unit box. The box is 14.3% taller than the ink.
2. The bottom of the mark sits on the baseline. The top of the wall sits on the cap line.
3. The gap between the right edge of the wall and the left edge of the C is half the cap height, measured ink to ink.
4. The name is "Claude Daycare", in that case and spelling, set in Hanken Grotesk at weight 700 and converted to outlines. No letter-spacing, no all caps, no italics. Kerning from the font is applied (see section 7).
5. The mark is on the left. The other arrangement is the stacked version (rule 7). Nothing else.
6. The mark and the name are always the same single colour.

In units where the cap height is 100: the mark is 100 by 100, the gap is 50, the name's ink is 1022.3 wide, and the whole ink is 1172.3 wide by 131.4 tall (the C and y reach past the cap line and baseline; see below). So the lockup is about 11.7 cap heights wide.

Measured in `lockup.svg` and its three twins, from their outlines: mark height 100.000, height of the flat capital D 100.000, mark bottom 0.000 and D bottom 0.000 (the baseline), gap 50.000. The round C overshoots the cap line and baseline by 2.24 units (2.2% of the cap height), as round letters do; the flat letters D, l and d and the wall sit exactly on both lines. Do not "fix" the overshoot.

Differences from the mock headers in `brand/logo-round-3/check.html` in the team's working repo (not in this folder): that page measured the half-cap gap to the start of the text box, which adds the C's left side bearing (about 0.056 of a cap height). The lockup here measures to the ink of the C, so the same gap looks the same in every font.

Stacked version (`stacked.svg`):

7. The mark sits above the name, centred on the name's ink width. The mark is 4 cap heights tall (a 14-cell mark at 4 cap heights makes a cell of 2/7 of a cap height). The gap from the bottom of the mark to the cap line of the name is 4 cells, the same as the mark's clear space (1.14 cap heights). In the same units, the name's ink is 1022.3 wide and the mark is 400 wide.

How to place the files: `lockup.svg` and its twins carry a one-cell margin all round (7.14 units when the cap height is 100), so for a cap height of `c` pixels the image is about `1.457 c` high and `11.866 c` wide. Do not rebuild the lockup by sizing `mark.svg` next to live text.

## 3. Colours

Only four colours exist in the logo files.

| Name | Value | Where |
|---|---|---|
| Ink | #1f1e1a | Mark and name on light grounds; the panel of every "on ink" file |
| Near-white | #f7f6f2 | Mark and name on ink |
| Black | #000000 | One-colour version, black-only print |
| White | #ffffff | One-colour version, over photos or any dark ground that is not ink |

- **On light grounds** (white or a light paper): ink. Contrast of ink on white is 16.7 to 1.
- **On dark grounds:** near-white on ink, using the `_on_ink` files, which carry their own ink panel. Contrast is 15.4 to 1. On a ground that is already ink the panel simply disappears, which is fine. On any other dark colour or a photo, use the white one-colour version instead of a visible ink box.
- **One colour:** `mono_black` and `lockup_mono_black` (pure #000000) for black-only print, stamps and photocopies; `mono_white` and `lockup_mono_white` (pure #ffffff) over photos and dark grounds. On a mid-tone or photo ground, pick whichever of black or white contrasts more, and aim for at least 4.5 to 1.
- The whole logo is one colour at a time. No two-tone version, no coloured wall, no accent colour on one bar, no tints, no transparency.

Favicon background rule: the favicon, the app icons and the avatar are the near-white mark on a full-bleed ink square, at every size, with square corners and no transparency. The ink tile shows against a light browser tab strip, and the near-white mark shows against a dark one. Do not round the corners yourself; iOS and Android apply their own mask.

## 4. Clear space

Clear space is four cells: two bar thicknesses, 25 units of the 100-unit mark box, 28.6% of the mark's visible height. For the lockup it is 0.286 of the cap height on every side. I chose two bar thicknesses (not one cell) so the space around the logo is clearly larger than the 2-cell gap between the longest bar and the wall; otherwise a neighbouring object could look like part of the mark.

- Measure from the outermost ink of the logo: for the lockup, the leftmost edge of the mark, the top of the C, the right edge of the final "e" and the bottom of the y.
- Nothing else (text, image edges, other logos) goes inside it. The `_on_ink` lockup and stacked files build this space into their ink panel.
- The transparent SVGs carry only a one-cell margin, to keep anti-aliased edges from being clipped. That margin is not the clear space.
- Exception: `mark_on_ink.svg`, `favicon.svg` and the favicon PNGs keep the one-cell margin. The edge of the tile is the boundary there and the mark has to be as large as possible at 16 px.

## 5. Smallest size

What I saw, rendered with macOS Quick Look and enlarged with nearest-neighbour. Nothing below was looked at on a real device.

**Mark alone: 16 px box (the ink is 14 px).**
- At 16, 32, 48 and 64 px every edge lands on a whole pixel: the 16 px render has two colours and no grey pixels; the bars are 2 px thick.
- At 20 and 24 px it reads clearly, with soft edges.
- At 14 and 12 px I could still count three bars and a wall, but the bars were grey and the wall thin.
- At 10 and 8 px the bars smeared into grey blocks. Do not go below 16 px.
- Prefer a box of 16, 32, 48 or 64 px where you can.
- `mark_square.svg` and `mark_square_on_ink.svg` are padded to 72%, so their bars are 9 units thick, not 12.5. By arithmetic (not by eye) they need a box of at least 24 px to keep bars at 2 px.

**Lockup: cap height 14 px (type size about 20 px, image about 20 px high by 166 px wide).**
- At a cap height of 14 px the mark's cell is exactly 1 px, so its edges are crisp when the lockup sits on a whole-pixel position.
- At 12 px the name reads and the bars are soft but visible. At 10 px the bars are soft. At 8 px and 6 px they smear into dashes. So the minimum is 14 px, and I would not go under 12 px even as a last resort.

**Stacked: name cap height 8 px (type size about 11 px), which makes the mark 32 px tall.**
- At a cap height of 6 px the name was very small and smudged. I looked at the stacked version only enlarged 4 times.

Print: not tested, so there is no millimetre minimum. Use the pixel sizes above at the resolution of the print.

## 6. What never to do

- No gradients, shadows, glows, blurs, textures or any filter.
- No stretching or squashing. Scale evenly only; a square stays a square.
- No outlines or strokes around or inside the mark, and no hollow version. It is filled shapes.
- No rotation, no tilt, no mirroring, no animation that moves the bars past the wall.
- Do not change the bar lengths, the thicknesses, the gaps or the wall, and do not recolour a single part.
- Do not retype the name beside the mark. Use the outlined lockup file. Do not change the space between mark and name, or put the name on the left.
- Do not add an A, a starburst, an asterisk or any radiating shape, and do not use or imitate an Anthropic or Claude logo.
- Do not place it on a busy photo or on a colour with less than 4.5 to 1 contrast.
- Do not use it below the minimum sizes in section 5.
- Do not crop the wall or the margin, and do not pre-round the favicon corners.

## 7. The name and the font

- The name is set in Hanken Grotesk, weight 700, in the files `lockup*.svg` and `stacked*.svg`. The letters are outlines, so no file needs the font and none contains a `<text>` element.
- Source: the variable font file `HankenGrotesk[wght].ttf` (132,892 bytes) from https://raw.githubusercontent.com/google/fonts/main/ofl/hankengrotesk/ , instanced at wght=700 with fontTools 4.66.1. Cap height of the flat H and D is 697 of 1000 units.
- Licence: SIL Open Font License 1.1, "Copyright 2021 The Hanken Grotesk Project Authors (https://github.com/marcologous/hanken-grotesk)". I downloaded and read `OFL.txt` from https://raw.githubusercontent.com/google/fonts/main/ofl/hankengrotesk/OFL.txt on 2026-10-09. It declares no Reserved Font Name. The licence lets the font be used, embedded, modified and redistributed if the font itself is not sold by itself and any copy of the font carries the notice and licence. This folder does not contain the font, only outlines drawn from it. My reading is that outlined letters in a logo are artwork made with the font, which clause 5 leaves outside the licence's requirements; that is my reading, not legal advice.
- Kerning: read from the font's own pair-adjustment table (GPOS `kern`) and applied to three pairs: a-y -14, y-c -18 and r-e -26 font units out of 1000. I checked the total in a browser: the kerned width of "Claude Daycare" at weight 700 came out 1 font unit (of 7,204) wider than my layout, and the browser's unkerned minus kerned width was 58 units, the same as my three pairs. No substitution feature that is on by default (ccmp, liga) changes any letter of this name; the one `locl` rule that touches "l" applies only to Catalan.
- If the team's heading font changes, the lockup, stacked and avatar files must be regenerated so the logo matches. Run `build_logo_set.py` with the new font file (below). Hanken Grotesk was the font used on the round-3 check page and is not a decision about the product's type; if the style guide picks another font, regenerate.

Regenerating:

```
python3 -m venv venv
venv/bin/pip install fonttools
venv/bin/python3 build_logo_set.py --font "/path/to/font.ttf" --weight 700
```

This rewrites the seven font-dependent or derived SVGs: the four lockups, the two stacked versions and `avatar.svg`. It reads `mark.svg` beside it. It does not change the mark files, the favicon, or the PNGs. The favicon and avatar PNGs do not depend on the font; only the lockup and stacked files do.

## 8. Files

SVGs (no `<text>`, gradients, filters, scripts, strokes or links; one well-formed XML root with a `viewBox`):

| File | Use |
|---|---|
| `mark.svg` | Mark alone, ink on light grounds. One-cell margin. |
| `mark_square.svg` | Mark centred and padded (72%) in a square, transparent, for square slots on light grounds. |
| `mark_on_ink.svg` | Near-white mark on an ink square, one-cell margin. The favicon artwork. |
| `mark_square_on_ink.svg` | The padded square mark on an ink square, for tiles on dark or mixed grounds. |
| `lockup.svg` | Mark beside the name in ink, transparent. Headers, documents, slides on light grounds. |
| `lockup_on_ink.svg` | The lockup in near-white on an ink panel with the clear space built in. |
| `mono_black.svg` | Mark in pure black, transparent. |
| `mono_white.svg` | Mark in pure white, transparent. Invisible on a white page. |
| `lockup_mono_black.svg` | Lockup in pure black, transparent. |
| `lockup_mono_white.svg` | Lockup in pure white, transparent. |
| `stacked.svg` | Mark above the name in ink, for square or portrait spaces. |
| `stacked_on_ink.svg` | Stacked version in near-white on an ink panel with the clear space built in. |
| `avatar.svg` | Social profile picture, vector. Mark at 5/8 scale on an ink square. |
| `favicon.svg` | Browser tab icon for browsers that take SVG. Same artwork as `mark_on_ink.svg`. |

PNGs and ICO (all near-white mark on an ink square, no transparency):

| File | Size | Use |
|---|---|---|
| `favicon-16.png` | 16 by 16 | Browser tab, smallest. |
| `favicon-32.png` | 32 by 32 | Browser tab on a 2x screen, taskbar. |
| `favicon-48.png` | 48 by 48 | Site-icon lists, Windows. |
| `apple-touch-icon.png` | 180 by 180 | iOS home-screen icon. |
| `favicon-192.png` | 192 by 192 | Android and web-app manifest icon. |
| `favicon-512.png` | 512 by 512 | Web-app manifest icon, splash. |
| `avatar-512.png` | 512 by 512 | Social profile upload. |
| `favicon.ico` | 16, 32, 48 inside | Legacy favicon at the site root. |

Other files: `matrix.html` (every file on white and on ink), `build_logo_set.py` (regenerates the lockup, stacked and avatar SVGs), this file.

Suggested head tags (not tested in a browser tab): `<link rel="icon" href="/favicon.ico" sizes="48x48">`, `<link rel="icon" href="/favicon.svg" type="image/svg+xml">`, `<link rel="apple-touch-icon" href="/apple-touch-icon.png">`, and the 192 and 512 files in the web-app manifest.

Avatar: the mark alone, no name (platforms print the name beside the picture). The mark is at 5/8 of its normal size on the ink square, so its farthest corner is 38.7 units from the centre of the 100-unit square. That keeps it inside a circular crop (radius 50) and inside the 40-unit safe circle that Android uses for maskable icons. At 512 px a cell is exactly 20 px, so the edges are crisp.

## 9. How the PNGs were made, and what is approximate

- Rendered from `favicon.svg` and `avatar.svg` with macOS Quick Look (`qlmanage -t -s <px>`), at the exact size of each file, then written as opaque 24-bit PNG with ImageMagick (`magick in.png -alpha off -strip PNG24:out.png`). `favicon.ico` is the three PNGs combined by `magick favicon-16.png favicon-32.png favicon-48.png favicon.ico`; each frame is pixel-identical to its PNG.
- 16, 32 and 48 px were rendered at their own size, not shrunk from a larger render. As a check I also shrank a 960 px render with a box filter, and the result was identical pixel for pixel to the direct renders (two colours only, no grey pixels). That holds because every edge of the artwork lies on a whole cell, and a cell is 1, 2 and 3 px at those sizes. They are still Quick Look's drawing, not what a browser or operating system would make for its own tab, so treat them as close approximations.
- 192, 512 and the 512 px avatar were rendered at their exact size and also have only two colours (a cell is 12 px, 32 px and 20 px).
- 180 px was rendered at its exact size. A cell is 11.25 px there, so the edges are anti-aliased (nine colours); this cannot be avoided at that size.

## 10. What I could not check

- No favicon was looked at in a real browser tab (light or dark), on an iPhone home screen, in an Android manifest, in a maskable-icon preview, or in a social profile crop.
- Print was not tested. The minimum sizes come from Quick Look renders and (for the lockup and stacked) renders I placed on whole-pixel positions; screens and browsers may differ.
- There was no look-alike or trademark search. "Not like an Anthropic or Claude mark" is a judgement by eye.
- `mark_square.svg` and `mark_square_on_ink.svg` were not looked at small; the 24 px figure for them is arithmetic.
- The SVGs were checked by parsing and by measuring outlines, and the matrix page was opened in the in-app browser; no other browser was tried.
- Nothing here has been seen by the team.
