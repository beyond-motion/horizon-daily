---
layout: default
title: "Horizon Summary: 2026-09-23 (EN)"
date: 2026-09-23
lang: en
---

> From 5 items, 2 important content pieces were selected

---

**Technology News**
1. [Claude Opus 5.5 and GPT-6 Sol/Luna launch amid price cuts](#item-tech-news-1) ⭐️ 8.0/10
2. [Claude Code Bug Skipped AGENTS.md When Telemetry Was Off](#item-tech-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Claude Opus 5.5 and GPT-6 Sol/Luna launch amid price cuts](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) ⭐️ 8.0/10

On September 22, 2026, Anthropic released Claude Opus 5.5 and, about an hour later, OpenAI released GPT-6 Sol and GPT-6 Luna, following the prior day&\#x27;s Grok 4.7 and Xiaomi MiMo v2.6 Flash/Pro launches. Simon Willison&\#x27;s first impressions highlight that GPT-6 Luna is half the price of its GPT-5.6 equivalent at $0.10 per million input tokens and $0.50 per million output tokens, while GPT-6 Sol also saw a similar reduction compared with GPT-5.6 Sol. Claude Opus 5.5, which Anthropic staff say addresses communication-style complaints, is better at Blender, and offers Fable 5.1-level intelligence at lower per-token cost, cut prices 20% from the $5/$25 per million input/output pricing shared by Opus 4.5 through 5 to $4/$20, and its cache-read price fell 60%, which matters for long agentic conversations where most input tokens are cached. Willison notes that GPT-5.6 has a scheduled 25% price increase in November, meaning GPT-6 is half the price of the promotional GPT-5.6 pricing, and that Anthropic says Sonnet 5.5 and Haiku 5.5 are coming soon. In his pelican SVG test, Claude Opus 5.5 at the &quot;max&quot; thinking level failed to return a response twice because it hit the 128,000 maximum output token limit while still reasoning, costing $2.56 and nearly 20 minutes each time.

rss · Simon Willison · Sep 22, 23:46

**「Background」** Anthropic&\#x27;s Opus line had held the same $5 per million input and $25 per million output pricing across Opus 4.5, 4.6, 4.7, 4.8 and 5, so the 5.5 reduction to $4/$20 was a break from that pattern; Anthropic describes Opus 5.5 as its first release since calling for pacing the frontier, and it was tested before release by external evaluators including Frontier Design and METR. OpenAI&\#x27;s GPT-5.6 family, including the cheap Luna tier that Simon Willison used for building applications, preceded the GPT-6 Sol and Luna launch, which halved those API prices through what OpenAI describes as improvements to inference and caching. The two launches landed roughly 90 minutes apart, part of a broader cluster of releases that also included xAI&\#x27;s Grok 4.7 and Xiaomi&\#x27;s MiMo v2.6.

**「Impact」** Developers building applications on these models, especially cached-input-heavy agentic workloads, benefit from materially lower costs: GPT-6 Luna at $0.10/$0.50 per million input/output tokens is one of OpenAI&\#x27;s cheapest releases, beaten only by the weaker GPT-4.1 Nano and GPT-5 Nano, while Opus 5.5&\#x27;s 20% price cut and 60% cache-read reduction lower the cost of long Claude conversations. Willison cautions these are early impressions and that Opus 5.5&\#x27;s &quot;max&quot; thinking mode failed to complete a simple SVG task twice by exhausting its 128,000-token output limit.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5 . 5 \ Anthropic</a></li>
<li><a href="https://bool.dev/news/detail/anthropic-releases-claude-opus-55">Anthropic Releases Claude Opus 5 . 5 — bool.dev</a></li>
<li><a href="https://venturebeat.com/technology/openai-releases-gpt-6-sol-and-luna-models-slashing-api-costs-50-or-more">OpenAI releases GPT-6 Sol and Luna models, slashing API costs 50% or more | VentureBeat</a></li>
<li><a href="https://thenewstack.io/openai-gpt-6-sol-luna-release/">OpenAI releases GPT-6 Sol and Luna — and cuts token prices in half - The New Stack</a></li>
<li><a href="https://thenextweb.com/news/openai-gpt-6-sol-luna-api-price-cut">OpenAI cuts GPT-6 prices in half with Sol and Luna</a></li>

</ul>
</details>

**Tags**: `#LLM releases`, `#Anthropic Claude`, `#OpenAI GPT`, `#AI model pricing`, `#frontier models`

---

<a id="item-tech-news-2"></a>
### [Claude Code Bug Skipped AGENTS.md When Telemetry Was Off](https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/) ⭐️ 7.0/10

Claude Code contained a bug that caused it to skip reading AGENTS.md instructions whenever telemetry was disabled. In the community thread, Anthropic&\#x27;s mpoteat described the behavior as a rollout artifact: a feature flag was used so the change could be turned off remotely if it broke something, but with telemetry off those flag states were not received. The commenter said the issue was already fixed as part of v2.1.281, described as releasing the same day, and apologized for what was called a fully human error in the launch approach. No source article content was available, so details rest on the item description and the supplied discussion.

hackernews · pszypowicz · Sep 23, 12:15 · [Discussion](https://news.ycombinator.com/item?id=49814947)

**「Background」** AGENTS.md is a widely used convention file that supplies repository-level instructions to AI coding agents, and Claude Code is Anthropic&\#x27;s agentic coding tool that also supports its own CLAUDE.md convention. Feature flags are commonly used to decouple deploying a change from enabling it, allowing a vendor to disable new behavior remotely across many installations without shipping a new build. The reported failure mode occurred because that remote control depended on telemetry being enabled.

**「Impact」** For Claude Code users running with telemetry disabled, project guidance stored in AGENTS.md was silently ignored, so the fix requires updating to v2.1.281 or later. A separate, still-relevant constraint raised in the thread is that AGENTS.md is not read by default when a CLAUDE.md is available, including a user-level ~/CLAUDE.md, unless the Project instructions setting is switched to the non-default \`claude-md-and-agents-md\`.

**「Community Discussion」** Commenters disagreed about the root cause: one attributed such subtle but severe bugs to piling up layers of AI-generated patches, while another argued feature flags are a normal way to separate deployment from activation and enable progressive rollouts. Others pushed back that flag-checked code may never be cleaned up, and one commenter explained the flag approach as a straightforward distributed systems problem of deploying to many hosts and triggering behavior with a lightweight switch.

**Tags**: `#Claude Code`, `#AI coding agents`, `#AGENTS.md`, `#telemetry`, `#feature flags`

---