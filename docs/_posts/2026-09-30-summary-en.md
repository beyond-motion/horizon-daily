---
layout: default
title: "Horizon Summary: 2026-09-30 (EN)"
date: 2026-09-30
lang: en
---

> From 2 items, 2 important content pieces were selected

---

**Technology News**
1. [You Said No MCP: Team Reverses MCP Adoption Stance](#item-tech-news-1) ⭐️ 7.0/10
2. [Anthropic: Newer Models Cross Binary Exploitation Threshold](#item-tech-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [You Said No MCP: Team Reverses MCP Adoption Stance](https://earendil.com/posts/you-said-no-mcp/) ⭐️ 7.0/10

The blog post “You Said No MCP” documents a team’s public reversal on adopting MCP, according to the supplied analysis summary. The post is described as an account of changing a strongly held position, and the accompanying Hacker News discussion drew 509 points and 288 comments. Because no article text was available, the specific technical reasons for the reversal, the MCP implementation details, and any version or compatibility constraints cannot be verified. Commenters pointed to real-world MCP deployments, including local-model workflows for oil and gas data, natural-language configuration of macOS apps, and debate over whether MCP or CLI tools are the better approach.

hackernews · yarapavan · Sep 30, 09:55 · [Discussion](https://news.ycombinator.com/item?id=49906637)

**「Background」** The Model Context Protocol \(MCP\) is an open-source standard for connecting AI applications such as Claude or ChatGPT to external data sources, tools, and workflows. Pi.dev had previously stated prominently that Pi does not support MCP, and the wider discourse swung from claims that MCP was mandatory to declarations that it was dead. This post documents the team&\#x27;s public reversal on that stance.

**「Impact」** For developers and teams evaluating MCP, the thread offers concrete examples of production and local-model use beyond coding assistants, though the original post’s technical claims remain unverified without the article text.

**「Community Discussion」** Commenters largely welcomed the public reversal and shared practical MCP deployments, including a six-month oil-and-gas deployment with C-suite use, local models, Postgres with Tiger, and Neo4j, plus macOS apps such as rcmd, Clop, and Lunar configured through natural language with local Qwen and Pi. Others argued that the earlier anti-MCP wave dismissed security, observability/telemetry, deployment, and operations concerns, while one commenter highlighted Armin Ronacher’s linked post about strong opinions relying on outdated arguments.

<details><summary>References</summary>
<ul>
<li><a href="https://earendil.com/posts/you-said-no-mcp/">“ You Said No MCP !” | Earendil</a></li>
<li><a href="https://news.ycombinator.com/item?id=49906637">Pi.dev: You Said No MCP | Hacker News</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol ( MCP )? - Model Context Protocol</a></li>

</ul>
</details>

**Tags**: `#MCP`, `#AI tooling`, `#local LLMs`, `#software engineering`, `#community debate`

---

<a id="item-tech-news-2"></a>
### [Anthropic: Newer Models Cross Binary Exploitation Threshold](https://simonwillison.net/2026/Sep/29/anthropic-frontier-red-team/) ⭐️ 7.0/10

Anthropic&\#x27;s Frontier Red Team reports that it evaluated several models on 100 randomly selected tasks from its internal Binary Exploitation benchmark. GLM-5.3 developed full control flow hijacks in 4% of trials, while Claude Mythos Preview did so in 6%. Earlier models, including Claude Opus 4.6 and GLM-5.2, did not succeed on any of the tasks. The team concludes that although GLM-5.3 trails Claude Mythos Preview, &quot;a meaningful threshold has clearly been crossed&quot; in AI cyber capability. Simon Willison quoted the finding from Anthropic&\#x27;s report &quot;GLM-5.3 and the spread of advanced cyber capabilities.&quot;

rss · Simon Willison · Sep 29, 22:20

**「Background」** Binary exploitation is the practice of turning memory-safety bugs in compiled software into working attacks, and a &quot;full control flow hijack&quot; — redirecting a program&\#x27;s execution to code of the attacker&\#x27;s choosing — is a standard marker that an exploit has succeeded end to end. Anthropic&\#x27;s Frontier Red Team is the group that stress-tests its own and rival models for these offensive-security capabilities, and it has previously published detailed technical write-ups of how it evaluated Claude Mythos Preview on computer-security tasks \(tool-1-2\). The benchmark referenced here is Anthropic&\#x27;s internal Binary Exploitation evaluation, so the quoted pass rates come from the vendor&\#x27;s own testing rather than an independently reproducible public suite.

**「Impact」** Security teams and developers can no longer treat full control-flow hijack capability as confined to a single frontier model family, since Anthropic&\#x27;s benchmark shows two independently developed models — GLM-5.3 at 4% and Claude Mythos Preview at 6% — reaching a tier that Claude Opus 4.6 and GLM-5.2 never reached, a tier that graded exploitation benchmarks treat as a distinct capability step above crashes and arbitrary read/write. The absolute success rates remain low, so the near-term consequence is a raised capability baseline across model families rather than turnkey exploit generation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/research/mythos-preview">Claude Mythos Preview&#x27;s cybersecurity capabilities - Anthropic</a></li>
<li><a href="https://arxiv.org/pdf/2605.14153">ExploitBench: A Capability Ladder Benchmark for LLM ...</a></li>

</ul>
</details>

**Tags**: `#ai-security`, `#llm-capabilities`, `#binary-exploitation`, `#anthropic`, `#ai-benchmarks`

---