# Plandit Style Guide

**Status:** Color, typography, logo direction, and production logo exports are complete. The first
landing page and mobile product screen should still be checked against this guide before the visual
system is treated as locked for product development.

**Purpose:** This guide defines Plandit's visual identity so landing pages, product screens, and
agent-generated work feel like the same product. Plandit should look confident, practical, and
ready to use: less like an inspiration board and more like the friend who has already made the
plan.

**Reference implementation:** Pending. The first full landing page and mobile product screen
should become the reference after the team reviews them at desktop and phone sizes.

---

## Visual Direction

Plandit uses a restrained two-color identity: emerald for action and black for structure.
Emerald suggests "go," forward movement, and staying on budget without using the low-quality
associations of the word "cheap." Black gives the product enough weight to feel reliable rather
than playful or disposable.

The visual system should feel:

- **Clean and decisive**, not decorative.
- **Energetic but controlled**, using emerald at moments of action.
- **Practical and credible**, with visible prices, time, distance, and route information.
- **Friendly but not childish**, using rounded details without cartoon styling.
- **Modern but not generic**, avoiding the blue-and-white default of many planning products.

### How the direction was chosen

The team first explored six three-color systems inspired by a clean primary, dark navy or black
base, and bold accent. Later rounds tested red, coral, orange, pink, and emerald variations. The
final round reduced the system to two colors so the logo and product would remain recognizable and
consistent.

The two-color finalists included jade/navy, teal/black, emerald/black, ocean/navy,
tangerine/navy, and red/navy. The team selected **emerald and black** because it was the clearest
combination of action, confidence, and distinctiveness.

---

## Color

| Token | Hex | Job |
|---|---|---|
| `emerald` | `#0FA968` | Primary brand color: logo field, major highlights, active states, large graphic moments, and primary buttons with dark text |
| `emerald-deep` | `#087A4B` | Accessible green for links, small controls, selected labels, and buttons that require white text |
| `ink` | `#0E0F12` | Primary text, navigation, dark backgrounds, secondary buttons, and the inverse logo field |
| `ink-muted` | `#5D626B` | Secondary copy, metadata, timestamps, distances, and helper text |
| `background` | `#F7F8FA` | Main light-mode page and app background |
| `surface` | `#FFFFFF` | Cards, sheets, inputs, and raised content areas |
| `border` | `#DDE2E8` | Dividers, input borders, card outlines, and inactive controls |
| `error` | `#C93434` | Errors, destructive actions, and unavailable states only |

### Contrast rules

- Use `ink` on `emerald` for button labels and ordinary text. The contrast is approximately
  **6.29:1**.
- White on `emerald` is approximately **3.05:1**. Reserve it for the large logo letter or large,
  bold display type. Do not use white for normal-size button labels on bright emerald.
- Use white on `emerald-deep` when a green control needs white text. The contrast is approximately
  **5.39:1**.
- `ink` on `background` is approximately **18.04:1**.
- `ink-muted` on `background` is approximately **5.77:1**.
- Emerald on black is approximately **6.29:1**, making it suitable for dark-mode accents and
  normal-size text.

### Color rules

- Emerald is the action color. Use it for the one decision or action that matters most in a view.
- Black provides structure. Navigation, headings, route lines, and high-emphasis information
  should usually be black before another color is introduced.
- Most screens should be primarily off-white, white, and black, with emerald occupying less
  visual area than the neutrals.
- Use `emerald-deep`, not bright emerald, for small green text on light backgrounds.
- Red is semantic, not decorative. Never use it as a general accent, because it must remain
  available for errors, cancellations, and unavailable plans.
- Never use a gradient in the interface. The official layered logo artwork is the only approved
  exception; do not recreate its tonal depth as a general UI effect.
- Do not introduce additional brand colors without team approval. Maps and third-party content may
  use necessary functional colors, but the surrounding interface remains emerald, black, and
  neutral.

---

## Type

Plandit uses **Manrope**, a geometric sans serif selected after comparing Inter, SF Pro, Roboto,
Segoe UI, Noto Sans, Arial/Helvetica Neue, Source Sans 3, IBM Plex Sans, Manrope, DM Sans, and
Public Sans.

Manrope was selected because it feels modern and friendly without becoming playful. Its open forms
remain readable in dense planning information, while its rounded geometry supports the simple
Plandit wordmark and icon direction.

- **Display and headings:** Manrope 700 or 800. Sentence case only. Use short, direct headings.
- **Body:** Manrope 400 or 500, 16–18px, line height 1.5–1.65, maximum measure 65ch.
- **Labels and controls:** Manrope 600, 14–16px. Avoid all caps.
- **Metadata:** Manrope 500, 13–14px. Use `ink-muted`, never low-opacity body text.
- **Wordmark:** `Plandit` in Manrope 700, capital P with the remaining letters lowercase. Never
  write `PlandIt`, `PLANdit`, or add a space. The name is pronounced like "planned it."

### Suggested type scale

| Role | Desktop | Mobile | Weight | Line height |
|---|---:|---:|---:|---:|
| Hero display | 56px | 40px | 800 | 1.05 |
| Page heading | 40px | 32px | 800 | 1.12 |
| Section heading | 30px | 26px | 700 | 1.2 |
| Card heading | 20px | 18px | 700 | 1.3 |
| Body large | 18px | 17px | 400–500 | 1.6 |
| Body | 16px | 16px | 400–500 | 1.55 |
| Label | 14px | 14px | 600 | 1.35 |
| Metadata | 13px | 13px | 500 | 1.4 |

Load Manrope from Google Fonts with weights 400, 500, 600, 700, and 800. Use
`system-ui, sans-serif` as the fallback stack.

---

## Space and Layout

- **Content width:** 1120px maximum for marketing pages; planning content may use a wider map
  layout when needed.
- **Page inset:** 24px on small screens, 32px on tablets, and 40px on desktop.
- **Section spacing:** 80px top and bottom on desktop; 56px on mobile.
- **Spacing scale:** 4, 8, 12, 16, 24, 32, 48, 64, and 80px.
- **Corner radius:** 12px for buttons and inputs; 16px for cards and panels; 20–24px only for
  large sheets or app-preview frames.
- **Grids:** One column below 720px. Two-column hero and content layouts above 720px. Three-column
  card grids only above 960px and only when each card remains easy to scan.
- **Planning screens:** On desktop, pair the plan timeline with a map. On mobile, prioritize the
  itinerary summary and use the map as a switchable view or sheet.

Group related information tightly. A place name should sit closer to its time, price, and travel
details than to the next stop. Do not spread small amounts of information across oversized cards.

---

## Components

### Buttons

- Minimum height: 48px; minimum tap target: 44 by 44px.
- Radius: 12px.
- Primary: `emerald` background, `ink` label, Manrope 600.
- Primary hover/pressed: darken toward `emerald-deep`; preserve a visible state change.
- Secondary: `ink` background with white text, or transparent with a 1px `ink` border.
- On dark backgrounds: emerald fill with `ink` text or white outline with white text.
- Destructive: `error` only when the action is genuinely destructive.
- Button copy uses a clear action: "Make my plan," "See the route," or "Share the plan." Avoid
  vague labels such as "Continue" when the next action can be named.

### Inputs and filters

- Inputs use white surfaces, 1px `border`, 12px radius, and a visible black or deep-emerald focus
  ring.
- Labels stay outside the field; placeholder text never replaces a label.
- Budget, distance, available time, and solo/group choices should be fast controls rather than
  open text fields when practical.
- Chips may be used for compact choices, but they must look interactive and show a clear selected
  state. Selected chips use a pale emerald treatment or black fill; do not make every label a
  pill.

### Cards

- Use white surfaces with a 1px `border`.
- Use shadows sparingly: one soft shadow level for floating sheets or a selected plan, not every
  card.
- Place cards prioritize decision information: time, total cost, distance, open status, and why
  the stop fits.
- Do not use a colored stripe on one side as decoration.

### Navigation and plan timeline

- Navigation is simple, with the mark/wordmark on the left and one primary action on the right.
- A plan timeline uses black for structure and emerald for the active or confirmed route.
- Stop numbers may use emerald circles with black numerals.
- Route status must not rely on color alone; pair color with text or an icon.

### Icons

- Use **Lucide** icons only, as inline SVG with `currentColor`.
- Default stroke width: 1.75; use 2 for small high-emphasis controls.
- Prefer literal utility icons: clock, wallet, map pin, walking, transit, share, users, and
  bookmark.
- Never mix icon libraries, use emoji as interface icons, or use sparkle/wand icons to represent
  AI.

### Lists and tables

- Use emerald dots or simple Lucide checks for short benefit lists.
- Planning lists should show sequence and timing, not generic bullets.
- Tables use full borders or clear row dividers, a light neutral header, and no zebra striping.

### Links

- Body links use `emerald-deep`, a 1px underline, and a 3px underline offset.
- Navigation links may use `ink` without an underline but need a visible hover and focus state.
- Standalone links and icon links must meet the 44px target floor.

---

## Imagery

### Photos

Use candid, natural-light photos of college-age people already doing something together or moving
through a real city environment. Useful searches include:

- Students comparing a plan on a phone before leaving.
- Friends meeting near campus, at a market, park, casual restaurant, gallery, or activity.
- A person confidently going somewhere alone.
- Close-ups of practical planning moments: a route, a shared link, a calendar, or a budget check.

Photos should feel observed rather than staged. Show a mix of solo and group situations. The
product is about making a day happen, not posing with a phone.

### Illustrations and motion

Use simple flat or lightly dimensional illustrations built from off-white, black, emerald, and
white. Illustrations should depict a real planning moment: saved places becoming an ordered route,
a group receiving a finished plan, or a nearby day organized around time and budget.

Motion should explain progress or sequence. A short route drawing or cards arranging into a plan
is appropriate. Decorative floating shapes and constant ambient motion are not.

### What to avoid

- Generic stock photos of people pointing at laptops.
- Glossy, obviously AI-generated people or city scenes.
- Travel clichés such as airplanes, suitcases, passports, or landmark collages.
- Decorative map pins scattered without meaning.
- Abstract blobs, neon gradients, glassmorphism, or fake 3D app icons.
- Images that imply luxury travel or expensive tourism.

### Alt text

Alt text tells the truth about the subject and how the image was made when relevant. Describe the
information the image contributes, not every decorative detail.

### Illustration prompt template

```text
Clean flat editorial illustration with rounded geometric forms and crisp edges. No border and no
decorative background shapes.
Palette: emerald #0FA968, deep emerald #087A4B, black #0E0F12, off-white #F7F8FA, and white.
Practical, energetic, and credible. Natural proportions and simple expressions. Avoid gradients,
photorealism, glossy 3D, generic AI imagery, sparkles, travel clichés, and text inside the image.

Scene: [A specific person or group turning saved places into a real plan]
Color emphasis: [Mostly off-white and black, with emerald marking the active route or action]
Composition: [Describe the shot, subject placement, and where open space is needed for page copy]
```

---

## Accessibility Floors

- Minimum 4.5:1 contrast for normal text and 3:1 for large text and interface boundaries.
- Visible keyboard focus on every interactive element.
- Minimum 44 by 44px tap targets.
- Semantic landmarks, logical heading order, and a skip link on web pages.
- Labels for every form field; errors explain how to fix the problem.
- Never rely on green, red, or any color alone to communicate status.
- Respect reduced-motion preferences and provide static alternatives.
- Maps require a text/list equivalent containing every stop and essential route detail.

---

## Never

- Gradients outside the approved logo artwork.
- Decorative blobs or floating shapes.
- Glassmorphism or excessive shadows.
- Blue as a substitute brand color.
- Red as a decorative accent.
- All-caps headings.
- Emoji as interface icons.
- Sparkles, magic wands, brains, or robot imagery for AI.
- Generic travel imagery or "hidden gem" visual clichés.
- Endless discovery feeds as the dominant interface.
- Tiny gray metadata that fails contrast.
- A different visual style for every generated screen.

---

## Logo

### Final direction

The selected mark is a bold, rounded **P** with layered tonal-emerald depth. The depth represents
**potential**: a saved intention becoming a real plan. The mark is based on the same soft,
geometric character as Manrope ExtraBold and remains recognizable without adding a separate map
pin, route, arrow, or calendar symbol.

The approved wordmark is `Plandit` in **Manrope ExtraBold 800**. In the standard color lockup,
`Pland` is black and the ending `it` is emerald, reinforcing that the name reads like
"planned it." On dark backgrounds, the main wordmark becomes white while the emerald accent
remains.

Approved configurations shown in `logo/logo-matrix.jpeg`:

- Layered emerald mark alone on a light background.
- Layered emerald mark alone on black.
- White `P` on an emerald rounded-square app icon.
- Emerald layered `P` on a white rounded-square app icon.
- Emerald layered `P` on a black rounded-square inverse icon.
- Horizontal lockups for light and dark backgrounds.
- Stacked wordmarks for light and dark backgrounds.
- One-color black and one-color white versions.
- Square social avatar.
- Favicon and platform-icon versions at the required sizes.

### Directions considered

The team explored literal planning symbols and more expressive marks, including an abstract plan
symbol, geometric fold, digital trace, dynamic curve, layered shield, infinite loop,
constellation P, sculptural relief, typographic block, and evolving ribbon. Earlier rejected
boards are retained in `logo/archive/`.

The final layered P was chosen because it is simpler, more legible, and more closely connected to
the Plandit name than marks that tried to communicate planning through several symbols at once.

### Logo rules

- The layered tonal treatment belongs only to the official supplied artwork. Do not approximate
  it with CSS gradients, shadows, bevels, or AI-generated replacements.
- Use the standard color mark on white or off-white and the inverse mark on black.
- Use only the approved emerald, black, and white versions.
- In the horizontal lockup, the square mark should be approximately the full height of the
  wordmark, vertically centered, with a gap of roughly one-quarter of the mark's width.
- Keep clear space on every side equal to at least one-quarter of the mark's width.
- Use the favicon-specific export below 24px. Use the regular standalone mark at 24px or larger.
- Do not use the horizontal lockup below approximately 120px wide; use the mark alone instead.
- Do not stretch, rotate, skew, outline, recolor, crop, or separate the layers of the mark.
- Do not place the logo over a busy image or any background that weakens contrast.
- The wordmark is always `Plandit`, never `PlandIt`, `PLANdit`, or `Plan It`.
- Monochrome contexts use the official one-color black or white file, not a desaturated color
  export.

### Files

The approved overview is `logo/logo-matrix.jpeg`. Exploration and rejected directions are stored
in `logo/archive/`.

The matrix is a visual reference. Use the following separate production exports:

- `mark.svg`
- `mark-square.svg`
- `mark-on-dark.svg`
- `mark-black.svg`
- `mark-white.svg`
- `lockup-light.svg`
- `lockup-dark.svg`
- `lockup-stacked-light.svg`
- `lockup-stacked-dark.svg`
- `avatar.svg`
- `favicon.svg`
- `favicon-16.png`
- `favicon-32.png`
- `favicon-48.png`
- `favicon-180.png`
- `favicon-192.png`
- `favicon-512.png`
- `favicon.ico` if required by the product stack

---

*When an implementation conflicts with this guide, use the guide unless a documented product or
accessibility requirement demands a change. Record approved changes here so future agents inherit
the same system.*
