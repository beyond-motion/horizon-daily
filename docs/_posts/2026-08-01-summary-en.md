---
layout: default
title: "Horizon Summary: 2026-08-01 (EN)"
date: 2026-08-01
lang: en
---

> From 10 items, 5 important content pieces were selected

---

**Technology News**
1. [DeepSeek V4-Flash-0731: 304B open-weights model with strong agentic skills at low cost](#item-tech-news-1) ⭐️ 8.0/10
2. [Stateless MCP 2.0 Reignites Interest, Sparks New Tools](#item-tech-news-2) ⭐️ 8.0/10
3. [Open Weight Revolution Podcast Recap with Simon Willison](#item-tech-news-3) ⭐️ 8.0/10
4. [Elevator Scheduling Algorithms: Destination Dispatch Underwhelms](#item-tech-news-4) ⭐️ 7.0/10
5. [smevals: Small Eval Suite for Models, Prompts, and Harnesses](#item-tech-news-5) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [DeepSeek V4-Flash-0731: 304B open-weights model with strong agentic skills at low cost](https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything) ⭐️ 8.0/10

DeepSeek has released DeepSeek-V4-Flash-0731, a 304-billion-parameter open-weights model available on Hugging Face at 167GB, described as having substantially enhanced agentic capabilities. According to Artificial Analysis, it ranks ahead of MiniMax M3, a 428B model, and its pricing of $0.14 per million input tokens and $0.27 per million output tokens may make it the best value-per-intelligence model currently available. Simon Willison tested the model through OpenRouter and found that while the default reasoning level produced a disappointing pelican image, using &\#x27;reasoning\_effort high&\#x27; yielded a much better result. The model appears on Artificial Analysis&\#x27; Intelligence Index versus Cost per Task chart as an outlier in the most attractive quadrant, outperforming many more expensive models but still lagging behind higher-priced models like Grok 4.5 and Claude Opus 5.

rss · Simon Willison · Jul 31, 23:59

**「Background」** DeepSeek V4 Flash first appeared on April 24, 2026 as the smaller half of the DeepSeek V4 family: a 284-billion-parameter mixture-of-experts \(MoE\) model with 13 billion active parameters per token, a 1M-token context window, and MIT-licensed weights, alongside the 1.6-trillion-parameter V4 Pro. The July 31, 2026 build, DeepSeek-V4-Flash-0731, is the official release of this small agent model, announced in DeepSeek&\#x27;s API changelog as a re-post-trained checkpoint that moves the V4-Flash API out of Preview into public beta, with dramatically higher agentic benchmark scores by DeepSeek&\#x27;s own measurements. The model is also available on Hugging Face as a 304B-parameter checkpoint \(167GB download\).

**「Impact」** AI practitioners seeking strong agentic performance at minimal cost can benefit from DeepSeek-V4-Flash-0731, but should set the reasoning effort to high when quality is critical, since the default level may yield noticeably poorer results.

<details><summary>References</summary>
<ul>
<li><a href="https://www.digitalapplied.com/blog/deepseek-v4-flash-0731-official-release-agent-benchmarks">DeepSeek V4 Flash 0731: Official Release, Agent Benchmarks</a></li>
<li><a href="https://www.modemguides.com/blogs/ai-news/deepseek-v4-flash-official-release">DeepSeek V4-Flash 0731: What Changed and What You Can Run</a></li>
<li><a href="https://www.developersdigest.tech/blog/deepseek-v4-flash-0731-opencode-guide">DeepSeek V4 Flash 0731: The Official Release, Benchmarks, and How to Run It in OpenCode - Developers Digest</a></li>

</ul>
</details>

**Tags**: `#deepseek`, `#large-language-models`, `#ai`, `#machine-learning`, `#open-source`

---

<a id="item-tech-news-2"></a>
### [Stateless MCP 2.0 Reignites Interest, Sparks New Tools](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything) ⭐️ 8.0/10

Simon Willison reports that Tuesday marked “Stateless MCP day,” the rollout of MCP 2.0, formally the 2026-07-28 Model Context Protocol specification, which he calls the most significant change since the protocol first launched. The new stateless design lets clients call tools with a single HTTP request using MCP-Protocol-Version and Mcp-Method headers, eliminating the legacy two-step initialize/session-id dance and the need for server-side session state. He says this reignited his interest in MCP, which had been eclipsed by Anthropic&\#x27;s Skills concept after terminal-and-curl agent harnesses seemed more flexible, because MCP tools are easier to audit and control and simple enough for smaller laptop models to drive. To explore the new spec, he built mcp-explorer, a uvx-runnable Python CLI for listing, inspecting, and calling MCP tools, and datasette-mcp, a Datasette plugin that exposes a /-/mcp endpoint with list\_databases\(\), get\_database\_schema\(\), and read-only execute\_sql\(\) tools. He is running the plugin on datasette.simonwillison.net/-/mcp and documented how to connect it to ChatGPT and Claude.

rss · Simon Willison · Jul 31, 23:13

**「Background」** MCP is a standard introduced by Anthropic in November 2024 for exposing tools to LLM-powered agent frameworks. After a surge of interest through much of 2025, it was partly overshadowed by Anthropic&\#x27;s Skills pattern, since an agent with a terminal and curl can often accomplish similar tasks more flexibly. The new 2026-07-28 specification simplifies the wire protocol by making individual tool calls stateless, replacing the older flow that required an initialize request, a session ID, and then a separate tool-call request.

**「Impact」** For developers building or running MCP clients and servers, the stateless redesign removes a major implementation burden—server-side session tracking and session routing—and makes MCP more attractive for scalable web applications and smaller, local models. Simon Willison&\#x27;s mcp-explorer and datasette-mcp demonstrate that the simplified spec is approachable enough to produce working tools quickly, including SQL access to a Datasette instance from agents like ChatGPT and Claude.

**Tags**: `#MCP`, `#Model Context Protocol`, `#AI agents`, `#software engineering`, `#Simon Willison`

---

<a id="item-tech-news-3"></a>
### [Open Weight Revolution Podcast Recap with Simon Willison](https://simonwillison.net/2026/Jul/31/oxide-and-friends/#atom-everything) ⭐️ 8.0/10

Simon Willison joined Bryan Cantrill and Adam Leventhal on the Oxide and Friends podcast to discuss a turbulent week in AI, highlighted by Kimi K3 demonstrating that open-weight models can compete with proprietary frontier models. The conversation also covered accidental cybersecurity attacks and public letters supporting open weights and American AI leadership, signed by nearly every major AI figure except Anthropic. Willison noted the episode was already outdated by the time it aired, as DeepSeek V4 Flash 0731 and Anthropic&\#x27;s own embarrassing cyber incident occurred just days later. The discussion also touched on Golden Gate Claude, the Zizians, Alameda wild turkey attacks, Soviet Marburg virus research, and the lead-crime hypothesis, while revisiting January predictions. A new prediction was added that the Pope will say something about open models by the end of the year.

rss · Simon Willison · Jul 31, 21:33

**「Background」** Open-weight models are AI models whose trained weights are publicly released, letting developers run, fine-tune, and self-host them, in contrast to proprietary frontier models such as GPT-5.5. Kimi K3 is a large open-weight model \(2.8T parameters, listed at $15/M tokens\) that launched with open weights on July 27, 2026, following the Modified MIT precedent set by Kimi K2; DeepSeek V4 Flash is a similarly recent open-weight release. The discussion centers on how these open releases increasingly match proprietary frontier quality, alongside industry letters urging support for open-weight leadership.

<details><summary>References</summary>
<ul>
<li><a href="https://www.vals.ai/models/kimi_kimi-k3">Kimi K 3</a></li>
<li><a href="https://datamy.co/resources/blog/kimi-k3-chinese-open-weight-vs-us-frontier-enterprise-2026">Will Kimi K 3 Flip the Table on Anthropic and OpenAI? | DataMy</a></li>
<li><a href="https://bota.chat/kimi-k3/">Kimi K 3 Explained: 2.8T Params, $15/M Tokens, Open</a></li>

</ul>
</details>

**Tags**: `#open-weights`, `#AI`, `#podcast`, `#Simon Willison`, `#industry-policy`

---

<a id="item-tech-news-4"></a>
### [Elevator Scheduling Algorithms: Destination Dispatch Underwhelms](https://john.fun/elevators) ⭐️ 7.0/10

The article provides an engaging technical analysis of elevator scheduling algorithms, comparing strategies such as destination dispatch and highlighting unexpected findings about their real-world performance. It draws an analogy between elevators and disk-scheduling algorithms like SCAN, which is relevant to software engineering and algorithm design. The piece is supported by interactive simulations and a strong community discussion, though it does not represent a groundbreaking industry change.

hackernews · Jrh0203 · Jul 31, 15:17 · [Discussion](https://news.ycombinator.com/item?id=49124218)

**「Background」** Elevator scheduling algorithms decide how cars respond to floor calls, balancing factors like wait time, energy use, and passenger flow. A classic method is SCAN \(the elevator algorithm\), which moves cars in one direction until no more calls remain ahead—a concept also used in hard-disk scheduling. The john.fun article &\#x27;Elevators&\#x27; presents an interactive simulation exploring these strategies, including destination dispatch, which groups riders by their selected floors.

**「Community Discussion」** Commenters connected elevator algorithms to disk-scheduling \(SCAN\), questioned whether the article&\#x27;s negative view of destination dispatch was an artifact of using random destinations, and shared practical experiences such as a 60-floor tower with three saturated elevators. One commenter also pointed to an elevator-scheduling game for hands-on exploration.

<details><summary>References</summary>
<ul>
<li><a href="https://upstract.com/x/fcf19264873998d7">Elevators - upstract.com</a></li>

</ul>
</details>

**Tags**: `#algorithms`, `#elevator-scheduling`, `#simulation`, `#disk-scheduling`, `#software-engineering`

---

<a id="item-tech-news-5"></a>
### [smevals: Small Eval Suite for Models, Prompts, and Harnesses](https://simonwillison.net/2026/Jul/31/smevals/#atom-everything) ⭐️ 7.0/10

Simon Willison announced smevals, a small eval suite developed with Prime Radiant, designed to evaluate models, prompts, and harnesses. It defines an eval as a collection of tasks, run against configs that specify models and other parameters, with results graded by graders composed of checks and checkers. Users interact through uvx smevals commands: run, grade, serve, and build, with eval suites stored as directories of YAML files. A provided example demonstrates evaluating haiku-writing across models like gpt-5.5 and claude-opus-4.6, generating static HTML reports with leaderboard-style results. Willison describes this as his third iteration on eval tooling and says it feels right for answering questions about model capabilities.

rss · Simon Willison · Jul 31, 21:15

**「Background」** Evals are structured benchmarks used to assess how well large language models perform on specific tasks, and they often also test prompt variations or agent harnesses. Many eval frameworks require significant setup, but smevals aims to be minimal and approachable, using YAML files and command-line tooling to define, run, and grade evaluations.

**「Impact」** AI engineers and researchers can now create reproducible model eval suites with minimal setup, run them against multiple models from the command line, and publish static HTML reports for sharing results with teams or the broader community.

**Tags**: `#evals`, `#LLM`, `#tooling`, `#machine-learning`, `#open-source`

---