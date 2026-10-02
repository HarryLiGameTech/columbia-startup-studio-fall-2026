# STYLE_GUIDE.md [Your Product Name]

**Purpose:** The visual identity for your product, so every page and screen looks like the same product. It is written for agents: hand it to a coding agent with your brand position, and the agent builds pages that look like yours instead of generic AI output. Update it as you build.

**Reference implementation:** [the page that shows this guide best, e.g., your landing page, once it exists]

See `resources/example_style-guide_stclair-ai.md` for a finished example.

---

## Color

<!-- Pick a primary accent first, then build around it. coolors.co helps.
     Give every color a job. If a color has no job, cut it. -->

| Token | Hex | Job |
|---|---|---|
| ink | #______ | Text and rules. Avoid pure black. |
| ink faint | #______ | Hints and meta lines. Check contrast. |
| background | #______ | Page ground |
| accent | #______ | The lead accent: primary buttons, the one saturated thing per screen |
| second color | #______ | [Its job] |
| tint | #______ | [Its job, e.g., code blocks, a section background] |
| error | #______ | Errors and alerts |

**Rules:** [e.g., one accent per element. Never a gradient.]

---

## Type

<!-- Two fonts at most. Google Fonts is the easiest source. -->

- **Headings:** [font and weights. Case rule, e.g., sentence case, no all caps.]
- **Body:** [font, size, line height, line length]
- **Wordmark:** [how your product name is set]

---

## Space and layout

- **Content width:** [e.g., 1024px]
- **Section spacing:** [e.g., 72px top and bottom]
- **Grids:** [when the layout goes from one column to two or three]

---

## Components

- **Buttons:** [shape, corner radius, minimum height. Primary and secondary styles.]
- **Icons:** [one library, e.g., Lucide. Stroke width. Never mix in icons from elsewhere or emoji.]
- **Cards:** [borders or fills, shadows or none]
- **Lists and tables:** [bullet style, table borders and header]
- **Links:** [color and underline]

---

## Imagery

- **Photos:** [Source: Pexels (pexels.com). Say what to search for, e.g., "real people cooking at home, natural light"]
- **Illustrations and video:** [Made in Gemini from the prompt template below. Say what style, e.g., "line drawings on white, one accent color"]
- **What to avoid:** [e.g., "Staged stock photos", "Generic AI art", "Anything that looks glossy and fake"]
- **Alt text:** tells the truth about the image, including how it was made.

### Illustration prompt template

<!-- Write this once and paste it at the top of every image prompt.
     Only the scene changes from image to image. -->

```
[Art style or medium]. [Composition rules, e.g., edge to edge, no borders].
Palette: [your hex codes from the Color section].
[Lighting and mood]. Avoid: [no photorealism, no stock look, etc.].

Scene: [what is happening, who, where]
Color emphasis: [which brand colors dominate]
Composition: [shot type, placement]
```

---

## Accessibility floors

4.5:1 text contrast, visible focus on every control, 44px tap targets, and real heading order.

---

## Never

[The things your product never does, e.g., gradients, stock people, emoji as icons, sparkles.]

---

## Logo

- **The mark:** [what it is and what it means]
- **Directions considered:** [two or three ideas you tried, and why you chose this one]
- **Files:** [where they live, e.g., brand/logo/. A square version and a favicon, a version on dark, and a one-color version.]
- **Rules:** [how it sits next to the wordmark, minimum size, colors it may and may not use]
