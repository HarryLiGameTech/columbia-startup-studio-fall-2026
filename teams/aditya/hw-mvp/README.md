# Gable: MVP

Gable is an AI sublet search for NYC university students. You describe the place you want in your own words, and each match shows what we checked about it.

App repo: [sam-hearst/gable](https://github.com/sam-hearst/gable)

## Pages

Production is the waitlist site, at [www.gable.fit](https://www.gable.fit) (also [gable-one.vercel.app](https://gable-one.vercel.app)).

| Page | URL | What it's for |
|---|---|---|
| Homepage | https://www.gable.fit | One chat box for any sublet search; routes to the pages below |
| Landing page 1 | https://www.gable.fit/verified | Stop messaging scammers: every lister is checked |
| Landing page 2 | https://www.gable.fit/summer | Summer sublets for interns and incoming students who can't visit first |
| Landing page 3 | https://www.gable.fit/together | Sublets for two: you and a friend |
| Blog | https://www.gable.fit/blog/how-to-find-your-dream-sublet-in-nyc | A real NYC sublet guide that links to the landing pages |
| Thank-you page | https://www.gable.fit/thanks | Shown after signup; fires the GA `sign_up` key event |

## MVP link

**MVP:** https://www.gable.fit

This is the live site people see. We test changes on a separate staging branch first, so work in progress never reaches it.

## Docs

- [mvp_doc.md](mvp_doc.md): core flow, what's in scope, cut, faked, stack, and roles
- [demand_strategy.md](demand_strategy.md): traffic owners, communities, the first 3 Reddit posts (posted Oct 23), the blog post, and the welcome email

## Analytics

- Google Analytics 4 is on every production page. The chat box sends `chat_request`, and `/thanks` sends `sign_up`, marked as a key event.
- Every link we post uses lowercase UTMs, e.g. `?utm_source=reddit&utm_medium=post&utm_campaign=together`.
- We started Google Analytics Academy 101 and 102 on Google Skillshop.
