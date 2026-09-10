---
layout: default
title: "Horizon Summary: 2026-09-10 (EN)"
date: 2026-09-10
lang: en
---

> From 5 items, 3 important content pieces were selected

---

**Technology News**
1. [Shopify moves back to native from React Native](#item-tech-news-1) ⭐️ 8.0/10
2. [Calif Research claims AI-built zero-click WeChat worm](#item-tech-news-2) ⭐️ 8.0/10
3. [Rust Is Now a Tier-1 Language at Microsoft](#item-tech-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Shopify moves back to native from React Native](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify&\#x27;s engineering blog details a move back to native mobile development from React Native. The item is a Hacker News discussion of that post, and commenters treated it as a notable case study of reversing a high-profile cross-platform migration. The debate centered on tradeoffs between React Native, Electron, and fully native apps, including resource constraints, team composition, and platform-specific optimization. Because the full article was not available in the supplied content, specific technical reasons, performance data, versions, and timelines from Shopify are not included here.

hackernews · fnthawar2 · Sep 10, 14:09 · [Discussion](https://news.ycombinator.com/item?id=49643982)

**「Background」** React Native is a cross-platform framework that lets teams share a single JavaScript codebase across iOS and Android, an approach Shopify had embraced: in 2025 it migrated two of its largest apps, Shopify Mobile and Shopify Point of Sale, to React Native&\#x27;s New Architecture while maintaining weekly releases for millions of merchants. Shopify says coding agents have changed what it costs to build mobile apps, and it had already moved its Shop app from React Native to Swift and Kotlin, going from proof-of-concept to publishing in 12 weeks with AI assistance. The latest move therefore returns Shopify&\#x27;s mobile stack to platform-native Swift and Kotlin.

**「Impact」** Shopify&\#x27;s return to native mobile development means its mobile teams will again maintain separate iOS and Android codebases, giving developers and organizations weighing cross-platform frameworks a concrete case that React Native&\#x27;s efficiency tradeoff can reverse at larger scale and platform-specific demands. Because only the engineering post&\#x27;s headline and framing were available here, the scope, timeline, and performance results of the migration cannot be verified.

**「Community Discussion」** Commenters largely agreed that the React Native versus native choice is a context-dependent engineering tradeoff rather than an absolute good or bad, though several argued the old motivation of reusing web developers has weakened as AI code generation improves and startups eventually hire dedicated native engineers. One commenter described migrating a 15–20 screen app from React Native to native iOS and Android overnight using Codex and Maestro before spending a few days polishing, while another said the cross-platform cycle is decades old and often fails to reduce headcount cost as promised.

<details><summary>References</summary>
<ul>
<li><a href="https://shopify.engineering/back-to-native">Native is now the future of mobile at Shopify (2026) - Shopify</a></li>
<li><a href="https://shopify.engineering/react-native-new-architecture">Migrating to React Native&#x27;s New Architecture (2025) - Shopify</a></li>
<li><a href="https://shopify.engineering/shop-app-migration">Migrating Shop app from React Native to native (2026) - Shopify</a></li>
<li><a href="https://shopify.engineering/back-to-native">Native is now the future of mobile at Shopify (2026) - Shopify</a></li>

</ul>
</details>

**Tags**: `#React Native`, `#native mobile development`, `#cross-platform development`, `#Shopify`, `#software engineering tradeoffs`

---

<a id="item-tech-news-2"></a>
### [Calif Research claims AI-built zero-click WeChat worm](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 8.0/10

Calif Research has released a demo of WeWorm, which it describes as the first zero-click worm to spread through WeChat calls on both iOS and Android. According to the announcement, victims do not need to answer the call or interact with their phone, and even if they answer they hear nothing while the exploit still succeeds. The team says that working with AI it found the bug and wrote the first remote code execution exploit in about two days, with building the worm taking one more week. Calif Research claims such a worm would previously have taken a larger team months, and that AI can already do most of the work while humans provided judgment about targeting and safe testing. The item is a short quoted announcement and demo summary without technical detail or independent verification, so the claims remain unsubstantiated.

rss · Simon Willison · Sep 10, 00:56

**「Background」** A zero-click exploit compromises a device without any action from the target — no tap, no answered call, no notification interaction — while a worm is malware that self-propagates by moving automatically from one victim&\#x27;s account or contacts to the next. WeChat, Tencent&\#x27;s messaging app, reaches over a billion phones or accounts, which is what makes an automatically spreading flaw in its voice-call feature unusually consequential. Calif Research presents WeWorm as a demo or proof-of-concept, and its published timeline places the first Android RCE on July 30, the iOS RCE on August 2, and the polished cross-platform worm demo on August 11, but the claim has not been independently verified.

**「Impact」** If the claim holds, the two days Calif Research says it needed for an AI-assisted WeChat RCE plus one week for the worm would compress zero-click exploit work that once took a larger team months, sharply narrowing the patch window for WeChat users on iOS and Android. The claim rests on a demo announcement with no technical detail or independent verification, and external reporting of AI-assisted zero-days supports only the broader trend, not this specific exploit.

<details><summary>References</summary>
<ul>
<li><a href="https://calif.io/research/weworm">WeWorm | Calif</a></li>
<li><a href="https://www.helpnetsecurity.com/2026/09/08/wechat-weworm-vulnerability-exploit-account-hijacking/">&quot;Zero-click&quot; WeChat worm could hijack accounts and spread via a single call - Help Net Security</a></li>
<li><a href="https://calif.io/research/weworm">WeWorm | Calif</a></li>
<li><a href="https://bishopfox.com/podcasts/ai-zero-day-exploit-ci-cd-supply-chain-poisoning-and-vibe-coded-data-exposure">AI Zero - Day Exploit , CI/CD Supply Chain Poisoning, and… | Bishop Fox</a></li>
<li><a href="https://articles.phantom-byte.com/five-days-to-zero-day-ai-exploit-threat-model.html">Five Days to Zero - Day : AI Exploit Threat Model - PhantomByte</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#zero-click exploit`, `#mobile security`, `#WeChat`, `#AI-assisted exploit development`

---

<a id="item-tech-news-3"></a>
### [Rust Is Now a Tier-1 Language at Microsoft](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 7.0/10

Microsoft has designated Rust as a tier-1 language, according to a guest post published by the Rust Foundation. The designation is a strategic and organizational commitment rather than a new technical release, but it signals Microsoft&\#x27;s growing emphasis on memory safety across its products and platforms. Microsoft&\#x27;s interest in Rust has been linked to memory-safety priorities: commenters cited Azure CTO Mark Russinovich&\#x27;s RustCon talk stating that 70% of Microsoft&\#x27;s CVEs are memory-safety issues. The announcement is notable as an industry-adoption milestone for Rust and may affect how Microsoft approaches systems programming and tooling, though it is not a product release or research breakthrough.

hackernews · mmastrac · Sep 10, 13:39 · [Discussion](https://news.ycombinator.com/item?id=49643546)

**「Background」** Rust is a systems programming language whose memory-safety guarantees have been a strategic interest at Microsoft for years, from Azure CTO Mark Russinovich&\#x27;s public statements on native-code strategy to the company&\#x27;s funding of the Rust Project. Microsoft&\#x27;s &quot;tier-1&quot; designation means Rust receives the same level of internal support as C++, C\#, and TypeScript, including secure toolchain builds, developer tooling, quality workflows, and compliance with the company&\#x27;s security requirements. The push is driven in part by memory-safety bugs accounting for roughly 70% of Microsoft&\#x27;s CVEs, a figure reported to be consistent across Google, Apple, and the Linux kernel.

**「Impact」** For developers and teams building on Microsoft platforms, making Rust a tier-1 language means it joins C++ and C\# as an officially supported option for systems and greenfield work, consistent with Microsoft&\#x27;s stated aim of migrating roughly 1 billion lines of C/C++ code to Rust by 2030. Because this is a strategic designation tied to the company&\#x27;s memory-safety push rather than a shipped release, concrete toolchain, MSVC-integration, and platform deliverables remain unconfirmed.

**「Community Discussion」** Commenters largely welcomed the move, seeing Rust as a mature, serious competitor to C++ and C\# that is more polished than newer &quot;better C/C++&quot; languages such as Zig and Odin. They also cited Microsoft goals to convert 1 billion lines of code to Rust by 2030 through automated tooling and DARPA work on C-to-Rust conversion, while raising side concerns about Windows 11&\#x27;s resource use and hardware requirements and noting rumors of MSVC integration.

<details><summary>References</summary>
<ul>
<li><a href="https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/">Guest Post: Rust Is Tier-1 Language at Microsoft</a></li>
<li><a href="https://newzino.com/story/rust-is-tier-1-language-at-microsoft-d647be">Microsoft makes Rust a Tier-1 language for internal ...</a></li>
<li><a href="https://rustify.rs/articles/rust-memory-safety-nsa-cisa-2026">Rust &amp; Memory Safety: What NSA, CISA &amp; White House Say (2026)</a></li>
<li><a href="https://www.buildmvpfast.com/blog/rust-replacing-cpp-cloud-infrastructure-microsoft-azure-2026">Microsoft Rust Mandate Azure C++ Migration 2026</a></li>
<li><a href="https://www.globalbrandsmagazine.com/microsoft-shifts-from-c-to-rust/">Microsoft Shifts from C++ to Rust by 2030: Key Insights</a></li>

</ul>
</details>

**Tags**: `#Rust`, `#Microsoft`, `#memory safety`, `#programming languages`, `#industry adoption`

---