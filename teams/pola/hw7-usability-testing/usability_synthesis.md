# AstraPath usability synthesis

**Team Pola, 2026-11-13.** These are the patterns from our usability sessions, and what we're changing because of them.

**Aha moment:** before walking, the tester sees the route to the room and can say which hallway, stairs, or elevator they would take.  
**Tasks:** join the waitlist, find the room, say the route before walking (aha moment), and get a route without stairs.  
**Sessions:** [session 1](sessions/session_1.md), [session 2](sessions/session_2.md), [session 3](sessions/session_3.md)

**Sessions run:** 3  
**Strangers among them:** 1 (P3)  
**Participants who reached the aha moment:** 3 of 3, all in task 3

| Participant | Who | Building and destination |
|---|---|---|
| P1 | Railway enthusiast in Beijing, someone we know (remote) | Yintai Center, room 3007 |
| P2 | Startup lawyer, someone we just met (on site) | Hudson Yards mall, Chipotle on floor 4 |
| P3 | Columbia first-year, a stranger (on site) | Northwest Corner, room 502 |

## Task results

| Task | P1 | P2 | P3 |
|---|---|---|---|
| 1. Join the waitlist | Yes | Yes | Yes |
| 2. Find the room | Partially: found the route, but didn't reach the room in 10 minutes | Yes, nearly one wrong turn | Yes, after a wrong result and one trip off the site |
| 3. Say the route before walking (aha moment) | Yes | Yes | Yes |
| 4. Route without stairs | Partially: missed the Step-free checkbox at first | Yes | Yes, but couldn't compare it with a stairs route |

## Patterns across sessions

- **Pattern:** Everyone got it at the same moment: when the route named the elevator and the floors before they walked. P3's aha line was the floors the car stops at ("This car goes to 1, 3, and 5"), which is exactly what P1 asked about out loud ("Does this elevator actually stop on the floor I need?").  
  **Sessions:** 3 (P1, P2, P3)
- **Pattern:** Telling AstraPath where you are and where you're going was the hardest step. P1 couldn't tell which starting node matched where they stood, and called it the most confusing part. P3 searched "Northwest Corner 502," got the water fountain on floor 5, and found room 502 only by typing "502" alone. They also called it the most confusing part. Both magic-wand answers were about this step: "figure out exactly where I am" (P1) and "let me type the building and the room and get that room" (P3).  
  **Sessions:** 2 (P1, P3)
- **Pattern:** Step-free wasn't seen as part of the route on screen. P1 overlooked the Step-free checkbox at first, and asked "Does avoiding stairs apply to the entire route?" P3 looked for a switch on the route card, didn't find one, and decided "Step-free is just another example, not a button on the route." P2 found the checkbox right away.  
  **Sessions:** 2 (P1, P3)
- **Pattern:** Reading the route was easy, but following it on foot was harder. P2 understood every step, but asked "How do I know when I've walked far enough?" and nearly made one wrong turn along a long corridor. P1 had the route but didn't reach room 3007 within 10 minutes. The notes don't say where that time went after the route was open.  
  **Sessions:** 2 (P1, P2)
- **Pattern:** People would come back only where AstraPath covers their building. P1: "It would depend on how many buildings are supported." P3: "This page, only if my room was one of the examples."  
  **Sessions:** 2 (P1, P3)

## What surprised us

- **A wrong result looked like a real route.** P3 was about to follow the fountain's stairs: "I was going to follow the stairs on the other card. That one isn't even my room." One confident wrong answer is the failure our brand position warns about most.
- **The tester who had no trouble on screen was the most worried on foot.** P2 explained the whole route correctly, and still said, "I'd still be a little worried about missing a turn."
- **The "Columbia demo" link in the menu took P3 off the site in the middle of task 2.** We had to ask them to come back.
- **P3 wouldn't install anything:** "I'd want it in the browser."

## What we're changing and why

The most important change comes first. Each one should be specific enough to start building today.

### Change 1: Search returns the room you asked for, or says it can't

> **What we observed:** In two of three sessions, the hardest step was telling AstraPath where you are and where you're going. P3 typed "Northwest Corner 502" and got a route to a water fountain, and nearly followed it. P1 couldn't match a starting node to where they stood.
>
> **What we're changing:**
> - Search treats a building name as a filter. "Northwest Corner 502," "NWC 502," and "502" all return room 502 in Northwest Corner. Exact room numbers rank above everything else.
> - When there's no exact match, search says so ("No room 502 in Northwest Corner") and lists the closest rooms. It never falls back to a different place's route.
> - Every route card starts with its destination in large type ("To: Room 502, floor 5"), so a wrong result is obvious before anyone walks.
> - Starting points are named by what you see standing there (the street, the sign, or the shop next to the door), not by node names.
>
> **Why:** All three testers reached the aha moment only after they were looking at the right route. Search is the step right before it, and P3 lost that step to a result that looked right. A route to the wrong place costs more trust than no route at all.

### Change 2: Step-free is a switch on the route you're looking at

> **What we observed:** P1 missed the Step-free checkbox at first, and asked whether it applied to the whole route. P3 looked for a switch on the route card, found Step-free only as a separate example, and couldn't ask for "no stairs" on the route in front of them.
>
> **What we're changing:**
> - A "Step-free" switch goes on every route card, next to the destination. Turning it on changes that same route.
> - With the switch on, the card says "No stairs or escalators on this route" and names each elevator with the floors it stops at.
> - When the fastest route already has no stairs, the card says "This route is already step-free" instead of offering a separate example.
> - The separate "Step-free to 502" example goes away.
>
> **Why:** Two of three testers didn't connect step-free with the route they were reading. Our brand position says step-free is a first-class route, not a setting you have to find. Naming the elevator's floors also answers the question P1 asked out loud, and it's the same detail that gave P3 the aha moment.

### Change 3: Long walking steps end at something you can see

> **What we observed:** P2 read the route correctly but couldn't tell how far to walk before a turn, nearly made one wrong turn, and asked for "a few more reference points along the way." P1 had the route and still didn't reach the room in 10 minutes.
>
> **What we're changing:**
> - Any "keep going straight" step longer than about 30 meters is split into shorter steps. Each one ends at something you can see: a named shop, a door number, restrooms, or an elevator ("Pass Chipotle on your left, then turn right at the restrooms").
> - Each walking step shows its rough distance ("about 40 m").
>
> **Why:** Planning the route worked in every session. Following it is where confidence dropped, and P2's magic wand asked for exactly this. Landmarks we already have on the map can be used for it, without any location tracking.

## What we're not changing (yet)

Things people mentioned that we chose not to act on, and why.

- **Finding where you are automatically** (P1's magic wand). That needs indoor positioning, which is expensive, and P1 said so too. We also cut always-on location from the MVP on purpose, so the user picks the start. Change 1's clearer starting points come first.
- **More buildings, beyond the examples** (P1, P3). Mapping by hand doesn't scale, and automated mapping from floor plans is already on our roadmap.
- **A missing McDonald's on the LG floor of Yintai Center** (P1). This is out-of-date map data in one building. We'll fix the label, but it isn't a product change.
- **The "Columbia demo" link that took P3 off the site.** We saw it once. If it happens in the next sessions, we'll label it with where it goes, or move it out of the menu.
- **Browser only, no install** (P3). The web version already works without an install, so there's nothing to change. We'll keep it that way.
