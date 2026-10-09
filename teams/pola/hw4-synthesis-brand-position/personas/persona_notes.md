# Persona notes: what each persona said about our brand position

We ran each persona agent on `brand_position.md` (2026-10-08 draft), using the agent files in this folder, and then revised the brand position. Nadia, the only persona with conditions, was re-run on the revision. Raw verdicts are at the bottom of each section.

| Persona | Who | Draft verdict | Revision verdict |
|---|---|---|---|
| Lena (lead) | First-year with 10-minute gaps between unfamiliar buildings | approve, 8 | (not re-run) |
| Nadia | Sophomore on crutches who needs step-free routes | approve with conditions, 6 | approve, 8 |
| Kenji | Master's student visiting access-controlled office towers | approve, 7 | (not re-run) |
| Owen | Senior RA, the "just ask someone" skeptic | approve, 7 | (not re-run) |

**What they agreed on:** three of the four (Lena, Kenji, Owen) flagged the same overreach. The positioning statement promised "the doors you're allowed through," while our own open questions admit we don't have the building data to deliver that. We removed it from the positioning, made access-aware routing conditional on buildings that confirm their rules, and added it to Language to Avoid.

**Where they disagreed:** Lena felt the access-rights material was "for someone else" and wanted time pressure to lead; Kenji wanted visitors named more prominently. We kept the first-year as the lead and added one line to the target identity naming the visitor and the step-free user, so neither drops out.

---

## Lena (lead persona): approve, 8

**What she said:** The position matches her real problem: name the hallway, no download, no "always allow," no jokes about being lost. She liked that it refuses to promise she'll be on time. She was put off by two things: the "who's walking it" and access-rights framing felt like it was for building visitors, and the $10 quote made her worry a paywall is coming.

**What we changed:**
- Removed "the doors you're allowed through" from the positioning statement.
- Light touch now puts the calendar link first and the QR code second.
- Marked the thesis as internal; public copy uses the canonical language instead.
- Added pricing as an open question (whether the person walking ever pays is a team decision we haven't made).

**What we didn't change:** We kept the thesis itself, because it is what unifies the step-free and visitor routes. Her request for an honest "this hallway bends" warning in a demo belongs on next week's landing page, not in this document.

<details><summary>Raw verdict</summary>

```json
{
  "persona": "persona-lena",
  "artifact": "Pola brand position (2026-10-08 draft)",
  "verdict": "approve",
  "score": 8,
  "headline": "This position goes after the exact moment I get stuck (which hallway, which door), opens from a link with no app or 'always allow', and refuses to promise I'll never be late, so I'd open it and trust it.",
  "must_fix": [],
  "nice_to_have": [
    "Make the time pressure lead the thesis. 'Depends on who's walking it' and access rights read like they're for building visitors and badge holders. My problem is ten minutes and a fourth floor I've never seen.",
    "Don't let any copy claim 'the doors you're allowed through' until you actually have the building data. A confident route to a locked door is my number one red line, and you already list this as an open question.",
    "Put the calendar-link flow up front everywhere. One tap from 'Discussion, Hamilton 405' in my calendar while I'm walking is the whole reason I'd use it. A QR code at the entrance comes second.",
    "Say plainly that it's free, or that it comes from the school. The $10 quote in key quotes makes me nervous that a paywall is coming, and I'm not paying for campus directions.",
    "Show an honest 'this hallway bends, keep going past 410' style warning in the demo, so I can see the 'honest, not confident' part working and not just being promised."
  ],
  "in_character_reaction": "ok this is basically my hamilton fourth-floor disaster written down as rules: name the hallway, no 'go to floor four', no download, no always-allow, no jokes about me being lost. and i like that it says it can't make me on time, it just stops me wasting minutes on wrong turns, because that's actually true. the access-rights and 'who's walking it' stuff feels like it's for someone else, and if it ever sends me to a locked door because it guessed, i'm done. but if the real thing sounds like this doc, yeah, i'd tap the link.",
  "would_flip_me": "n/a",
  "would_pay": "n/a"
}
```
</details>

---

## Nadia (step-free persona): approve with conditions, 6

**What she said:** The thinking is right: step-free is a first-class route with a plain name, honesty comes before confidence, and there's no charity language. But she had two must-fixes. First, the position never promises to show how current the entrance and elevator information is, and after following a sign to a locked accessible entrance, "we'll tell you when we're not sure" isn't enough. Second, nothing says her step-free choice is remembered, so with no account she might have to pick it again on every route.

**What we changed:**
- Exact over approximate: every route shows when its entrances and elevators were last checked, elevator steps name the floors they reach, and "elevator may be out of service" now sits next to "door may be locked."
- Your route, not the map's: a route is never labeled step-free unless its entrance, its elevator, and the floor that elevator reaches have all been checked.
- Light touch: a step-free choice is remembered on the phone without an account; one instruction per screen, usable one-handed.
- Target identity: a line saying a wrong turn costs someone on crutches ten minutes and pain, not one minute.
- Objection Handling: a new row for "The last "accessible" entrance I was sent to had steps, or was locked."
- Open questions: who keeps "last checked" current, and how often.

**What we didn't change:** Her advice to interview someone with a mobility need before making step-free a headline claim was already an open question; it stays there until the team runs that interview.

**Re-test on the revision: approve, 8.** Both must-fixes are resolved: "Step-free is treated as a real, checked route that names the entrance, the elevator and its floors, and says what hasn't been checked." Her new nice-to-haves are for the product and next week's landing page, not this document: opening hours on entrances, a one-tap "report a wrong entrance" button (which also partly answers who keeps "last checked" current), the length of the step-free route compared with the main one, and offering the step-free option on the first screen.

<details><summary>Raw verdict (re-test)</summary>

```json
{
  "persona": "persona-nadia",
  "artifact": "Pola brand position (2026-10-08 revision)",
  "verdict": "approve",
  "score": 8,
  "headline": "Step-free is treated as a real, checked route that names the entrance, the elevator and its floors, and says what hasn't been checked, so this is the research I do every morning written down as rules.",
  "must_fix": [],
  "nice_to_have": [
    "Add opening hours to entrances, not only 'may be locked': 'East entrance unlocked from 10 a.m.' is what I actually need at 9.",
    "Give me a one-tap way to report a wrong entrance or a broken elevator right from the route. I'd report it, and that also partly answers your open question about who keeps 'last checked' current.",
    "Show how long the step-free route is, or how far it walks compared with the main route. My grandmother can manage no stairs, but she can't manage a long detour either.",
    "The open question says to wait before making step-free a headline claim. Fine, but while you wait, don't let it drift down to the footer or an FAQ. It's already in the positioning statement, so keep it on the first screen of the landing page too.",
    "'The step-free way if you need it' is okay, but on the first screen I'd rather see the step-free option offered next to the main route than have to go looking for it."
  ],
  "in_character_reaction": "Okay, 'Elevator to 5, not take the elevator up' and 'we never label a route step-free unless the entrance, the elevator, and the floor it reaches have all been checked': that's exactly the thing I keep having to explain to people. You remember my setting without making me create an account, it works one-handed, and you tell me which part you're not sure about instead of sending me around the side of a building to a locked door. You haven't built it yet, and I'll believe the check dates when I see them on a real route, but as a set of rules for the product, I'd open this.",
  "would_flip_me": "",
  "would_pay": "n/a"
}
```
</details>

<details><summary>Raw verdict</summary>

```json
{
  "persona": "persona-nadia",
  "artifact": "Pola brand position (2026-10-08 draft)",
  "verdict": "approve_with_conditions",
  "score": 6,
  "headline": "The thinking is right: step-free is a first-class route with a plain name, honesty comes before confidence, and there's no charity language. But the position never promises to show how current the entrance and elevator info is, or to remember that I need step-free.",
  "must_fix": [
    "Promise to show how current the step-free info is for every entrance and elevator (for example, 'Entrance checked 2 weeks ago'). Never label a route step-free unless the entrance, the elevator, and the floor it reaches have all been checked. If something is unchecked, say which part. 'We say so when we're not sure' is a good instinct, but it doesn't help me if I can't tell how old the information is.",
    "Make sure my step-free setting is remembered once I choose it, even though Pola opens from a link or a QR code with no app. The 'Light touch' value doesn't require an account, so as written I might have to pick step-free again on every route. Re-explaining my situation every time is exactly what makes me quit a tool."
  ],
  "nice_to_have": [
    "Under 'Exact over approximate', say outright that directions name which floors the elevator reaches ('Elevator to 5, not 4'). Mention 'elevator may be out of service' next to 'door may be locked'.",
    "Add an objection row for the person who has already been burned: 'The last accessible entrance I was sent to had steps' or 'was locked.' Answer it with the freshness note and the named entrance.",
    "The target identity is entirely the time-crunched first-year. Add a line saying a wrong turn costs someone on crutches ten minutes and pain, not one minute, so step-free doesn't slide into a footnote on the landing page.",
    "Add a tone or interaction note for one-handed use: one instruction per screen, big tap targets, no multi-step menus mid-route.",
    "Good call in the open questions to interview someone with a mobility need before making step-free a headline claim. Do it before the landing page copy is locked, not after."
  ],
  "in_character_reaction": "Okay, this is closer than anything I've used. 'Step-free route, named plainly' and 'not a setting buried in a menu' is exactly what I want, and thank you for not putting a wheelchair icon next to 'we care about everyone.' But last week I followed an accessible-entrance sign to a locked door, so 'we'll tell you when we're not sure' isn't enough. Tell me when someone last actually checked that door and that elevator. And if I'm scanning a QR code with a crutch in one hand, please don't make me tap 'step-free' again every single time.",
  "would_flip_me": "Add one sentence under 'Your route, not the map's': 'Step-free routes show when each entrance and elevator was last checked, and once you choose step-free, Pola remembers it.'",
  "would_pay": "n/a"
}
```
</details>

---

## Kenji (visitor persona): approve, 7

**What he said:** The position says outright that a visitor's route through a tower differs from an employee's, bans floor-only directions and unlabeled entrances, and promises to admit what it doesn't know. But the person it's written for is a student late for class; his problem isn't time (he arrives 20 minutes early), it's which entrance, desk, turnstile, and elevator bank a visitor uses, and the fear of the wrong door. He also wanted "Reception" on the avoid list, an answer to "I just ask security," and plain, literal wording for second-language readers.

**What we changed:**
- Target identity: a line naming the visitor who arrived early but can't afford the wrong door.
- Your route, not the map's: we route by access rules only in buildings that have confirmed them, and otherwise say "check at the desk."
- Language to Avoid: "Reception" joins "Office Entrance" and "Main Entrance."
- Objection Handling: the "I just ask someone" answer now includes the cost of asking, with Devesh's quote.
- Tone: plain, literal words with no idioms.

**What we didn't change:** We didn't add his suggested canonical phrase ("the way a visitor is allowed to go"). It's the persona's wording, not something a real user said, and canonical language should come from users.

<details><summary>Raw verdict</summary>

```json
{
  "persona": "persona-kenji",
  "artifact": "Pola brand position (2026-10-08 draft)",
  "verdict": "approve",
  "score": 7,
  "headline": "The position says outright that a visitor's route through a tower is not an employee's route, bans vague floor-only directions and unlabeled entrances, and promises to admit when it doesn't know, but the person it is written for is a student late for class, not a visitor who arrived early and could walk through the wrong door.",
  "must_fix": [],
  "nice_to_have": [
    "Widen the target identity beyond the student who is short on minutes. My problem is not time; I arrive 20 minutes early. My problem is not knowing which entrance, desk, turnstile and elevator bank a visitor uses, and the fear of walking through a door that is not for me. Name that stake next to Maya's story.",
    "Add canonical language for the visitor sequence: entrance, check-in desk, visitor pass, turnstile, elevator bank, door. 'Your route' is right, but a phrase like 'the way a visitor is allowed to go' would tell me in one line that it is for me.",
    "Add 'Reception' to the language to avoid unless it says who it is for and where it is. That word sent me to a staff door.",
    "Add an objection row for 'I just ask security.' Asking once is fine. Asking twice in a second language, before an interview, in front of people I want to impress, is the real cost.",
    "The positioning promises 'the doors you're allowed through,' but the open questions admit this needs building data that does not exist yet. Until it does, the copy should say per building whether access rules are confirmed or estimated, for example 'elevator bank not confirmed for visitors, check at the desk.' Otherwise the promise becomes the overconfident direction I cannot recover from.",
    "Keep the instructions in plain, literal language with no idioms. Many visitors are reading in their second language while under pressure."
  ],
  "in_character_reaction": "It says a visitor's route and an employee's route through the same tower are different routes, and that 'go to floor four' is not an instruction. That is exactly the problem I had in Hudson Yards, so I would open a link from my calendar invite the night before. But the person this document describes is a student four minutes late to class. I am twenty minutes early, and what worries me is the turnstile and the elevator bank, not the clock. If the building has not told you which bank goes to 38, please say so before I walk to the wrong one.",
  "would_flip_me": "n/a",
  "would_pay": "n/a"
}
```
</details>

---

## Owen (skeptic persona): approve, 7

**What he said:** A product built on this would be free, quick to open, honest about doubt, and focused on the inside of the building, "the part where even I get it wrong." His worries: the headline promised access-rights routing Pola can't deliver yet; the document never says where routes come from or how often they're checked; it doesn't say "no account"; and answering "I just ask someone" with a quote about bad directions "reads as a dig at the people being asked."

**What we changed:**
- Positioning: the access-rights promise is gone; it now leads with which hallway and which door.
- Exact over approximate: every route shows when it was last checked; who checks it, and how often, is now an open question.
- Light touch: says "no account, and no sign-up screen" before the first instruction.
- Canonical language: "first visits and new buildings" is now said out loud.
- Objection Handling: the "I just ask someone" answer is friendlier: Pola is for when no one is around, or when the person you ask isn't sure.
- Thesis: marked internal; public copy uses the canonical language.

**What we didn't change:** We kept the OISE quote ("tbh I didn't  know oise layout that well either"), but reframed it as something that happens to locals, not as a gotcha.

<details><summary>Raw verdict</summary>

```json
{
  "persona": "persona-owen",
  "artifact": "Pola brand position (2026-10-08 draft)",
  "verdict": "approve",
  "score": 7,
  "headline": "A product built on this would be free, quick to open, honest about doubt, and focused on the inside of the building, which is the part where even I get it wrong. My one worry is that the headline promises routing around who can use which door, before Pola knows that.",
  "must_fix": [],
  "nice_to_have": [
    "Don't put 'the doors you're allowed through' in the positioning statement or on any public page until a building has actually given you that data. Your own open questions say it isn't tested. Lead with 'which hallway, which door' and 'the right room, not just the right building', because you can actually deliver those. The first time it sends a first-year to a badge-only door, it's dead on my floor.",
    "Say where the indoor routes come from and how often they're checked. 'Exact over approximate' is a promise, and the document never says what backs it. Accuracy is the first thing anyone will ask about.",
    "Move 'first visits and new buildings are where Pola matters most' from the open questions into the canonical language. Saying it out loud makes the whole thing more believable to people like me who think getting lost ends by October.",
    "Soften the 'I just ask someone' answer. 'Even locals get it wrong' is true, and I'll admit I've sent someone to the wrong end of a hallway. But it reads as a dig at the people being asked. A friendlier version: 'Use it when there's no one around to ask, or when the person you ask isn't sure.'",
    "The thesis 'the right way through a building depends on who's walking it' is a bit grand for 'room 405 is around the corner to your left.' Keep it internal, and have the copy talk like the tone section does.",
    "Make sure the QR code and calendar link really open straight to directions, with no sign-up screen and no location prompt before the first instruction. The document promises no download but doesn't actually say 'no account.'"
  ],
  "in_character_reaction": "'Campus maps stop at the front door. Pola starts there.' Fine, that's the part I actually get wrong, and no download, a QR code, and admitting when it doesn't know if a door is open is more honesty than most apps manage. I could put the QR code on my floor's whiteboard in September. But the 'doors you're allowed through' pitch is a promise you can't keep yet, and if it sends one first-year into a locked stairwell, they're back knocking on my door and telling their friends. Also, quoting a guy who gave bad directions at me is a little rude. Accurate, but rude.",
  "would_flip_me": "n/a",
  "would_pay": "n/a"
}
```
</details>
