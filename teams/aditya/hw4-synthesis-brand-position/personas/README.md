# Persona agents

Four synthetic judges for Gable, built with `resources/template_persona-agent.md`. Each one is
grounded in exact quotes from our housing interviews (see `../synthesis_comparison.md`) and our
Reddit research (see `../reddit_research/`). Install by copying the files into `.claude/agents/`.

| Agent | Who | Where they come from |
|---|---|---|
| [persona-dana](persona-dana.md) | Dana Whitfield, 20, out-of-town summer intern who can't tour in person | Jasmine (H5); Reddit theme 2, "you can't see it before you pay" |
| [persona-theo](persona-theo.md) | Theo Ramirez, 21, Columbia junior who gets ghosted while racing a semester deadline | Marcus (H4); Reddit themes 1, 4 and 9 |
| [persona-nora](persona-nora.md) | Nora Kim, 23, grad student hunting a 12-month lease with a dog | Emma (H2); Reddit theme 5, "the search is scattered" |
| [persona-jordan](persona-jordan.md) | Jordan Ellis, 24, grad student subletting their own room | Reddit theme 8, "subletters need honest people too" |

Why these four: our synthesis found two kinds of seeker who want different things. Open-market
lease hunters like Emma want fewer sites and accurate details. Sublet seekers like Marcus and
Jasmine want to know the person is real. The sublet seekers then split by whether they're in NYC
(Theo) or can't visit (Dana). Jordan is the supply side: without trustworthy listers there are no
listings. Tina (H3), who found housing through her cousin, is not a persona; she has no problem
for Gable to solve.

## What each persona said about our brand position

We ran all four agents against `../brand_position.md` on Oct 15, fixed what came up more than once, then re-ran Dana and Jordan on the new version. Scores are before → after.

- **Dana (5 → 8, now approves):** She liked the Reddit quote about arranging a sublet "over the internet without being at risk of being scammed" because that's literally her. But she said the doc was mostly about saving people from tours she can't even go to, and never said how her deposit is protected, what happens if a listing is fake, or what we actually check. **Changed:** added a "What We Check (and What We Don't)" section (school email, proof they're on the lease, money only through Gable, deposit comes back if the listing is fake) and a line saying trust has to work without a visit.
- **Theo (6, not re-run):** Said we nailed the problem ("never finding listings, it's figuring out which ones are real") but our big feature is scheduling tours, and his problem is 26 out of 30 people never writing back. He also needs exact dates and room for two. **Changed:** every listing now shows when the lister was last active and how fast they reply (also added to the positioning statement), and search covers exact dates, number of rooms, and furnished.
- **Nora (6, not re-run):** Loved the coordination part ("half my weekends right there") but her issue is details that lie, like "pet friendly" meaning cats only. **Changed:** listing details are now marked as confirmed or just claimed by the lister. **Didn't change:** she also wanted one place to save listings from every site. That's a real product idea, but it's a feature, not positioning, so we're saving it for the MVP doc.
- **Jordan (4 → 6, no longer rejects):** The only reject. Jordan is a student subletting their own room and couldn't find themselves anywhere in the doc. Our "Renters first... we side with the renter" value made listers sound like the other side. **Changed:** swapped that value for "Students on both sides," added students subletting their room to the target identity, added "cover your rent while you're away" (never "earn income from your space"), and (after the re-run) said only verified students can apply, with their dates up front. **Didn't change:** Jordan still wants to know what happens if a subletter stops paying or won't leave in May. We put it in open questions instead of making a promise we don't have a plan for yet.

What we learned: payment and "what do you actually check?" came up from almost everyone, and the original doc only spoke to people searching, not the students listing rooms. The coordination pitch works for Nora but not for Dana or Theo, which backs up testing both headlines on the landing pages.
