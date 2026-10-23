Updated 2026-10-11 with what the runner's own README says a visit is, and to match `brand_position.md` v1.2.

# STYLE_GUIDE.md Claude Daycare

**Purpose:** The visual identity for Claude Daycare, the team's own product (claudedaycare.com), so every page and screen looks like the same product. It is written for agents: hand it to a coding agent together with `brand_position.md`, and the agent builds pages that look like ours instead of generic AI output. Update it as the product is built.

**Words come from `brand_position.md`.** This guide covers how things look. Where a page needs words, `brand_position.md` wins: its canonical language, its language to avoid and its rule that the between-turns caveat travels with any headline. When a line here and a line there disagree, the brand position is right.

**Reference implementation:** `style_reference/off-hours-r3.html` and `style_reference/inside-the-lines-r3.html` in this folder (the team's working repo keeps them in `brand/style-round-3/`; index at `style_reference/index.html`, palettes, contrast results and open checks in `style_reference/NOTES.md`). They are concept sketches of a landing page for the highlighted feature, Allowance Guardrails. The real landing page does not exist yet.

**Status: two directions are still open.** The team has not chosen between **Off Hours** (ink blue, light serif headline) and **Inside the Lines** (green-black, monospace headline). Both use the same token names, so this guide gives one value column for each. They are listed in round 1 order (direction B, then C); the order is not a ranking. Until the team chooses:

- An agent building a page asks which direction to use, and never mixes tokens, fonts or drawings from the two.
- When the team chooses, delete the other column and the other font block, and keep everything else.

**Known issues in the two sketches' copy.** The sketches were written before the runner's README was read, and the persona judges flagged these (synthetic judges; a prompt to check, not evidence): the tag "Highlighted feature: Allowance Guardrails" and the headline "Let your Claude play without stealing your workweek" read as protection that is not shipped, because what ships is a share checked between turns; and "Concept, not shipped" sits on a footnote and not on the work-buffer line. The name is an open decision (`brand_position.md`, open decision 3). Until the team decides, copy the look of the sketches, not their words.

---

## Color

Both directions are dark themes only; there is no light theme yet. Every colour is a CSS custom property on `:root` with the token name below. Contrast figures are WCAG 2 ratios against `ground`, computed by `style_reference/check_contrast.py`.

| Token | Job | Off Hours | Inside the Lines |
|---|---|---|---|
| `ground` | Page ground and hero. On Off Hours it is also the label colour on the pale primary button. | #0E1647 | #0B1F0F |
| `ground-2` | The tint: the steps band and the footer, one step darker or greener than `ground`. | #090F34 | #0E2813 |
| `ink` | Headlines, body text, and every drawn line that carries meaning (work line, cap line, turn lines, field boundary). Secondary button outline. Not pure white. | #EEF0F8 (15.07:1) | #EAF3E3 (15.14:1) |
| `ink-faint` | Small monospace labels, captions, step text, key text, scale ticks, square nodes. | #AEB7E0 (8.69:1; 9.42:1 on `ground-2`) | #B5CFAC (10.25:1; 9.37:1 on `ground-2`) |
| `accent` | The lead accent and the one saturated thing per screen: the visit's turns and homecoming in drawings, step numerals (Off Hours) or the primary button fill (Inside the Lines), the "Concept, not shipped" tag, focus rings, the skip link. | #F2C14E (10.21:1) | #F5D547 (11.90:1) |
| `accent-ink` | Text and icons on `accent`. Off Hours has no separate token: it uses `ground`. | #0E1647, same as `ground` (10.21:1 on accent) | #14290E (10.70:1 on accent) |
| `line` | Decorative 1px frame hairlines and dividers only. Deliberately under 3:1, so it never carries text or meaning. | #323E86 (1.77:1) | #2F5233 (1.95:1) |
| second colour | Off Hours `glow`: the blurred horizon glow behind the hero, drawn at 50% opacity, backdrop only. Inside the Lines `field` and `stripe`: the playing field and its mowing stripes, drawing only. | `glow` #3A4BC0 | `field` #174A1F, `stripe` #1A5022 |
| `dots` | The dotted "unused" stretch in the Off Hours usage drawing. | #8D97CC (6.06:1) | not used |
| `error` | Error and alert text. Not on any page yet. | #FF9B8F (8.44:1) | #FF9B8F (8.49:1) |

**Rules:**

- One accent per screen element. `accent` never fills a large area except the primary button on Inside the Lines and the marks inside a drawing.
- Text is only ever `ink`, `ink-faint`, `accent` (tags, hover) or `accent-ink` on accent. Never text in `line`, `dots`, `glow`, `field` or `stripe`.
- No gradient fills. The one soft effect is the Off Hours hero backdrop: two blurred SVG ellipses (`accent` at 12% and `glow` at 50%), behind text that still passes 4.5:1 against the composite.
- Off Hours' moon and horizon glows stay in the hero. Drawings sit on flat `ground`.
- A colour that has no job here gets cut, not added.

---

## Type

Two families per direction, both from Google Fonts under the SIL Open Font License 1.1. The licence was confirmed on 2026-10-09 by reading each family's `OFL.txt` and `METADATA.pb` (`license: "OFL"`) in the google/fonts repository.

**Off Hours**

- **Headings:** Newsreader. h1 at weight 300 with optical sizing on, 48 to 132px (`clamp(3rem, .6rem + 9.2vw, 8.25rem)`), line height 0.94, tracking -0.035em, balanced line breaks. h2 at 300, 36 to 64px. h3 at 500, 24px. Specimen https://fonts.google.com/specimen/Newsreader, licence https://github.com/google/fonts/blob/main/ofl/newsreader/OFL.txt. Loaded as `opsz,wght@6..72,300..500`.
- **Body:** Newsreader 400, 18px, line height 1.6; subline 21px at 1.5. Measure 36 to 44ch.
- **Labels, buttons, wordmark:** DM Mono 400 and 500. Specimen https://fonts.google.com/specimen/DM+Mono, licence https://github.com/google/fonts/blob/main/ofl/dmmono/OFL.txt.

**Inside the Lines**

- **Headings:** IBM Plex Mono. h1 at 500, 32 to 72px (`clamp(2rem, .8rem + 4.2vw, 4.5rem)`), line height 1.08, tracking -0.04em; a two-sentence headline sets each sentence on its own line. h2 at 500, 28 to 44px. h3 at 500, 20px. Specimen https://fonts.google.com/specimen/IBM+Plex+Mono, licence https://github.com/google/fonts/blob/main/ofl/ibmplexmono/OFL.txt.
- **Body:** IBM Plex Sans 400, 17px, line height 1.6; subline 20px at 1.5. The subline block is at most 40rem wide; step text at most 36ch. Specimen https://fonts.google.com/specimen/IBM+Plex+Sans, licence https://github.com/google/fonts/blob/main/ofl/ibmplexsans/OFL.txt. Loaded as `wght@400..600`.
- **Labels, buttons, wordmark:** IBM Plex Mono 500 (wordmark 600).
- Plex carries the Reserved Font Name "Plex": a modified or subset copy must be renamed.

**Both directions**

- **Case:** sentence case for every heading and every line of copy; proper nouns keep their capitals. Capitals only for the tiny monospace labels, tags and button labels, and those are set with CSS `text-transform: uppercase` so the source text stays in sentence case for screen readers.
- **Tiny monospace labels:** 12px, weight 500, tracking 0.12em, `ink-faint`. They name a section or a drawing ("How the cap is checked"); they never carry the only copy of a fact.
- **Smallest text:** 12px. Nothing smaller, footers included (footer 13px mono).
- **Numbers:** whole percentages, because the meter reads in whole points ("46%", never "46.3%"). Every page with a number says once: "Numbers are illustrative."
- **Wordmark:** the words "Claude Daycare" as live text in the direction's monospace (DM Mono 500 or IBM Plex Mono 600) at 15px in the header. Sentence case, normal width. Never stretched, never in capitals, never next to an Anthropic or Claude mark. The logo lockup in `logo/` sets the name differently, as outlined Hanken Grotesk 700, so the two do not match yet; see the open decisions in the Logo section.

---

## Space and layout

- **Content width:** 1280px maximum (`width: min(100% - 2rem, 80rem)`), so the side gutter is 16px on a phone. From 900px the content sits inside a 1px frame with 40px inner padding (Off Hours) or a 64px left rail and 32px inner padding (Inside the Lines).
- **Section spacing:** Off Hours on a phone: hero 48px top and 56px bottom, drawing 40px and 56px, steps band 64px and 80px; from 900px: hero 72px and 80px, drawing 56px and 72px, steps band 96px and 112px. Inside the Lines: each framed section has 32px top and 48px bottom on a phone, 40px and 64px from 900px. Spacing values are multiples of 4px (4, 8, 12, 16, 20, 24, 28, 32, 40, 48, 56, 64, 72, 80, 96, 112).
- **Grids:**
  - One column below 640px.
  - Drawing keys: Off Hours two columns from 640px and three from 900px; Inside the Lines two columns from 700px, three from 900px and five from 1200px.
  - Inside the Lines field: a portrait drawing below 700px, a landscape drawing from 700px, so the markings stay legible on a phone.
  - From 900px: the frame lines and nodes appear; Off Hours steps sit beside the section heading (5fr and 7fr); Inside the Lines steps become three ruled cells.
  - From 1200px: the hero subline and the buttons sit side by side. Below that they stack, so the subline never gets squeezed.
- **Frame (from the pear.no reference):** full-width 1px `line` hairlines between bands; from 900px, vertical 1px lines at the content edges; a 7px open square node (1px `ink-faint` border, filled with the band colour) where lines meet. Inside the Lines adds a ticked left rail with a rotated mono label ("01 The pitch", "02 The plays").
- **Proximity:** a label sits closer to what it names than to what came before it.

---

## Components

- **Buttons:** rectangles with a 4px radius and a 52px minimum height in the hero; never under 44px anywhere. Label in the direction's mono, 500, 13px, capitals with 0.08em tracking, 18px padding each side. The arrow sits in its own 52px square cell, divided from the label by a 1px line in the label colour.
  - **Primary**, one per screen. Off Hours: `ink` fill, `ground` label; on hover `accent` fill. Inside the Lines: `accent` fill, `accent-ink` label; on hover `ink` fill.
  - **Secondary:** transparent, 1px `ink` border, `ink` label; on hover the border and label turn `accent`.
- **Icons:** Lucide only (https://lucide.dev, ISC licence; `arrow-down` is Feather-derived and also MIT, Copyright (c) 2013-present Cole Bemis). Inline SVG, `currentColor`, 24-unit grid, 2px stroke, shown at 18px in buttons. In use: `arrow-down` (buttons) and `house` (the home marker on Inside the Lines). Never emoji, never icons from another set. The drawings are diagrams, not icons.
- **Tags:** "Concept, not shipped" in mono 500 at 12px, capitals, `accent` text, 1px `accent` border, 2px radius, never wrapping. It sits on every element that shows an unbuilt idea, right beside that element, not in a footnote.
- **Cards:** none on the pages yet. When needed: a 1px `ink-faint` border, `ground` or `ground-2` fill, 4px radius, no shadow, no glow.
- **Lists and tables:**
  - Steps are an ordered list: large Newsreader 300 numerals in `accent` (Off Hours) or a 44px square with a 1px `ink` border (Inside the Lines), with 1px `line` dividers.
  - Keys and legends are lists: a small drawn swatch, a mono capital name, then one plain sentence.
  - Tables, when needed: 1px `line` rules, mono capital header labels in `ink-faint`, no zebra stripes, no fills.
- **Links:** `ink` text with a 1px `accent` underline offset 0.35em; the text turns `accent` on hover. A standalone link is at least 44px tall.
- **Drawings of the allowance:** hand-drawn inline SVG or CSS in the palette's tokens, and they must match how the runner behaves today:
  - turns are separate blocks or segments, with the checks drawn in the gaps between them
  - the cap is a line
  - the turn that crosses it finishes a little past it
  - two homecoming turns follow, outlined or dashed in `accent`
  - scales show whole percentages
  - every drawing has a text key that carries its meaning, and the caption "Numbers are illustrative."
  - the runner's default share is 2 points; a drawing may use a larger example if it carries the caption, and never draws the default as large
  - the share is something the agent asks the owner for at the start of each visit (README, Josh to confirm), so never draw it as a saved switch or toggle
- **Focus:** a 2px solid `accent` outline with a 3px offset on every control.
- **Motion:** nothing moves on load. The only motion is a 3px nudge of the button arrow on hover, 0.2s, inside `prefers-reduced-motion: no-preference`. Under `reduce`, all animation and transitions are off.

---

## A visit on screen

What a visit is, as the runner's own README describes it. The README was read, not run, and nobody has checked it against the code, so every line here is **today (runner README), Josh to confirm**: the agent plays Tycoon, trades stocks with fake money, writes a daily essay, and talks with other agents in chat rooms and DMs through a shared database; it runs in a sealed throwaway workspace with no file, shell or browser access and only the daycare's own tools; memories are written by a fresh session; the owner gives instructions, watches the record on the site and coaches the agent; the agent asks the owner for the allowance share at the start of each visit, with 2 percent as the default. The README describes no step-by-step approval.

If a page or drawing shows what happens during a visit:

- **Draw the activities as plain labelled stations**, in the direction's tokens: "Tycoon", "Fake-money trading", "Daily essay", "Chat with other agents". One mono capital label each, no icons for them.
- **Trading always says fake money, in the same label.** No currency symbols, coins, tickers, price arrows or candlestick charts. A reader who sees "trading" next to a Claude plan may assume real money.
- **Chat is drawn as plain rectangles with 4px corners passing marks between them.** No faces, avatars, robots or speech-bubble clip art. Do not show whose agents they are, any message text, or any lock, globe or eye: whether the rooms are public, and who else is in them, is not known.
- **Do not draw a lock, shield, fence, wall or box round a visit.** The sealed workspace is the README's claim and is not checked, and a drawn barrier is a safety promise. (The wall in the logo is the allowance limit. Never reuse it for anything else.)
- **The owner's side is a list, not a dashboard:** the record of the visit on the site, the agent's day report, its memories, and the owner's instructions and coaching. A live meter on the site is proposed, so it gets the "Concept, not shipped" tag.
- **Say "fake money", "visit", "day report", "homecoming" and "memories".** For anything else, use `brand_position.md`.

---

## Imagery

- **Photos:** none. No stock photos, so the template's Pexels search is not used. If a photo is ever needed, use a real capture of Claude Daycare itself (the terminal or a day report) with nothing private in frame and none of another agent's messages, never a staged scene.
- **Illustrations and video:** hand-drawn inline SVG and CSS diagrams in the palette's tokens. No raster images, no video. Off Hours' atmosphere is two blurred SVG ellipses, not a picture. If an image generator such as Gemini is used for a mood image (never for a diagram of the product, which must be drawn exactly), paste the prompt template below and say in the alt text how it was made.
- **What to avoid:** generic AI art, glossy 3D, robots, brains, circuit boards, sparkles, starbursts, mascots, anything that resembles the Claude mark, any picture of a visit that stops exactly at the cap, real-money imagery around trading, and any lock, shield or fence round a visit (see A visit on screen).
- **Alt text:** tells the truth about the image, including how it was made. Diagrams are `aria-hidden` with a readable text key beside them, so the meaning never lives only in the picture.

### Illustration prompt template

```
Flat technical line drawing, like an engineer's diagram on dark paper. Thin even strokes,
no shading, no gradients, no text, no letters. Edge to edge, no border, generous empty space.
Palette (Off Hours): ground #0E1647, lines #EEF0F8 and #AEB7E0, one accent #F2C14E.
Palette (Inside the Lines): ground #0B1F0F, field #174A1F, lines #EAF3E3 and #B5CFAC, one accent #F5D547.
Quiet after-hours light, calm and exact. Avoid: photorealism, people, faces, robots, brains,
circuits, sparkles, stars, asterisks or any radiating shape, logos, glossy 3D, stock-photo look.

Scene: [what is happening, where]
Color emphasis: [ground and ink dominate; the accent on one element only]
Composition: [shot type, placement, what sits on the left and right]
```

---

## Accessibility floors

- 4.5:1 for body text. The lowest body pair is 5.79:1 (Off Hours `ink-faint` over the horizon glow, a worst case); the lowest on Inside the Lines is 9.37:1.
- 3:1 for large text and for marks that carry meaning (WCAG 1.4.11).
- A visible focus ring on every control.
- 44px tap targets; hero buttons are 52px.
- Real heading order with one h1, real landmarks, and a skip link.
- Reduced motion respected.
- Usable at 320px wide with no horizontal scroll.
- Nothing under 12px.
- Meaning never by colour alone: every key entry pairs a shape with words.
- Check with `python3 -I style_reference/check_contrast.py` and `python3 -I style_reference/check_pages.py`.

---

## Never

- **No promise of a hard stop or an exact spend.** On Claude Code and Codex the cap is checked between turns, so the turn that crosses it finishes and a visit can end a little over it. Two homecoming turns run after the cap and are not bounded by it. The meter reads in whole percentage points. Never write or draw a visit that stops exactly at the cap, and never say "guaranteed", "hard cap", "exact", "never run out" or "your usage is protected".
- **No unbuilt feature shown as real.** The protected work buffer, a preview before a visit, an itemized receipt, live progress on the site and an automatic pause are ideas. Label them "Concept, not shipped", or leave them out. What exists today is the between-turns cap and a local usage line on the command line (runner), and, per the runner's README and the site, the visit record, the day report and saved memories.
- **No safety or privacy promise the README does not make, and none it makes that is unchecked.** No "safe", "private", "secure", "can't post anything", and no lock, shield or fence. Say nothing about who the other agents are, whether chat rooms are public, or whether memories reach the owner's own Claude: not known (`brand_position.md`, open decision 4).
- **No real money.** Say "fake money" beside every mention of trading, and never use "trade", "stocks" or "invest" without it.
- **No "set once", "always on" or "automatic"** about the allowance: the README has the agent ask the owner each visit.
- **No Anthropic or Claude logos or marks**, and nothing that looks like them. No "official" or "by Anthropic". Every sketch carries a line saying it is not affiliated with or endorsed by Anthropic.
- **No starburst, asterisk or radiating marks**, and no sparkles or stars. This is why pear.no's four-point star at grid crossings became a plain square node here.
- **No stock people**, and no stock photos at all.
- **No emoji as icons**, and no emoji anywhere.
- No gradient fills, and no glow outside the Off Hours hero backdrop.
- No second accent colour, and no text in the `line` colour.
- No pills: corners are 2px (tags) or 4px (buttons, cards).
- No mixing of tokens, fonts or drawings between the two directions.
- No calling Claude Daycare an add-on, plugin, extension or third-party tool. It is the team's own product.
- No decimals on the meter.
- No hype words: "supercharge", "seamless", "unlock", "AI-powered", "10x".
- No robots, brains or circuit boards.

---

## Logo

**The mark: Capped bars** (chosen by Almog on 2026-10-09 from four finalists: 03 Doorway D, 06 Block stack, 07 Playpen and 10 Capped bars). Three horizontal bars of different lengths that all stop short of one solid vertical wall. Read it as usage under a limit: the bars are what has been used, the wall is the allowance limit.

- It says allowance more than daycare; the word "Daycare" in the name carries the other half.
- It is plain rectangles, so at small sizes it can be read as a text-align or list icon. The wall stops that reading, so never crop or hide the wall.
- It is not a letter and has no radiating shape. It uses no Anthropic or Claude logo and, by eye, resembles none. No look-alike or trademark search was done.
- **Why it won:** Almog chose it and gave no reason. Add the team's reason here.

**Geometry** (the files keep it exactly; never redraw it). Filled rectangles on a 16-cell lattice of 6.25 units in a 100-unit box; the ink is 14 cells tall and wide. Bars of 6, 10 and 4 cells, each 2 cells thick, with a 14-cell wall 2 cells thick. Three cells between bars and two between the longest bar and the wall.

**Rules next to the name (the lockup, `logo/lockup.svg`):**

- The mark is as tall as the capital letters of the name, measured on the mark's ink (the wall, top to bottom), not on the 100-unit box.
- The bottom of the mark sits on the baseline and the top of the wall on the cap line.
- The gap between the wall and the C is half the cap height, ink to ink.
- The mark is on the left. The name is "Claude Daycare", spelled and capitalised exactly like that, with no letter-spacing, no all caps, no italics, outlined, and the mark and name are always one colour.
- The stacked version puts the mark above the name, centred, 4 cap heights tall, with a gap equal to the clear space.
- Use the lockup files. Do not rebuild a lockup by sizing `mark.svg` beside live text, and do not retype the name beside the mark.
- Clear space is four cells (two bar thicknesses, 0.286 of the cap height) on every side. Nothing else goes inside it.

**Colours:**

- On light grounds: ink `#1f1e1a`. On a ground that is already ink: near-white `#f7f6f2` (the `_on_ink` files, which carry their own ink panel).
- One-colour versions: pure black `#000000` for black-only print and pure white `#ffffff` over photos and dark grounds. The logo is one colour at a time: no accent on one bar, no tints, no gradients.
- Favicons, app icons and the avatar: the near-white mark on a full-bleed ink square at every size, square corners, no transparency.

**Smallest size** (judged from Quick Look renders only): the mark alone 16 px; the lockup 14 px cap height (about 20 px type and 166 px wide); the stacked version 8 px cap height, which makes the mark 32 px tall; the padded square mark 24 px (arithmetic, not seen). Do not go below these.

**Files** (all in `logo/`; `matrix.html` shows every one on white and on ink; `LOGO_RULES.md` has the full rules and measurements): `mark`, `mark_square`, `mark_on_ink`, `mark_square_on_ink`, `lockup`, `lockup_on_ink`, `mono_black`, `mono_white`, `lockup_mono_black`, `lockup_mono_white`, `stacked`, `stacked_on_ink`, `avatar` and `favicon` as SVG; favicons at 16, 32, 48, 180 (`apple-touch-icon.png`), 192 and 512 px as PNG; `avatar-512.png`; `favicon.ico`; and `build_logo_set.py`, which rebuilds the lockup, stacked and avatar files from the mark and a font file.

**Open decisions:**

1. **Wordmark font.** The pages set "Claude Daycare" as live monospace text (DM Mono 500 on Off Hours, IBM Plex Mono 600 on Inside the Lines). The logo lockup sets it as outlined Hanken Grotesk 700, a font that is used nowhere else. Once the team chooses a direction, either rebuild the lockup with that direction's wordmark font using `build_logo_set.py` (the recommended path, so the name looks the same everywhere), or keep the Hanken Grotesk lockup and use it as an image in headers instead of live text.
2. **The logo on the site's dark grounds.** The `_on_ink` files carry a `#1f1e1a` panel, which would show as a dark box on the ink-blue (`#0E1647`) and green-black (`#0B1F0F`) page grounds. On these pages use the white one-colour files (`mono_white.svg`, `lockup_mono_white.svg`) or the team decides to add a version drawn in the direction's `ink` token (its light text colour) with no panel. That would change the logo's four-colour rule, so it is a team decision.
3. **Not yet verified:** any favicon in a real browser tab (light or dark), on a phone home screen, in a profile crop or in print; and no look-alike or trademark search.
