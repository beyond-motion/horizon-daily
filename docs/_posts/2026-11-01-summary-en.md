---
layout: default
title: "Horizon Summary: 2026-11-01 (EN)"
date: 2026-11-01
lang: en
---

> From 11 items, 2 important content pieces were selected

---

**Technology News**
1. [ChatGPT account takeover via sandboxed HTML preview exploit](#item-tech-news-1) ⭐️ 8.0/10
2. [Karpathy’s HackerTube Builds a YouTube-Like Feed From Hacker News Comments](#item-tech-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [ChatGPT account takeover via sandboxed HTML preview exploit](https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts/) ⭐️ 8.0/10

Parameter Labs described an exploit chain against ChatGPT&\#x27;s sandboxed HTML previews, formerly called Canvas, in which interactive custom HTML apps run inside an iframe. The chain abused MathLive&\#x27;s virtual keyboard, whose parent-page postMessage handler used innerHTML and accepted messages from sandboxed frames, allowing untrusted HTML to insert a new iframe without sandbox restrictions. OpenAI&\#x27;s CSP blocked inline scripts and restricted script sources, but a YouTube oEmbed endpoint could reflect JavaScript that executed in the ChatGPT origin, after which attacker-controlled code could read private data from APIs and exfiltrate it through an image reference. A crafted ChatGPT share URL could therefore exfiltrate a signed-in visitor&\#x27;s private data or act on their behalf, and OpenAI closed the hole and paid a $5,000 bug bounty, which Simon Willison called low for the severity.

rss · Simon Willison · Oct 31, 23:15

**「Background」** ChatGPT&\#x27;s HTML preview feature, which grew out of the artifacts/Canvas pattern, renders user-authored HTML as an interactive page inside a sandboxed iframe, typically on a separate origin. That isolation is intended to stop arbitrary preview code from reading a signed-in user&\#x27;s ChatGPT data or acting through OpenAI&\#x27;s APIs. Parameter Labs&\#x27; write-up describes a chain that abused a MathLive virtual-keyboard postMessage handler in the parent page; OpenAI said both frontends rejected the reported messages and fixed the issue, paying a $5,000 bounty, and the attack required a victim to click a shared link.

**「Impact」** ChatGPT users who opened shared HTML-preview links faced possible private-data theft or actions taken on their behalf until OpenAI fixed the flaw, and the chain shows that sandboxed artifact systems must secure cross-frame postMessage handlers and every CSP-allowed script source.

<details><summary>References</summary>
<ul>
<li><a href="https://www.parameter.ai/labs/we-found-a-gap-at-openai">Do the Math : How We Took Over ChatGPT Accounts - Parameter</a></li>
<li><a href="https://news.ycombinator.com/item?id=50314699">Do the math : How we took over ChatGPT accounts | Hacker News</a></li>

</ul>
</details>

**Tags**: `#security`, `#ChatGPT`, `#sandboxing`, `#postMessage`, `#vulnerability research`

---

<a id="item-tech-news-2"></a>
### [Karpathy’s HackerTube Builds a YouTube-Like Feed From Hacker News Comments](https://karpathy.bearblog.dev/hacker-tube/) ⭐️ 7.0/10

Karpathy has launched HackerTube, a YouTube-style interface at hackertube.org that organizes 6,454 videos sourced from 39,834 Hacker News comments since 2007. The project turns years of scattered HN comment recommendations into a browsable, video-centric feed. It is a brief project announcement rather than a technical deep dive, so details on ranking, deduplication, or curation beyond the video and comment counts are not provided. The result is a concrete experiment in community-driven video discovery for the Hacker News audience.

hackernews · karpathy · Oct 31, 19:56 · [Discussion](https://news.ycombinator.com/item?id=50319510)

**「Background」** Hacker News is a long-running technology forum where commenters frequently share and discuss YouTube videos, making its archives a large informal record of community recommendations. HackerTube, a side project by Andrej Karpathy, turns that record into a YouTube-style browsing interface by extracting 6,454 videos from 39,834 comments dating back to 2007. Coverage of the build reports that Karpathy used Claude Opus 5.5 and a Claude Sonnet filtering workflow inside Claude Code to process the recommendations, completing the project in roughly two hours.

**「Impact」** For Hacker News readers, HackerTube provides a single browsable library of videos surfaced in comments since 2007, offering an alternative to YouTube’s own recommendation feed. Its scope is comment-derived, so videos submitted as HN links but not discussed in comments may be absent.

**「Community Discussion」** Commenters were broadly positive, with one arguing that HackerTube points to a larger opportunity to build personal, LLM-assisted feeds that reduce dependence on engagement-maximizing platforms and another saying the model could work for different niches. Others proposed a friend-based pub/sub recommendation feed, noted that HN’s directly submitted YouTube links are also valuable, and pointed to a books-focused version of the same idea.

<details><summary>References</summary>
<ul>
<li><a href="https://runtimewire.com/article/andrej-karpathy-hackertube-hacker-news-youtube">Andrej Karpathy builds HackerTube from 6,454 videos ...</a></li>
<li><a href="https://aiweekly.co/alerts/karpathy-ships-hackertube-in-2-hours-with-claude-opus-55">Karpathy ships HackerTube in ~2 hours with Claude Opus 5.5</a></li>
<li><a href="https://elsolitario.org/en/2026/11/01/karpathy-builds-hackertube-claude-opus/">Hacker News HackerTube: How Karpathy Built It - elsolitario.org</a></li>

</ul>
</details>

**Tags**: `#Hacker News`, `#content curation`, `#recommendation systems`, `#video discovery`, `#side projects`

---