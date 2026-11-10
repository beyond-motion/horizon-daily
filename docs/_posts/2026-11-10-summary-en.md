---
layout: default
title: "Horizon Summary: 2026-11-10 (EN)"
date: 2026-11-10
lang: en
---

> From 7 items, 3 important content pieces were selected

---

**Technology News**
1. [DeepMind Introduces AlphaProof Code for Formal Verification](#item-tech-news-1) ⭐️ 8.0/10
2. [Blender 5.3 Released With Gaussian Splat Support](#item-tech-news-2) ⭐️ 7.0/10
3. [SWE-Pair benchmark pairs two real Python bug fixes per coding-agent task](#item-tech-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [DeepMind Introduces AlphaProof Code for Formal Verification](https://deepmind.google/blog/introducing-alphaproof-code/) ⭐️ 8.0/10

DeepMind has introduced AlphaProof Code, an AI agent for formal code verification, according to the announcement. The launch prompted Hacker News discussion about what the agent&\#x27;s proofs actually establish. Commenters questioned a claimed verification of a non-trivial human-written library that found zero bugs, asking whether the theorems were wrong or covered only narrow properties. Discussion also compared the agent with conventional coding agents that iterate over a codebase while writing Lean or Rocq proofs, and asked whether it challenges specifications or only implementations. The supplied evidence lacks further technical detail on the evaluation, so the strength and scope of the verification claims remain unclear.

hackernews · ilreb · Nov 10, 12:11 · [Discussion](https://news.ycombinator.com/item?id=50439193)

**「Background」** Formal verification means expressing a program&\#x27;s intended properties as a specification and proving, with machine-checked logic, that the implementation satisfies them. Signal&\#x27;s libsignal is the reference implementation of the Signal protocol; DeepMind describes AlphaProof Code as a multi-agent AI framework for formal software specification and verification and says it used the system to prove key security properties of libsignal at the machine-code level. DeepMind also reports that when it reintroduced two previously fixed bugs into an isolated version of Signal&\#x27;s code, AlphaProof Code produced machine-checked proofs that the buggy versions were insecure.

**「Impact」** Developers assessing AlphaProof Code should focus on specification quality and theorem scope, because a zero-bug finding is only as strong as the properties that were actually proved.

**「Community Discussion」** Several commenters were skeptical of the zero-bug framing, with concerns that AI-generated proofs or tests can pass while missing the intended behavior; some nevertheless welcomed formal verification as a useful AI application. Others asked how the agent differs from a standard coding agent writing Lean or Rocq proofs, and whether it can challenge the specification rather than just the implementation.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/blog/introducing-alphaproof-code/">Formal Verification of Signal’s Protocol with... — Google DeepMind</a></li>
<li><a href="https://google-deepmind.github.io/code-verification/">AlphaProof Code : Verifying Signal’s Security at the Machine- Code ...</a></li>
<li><a href="https://www.wired.com/story/a-new-ai-tool-from-google-deepmind-formally-verified-the-signal-protocol/">A New AI Tool From Google DeepMind Proved the Signal... | WIRED</a></li>

</ul>
</details>

**Tags**: `#formal verification`, `#AI for code`, `#DeepMind`, `#Lean`, `#program verification`

---

<a id="item-tech-news-2"></a>
### [Blender 5.3 Released With Gaussian Splat Support](https://www.blender.org/download/releases/5-3/) ⭐️ 7.0/10

Blender 5.3 has been released with Gaussian Splat support, according to the item. The release matters because Blender is a widely used open-source 3D creation suite, and Gaussian Splatting is relevant to graphics and AI-adjacent workflows. The item also identifies geometry nodes bundle features as significant for complex pipelines. The supplied material does not include detailed compatibility constraints, release-note specifics, or official performance data.

hackernews · amlib · Nov 10, 16:15 · [Discussion](https://news.ycombinator.com/item?id=50442426)

**「Background」** 3D Gaussian Splatting is a scene-representation and rendering technique that stores a captured scene as many oriented, semi-transparent 3D Gaussians rather than meshes or triangles; it became popular for turning photographs or video into realistic, real-time viewable 3D scenes. Blender&\#x27;s Geometry Nodes system, meanwhile, is its node-based procedural modeling toolset, and bundles extend it by letting node groups pass structured collections of data through a graph. In Blender 5.3, splats can be imported from PLY and SPZ files as point clouds, manipulated with Geometry Nodes, previewed in Workbench, and rendered natively in EEVEE or Cycles, though export of splats is not yet supported.

**「Impact」** Blender 5.3 gives artists native import, editing, and rendering of Gaussian splat captures, allowing captured real-world environments to enter existing 3D and VFX workflows without leaving the suite, though splats complement rather than replace polygon-based modeling.

**「Community Discussion」** Commenters who tested the beta describe the Gaussian Splat integration as mature, fast, and consistent with the rest of Blender, including a 4-million-splat scene on an Apple M4. Others highlight geometry nodes bundles, lists, and closures as a major workflow improvement once understood, while one commenter contrasted Gaussian splatting with triangle splatting as an alternative better aligned with GPU rendering.

<details><summary>References</summary>
<ul>
<li><a href="https://www.blender.org/download/releases/5-3/">5 . 3 — Blender</a></li>
<li><a href="https://80.lv/articles/blender-5-3-is-getting-native-3d-gaussian-splat-support">Blender 5 . 3 Is Getting Native 3D Gaussian Splat Support</a></li>
<li><a href="https://xanathon.com/2026/10/gaussian-splatting-what-is-it-and-how-to-use-in-blender/">Gaussian Splatting: Tech, Limits, Blender Workflow - xanathon</a></li>
<li><a href="https://zgian.com/blender-5-3-gaussian-splatting-vfx/">Blender 5.3 Gaussian Splatting: New VFX Tools - zgian.com</a></li>

</ul>
</details>

**Tags**: `#Blender`, `#Gaussian Splatting`, `#3D graphics`, `#open source`, `#geometry nodes`

---

<a id="item-tech-news-3"></a>
### [SWE-Pair benchmark pairs two real Python bug fixes per coding-agent task](https://www.reddit.com/r/MachineLearning/comments/1xsuqem/swepair_a_codingagent_benchmark_where_every_task/) ⭐️ 7.0/10

SWE-Pair is a new 161-task coding-agent benchmark drawn from 69 Python projects in which each task requires fixing two real bugs at once. Its public announcement reports that DeepSeek V4.1 Flash at medium effort solved 90% of tasks for about 6 cents per solved task, while GPT-6 Luna at max effort solved 78% for about 23 cents. Raising reasoning effort did not help in the reported runs: DeepSeek at max effort scored 88%, slightly below medium, and cost 1.7x more. The benchmark dataset and every agent run are public, and agents can be run with the Harbor command \`harbor run -d evaligo/swe-pair -a &lt;agent&gt; -m &lt;provider/model&gt;\`.

reddit · r/MachineLearning · /u/heyitsdannyle · Nov 10, 18:33

**「Why a dual-bug benchmark matters」** Agentic coding benchmarks in the SWE-bench style hand a model a real repository and a real issue, then score the agent on whether the resulting patch passes the project&\#x27;s tests; curated variants such as Datacurve&\#x27;s DeepSWE package such tasks for automated evaluation. Most of these benchmarks present a single issue per task, so they measure an isolated fix rather than the mixed, multi-part workloads developers actually face. &quot;Reasoning effort&quot; is a per-request setting \(typically low through max\) that controls how many internal thinking tokens a model is allowed to spend, letting users trade inference cost and latency against accuracy.

**「Impact」** For coding-agent developers and benchmark users, the reported results suggest that higher reasoning effort can reduce cost efficiency without improving task success, at least on this dual-bug Python benchmark.

<details><summary>References</summary>
<ul>
<li><a href="https://maxxbench.unlap.ai/research/coding-sandboxes/">DeepSeek V 4 . 1 Flash Uses a Network Bypass in... | MaxxBench</a></li>

</ul>
</details>

**Tags**: `#coding agents`, `#benchmarks`, `#LLM evaluation`, `#software engineering`, `#cost efficiency`

---