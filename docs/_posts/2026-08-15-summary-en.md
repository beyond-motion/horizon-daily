---
layout: default
title: "Horizon Summary: 2026-08-15 (EN)"
date: 2026-08-15
lang: en
---

> From 3 items, 2 important content pieces were selected

---

**Technology News**
1. [AI-Driven Kernel Optimization Reports a 232x Speedup](#item-tech-news-1) ⭐️ 7.0/10
2. [Don&\#x27;t Classify, Hallucinate: Mapping Imagined Tags with Embeddings](#item-tech-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [AI-Driven Kernel Optimization Reports a 232x Speedup](https://sankalp.bearblog.dev/autoresearch/) ⭐️ 7.0/10

A developer describes using Codex in an auto-research loop to optimize a kernel, reporting a 232x speedup on the target workload. The loop involved repeatedly benchmarking, profiling, verifying, and improving the code, with Codex driving research and implementation between iterations. The result matters as a concrete example of an LLM-based agent acting as an autonomous performance engineer on a narrow numerical task. The source item does not include the technical details needed to verify the optimization, and community comments emphasize that such automated approaches can lose generality and robustness outside the exact inputs used during optimization.

hackernews · tosh · Aug 15, 11:00 · [Discussion](https://news.ycombinator.com/item?id=49309549)

**「Background」** Codex is an AI coding assistant that can generate and modify code from natural-language instructions. An &quot;auto-research loop&quot; typically combines profiling, research, and iterative code changes to optimize performance. The article describes applying this approach to a kernel that performs QR decomposition, a matrix factorization used in numerical linear algebra, with references to Householder reflections and algorithmic improvements. Such kernels are often written for GPUs or SIMD hardware, where small optimizations can produce large speedups.

**「Community Discussion」** Commenters shared related experiments: one tried a benchmark-profile-verify-research-improve loop with DeepSeek v4 on a video codec that has a bitstream verifier, while another observed that 8 of 10 competition solutions produced this way broke on out-of-distribution shapes, with only expert-adjusted, reasonably bounded solutions remaining robust. The overall sentiment is that these loops can work, but they tend to overfit unless humans constrain and steer the optimization.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49309549">Auto - research with codex : How I achieved a 232 x Faster Kernel</a></li>
<li><a href="https://sankalp.bearblog.dev/autoresearch/">Auto - research with codex : How I achieved a 232 x Faster Kernel ...</a></li>
<li><a href="https://vk.ru/wall-55993443_67318">Article URL: https://sankalp.bearblog.dev/autoresearch/ Comments...</a></li>

</ul>
</details>

**Tags**: `#AI-assisted development`, `#performance optimization`, `#kernel`, `#Codex`, `#software engineering`

---

<a id="item-tech-news-2"></a>
### [Don&\#x27;t Classify, Hallucinate: Mapping Imagined Tags with Embeddings](https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/) ⭐️ 7.0/10

Simon Willison highlights Doug Turnbull&\#x27;s technique for tagging content against a very large vocabulary: instead of asking an LLM to pick from thousands of existing tags, let the model freely hallucinate candidate tags and then use vector embeddings to match those imagined tags to the closest real tags in the existing corpus. Willison notes his own blog has 1,856 tags, too many to feed to an LLM in one prompt. Turnbull&\#x27;s example prompt includes a few sample tag shapes, such as &quot;Furniture / Living Room Furniture / Coffee Tables &amp; End Tables / Coffee Tables,&quot; to guide the model toward useful hypothetical classifications. This approach avoids the context-window and enumeration problems of large classification vocabularies while still mapping output back to concrete, known tags.

rss · Simon Willison · Aug 14, 21:54

**「Background」** Classifying content with LLMs usually requires restricting output to a fixed set of allowed tags or categories, but large vocabularies can exceed prompt limits or cause errors. Doug Turnbull&\#x27;s &quot;hallucinate&quot; approach avoids that by letting the LLM freely propose hypothetical tags, then using vector embeddings to map each guess to the nearest existing tag in the vocabulary. This builds on embeddings that place similar words and concepts near each other in vector space, enabling fuzzy matching without listing all possible tags.

**「Impact」** Bloggers, search engineers, and AI practitioners who need to classify content against thousands of predefined tags can use this hallucinate-then-embed approach to work around context limits and vocabulary size, enabling practical auto-tagging of legacy or unlabeled content.

<details><summary>References</summary>
<ul>
<li><a href="https://softwaredoug.com/blog/2026/08/10/hypothetical-classifications">Don &#x27; t classify . Hallucinate ! | Doug Turnbull &#x27;s Blog</a></li>

</ul>
</details>

**Tags**: `#LLM classification`, `#embeddings`, `#tagging`, `#prompt engineering`, `#vector search`

---