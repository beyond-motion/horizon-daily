---
layout: default
title: "Horizon Summary: 2026-09-23 (ZH)"
date: 2026-09-23
lang: zh
---

> 从 5 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [Anthropic 与 OpenAI 同日发布新模型并掀起价格战](#item-tech-news-1) ⭐️ 8.0/10
2. [Claude Code 遥测关闭时漏读 AGENTS.md，v2.1.281 已修复](#item-tech-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Anthropic 与 OpenAI 同日发布新模型并掀起价格战](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) ⭐️ 8.0/10

在这篇 9 月 22 日的文章中，Simon Willison 记录了一轮密集的前沿模型发布：前一天是 xAI 的 Grok 4.7 与小米的 MiMo v2.6 Flash/Pro，随后 Anthropic 发布 Claude Opus 5.5，约一小时后 OpenAI 发布 GPT-6 Sol 与 GPT-6 Luna。价格方面，GPT-6 Luna 为每百万 token 输入 0.10 美元、输出 0.50 美元，仅为 GPT-5.6 Luna（0.20/1.20 美元）的一半；GPT-6 Sol 定价 2/10 美元，也相当于 GPT-5.6 Sol（4/20 美元）的一半，而由于 GPT-5.6 计划在 11 月涨价 25%，这一对比是相对促销价而言的。Claude Opus 5.5 的价格从 Opus 4.5 至 5 系列一直沿用的 5/25 美元降至 4/20 美元（降幅 20%），缓存读取价格下降 60%——作者指出这对 90% 以上输入 token 走缓存价格的长程 agentic 对话意义重大；Anthropic 还表示 Sonnet 5.5 与 Haiku 5.5 即将推出。不过在他的“骑自行车的鹈鹕”SVG 测试中，Opus 5.5 在 max 思考档位下两次都因触及 128,000 输出 token 上限而未返回结果，每次耗时近 20 分钟、花费 2.56 美元，他因此怀疑 max 档位实质上不可用。作者强调这些只是“目前为止”的初步印象，且所提供正文在结尾处被截断，完整评测尚无法评估。

rss · Simon Willison · 9月22日 23:46

**「背景」** 前沿模型（frontier model）指各厂商能力最强、定价也最高的旗舰层级，其 API 一般按每百万 token 分别计算输入与输出费用，并对缓存输入给出大幅折扣——对长上下文、多轮调用的智能体（agentic）工作负载而言，缓存读取价格往往是成本的主要变量。Anthropic 的 Opus 系列自 4.5 到 5 长期维持每百万 token 输入 5 美元、输出 25 美元，OpenAI 的 GPT-5.6 家族则按 Luna、Sol、Terra 等档位分层定价，其中 GPT-5.6 原本还安排了 11 月上调 25% 的计划。此次 Claude Opus 5.5 是 Anthropic 呼吁为前沿发展设定节奏后发布的第一个模型，发布前经 Frontier Design、METR 等外部机构评测，具备 100 万 token 上下文窗口和 12.8 万 token 的最大输出（tool-1-1、tool-1-3）；OpenAI 方面则表示 GPT-6 的降价部分来自推理与缓存（caching）方面的改进（tool-2-1）。

**「影响」** 对基于这些 API 构建应用的开发者来说，GPT-6 Luna 与 Claude Opus 5.5 的降价直接压低了推理与长上下文 agentic 会话的成本，但 Opus 5.5 的 max 档位可能因触及输出上限而无法返回结果，需谨慎用于实际工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5 . 5 \ Anthropic</a></li>
<li><a href="https://openrouter.ai/anthropic/claude-opus-5.5">Claude Opus 5 . 5 - API Pricing &amp; Providers | OpenRouter</a></li>
<li><a href="https://venturebeat.com/technology/openai-releases-gpt-6-sol-and-luna-models-slashing-api-costs-50-or-more">OpenAI releases GPT-6 Sol and Luna models, slashing API costs 50% or more | VentureBeat</a></li>

</ul>
</details>

**标签**: `#LLM releases`, `#Anthropic Claude`, `#OpenAI GPT`, `#AI model pricing`, `#frontier models`

---

<a id="item-tech-news-2"></a>
### [Claude Code 遥测关闭时漏读 AGENTS.md，v2.1.281 已修复](https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/) ⭐️ 7.0/10

Claude Code 曾被曝出一个 bug：在遥测关闭时不会读取 AGENTS.md。一位官方评论者解释，这是功能开关（feature flag）分阶段发布造成的：团队需要能在功能出问题时远程关闭它，而遥测关闭时这类控制信号无法送达。该问题已作为 v2.1.281 的一部分修复，该版本于当天发布；评论者称这是其人为失误并致歉。另有用户提醒，即便没有该 bug，若存在 CLAUDE.md，Claude Code 默认也可能不读 AGENTS.md，需要把项目指令设置改为非默认的 claude-md-and-agents-md 才会同时读取两者。

hackernews · pszypowicz · 9月23日 12:15 · [社区讨论](https://news.ycombinator.com/item?id=49814947)

**「背景」** AGENTS.md 是面向 AI 编码代理的项目指令约定文件，而 Claude Code 默认还使用 CLAUDE.md，并且只有在特定设置下才会同时读取两者。遥测通常用于收集使用和错误数据，功能开关则用于分阶段发布新功能或在出问题时远程关闭。此次问题在于，该功能的开关依赖遥测链路，遥测关闭时无法收到远端配置，于是 AGENTS.md 读取被跳过。

**「影响」** 对关闭遥测的 Claude Code 用户而言，该 bug 会使其 AGENTS.md 项目指令被静默忽略；升级到 v2.1.281 可修复，但存在 CLAUDE.md 时仍需按需调整项目指令设置。

**「社区讨论」** 评论区对功能开关的必要性存在分歧：有人认为部署与触发分离是分布式系统的常规做法，也有人批评叠加 AI 生成补丁会埋下隐蔽而严重的 bug，并质疑是否所有功能都受遥测或开关约束。还有用户分享经验称，只要存在 CLAUDE.md（包括 ~/CLAUDE.md），默认就不会读取 AGENTS.md，需手动切换设置。

**标签**: `#Claude Code`, `#AI coding agents`, `#AGENTS.md`, `#telemetry`, `#feature flags`

---