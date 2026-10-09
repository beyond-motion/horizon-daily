---
layout: default
title: "Horizon Summary: 2026-10-09 (EN)"
date: 2026-10-09
lang: en
---

> From 10 items, 3 important content pieces were selected

---

**Technology News**
1. [Cloudflare acquires Deno, raising questions about runtime&\#x27;s future](#item-tech-news-1) ⭐️ 8.0/10
2. [Oxide Computer raises $445M Series D](#item-tech-news-2) ⭐️ 7.0/10
3. [Matthew Green warns AI surprises may outpace cryptographic standards](#item-tech-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Cloudflare acquires Deno, raising questions about runtime&\#x27;s future](https://deno.com/blog/cloudflare) ⭐️ 8.0/10

Cloudflare has acquired Deno, the JavaScript/TypeScript runtime created by Node.js founder Ryan Dahl, according to the submission. The acquisition prompted extensive community discussion about Deno&\#x27;s future and a broader wave of developer-tooling consolidation. In comments, users quote the Deno blog as saying Cloudflare will support the Deno runtime for another year with monthly bug-fix and security releases, after which it will end development of the Deno runtime; Deno will remain open source and others are welcome to continue it. Commenters debated whether the move amounts to an acquihire and pointed to other recent acquisitions involving Astro.js, VoidZero, and Bun.

hackernews · ilreb · Oct 9, 13:03 · [Discussion](https://news.ycombinator.com/item?id=50019911)

**「Background」** Deno is a JavaScript/TypeScript runtime co-created by Ryan Dahl, the creator of Node.js, and Bert Belder; it combines runtime and package manager in a single executable. The announced move brings Deno under Cloudflare, where the team will work with the Workers and Durable Objects teams, following a progression from Deno to Deno Deploy to celld. Reports say the Deno team, including Dahl and Belder, will lead an effort to merge celld&\#x27;s distributed Durable Objects implementation into workerd to support self-hosted deployments with object placement, routing, and durable storage across multiple machines.

**「Impact」** For Deno developers and Deno Deploy customers, the acquisition means Deno Deploy will shut down after six months and paying customers are being offered migration support to Cloudflare Workers, while the Deno runtime remains open source but—according to the blog post quoted in the community discussion—will receive only another year of monthly bug and security updates before Cloudflare ends its development unless others take over.

**「Community Discussion」** Commenters largely treated the acquisition as the end of active Deno runtime development, citing the quoted one-year support window, while some characterized it as an acquihire and reflected on Deno&\#x27;s earlier shift toward npm compatibility. Others discussed Cloudflare&\#x27;s business rationale and noted alternatives such as workerd and celld.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Deno_%28software%29">Deno (software) - Wikipedia</a></li>
<li><a href="https://www.brocker.org/deno-joins-cloudflare-self-hosted-workers">Deno joins Cloudflare to simplify self-hosted Workers</a></li>
<li><a href="https://deno.com/blog/cloudflare">Deno is joining Cloudflare | Deno</a></li>
<li><a href="https://deno.com/blog/cloudflare">Deno is joining Cloudflare | Deno</a></li>

</ul>
</details>

**Tags**: `#JavaScript runtime`, `#acquisitions`, `#Cloudflare`, `#Deno`, `#developer tooling consolidation`

---

<a id="item-tech-news-2"></a>
### [Oxide Computer raises $445M Series D](https://oxide.computer/blog/our-445m-series-d) ⭐️ 7.0/10

Oxide Computer announced a $445M Series D funding round. The round is significant industry news for the systems, hardware, and on-prem cloud space, though the item is a corporate fundraising announcement rather than a technical deep-dive. No source content was available to detail investors, valuation, product plans, or technical milestones. Hacker News discussion focused on the company’s reputation, the decision to raise equity instead of using debt or trade finance, and the changing cloud infrastructure market.

hackernews · ahlCVA · Oct 9, 13:12 · [Discussion](https://news.ycombinator.com/item?id=50020014)

**「Background」** Oxide Computer Company is an on-premises cloud computing company whose product is a rack-scale system that integrates hardware and software for running infrastructure at scale, marketed as a cloud you own. It introduced its commercial Cloud Computer in October 2023. A Series D is a later-stage venture-capital financing round; Oxide&\#x27;s was led by Eclipse with participation from existing investors.

**「Impact」** The capital is earmarked for component procurement, manufacturing expansion, and fulfillment of existing and future customer orders, which is the most direct consequence for enterprises evaluating Oxide&\#x27;s integrated on-premises racks as an alternative to hyperscaler cloud for compliance- and data-gravity-driven workloads. The announcement provides no specific capacity, shipment, or pricing figures, so any near-term improvement in availability or delivery times remains unquantified.

**「Community discussion」** Commenters were broadly positive about Oxide and its communications, with praise for the company and the fundraising announcement’s framing. One commenter questioned why Oxide raised equity rather than using debt or trade finance and speculated about locking in supplier orders, while another offered a practical anecdote about migrating a Firestore app to SQLite as evidence that cloud lock-in is weakening.

<details><summary>References</summary>
<ul>
<li><a href="https://finance.yahoo.com/technology/articles/oxide-raises-445m-series-d-130000230.html?fr=sycsrp_catchall">Oxide Raises $445M Series D as the Company Proves Vision of ...</a></li>
<li><a href="https://oxide.computer/">Oxide Computer Company</a></li>
<li><a href="https://www.hpcwire.com/off-the-wire/oxide-introduces-innovative-cloud-computer-bridging-the-gap-between-hardware-and-software-for-on-prem-solutions/">HPCwire - Since 1987 – Covering the Fastest Computers in the ...</a></li>
<li><a href="https://finance.yahoo.com/technology/articles/oxide-raises-445m-series-d-130000230.html?fr=sycsrp_catchall">Oxide Raises $445M Series D as the Company Proves Vision of ...</a></li>
<li><a href="https://www.citybiz.co/article/917002/oxide-raises-445-million-series-d-to-expand-on-premises-cloud-infrastructure-manufacturing/">Oxide Raises $445 Million Series D to Expand On-Premises ...</a></li>

</ul>
</details>

**Tags**: `#hardware`, `#data center infrastructure`, `#venture capital`, `#systems software`, `#on-prem cloud`

---

<a id="item-tech-news-3"></a>
### [Matthew Green warns AI surprises may outpace cryptographic standards](https://simonwillison.net/2026/Oct/9/matthew-green/) ⭐️ 7.0/10

Matthew Green, quoted by Simon Willison, warned that AI’s pace of producing surprises may far exceed the pace at which humans can replace cryptographic standards, even with the best AI assistance. He assigned a 1% chance to living in Minicrypt—Russell Impagliazzo’s hypothetical world in which public-key encryption is impossible—and a 15% chance that society functionally loses confidence in existing public-key encryption algorithms. Green argued that recovering from such a surprise requires preparation done in advance, framing the warning as a deliberately worst-case possibility rather than a confident prediction. The item is a short quoted tweet rather than a technical deep dive or research result, and no specific algorithms, versions, or timelines are identified.

rss · Simon Willison · Oct 9, 15:02

**「Background」** Minicrypt is Russell Impagliazzo&\#x27;s hypothetical world in which public-key encryption is impossible, and Green puts the chance of living in it at 1%. Green has also clarified that &quot;losing public-key encryption&quot; would not mean cryptography or encryption is impossible, or that we live in Minicrypt, but rather that imminent cryptanalytic results substantially improve attacks on standardized schemes. In that scenario, schemes previously considered &quot;good enough&quot; at 128-bit security might in reality offer only 96- or 108-bit security.

**「Impact」** If confidence in existing public-key algorithms such as RSA and ECC erodes, the organizations, protocols, and hardware that depend on them would face a rushed migration to replacement standards, a transition that supporting material notes can create compatibility problems for older systems. Green&\#x27;s figures are explicitly worst-case guesses rather than demonstrated results, and his stated condition for recovery is that preparation be done in advance.

<details><summary>References</summary>
<ul>
<li><a href="https://agihunt.info/en/p/1a11d1439a5beb7ab92ded8df30">Cryptographer Matthew Green: losing public-key… · AGI Hunt</a></li>
<li><a href="https://x.com/matthew_d_green/status/2108282817343824147">Matthew Green on X: &quot;So what does “losing public-key ...</a></li>
<li><a href="https://www.nist.gov/cryptography">What is cryptography ? Cryptography uses mathematical techniques...</a></li>
<li><a href="https://www.researchgate.net/publication/388882504_Quantum_Computing_and_Cryptography_Preparing_for_the_Post-Quantum_Era">(PDF) Quantum Computing and Cryptography : Preparing for the...</a></li>

</ul>
</details>

**Tags**: `#cryptography`, `#AI risk`, `#public-key encryption`, `#standards`, `#security`

---