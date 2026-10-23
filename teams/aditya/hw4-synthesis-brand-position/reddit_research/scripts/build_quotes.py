#!/usr/bin/env python3
"""Build quotes.jsonl from saved Reddit pages. Every quote is checked word for word
against the saved post or comment text; the script stops if any quote doesn't match."""
import glob, html, json, os, re, sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "..", "..", "reddit_corpus", "raw")
OUT = os.path.join(HERE, "..", "quotes.jsonl")

def norm(s):
    return re.sub(r"\s+", " ", html.unescape(s)).strip()

posts, comments = {}, {}
for f in glob.glob(os.path.join(RAW, "*.json")):
    d = json.load(open(f))
    if isinstance(d, dict):
        for x in d["data"]["children"]:
            posts[x["data"]["id"]] = x["data"]
        continue
    p = d[0]["data"]["children"][0]["data"]
    posts[p["id"]] = p
    def walk(ch):
        for c in ch:
            if c["kind"] != "t1":
                continue
            comments[c["data"]["id"]] = (c["data"], p)
            r = c["data"].get("replies")
            if isinstance(r, dict):
                walk(r["data"]["children"])
    walk(d[1]["data"]["children"])

# (post_id, comment_id or None for the post itself, exact quote, theme, use_for)
Q = [
 # Real vs fake
 ("1o4bou1","oe8t3vv","the hardest part of subletting in nyc was never finding listings, it's figuring out which ones are real","Which listings are real","canonical_language"),
 ("1o4bou1","oe8t3vv","half the photos are stolen from streeteasy and the person wants you to wire a deposit before you even see the place","Which listings are real","pain_point"),
 ("1kmxk6o",None,"why are 95% of facebook group housing posts scams","Which listings are real","canonical_language"),
 ("1kmxk6o",None,"facebook groups: it’s been almost entirely scammers, and only one person has even replied back to me.","Which listings are real","persona"),
 ("1vnjm4d",None,"Used to use craigslist to find sublets, seems to be nothing but scams there these days.","Which listings are real","pain_point"),
 ("1pjtbcb","ntgsz53","I also beg everyone to stay off Facebook marketplace and craigslist because there’s a 1% chance you find anything real.","Which listings are real","pain_point"),
 ("1vk68ol","p2r2mlk","Doubly true for shit on Craigslist - that’s scammer central now.","Which listings are real","pain_point"),
 ("1qhaawg",None,"reported the listing on Marketplace (which likely will stay live as Meta loves scams)","Which listings are real","objection"),
 ("nl3sok",None,"Are these all legit? They all look newly renovated and clean. Or just like craiglist, are there scams at OCHA?","Which listings are real","persona"),
 ("1beb8hf",None,"The FB groups are a it sketch","Which listings are real","persona"),
 ("1rndpst","o98f00r","this one didn’t seem clear to me until I had engaged with “her” for quite a while","Which listings are real","pain_point"),
 ("1synk84","ok6mv08","A good trick i found for checking for scams has been a simple reverse image search","Which listings are real","pain_point"),
 # Can't see it in person
 ("1cpwev9",None,"have never been to NYC before; as such, I fear I am a prime target for scams","Can't see it in person","persona"),
 ("1cpwev9",None,"I feel like I have been and finding some pretty darn good deals... suspiciously good","Can't see it in person","persona"),
 ("1rndpst",None,"It is too far away to just swing by for a visit.","Can't see it in person","persona"),
 ("1rndpst","o9646h6","my question is how do you arrange that over the internet without being at risk of being scammed?","Can't see it in person","canonical_language"),
 ("1vk68ol","p2r228e","Never rent a place in New York sight unseen, period.","Can't see it in person","objection"),
 ("1vm1uc3","p360ouk","Virtual tour = scam.","Can't see it in person","objection"),
 ("1synk84","oixhxmw","I got lit up by people saying I shouldn’t sign anything even if there was a video tour offered and that I have to do it in person.","Can't see it in person","persona"),
 ("1rndpst","o97ky5f","never pay for something like this ahead of time","Can't see it in person","objection"),
 # Paying with no recourse
 ("1vk68ol","p2r7cbr","Zelle is only for people you are already face to face with.","Paying with no protection","pain_point"),
 ("1vk68ol","p2r3sko","Triply true for Zelle, which has zero protections.","Paying with no protection","canonical_language"),
 ("1pjtbcb",None,"He told me I was approved, made me sign a lease, and asked for a USPS money order for the deposit.","Paying with no protection","pain_point"),
 ("1pjtbcb","ntl26bo","A money order for the deposit is a huge red flag","Paying with no protection","pain_point"),
 ("1pjtbcb","ntl7b3e","why? how should you pay?","Paying with no protection","pain_point"),
 ("1rndpst","o965cql","I would use a payment app that gives you the ability to send the money as a purchase as opposed to as a gift.","Paying with no protection","pain_point"),
 # Ghosting
 ("1synk84","oiwwd74","For any long, legitimate sublets, or for actual rentals, it's impossible to get a reply.","Nobody answers","pain_point"),
 ("1vnjm4d",None,"Tried out listings project but no one returns my emails.","Nobody answers","pain_point"),
 ("1u7ufvs",None,"In many cases nobody responds at all.","Nobody answers","pain_point"),
 ("1synk84","oixgz5h","I have reached out to several places that don't appear to be scams but I haven't heard anything back.","Nobody answers","pain_point"),
 ("1kmxk6o",None,"the few people I’ve reached out to haven’t responded","Nobody answers","pain_point"),
 ("1synk84","oixfqfa","I listed my own room last week and I got over 40 replies.","Nobody answers","persona"),
 ("1synk84","oj0fsu0","She said she listed on fb marketplace also but was bombarded by messages","Nobody answers","persona"),
 # Scattered
 ("1o4bou1",None,"It really is a full time job trying to find a place in NYC.","Search is scattered","canonical_language"),
 ("1o4bou1",None,"The fact you can't filter through this pages was annoying.","Search is scattered","pain_point"),
 ("1synk84",None,"even more spammy than craigslist and difficult to sort the posts by date posted","Search is scattered","pain_point"),
 ("1onrwz9",None,"Where do students usually post short term leases for 4/8-month terms? is there some kind of discord server?","Search is scattered","persona"),
 # Trust through people
 ("1cpwev9","l3nugjb","they require your uni to join the group","Trust comes from people you know","canonical_language"),
 ("1synk84",None,"word of mouth - i posted on IG a bunch just asking people if they knew of anything opening up.","Trust comes from people you know","persona"),
 ("1synk84",None,"this seems like one of the most effective routes tbh","Trust comes from people you know","pain_point"),
 ("1u7ufvs","os4sdce","That's how wide you have to network haha","Trust comes from people you know","pain_point"),
 ("1wrcqru","pcbgvv2","Maybe if you have mutual friends on Facebook?","Trust comes from people you know","canonical_language"),
 ("1wrcqru","pck58kd","We also don’t have any mutual friends, so there isn’t really much of a digital footprint for me to verify.","Trust comes from people you know","pain_point"),
 ("1beb8hf",None,"My sister's friend's little sister works for a startup at USF that does student subleasing.","Trust comes from people you know","persona"),
 # Is the sublet even allowed
 ("1rndpst",None,"We plan to confirm with the landlord organization that she’s a renter there & her permission to sublease.","Is the sublet allowed","pain_point"),
 ("1rndpst","o97rcxu","they said they have no tenant by that name and that the apartment number she gave me doesn’t exist in the building","Is the sublet allowed","pain_point"),
 ("1wrcqru","pck0v34","my bigger concern is whether she’s actually allowed to rent the room out in the first place","Is the sublet allowed","canonical_language"),
 ("1pjtbcb","nti53va","as soon as he leased the unit, he began posing as the \"owner\" and was subleasing the unit out","Is the sublet allowed","pain_point"),
 # Subletter side
 ("1r5gvmn","odeuqif","worried about finding a reliable, honest sub letter for my rent stabilized apartment","Subletters need honest people too","canonical_language"),
 ("1r5gvmn","o5m9eoq","The only risk of this is the subletter becoming a squatter and refusing to leave once u come back","Subletters need honest people too","objection"),
 ("1ow4lyn",None,"(Preferably college students / 20 somethings)","Subletters need honest people too","persona"),
 ("1ow4lyn","nonjd9k","I was wondering if I should’ve even bothered trying Reddit!","Subletters need honest people too","persona"),
 # Dates and short terms
 ("1q1be9k","nx4ts04","The only thing i’m worried about with subletting is that i won’t be able to get the right dates and/or my roommate won’t be able to live with me","Students need exact dates","persona"),
 ("1rndpst","o95yc6j","She’s only going to be there for 3 months and can’t afford to spend her summer in a hotel.","Students need exact dates","persona"),
 ("1rndpst",None,"it’s basically impossible to lease a furnished apartment for only 3 months from a leasing company, it needs to be a sublet from a longer term renter.","Students need exact dates","pain_point"),
 ("1vm1uc3",None,"need to find a place to sublet for a few months before moving into student housing","Students need exact dates","persona"),
 ("1q1be9k","nx4bx4y","you can 1000% sublet a room for half that","Students need exact dates","pain_point"),
 # Objections
 ("1o4bou1","nj17hmc","We get a new one every year.","Objections to a new platform","objection"),
 ("1rndpst","o96uewo","Keep all messaging and payment on Airbnb, and if something goes wrong they'll find her another place to stay and pay for it.","Objections to a new platform","objection"),
 ("1wrcqru","pcejerq","If you want some measure of security and a contract, pay for a real Airbnb.","Objections to a new platform","objection"),
 ("1vm1uc3","p36kg4s","There is no way you can validate any ID. So what’s the point in receiving a copy of someone’s ID?","Objections to a new platform","objection"),
 ("1synk84","oizk4hv","I wouldn't trust it. Its not very accurate.","Objections to a new platform","objection"),
 ("1o4bou1","pek5k6n","and the fb posts but i personally find them sus","Objections to a new platform","objection"),
 # Mocked language
 ("1vm1uc3","p369a1h","Refundable \"If you decide to cancel\", so what the heck is the deposit for lol...","Language people mock","objection"),
 ("1vm1uc3","p360a0s","The sob story about the wife, offered up totally unprompted, is another red flag.","Language people mock","objection"),
 ("1synk84","oj4uobg","five days is not a sublet…just pay your rent!","Language people mock","objection"),
 ("1synk84","oiwwd74","They even have a \"World Cup Rentals\" section that is basically Airbnb by another name.","Language people mock","objection"),
 ("1vk68ol","p2rwe46","They want people to get excited over the opportunity so they'll send money without thinking it through","Language people mock","objection"),
]

def ym(ts):
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m")

out, bad = [], []
for pid, cid, quote, theme, use in Q:
    if cid:
        if cid not in comments:
            bad.append((cid, "comment missing")); continue
        c, p = comments[cid]
        text, score, ts = c["body"], c["score"], c["created_utc"]
        link = f"https://www.reddit.com/r/{p['subreddit']}/comments/{p['id']}/_/{cid}/"
    else:
        if pid not in posts:
            bad.append((pid, "post missing")); continue
        p = posts[pid]
        text, score, ts = p["title"] + " " + p.get("selftext", ""), p["score"], p["created_utc"]
        link = "https://www.reddit.com" + p["permalink"]
    if norm(quote) not in norm(text):
        bad.append((cid or pid, quote[:60])); continue
    out.append({"subreddit": "r/" + p["subreddit"], "permalink": link, "thread_title": norm(p["title"]),
                "score": score, "date": ym(ts), "quote": quote, "is_verbatim": True,
                "theme": theme, "use_for": use})

if bad:
    for b in bad: print("NOT VERBATIM / MISSING:", b)
    sys.exit(1)
with open(OUT, "w") as f:
    for r in out: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"wrote {len(out)} verified quotes to quotes.jsonl")
