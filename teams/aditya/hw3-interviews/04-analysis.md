# Team Aditya — HW3 interview analysis

We documented ten interviews across our two ideas: a group chat planning bot and a student subleasing/rental platform. We found relevant problems in both spaces, but the interviews do not yet validate either full product or paid demand. Our decision is to **narrow both ideas** before building.

## Idea 1: Group chat bot

### Five snapshots side by side

| Participant | Problem and current workaround | Cost or commitment | Signal |
|---|---|---|---|
| Aditya | Avoids the uncertainty of new places by returning to roughly five familiar spots and relying on friends. | Weekly recurrence; effort rather than money. No product reaction or follow-up recorded. | Yellow |
| Pranav | Worries a new place will waste money; relies on friends and a shared Google Maps list. | Time and effort; described a disappointing bar visit. No payment for a planning tool recorded. | Yellow |
| Navaneeth | Finding a suitable new place can be frustrating; keeps a shared Google Doc and Notes list. | Manual research and comparison. No paid tool or follow-up recorded. | Yellow |
| Kimberly | Cannot easily see friends’ availability; reports that about half of plans happen. Proposes a time and place in chat. | No planning-tool spending recorded. Agreed to referrals and a follow-up. | Green, conditional on calendar integration |
| Natalia | Coordinating busy schedules and getting everyone to attend is difficult. Uses messages and advance planning. | No planning-tool spending recorded. Agreed to follow up; reluctant to link her calendar. | Green with a privacy qualification |

### Patterns in the interviews

**Choosing a place with confidence: 3 of 5.** Aditya, Pranav, and Navaneeth described uncertainty or frustration around trying new places and already rely on recommendations or saved lists. These three interviews support a discovery problem. They do not independently establish that an AI inside a group chat is the preferred solution. Their notes are paraphrased, so we cannot claim three matching verbatim quotes.

**Coordinating schedules and attendance: 2 of 5.** Kimberly and Natalia directly described this problem. Kimberly said, “I guess always hard to find a good time because you don't know what's on people's calendars.” Natalia said, “I think getting, like, everyone to show up is a really hard thing.” Scheduling availability and getting people to commit are related, but a calendar integration would not necessarily solve attendance.

The current alternatives are familiar places, recommendations from friends, Google Maps lists, Google Docs, Notes, and messages. These cost time and effort; the notes do not document purchases of a dedicated planning product. Kimberly’s referral agreement and both students’ follow-up agreements are useful next steps, but they are not evidence of payment or sustained use.

### What changed our thinking

Our initial concept combined recommendations, availability, and booking. The interviews suggest that these are separate jobs. The strongest repeated pattern is reducing the risk of choosing a disappointing place. Scheduling has two clear accounts, with conflicting preferences about automation: Kimberly wants calendar synchronization, while Natalia prefers manual entry or screenshots over broad calendar access.

Unlabeled notes also mention privacy, reliability, Google/ChatGPT, Beli, and menu scanning. We retained these in the raw notes but excluded them from participant-level counts because the speaker is unrecorded.

### Decision: Narrow

We would narrow the next test to helping students and recent graduates choose a nearby place they trust, using their preferences and existing friend recommendations. The 3-of-5 pattern supports investigating this narrower problem; it does not validate the complete group chat bot.

The clearest attributed quote illustrating the separate scheduling opportunity is Kimberly’s: “I guess we should plan better, like, using calendars and stuff.” For the discovery decision itself, our strongest evidence is the three concrete accounts above, not an invented exact quote.

Next, we would test a short, manually curated list against each participant’s current method for a real outing. We would observe whether they choose a place, use the recommendation, and return for another occasion. We would separately follow up with Kimberly and Natalia about a real planning attempt before deciding whether calendar coordination belongs in the product.

## Idea 2: Student subleasing and renting

### Five snapshots side by side

| Participant | Problem and current workaround | Cost or commitment | Signal |
|---|---|---|---|
| Ruby | Concerned about scams, cleanliness, affordability, and community fit; relies on campus housing and family/community networks. | Limited direct subleasing experience; no search-tool spending recorded. Agreed to follow up. | Yellow |
| Emma | Described inaccurate information, weak filters, and difficult tour scheduling across rental platforms. | About 30 tours in one week; declined a hypothetical $10 fee in her current situation. | Green for the problem; yellow for adoption/payment |
| Tina | Found a sublease through her cousin and did not search elsewhere. | Little search friction; no willingness to pay recorded. | Red |
| Marcus | Suspicious listings and unanswered messages made finding a room difficult; eventually used a school housing group. | No search-platform payment; hypothetical interest in paying for trustworthy listings and testing an early version. | Green for problem relevance; paid demand unproven |
| Jasmine | Distrusted strangers online; found a summer sublease through a mutual connection. | No search payment; unlikely to pay just to browse. Future trial and sharing interest are conditional. | Yellow/Green |

### Patterns in the interviews

**Actual online housing-search friction: 3 of 5.** Emma, Marcus, and Jasmine described personal search difficulties. Their problems overlap but differ: Emma emphasized listing accuracy and tour coordination; Marcus emphasized trustworthy listings and responses; Jasmine emphasized trust before sending money. This meets a broad 3-of-5 problem pattern, not proof that all three need the same feature.

**Trust or authenticity concerns: 4 of 5.** Ruby, Emma, Marcus, and Jasmine raised these concerns. Ruby’s account is primarily concern rather than a completed difficult sublease search, so we do not count it as a fourth demonstrated search failure.

**Personal networks as an effective alternative: 2 of 5.** Tina’s cousin and Jasmine’s mutual connection solved their housing needs. Tina is a useful negative case: “No. I didn’t look at a single other place.” A new platform must offer value to people who lack that trusted connection, rather than assuming every student needs another listing site.

Quotes supporting the main patterns:

- Search burden — Emma: “We visited, like, 30 places, and we messaged probably way more than that.”
- Trust and responsiveness — Marcus: “I messaged probably like twenty people and half of them never answered. The other half I wasn’t even sure were real.”
- Trust through connections — Jasmine: “I’d rather rent from somebody who knows somebody I know than just send money to a random person online.”

Current alternatives include rental websites, Facebook groups, school housing groups, Instagram, friends, and family. The clearest demonstrated cost is time and effort. No interview documents a purchase of our proposed service. Emma declined $10 in her situation, Jasmine would probably not pay to browse, and Marcus’s willingness to pay a small amount remains hypothetical.

### What changed our thinking

An all-in-one platform may be too broad. Trust can matter more than the number of listings, while a trusted personal connection can remove the problem almost entirely. Emma also shows that ordinary apartment hunting and student subleasing are not identical workflows. Her scheduling and filtering needs should not automatically become requirements for a subleasing product.

### Decision: Narrow

We would focus further research on students actively seeking a short-term room or sublease without a trusted personal lead. The next test would explore whether school affiliation, mutual connections, clear listing details, and responsive contacts reduce uncertainty enough to change their behavior. School-email verification would establish affiliation, not guarantee that a listing or transaction is safe.

Jasmine’s quote about preferring someone connected to her network most clearly supports this direction. Marcus adds a concrete case where unreliable contacts made the search harder. We would test a small set of relevant listings with active searchers, observing whether they contact a lister and arrange a viewing. We would test payment separately rather than treating enthusiasm as willingness to pay.

## Limits of these findings

This is a small convenience sample with mixed fit for the original ideas. Some raw notes are brief, and several snapshots contain more detail than the raw-note sections. Quotes reproduced here come from the supplied snapshots; complete transcripts were not provided. The first three group-bot interviews have no recorded dates, format, or emotional-intensity scores. The source describes several problems as unprompted, but the available notes do not let us independently verify question order. Snapshot completion within one hour is also unverified. Negative cases, unknowns, and conditional interest are retained in the submission.

Source: [Team interview kit](https://docs.google.com/document/d/1gKwrN3CtTT7g4PLf3lj8xOvRKPI0GiT-2lFnasES840/edit).
