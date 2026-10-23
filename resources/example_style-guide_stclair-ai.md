# Example style guide: St. Clair AI

*A real, working style guide: the one behind [stclair.ai](https://stclair.ai). File paths point to files in that project. Use it as a model for how specific yours can get.*

---

# St. Clair AI style guide (summary, Sep 9, 2026)

The site is the reference implementation: `site/index.html`. This is the short version for anyone designing against it. The long version, with every decision and the reason, is `tearsheets/REVIEW_NOTES.md`.

## Color

| Token | Hex | Job |
|---|---|---|
| ink | #1f1e1a | Text, footer and CTA bands, secondary button outlines, rules |
| ink faint | #6b6860 | Hints, meta lines (5.56:1 on white) |
| white | #ffffff | Page ground |
| purple | #46188c | Lead accent: primary buttons, the one saturated thing per screen. Hover #35126b |
| cobalt | #0760c7 | Structure: the announcement band, solid product band, illustration accents |
| cobalt tint | #e6effc | Code blocks, table headers |
| sage | #8fb5a0 | Soft third: bullet dots, illustration fills |
| sage tint | #e7f1ed | The about section |
| link | #6d28d9 | Body links on white; inline links inside copy are ink instead |

Rules: more than one color on a page, even in tiny doses, but one accent per element. One color per button pair (purple primary beside an ink-outline secondary). A solid band is rhythm, not a spotlight. Never a gradient.

## Type

- **Headings:** Schibsted Grotesk 600 and 700. Hero h1 large, section h2 mid, card h3 18px. Sentence case for every heading; proper nouns keep their capitals. No all caps.
- **Body:** Hanken Grotesk 400 and 500, 17 to 18px, line height 1.55 to 1.6, measure 62 to 68ch.
- **Wordmark:** "St. Clair AI" in Schibsted Grotesk 600 at nav size today. Normal width. Never scaleX, never font-stretch, never a face that reads as stretched.
- Rules match type: heavy rules only next to heavy type. Hairlines elsewhere.

## Space and layout

- Content width 1024px with a 44px inset. Sections 72px top and bottom (hero 72/104). Spacing scale s3 12, s4 16, s5 24, s6 32, s7 72 (approximate; see tokens in the page).
- Grids: services three columns above 860px; about copy plus a 340px photo above 860; hero two columns above 700.
- Proximity groups: a heading sits closer to what it labels than to what precedes it.

## Components

- **Buttons:** rectangular, 4px radius, 44px min height, Lucide icons at 1.75 stroke when used. Primary purple filled, secondary ink outline, on-dark white outline.
- **Icons:** Lucide, inline SVG, `currentColor`, stroke follows the type it sits beside: 1.5 with 400-weight body, 1.75 with 600-weight display and in buttons (settled on X3, Sep 9: "Okay, great. Yes."). Uses: a service card with the icon above the title (a keep: "you know I love an icon. These are good."); an icon beside a list title; an icon in a button. Examples in `tearsheets/X3_components.html`. Never custom-drawn icons beside Lucide ones; the mark is the only bespoke glyph.
- **Bands:** cobalt announcement band under the nav; solid cobalt products band; ink CTA and footer.
- **Cards:** full 1px ink borders or filled panels. Never a single-side colored border. No shadows.
- **Lists:** sage dot bullets. **Tables** over callouts; full borders, tinted header row, no zebra.
- **Blog block:** one featured post as a full-bordered panel with a 200 by 150 illustration thumbnail on the left and the text on the right (stacks on phones). With several posts, the future layout is a featured split panel over thin thumbnail rows (L8, t6).
- **Blockquote:** copied from the command-center document design system (`lib/templates/document.css`), not invented locally: no fill, no full border, a 3px hairline-color (`--rule`) rule on the left, `ink-soft` text, `s4` padding-left. This is the one place a single-side border is right, because it is the same quote convention that system already uses (settled Sep 22, 2026, on the debugging-hell post).
- **Links:** inline links in copy are ink with a 1px underline, offset 3px; external links open a new tab; standalone links reach 44px.

## Imagery

- Hand-drawn isometric line illustrations on pure white: ink lines, one cobalt accent, one sage fill. Any scene with agents shows the person they help. Illustrations depict a subject, never an abstract diagram.
- Photos are objects and workplaces, not stock people. Only Ken appears in the about. No wood tables. Check props and text in frame.
- Alt text tells the truth about how an image was made.

## Accessibility floors

4.5:1 text contrast, visible focus on every control, 44px tap targets, real landmarks and heading order, a skip link, reduced motion respected (stills instead of loops).

## Never

Em dashes. Pills. Gradients. Single-side colored borders. Partial-width rules. Grid behind text. Stretched type. Stock people. Sparkles, brains, circuits, hexagons.

## Logo (decided Sep 9, 2026)

The brand kit, `brand/BRAND_KIT.md`, is the reference for using the logo; `brand/LOGO.md` records how it was chosen.


The mark is a proofreader's insert caret under a three-segment line, which is also the NAND glyph. Parameters on a 100-unit box: stroke 12.5; three segments of 20.5 with 9.5 gaps, mirrored about center; the middle segment cobalt (#0760c7) on white and sage (#8fb5a0) on ink; caret arms at 50 degrees, caret height 0.9 of the base (34.2 units), apex 11 units clear of the line. Files in `brand/logo/`: `mark.svg` (fitted), `mark_square.svg` and `favicon.svg` (square), `mark_on_ink.svg`, one-color `mark_mono_ink.svg` and `mark_mono_white.svg`, `lockup.svg` and `lockup_on_ink.svg` (mark left of the wordmark, mark height equal to the wordmark cap height, mark bottom on the baseline, gap half the cap height), plus `mark_<color>.svg` and `lockup_<color>.svg` for cobalt, purple, sage, and ink-only middles (cobalt is the default; sage is the approved alternate on white and ink; the one-color ink and white marks are approved for print and single-color use; purple was rejected in the lockup), `lockup_stacked.svg` and `avatar.svg` (square, for social), favicons at 16, 32, 48, 180, 192, 512 and `favicon.ico`. Generator: `scripts/finalize_logo.py` from `scripts/nand_grid.py`. Rules: never a serif wordmark; the wordmark is live Schibsted Grotesk 600 text beside the inline mark on the site; the colored segment stays centered; the apex never touches the line; the mark's stroke sits close to the wordmark stem (12.5 on the 100 box is about 5 percent over the stem at nav size); in the nav and footer the mark is exactly the cap height (0.7036 em of Schibsted Grotesk 600), baseline aligned, with a gap of 0.35 em; 1.2 times cap height "oversizes against the text" (Ken, Sep 9).
