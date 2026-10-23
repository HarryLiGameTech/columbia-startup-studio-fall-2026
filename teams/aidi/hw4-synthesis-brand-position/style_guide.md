# STYLE_GUIDE.md — Aplovia

**Status:** Style direction, product name, and logo direction selected. Complete domain and trademark clearance before public launch.

**Purpose:** This guide defines the visual identity for the product so that every page and screen feels professional, trustworthy, clear, and calm. Give it to a coding agent together with `brand_position.md` before building product interfaces.

**Reference implementation:** Visual direction 2A — Midnight Navy, tested in the browser at desktop and iPad widths before this guide was finalized.

---

## Reference direction

- **ChatGPT:** Keep the clearly separated, collapsible left navigation and the account entry at the bottom. Use a separate optional right drawer for contextual AI help. Do not imitate ChatGPT's conversation-first content model.
- **Canvas:** Keep familiar dashboard labels and a straightforward course-management-style information hierarchy so first-time users can predict where to find work. Avoid its denser institutional administration feel.
- **Notion:** Keep modular cards and flexible planning blocks that let students organize their own work. Avoid blank-canvas ambiguity and excessive customization in the MVP.
- **Grammarly:** Keep the searchable document-card grid, short previews, status, and last-edited metadata. Avoid promotional banners and upgrade pressure inside core work areas.
- **U.S. News:** Keep the scan-friendly school-result structure and comparable facts. Place personalized fit, affordability, sources, and reasoning above rank so the interface does not become ranking-first.

These references supply familiar interaction patterns, not a visual identity to copy. Aplovia combines them in one restrained Midnight Navy system with less decoration, lower saturation, and a clearer next-action hierarchy.

---

## Color

| Token | Hex | Job |
|---|---|---|
| `ink` | `#15202C` | Primary headings, body text, and high-emphasis data. Never use pure black. |
| `ink-faint` | `#66717C` | Secondary copy, hints, timestamps, and metadata. Contrast is 4.98:1 on white. |
| `background` | `#F5F7F9` | Main workspace background. |
| `surface` | `#FFFFFF` | Cards, panels, inputs, menus, and the AI drawer. |
| `nav` | `#172331` | Expanded and collapsed left navigation rail. |
| `nav-ink` | `#B8C4CF` | Inactive navigation labels and icons on `nav`. Contrast is 8.96:1. |
| `accent` | `#294A69` | Primary buttons, selected controls, active links, and focus emphasis. White text has 9.22:1 contrast. |
| `accent-muted` | `#607C9A` | Secondary blue details and supporting data visualization. Do not use for small text on white. |
| `accent-tint` | `#E4EBF1` | Selected navigation backgrounds, fit badges, and subtle contextual highlights. |
| `border` | `#D9DEE3` | Card, input, table, and divider borders. |
| `due-soon` | `#9A681F` | Outline and text for the “Due soon” status. Contrast is 4.80:1 on white. |
| `overdue` | `#B33D45` | Outline and text for the “Overdue” status. Contrast is 5.72:1 on white. |
| `completed` | `#4F746B` | Outline and text for the “Completed” status. Contrast is 5.19:1 on white. |

**Rules:** Use a single Midnight Navy theme: a dark navigation rail with a light workspace. The MVP has no full dark mode. Use one accent per interactive element. Keep colors low-saturation. Never use gradients. Status colors appear as outlined text labels near the relevant action; they do not recolor the entire task card. “Due soon” begins seven days before the deadline. “Overdue” begins after an incomplete task passes its deadline. “Completed” appears after the student marks the task complete.

---

## Type

- **Headings:** Inter 600 and 700; sentence case; compact tracking from `-0.01em` to `-0.03em` for larger headings. Never use cartoon, handwritten, inflated, or futuristic display faces.
- **Body and interface:** Inter 400, 500, and 600. Default interface text is 15–16px with 1.5 line height. Supporting labels and metadata may use 12–13px only when contrast remains sufficient.
- **Chinese:** Noto Sans SC / Source Han Sans SC in corresponding weights. Use a 1.55–1.65 line height for paragraph-length Chinese text. Allow cards and buttons to grow instead of truncating important translated instructions.
- **Fallback stack:** `Inter, Aptos, "Segoe UI", "Noto Sans SC", "Microsoft YaHei", sans-serif`.
- **Wordmark:** Set “Aplovia” in Inter 700 with clean, unmodified letterforms. Use the supplied horizontal or stacked lockup whenever space allows.

---

## Space and layout

- **Application shell:** A collapsible left navigation rail, flexible central workspace, and optional right AI drawer. The two sidebars open and close independently.
- **Left rail:** 236px expanded and 72px collapsed. Use the `nav` color so it is visibly separate from the light workspace. The account avatar and account menu stay at the bottom; Settings is not a primary navigation item.
- **Right AI drawer:** Approximately 360px on desktop and closed by default. It may show a subtle prompt when a student remains stuck, but it never opens automatically.
- **Content width:** Up to 1180px, centered within the available workspace.
- **Page inset:** 32–34px on desktop and 18–24px on small screens.
- **Spacing scale:** 4, 8, 12, 16, 24, 32, and 48px. A heading sits closer to the content it labels than to the preceding section.
- **Dashboard hierarchy:** Show one deadline-driven “Your next step” card first. Progress, school review, and recent documents follow below.
- **Supported viewport:** Phase 1 is designed and tested for desktop and iPad-class web browsers, beginning at approximately 768px wide. Phone layouts are not a release target.
- **Grids:** Document cards use three columns on wide desktop screens and two columns on iPad-class screens. School result cards remain horizontal while their data can be read comfortably; secondary metrics may wrap below the school identity on iPad portrait layouts.
- **Responsive sidebars:** On iPad portrait layouts, sidebars may become overlays and only one may be open at a time. Preserve a basic narrow-screen fallback, but do not weaken the desktop or iPad information architecture to create a phone-first interface.

---

## Components

- **Buttons:** 6px radius and at least 44px high. Primary buttons use `accent` with white text. Secondary buttons use `surface`, a `border` outline, and `ink` text. Use direct verbs such as “Continue,” “Compare,” or “View details.”
- **Icons:** Use one outline icon family, preferably Lucide, at 1.5–1.75 stroke. Icons inherit `currentColor`. Do not mix icon libraries or use emoji as interface icons.
- **General cards:** `surface` background, full 1px `border`, 8px radius, and no default shadow. Use spacing and borders—not decoration—to establish hierarchy.
- **Task card:** Prioritize the task title, deadline, estimated completion time, reminder status, and one primary action. Put the status pill near the action button with approximately 16–18px of separation.
- **Task-status pills:** White background, 1px colored outline, matching text, 999px radius, minimum height 28px, and 12px semibold label. Use exactly “Due soon,” “Overdue,” and “Completed,” with equivalent Chinese labels. Do not use “Missing.”
- **School result card:** Follow a structured U.S. News-like result pattern, but place personalized fit above rank. Show school name, location, institution type, Reach/Match/Safety classification, brief matching reasons, essential metrics, save/compare actions, primary sources, and last-checked date. Ranking is secondary information, never the decision.
- **Reach/Match/Safety labels:** Display as compact classifications with an explanation available. Never imply guaranteed admission, and never use red/yellow/green alone to communicate the classification.
- **Document cards:** Follow the Grammarly document-dashboard pattern: a searchable grid showing document type, title, short content preview, draft status, last-edited time, and an overflow menu. Keep card heights aligned within a row.
- **AI drawer:** Show what context the AI is currently using and what it is not using. A document or other sensitive material is included only after the student selects it. The drawer is assistance within the current page, not a separate primary destination.
- **Navigation:** Primary destinations are Dashboard, Find Colleges, My College List, Application Plan, Documents, and Calendar. Find Colleges and My College List are separate pages.
- **Lists and tables:** Use clear column headers, horizontal dividers, and no decorative zebra striping. On narrow screens, turn data rows into labeled stacks rather than forcing horizontal scrolling where practical.
- **Links:** Use `accent` for standalone links. Inline links are underlined with a 2–3px underline offset. Do not use color alone to distinguish links from surrounding copy.
- **Language control:** Keep a visible `EN | 中文` control in the top bar. Switching changes the entire interface, but never automatically translates a student’s application document.

---

## Imagery

- **Photos:** Avoid decorative photography inside the product. Use an image only when it provides necessary information.
- **Functional imagery:** School marks, user avatars, and useful document previews are allowed. Verify rights and provide a text fallback for school marks.
- **Illustrations and video:** Do not use them by default. A small functional empty-state illustration is allowed only when an icon and clear instruction are insufficient.
- **What to avoid:** Staged student stock photos, decorative campus photos, cartoon mascots, glossy 3D shapes, generic AI artwork, sparkles, brains, circuits, and images used only to fill space.
- **Alt text:** Describe the information conveyed by the image and disclose when a generated visual is used. Decorative images, if ever present, use empty alt text.

### Illustration prompt template

Use only for a necessary empty state:

```text
Minimal flat line illustration with no border and no decorative background.
Palette: #15202C, #294A69, #607C9A, #E4EBF1, and #F5F7F9.
Cool, calm, professional, and functional. Low saturation and even lighting.
Avoid: gradients, photorealism, cartoon characters, glossy 3D forms, sparkles,
brains, circuits, generic AI imagery, and unnecessary visual detail.

Scene: [the exact empty state or unavailable item]
Color emphasis: Midnight Navy linework with one muted blue detail
Composition: compact, centered, and readable at a small size
```

---

## Accessibility floors

- Maintain at least 4.5:1 contrast for normal text and 3:1 for large text and meaningful non-text UI boundaries.
- Give every interactive control a visible focus treatment. Use a 3px low-opacity accent ring with at least 2px offset.
- Use at least 44 by 44px pointer targets, even when the visible icon is smaller.
- Use real landmarks, labels, buttons, links, and heading order; do not simulate controls with generic containers.
- Never communicate status, fit, or urgency through color alone. Pair color with explicit text and, where useful, an icon.
- Respect reduced-motion settings. The core experience must not depend on animation.
- Test both English and Chinese at desktop and iPad portrait and landscape widths. Allow for approximately 30% text expansion without overlap or clipped actions.

---

## Never

- No full dark mode in the Phase 1 MVP.
- No gradients, neon colors, highly saturated accents, or pure black.
- No decorative stock people, large hero imagery, or generic AI art inside the product.
- No cartoon type, emoji icons, mixed icon families, or unnecessary animation.
- No large shadows as the primary way to separate content.
- No ranking-first school presentation, unexplained admission score, or color-only Reach/Match/Safety meaning.
- No automatically opened AI drawer and no hidden use of documents or personal information.
- No automatic translation or rewriting of a student’s application materials.
- No settings item in the primary navigation; settings live in the account menu.
- Do not use “AIDI” or “Product Name” as the public product name. AIDI remains the team name; Aplovia is the selected product name.

---

## Logo

- **Product name:** Aplovia, formed from “apply/application” and “via” (a way or path). The name supports the idea of a clear, self-directed route through college applications without promising admission.
- **Directions considered:** The wide round explored letter combinations, stand-alone route symbols, and a start-to-destination symbol. The **AV monogram** was retained because it connected the product name to the mark; the **road/path** idea was retained as movement through an application journey but rejected as a generic stand-alone icon; the **start-to-destination** idea communicated progress but felt too diagrammatic by itself. The selected mark combines all three ideas through an AV structure, central route, and separated destination triangle.
- **The mark:** A geometric fusion of **A** and **V**. Its separated upper triangle acts as a destination, while the lower V and angled outer forms suggest a route moving from a starting point toward that destination. The idea communicates guidance and progress without promising admission. AIDI remains the team name and does not appear in the public mark.
- **Primary color:** Use Midnight Navy `#172331` on white or other light neutral backgrounds. On the Midnight Navy navigation rail or another sufficiently dark background, use the all-white version. Do not introduce a separate logo-only color.
- **Lockup:** The mark functions as the initial **A** and is followed only by **plovia**. Never place the mark beside the full word “Aplovia,” which would repeat the A. In the horizontal lockup, size the mark close to the letter height, align its lower point with the wordmark baseline, and use only a narrow optical gap before the p so the result reads as one word. Use the stacked lockup only in centered or vertically oriented placements; there, the mark appears above **plovia**.
- **Clear space:** Keep empty space around the mark and lockups equal to at least the width of the mark's central white channel. Do not place text, borders, or other marks inside that space.
- **Minimum size:** The mark alone may be used down to 16px square only in the supplied square favicon treatment. Use the transparent mark at 24px wide or larger. Use the horizontal lockup at 120px wide or larger; below that size, use the mark alone.
- **Backgrounds:** Prefer white, `background`, `surface`, or Midnight Navy. Never place the logo over photography, a gradient, a busy texture, or a background that reduces contrast.
- **Do not:** Do not rotate, stretch, outline, rearrange, add shadows, round individual geometric pieces, close the intentional gaps, or use the mark as a decorative pattern. Do not add an AI sparkle or graduation cap.
- **Files:** Final assets live in [`logo/`](logo/). The folder includes the transparent primary mark, square mark, horizontal and stacked lockups, dark-background and one-color versions, a social avatar, a scalable favicon, and PNG favicons at 16, 32, 48, 180, 192, and 512 pixels.
