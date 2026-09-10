---
layout: default
title: "Horizon Summary: 2026-09-10 (EN)"
date: 2026-09-10
lang: en
---

> From 6 items, 3 important content pieces were selected

---

**Technology News**
1. [Calif Research releases WeWorm zero-click worm](#item-tech-news-1) ⭐️ 9.0/10
2. [Shopify migrates from React Native to native mobile platforms](#item-tech-news-2) ⭐️ 7.0/10
3. [Windows XP Initial User Picture Selection Algorithm](#item-tech-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Calif Research releases WeWorm zero-click worm](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research has released a demo of WeWorm, the first zero-click worm capable of spreading through WeChat calls on both iOS and Android platforms. The exploit functions without any user interaction, meaning victims do not need to answer or even see the incoming call for the attack to succeed. The development team utilized AI assistance to identify the underlying vulnerability and write the initial remote code execution \(RCE\) exploit in approximately two days, with the full worm construction taking an additional week. This rapid timeline contrasts sharply with traditional methods, which typically require larger teams and several months to achieve similar results.

rss · Simon Willison · Sep 10, 00:56

**「Background」** Zero-click exploits are high-value security vulnerabilities that allow attackers to compromise devices without any action from the target, making them particularly dangerous and difficult to detect. Historically, developing such complex malware requires significant human expertise and time, often involving extensive manual reverse engineering and testing by specialized security research teams.

**「Impact」** This release demonstrates that AI-assisted development can drastically reduce the time and resources required to create sophisticated mobile worms, potentially lowering the barrier to entry for advanced cyber threats. It signals a paradigm shift in cybersecurity where human judgment is increasingly augmented by AI for rapid exploit generation and testing.

**Tags**: `#AI Security`, `#Zero-Click Exploits`, `#Mobile Security`, `#Malware Development`, `#AI-Assisted Research`

---

<a id="item-tech-news-2"></a>
### [Shopify migrates from React Native to native mobile platforms](https://shopify.engineering/back-to-native) ⭐️ 7.0/10

Shopify has announced a strategic migration of its mobile applications from React Native back to native iOS and Android codebases. This decision reflects a broader industry trend where companies re-evaluate cross-platform frameworks in favor of native development, often leveraging modern AI-assisted tooling to mitigate the traditional costs and complexity of maintaining separate codebases. The move highlights the ongoing engineering trade-offs between development speed, performance, and long-term maintainability in mobile app architecture.

hackernews · fnthawar2 · Sep 10, 14:09 · [Discussion](https://news.ycombinator.com/item?id=49643982)

**「Background」** React Native is a widely used open-source framework that allows developers to build mobile applications using JavaScript and React, enabling code sharing across iOS and Android platforms. Native development refers to writing platform-specific code \(such as Swift for iOS or Kotlin/Java for Android\) to access device hardware and operating system features directly, often providing better performance and deeper integration but requiring separate codebases.

**「Community Discussion」** Developers view this as a pragmatic engineering decision driven by resource constraints rather than an absolute rejection of cross-platform tools. Some community members report that large-scale migrations can now be executed rapidly using LLMs like Codex, while others caution that such success stories may not generalize to all mid-sized applications without significant prior preparation.

**Tags**: `#Mobile Development`, `#Software Architecture`, `#React Native`, `#Engineering Decisions`

---

<a id="item-tech-news-3"></a>
### [Windows XP Initial User Picture Selection Algorithm](https://devblogs.microsoft.com/oldnewthing/20260909-00/?p=112683) ⭐️ 7.0/10

A recent analysis of Windows XP internals reveals the specific algorithm used to randomly select initial user profile pictures during account setup. This technical deep-dive, originally discussed by Raymond Chen, highlights how legacy operating systems handled file enumeration and randomness without modern abstractions. The discovery offers valuable educational insights for software engineers interested in OS history, legacy code analysis, and fundamental programming concepts regarding random selection from a set.

hackernews · soheilpro · Sep 10, 09:04 · [Discussion](https://news.ycombinator.com/item?id=49640646)

**「Background」** Windows XP, released in 2001, introduced the ability for users to customize their login screen with personal images. The operating system&\#x27;s user profile setup process included a feature to randomly select an initial picture from a predefined directory of available images.

**「Impact」** This insight aids developers and historians in understanding the practical constraints and design choices of early Windows architecture. It serves as a concrete example of how low-level system tasks were implemented before high-level libraries became standard.

**「Community Discussion」** Commenters appreciate the detailed look at Windows internals, with some noting that such simple-seeming problems often require careful consideration to avoid pitfalls like counting files first. Others share links to source code repositories and reflect on the cognitive differences between human intuition and computer execution when handling randomness.

<details><summary>References</summary>
<ul>
<li><a href="https://devblogs.microsoft.com/oldnewthing/20260909-00/?p=112683">What algorithm did Windows XP use to choose your initial user picture?</a></li>
<li><a href="https://www.scribd.com/document/586119354/Raymond-Chen-The-Old-New-Thing-Practical-Development-Throughout-the-Evolution-of-Windows-Addison-Wesley-2007">Raymond Chen - The Old New Thing - Practical Development Throughout ...</a></li>

</ul>
</details>

**Tags**: `#Windows Internals`, `#Legacy Systems`, `#Algorithm Design`, `#Software Engineering History`

---