# ClientReady visual exploration and decision record

Date: October 9, 2026. Product focus: ClientReady, confirmed by the user. Visual choice: **Content desk (A), selected by the user on October 9, 2026; logo 02 Aligned sheets selected by the user**. All first-round creative decisions below were made by AI using the supplied interview evidence and provisional brand direction.

## Evidence that shaped the brief

The supplied ClientReady interviews describe uneven contributions, a long document plus images that still need sorting, and uncertainty about what to write. One participant also described waiting for someone to reply; another described changing information. These are related but distinct tasks. The visual exploration focuses on organizing content by page and making unanswered questions visible. It does not claim that a tool can remove waiting, resolve every story decision, or establish demand among professional agencies.

Provisional core line: **“Know what belongs on each page.”** Supporting line: **“Turn scattered text and images into a clear content handoff.”** The sample project names and content are clearly labeled illustrative.

## Reference set

These are **AI-selected references**, not websites the user said they liked. Official pages were inspected through web text retrieval on October 9, 2026. No screenshot-based visual audit was performed. The observations below concern accessible page content and organization, not an exact recreation of those brands.

| Reference | What was inspected | Principle to explore | What not to borrow |
|---|---|---|---|
| [Are.na](https://www.are.na/) | Its sequence for capturing, arranging, searching and connecting material | Make organizing content a concrete activity; keep the explanation direct | Its logo, typography files, content or community claims |
| [Basecamp](https://basecamp.com/) | A detailed website-redesign project example with tasks and source materials | Demonstrate the workflow using a specific example instead of only abstractions | Fictional demo people presented as ClientReady customers, product capabilities or testimonials |
| [Linear](https://linear.app/) | Official product-development homepage and organization of its product story | Keep a strong hierarchy between product proposition and workflow detail | Its visual identity, icons or implied feature parity |
| [GOV.UK](https://www.gov.uk/) | Its task-oriented information categories and direct link language | Use clear destination names and labels people can act on | Government authority cues, crown mark or official-service styling |

The team should add 3–5 references it actually likes or explicitly approve this set and explain why. A preference cannot be inferred from memory that contains no visual choices.

## Round 1: six distinct HTML directions

Each option contains a hero and at least one developed content section, a mobile breakpoint, a functional feedback form, and a self-contained asset path. Open [`index.html`](index.html) to compare.

| ID | Direction | Composition and character | AI critique / tradeoff |
|---|---|---|---|
| 01 | [Paper and plan](explorations/01-paper-and-plan.html) | Asymmetric editorial hero; serif headline; cream, cobalt and sage; page ledger | Recommended: close to content preparation and sufficiently calm. May feel more editorial than a software workspace. |
| 02 | [Cobalt workspace](explorations/02-cobalt-workspace.html) | Centered hero; sidebar and three-column task board; cool blue | Communicates a workspace clearly. Risks implying a more mature app than exists; labels explicitly identify the concept. |
| 03 | [Warm workshop](explorations/03-warm-workshop.html) | Rounded worktable; angled sheets; terracotta; warm serif | Supports collaborative decision-making. Paper metaphor may be too informal for professional studios. |
| 04 | [Technical index](explorations/04-technical-index.html) | Dark surface; content manifest; monospace details; lime accent | Speaks to a builder who thinks in source files. Potentially alienating for contributors who are not technical. |
| 05 | [Quiet current](explorations/05-quiet-current.html) | Centered serif; materials-to-page flow; quiet teal | Makes the transformation legible. Less distinctive than the editorial or expressive alternatives. |
| 06 | [Content in place](explorations/06-content-in-place.html) | Oversized display type; hard rules; citron and ink; page strip | Distinctive and easy to remember. The large word shapes compete with explanation on smaller screens. |

These critiques are AI judgments. They are not invented comments from Anson, teammates, interview participants, or personas.

## Team feedback collection

Each full page ends with an empty **keep / kill / why** form. It saves in the current browser's local storage and can export a JSON file. Nothing is sent to a server. No choice is preselected. Exported feedback should be placed with the assignment's design process materials.

Record the reviewer, selection, elements to keep, elements to kill, rationale, and mobile observations. The user supplied feedback on directions 01–04 in this conversation; it is preserved below. The user subsequently selected A; subsequent team-direction and phone-review confirmations are recorded below.

## Actual user feedback and round two

User’s exact message:

> 1和2过于简洁 无法展示核心内容 3配色可以 单身有点冗余 4也是 太像GitHub来

Interpretation used for revision: 01 and 02 are too sparse to explain the core; keep 03’s colors but reduce redundancy (the phrase “单身” was interpreted in context as a typing error for “但是”); 04 feels too much like GitHub/developer tooling. The user did not review 05 or 06 in this message.

| Feedback | Concrete revision |
|---|---|
| Core content is not visible enough | Put the source document, image names, exact page-specific questions, proposed Home/About copy and unresolved decisions in the main example. |
| Keep direction 03’s palette | Use cream `#F8ECD9`, terracotta `#943E23` and brown ink `#4E281F`; update the provisional logo palette. |
| Too repetitive | Shorter hero, one complete example, one concise explanation. No repeated feature marketing. |
| Too GitHub-like | Remove the dark file manifest and developer language from both revisions. |

Two feedback-driven revisions are in [`refinements/index.html`](refinements/index.html):

- **[A / Content desk](refinements/a-content-desk.html)**: three visible columns show received material → questions to ask → page-by-page handoff. AI recommendation for explaining the core quickly.
- **[B / Page workbook](refinements/b-page-workbook.html)**: source material sits beside a workbook with questions and draft output paired for Home and About. A closer view of contributor use.

These are a real user-feedback-driven second round. The user subsequently selected A with the exact response: “A：材料 → 问题 → 页面内容（推荐）”. This records the individual user’s choice, not an unreported vote by the whole team. Each full page retains an empty feedback form for the next decision. Only one discreet prototype/example notice appears in the main content; no fake sign-up or functioning-product claim is included.

## Logo exploration

Twelve original SVG sketches explore page boundaries, slots, aligned sheets, brackets, handoff frames and a site map. See [`logo/concepts/contact-sheet.html`](logo/concepts/contact-sheet.html) and its PNG/SVG versions.

The AI initially shortlisted 01 Page slots, 03 Content brackets and 07 Handoff and developed 01 provisionally. The user then selected **02 Aligned sheets** on October 9, 2026 with the exact message **“02吧”**. No rationale was provided. This is an individual user choice, not an invented full-team vote.

The complete developed family was replaced with concept 02: mark, square, wordmark/lockup, explicit dark-background treatments, true black/white versions, stacked treatment, social avatar, and 16, 32, 48, 180, 192 and 512 px icons. Original twelve sketches remain unchanged. The selected A page and alternative B headers now use 02. The small icon has optically adjusted integer-aligned cutouts; the main SVG uses transparent cutouts so the detail works on every background. Wordmark text remains editable rather than outlined.


## Validation performed

- Source checks for local assets, links, titles, viewport tags, matching feedback identifiers and labels.
- Contrast calculations for the recommended guide's principal text pairings; see `validation.json`.
- Raster rendering of the SVG contact sheet, horizontal lockup and icon sizes.
- Visual inspection of the logo contact sheet and horizontal lockup.
- Inspection of the 16 px mark enlarged with nearest-neighbor scaling; the edges are crisp and align to whole pixels.

## Validation not completed

Browser preview was blocked in this environment. No desktop or mobile browser screenshot audit is claimed. CSS contains responsive breakpoints, but that is not proof of no layout overflow. The user opened the local preview and gave feedback on 01–04. An automated screenshot audit is still not claimed. The user subsequently reported that the selected A page and 02 logo displayed normally on a real phone. Device/browser details were not supplied. A keyboard walkthrough, screen-reader spot check and systematic automated browser audit remain open.

## Required next team steps

1. Record the selected A direction with the rest of the team; gather any additional critique.
2. Keep the user’s A selection and further feedback with the submission; approve or replace the reference set.
3. Record full-team review of the user-selected 02 Aligned sheets logo.
4. Retain Content desk as the reference implementation and Aligned sheets as the logo; further revisions should respond to actual new critique.
5. Preserve the user-reported real-phone pass; record device details and new findings if further testing occurs.
6. Update the guide and replace “provisional” only when those decisions are real.


## Final user confirmations — October 9, 2026

Handong answered “已共同同意 ClientReady” when asked whether both teammates had agreed to submit ClientReady. This confirms the direction, not an invented detailed team critique. When asked about a real-phone review of A and logo 02, Handong answered “已经看过，显示正常” (already checked; displays normally). Device/browser details were not recorded. See [confirmation record](../evidence/final_user_confirmations.json). The original keep/kill comments and individual logo selection remain unchanged.
