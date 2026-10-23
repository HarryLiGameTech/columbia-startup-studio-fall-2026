# Style round 3: notes

Two landing-page directions for **Claude Daycare**, each a refinement of its round 2 page. Claude chose them after Almog said "whatever you think" about round 2: Off Hours and Inside the Lines are carried forward, while Visit Slip and The Week are dropped. This file does not rank the two. They are listed in the order of the brief.

- Pages: `off-hours-r3.html`, `inside-the-lines-r3.html`, and `index.html`, which links to both.
- Scripts:
  - `check_contrast.py` computes the contrast table in section 5. Run it with `python3 -I check_contrast.py`, and add `--markdown` to get the tables.
  - `check_pages.py` checks well-formedness, structure and copy (section 6). Run it with `python3 -I check_pages.py`.
- The draft style guide built from these pages is `../../hw4-handin/style_guide.md`.
- Each page is one self-contained HTML file: inline CSS, no JavaScript, no images, no trackers. It opens by double-click. The only outside request is the Google Fonts stylesheet; without a connection the pages fall back to system fonts. `index.html` uses system fonts and makes no outside request.
- Round 1 and round 2 files are untouched.

---

## 1. What changed from round 2

### On both pages

| Change | Why |
|---|---|
| **The drawings now show how the runner behaves.** A visit is drawn as separate turns, the checks sit in the gaps between turns, and the last turn crosses the cap and finishes a little past it. Two homecoming turns follow in an `accent` outline (Off Hours) or a dashed `accent` line (Inside the Lines). | Round 2 drew a visit ending exactly at its cap. NOTES section 8 of round 2 and the repo study say the cap is checked between turns, the crossing turn finishes, and two homecoming turns run after the cap, unbounded by it. |
| **Copy rewritten to the honest-claims rule.** Both sublines and step 2 now say "checked between turns". Step 3 names the two homecoming turns, says they run after the cap, and mentions the usage line the command line prints today. Each figure's caption adds "The meter reads in whole percentage points" and "On OpenCode the allowance is a token cap, which can stop a turn in progress." | Section 2 lists each claim and its source. |
| **The concept label is now "Concept, not shipped"**, set in capitals by CSS, so the source text matches the brief. The protected work buffer is still the only unbuilt idea drawn. | The brief's wording. Round 2 used "CONCEPT — NOT SHIPPED". |
| **The footer is the brief's two sentences only.** The round 2 caveat about the cap moved into the drawings and the copy, where it is now shown rather than footnoted. | The brief. |
| **A secondary button, "How the cap is checked",** jumps to the drawing. | pear.no pairs a pale and a dark button. The guide needs a secondary style, and this one points at the part that states the limits. |
| **Button labels are tiny monospace capitals** (13px, 0.08em tracking), with the arrow in its own square cell. | pear.no. |
| **Order in the hero** is now label, headline, subline and buttons, then the drawing. | Off Hours round 2 put the drawing before the button, which pushed the button far down on a phone. |
| **Plus marks replaced by small open squares** (7px, 1px border) wherever frame lines meet. | pear.no uses four-point stars at crossings. The guide's Never list bans starburst, asterisk and radiating marks, and a plus or star at that size reads close to one. |
| **No load animation.** The only motion is a 3px nudge of the button arrow on hover, inside `prefers-reduced-motion: no-preference`. | Restraint. Also, static renderers caught round 2's animations mid-way, and a first round 3 draft showed the turns faded in a snapshot. |
| **Hero text and buttons sit side by side only from 1200px.** | At 900 to 1100px the two buttons squeezed the subline into a narrow column (seen in renders at 1024 and 1100px). |
| **Tokens share names** across the two pages (`ground`, `ground-2`, `ink`, `ink-faint`, `accent`, `line`, plus a few per direction). | The style guide can then give one table with a column per direction. |

### Off Hours (`off-hours-r3.html`)

- **Kept:** the ink-blue ground, the team's own line as the headline ("Let your Claude play without stealing your workweek."), Newsreader 300 headline, DM Mono labels, lamp-yellow accent, the moon and horizon glows, and the steps as a ruled list with large numerals.
- **New from pear.no:**
  - A thin frame: full-width 1px hairlines between the header, hero, drawing, steps and footer.
  - From 900px, vertical 1px lines at the content edges, with square nodes where the lines meet.
  - Mono capital section labels ("How the cap is checked", "The visit").
- **The drawing is new:**
  - A week strip (work so far, this visit, an unused dotted stretch, and the guardrail-rail work buffer labelled as a concept).
  - A zoom window around 40 to 50% with thin leader lines down to a detail strip.
  - The detail strip has a whole-point scale from 40 to 50% and five turns with a check in each gap. The cap is a line at 46%, and the fifth turn finishes past it, marked "Over". Two homecoming turns follow as outlined blocks.
  - The key under it has six entries, and each entry pairs a drawn mark with a sentence.
- **Copy:** the subline is now "Set an allowance before each visit. It is checked between turns, and your agent comes home once it has run out."
- **Removed:** the round 2 "This visit's allowance" end mark that implied an exact stop, and the visit bar's load animation.

### Inside the Lines (`inside-the-lines-r3.html`)

- **Kept:** the green-black ground, IBM Plex Mono headline, the ticked left rail with a rotated mono label, 1px frame lines, the playing field with a dashed allowance line and a hatched work buffer, the whistle-yellow accent and home marker.
- **New headline:** "Set the allowance first. Then let your agent play." Round 2's "Your agent plays inside it" implied the visit stays inside the cap, which it may not.
- **New subline:** "Before each visit you choose a weekly percentage or a token cap. It is checked between turns, so a visit can end a little over it."
- **The field drawing is new:**
  - The visit is a straight-segment path where each segment is one turn and each dot is a check.
  - The last segment crosses the allowance line.
  - Two dashed `accent` segments (homecoming) lead to the home marker, which uses Lucide `house` (the current name of the round 2 `home` icon, path re-read from Lucide's repository).
  - The legend has five entries: a turn, a check, the allowance line, homecoming, and the work buffer (labelled as a concept).
- **Quieter field:** `field` moved from #1C5A25 to #174A1F and `stripe` from #206830 to #1A5022, so the yellow is the one saturated thing. The secondary field markings (halfway line, centre circle, penalty box) are drawn in `ink-faint` at 1.5px instead of `ink` at reduced opacity.
- **Smaller changes:** step numbers moved from circles to 44px squares, which rhyme with the nodes and the 4px-radius buttons. The rail labels are numbered ("01 The pitch", "02 The plays").

### Not borrowed

- pear.no's full-screen film: there are no videos or images here.
- Resend's metallic letter shading.
- Cursor's painterly landscape. Off Hours' blurred SVG glows are the nearest thing.
- The Week's week-of-bars chart: the brief allowed it, but the Off Hours week strip already does that job in one bar, so it was not added.

---

## 2. Copy against the honest-claims rule

Facts come from the vault note "Background/Claude Daycare repo — how the allowance works today" (a read of the runner code at commit 97424e9; nothing there was run) and round 2's NOTES section 8.

| Statement on the pages | Status | Source |
|---|---|---|
| You set a weekly percentage (Claude Code, Codex) or a token cap (OpenCode) before a visit | Today | Repo study 3.1; site, per round 2 |
| The allowance is checked between turns, never during one; the crossing turn finishes, so a visit can end a little over | Today | Repo study 3.3 (`Ledger::should_end`) |
| On OpenCode the token cap can stop a turn in progress | Today | Repo study 3.3 (`run_turn`) |
| Two homecoming turns: one can save memories (the private account), one writes the day report; they run after the cap and are not bounded by it | Today | Repo study 4.2 |
| The command line prints about how much weekly usage moved while the visit ran | Today (local only) | Repo study 6 (`weekly_usage_line`) |
| The meter reads in whole percentage points | Today, at best | Repo study 1 and 2.1 |
| Plays with Daycare's own tools only | Site wording, carried from round 2 | Not re-checked this round |
| Works with Claude Code, Codex CLI and OpenCode | Site wording, carried from round 2 | Not re-checked this round |
| Work buffer: "the last 30% of the week, held back for work" | **Concept, not shipped**, labelled on both pages | Repo study 6 |

Not drawn or mentioned at all: an itemized receipt, a preview before a visit, live progress on the site, and an automatic pause. The Off Hours headline is the team's own tagline. It promises an outcome ("without stealing your workweek") that the protected buffer would back, and that buffer is not built. The page's own sentences stay literal. **The team should decide whether the tagline stays while the buffer is a concept** (the brand position draft holds back the "protect work usage" half for the same reason).

---

## 3. Palettes

Token names are shared where the job is shared. Every colour that carries text or meaning is checked in section 5.

### Off Hours

| Token | Hex | Job |
|---|---|---|
| `--ground` | #0E1647 | Page and hero ground; label and arrow on the pale primary button; the halo around the cap line; label backgrounds inside the drawing |
| `--ground-2` | #090F34 | Steps band and footer |
| `--ink` | #EEF0F8 | Headline, body text, wordmark, primary button fill, secondary button border and label, drawing lines (work line, guardrail rails and posts, cap line, checks, "over" bracket). Also a literal in the guardrail-posts pattern |
| `--ink-faint` | #AEB7E0 | Labels, scale numbers and ticks, key text, caption, step text, footer text, zoom window, leader lines, detail frame, square nodes |
| `--accent` | #F2C14E | Turn blocks, homecoming outlines, the week's visit bar, step numerals, concept tag, focus ring, link underline, button hover, skip link; the moon glow at 12% |
| `--line` | #323E86 | Decorative 1px frame hairlines and step dividers |
| `--dots` | #8D97CC | The dotted unused stretch in the drawing |
| `--glow` | #3A4BC0 | Backdrop only: the horizon glow at 50% |

### Inside the Lines

| Token | Hex | Job |
|---|---|---|
| `--ground` | #0B1F0F | Page ground (green-black) |
| `--ground-2` | #0E2813 | Steps band and footer |
| `--field` | #174A1F | The playing field |
| `--stripe` | #1A5022 | Mowing stripes on the field |
| `--ink` | #EAF3E3 | Headline, body text, wordmark, secondary button, field boundary, turn lines and check dots, allowance line, buffer edge, step number squares |
| `--ink-faint` | #B5CFAC | Labels, rail label, legend text, caption, step text, hatching in the work buffer, secondary field markings, square nodes; also a literal in the rail-tick patterns |
| `--line` | #2F5233 | Decorative 1px frame lines, rail border, step cell borders |
| `--accent` | #F5D547 | Primary button fill, homecoming lines, hollow dot and home marker, concept tag, focus ring, link underline, skip link |
| `--accent-ink` | #14290E | Label, arrow and house icon on the accent |

### Index (`index.html`)

These are the same tokens as round 2's index: `--bg` #FAF8F4 (page), `--card` #FFFFFF (cards), `--ink` #1B1B1B (text, focus ring, tag border), `--ink-2` #55524C (secondary text), `--link` #0B57D0 (links), `--rule` #6F6A60 (card and footer borders). The swatches on each card are decorative copies of that direction's ground and accents.

### Style guide only

`error` #FF9B8F, for error text on either ground. Not on a page yet; it is checked in section 5.

---

## 4. Fonts and icons, with licences

| Family | Page | Weights loaded | Used for | Specimen | Licence file |
|---|---|---|---|---|---|
| Newsreader | Off Hours | wght 300 to 500, opsz 6 to 72 | Headline (300), body (400), step headings (500), section heading and drawing heading (300) | https://fonts.google.com/specimen/Newsreader | https://github.com/google/fonts/blob/main/ofl/newsreader/OFL.txt |
| DM Mono | Off Hours | 400, 500 | Wordmark, labels, buttons, tag, drawing labels, scale, footer | https://fonts.google.com/specimen/DM+Mono | https://github.com/google/fonts/blob/main/ofl/dmmono/OFL.txt |
| IBM Plex Mono | Inside the Lines | 400, 500, 600 | Headline and headings (500), wordmark (600), labels, buttons, tag, caption, footer | https://fonts.google.com/specimen/IBM+Plex+Mono | https://github.com/google/fonts/blob/main/ofl/ibmplexmono/OFL.txt |
| IBM Plex Sans | Inside the Lines | wght 400 to 600 | Subline, body, legend and step text | https://fonts.google.com/specimen/IBM+Plex+Sans | https://github.com/google/fonts/blob/main/ofl/ibmplexsans/OFL.txt |

**How the licences were verified (2026-10-09, from the sources, not from memory):**

- For each family, `OFL.txt` and `METADATA.pb` were fetched from `raw.githubusercontent.com/google/fonts/main/ofl/<family>/` with curl, as plain text into a scratch folder.
- Each `OFL.txt` reads "SIL OPEN FONT LICENSE Version 1.1 - 26 February 2007", and each `METADATA.pb` has `license: "OFL"`.
- The copyright lines are: Newsreader, 2020 The Newsreader Project Authors (designer Production Type). DM Mono, 2020 The DM Mono Project Authors (Colophon Foundry). IBM Plex Mono and IBM Plex Sans, 2017 IBM Corp., with the **Reserved Font Name "Plex"**, so a modified or subset copy must not be called Plex.
- The axes and weights in `METADATA.pb` cover what the pages request: Newsreader wght 200 to 800 and opsz 6 to 72; DM Mono static 300, 400 and 500; IBM Plex Mono static 100 to 700; IBM Plex Sans wght 100 to 700.
- Both Google Fonts stylesheet URLs answered HTTP 200 with `text/css`.
- In the browser pane, `document.fonts` reported every requested family and weight as loaded.

**Icons:**

- Lucide `arrow-down` (both pages, buttons) and Lucide `house` (Inside the Lines, home marker).
- On 2026-10-09 the icon SVGs, their JSON metadata and the `LICENSE` file were fetched from `raw.githubusercontent.com/lucide-icons/lucide/main/`, and the paths in the pages are copied from them.
- The `LICENSE` file is ISC, "Copyright (c) 2026 Lucide Icons and Contributors". It also lists the icons derived from Feather, which are additionally under the MIT License, "Copyright (c) 2013-present Cole Bemis".
- `arrow-down` is on that Feather list; `house` is not. Each page's head comment carries the matching notices.

Everything else is hand-written CSS or inline SVG: the frame lines, square nodes, rail ticks, backdrop glows, guardrail rails, the usage strips, the field, the hatching and the path. No paid kit, template or stock asset is used.

---

## 5. Contrast

`check_contrast.py` reads each page's `:root` colour tokens, so the numbers follow the files. For every kind of text and every mark that carries meaning, it computes the WCAG 2.x ratio (L1 + 0.05) / (L2 + 0.05) from WCAG relative luminance. Ratios are rounded down to two decimals, so a displayed pass is a real pass.

Thresholds:

- **body:** 4.5:1, for text under 24px regular or 18.66px bold.
- **large:** 3:1, for text at or above those sizes.
- **ui:** 3:1, for marks that carry meaning (WCAG 1.4.11).
- **decor:** listed with no threshold. These are purely decorative hairlines, the backdrop and the stripes; something else always carries the meaning.

Off Hours text that sits over a glow is checked against the glow composited at its opacity over the ground. These are worst cases, because the blur lowers the real peak.

**Result: 67 pairs checked, 0 under their threshold, 0 colour tokens left without a pair.** The lowest body-text pair is 5.79:1 (Off Hours `ink-faint` over the horizon glow).

| Page | Pairs | Lowest body | Lowest large | Lowest ui |
|---|---|---|---|---|
| off-hours-r3.html | 27 | 5.79:1 | 11.07:1 | 6.06:1 |
| inside-the-lines-r3.html | 25 | 9.37:1 | 13.83:1 | 5.63:1 |
| index.html | 11 | 6.02:1 | 16.23:1 | 5.06:1 |
| style guide only | 4 | 7.76:1 | none | none |

#### off-hours-r3.html

| Foreground | Background | Where | Role | Ratio | Needs | Result |
|---|---|---|---|---|---|---|
| --ink #EEF0F8 | --ground #0E1647 | Headline (h1, 48-132px); drawing heading (28-40px) | large | 15.07:1 | 3.0:1 | pass |
| --ink #EEF0F8 | --ground #0E1647 | Wordmark, header link, key names, labels inside the drawing | body | 15.07:1 | 4.5:1 | pass |
| --ink-faint #AEB7E0 | --ground #0E1647 | Feature label, drawing label, scale numbers, key text, caption | body | 8.69:1 | 4.5:1 | pass |
| --ink #EEF0F8 | --accent at 12% over --ground = #292B48 | Headline where the moon glow sits behind it | large | 12.08:1 | 3.0:1 | pass |
| --ink-faint #AEB7E0 | --accent at 12% over --ground = #292B48 | Feature label near the moon glow | body | 6.97:1 | 4.5:1 | pass |
| --ink #EEF0F8 | --glow at 50% over --ground = #243084 | Subline and secondary button label over the horizon glow | body | 10.04:1 | 4.5:1 | pass |
| --ink-faint #AEB7E0 | --glow at 50% over --ground = #243084 | 'Works with' line over the horizon glow | body | 5.79:1 | 4.5:1 | pass |
| --accent #F2C14E | --glow at 50% over --ground = #243084 | Secondary button label on hover, over the horizon glow | body | 6.81:1 | 4.5:1 | pass |
| --ground #0E1647 | --ink #EEF0F8 | Primary button label | body | 15.07:1 | 4.5:1 | pass |
| --ground #0E1647 | --accent #F2C14E | Primary button label on hover, skip-link label | body | 10.21:1 | 4.5:1 | pass |
| --accent #F2C14E | --ground #0E1647 | 'Concept, not shipped' tag text and border | body | 10.21:1 | 4.5:1 | pass |
| --ink #EEF0F8 | --ground-2 #090F34 | Section heading (h2, 36-64px), step headings (24px) | large | 16.33:1 | 3.0:1 | pass |
| --ink #EEF0F8 | --ground-2 #090F34 | Footer link | body | 16.33:1 | 4.5:1 | pass |
| --ink-faint #AEB7E0 | --ground-2 #090F34 | Section label, step text, footer text | body | 9.42:1 | 4.5:1 | pass |
| --accent #F2C14E | --ground-2 #090F34 | Step numerals (52px) | large | 11.07:1 | 3.0:1 | pass |
| --ink #EEF0F8 | --ground #0E1647 | Drawing: work line, guardrail rails and posts, cap line, checks, 'over' bracket | ui | 15.07:1 | 3.0:1 | pass |
| --ink-faint #AEB7E0 | --ground #0E1647 | Drawing: scale ticks, zoom window, leader lines, detail frame; square nodes | ui | 8.69:1 | 3.0:1 | pass |
| --accent #F2C14E | --ground #0E1647 | Drawing: turn blocks, homecoming outlines, visit bar; focus ring | ui | 10.21:1 | 3.0:1 | pass |
| --dots #8D97CC | --ground #0E1647 | Drawing: dotted unused stretch | ui | 6.06:1 | 3.0:1 | pass |
| --ink #EEF0F8 | --glow at 50% over --ground = #243084 | Secondary button border over the horizon glow | ui | 10.04:1 | 3.0:1 | pass |
| --accent #F2C14E | --glow at 50% over --ground = #243084 | Focus ring over the horizon glow | ui | 6.81:1 | 3.0:1 | pass |
| --ground #0E1647 | --ink #EEF0F8 | Primary button arrow and its divider | ui | 15.07:1 | 3.0:1 | pass |
| --accent #F2C14E | --ground-2 #090F34 | Focus ring on the steps band and footer | ui | 11.07:1 | 3.0:1 | pass |
| --ink-faint #AEB7E0 | --ground-2 #090F34 | Square nodes on the steps band and footer | ui | 9.42:1 | 3.0:1 | pass |
| --line #323E86 | --ground #0E1647 | 1px frame hairlines | decor | 1.77:1 | none | decor, no threshold |
| --line #323E86 | --ground-2 #090F34 | 1px frame hairlines and step dividers on the steps band | decor | 1.92:1 | none | decor, no threshold |
| --glow #3A4BC0 | --ground #0E1647 | Backdrop: horizon glow against the ground | decor | 2.40:1 | none | decor, no threshold |

The cap line crosses the yellow fifth turn. It is drawn in `ink` with a 2px `ground` halo, so its contrast is `ink` on `ground` (15.07:1) rather than `ink` on `accent`.

#### inside-the-lines-r3.html

| Foreground | Background | Where | Role | Ratio | Needs | Result |
|---|---|---|---|---|---|---|
| --ink #EAF3E3 | --ground #0B1F0F | Headline (h1, 32-72px) | large | 15.14:1 | 3.0:1 | pass |
| --ink #EAF3E3 | --ground #0B1F0F | Wordmark, header link, subline, drawing heading, legend names, secondary button label | body | 15.14:1 | 4.5:1 | pass |
| --ink-faint #B5CFAC | --ground #0B1F0F | Feature label, rail label, drawing label, 'works with' line, legend text, caption | body | 10.25:1 | 4.5:1 | pass |
| --accent #F5D547 | --ground #0B1F0F | 'Concept, not shipped' tag text and border; secondary button label on hover | body | 11.90:1 | 4.5:1 | pass |
| --accent-ink #14290E | --accent #F5D547 | Primary button label, skip-link label | body | 10.70:1 | 4.5:1 | pass |
| --accent-ink #14290E | --ink #EAF3E3 | Primary button label on hover | body | 13.61:1 | 4.5:1 | pass |
| --ink #EAF3E3 | --ground-2 #0E2813 | Section heading (h2, 28-44px) | large | 13.83:1 | 3.0:1 | pass |
| --ink #EAF3E3 | --ground-2 #0E2813 | Step headings (20px), step numbers, footer link | body | 13.83:1 | 4.5:1 | pass |
| --ink-faint #B5CFAC | --ground-2 #0E2813 | Section label, step text, rail label, footer text | body | 9.37:1 | 4.5:1 | pass |
| --ink #EAF3E3 | --field #174A1F | Field: boundary, turn lines, check dots, allowance line, buffer edge | ui | 9.05:1 | 3.0:1 | pass |
| --ink #EAF3E3 | --stripe #1A5022 | Same marks over a mowing stripe | ui | 8.32:1 | 3.0:1 | pass |
| --ink-faint #B5CFAC | --field #174A1F | Field: hatching in the work buffer | ui | 6.13:1 | 3.0:1 | pass |
| --ink-faint #B5CFAC | --stripe #1A5022 | Hatching over a mowing stripe | ui | 5.63:1 | 3.0:1 | pass |
| --accent #F5D547 | --field #174A1F | Field: homecoming lines, hollow dot, home marker | ui | 7.11:1 | 3.0:1 | pass |
| --accent #F5D547 | --stripe #1A5022 | Homecoming marks over a mowing stripe | ui | 6.54:1 | 3.0:1 | pass |
| --accent-ink #14290E | --accent #F5D547 | House icon in the home marker; primary button arrow and divider | ui | 10.70:1 | 3.0:1 | pass |
| --ink #EAF3E3 | --ground #0B1F0F | Legend swatches; secondary button border | ui | 15.14:1 | 3.0:1 | pass |
| --accent #F5D547 | --ground #0B1F0F | Legend homecoming swatch; focus ring on the main ground | ui | 11.90:1 | 3.0:1 | pass |
| --ink #EAF3E3 | --ground-2 #0E2813 | Step number squares | ui | 13.83:1 | 3.0:1 | pass |
| --accent #F5D547 | --ground-2 #0E2813 | Focus ring on the steps band and footer | ui | 10.88:1 | 3.0:1 | pass |
| --ink-faint #B5CFAC | --ground #0B1F0F | Square nodes and rail ticks | decor | 10.25:1 | none | decor, no threshold |
| --line #2F5233 | --ground #0B1F0F | 1px frame lines and rail border | decor | 1.95:1 | none | decor, no threshold |
| --line #2F5233 | --ground-2 #0E2813 | 1px frame lines and step cell borders on the steps band | decor | 1.78:1 | none | decor, no threshold |
| --field #174A1F | --ground #0B1F0F | Field against the page (the 2px boundary line carries the shape) | decor | 1.67:1 | none | decor, no threshold |
| --stripe #1A5022 | --field #174A1F | Mowing stripes against the field | decor | 1.08:1 | none | decor, no threshold |

#### index.html

| Foreground | Background | Where | Role | Ratio | Needs | Result |
|---|---|---|---|---|---|---|
| --ink #1B1B1B | --bg #FAF8F4 | Heading (h1, 30-44px) | large | 16.23:1 | 3.0:1 | pass |
| --ink #1B1B1B | --bg #FAF8F4 | Wordmark | body | 16.23:1 | 4.5:1 | pass |
| --ink-2 #55524C | --bg #FAF8F4 | Intro, note, footer text | body | 7.33:1 | 4.5:1 | pass |
| --bg #FAF8F4 | --ink #1B1B1B | Skip-link label | body | 16.23:1 | 4.5:1 | pass |
| --ink #1B1B1B | --card #FFFFFF | Card text | body | 17.22:1 | 4.5:1 | pass |
| --ink-2 #55524C | --card #FFFFFF | Card descriptions and 'refined from' labels | body | 7.78:1 | 4.5:1 | pass |
| --link #0B57D0 | --card #FFFFFF | Direction names (links) | body | 6.38:1 | 4.5:1 | pass |
| --link #0B57D0 | --bg #FAF8F4 | NOTES.md and style guide links | body | 6.02:1 | 4.5:1 | pass |
| --ink #1B1B1B | --bg #FAF8F4 | Concept tag border; focus ring | ui | 16.23:1 | 3.0:1 | pass |
| --rule #6F6A60 | --card #FFFFFF | Card border | ui | 5.37:1 | 3.0:1 | pass |
| --rule #6F6A60 | --bg #FAF8F4 | Footer rule, swatch borders | ui | 5.06:1 | 3.0:1 | pass |

#### Style guide only (not on a page yet)

| Foreground | Background | Where | Role | Ratio | Needs | Result |
|---|---|---|---|---|---|---|
| #FF9B8F | #0E1647 | Error text on the Off Hours ground (style guide token 'error') | body | 8.44:1 | 4.5:1 | pass |
| #FF9B8F | #090F34 | Error text on the Off Hours band | body | 9.15:1 | 4.5:1 | pass |
| #FF9B8F | #0B1F0F | Error text on the Inside the Lines ground | body | 8.49:1 | 4.5:1 | pass |
| #FF9B8F | #0E2813 | Error text on the Inside the Lines band | body | 7.76:1 | 4.5:1 | pass |

---

## 6. Checks that ran, and what was seen

| Check | How it ran | Result |
|---|---|---|
| Contrast | `python3 -I check_contrast.py` | 67 pairs, 0 under threshold, 0 unused tokens (section 5) |
| Well-formedness and structure | `python3 -I check_pages.py`, standard-library `html.parser` | All three pages pass (details below) |
| Parser sanity | The same parser fed three broken snippets (a misnested tag, an unclosed element, a closed void element) | All three were caught |
| Browser, phone widths | Folder served with `python3 -I -m http.server --bind 127.0.0.1 8763`, viewed in the built-in browser pane at 375 and 320px, and Off Hours also at 640px. The server was stopped afterwards | See below |
| Renders | Headless Chrome screenshots at 1024, 1280 and 1440px, and at 375px through a 375px iframe (Chrome would not make a window that narrow); macOS Quick Look (`qlmanage -t -s 1100`) of all three files, opened as plain files | See below |

`check_pages.py` checks:

- Every non-void element is closed in order; there are no duplicate ids.
- Every `#anchor`, `aria-labelledby` and local link resolves.
- `lang`, charset, viewport and title are present.
- Exactly one h1, with no skipped heading level.
- No `<script>`, no `<img>` or other embedded media, no `src`, no CSS `url()` other than inline SVG, and no outside resource other than Google Fonts.
- No more than two font families.
- A `:focus-visible` rule and a reduced-motion rule are present.
- A 44px minimum on the skip link, nav links and buttons.
- The footer disclaimer is present.
- On the direction pages: the three step titles, "checked between turns", "Concept, not shipped" and "not bounded by" are present, and "Numbers are illustrative." appears exactly once.
- None of a list of overclaiming, ranking, filler and "add-on" phrases.
- No emoji, star, sparkle or asterisk glyph in the page text.

**In the browser pane:**

- **No horizontal scroll.** At 375 and 320px (and Off Hours at 640px) the scroll width equalled the viewport width. The only elements outside the viewport were the two blurred backdrop ellipses, which their SVG clips. At 375px the text runs from x = 16 to x = 359, so the 16px gutter holds.
- **Tap targets.** The skip link, header link, both buttons and the footer link measured 158x44, 109x44, 231x52, 284x52 and 201x44 on both pages at 375px, and the same on Inside the Lines at 320px. Off Hours at 320px was checked for overflow and label overlap only.
- **Overlap.** At 320 and 640px no label inside the Off Hours drawing overlapped another.
- **Keyboard.** On Off Hours, Tab visits the skip link, the header link, both buttons and the footer link, in that order. Each matched `:focus-visible` and drew a 2px solid outline in the accent colour (rgb 242, 193, 78).
- **Computed colours.** A script read the rendered colour of every text element and its nearest solid background: 49 elements on Off Hours and 39 on Inside the Lines at 375px. None was under its threshold; the lowest body pairs were 8.70 and 9.38. Glows are not visible to this check and are covered by the compositing in section 5. The smallest rendered text was 12px.
- **Fonts.** The pane reported DM Mono 400 and 500, Newsreader 300 to 500, IBM Plex Mono 400, 500 and 600, and IBM Plex Sans 400 to 600 as loaded.
- **The pane was shared.** During the session another task navigated the same browser tab to its own page. Measurements stopped there, and the desktop widths were judged from headless Chrome renders instead.

**Bugs found by looking, and fixed:**

1. Off Hours: the square nodes on the steps band and footer floated 64px below their hairline on a phone, because the padding was on the band, not the inner wrap.
2. Off Hours: the first key mark showed one turn block instead of two (an `nth-child` selector counted the wrong element).
3. Off Hours: a centred figure lost its centring because `margin: 0` overrode the wrap's auto margins.
4. Off Hours: the in-drawing labels first sat where the leader lines cross them. They now sit inside the detail frame on a solid label background.
5. Inside the Lines: legend entries in the same row started at different heights (grid rows stretched). They now align to the top.
6. Both: from 900 to 1100px the buttons squeezed the subline into a narrow column, and the concept tag wrapped onto two lines in a five-column legend. The two-column hero now starts at 1200px, the legend has three columns from 900px and five from 1200px, and the tag never wraps.
7. Both: the first turn animation looked faded in static renders and was removed, along with the home-marker animation.

Renders and snapshots are in the session scratchpad folders `r3-renders/` and `r3-ql/`, not in this repo.

---

## 7. Not verified

- **Other browsers and real devices.** Only Chromium (the pane and headless Chrome) and Quick Look's WebKit snapshot were used. Not tried: Safari, Firefox, and real iOS and Android phones. Worth checking there: `text-wrap: balance` and `pretty`, Newsreader's optical-size axis, `writing-mode` on the rotated rail label, and `vector-effect` on the leader lines.
- **Desktop widths in a live browser.** The 1024, 1280 and 1440px checks are renders that were looked at. Overflow and tap targets were measured live only at 320, 375 and 640px, because the shared pane tab was taken over mid-session.
- **Keyboard on Inside the Lines.** The tab order was not stepped through live; it has the same five controls in the same order as Off Hours.
- **Screen readers.** VoiceOver, NVDA and TalkBack were not run. The drawings are `aria-hidden` with text keys, the figures are named through `aria-labelledby`, and the rail labels are `aria-hidden`, but how they are announced was not heard.
- **Reduced motion.** The setting was not switched on and checked. Only the arrow nudge is affected.
- **Zoom, forced colours, print.** Not checked: 200% zoom, text-only resizing, Windows High Contrast or forced colours (the drawings use token colours and may not adapt), and print.
- **Text over the glows.** Checked by compositing, not by sampling pixels from a render.
- **Product claims.** The facts come from the repo study, which read code and ran nothing, and from round 2's NOTES section 8. Not re-checked this round: the site wording ("Daycare's own tools only", "Works with Claude Code, Codex CLI and OpenCode") and how large a crossing turn or the homecoming turns really are. The drawn sizes (about 0.6 points over, about 2 points of homecoming) are illustrative only.
- **The tagline.** Whether "without stealing your workweek" is acceptable while the work buffer is a concept is a team decision (section 2).
- **Licences.** These were read from the files in the google/fonts and lucide-icons repositories on 2026-10-09; they are not legal advice. Google Fonts' own terms of service for the hosted API were not read.
- **Audience.** No one outside the team has seen these pages.

## 8. Privacy note

The two direction pages load their fonts from Google Fonts. Each visit sends the visitor's IP address and the usual request headers to Google. There are no analytics, no scripts and no cookies set by these pages. For a production site, self-host the same font files (the OFL allows it; a modified or subset copy of Plex must be renamed), keep the licence text next to them, and drop the two `preconnect` lines and the stylesheet link. `index.html` makes no outside request.
