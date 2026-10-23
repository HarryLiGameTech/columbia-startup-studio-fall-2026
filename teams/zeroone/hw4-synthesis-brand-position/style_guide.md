# STYLE_GUIDE.md — CallIt

**Team:** ZeroOne · **Course:** Columbia 4995 AI Startup  
**Version:** 1.4 · **Updated:** October 9, 2026  
**Status:** Final for Part 5 — B2 room + BE visual style, with the sun character as the final logo.

**Purpose:** Make CallIt recognizable across product screens and brand materials. Use these concrete decisions with the team's brand position when creating or reviewing a page.

**Applied direction:** B2's group / prediction / comments room, combined with BE's colors, type and rounded controls. The classroom prototype was checked at desktop and 390px widths, and a team member reviewed the final page on an actual phone and reported no issues. It has no accounts, real scoring or dispute handling.

This guide follows the eight sections of the teacher's [template](https://github.com/kenxle/columbia-startup-studio-fall-2026/blob/main/resources/template_style-guide.md). The [St. Clair AI example](https://github.com/kenxle/columbia-startup-studio-fall-2026/blob/main/resources/example_style-guide_stclair-ai.md) informed the level of specificity; CallIt's design decisions remain its own.

The brand thesis is **Being right is better when your group remembers.** CallIt is group-centered prediction, light competition and a shared record. Use the spelling **CallIt**.

---

## Color

| Token | Hex | Job |
| --- | --- | --- |
| ink | `#F5F4FB` | Main interface text on the dark product surfaces |
| ink faint | `#BEBBCF` | Descriptions, terms, timestamps and metadata |
| background | `#171824` | Main product ground |
| accent | `#67E3DD` | Primary button, selected answer and one focal phrase |
| on accent | `#14252A` | Labels inside cyan controls |
| second color | `#E7A1C2` | Small group indicators and avatar accents |
| tint | `#2D2940` | Grouping the room and prediction-linked conversation |
| card | `#222431` | Prediction and form surfaces |
| line | `#4F4D64` | Quiet divisions and outlined secondary controls |
| error | `#FFB4AB` | Invalid-input boundary and error text on a dark surface; never an incorrect prediction |
| logo coral | `#E66C57` | Character body and primary social-avatar background |
| logo cream | `#FAF8F0` | Eyes, inverse character and wordmark on dark; logo presentation ground |
| logo charcoal | `#25252A` | Facial details and wordmark on light |

**Rules:** cyan owns the main product action. Coral belongs to the character and may repeat sparingly in avatars, small group identifiers and brand details. Keep cyan as the primary action color. Pink is a small supporting cue. Give answers equal color treatment before selection; never imply likelihood through red/green. Use flat fills, no gradients, and no color-only state changes. A full light product theme is not defined; the logo has light/dark applications.

---

## Type

- **Headings:** Space Grotesk, weights 600–700. Sentence case for the main headings; short 10–11px metadata/eyebrows may use uppercase. Desktop hero up to 64px/1.08; phone hero 43px/1.08. Section titles 29–31px/1.15. Prediction titles 29px desktop and 25px phone, line height 1.22.
- **Body:** DM Sans 400–500; 16–17px, line height 1.7, about 60–65 characters per line. Controls 14–16px/1.5 at 600–700. Terms and metadata 12–13px/1.6. Do not use the playful wordmark lettering for long text.
- **Wordmark:** use the custom outlined `logo/wordmark-*.svg` or supplied lockup. Exact spelling: uppercase-C a l l uppercase-I t. The capital I has short rounded top and bottom bars, a slightly wider silhouette and extra separation from the two lowercase l letters. Never substitute a similar font, stretch the name, or reposition letters.

The interface uses two families. Use Space Grotesk and DM Sans; do not introduce the explored Nunito Sans or Fraunces into the final interface.

---

## Space and layout

- **Content width:** 1200px maximum shell, including 40px left/right desktop padding; 30px at the tablet breakpoint; 22px on phones.
- **Section spacing:** final hero 20px top / 34px bottom; supporting section 30px top / 38px bottom. Hero actions use 25px top / 32px bottom spacing. Follow an 8px rhythm with 4px adjustments; keep a heading closer to its content than to the preceding section.
- **Grids:** desktop room uses 140px members, a flexible prediction, and 220px comments, with 10px gaps and 12px outer padding. Below 950px, comments move under the prediction. At 640px and below, show members, prediction, then comments in one column; answer controls stack so labels stay readable.

The room expresses one group prediction and its comments. It must not suggest a full general messaging service. Question, closing time and what counts appear before answering; the result follows with the recorded answer.

---

## Components

- **Buttons:** rounded rectangle, 12px radius. Primary: cyan fill with on-accent text, 48px minimum height. Secondary: transparent/dark surface with a 1px line border. Compact header, reset and reveal controls still have at least 44px hit height. Hover may move a button slightly; disable that movement with reduced motion.
- **Icons:** Lucide only for interface icons, 2px stroke on a 24-unit viewBox, usually rendered at 16–20px. The current primary CTA uses its arrow-up-right icon. Use visible text beside icons; hide decorative icons from assistive technology. Do not mix emoji or custom decorative glyphs into the icon system. The brand mark and initial-letter avatars are separate assets, not interface icons.
- **Cards:** prediction has a 17px radius and 22–26px padding; the room has a 23px radius and a plum fill. Use fills and quiet full boundaries; no drop shadows. Avoid turning every paragraph into a separate card.
- **Lists and tables:** members/comments are simple aligned rows with names. Bulleted prose uses ordinary round bullets. Information tables use clear column labels, left alignment, subtle horizontal separators and a tinted header. Keep wide documentation tables in a horizontal scroller on phones, rather than overflowing the page.
- **Links:** inline text links are visibly underlined. Product navigation/standalone actions have a 44px hit area. On dark, use readable ink or cyan; on light documentation, use a darker link tone rather than low-contrast coral. Never remove keyboard focus.

**States:** show selected text and `aria-pressed`, explicit results, and kindly phrased incorrect answers. Errors are input failures, not losing a prediction. The demo can create a question with a winning condition, choose an answer, reveal a sample result and reset; it clears unrelated comments on new questions. Its group list is illustrative, not a working group switcher.

---

## Imagery

- **Photos:** none in the current product. If a later page needs photography, use licensed Pexels images or original team photographs. Search for a real shared activity such as “students studying together library natural light” or “friends watching basketball at home”. Choose ordinary participation, with plausible context, rather than staged celebrations. Check the individual source license before use.
- **Illustrations and video:** we developed the selected concept with ImageGen from a sun-face visual reference, then adapted it into a consistent native vector logo. No generated video is included. For future supporting scenes, use the same flat, rounded, warm visual language and the prompt below; do not generate the official logo again for each placement.
- **What to avoid:** glossy 3D mascots, gradients, stock confetti celebrations, casino props, money symbols, unrelated decorative imagery and a repeated character expression that mocks someone for being wrong.
- **Alt text:** identify the content and its purpose without inventing facts. A meaningful generated scene can be described as an AI-generated illustration when that provenance matters. The logo's accessible name is “CallIt”; decorative repeats have empty alt text.

### Illustration prompt template

```text
Flat editorial illustration with soft rounded silhouettes and clean edges.
Use generous negative space and one clear shared activity.
Palette: dark #171824, cream #FAF8F0, coral #E66C57;
use cyan #67E3DD sparingly to support the main action.
Mood: friendly confidence and curiosity, with kind expressions.
Avoid gradients, gloss, 3D effects, casino imagery, text and stock-photo poses.
Scene: [one concrete moment a group is experiencing together]
Color emphasis: [choose the background and one dominant accent]
Composition: [wide or square, focal group placement, empty space for page copy]
Keep the official logo separate and reuse its supplied SVG master unchanged.
```

---

## Accessibility floors

Use a minimum 4.5:1 contrast ratio for normal text. Measured pairings: Ink/Background 16.11:1, Muted ink/Card 8.21:1, and On accent/Accent 10.25:1. Error text is a light salmon on the dark surfaces; pair it with a written message.

Product controls have at least 44px hit areas, with 48px primary/answer buttons. Keyboard focus is visible on links, buttons, disclosures and inputs. Use labeled fields, native controls/dialogs, an h1 followed by h2 section/prediction titles, meaningful landmarks, a skip link, and text feedback. Retain comments at narrow widths. Respect reduced motion and do not rely on color alone.

The applied page was checked at desktop and 390px responsive widths. On October 9, 2026, a team member also viewed the final page on an actual phone and reported no issues. These visual checks do not establish usability research or accessibility certification.

---

## Never

- Gambling language in product copy, payment promises, casino graphics or cash-value rewards.
- Unsupported claims about adoption, automation, fairness or engagement; invented scoring or dispute rules.
- Gradients, heavy shadows, stretched lettering, mixed icon families, emoji as interface icons or glossy mascot rendering.
- Multiple competing primary accents in a single control; colors that imply an answer is more likely to happen.
- A full-chat promise, a sports-only identity, or making every prediction a joke.
- An incorrect answer framed as a personal failure or an input error.
- Regenerating, rotating, distorting or changing the official character for arbitrary placements.

The draft position allows local points/tokens without cash value; their actual rules remain unresolved and are not implemented in this brand preview.

---

## Logo

- **The mark:** a warm sun character with a raised eyebrow and a knowing smile, paired with heavy rounded CallIt lettering. It captures the friendly “I had a hunch” moment and the social payoff of a group remembering who called it.
- **Directions considered:** M01's C/conversation clearly connected the initial to a social product but could read as a messaging app. M10's open ring/dot worked well small but was more generic. The sun reference added expression and a memorable character. We selected the sun character as the final logo direction. We retained B2's room for group context and BE's visual style for a clearer primary action. The sun direction adds the warmth and personality missing from the earlier abstract marks.
- **Files:** the current official set is **`logo/`**. This submission contains the final logo assets only; use the color matrix below to select a version.
- **Rules:** reuse the native vector master and outlined wordmark. The horizontal mark matches the capital I's height and baseline. Color, clear space, minimum sizes and export rules below apply to every placement. The vector version intentionally normalizes the source concept's larger mascot and removes raster texture; it is not a pixel-perfect bitmap trace.

### Construction, alignment and clear space

- Master mark: 256 × 256 viewBox; full-detail filled shape spans y=12 to y=244, a 232-unit height.
- Horizontal lockup: 648 × 160 viewBox. The filled mark and capital I are both **140 units tall**, aligned from y=9 to y=149.
- Mark transform: `translate(0 1.76) scale(0.603448275862)`. Wordmark starts at x=176. The visible mark-to-wordmark gap is approximately 0.2 × capital height.
- Clear space: **0.25 × capital height** around the complete lockup. At 32px CSS height, capital height is 28px, so leave at least 7px clear space.
- Standalone mark: preserve the supplied face and contour. For avatars, use the square asset's built-in padding.
- Use supplied lockups. Set the image height and use automatic width to preserve its proportions; do not reposition individual letters or recreate the logo from text.

### Color matrix

| Application | Mark / face | Wordmark | Background |
| --- | --- | --- | --- |
| Light | Coral body, cream eyes, charcoal features | Charcoal | White or Cream |
| Dark | Same full-color character | Cream | BE Background or comparable dark surface |
| One-color black | Black with transparent face cutouts | Black | Light |
| One-color white | White with transparent face cutouts | White | Dark |
| Primary avatar | Cream character with charcoal features | None | Coral rounded square |
| Alternate square | Matching light/dark/black/white version | None | Supplied square background |
| Favicon 16px | Simplified cream character, two eyes and smile | None | Coral square |

Transparent backgrounds are used for marks, wordmarks and lockups. Square/avatar/icon files intentionally contain backgrounds. Monochrome versions simplify the face into negative space, preserving single-color production.

### Minimum sizes

| Asset | Minimum | Preferred use |
| --- | --- | --- |
| Full-detail mark | 32px SVG box | 40–48px or larger |
| Horizontal lockup | 32px CSS height (about 130px width) | 40px height in desktop header; 34px on phone |
| Stacked lockup | 120px width | Profiles, posters and narrow spaces |
| Simplified favicon | 16px | Browser tab |
| Primary avatar | 32px | Use larger sizes where its facial detail matters |

Use the simplified favicon at 16px rather than shrinking the full wordmark. Check all placements against their actual background. Minimums were established from rendered small-size comparisons, not user research.

### Full file set

`logo/` includes **23 SVG logo masters** with matching PNG exports, six exact-size favicon PNGs, a multi-size ICO, and `logo-matrix.svg` / `logo-matrix.png`. There are **24 SVG files in total: 23 logo masters + 1 overview matrix**.

- Mark alone, wordmark, horizontal lockup, stacked lockup and square avatar, each in light, dark, black and white versions.
- Primary coral social avatar; full-detail app-icon SVG; simplified favicon SVG.
- Favicons at **16, 32, 48, 180, 192 and 512 pixels**; multi-size ICO with 16/32/48px images.
- `logo-matrix.svg` and `logo-matrix.png`: a complete overview of the final versions and favicon exports.

PNG marks are exported at 512px width; wordmarks at 1200px; horizontal lockups at 1600px; stacked lockups at 1000px. SVG is preferred for scalable placement. Use PNG where SVG is unsupported. White files need a dark background.

Do not stretch, rotate, add shadows/gradients, change the facial expression, use exploration marks as official alternatives, recolor the logo arbitrarily or alter its spelling.
