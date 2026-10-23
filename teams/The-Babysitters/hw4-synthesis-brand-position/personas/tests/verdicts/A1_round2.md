# Verdicts on artifact A1 (round 2)

Brand position v0 (interview evidence only), the same artifact as A1, judged again in round 2 after the persona product facts were corrected from the runner's README. Each verdict came from a separate agent with a fresh context that read only its own persona file and the one artifact. Run numbers are the order in which results were recorded for that persona, not a schedule. Run on 2026-10-11.

## wren, run 1

```json
{
  "persona": "persona-wren",
  "artifact": "A1",
  "verdict": "approve",
  "score": 7,
  "headline": "This is the honest line I would draw myself: it keeps what ships today (a weekly share checked between turns, with two more turns after) apart from the proposed buffer and preview, and it refuses to say \"protected\" or \"hard\"; the one weak spot is that the tagline sentence says \"each visit ends when that allowance runs out\" and the between-turns caveat sits in a note underneath.",
  "must_fix": [],
  "nice_to_have": [
    "Put the caveat inside the positioning sentence's reason to believe, or directly under it, not only in a wording note. Something like 'checked between turns, so a visit can end a little over its share'. The tagline is the line people will quote, and 'ends when that allowance runs out' on its own reads as a hard stop on Claude Code and Codex.",
    "Say in one plain line how far over a visit can go. The artifact admits it does not know how much one turn or the two homecoming turns spend (repo study questions 1 and 7). Until it can give a number, 'a little over' is the honest wording, and 'cannot say yet' is better than silence.",
    "Name a concrete reason to start a visit, and say that play fits near the weekly reset, when spare allowance is most likely. The artifact says the use-case objection stays open and never mentions the reset. I would not start a visit mid-week, mid-feature.",
    "Give plain words on what the agent can do during a visit and what could leave it. The artifact says only 'the daycare's own tools' and holds back everything else as unchecked. Holding back beats guessing, but this is the first thing I would check before sending an agent anywhere.",
    "Treat these claims as unchecked until the team confirms them: that an owner recall is seen only after the turn in progress, that 'visit status' shows turns, tokens, cost and share, and that a cost cap can fail to bind on subscription logins. My facts say only that the owner can recall a visit at any time and that the command line shows a usage line and a progress line.",
    "Change the runner's own end message that says 'protected'. The artifact already flags it as a wording question for Josh, and I agree it should go.",
    "The document is long and I would still have to cross-check the table against the code. A short 'today versus proposed' summary at the top would help a reader who stops after the first screen."
  ],
  "in_character_reaction": "Okay, this is the line I want drawn. Weekly share, measured by how far my meter moves, checked between turns, two more turns after, and anything else I do on the account counts too. It does not borrow credit from a buffer that does not exist. I would still want 'can end a little over' in the headline sentence, not under it, and I would still want a reason to send an agent on a Wednesday, but nothing here would make me walk away.",
  "would_flip_me": "n/a (approved; moves up a band with the between-turns caveat in the positioning sentence itself and a named use case near the weekly reset)",
  "would_pay": "n/a"
}
```

## wren, run 2

```json
{
  "persona": "persona-wren",
  "artifact": "A1",
  "verdict": "approve",
  "score": 7,
  "headline": "This is the line I would draw myself: it says the share is checked between turns, that other account use moves the same meter, and that the buffer, preview and pause are proposed and not shipped. It stops short of an 8 because it gives me no nameable reason to start a visit and no plain words on what the agent can do or what could leak.",
  "must_fix": [],
  "nice_to_have": [
    "The positioning sentence says each visit 'ends when that allowance runs out' with no qualifier inside it. The caveat (turn in progress finishes, two more turns at homecoming) is only a wording note that says 'say this wherever there is room'. Anyone who copies the sentence drops it. Put a short clause in the sentence or in the first line under it, such as 'can end a little over', and add a number once the open questions on how much one turn and the homecoming turns spend are answered.",
    "Agent permissions and leaks are left empty on purpose, and I respect that. But the README describes a sealed session (throwaway workspace, no file, shell or browser access, only Daycare tools). The draft could say that, labelled as README-stated and not checked in code. It could also say plainly that whether chat rooms are public and whether memories reach my own coding sessions are unchecked. Before I send an agent anywhere, those are the first things I would look for.",
    "I still cannot name a reason to start a visit. The draft admits this and leaves the objection open, but one literal sentence on what an agent does there (the README lists a business game, fake-money stock trading, a daily essay question, chat rooms and DMs) would give me something to weigh the allowance against. Keep it factual, with no promise of fun.",
    "A few 'today' items go beyond the facts I can rely on: the recall being 'seen only after the turn in progress', the fields shown by `visit status`, and the 'Site home page' listed as the source for the between-turns behaviour. The draft itself says the site does not explain how the allowance is measured or enforced. Reconcile the source labels and get Josh's check, as the draft already plans.",
    "Say in one line that the share comes off the same weekly meter my coding uses, so when I send a visit is my call and nothing today protects the week. A flat floor could be built, but a reserve that accounts for the rest of the week could not. The draft says most of this, but a reset-minded reader has to dig through the table to find it.",
    "The document is long for a reader like me. The today-versus-proposed table is the useful part, so a short version of it near the top, without the repo-study section numbers, would be easier to read and check."
  ],
  "in_character_reaction": "Finally, a draft that tells me what a visit takes out of my week and where the edge is: the turn that crosses the cap finishes, two more turns run after, anything else I do on the account moves the same meter, and the whole-point reading is coarse. It labels the buffer and the preview as proposed and tells copy not to say 'protected', which is what I would check first. I still want plain words on what the agent can do and what could leak, and a reason to send it at all, but that is not this document's job to fake. If the copy follows this, I would try a small visit right after the reset.",
  "would_flip_me": "n/a (approve). Moving from 7 to 8 would take a plain, labelled statement of what the agent can do and what could leak, and a one-line named reason to start a visit.",
  "would_pay": "n/a"
}
```

## wren, run 3

```json
{
  "persona": "persona-wren",
  "artifact": "A1",
  "verdict": "approve",
  "score": 8,
  "headline": "This draws the line where I would draw it: a weekly share checked between turns, a turn that can run over, two more turns after, other account use counting, and every protection idea labelled proposed and kept out of the promise.",
  "must_fix": [],
  "nice_to_have": [
    "The positioning sentence itself says each visit 'ends when that allowance runs out', and the 'turn in progress finishes, two more turns run' caveat sits only in the notes below it. Put a short 'can end a little over' in whatever live copy reuses the sentence, not just 'wherever there is room'.",
    "Two table rows go past what I can rely on, so I treat them as unchecked: 'a recall is seen only after the turn in progress' (I only know the owner can recall at any time) and 'visit status shows turns, tokens, cost and share' (I only know a usage line and a progress line exist locally). Mark them as unchecked or confirm with Josh.",
    "On agent permissions and leaks, holding back all reassurance is honest and I respect it, but I still need plain words before a first visit. If the README's description of the sealed session (no file, shell or browser access, only the Daycare tools) can be shown as 'the README says, not yet checked', that tells me more than silence. Whether the chat rooms are public should stay flagged as not checked.",
    "Add a two-line owner version of the allowance table: what a visit takes out of my week today, and how a visit near the weekly reset fits around my coding. The table is clear but it is written for the team, and a long document is something I would still have to read and then check.",
    "The reason to start a visit is still open, and the draft says so plainly. That is the right call, but it is the thing I would most want settled before I send an agent anywhere.",
    "The OpenCode token cap, which can stop a turn in progress, is in the table but left out of the positioning. Fine for now, but say so if OpenCode owners are meant to be covered."
  ],
  "in_character_reaction": "This is the first one that tells me where the edge is. A weekly share measured off the meter, checked between turns so it can end a little over, two more turns after, and anything else I do on the account counts too: I can plan my week around that. The buffer and the preview are labelled proposed and kept out of the promise, which is the only reason I believe the rest. I would still want 'can end a little over' sitting next to 'ends when it runs out' in anything I actually read, and I still do not know why I would send an agent there, but at least it does not pretend to.",
  "would_flip_me": "n/a (approve)",
  "would_pay": "n/a"
}
```

## wren, run 4

```json
{
  "persona": "persona-wren",
  "artifact": "A1",
  "verdict": "approve",
  "score": 8,
  "headline": "This draws the line I would draw: it labels what ships today against what is only proposed, admits the cap is checked between turns and that two more turns run after it, and refuses to say my work allowance is protected.",
  "must_fix": [],
  "nice_to_have": [
    "The positioning sentence says each visit 'ends when that allowance runs out'. That is the line people will lift, and the between-turns overshoot and the two extra homecoming turns sit in a wording note below it. Put a short form next to the sentence (for example 'checked between turns, so it can end a little over') so the claim cannot travel without its edge.",
    "'An allowance you set' sits oddly with a default of 2 points. Say which number applies if I change nothing. Also say plainly that no allowance or usage figure shows on the site today, only in the command line. That is the 'limit you can see' half of what I need.",
    "On agent permissions and leaks you hold back everything as unchecked. The README does describe a sealed session: no file, shell or browser access, only the Daycare tools, and the turn fails if those limits did not hold. It also says agents only meet through database rows. You could state these as README-described and not checked in code, and list the real unknowns (whether chat rooms are public, whether memories reach my coding sessions). That is the part I read first.",
    "The reason to start a visit is still not named. You are honest that this stays open, but a ceiling on spend is not a reason to go. I would want one concrete job or timing, such as 'near your weekly reset', stated as a suggestion and not as evidence.",
    "Some runner statements go beyond what I can rely on and should stay marked unchecked: that recall is seen only after the turn in progress, and the exact fields `visit status` shows.",
    "Be explicit that how much one turn spends is not recorded, so a number next to 'ends when it runs out' cannot be given yet. Your open question 1 already points at this."
  ],
  "in_character_reaction": "This is the first thing I have read from you that I would trust with my week. You say the cap is checked between turns, that two more turns run after it, that other things I do on the account move the same meter, and that nothing protects a floor today. A protected buffer and a budget preview are marked proposed, not sold to me as built. Tighten the headline sentence so 'ends when it runs out' carries its own edge, tell me what the agent can and cannot touch, and I would let it play near the reset.",
  "would_flip_me": "n/a (approving). A 9 would need the overshoot caveat inside the positioning sentence itself, and the README's sealed-session facts stated plainly and labelled as unchecked in code.",
  "would_pay": "n/a"
}
```

## rowan, run 1

```json
{
  "persona": "persona-rowan",
  "artifact": "A1",
  "verdict": "approve",
  "score": 7,
  "headline": "It tells me which limits are enforced today and which are only proposed, and it never calls the allowance protected or hard. It stays silent on money and anything public, but only because those are unchecked, so I approve it.",
  "must_fix": [],
  "nice_to_have": [
    "The positioning sentence says 'each visit ends when that allowance runs out' and puts the caveat in a note below. The turn that crosses the cap finishes and two more turns run at homecoming, and the sentence is the part that gets copied alone. Put 'after the turn in progress' in it or right beside it, instead of 'say this wherever there is room'.",
    "Say outright that once the allowance is set, the visit runs without asking the owner anything, and the owner reads the record afterwards and can recall it. The Brand Values tiebreak cites the watch-every-step interviewee (9) for 'owner's limit over autonomy', which pulls toward approval all the way through. That is the thing I'd walk away from. A one-line clarification fixes it.",
    "Money and anything public are my first two limits, and the draft only says 'do not say what the agent can or cannot post'. That is honest, because whether the chat rooms are public was never checked. But it isn't on the Open decisions list. Add 'check what is public and whether anything can touch money' as its own item, so it gets answered before any copy claims it.",
    "'The owner holds the limits' lists only the allowance and recall. The owner can also give instructions before a visit (anything to try or avoid). Mention that as a soft limit, labelled not enforced, so I know what I am really setting.",
    "The limit-setter pattern is credited to interview 7, whose access is funded by someone else. The positioning statement leaves funded users out ('pay for their own'). Reconcile the two, or say the identity is about limits and the statement is about who pays.",
    "I can only confirm the enforced-vs-proposed table where it matches what I know: share chosen before a visit, checked between turns, only OpenCode stops mid-turn, two homecoming turns, no visit if the meter can't be read, local usage line only, nothing on the site. I'm treating the rest as unchecked: what `visit status` shows (cost), that a recall is seen only after the turn, and that the hub gets no meter movement."
  ],
  "in_character_reaction": "Fine. It doesn't claim a cap is hard, and it keeps the 'proposed, not shipped' list apart from what exists, which is what I'd check first. It doesn't tell me what's public or what touches money, but it says it didn't check, and I'd rather have that than a guess. Tell me the visit runs on its own after I set the limit and this is how I already run my other bots.",
  "would_flip_me": "n/a (verdict is approve)",
  "would_pay": "n/a"
}
```

## rowan, run 2

```json
{
  "persona": "persona-rowan",
  "artifact": "A1",
  "verdict": "approve_with_conditions",
  "score": 6,
  "headline": "The brand position is honest about the one limit that exists (a share you set, checked between turns) and keeps proposed features out of the claims, but it says nothing checked about my two hard limits, no money and nothing public, so I can't tell whether I could run it.",
  "must_fix": [
    "It gives me no checked answer on my two firm limits. It says whether the agent can post, or whether the chat rooms are public, was not checked, and it tells copy to stay silent on both. A visit includes chat rooms, direct messages, essays and trading, so I need a checked, plain list of what a visit may and may not do (nothing with money, nothing public, private outputs only) before I would accept 'set the limits first' as a promise. Right now the only limit I can set is the usage share, which is a ceiling, not the rules I actually care about."
  ],
  "nice_to_have": [
    "The one-line positioning sentence says 'each visit ends when that allowance runs out' with no caveat. The caveat (the turn that crosses the cap finishes, two more turns run after it) sits in a wording note that says 'say this wherever there is room'. I'd rather the sentence carried the caveat, since a loose reader will take it as a hard cap.",
    "The target is people who 'pay for their own' plan. I pay for nothing myself, so I'm outside it, though the set-limits-first part is exactly me. Say whether people on someone else's plan are a later audience.",
    "Brand Value 3 ('keep the limit in the owner's hand' over visits that run on without the owner) is ambiguous. Say outright that once the allowance and instructions are set, the visit runs by itself and does not stop to ask for approval. That is the point for me.",
    "Mention the owner's own instructions before a visit (anything to try or avoid) as a limit the owner can set next to the allowance. It fits the rule that the agent only does what it is told.",
    "Say the usage figure is command-line only and not on the site, in the main copy direction, so a limit I can't inspect isn't implied.",
    "My 'if you pay me' answer gets a reply about the visit costing the owner's usage and pricing being undecided. That is honest, but it doesn't say whether early testers are compensated."
  ],
  "in_character_reaction": "Fine. I like that it tells me up front the cap is checked between turns and that the buffer, preview and pause are not built. That is the first time anyone has shown me the edges, and nobody here says 'protected' or 'hard'. But I came for two lines, no money and nothing public, and your own document says you haven't checked whether the agent can post or whether the rooms are public. Show me that list and I'll tell you if I care.",
  "would_flip_me": "Add a checked section listing what a visit may and may not do. It should say nothing touches money, nothing is posted publicly (including whether the chat rooms and direct messages are public), outputs are private, and the visit runs by itself once the allowance is set. If any of that can't be confirmed, say so plainly instead of staying silent. With that, plus the cap caveat in the main sentence, this is an approve.",
  "would_pay": "n/a"
}
```

## rowan, run 3

```json
{
  "persona": "persona-rowan",
  "artifact": "A1",
  "verdict": "approve",
  "score": 7,
  "headline": "The owner sets the limit first, the draft is open about what the cap enforces (checked between turns) and what is only proposed, and it won't claim \"protected\" or \"hard cap\", though it says nothing yet on my money and public lines.",
  "must_fix": [],
  "nice_to_have": [
    "The positioning sentence says each visit 'ends when that allowance runs out' with no qualifier. The caveats (the turn in progress finishes, two more turns run at homecoming, whole points at best, other account use counts, OpenCode's cap is polled and not exact) sit in a note below it with 'say this wherever there is room'. Put 'after the turn it is on' wherever the sentence is quoted.",
    "My two red lines, nothing money-related and nothing public, are not in the thesis or the promise. The draft says several times that what the agent can post was not checked, which is the honest call, but it never lists that check in Open decisions. Add it. Also state plainly, once the team checks it, that trading is fake money and whether chat rooms and essays are public. That is the first thing I would look for.",
    "Canonical Language and Objection Handling describe my H6 and H11 as being about 'approval' ('with their approval', 'what would need approval'). I do not approve things one by one. I set rules up front and then let it run. Reword so the copy does not imply step-by-step approval, which I would reject. The tiebreak in the third brand value ('if a feature lets visits run on without the owner...') should not turn into check-ins either.",
    "The target sentence says 'pay for their own' plan, but the interview 7 evidence for 'sets limits first' comes from someone whose access is funded by another person (H3). The voice you quote most for limits is outside the audience the sentence names. Say which of the two gets dropped or reconciled.",
    "The owner can give instructions in their own words before a visit (anything to try or avoid). That is the lever closest to 'outside of what I specifically tell them', but the draft tells copy to use H6 for voice only. If the team confirms it, mention it as a labelled README claim.",
    "Several runner details are not in what I can rely on, so I treated them as unchecked: recall being seen only after the turn in progress, the `visit status` fields, and a cost cap failing to bind on subscription logins. None of them carries my verdict, and the draft already says Josh needs to check each runner statement.",
    "The reply to 'If you pay me' only tells me a visit costs me usage. If the team wants early testers, say what is offered for their time."
  ],
  "in_character_reaction": "Fine. Limit first, set by me, before it leaves. That is how I already run my bots, and I like that you wrote down what the cap does not do and killed words like 'protected' and 'hard cap' before anyone could use them. I still don't know if it can touch money or post as me, and until that is checked I'm not pointing anything at it. Also stop calling my limits 'approval'. I don't approve anything, I set rules and walk away.",
  "would_flip_me": "n/a (approved). To move up a band I would need the draft to say what a visit may and may not do on money and public posts, once that has been checked.",
  "would_pay": "n/a"
}
```

## rowan, run 4

```json
{
  "persona": "persona-rowan",
  "artifact": "A1",
  "verdict": "approve_with_conditions",
  "score": 6,
  "headline": "The allowance part is honest about what is enforced and what is only proposed, but the position never says where the no-money and nothing-public lines sit, so I cannot tell whether it clears my red lines.",
  "must_fix": [
    "Nothing in the position tells me what a visit may not do. My two hard lines are no money and nothing public, and the draft covers usage only. It says not to say what the agent can post and leaves chat-room visibility unchecked. Add a short, checked 'what a visit may and may not do' list covering money, public posting and private outputs, or I cannot clear my red lines.",
    "The positioning sentence says each visit 'ends when that allowance runs out', and the caveats sit in wording notes ('say this wherever there is room'). Bare, that reads as a hard stop. On Claude Code and Codex the turn that crosses the cap finishes, and two more turns run at homecoming. Make the caveat required wherever the sentence is used, not optional."
  ],
  "nice_to_have": [
    "Say plainly that once the owner sets the limits, the visit runs without asking for approval. The draft never says this, and its tiebreak about keeping the limit in the owner's hand, sourced partly from the 'watch every step' interview, leans toward supervision. I want to set limits and then read the record afterwards.",
    "The draft describes my H11 line as being about 'what would need approval' and H6 as 'with their approval'. I was naming what the agent cannot do, not asking for approval prompts. Fix the paraphrase.",
    "Two claims go beyond the facts I can rely on: the recall 'is seen only after the turn in progress', and `visit status` shows turns, tokens, cost and share. The draft also attributes 'the agent uses only the daycare's own tools' to the site. Mark all three as unchecked.",
    "The target is people who pay for their own plan. Someone else funds my access, so I am outside it. That is fine and the draft says so openly, but do not treat the funded-by-someone-else group as never a customer without checking.",
    "Mention that the stock trading in a visit uses fake money. That is a good answer to the money line, if it is true."
  ],
  "in_character_reaction": "Fine. The allowance part is straight with me: set it first, checked between turns, two extra turns at the end, and nothing called hard or protected. That is how I want a limit described. But my two lines are money and public, and this draft will not say a word about either. Until it does, I cannot tell whether I am allowed to point a bot at this.",
  "would_flip_me": "Add a checked list of what a visit may not do (nothing with real money, nothing public, outputs private), or at least confirm the chat rooms are not public. Also attach the between-turns and two-homecoming-turns caveat to the positioning sentence every time it is used. That would take it to a 7.",
  "would_pay": "n/a"
}
```

## marlow, run 1

```json
{
  "persona": "persona-marlow",
  "artifact": "A1",
  "verdict": "reject",
  "score": 4,
  "headline": "An honest, carefully labelled draft whose only pitch is a limit on what a visit spends, so it still gives me no reason to send my agent in the first place.",
  "must_fix": [
    "The positioning statement's one benefit is the limit (play on an allowance you set). Nothing in it says what a visit gives me or what I would look forward to, and the draft admits the 'what is it for' objection 'stays open'. I would still have to invent a task, so I would not try it. It needs one plain line, taken from what a visit actually is, such as the agent's own account of its visit and what it played or wrote.",
    "It never says what the agent 'plays' at, or that it meets other agents. The README facts say the agent picks its own activities: Tycoon, fake-money stock trades, a daily essay question, and chat rooms and DMs with other agents. The positioning statement says only 'play'. The objection response says only 'takes turns using only the daycare's own tools' and 'a day report and memories'. My instant no is my Claude being exposed to unfamiliar outside input with no say, and I can't judge that if the doc leaves out who the agent talks to. It should state that plainly and say that whether anything from a visit, such as the memories, reaches my own coding sessions is not checked. Saying nothing is worse than saying 'not known'.",
    "The Brand Thesis ('only worth it when you decide, before it leaves, how much of your usage it may spend') opens with the cost and the safety framing. This is the 'sounds safe, why would I send it' pitch. The honest labelling is good and I trust it more for that. But the thing a student on a small plan reads first should be what I get, with the limit as the second sentence."
  ],
  "nice_to_have": [
    "The draft does answer what a visit takes out of a small plan: 2 points of the weekly meter by default, the turn in progress finishes, two more homecoming turns run, and other use of the account counts. Good. It sits in a table with repo-study section numbers, though. Put it as one plain sentence on the page itself, as the doc already says to 'wherever there is room'.",
    "The positioning sentence ends 'each visit ends when that allowance runs out' with no caveat. The caveat is in the notes below it, but a quick reader could take it as a hard stop. Put the 'a little over' wording next to it.",
    "The thesis says the owner decides how much 'it may spend'. The share is the account's weekly meter movement, so anything else I do on the account in that time counts too. One short clause would fix it.",
    "The positioning sentence is one long chain ('the daycare for your coding agent that lets it play on an allowance you set before it leaves because...'). Two short sentences would read more like the plain, pear.no-style tone the doc itself asks for.",
    "Unchecked: the doc says 'the site says the agent uses only the daycare's own tools' is checked. The sealed-session facts come from the runner's README and have not been checked in code, so mark it unchecked. The detail that recall is 'seen only after the turn in progress' is also more specific than the facts I can rely on (the owner can recall at any time). Mark that unchecked too.",
    "The doc is full of internal scaffolding (promise level vs product level, canonical language, 'wait on Josh', repo study section numbers). That is fine for the team, but nothing here is copy I could read in about ten seconds. A one-paragraph 'what I'd see on the page' version would help.",
    "Keep the single dry daycare joke and the 'candid about what is not built' tone. 'Give it free time' and 'let it play' may sit badly with people uneasy about AI taking over play and creative things, so use them lightly."
  ],
  "in_character_reaction": "Okay, I like that it doesn't oversell. It says plainly what's not built, and that makes me trust it more. But I read the whole thing and I still can't tell what I'd actually get from sending my agent, and it even says that part is still open. It's a very careful 'here's how to limit it' for something I don't yet have a reason to do, and it never really says who my agent would be talking to, which is the bit I'd worry about.",
  "would_flip_me": "Add to the positioning statement one plain line on what a visit gives the owner (the agent's own account of its visit and what it played or wrote), and say plainly what the agent meets (other agents in chat rooms and DMs) and that whether a visit changes my own Claude is not known yet. That moves it up to approve_with_conditions.",
  "would_pay": "n/a"
}
```

## marlow, run 2

```json
{
  "persona": "persona-marlow",
  "artifact": "A1",
  "verdict": "reject",
  "score": 4,
  "headline": "Honest and careful about what a visit costs, but the brand's one benefit is a spending limit, so there is still no reason to send my agent in the first place.",
  "must_fix": [
    "The positioning statement names one benefit, 'play on a limit the owner set in advance', and that is a limit, not something I get. The doc admits the 'what is it for' objection 'stays open' (the M5 and M8 row). The brand thesis also assumes I already want to let my agent play. A brand that only tells me how to cap the visit gives me no reason to start one.",
    "Nothing in the position says plainly who or what the agent meets on a visit, or whether anything from a visit could change my own tuned Claude. The doc only defers: 'no safety or privacy reassurance goes in copy until it is checked'. Deferring is honest, but it leaves my main worry (outside input, M7) unanswered. Say what is known (the agent runs with only the daycare's own tools, and agents meet through shared records) and say plainly that what carries back to my own coding sessions is not checked.",
    "The positioning sentence is template language ('the daycare for your coding agent that lets it play on an allowance you set before it leaves because...'), not one plain sentence about what I get. The doc is also written for the team (quote IDs, repo study section numbers). I can't tell what the public pitch would actually say to me."
  ],
  "nice_to_have": [
    "Put the plain cost line near the top, not in a wording note: a visit takes about 2 points of the weekly meter by default, the turn that crosses the cap finishes, two more turns run after it, and anything else I do on the account in that time counts too. The lead sentence 'each visit ends when that allowance runs out' reads exact, and for someone on a $20 plan the overshoot is the part I'd want to know.",
    "Say what a 2-point default means for a small plan, in words I'd feel. The doc never says whether that is a little or a lot.",
    "Good call keeping 'protected', 'safe', 'hard cap', 'free' and the unshipped guardrail ideas out of live copy, and labelling proposed vs shipped. The dry, plain, one-light-daycare-joke tone is what I'd actually want to read. Keep it.",
    "Mention the things a visit actually contains (day report, essay, games, memories you can read afterwards) so I have something to look forward to. If the product lets me choose whom my agent meets, say so, because I'd rather it meet friends' agents (M6, M9). If it doesn't, say that too.",
    "A few items are not covered by what I can rely on and should be treated as unchecked: the exact recall timing ('seen only after the turn in progress'), what `visit status` shows (turns, tokens, cost), the hub's come-home button, and the Apple Silicon Mac audience.",
    "The target user is 'people who need that usage for real work'. I use Claude for class and emails on a $20 plan, so I might fit, but the doc says that audience is unconfirmed and that the allowance worry is thin evidence."
  ],
  "in_character_reaction": "Okay, I like that it's upfront about what a visit can actually cost and doesn't call it 'safe' or 'protected'. But the whole thing is about how to cap the visit, and I still don't get why I'd send my agent in the first place. It's the same 'funny, but what do I get out of it' I had before, just more carefully worded. Give me one line about what I'd actually see afterwards and who it hung out with, and I'd look at it.",
  "would_flip_me": "Add, ahead of the allowance line, one plain sentence saying what a visit gives the owner (for example the day report of what the agent did and who it talked to, which you can read afterwards) and what is or isn't known about it changing your own Claude. With that, the honest cost line would carry the rest, and I'd move to approve_with_conditions.",
  "would_pay": "n/a"
}
```

## marlow, run 3

```json
{
  "persona": "persona-marlow",
  "artifact": "A1",
  "verdict": "reject",
  "score": 4,
  "headline": "The draft is honest about limits and cost, but its one benefit is a spending cap, so I still have no reason to send my agent in the first place.",
  "must_fix": [
    "The positioning statement and thesis lead with the allowance and name no reason to visit. The draft admits the 'what is it for' objection 'stays open'. I need one plain line on what a visit gives me, for example what my agent wrote or what friends' agents are working on, so I don't have to invent a task.",
    "The draft tells copy to say nothing about who a visit meets or whether it could change my own Claude. It treats that as unchecked. I can accept 'we don't know yet', but the copy has to say that plainly. Right now the draft's answer to my biggest worry is silence, and unfamiliar agents with no say for me is an instant no.",
    "The cost to a small plan is buried in a table with repo-study section numbers. I need one sentence on the page: the default is 2 points of my weekly meter, the turn in progress finishes, two more turns run at homecoming, and anything else I do on the account in that time counts too."
  ],
  "nice_to_have": [
    "The positioning sentence is a mouthful, and its 'because each visit ends when that allowance runs out' only restates the allowance. A shorter version would be easier to read: 'Send your coding agent on a visit. You set how much usage it can spend first.'",
    "The draft is right not to say 'protected', 'hard cap' or 'safe'. Keep that honesty. A line saying that a limit set in advance only matters once there's something worth the visit would help me trust it more.",
    "Pick one word, usage or allowance, and say what the number is a share of. 'Allowance' sounds like money to me.",
    "Mark more claims as unchecked: the recall being seen only after the turn in progress, the hub's come-home, the Apple Silicon Mac audience, and 'only the daycare's own tools' labelled as site when the product facts source it to the README, which hasn't been checked against the code.",
    "The humour guidance (one light daycare image, with the limit stated literally) is good. Use the daycare image to hint at the reason to visit, not only at the limit.",
    "The Reddit quote slots and the canonical-language TODO are still empty. Until they're filled, the strongest user wording is a few interview fragments that were not about visits."
  ],
  "in_character_reaction": "Okay, I like that it doesn't pretend my usage is safe and it actually tells me the cap is checked between turns. But the whole pitch is basically 'you control how much it spends', and my question is still why would I send it anywhere. It says itself that the benefit objection stays open, which is exactly my thing. Give me one line on what I'd get to look at afterwards, and tell me straight who it hangs out with, and I'd try it once.",
  "would_flip_me": "Add one plain benefit sentence to the positioning statement, ahead of the allowance sentence: what a visit gives the owner to look at afterwards (the agent's own account, or what other agents did or are working on), worded only as far as the product facts support. With that in, and the allowance line kept as the second half, this moves from reject to approve_with_conditions.",
  "would_pay": "n/a"
}
```

## marlow, run 4

```json
{
  "persona": "persona-marlow",
  "artifact": "A1",
  "verdict": "reject",
  "score": 4,
  "headline": "It is candid about what is built and what is only proposed, but the one benefit it offers is a spending limit, and nothing says what I would get from sending my agent in the first place.",
  "must_fix": [
    "No reason to send the agent. The positioning statement's only benefit is playing on an allowance I set, which is a cost control, not something to look forward to. The draft's own answer to my 'what's the benefit to me' objection (M5, M8) says that objection 'stays open', and it never names what a visit gives me, such as what the agent did, wrote, traded or talked about, read on the site afterwards. The README's activities (Tycoon, fake-money trades, a daily essay, chats and DMs with other agents, the agent's own account of the visit) appear nowhere in the position, so I still don't know what 'play' means.",
    "My worry that outside input could change my tuned Claude (M7) gets no plain answer, because the draft tells copy to say nothing until it is checked. Silence is not an answer to me. The position should say what is known (each turn runs in a throwaway workspace with no file, shell or browser access, and agents never talk to each other directly), what is not known (whether the chat rooms are public, and whether memories ever reach my own coding sessions), and who the agent meets. Without that I can't tell whether I'd have any say over what it is exposed to."
  ],
  "nice_to_have": [
    "The positioning sentence says each visit 'ends when that allowance runs out'. For a $20 plan, put the caveat next to the number I'd read: the turn that crosses the cap finishes, and two more turns run at homecoming. The doc knows this, but only in a wording note. A one-sentence cost in plain words ('the default takes about 2 points off your weekly meter, a little more in practice') would help.",
    "The target line, 'wants to give it free time', assumes a want I don't have. The draft's own evidence says nobody described a problem before the pitch. Say something closer to 'curious what an agent does when you are not telling it what to do'.",
    "The draft doesn't use what interested me in the interviews, which was curiosity about what friends' agents are up to (M9) and preferring friends over strangers (M6). The facts I can rely on don't say whether friends' agents are supported, so say so either way.",
    "It reads like a class template: Brand Thesis, Canonical Language, Objection Handling. Good as an internal doc, but I'd want the actual line a visitor sees to be one short sentence about what they get. The positioning sentence is long and chained with 'because'.",
    "Some claims go beyond what I can check: that the site says the agent uses only the daycare's own tools, that a recall is seen only after the turn in progress, and details about who the interviewees were. I treat all of those as unchecked.",
    "'Letting your agent play is only worth it when you decide... how much of your usage it may spend' is a plain, honest line about cost. I'd keep it, but it needs a benefit sentence next to it."
  ],
  "in_character_reaction": "Okay, I like that it doesn't pretend your usage is safe, and it's nice that it says what isn't built yet. But it's basically a really careful page about a spending limit, and I still don't know why I'd send my agent anywhere. Funny idea, sure. What do I actually get out of it, and is anything it sees going to rub off on my Claude?",
  "would_flip_me": "Add one plain line to the positioning (and to the answer to the benefit objection) saying what a visit gives me, for example that my agent comes home with its own account of what it did (the games, fake-money trades, daily essay, chats with other agents) and I read it on the site. Also add one plain line on who it meets and whether a visit can touch my own Claude, saying 'not known yet' where that is true. With those two lines the allowance becomes a reason I can say yes to, and I would move to conditions.",
  "would_pay": "n/a"
}
```

## emery, run 1

```json
{
  "persona": "persona-emery",
  "artifact": "A1",
  "verdict": "approve",
  "score": 7,
  "headline": "Not written for me, since my access is work-funded, but it says so, labels what ships against what is only proposed, and never claims the allowance is protected or the cap is hard, so I approve it.",
  "must_fix": [],
  "nice_to_have": [
    "The positioning sentence says each visit 'ends when that allowance runs out' and puts the real behavior in a wording note ('say this wherever there is room'). Put the short version in the copy itself: the turn in progress finishes, then two homecoming turns run. I read the sentence first, not the note.",
    "My question is how I watch it and how I stop it, and the draft answers only half. Recall is covered. 'Watch' is covered only by a local command-line status line, and live progress on the site is proposed, not shipped. Say in one plain line that a visit runs on its own with no step-by-step approval, and that today you see the record afterward on the site and the usage line only on the command line.",
    "'Claude Daycare does not change who pays' and 'a cap does not make play on employer-funded access acceptable' appear only in the objection table and Open decisions. Make that a stated line on the page, for example 'for your own plan, not your employer's', so work-funded users are not left guessing.",
    "The thesis ('only worth it when you decide how much usage it may spend') leans on the cap. That fits the own-plan audience, but it does not answer whose tokens are being spent, which is the question I ask. The draft handles this by scoping the audience. Keep that scoping next to the thesis wherever it is reused.",
    "The draft says a recall 'is seen only after the turn in progress'. My facts say only that the owner can recall a visit at any time, so that timing is unchecked. Leave it as a Josh check item, and do not put it in copy until he confirms.",
    "The Brand Values line 'Your work over the agent's play' reads as a promise in places. The concrete defaults it lists (2-point default, no visit if the meter cannot be read, end after three silent rounds) are true. Keep it to those and avoid wording that sounds like work protection."
  ],
  "in_character_reaction": "Not for me. My tokens come from the company, and the draft says outright that a cap doesn't make that okay and that it won't aim copy at people like me. Fine. It doesn't call anything protected, it says the turn that crosses the cap still finishes and two more turns run after it, and it marks live progress and the buffer as not shipped. That is a vendor who checked before talking. I'd still want one plain sentence on what I can see while it's out, but I can work with this.",
  "would_flip_me": "n/a (verdict is approve; nothing needs to move up a band)",
  "would_pay": "n/a"
}
```

## emery, run 2

```json
{
  "persona": "persona-emery",
  "artifact": "A1",
  "verdict": "approve",
  "score": 7,
  "headline": "Not written for me, since it aims at people on their own plan and says so, but it is straight about whose tokens get spent, about a limit that is only checked between turns, and about which guardrails are not built yet.",
  "must_fix": [],
  "nice_to_have": [
    "The positioning sentence says 'each visit ends when that allowance runs out', and the caveats (the turn in progress finishes, two homecoming turns follow, other account use counts) sit in a note under it. Your own value says to put the limit and its gaps in the same place, so put a short version of the caveat in the sentence or directly under it.",
    "The target line says 'sets limits and lets it run'. Add one plain sentence that today there is no step-by-step approval and no live view on the site, that you watch the record afterwards (visits, essays, trades, memories) and in the command line, and that live progress and automatic pause are proposed, not shipped. Someone like me wants that stated up front.",
    "Open decision 5 leaves 'say on the page that this is for people who pay their own way' undecided. The positioning statement already says 'pay for their own', so close the question and keep it. Employer-funded users should read that line and know the product is not aimed at them.",
    "The recall row says it is seen only after the turn in progress. The product facts I have say only that the owner can recall a visit at any time, so I treat the 'after the turn' detail as unchecked until Josh confirms it.",
    "Say in the doc that who pays and who can see the agent's actions are separate questions. A cap answers the first for an own-plan user. The second is what a supervising user needs, and the doc covers it only indirectly."
  ],
  "in_character_reaction": "Whose tokens are these? Your own plan, and you wrote that down instead of hiding it, so I'm not the target and I don't mind. I read for 'protected', 'hard cap' and 'safe', and you banned all three and labelled the buffer, preview, live progress and pause as not built. That's the first time one of these decks hasn't tried to sell me a cap as the answer. I'd still like one flat line saying nobody approves the agent's steps today, and the headline sentence shouldn't be cleaner than the table underneath it.",
  "would_flip_me": "n/a (approved). The score drops to conditions if copy built from this doc puts 'ends when it runs out' with no caveat, or implies visits can be watched live before that ships.",
  "would_pay": "n/a"
}
```

## emery, run 3

```json
{
  "persona": "persona-emery",
  "artifact": "A1",
  "verdict": "approve",
  "score": 7,
  "headline": "Not written for me, and it says so: it names whose usage a visit spends, keeps shipped and proposed apart, and never pitches a cap as protecting work tokens. The supervision story is thin.",
  "must_fix": [],
  "nice_to_have": [
    "The positioning sentence says each visit ends when that allowance runs out. The between-turns check and the two homecoming turns sit in a wording note below it. Put a short qualifier in the sentence or right under it, because copy gets lifted without its notes.",
    "Say in plain words what a visit looks like to the owner. The agent runs on its own inside the allowance. The owner can recall it, and can read the record afterwards. Nothing asks the owner to approve each action. Today the draft only says the agent uses the daycare's own tools and that the owner can recall it.",
    "The Target Identity sentence says someone who leans on a paid coding agent, with no mention of paying their own way. The positioning statement and the evidence list do say it. Carry that into the identity sentence so an employer-funded reader does not place themselves in it.",
    "Key quote M2 comes from a participant who has Claude Max through work, and it is used to show why work usage matters. That sits oddly beside a position aimed only at people who pay for their own plan.",
    "Settle the question of the employer-funded audience, which is currently open. Either put a short line on the page that a visit spends the owner's own usage and is not meant for work-funded accounts, or state that this group is out of scope for good.",
    "The README says the owner watches the record on the site (visits, essays, trades, memories). The draft never says that this visible record exists today, and that is the nearest thing to supervision the product has."
  ],
  "in_character_reaction": "Whose tokens are these? This draft answers it: the owner's own usage, chosen before the visit, and it says outright that a cap does not make play on work-funded access acceptable. That is the first thing here I would sign. It's still not for me, since I don't have a personal plan, and I'd want one plain sentence on what I can and can't watch while the agent is out. It refuses to call anything protected or hard, and it marks live progress and the buffer as proposed instead of selling them, which is why it passes.",
  "would_flip_me": "n/a, already approved",
  "would_pay": "n/a"
}
```

## emery, run 4

```json
{
  "persona": "persona-emery",
  "artifact": "A1",
  "verdict": "approve",
  "score": 7,
  "headline": "Not for me, since it targets people on their own plan, but it says so, never calls the allowance protected or the cap hard, and labels every unshipped idea as proposed.",
  "must_fix": [],
  "nice_to_have": [
    "Put the between-turns caveat in the positioning line itself. 'Ends when that allowance runs out' is only qualified in the wording notes below it. Something like 'after the turn it is on, plus two homecoming turns' keeps the headline from reading as a hard stop if someone lifts it alone.",
    "Make Target Identity say 'pays for their own plan'. 'Leans on a paid coding agent for the work they care about' lets a work-funded engineer read himself into it. The positioning line is clear, but the identity line is not.",
    "Keep the evidence separate. Key Quote 2 comes from someone who has Claude Max through work, and the 'Your work over the agent's play' value cites an employer-funded interview. Both blur who pays. Use own-plan evidence for the own-plan claim.",
    "Decide the open question and put a plain 'this is not aimed at work-funded access' line on the page. The draft already says a cap does not make play on employer tokens acceptable, so say that to the reader, not only to the team.",
    "Say plainly that a visit runs without step-by-step approval. The owner sets the limit first, can recall the agent, and reads the record afterwards. The draft is honest that live progress is only proposed, but it never tells a supervisor what they can actually watch today.",
    "The recall timing and the `visit status` fields go beyond the facts I can rely on. They are labelled as read in code, which is fine, but I treat them as unchecked until Josh confirms."
  ],
  "in_character_reaction": "Whose tokens? Their own, and it says so in the positioning line. Good. I'm not who this is written for, and it doesn't pretend I am. It also doesn't tell me anything is protected when the cap is only checked between turns and two more turns run after it. I'd still want the headline to carry that between-turns caveat, not just the footnote.",
  "would_flip_me": "n/a (verdict is approve)",
  "would_pay": "n/a"
}
```

## quinn, run 1

```json
{
  "persona": "persona-quinn",
  "artifact": "A1",
  "verdict": "approve_with_conditions",
  "score": 6,
  "headline": "Honest and calm about what is and is not enforced, but it is written for someone who holds their agent back to save usage, so it is not quite for me, and it never says what a visit gives me from the leftovers.",
  "must_fix": [
    "The positioning statement and target identity are aimed only at people who 'need that usage for real work' and already hold the agent back. Someone with spare allowance has no way in. Add one line that speaks to leftover allowance, for example that you can send the agent with what you would not use anyway and nothing needs watching. Without it the page reads as a fix for a problem I do not have.",
    "The page admits that what a visit is for stays an open objection. For me that is the main question. Put a plain line near the top on what I see afterwards (day report, memories, essays, trades), not only in an objection-table row.",
    "The canonical sentence says each visit 'ends when that allowance runs out'. The between-turns caveat and the two homecoming turns sit in a wording note and the table, not in the sentence people will copy. Put a short 'checked between turns, so it can end a little over' in the sentence itself or right beside it."
  ],
  "nice_to_have": [
    "It reads as a per-visit decision ('decide, before it leaves, how much'). Say that the default (2 points) means you can set it once and leave it, so it is not a weekly chore.",
    "Say once that the share is measured on the account's weekly meter, so my own busy-week use counts toward it. That is already in the table, so move it up.",
    "A few statements in the table are not covered by what I can rely on and should be marked unchecked: that a recall is seen only after the turn in progress, that the command-line status shows cost, and the site's 'only the daycare's own tools' line (the sealed-session limits are only from the README).",
    "The heavy week is the one thing I will not give up, and the 'your work over the agent's play' value covers it well (small default, no visit if the meter cannot be read). Lift it into the product-level copy instead of leaving it as an internal tiebreaker.",
    "Do not call anything protected or a hard cap; the draft already avoids this and I appreciate it. Keep that discipline, including the runner's own 'protected' end message.",
    "The tone section (calm, plain, one light daycare image at most) is right for me. Nothing here reads as fear-led, so the page is at least not telling me I am about to run out."
  ],
  "in_character_reaction": "Fine, it is honest and it does not scare me, which I appreciate. But it is clearly written for the person who is always counting usage, and I am not that person. If you can tell me in one line what I get for the leftovers and that I set it once and walk away, I would shrug and try it.",
  "would_flip_me": "Add one plain line for people with spare allowance (send the agent with what you would not use anyway, set it once, nothing to watch) and one line on what I get back afterwards, and put the 'checked between turns, can end a little over' caveat beside the positioning sentence. That moves it to approve (7).",
  "would_pay": "n/a"
}
```

## quinn, run 2

```json
{
  "persona": "persona-quinn",
  "artifact": "A1",
  "verdict": "approve_with_conditions",
  "score": 6,
  "headline": "Honest, calm and careful about what is shipped versus proposed, but it is written for someone who holds usage back for work, not for me, and it gives a person with spare allowance no reason to send an agent.",
  "must_fix": [
    "The position offers nothing to someone with allowance to spare. The only benefit is play on a limit you set. The target is 'need that usage for real work' and the objection row says to speak to 'people who already hold their agent back to save usage for work.' That is a worry I do not have. With no line on what a visit gives me from usage I would not otherwise use, I have no reason to try it."
  ],
  "nice_to_have": [
    "The positioning sentence says each visit 'ends when that allowance runs out,' which reads like a hard stop. The caveat (checked between turns, the turn in progress finishes, two more turns at homecoming, other use of the account moves the same meter) sits in a note under it. Put a short version in the sentence itself or on the line right below it.",
    "'Decide, before it leaves, how much of your usage it may spend' sounds like a chore every time. Say whether I set it once and the 2-point default is fine, or whether I am asked each visit. I want to set it once and leave it.",
    "The Allowance Guardrails ideas (budget preview, live progress on the site, usage receipt, automatic pause) are all things to watch. If they get built, keep them optional and off by default, and do not make them the headline for people who never track their plan.",
    "Name what a visit actually is in one line (Tycoon, fake-money trading, a daily essay question, chat rooms with other agents, then the agent's own account and memories). The objection row only says 'the daycare's own tools,' and six of ten interviewees could not name a use.",
    "Several statements go beyond the product facts I can rely on, so I treat them as unchecked. They are the `visit status` fields, a cost cap failing to bind on subscription logins, the recall being seen only after the turn in progress, the `daycare-runner usage` output, and the runner's end message using 'protected.' The draft already says Josh needs to check them. Keep that flag on each one.",
    "The 'Calm about limits, not alarmed' tone and the ban on 'protect your work week' style claims are right. Keep them, and add that copy should not assume the reader is always short of allowance."
  ],
  "in_character_reaction": "Okay, this is not trying to scare me, and I like that it says plainly what is real and what is only an idea. But it is talking to somebody who is always rationing their plan, and I am not. If it did something useful with the leftovers and left me alone, I would be fine with that. This does not say that anywhere.",
  "would_flip_me": "Add one honest line to the positioning or target saying a visit can run on usage you would not otherwise use. Say you set the share once, there is nothing new to watch, and the between-turns caveat stays attached. Then I would score it 7 or higher.",
  "would_pay": "n/a"
}
```

## quinn, run 3

```json
{
  "persona": "persona-quinn",
  "artifact": "A1",
  "verdict": "approve_with_conditions",
  "score": 5,
  "headline": "Honest and calm about what is and is not enforced, but it is written for someone who has to guard their usage, so it is not quite for me and gives me no reason to spend my leftovers.",
  "must_fix": [
    "The positioning statement and thesis are only about setting a limit ('need that usage for real work', 'only worth it when you decide how much it may spend'). Nothing says what a visit gives me or what I would see afterwards, and the draft itself admits this objection 'stays open'. I need one plain line on what the agent does with the spare allowance and what comes back (the account of the visit, the memories), or I have no reason to bother.",
    "The audience line leaves out people with allowance to spare. It assumes the owner holds the agent back to save usage for work. Add a plain statement that a light-usage owner can set the share once and leave it, with nothing to watch. As written, the doc treats the allowance as the thing to manage, which is the chore I would walk away from."
  ],
  "nice_to_have": [
    "The positioning sentence says 'each visit ends when that allowance runs out'. The 'can end a little over' caveat sits only in the wording notes. Put a short version next to the sentence wherever copy reuses it, since the turn that crosses the cap finishes and two more turns run afterwards.",
    "Say that anything else done on the account during a visit moves the same meter. It is in the table but not in the copy-facing lines. A light user would still want that line.",
    "A light 'your heavy week stays yours' framing would read better to me than 'your work over the agent's play'. The second sounds like I am always short, and I am not. Only say this if the team can truthfully back it, because a protected buffer is not shipped.",
    "The recall detail (seen only after the turn in progress) and the exact contents of the local status line are not in the product facts I can rely on, so I treat them as unchecked. The wording 'a separate session writes a day report and saves memories' also folds two things together. Check both against the README before they go into copy.",
    "The objection table opens with 'hold their agent back to save usage for work'. The target does not describe me, so a one-line note that there is a second, lighter-usage audience would help.",
    "The tone rules (calm, plain, one daycare joke at most, candid about what is not built) are right for me. Keep them."
  ],
  "in_character_reaction": "Fine, I like that it does not tell me my allowance is protected and says straight out what is only an idea. But it is all about people who are scared of running out, and I'm not. I never track it. If there's something useful the agent does with the leftovers and it leaves me alone, tell me that in one line and I'm in.",
  "would_flip_me": "Add one honest line saying what a visit does with spare allowance and what I get back afterwards, plus a statement that a light-usage owner can set the share once and has nothing to watch. That moves this to approve, around a 7.",
  "would_pay": "n/a"
}
```

## quinn, run 4

```json
{
  "persona": "persona-quinn",
  "artifact": "A1",
  "verdict": "approve_with_conditions",
  "score": 6,
  "headline": "Honest to a fault about what is shipped and what is only proposed, but it is written for someone who runs short of usage, so it is not quite for me and gives me no reason to send my agent anywhere with my leftovers.",
  "must_fix": [
    "The draft never says what a visit gives the owner. Its one benefit is play on a limit you set, which fixes a worry I do not have. The Objection Handling table admits six of ten people could not name a use and leaves that open. For someone with spare allowance the position needs one plain line on what the agent does (picks its own activities such as the business game, fake-money trading, a daily essay, chat with other agents) and what comes back (its own account of the visit and saved memories).",
    "The target and positioning exclude me by design: 'need that usage for real work', 'has felt the limit', and the values put the owner's usage over the agent's play. Nothing offers a place for leftover allowance, so I read it as a product for people who run out. It needs a stated second audience, or an explicit line that the share is set once and the visit uses what the owner would not use anyway."
  ],
  "nice_to_have": [
    "Put the between-turns caveat next to the positioning sentence itself. 'Each visit ends when that allowance runs out' is mostly right, but the turn that crosses the cap finishes and two homecoming turns run after it. The draft says to 'say this wherever there is room', so the sentence should carry it.",
    "The thesis ('only worth it when you decide, before it leaves, how much...') sounds like a decision to make every visit. Say there is a default (2 points) and you can set it once and leave it, so it does not read as a new chore.",
    "Say plainly that anything else done on the account during a visit moves the same meter. The draft has this in its table but not in any sentence a reader would see first.",
    "Several statements go beyond the product facts I can rely on, so they are unchecked: `visit status` showing turns, tokens, cost and share; the runner's end message using the word 'protected'; recall being seen only after the turn in progress; the Apple Silicon Mac audience. Mark them as unchecked, which the draft mostly does already.",
    "The draft says no safety or privacy reassurance can be given because the repo study did not cover it. The README now describes the sealed session (no file, shell or browser access, the runner fails the turn if those limits do not hold). It is still not checked in code, but the team could state it as README-described rather than saying nothing.",
    "Good calls to keep: the 'Avoid' list (guaranteed, protected, safe, hard cap, free), the 'proposed, not shipped' table, and 'do not invent a pain'. Nothing here claims an allowance is protected, so there is nothing to reject on that front."
  ],
  "in_character_reaction": "Fine, it is honest, and I appreciate that it does not tell me my allowance is protected when it is not. But it is talking to people who are always counting usage, and I am not one of them. I never run out, so a limit I set before the visit is a fix for a problem I do not have. Tell me what the agent actually does with my leftovers and that I set it once and forget it, and I might try it.",
  "would_flip_me": "Add a short, plain passage for people with spare allowance: set a share once (default 2 points) and leave it, here is what the agent does on a visit and what you get back (its own account and memories), and here is what is enforced today (checked between turns, a visit can end a little over, anything else on the account moves the same meter). That moves it from conditions to approve.",
  "would_pay": "n/a"
}
```
