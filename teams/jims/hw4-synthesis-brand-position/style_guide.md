# STYLE\_GUIDE.md — SettleWise

**Team:** Team Jims  
**Product:** SettleWise  
**Tagline:** Know before you settle.  
**Purpose:** This is SettleWise's visual identity and implementation guide. Give it to a designer or coding agent alongside the brand-position document so every screen feels like the same product. Update the guide when the team approves a design change.  
**Reference implementation:** The selected *Neighborhood Notebook* landing-page direction (Round 3, Design A), as refined through the team's typography, color, and logo feedback. The landing page is a visual reference, not an additional deliverable for this style-guide assignment.

## Brand direction

**Brand promise:** Apartment hunting is stressful enough. Understanding your options and choosing a place to live should not have to be.

SettleWise is an NYC apartment **decision-support** experience. It helps renters organize apartment options, compare details against their own priorities, understand trade-offs, and see unanswered questions. It does not make the decision for them or promise that a listing is verified, safe, or complete. The design should feel **warm, cozy, friendly, lightly playful, trustworthy, and organized**. It can be cute in small details, but never childish, busy, or overly technical. The audience is NYC renters broadly; students and first-time renters are useful examples, not the only intended users.

**Brand principles:** Clarity over complexity; relief over pressure; honesty over false certainty; personal choice over prescribed answers.

**Writing voice:** Plain English, short sentences, calm and practical. Prefer “Compare what matters to you,” “Understand the trade-offs,” and “See what's missing.” Do not say that SettleWise finds the objectively best apartment. Use the approved tagline **“Know before you settle.”**

---

## Color

Every color has a specific job. Use these exact brand HEX values; do not sample slightly different colors from generated preview images.

| Token | Hex | Job |
| :---- | :---- | :---- |
| `background` / `cream` | `#FFF8EE` | Default page background, warm negative space, light logo path |
| `ink` / `deep-green` | `#34443A` | Main text, headings, primary-button background, dark sections |
| `sage` | `#739282` | Primary logo marker, supporting illustrations, larger decorative surfaces |
| `accent` / `terracotta` | `#BD6248` | Selective emphasis, primary logo destination dot, dark-treatment logo marker |
| `tint` / `peach` | `#F7E1CF` | Soft section and card fills, subtle illustrations |
| `surface` / `white` | `#FFFFFF` | Card surfaces and optional neutral UI backgrounds |
| `error` | **Not yet approved** | Use a clearly labeled, accessible error treatment during implementation; do not invent an “official” brand error HEX without team approval |

&nbsp;

**Rules:** The site should read as mostly cream and deep green, supported by sage and small terracotta accents. Peach adds warmth without competing with content. Prefer deep-green text on cream or white; do not assume sage or terracotta text on cream passes accessibility contrast. Test every text/background combination. Use flat color in the logo: **no gradients, textures, shadows, or approximate hues**. Avoid blue, purple, neon colors, and cool gray-green variations that appeared in rejected generations. A decorative surface must never reduce text readability.

### Approved logo color mapping

| Logo part | Primary / light treatment | Dark-background treatment |
| :---- | :---- | :---- |
| Preview background | Cream `#FFF8EE` | Deep green `#34443A` |
| Location marker | Sage `#739282` | Terracotta `#BD6248` |
| Winding path | Cream `#FFF8EE` | Cream `#FFF8EE` |
| Destination dot | Terracotta `#BD6248` | Sage `#739282` |
| Wordmark | Deep green `#34443A` | Cream `#FFF8EE` |

&nbsp;

The winding path must connect directly to the dot. **Never place a white or cream ring, outline, halo, or separate background around the dot.** This applies to both treatments. The dark treatment must use the **terracotta marker and sage dot**, not a dark-green marker or white marker.

---

## Type

- **Headings:** **Plus Jakarta Sans**, weight 600–700. Use sentence case, clear hierarchy, and a welcoming rather than corporate tone. No decorative serif font: the Fraunces direction was considered and rejected as too fancy.  
- **Body:** Plus Jakarta Sans, weight 400–500; default **16–18px** with about **1.5–1.65 line height**. Aim for approximately 60–70 characters per line for long paragraphs. Prefer readable, direct copy rather than dense blocks.  
- **Wordmark:** **SettleWise**, with **“Settle” lighter (approximately 500\)** and **“Wise” bolder (approximately 700\)**. Preserve the provided vector wordmark artwork when using the approved logo files; do not recreate it with a different font.  
- **Suggested responsive scale:** Desktop display 56–68px, H1 around 48px, H2 around 36px, H3 around 24px, body 16–18px, captions 13–14px. Mobile H1 around 36–42px, H2 around 28px. Adjust for actual content and accessibility rather than forcing fixed sizes.  
- **Fallback:** `sans-serif` only if Plus Jakarta Sans is unavailable for live interface text. The final logo artwork should remain the approved vector asset.

Use one type family consistently. Strong typography and whitespace should do most of the visual work.

---

## Space and layout

- **Content width:** Maximum **1160–1200px**, centered. Desktop side gutters about **24px**, mobile about **20px**.  
- **Spacing system:** Use increments from **4, 8, 12, 16, 24, 32, 48, 64, 96px**. Typical card padding **16–24px**.  
- **Section spacing:** About **64–96px** vertically on desktop and **48–64px** on mobile.  
- **Grids:** Responsive 12-column structure when useful; commonly two or three content cards on desktop, two on medium screens, and **one column on small screens**. Do not cram comparison details into tiny columns.  
- **Shapes:** Rounded but not bubbly. Use roughly **18–24px** radii on cards, **12px** on inputs, and pill shapes for chips or selected buttons.  
- **Visual rhythm:** Generous cream whitespace, soft cards, clear sections, balanced asymmetry, and restrained NYC details. Information should be revealed gradually and be easy to scan.

The selected direction is **Neighborhood Notebook**, specifically **Round 3, Design A**. Keep its cozy, organized character. Inspiration included Headspace's warmth, Airbnb's navigational clarity, and Notion's polish; **do not copy** any of their distinctive visual identities. Avoid Linear-like technical severity and Zillow-like clutter.

---

## Components

- **Buttons:** Primary buttons use deep green `#34443A` with cream `#FFF8EE` text, a rounded pill shape, clear action wording, and at least **44px** height and practical 44×44px targets. Secondary buttons use a cream or transparent surface with a deep-green border and label. Provide hover, keyboard focus, disabled, and active states; do not rely on color alone.  
- **Icons:** Use a single consistent set of **simple, rounded line icons**. **Lucide** is the recommended implementation library, not a previously approved proprietary asset. Keep strokes and optical sizes consistent, approximately 1.75–2px at 24px. Small navigation icons can accompany labels but must not replace them. Do not mix icon packs or use emoji as interface icons.  
- **Cards:** White or soft-peach surfaces over cream, **18–24px** corners, **16–24px** padding, subtle borders, and little or no shadow. Use short headings, plain supporting copy, and clear grouping. Cards should feel like organized notes rather than crowded listing tiles.  
- **Lists and tables:** Use restrained dividers, legible column labels, and sufficient row padding. For apartment comparisons, show user priorities, trade-offs, notes, and missing information explicitly. Stack or scroll carefully on mobile rather than shrinking text.  
- **Links:** Deep-green readable link text; underline links in paragraphs and make focus visible. Do not depend only on a color difference to indicate clickability.  
- **Tabs and chips:** Soft pills with a clearly differentiated selected state, visible labels, and appropriate button or tab semantics. Small tabs should remain touch-friendly.  
- **Inputs and forms:** Visible labels, generous hit areas, descriptive error/help text, and a clear focus outline. Do not rely on placeholder text as the only label.  
- **Navigation:** Simple top-level choices, short labels, optional small accompanying icons, and one clear primary action. Keep mobile navigation easy to use.

**Illustrative product content:** Apartment cards, notes, and comparisons on the landing page must be labeled as examples when they are fictional. Do not imply a working live feed, automatic verification, or confirmed integrations unless implemented.

---

## Imagery

- **Photos:** Prefer no photos when a simple illustration or UI example communicates better. If photos are needed, choose authentic-looking NYC residential details, real streets, apartment windows, or people in natural settings, with permission/licensing verified. Avoid staged real-estate stock imagery, fake-looking luxury apartments, and visuals implying a particular listing is verified.  
- **Illustrations and video:** Prefer **original, simple, minimal, flat illustrations**. Good motifs include NYC brownstones, apartment windows, modest street scenes, subway details, plants, sunsets, and diverse neighbors where relevant. Use clean rounded shapes, very little texture, and the SettleWise palette. Illustrations support the message and should not compete with the content.  
- **What to avoid:** Busy editorial artwork, elaborate skylines, mascots, detailed characters, glossy 3D, generic AI stock art, overly cute children's-book styling, gradients, and imitations of Headspace or another brand's recognizable illustration style.  
- **Alt text:** Describe what an informational image actually shows and, where material, clarify that it is an illustration or generated visual rather than a real property photo. Decorative illustrations should use empty alt text or be hidden from assistive technology.

### Illustration prompt template

Use this as the starting point for new illustrations. Change only the scene and composition details needed for the page.

```
Create an original, simple, minimal flat illustration for SettleWise,
an NYC apartment decision-support platform. Use soft rounded shapes,
clean outlines where needed, generous empty space, and very low detail.
Friendly and warm, polished rather than childish. Do not imitate the
recognizable illustration style of any existing brand.

Palette (exact HEX): warm cream #FFF8EE, sage green #739282,
deep green #34443A, terracotta #BD6248, soft peach #F7E1CF.
Use cream as breathing room, sage and peach for larger shapes,
and terracotta only as a small accent.

Scene: [describe a simple NYC apartment-hunting moment or detail]
Color emphasis: [which approved brand colors should dominate]
Composition: [subject placement, empty space, intended aspect ratio]

Avoid photorealism, gradients, shadows, detailed editorial scenes,
mascots, busy backgrounds, unapproved colors, and text embedded in art.
```

&nbsp;

---

## Accessibility floors

- **Contrast:** Minimum **4.5:1** for normal text and **3:1** for large text; at least **3:1** for essential non-text controls and boundaries. Check actual pairings instead of assuming brand colors pass.  
- **Focus:** Visible keyboard focus on every interactive control; all essential actions must work without a mouse.  
- **Touch:** Aim for at least **44×44px** practical tap targets, with sufficient spacing.  
- **Structure:** Real heading hierarchy, semantic landmarks, accessible labels, descriptive links, and correct button/tab semantics.  
- **Responsive use:** Support small screens around **320px**, text resizing, and **200% zoom** without hiding critical information.  
- **Motion:** Respect `prefers-reduced-motion`. Do not use animation as the only way to understand a state.  
- **Information:** Never communicate unknown data, status, confidence, or apartment ranking by color alone. Label uncertainty in words.

Target WCAG 2.2 AA where applicable. These are implementation floors, not a claim that the current prototype has passed a full accessibility audit.

---

## Never

- Never redesign the approved logo, change its winding path, disconnect its dot, or add a white ring around the dot.  
- Never use off-palette blues, purples, neon colors, cold gray-greens, gradients in the logo, or decorative effects that reduce legibility.  
- Never use Fraunces or another decorative serif as the SettleWise heading font.  
- Never crowd the page with dense listing tables, excessive CTAs, tiny type, or busy illustrations.  
- Never copy another company's distinctive visual identity.  
- Never use pressure tactics, countdowns, false urgency, or exaggerated claims.  
- Never claim apartments are “100% verified,” “scam-free,” “risk-free,” or objectively “the best” without evidence. Never imply that SettleWise decides for the renter.  
- Never hide missing apartment details or invent property, neighborhood, or listing data.

---

## Logo

### The mark

The approved symbol is a **rounded location pin** containing a **smooth, winding, S-like cream path** that **connects directly to a circular destination dot**. The pin grounds the product in place; the path represents a renter navigating a complicated decision; the destination suggests greater clarity rather than a guaranteed outcome. The symbol is simple enough to recognize without the wordmark at small sizes.

### Directions considered and feedback

The team explored literal houses and roofs inside pins, NYC building silhouettes, abstract letterforms, a winding journey/path, and complicated “confusion to clarity” marks. Literal house/pin hybrids felt awkward; overly elaborate paths became hard to remember and scale. The team selected the **simple pin with the winding S-shaped path and destination dot**. A key revision was to **connect the path to the dot**. Later feedback required exact palette matching and a distinct dark-background treatment with an **orange marker and green dot**. The final rule explicitly rejects a white halo around the dot.

&nbsp;

### Usage rules

- Derive all versions from the **same master symbol geometry**. Only the approved colors, size, and lockup orientation may change.  
- Use the horizontal lockup when there is room for a full brand name; use the stacked lockup for centered layouts; use the mark alone for small icons and favicons.  
- Use SVG where possible for crisp scaling. Do not stretch, skew, rotate, crop, trace over, or add effects to the logo.  
- Leave clear space around the logo, ideally at least **one destination-dot diameter** on all sides. Treat this as a working spacing rule, not a measured specification from the original artwork.  
- Preserve readable contrast against the background. Use the approved primary or dark color mapping above.  
- Do not outline the dot, create a halo, or separate the path from it.  
- At favicon sizes, prioritize recognition of the original mark; do not invent a different icon.

&nbsp;