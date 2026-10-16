---
layout: default
title: "Horizon Summary: 2026-10-16 (EN)"
date: 2026-10-16
lang: en
---

> From 5 items, 1 important content pieces were selected

---

**Technology News**
1. [Chirp Pong: two-player phone game networked by audio chirps](#item-tech-news-1) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Chirp Pong: two-player phone game networked by audio chirps](https://simonwillison.net/2026/Oct/15/chirp-pong/) ⭐️ 7.0/10

Simon Willison released Chirp Pong, a two-player competitive game for two phones placed close together in which game state is transmitted as audio chirps that the web microphone API interprets. The game runs as static HTML with no server-side networking, and Willison describes it as an experiment to test whether phone-to-phone networking via microphone-detected chirps was feasible; he reports that it appears to work. He built it with Claude Opus 5.5 Extra inside Claude Code, using a prompt that asked for a competitive pong-like game with graphical and gameplay twists to make it more intertwined than pong. The published post is brief and does not include detailed implementation notes, latency figures, or browser compatibility information, so the reliability and range of the chirp link remain untested in the source.

rss · Simon Willison · Oct 15, 19:47

**「Background」** Chirp Pong depends on the browser&\#x27;s Web Audio and microphone APIs, which allow a static HTML page to both emit and detect sound without any server-side networking layer. This is a form of data-over-sound networking: one phone plays encoded audio chirps through its speaker while the other listens through its microphone, so game state travels over the air instead of over Wi-Fi or Bluetooth. Simon Willison built the experiment by prompting Claude Opus 5.5 Extra inside Claude Code, Anthropic&\#x27;s command-line coding assistant, making the project a demonstration of LLM-assisted software development as much as of acoustic networking.

**「Impact」** For developers, the demo is a working example that static, serverless HTML pages can exchange state between nearby phones using only the microphone and speakers, a pattern relevant to local multiplayer games and offline peer-to-peer experiments, though the source provides no evidence yet about latency, accuracy, or browser support.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/">Claude</a></li>

</ul>
</details>

**Tags**: `#AI-assisted development`, `#Web Audio API`, `#game design`, `#experimental tooling`, `#LLM code generation`

---