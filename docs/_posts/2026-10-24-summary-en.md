---
layout: default
title: "Horizon Summary: 2026-10-24 (EN)"
date: 2026-10-24
lang: en
---

> From 6 items, 3 important content pieces were selected

---

**Technology News**
1. [Moonshot&\#x27;s Kimi K3.1 Pro hits API with frontier-level scores](#item-tech-news-1) ⭐️ 8.0/10
2. [HTTP2Shell Brotli RCE reported across many HTTP libraries](#item-tech-news-2) ⭐️ 7.0/10
3. [OBS Studio 33 ships overdue CEF security update](#item-tech-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Moonshot&\#x27;s Kimi K3.1 Pro hits API with frontier-level scores](https://simonwillison.net/2026/Oct/23/kimi-k31-pro/) ⭐️ 8.0/10

Moonshot AI released Kimi K3.1 Pro on the Kimi API, with full model weights promised by November 4, 2026 — the model is not yet open weights. Pricing is $2.00 per million input tokens and $10 per million output tokens, matching GPT-6.1 Sol at half the price of Claude Opus 5.5, and a &quot;Highspeed&quot; tier runs 2-3x faster at twice the price, except for input token cache hits, which are priced the same. Moonshot&\#x27;s own benchmarks place Kimi roughly level with Opus 5.5 and GPT-6 Astra, beating them on some tests and nearing them on others. Artificial Analysis scored the model 55, ahead of Claude Fable 5.1, GPT-6 Astra, and Gemini 4 Argon \(all 53\) and behind only Claude Opus 5.5 at 58; Simon Willison notes this is the first time a soon-to-be open-weight model has scored this highly against the frontier. Willison tested it through the Moonshot API using the \`llm openai endpoint\` command added in LLM 0.32, generating pelican SVGs at the low, medium, and max reasoning levels it supports and comparing them against Kimi K3.

rss · Simon Willison · Oct 23, 19:40

**「Background」** Moonshot AI is a Chinese lab whose Kimi models have been released under open weights, making it possible to download and self-host them rather than only call an API. Benchmark vendors and independent evaluators like Artificial Analysis score frontier models on standardized tasks, but vendor-reported comparisons are typically the most favorable evidence available at launch. A high score from a model whose weights are not yet published therefore remains provisional until the weights actually ship.

**「Impact」** Developers gain an OpenAI-compatible endpoint priced at $2/$10 per million tokens that can be swapped in with existing tooling, but teams planning to self-host should treat the announced November 4, 2026 weight release as a stated intention rather than a shipped capability.

**Tags**: `#Kimi`, `#Moonshot AI`, `#LLM releases`, `#model pricing`, `#benchmarks`

---

<a id="item-tech-news-2"></a>
### [HTTP2Shell Brotli RCE reported across many HTTP libraries](https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497) ⭐️ 7.0/10

A newly publicized Brotli-related remote code execution vulnerability, rebranded from Node2Shell to HTTP2Shell, is reported to affect many HTTP libraries and applications. The issue is tied to Brotli decompression, with discussion describing it as unauthenticated RCE that can work in both directions, although the available material does not clearly establish which packages or configurations are affected in practice. The broad HTTP framing and the new name have drawn scrutiny because the flaw may also be reachable outside HTTP when Brotli decoding is used manually. The report is significant because it concerns widely used HTTP software and an RCE class of bug, but the scope and severity depend on how commonly Brotli-compressed request bodies are supported and enabled.

hackernews · theanonymousone · Oct 24, 08:06 · [Discussion](https://news.ycombinator.com/item?id=50219177)

**「Background」** Brotli is a general-purpose compression algorithm that HTTP clients and servers commonly negotiate through the Content-Encoding header, and CVE-2026-111497 is an out-of-bounds write in the Brotli decoder bundled with Node.js that the project says can permit remote code execution, with fixes released for the 22.x, 24.x and 26.x lines. The flaw is reachable over ordinary HTTP paths, such as Brotli-compressed responses consumed by fetch\(\) or incoming Brotli request bodies decoded by middleware. It was initially publicized as Node2Shell and framed around Node.js, but the same Brotli bindings—brotli or brotlicffi—are used by many other HTTP libraries and applications, which is why the disclosure has been rebranded HTTP2Shell with a correspondingly wider blast radius.

**「Who is affected」** Developers and operators running Node.js 22.x, 24.x, or 26.x with the bundled Brotli decoder, along with applications that decode Brotli through libraries such as brotlicffi, should upgrade to the fixed releases, since the out-of-bounds write can permit remote code execution. The precise set of reachable configurations remains disputed in the discussion, where commenters note the flaw can also be triggered by manual Brotli decoding rather than HTTP alone.

**「Community discussion」** Commenters broadly criticized the HTTP2Shell name as overly broad and sensational, with several preferring Brotli2Shell or Broccoli2Shell because the flaw can occur wherever Brotli is decoded, not only over HTTP. They also questioned the article’s clarity on how many affected libraries actually support Brotli-compressed request bodies in common configurations versus other Brotli uses, and one commenter asked how a reported unauthenticated RCE could have been fixed in February without being recognized as a security issue.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aikido.dev/blog/node2shell-nodejs-brotli-rce-cve-2026-111497">Node 2 Shell : Node .js Brotli vulnerability allows remote code ...</a></li>
<li><a href="https://www.imperva.com/blog/node2shell-from-brotli-data-to-remote-code-execution/">Node 2 Shell : From Brotli Data to Remote Code Execution | Imperva</a></li>
<li><a href="https://dbu.gs/vulnerability/PT-2026-120553">CVE - 2026 - 111497 — DoS in Openjs Foundation Node.Js | dbugs</a></li>
<li><a href="https://www.aikido.dev/blog/node2shell-nodejs-brotli-rce-cve-2026-111497">Node 2 Shell : Node.js Brotli vulnerability allows remote code...</a></li>
<li><a href="https://www.imperva.com/blog/node2shell-from-brotli-data-to-remote-code-execution/">Node 2 Shell : From Brotli Data to Remote Code Execution | Imperva</a></li>

</ul>
</details>

**Tags**: `#security vulnerability`, `#Brotli`, `#remote code execution`, `#HTTP libraries`, `#open source security`

---

<a id="item-tech-news-3"></a>
### [OBS Studio 33 ships overdue CEF security update](https://github.com/obsproject/obs-studio/releases/tag/33.0.0) ⭐️ 7.0/10

OBS Studio 33 has been released, and the most prominent change discussed by commenters is an update to Chromium Embedded Framework from 127/6533 to 150/7871. The release matters because OBS is a widely used open-source streaming tool, and the older CEF version had been linked in community discussion to in-the-wild remote code execution exploits that drew media coverage. Commenters say the fix arrived about a month after those exploits became widely known and describe the previous framework version as roughly two years out of date. No detailed release notes were supplied, so other changes in OBS Studio 33 are not covered here.

hackernews · pentagrama · Oct 24, 04:49 · [Discussion](https://news.ycombinator.com/item?id=50218430)

**「Background」** OBS Studio is a widely used open-source application for recording and live streaming video, and version 33 is a major release of that project. Its browser sources and docks rely on the Chromium Embedded Framework \(CEF\), an open-source framework for embedding a Chromium browser within another application. OBS 33 updates CEF from 127/6533, associated with a July 2024 release, to 150/7871 from September 2026; the project describes this as a massive backend update that should be invisible to users.

**「Impact」** For OBS users, especially those loading browser-based sources, moving to version 33 is the concrete mitigation for the CEF vulnerability discussed by commenters.

**「Community discussion」** Commenters broadly welcomed the release: one celebrated the CEF jump as “Finally” after the exploits, and another thanked the OBS developers while describing reliability problems with Zoom recordings. Others shared adjacent uses, including VDO.ninja for low-latency browser video and an HDMI-capture setup feeding OBS.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chromium_Embedded_Framework">Chromium Embedded Framework - Wikipedia</a></li>
<li><a href="https://github.com/obsproject/obs-studio/releases">Releases · obsproject/ obs - studio</a></li>

</ul>
</details>

**Tags**: `#OBS Studio`, `#security update`, `#Chromium Embedded Framework`, `#open-source software`, `#video streaming`

---