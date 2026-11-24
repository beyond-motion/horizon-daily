---
layout: default
title: "Horizon Summary: 2026-11-24 (EN)"
date: 2026-11-24
lang: en
---

> From 6 items, 3 important content pieces were selected

---

**Technology News**
1. [Ladybird releases first alpha for macOS and Linux](#item-tech-news-1) ⭐️ 8.0/10
2. [GPT-6.2 Astra Identifies 1808 Sketchbook Creator in 22 Minutes](#item-tech-news-2) ⭐️ 7.0/10
3. [Z.ai Releases GLM-5.4, Its First Looped Transformer Coding Model](#item-tech-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Ladybird releases first alpha for macOS and Linux](https://simonwillison.net/2026/Nov/23/ladybird/) ⭐️ 8.0/10

Ladybird released its first alpha, making its independent browser engine installable on macOS and Linux without users compiling it themselves. The project implements most core web platform components—including HTML parsing, CSS, layout, JavaScript, and WebAssembly—while still using external components such as HarfBuzz, Skia, ffmpeg, and SQLite. Simon Willison reported that the alpha felt fast and lightweight and that most sites worked, including WebAssembly-based ffmpeg and Pyodide tools, but Datasette Lite failed on an unimplemented navigator.serviceWorker.startMessages call already marked FIXME in the source. The release follows an October development surge in which Ladybird gained 75,650 web-platform-tests passes, reaching 2,184,722 and overtaking Safari&\#x27;s 2,172,990, with AI coding agents filling in missing functionality. The alpha is explicitly unstable: some websites will not work, and the browser will sometimes crash.

rss · Simon Willison · Nov 23, 21:46

**「Background」** Ladybird is an independent browser project with its own implementations of HTML parsing, CSS, layout, JavaScript, and WebAssembly, rather than a Chromium- or Gecko-based browser. It draws code from the earlier SerenityOS project and still uses external libraries such as HarfBuzz, Skia, ffmpeg, and SQLite. An alpha release is an early, unstable build intended for testing and feedback, not daily production use.

**「Impact」** macOS and Linux users can now install and test Ladybird without compiling it, though sites relying on unimplemented APIs such as navigator.serviceWorker.startMessages—including Datasette Lite—will still fail.

**Tags**: `#Ladybird`, `#web browsers`, `#open source`, `#browser engines`, `#alpha release`

---

<a id="item-tech-news-2"></a>
### [GPT-6.2 Astra Identifies 1808 Sketchbook Creator in 22 Minutes](https://simonwillison.net/2026/Nov/24/astra-historical-mystery/) ⭐️ 7.0/10

Simon Willison highlighted a case study by history professor Mark Humphries in which GPT-6.2 Astra, with minimal prompting, autonomously identified the creator of an anonymous 1808 sketchbook held at Yale&\#x27;s Beinecke Library in 22 minutes using publicly available primary and secondary sources. According to the account, the model found a little-known source in a paper archive, predicted that examining it would confirm its hypothesis, and was correct; the source is described as a major find for Canadian and fur-trade historians. Astra reportedly traced a diary reference to a visit by the vicomte de Chabot five days before a date in the sketchbook near a nearby river and suggested that Chabot&\#x27;s journal, available only by order from Cleveland State University, might confirm the attribution. Humphries expects only a mild crisis of confidence for historians, less severe than in mathematics, because historians reinterpret the past and produce literature rather than pursue a single universal truth. The item is a brief secondhand excerpt, so the claims have not been independently verified in the supplied material.

rss · Simon Willison · Nov 24, 16:53

**「Background」** The item concerns an anonymous 1808 sketchbook held at Yale&\#x27;s Beinecke Library, a rare-book and manuscript archive; secondary coverage describes the volume as recording a journey from Montreal to Lake Superior with only four dated images as clues to its author. Attributing unsigned archival material normally depends on correlating travel dates, routes, and provenance with independent documents such as diaries, journals, and paper archives. GPT-6.2 Astra is the model and agent in the case study, which historian Mark Humphries says was given minimal prompting and worked from publicly available primary and secondary sources.

**「Impact」** For historians and cultural institutions, the case suggests agentic AI could speed provenance research by proposing and testing archival hypotheses, but the evidence here is a short secondhand summary rather than a peer-reviewed demonstration.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=Lfgz2tLJGEM">Mark Humphries fed an 1808 Yale sketchbook to GPT-6.2 Astra # ...</a></li>
<li><a href="https://blockchain.news/ainews/gpt-6-2-astra-traced-1808-sketchbook-to-vicomte-de-chabot">GPT-6.2 Astra traced 1808 sketchbook to vicomte de Chabot</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#historical research`, `#GPT-6.2 Astra`, `#case study`

---

<a id="item-tech-news-3"></a>
### [Z.ai Releases GLM-5.4, Its First Looped Transformer Coding Model](https://simonwillison.net/2026/Nov/23/glm-54/) ⭐️ 7.0/10

Z.ai released GLM-5.4, its first model built on a looped transformer architecture. In a looped transformer, a group of weight-shared layers runs for multiple iterations and refines hidden states from the previous pass, yielding a deeper network without increasing parameter count; the release follows Thinking Machines Lab&\#x27;s November 20 Inkling 2 Mini, which runs middle layers three times per token. GLM-5.4 is not yet available as open weights—Z.ai says it plans to open-source them after safety hardening—and it currently requires the Coding Plan subscription rather than the regular API, though both share the same OpenAI-compatible Responses API at https://api.z.ai/api/v1. Simon Willison built an llm-glm plugin because Tommy Hughes&\#x27;s existing llm-zai plugin does not yet support the new model, and he expects to retire his once llm-zai catches up. In pelican SVG tests at low, high, and max effort, GLM-5.4 looked similar in quality to GLM-5.3 and more comparable to OpenAI and Anthropic outputs than earlier GLM generations, and the source provided no benchmark results.

rss · Simon Willison · Nov 23, 23:40

**「Background」** Looped transformers address a constraint of standard Transformers, in which every layer runs once per forward pass: they execute a shared block of layers for multiple iterations, refining the hidden states from the previous pass and gaining effective depth without increasing the parameter count. The approach is not new, but it drew attention in November 2026 when Thinking Machines Lab released Inkling 2 Mini on November 20 and Z.ai released GLM-5.4, its first flagship built on the architecture, on November 23. Z.ai says the design can match models with 2T–3T parameters.

**「Impact」** Developers who want to use GLM-5.4 must go through Z.ai&\#x27;s Coding Plan subscription, since the model is not yet reachable via the regular API, and self-hosting is off the table until open weights ship after safety hardening. Prospective adopters also have no published benchmarks or API pricing to evaluate it against GLM-5.3 or rival models.

<details><summary>References</summary>
<ul>
<li><a href="https://z.ai/blog/glm-5.4">GLM-5.4: Toward Generalized Coding with Our First Loop ...</a></li>
<li><a href="https://dev.to/amananandrai/loop-transformers-thinking-deeper-without-getting-bigger-glm-54-inkling-2-mini-501m">Loop Transformers: Thinking Deeper Without Getting Bigger ...</a></li>
<li><a href="https://thenextweb.com/news/zai-glm-5-4-loop-transformer-coding-model">Z . ai ’s GLM - 5 . 4 runs its layers twice to rival 2T-parameter models</a></li>
<li><a href="https://www.orcarouter.ai/blog/glm-5-4-release-what-we-know">GLM - 5 . 4 Arrives on Z . ai &#x27;s Coding Plan: No Benchmarks Yet</a></li>
<li><a href="https://www.youtube.com/watch?v=J7cqbnLtPTs">OPUS 5.6 LEAKED?! GLM - 5 . 4 Loop Model, Neon vs Opus... - YouTube</a></li>

</ul>
</details>

**Tags**: `#looped transformers`, `#LLM architecture`, `#GLM-5.4`, `#Z.ai`, `#AI model releases`

---