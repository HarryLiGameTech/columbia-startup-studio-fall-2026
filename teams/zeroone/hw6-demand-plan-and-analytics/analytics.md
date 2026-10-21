# Analytics guide

How we measure the waitlist page and where to look. Owner: Yuval. The code lives in `landing-pages/src/analytics.js` and `landing-pages/src/attribution.js`; the storage in `waitlist-service/`.

## What is measured

| Question | Where the answer is | How it gets there |
|---|---|---|
| How many people visit, from where, on what device | Google Analytics 4 | gtag.js on every landing page view, loaded only when `VITE_GA_MEASUREMENT_ID` is set |
| Which of the five designs each visitor saw | GA4 event `view_design` (`design`, `pinned`, `explorer`) and our table `landing_design_views` | sent after `/api/design` picks the design |
| How many open the signup form | GA4 event `open_signup` (`design`) | sent when the form opens |
| Which audience page converts | `page_view` per path (`/`, `/for/friends`, `/for/sports`, `/for/agreements`) and the `page` parameter on `view_design` and `sign_up`; register `page` as a custom dimension in GA4 Admin → Custom definitions to break conversions down by page. |
| How many sign up (the conversion) | GA4 event `sign_up` (`design`, `group_type`) plus a page view of `/thanks`; our tables `waitlist_contacts` and `waitlist_signups` | sent after the server says the signup is saved, then the browser goes to `/thanks?option=<design>` |
| How many fail to sign up | GA4 event `signup_failed` (`design`) | sent when the server refuses |
| Which design converts best | `npm run waitlist:db -- designs` | views and signups per design from our tables; also drives the adaptive choice |
| Which campaign or community each signup came from | `npm run waitlist:db -- sources`; GA4 Acquisition reports | `utm_*` and referrer captured on landing, stored first-touch in `waitlist_attribution` |

Nothing we store identifies a visitor: GA4 has its own cookies, our tables hold emails only for people who signed up, and attribution rows hold only campaign labels.

## One-time setup

Status on 2026-10-16: steps 1, 2, 4 and 5 are done and verified on the live domain. Step 3 is the only thing left, and it is a click in the GA4 dashboard.

1. **Create the GA4 property.** Done. Property for call-it.app with a Web data stream; Measurement ID `G-HPKQ2CBQT7`. Enhanced measurement is on (it is what sends `form_start`).
2. **Give the build the ID.** Done. `VITE_GA_MEASUREMENT_ID` is in `/etc/callit/landing.env` on the server and baked into the live bundle. The ID is public by design.
3. **Mark the conversion.** Not done, needs a human in the GA4 dashboard: Admin → Events (or Admin → Key events), find `sign_up` (it has already been received, so it is listed) and toggle "Mark as key event". Until then `sign_up` is counted as an ordinary event and does not appear in the key-event columns of the acquisition reports.
4. **Create the attribution table on the hosted database.** Done by Elad on 2026-10-15 (`waitlist_attribution` exists and receives rows).
5. **Check it works.** Done on 2026-10-16 against `https://call-it.app` with a real browser and a DevTools network capture, see "Verification" below.

## Verification (2026-10-16, live domain)

A signup through `https://call-it.app/?utm_source=livecheck&utm_medium=agent&utm_campaign=cutover` in Chrome, with every request to Google captured over the DevTools protocol:

| Check | Result |
|---|---|
| gtag.js loads with `G-HPKQ2CBQT7` | yes |
| `page_view` on `/` | sent |
| `view_design` (`design=home`) | sent |
| `open_signup` (`place=hero`) | sent |
| Signup saved to Supabase `waitlist_signups` | yes (not the server's fallback file) |
| UTM first touch in `waitlist_attribution` | row with `livecheck / agent / cutover` |
| `/thanks` page view | sent |
| `sign_up` (`method=waitlist`, `design=home`, `place`, `group_type=friends`) | sent once from `/thanks`; not sent again on reload |

To repeat the check: sign up with a test address from a UTM-tagged link, then GA4 Reports → Realtime should show `sign_up` within a minute, and on the server `npm run waitlist:db -- sources` (run from `/srv/callit/current/landing-pages` with `/etc/callit/landing.env` loaded) lists the source.

## Tagging links

Every link we post gets UTM parameters so the source is known:

```
https://call-it.app/?utm_source=reddit&utm_medium=post&utm_campaign=launch&utm_content=r_sideproject
https://call-it.app/?utm_source=instagram&utm_medium=bio&utm_campaign=launch
https://call-it.app/?utm_source=friends&utm_medium=whatsapp&utm_campaign=launch
```

Rules: `utm_source` is the site or channel, `utm_medium` is the kind of placement (post, bio, dm, email, ad), `utm_campaign` is the push (launch, blog-1), `utm_content` tells two links in the same place apart. Lower-case, no spaces. `?option=<design>` can be added to pin a design for a specific audience, and that design's views still count.

## Reading the numbers

**Weekly, from a terminal** (needs the hosted `DATABASE_URL`):

```sh
cd landing-pages
npm run waitlist:db -- status     # contacts and signups
npm run waitlist:db -- designs    # views, signups, rate and current share per design
npm run waitlist:db -- sources    # signups per source, medium, campaign
```

**In GA4:**

- Reports → Realtime: live visitors and events, useful right after posting a link.
- Reports → Acquisition → Traffic acquisition: sessions and key events per source and medium. This is where UTM links show up.
- Reports → Engagement → Events: counts of `view_design`, `open_signup`, `sign_up`, `signup_failed`. The funnel is view_design → open_signup → sign_up.
- Explore → Funnel exploration: build the same three steps as a funnel, broken down by the `design` parameter (register `design` as a custom dimension in Admin → Custom definitions first).
- Reports → Tech: device and browser, to catch layouts that fail on phones.

**What to watch:** signup rate per design (our `designs` report), signup rate per source (GA traffic acquisition with the `sign_up` key event), and the drop between `open_signup` and `sign_up` (form problems).

## Changing what is tracked

- New event: call `track('name', { params })` from `src/main.js`. Keep the names in `src/analytics.js`'s header comment up to date and add the event to the first table above.
- New attribution field: add it to `ATTRIBUTION_KEYS` in `waitlist-service/database.js`, the table in `schema.sql`, and `UTM_KEYS` in `attribution.js`; run the waitlist tests.
- The web app (callit-web-app) has no analytics yet. When it needs some, reuse the same pattern: load only with an environment variable, send named events, never send emails or group content.

## Note on the sign_up event (2026-10-16)

The `sign_up` conversion is sent from the `/thanks` page, not at the moment of the save. gtag.js queues events for a few seconds and the redirect to `/thanks` dropped the hit; a DevTools capture on the live site showed every other event arriving and `sign_up` never leaving. The signup form stores a one-time flag in `sessionStorage`, `/thanks` reads it, sends `sign_up` with `design`, `place` and `group_type`, and clears it, so a reload does not count twice. Verified live on 2026-10-16: one `sign_up` hit per signup, none on reload.
