---
layout: default
title: "Horizon Summary: 2026-08-24 (EN)"
date: 2026-08-24
lang: en
---

> From 7 items, 4 important content pieces were selected

---

**Technology News**
1. [MS Paint and Photos invisibly watermark AI-edited images with GUIDs](#item-tech-news-1) ⭐️ 8.0/10
2. [IPFS Maintainers Wind Down at Shipyard, Raising Ecosystem Concerns](#item-tech-news-2) ⭐️ 7.0/10
3. [Make a SQLite database that runs as a Linux executable](#item-tech-news-3) ⭐️ 7.0/10
4. [Anthropic revenue soars but new flagship models lag in adoption](#item-tech-news-4) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [MS Paint and Photos invisibly watermark AI-edited images with GUIDs](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

A reverse-engineering analysis found that Microsoft Paint and Microsoft Photos embed invisible GUID watermarks into images that have been AI-manipulated, including output generated entirely with local models. The visible watermark can be turned off, but the invisible one cannot be disabled and is added silently in the background. The finding raises privacy and accountability concerns because the GUID is a unique identifier that could be tied to a Microsoft account, potentially enabling identification through legal requests. It is not yet clear whether the behavior applies to features such as AI-enhanced background deletion or removal.

hackernews · ComputerGuru · Aug 24, 15:28 · [Discussion](https://news.ycombinator.com/item?id=49421158)

**「Background」** Watermarking is a technique for marking content provenance, and invisible watermarks are designed to survive editing while remaining unnoticed by viewers. A reverse-engineering analysis by Xusheng Li shows that Microsoft Paint and Photos embed server-issued GUIDs as invisible watermarks in locally generated images, in addition to a visible Copilot logo watermark that users can disable.

**「Impact」** Users who create or edit images with AI features in MS Paint or MS Photos may have a hidden unique identifier embedded in their files, which could be used to link an image back to their Microsoft account via a subpoena or similar request. The exact scope, including whether simple AI-assisted edits like background removal trigger it, remains unconfirmed.

**「Community discussion」** Commenters largely agreed the AI angle is a red herring and focused on the silent unique identifier as a threat to anonymity, with one noting Microsoft could hand over account data in response to a copyright subpoena. Others cited Microsoft&\#x27;s history of sloppy implementations, including a false Copilot watermark on Azure DevOps commits, and one user reported installing Paint.net after the watermark triggered incorrectly on a simple screenshot resize.

<details><summary>References</summary>
<ul>
<li><a href="https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/">Microsoft Paint and Photos Embed Server-Issued GUIDs as Invisible Watermarks in Locally-Generated Images :: Xusheng Li</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#watermarking`, `#Microsoft`, `#AI-generated content`, `#reverse engineering`

---

<a id="item-tech-news-2"></a>
### [IPFS Maintainers Wind Down at Shipyard, Raising Ecosystem Concerns](https://ipshipyard.com/blog/2026-the-end-of-ipfs-at-shipyard/) ⭐️ 7.0/10

IPFS maintainers are winding down the project at Shipyard, according to a post on the IP Shipyard blog, marking a significant shift for the decentralized-web and open-source ecosystem. The announcement asks the community to share memories and ideas via a Google Form, and it follows earlier signals such as Cloudflare dropping IPFS support. Commenters note sustainability concerns: a former maintainer recommends Iroh, a p2p project built by ex-IPFS and ex-Protocol Labs developers, as a more business-backed alternative, while others point to IPNS and in-browser deliverability problems as long-standing obstacles. The full details of the wind-down timeline and any successor plans are not available in the supplied material.

hackernews · iand · Aug 24, 15:48 · [Discussion](https://news.ycombinator.com/item?id=49421489)

**「Background」** IPFS \(InterPlanetary File System\) is a peer-to-peer protocol for storing and sharing content-addressed data, with multiple implementations maintained by the IPFS community. The IPFS Shipyard is a GitHub organization that hosts experimental and incubated projects by that community, with maintenance provided on a best-effort basis and pull requests welcome. This announcement concerns the winding down of maintenance work at Shipyard, which affects the ongoing development and support of those IPFS-related projects.

**「Impact」** The immediate consequence is reduced upstream maintenance for IPFS, so projects and companies that depend on the protocol must plan for fewer updates and consider alternatives such as Iroh or self-maintained forks.

**「Community Discussion」** Commenters expressed sadness and frustration, with a former maintainer recommending Iroh as a sustainable p2p alternative and others citing Cloudflare&\#x27;s earlier IPFS drop and unreliable in-browser IPFS.js as factors in the project&\#x27;s decline. One commenter also criticized the request for feedback via a Google Form as ironic for a decentralized-web project.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ipfs-shipyard">IPFS Shipyard · GitHub</a></li>
<li><a href="https://docs.ipfs.tech/concepts/ipfs-implementations/">IPFS implementations | IPFS Docs</a></li>

</ul>
</details>

**Tags**: `#IPFS`, `#decentralized web`, `#open source`, `#p2p`, `#Protocol Labs`

---

<a id="item-tech-news-3"></a>
### [Make a SQLite database that runs as a Linux executable](https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/) ⭐️ 7.0/10

Farid Zakaria described a Linux pattern in which a SQLite database file is also a valid executable binary. The trick sets SQLite&\#x27;s 4-byte application ID at byte offset 68 to the ASCII value SELF, then stores ELF executable components across SQLite tables using the selfdb schema. A C interpreter called self-exec extracts and runs those pieces, and Linux&\#x27;s binfmt\_misc can register the SELF pattern so the kernel invokes self-exec automatically. On non-NixOS systems, registration looks like writing &\#x27;:self:M:68:SELF::/usr/local/bin/self-exec:&\#x27; to /proc/sys/fs/binfmt\_misc/register. The approach is a clever systems-programming hack that merges SQLite and ELF formats, though it is not a major industry shift.

rss · Simon Willison · Aug 24, 11:38

**「Background」** SQLite stores metadata in a 100-byte file header, including a 4-byte application ID at offset 68 that applications can set to identify the database. ELF is the standard executable format on Linux, and binfmt\_misc lets the kernel recognize arbitrary binary patterns and hand matching files to an interpreter.

**「Impact」** Systems programmers can now create dual-format files that are both queryable SQLite databases and runnable executables, enabling tools to inspect or modify a binary&\#x27;s structure with SQL; the practical reach is limited to Linux systems that register the binfmt\_misc handler.

**Tags**: `#SQLite`, `#ELF`, `#Linux`, `#systems programming`, `#binfmt\_misc`

---

<a id="item-tech-news-4"></a>
### [Anthropic revenue soars but new flagship models lag in adoption](https://simonwillison.net/2026/Aug/23/anthropics-best-ai-model-struggles-to-attract-users-as-cheaper-t/) ⭐️ 7.0/10

According to an FT report citing people with knowledge of the matter, Anthropic&\#x27;s annualized revenue reached $65bn in July, up from $47bn in May, and the company expects Q3 to be profitable using the same model that declared Q2 profitable, while telling investors it has 6,000 customers spending $100,000 or more annually. OpenAI&\#x27;s annualized revenue has jumped 35% in the quarter to date to over $40bn, boosted by the July launch of GPT 5.6 after a sluggish start to the year. Ramp&\#x27;s AI index, based on billing data from 70,000 companies, shows Anthropic model spend in July led by Opus 4.8 at 28.0%, followed by Sonnet 4.6 at 8.3% and Fable 5 at 8.0%, with the newly released Opus 5 at only 3.5%. The data supports the view that Fable 5&\#x27;s cost has made it a less popular model, and that Opus 5&\#x27;s late-July release limited its initial adoption.

rss · Simon Willison · Aug 23, 20:24

**「Background」** Anthropic&\#x27;s Claude lineup is split into tiers: Opus is the flagship high-end family, Sonnet is the balanced mid-tier, and Haiku is the fast, low-cost option; in 2026 the company also added Fable 5, a &\#x27;Mythos-class&\#x27; model aimed at reasoning, coding, and agentic workloads. The FT story and Ramp&\#x27;s AI index measure model adoption through customer billing data, so the reported percentages reflect actual spending on each Claude model rather than just marketing positioning. That context explains why a newly released, expensive flagship can show low adoption if cheaper or established models already meet most customers&\#x27; needs.

**「Impact」** For enterprises and developers choosing Claude models, Ramp billing data indicates Anthropic&\#x27;s newest flagship models, Fable 5 and Opus 5, together accounted for only about 11.5% of Anthropic spend in July, while the older Opus 4.8 remained dominant at 28%, suggesting cost and release timing are currently limiting uptake of the latest models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.usecarly.com/blog/claude-models-explained/">Claude Models Explained (2026): Opus vs Sonnet vs Haiku vs Fable</a></li>
<li><a href="https://datrick.com/claude-models-comparison">Claude Models Comparison 2026: Fable, Opus, Sonnet &amp; Haiku</a></li>
<li><a href="https://aiportalx.com/blog/claude-opus-4-8-vs-sonnet-5-vs-fable-5-anthropic-2026-lineup">Claude Opus 4.8 vs Sonnet 5 vs Fable 5: Anthropic&#x27;s 2026 ...</a></li>

</ul>
</details>

**Tags**: `#AI industry`, `#Anthropic`, `#OpenAI`, `#business metrics`, `#model adoption`

---