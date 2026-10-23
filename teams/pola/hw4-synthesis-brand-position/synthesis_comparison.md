# Synthesis comparison

## Part A — Team synthesis draft

### Key patterns across interviews

The interviews show that indoor navigation is a bigger problem in some situations than others. Devesh and the second participant in the POLA interviews have trouble finding rooms in unfamiliar buildings, especially when they are rushing. Maya described taking the wrong hallway in Hamilton and arriving about four minutes late. But Jeanmarie and Jude usually find their way by reading signs, using kiosks, or asking someone. The Barnard senior had a more stressful experience when her family could not find the right exit for a mall pickup. Having elderly grandparents with them made walking around harder. These examples suggest that getting lost matters more when someone has little time or cannot easily keep searching.

Accuracy came up in several interviews. Devesh, Jude, Maya, and the second POLA participant all wanted to know whether they could trust the directions. If the app sends someone the wrong way, they may stop using it. Maya also pointed out that knowing the floor would not have helped much because she was already on the correct floor. She needed to know which hallway to take. The directions would have to be specific enough to help at the moment someone gets confused.

The departure interviews were more mixed. Tristan said elevators and crowded hallways make travel time hard to predict. He once arrived late and missed an attendance quiz, even though his lab ended on time. Steve already leaves early, and that worked on his latest trip. His bigger concern was having nowhere to rest between classes. Shuya usually has no trouble because the classrooms are close together and familiar. These answers suggest that a departure assistant would be useful for some students, but probably not everyone.

In the social interviews, people had different reasons for not staying in touch. Shawniece wanted to message an acquaintance but felt she had no natural reason to do it. Shuya sometimes forgets to text because of work and career preparation. Steve has fewer topics to talk about with an acquaintance, but they still keep in touch by meeting for meals. A photo might give Shawniece a reason to start a conversation. It is less clear whether it would help someone who is simply too busy or forgets to reach out.

Several people liked the ideas, but that does not mean they would use them regularly. Maya would rather open a link than download another app. Tristan does not want more notifications or constant location tracking. Shawniece only wants the tool to access photos she chooses. The interviews suggest that people care about how much effort a tool takes and how much control they have, as well as what it can do.

### Top five exact quotes

Maya: 
"Downloading an app just for one confusing hallway feels like a lot."

Jude:
"I guess I’d wonder how accurate it is. If I have to use the app and then double-check the signs anyway, there’s not much point."

Tristan:
"Another notification. I already ignore most of them. And I'd have to give it my location all the time, which I'm not thrilled about."

Shuya:
"So I think the amount of work you have can make it hard for that too."

Shawniece:
"I didn't want it to be weird, like why am I suddenly messaging you. A photo would've been a reason."

### Contradictions and what they might mean

Some participants see indoor navigation as frustrating, while others find their current methods good enough. Jeanmarie uses directories, and Jude is comfortable asking people. Devesh dislikes asking because he feels embarrassed, while Maya is willing to ask despite some awkwardness. These differences may reflect both building complexity and how comfortable people feel requesting help.

Willingness to pay also differs. The second POLA participant says he would probably pay $10 if the app worked, while Devesh and Jude would try it free but reject paying initially. Maya would not pay for campus navigation now and expects the university or building to provide directions. The Barnard senior reacts enthusiastically, but no purchase is recorded. People may value the tool differently depending on the consequences of getting lost.

Privacy is another difference. The second POLA participant does not mind location collection, while Maya wants access only during navigation and Tristan dislikes constant tracking. In the social interviews, Shawniece wants selected-folder access, whereas Steve worries about unfamiliar recipients after the concept discussion shifts toward random people. These concerns should be addressed separately.

### Surprises

A useful finding is that familiarity can reduce the problem. Maya expects later visits to be easier, and Shuya describes first-week uncertainty that disappeared. This suggests that new students and first-time visitors may have a stronger need than people repeating the same route.

The mall account also broadens the navigation problem. The issue was not simply finding a store; it was coordinating a pickup across exits and parking areas while limiting unnecessary walking for grandparents. This could require different features from a classroom-finding tool.

The social interviews show that enjoying old photos and reconnecting are separate actions. Shawniece already shares resurfaced photos with a close friend, while Shuya looks at old photos without reporting that this leads to a message. A photo suggestion would need to help someone take the next step, rather than only remind them of a memory.

### Overall read on the data

Indoor navigation seems most promising in situations involving unfamiliar buildings, time pressure, or complicated exits. A focused first version could help someone find the correct room or hallway through accurate directions that are easy to open. The interviews do not show that everyone needs another navigation app, and existing signs and people remain effective alternatives.

Departure timing and photo-based reconnection need separate tests. For departure timing, the team should check whether better estimates actually help students facing delays. For social reconnection, it should check whether a relevant photo leads to a message to an acquaintance. Positive reactions are encouraging, but actual use would tell us more about whether the products solve these problems.

## Part B — AI synthesis

### Scope and source inventory

I reviewed all 15 supplied files before identifying themes. They contain **12 topic-specific interview accounts from 10 apparent participants**, not 15 independent interviews. Steve and Shuya each discussed two concepts. Notes, snapshots, and the transcript within Maya's document are multiple representations of the same account.

The material explores three related but distinct problem spaces: indoor navigation, campus departure timing, and social reconnection through photos. Findings are separated by topic rather than combined into a general claim about students needing an assistant.

| ID | Participant and topic | Source files |
| --- | --- | --- |
| N1 | Jeanmarie, mother of two; indoor/offline navigation | `Interviews.pdf`, first participant |
| N2 | Unnamed Barnard senior studying economics and math; indoor/offline navigation | `Interviews.pdf`, second participant |
| N3 | Devesh; indoor navigation | `POLA interviews.pdf`, interview 1 |
| N4 | Unnamed roommate's friend; indoor navigation | `POLA interviews.pdf`, interview 2 |
| N5 | Jude; indoor navigation | `POLA interviews.pdf`, interview 3 |
| N6 | Maya, first-year Columbia student; indoor navigation | `campus_navigation_interview_yining_ma.docx`, transcript, notes, and snapshot |
| D1 | Tristan, sophomore; departure timing | `campus_notes.pdf`, `campus_snapshot.pdf` |
| D2 | Steve, Boston University sophomore; departure timing | `campus-notes.md`, `campus-snapshot.md` |
| D3 | Shuya, Columbia graduate student; departure timing | `campus-notes(1).md`, `campus-snapshot(1).md` |
| S1 | Shawniece, junior; social reconnection | `social_notes.pdf`, `social_snapshot.pdf` |
| S2 | Steve; social reconnection | `social-note.md`, `social-snapshot.md` |
| S3 | Shuya; social reconnection | `social-notes.md`, `social-snapshot(1).md` |

### 1. Patterns and strength of evidence

#### Indoor navigation

**A. Confusion matters most when unfamiliarity meets time pressure or difficult coordination.**

- **N6, Maya:** A detailed recent event supports situational stress: a wrong hallway in Hamilton, backtracking, and an estimated four-minute late arrival. She explicitly qualifies the impact as temporary and manageable. This is concrete evidence of occasional inconvenience, not persistent severe pain.
- **N4, unnamed roommate's friend:** Reports arriving late and wanting precise directions when rushed. The frustration is clear in the words, but no dated incident or frequency is established, and the questions suggest stress and lateness before the response.
- **N3, Devesh:** Describes wandering in unfamiliar buildings and feeling uncomfortable asking for help. Evidence supports uncertainty and social discomfort; severity and frequency are unknown.
- **N2, Barnard senior:** The strongest reported consequence is roughly 30 minutes coordinating a mall pickup with elderly grandparents who could not walk long distances. The notes describe substantial distress. This is a different task from finding a classroom: coordinating people across exits and parking areas.

The evidence favors studying specific difficult journeys rather than assuming every indoor trip is painful. N2's stronger consequences deserve attention even though they come from one participant.

**B. Signs, directories, room numbers, and people are substantial existing competitors.**

- **N1, Jeanmarie:** Treats mall navigation as a small problem because kiosks and physical cues work. Her indoor emotional intensity is low in the snapshot.
- **N5, Jude:** Asking someone usually works and is not particularly annoying. His need for a replacement is weak.
- **N6, Maya:** Her current approach usually works quickly and requires no setup, although signs were easy to miss while rushed.
- **N3 and N4:** Both use signs and people, but describe dissatisfaction or embarrassment. Asking for help is therefore not equally costly for everyone.

A new tool must improve on a working physical solution, not merely offer another map.

**C. Accurate, specific directions are a prerequisite for trust.**

**N3, N4, N5, and N6** independently state accuracy concerns in their recorded responses. N3 describes losing trust if an instruction points to a nonexistent hallway. N5 questions value if he must double-check the signs. N6 distinguishes useful turn-level guidance from an instruction to reach a floor she already found, and raises locked entrances and outdated information. The concern is explicit and consequential, although it is prospective rather than based on trying this product.

**N1** also describes losing confidence in existing phone maps; this concerns current map failure, not a tested reaction to the team's tool. Keep those two kinds of evidence separate.

**D. Low setup effort and permission control can matter more than a free price.**

**N6** gives the clearest evidence: she would try a schedule link or entrance QR code but probably would not download a free app immediately. She would allow location while navigating, not continuously. **N4**, in contrast, expresses little concern about location collection. This is a meaningful difference, not a universal privacy preference.

Only N6 directly establishes a preference for links over installation; other participants' answers do not justify generalizing that preference to everyone.

#### Departure timing

**E. The three campus accounts describe different tasks, not one shared reminder problem.**

- **D1, Tristan:** His specific failure involved an elevator delay after leaving a lab on time. The raw notes record lateness and a missed attendance quiz. This supports uncertainty in travel duration. It does not show that an earlier notification could have let him leave the lab sooner. He expresses low interest for familiar routes and concerns about notifications and constant location access.
- **D2, Steve:** His independently raised difficulty is nowhere to rest during an hour-long gap. His 30-minute departure rule worked on the last trip. His question about unexpected tram delays is a substantive feasibility concern, but repeated departure failures are not established.
- **D3, Shuya:** Nearby classrooms and familiarity make current trips easy. A prompted late-class example still ended on time. First-week room finding is a separate orientation issue. Positive comments about students with distant classes concern a hypothetical audience rather than personal demand.

The evidence for a general departure assistant is mixed and weaker than a simple count of favorable reactions would suggest.

#### Social reconnection

**F. Contact tools exist; the obstacles are conversational context, remembering, and time.**

- **S1, Shawniece:** Describes a recent unsent message and a lack of a natural reason to initiate contact. The notes report hesitation a couple of times a month, with mild emotional impact.
- **S2, Steve:** Limited shared interests restrict conversation topics, but meals already provide a successful reason to message and meet. His latest invitation succeeded. This supports limited conversation breadth, not inability to maintain contact.
- **S3, Shuya:** Independently describes forgetting to text and workload interfering with relationships. No specific failed attempt or frequency count is established. The obstacle is attention and scheduling, rather than Shawniece's fear of a message feeling strange.

These mechanisms should remain separate even though all three involve existing messaging tools.

**G. Remembering a photo is not the same as reconnecting with an acquaintance.**

**S1** already sends resurfaced photos to a close friend, not the acquaintance she hesitates to contact. **S3** revisited study-abroad photos and remembered people, but no subsequent message is reported. Both describe a plausible photo-based use case after hearing the concept. Neither provides observed evidence that the proposed tool causes an acquaintance conversation to restart.

**S2** provides no photo-driven reconnection example. His concept reaction is additionally complicated by a shift toward unfamiliar recipients.

#### Across concepts: evidence quality and demand

**H. Positive reactions and hypothetical purchases do not establish adoption.**

**N2** expresses strong enthusiasm and says she will buy; **N4** says he would probably pay $10 if it worked. Neither account records a completed purchase or trial. **N3 and N5** reject an initial $10 charge; **N6** rejects paying for campus use now and is hesitant even about a free installation.

No actual spending on the proposed products is recorded. Several participants explicitly report no problem-specific spending, while some were not asked. **D2's taxi spending is a transport workaround**, not payment for a departure assistant. Follow-up consent and possible introductions are useful next steps, but do not demonstrate demand; some commitments remain ambiguous or uncompleted.

### 2. Five telling exact quotes

Each quotation below was checked against the supplied source named alongside it. None is taken from a passage labeled approximate paraphrase.

1. **Maya, N6 — time pressure changes the importance of confusion.**
   > If I’d had more time, I probably wouldn’t even remember it.
   Source: `campus_navigation_interview_yining_ma.docx`, Section A, answer about the hardest part of the trip. Also reproduced in Section C.

2. **Devesh, N3 — incorrect guidance destroys trust.**
   > My first thought is accuracy. If it tells me to turn left and there’s actually no hallway there, I’m going to stop trusting it.
   Source: `POLA interviews.pdf`, interview 1, Solution Signal.

3. **Tristan, D1 — travel duration varies even on a familiar campus.**
   > Honestly, guessing how long it'll take. Sometimes it's six minutes, sometimes it's twelve if the elevator's slow or the hallway's packed.
   Source: `campus_notes.pdf`, question 2.

4. **Shawniece, S1 — initiating a conversation lacks a natural reason.**
   > Honestly I don't have a reason to message. We're not in the same class anymore, so there's nothing to say, and a random 'hey' feels like a lot.
   Source: `social_notes.pdf`, question 2.

5. **Steve, S2 — an existing solution already works.**
   > And I think it actually works well because we're still in touch.
   Source: `social-note.md`, Meals and messages are an adequate current solution; attributed to 209.20–216.80 seconds.

### 3. Contradictions and possible explanations

**Indoor maps: unnecessary versus valuable.** N1 considers kiosks adequate, while N2 reports severe trouble coordinating a pickup in a large mall. Do not pick a winner. Directories may solve finding a shop without solving alignment between a pedestrian, a driver, an exit, and a parking loop. Venue complexity and companions' mobility also differ.

**Asking for help: effective versus uncomfortable.** N5 readily asks; N3 feels embarrassed; N6 finds interruption slightly awkward but will still ask. Different comfort levels may explain different willingness to substitute an app for a person.

**Payment: no need versus conditional willingness.** N3 and N5 reject $10, N6 rejects it for current campus use, and N4 conditionally accepts it. N2 expresses purchase enthusiasm without a price or transaction. Differences in perceived consequences might explain these responses; the records cannot establish a viable price.

**Location access: acceptable versus restricted.** N4 is unconcerned, while N6 wants access to end after navigation and D1 objects to constant tracking. Usage-only permission and continuous monitoring are different requests, so this is not a clean comparison of identical consent conditions.

**Departure assistance: real delay versus already workable routine.** D1 missed a quiz after an elevator delay; D2's latest trip succeeded; D3 has nearby classrooms. Different constraints and distances may explain the contrast. The records do not show whether a departure assistant would improve any of those outcomes.

**Social difficulty: lost contact versus successful contact.** S1 hesitates to send; S3 forgets amid work; S2 maintains weekly meetings. S2's activity routine may provide the shared context missing for S1, while S3's obstacle could persist even with a suitable photo.

**Social safety: privacy of photos versus safety of strangers.** S1 wants a selected folder rather than whole-camera-roll access. S2 questions unknown recipients after the interviewer accepts a random-people interpretation. S3 states no objection after clarification. These are different concerns and differently understood concepts, not interchangeable privacy findings.

### 4. Surprises and findings that resist the main patterns

- **Familiarity can reduce repeat need.** N6 says subsequent visits are easier; D3's first-week uncertainty faded. A useful orientation experience may have limited repeat use for a stable schedule.
- **Accessibility appears through companions' constraints.** N2's grandparents intensified the cost of wandering. This suggests interviewing people with mobility constraints directly; it does not establish a validated accessibility market.
- **A departure interview uncovered a resting-space problem.** D2's main concern was what to do between classes, which a timing reminder would not itself solve.
- **A reminder cannot necessarily change departure time.** D1 left when the lab ended. Better navigation and more accurate time estimates may help differently; neither should be presumed to eliminate elevator waits.
- **No download can be more attractive than a free download.** N6's access preference challenges a focus on price alone.
- **A social concept changed during the interview.** S2's safety objection followed a shift from acquaintances to random recipients, weakening conclusions about the intended design.
- **Some snapshot claims exceed their raw evidence.** D1's snapshot mentions a prior transit app failing indoors, a failed prior workaround, and a repeated incident. The supplied raw notes do not document that app failure or multiple late incidents. They record an offered introduction and follow-up consent, not a completed referral. These stronger snapshot claims are excluded from this synthesis.
- **A broad market conclusion exceeds one interview.** N1's snapshot labels defense, search-and-rescue, and other offline settings a green signal. Her account supports investigating rural/outdoor navigation difficulties, but does not validate demand in those specialist markets.

### 5. Provisional segments

These are research hypotheses, not representative market sizes or finished personas. Participants can belong to more than one segment.

| Segment | Supporting accounts | Distinct need or constraint |
| --- | --- | --- |
| Unfamiliar-building users under time pressure | N3, N4, N6; D3's first-week account | Correct hallway or entrance with minimal searching; repeat need may fade |
| Users adequately served by signs and people | N1, N5; parts of N6 | A replacement must beat quick, familiar, no-setup methods |
| Complex-venue pickup and mobility-sensitive groups | N2 | Clear exits and coordination across indoor/outdoor spaces; severe consequences in one account |
| Travelers dealing with uncertain duration | D1, D2, with different delay sources | Elevator/crowd variability versus tram/traffic uncertainty; intervention remains untested |
| Familiar-route students with little current timing need | D3; D1 on known routes | Low value from routine reminders or installation |
| Acquaintances needing a socially natural opener | S1; S2's limited-topic account | Shared context; S2 already obtains it through meals |
| Busy people who forget to maintain contact | S3 | A timely, low-effort prompt; a photo may not solve lack of time |
| People already maintaining contact through activities | S2 | A working routine creates a high bar for an additional tool |

### 6. Overall interpretation and unresolved questions

The most concrete indoor evidence concerns unfamiliar hallway choices and one complex mall pickup. Accuracy, current building information, and easy access deserve focused testing. These records do not establish broad paid demand for a standalone campus app. Departure timing is a separate hypothesis with mixed support: one account documents a meaningful consequence, but two others show working routines or adjacent problems.

Social reconnection has at least two distinct candidate mechanisms—needing an opener and forgetting to reach out—but photos have not been shown to change acquaintance-contact behavior. Favorable comments should lead to a behavioral test rather than be treated as validation.

Useful next tests are: an accurate link-based room-finding task in an unfamiliar building; a recorded comparison of estimated versus actual travel time, including elevator waits; and a voluntary, selected-photo suggestion to a known acquaintance, observing whether it results in a message and response. These are proposed tests, not interview findings. Clarify recipient selection and permissions before testing social reactions. Interview direct users of the highest-stakes scenarios before extending market claims.

## Part C — Comparison
The AI pointed out something missing from Part A: a departure reminder might not have prevented Tristan’s lateness because he already left as soon as his lab ended. It also found differences between his snapshot and raw notes, including an unsupported claim about a previous transit app failing indoors. These details made the conclusions about departure assistance more cautious.

Part A put more emphasis on practical barriers, such as downloading another app, unwanted notifications, and control over photos. The AI covered these too, so the difference was mainly emphasis rather than something it completely missed. All five quotes in Part B match the supplied notes. The AI also kept separate problems apart, such as Shawniece needing a reason to message and Shuya forgetting to text.
