---
layout: default
title: "Horizon Summary: 2026-10-31 (EN)"
date: 2026-10-31
lang: en
---

> From 7 items, 2 important content pieces were selected

---

**Technology News**
1. [ChatGPT account-takeover flaw fixed; $5,000 bounty criticized](#item-tech-news-1) ⭐️ 7.0/10
2. [NES CPU emulator embedded in Qwen3.5-4B weights](#item-tech-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [ChatGPT account-takeover flaw fixed; $5,000 bounty criticized](https://www.parameter.ai/labs/we-found-a-gap-at-openai) ⭐️ 7.0/10

A write-up on Parameter.ai describes a ChatGPT account-takeover vulnerability that OpenAI confirmed and fixed, with a total bounty of $5,000. The reported attack required the user to click a link, according to discussion quoting the disclosure. The case matters because account takeover can expose ChatGPT accounts, and the payout has sparked debate over whether bug bounties adequately reward responsible disclosure. The supplied material does not detail the affected frontends, exploitation steps, or the remediation timeline.

hackernews · armcat · Oct 31, 10:30 · [Discussion](https://news.ycombinator.com/item?id=50314699)

**「Background」** Account takeover in a web application generally means an attacker gains the ability to act as another user without their credentials; in ChatGPT&\#x27;s case the researchers achieved this by getting arbitrary JavaScript to run as chatgpt.com, having a trusted component in the main page create an unsandboxed document and thereby cross the boundary from the isolated Preview frontend on its separate address. Such cross-site scripting flaws are typically reported through vendor bug bounty programs, which pay researchers according to the severity and impact of the finding. OpenAI confirmed both frontends rejected the reported messages, fixed the issue, and paid a $5,000 bounty.

**「Impact」** For ChatGPT users, the reported fix closes a link-based account-takeover path, while the $5,000 payout raises concerns that low rewards could discourage future responsible disclosure.

**「Community discussion」** Commenters broadly criticized the $5,000 bounty as too low, arguing it could discourage responsible reporting or push researchers to sell exploits on the black market. Some also blamed OpenAI&\#x27;s software complexity and bug surface, but the thread did not dispute that the reported issue was fixed.

<details><summary>References</summary>
<ul>
<li><a href="https://www.parameter.ai/labs/we-found-a-gap-at-openai">Do the Math: How We Took Over ChatGPT Accounts - Parameter</a></li>
<li><a href="https://news.ycombinator.com/item?id=50314699">We Took over ChatGPT Accounts | Hacker News</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#ChatGPT`, `#account takeover`, `#vulnerability disclosure`, `#bug bounty`

---

<a id="item-tech-news-2"></a>
### [NES CPU emulator embedded in Qwen3.5-4B weights](https://simonwillison.net/2026/Oct/30/nesformer/) ⭐️ 7.0/10

Drew Breunig has released dbreunig/nesformer, an experimental project that embeds a working emulator for the Nintendo Entertainment System&\#x27;s 6502 CPU in the weights of Qwen3.5-4B. Inspired by Divyansh Agrawal&\#x27;s qwenputer, the project lets users run NES ROMs such as Super Mario Bros inside the model, though very slowly. In a Hacker News comment, Breunig revealed the Opus 5.5 prompts he used to explore the idea and then build a version with the weights and a command-line interface that can be pointed at a ROM. The project also used Christopher Pow&\#x27;s collection of NES CPU conformance tests, released 15 years ago. The result is presented as a proof of concept rather than a fast emulator.

rss · Simon Willison · Oct 30, 21:59

**「Background」** The project follows Qwenputer, an experiment by Divyansh Agrawal that compiled a 32-bit RISC-V CPU directly into the weights of a stock Qwen 3.5-4B model and used its Gated DeltaNet layers as RAM rather than running the CPU as an external plugin or tool \[tool-1-1\]\[tool-1-2\]. Nesformer applies the same weight-embedding idea to the NES’s 6502 CPU—the core of its 2A03 chip—along with its 2 KB of work RAM and a cartridge’s program ROM inside a standard Qwen3\_5ForCausalLM checkpoint \[tool-2-1\]. This makes it a proof-of-concept for running a classic console’s processor inside an LLM’s parameters, albeit at roughly 1 to 6 seconds per frame \[tool-2-2\].

<details><summary>References</summary>
<ul>
<li><a href="https://divagr.com/blog/qwenputer">Qwenputer : a fully functioning, deterministic RISC-V CPU inside...</a></li>
<li><a href="https://github.com/divagr18/qwenputer">GitHub - divagr18/ qwenputer : A computer, compiled into the weights ...</a></li>
<li><a href="https://github.com/dbreunig/nesformer">GitHub - dbreunig/nesformer: An NES CPU compiled into the ...</a></li>
<li><a href="https://explainx.ai/blog/nesformer-nes-cpu-compiled-into-qwen3-5-4b-weights-super-mario-bros-qwenputer-2026">Nesformer: NES Emulator Inside Qwen3.5 Weights Explained ...</a></li>

</ul>
</details>

**Tags**: `#LLM weight embedding`, `#NES emulation`, `#Qwen`, `#experimental AI`, `#systems hacking`

---