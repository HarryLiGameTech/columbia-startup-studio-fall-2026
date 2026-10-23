# CallIt analytics

Google Analytics 4 measures visits and signups on the CallIt marketing pages. Lowercase UTM values identify the source, medium, campaign, and post for each tagged link.

## Measurement plan

| Question | Measure |
|---|---|
| Which page attracts interest? | Sessions by page path. |
| Which source brings visitors? | Sessions by UTM source, medium, campaign, and content. |
| Which visitors join the waitlist? | The `sign_up` event after a successful signup. |
| Which page converts? | Signups compared with sessions for the same page. |

## Setup

The Google tag should load on the homepage and each landing page. After a successful signup, the visitor reaches the thank-you page and the site sends one `sign_up` event. Mark this event as a key event in Google Analytics. Do not send email addresses or private group content to analytics.

## Latest documented check

A live check dated October 16, 2026, reported that the tag loaded across the homepage and three landing pages, and that the thank-you page sent one signup event after signup. The event was not yet marked as a key event at that check. Confirm the key-event setting and use Realtime to check current activity. Standard reports can take 24 to 48 hours to populate.

## Weekly review

Compare sessions and signup events by page and tagged source. Treat conversion rates as estimates when the sample is small. Exclude verification visits when possible.
