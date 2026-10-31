---
layout: default
title: "Horizon Summary: 2026-10-31 (ZH)"
date: 2026-10-31
lang: zh
---

> 从 7 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [OpenAI 修复 ChatGPT 账号接管漏洞，5,000 美元赏金引争议](#item-tech-news-1) ⭐️ 7.0/10
2. [实验：在 Qwen3.5-4B 权重中嵌入 NES 模拟器](#item-tech-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenAI 修复 ChatGPT 账号接管漏洞，5,000 美元赏金引争议](https://www.parameter.ai/labs/we-found-a-gap-at-openai) ⭐️ 7.0/10

Parameter.ai Labs 发布文章，披露其发现的 ChatGPT 账号接管漏洞。OpenAI 确认该问题并完成修复，同时支付总计 5,000 美元的漏洞赏金。该事件受到关注，是因为它涉及 AI 平台的账号安全，也凸显漏洞披露与赏金激励之间的张力。现有公开信息未详细说明完整的利用链和影响范围，相关技术细节仍需以原始披露为准。

hackernews · armcat · 10月31日 10:30 · [社区讨论](https://news.ycombinator.com/item?id=50314699)

**「背景」** ChatGPT 的预览类功能（Preview）此前被放在与 chatgpt.com 分开的独立域名上，借此实现隔离，以降低渲染用户内容带来的风险。这种跨域隔离是防范跨站脚本（XSS）和账户接管（account takeover）的常见手段：一旦攻击者能在主站域下执行任意 JavaScript，就能以受害者身份操作其会话。漏洞赏金（bug bounty）项目是厂商用现金奖励鼓励外部研究者私下报告此类问题、而非公开或转卖漏洞的机制，赏金金额通常与漏洞的严重性和影响范围挂钩。

**「影响」** 对 ChatGPT 用户而言，直接风险已随修复解除，但公开细节有限，仍难以判断此次漏洞的具体影响范围。

**「社区讨论」** 评论普遍批评 5,000 美元赏金过低，认为这可能削弱研究者报告漏洞的意愿，甚至促使他们转向黑市出售利用。也有评论借机讨论大型系统复杂度与缺陷面的关系，并提醒用户不要点击可疑链接。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.parameter.ai/labs/we-found-a-gap-at-openai">Do the Math: How We Took Over ChatGPT Accounts - Parameter</a></li>
<li><a href="https://news.ycombinator.com/item?id=50314699">We Took over ChatGPT Accounts | Hacker News</a></li>

</ul>
</details>

**标签**: `#AI security`, `#ChatGPT`, `#account takeover`, `#vulnerability disclosure`, `#bug bounty`

---

<a id="item-tech-news-2"></a>
### [实验：在 Qwen3.5-4B 权重中嵌入 NES 模拟器](https://simonwillison.net/2026/Oct/30/nesformer/) ⭐️ 7.0/10

Drew Breunig 发布了实验项目 nesformer，把可运行的 NES 6502 CPU 模拟器嵌入 Qwen3.5-4B 的权重中，灵感来自 Divyansh Agrawal 的 qwenputer。该模型可通过 CLI 指向 NES ROM，让《Super Mario Bros》等游戏在 Qwen 内以很慢的速度运行。Breunig 在 Hacker News 评论中披露，他使用 Opus 5.5 的提示词研究 qwenputer 及相关源码，并要求实际构建权重与 CLI 方案；据称 Opus 还找到并使用了 Christopher Pow 约 15 年前发布的 NES CPU 一致性测试集。该项目更像是展示模型容量与系统黑客手法的概念验证，速度远未达到实用水平。

rss · Simon Willison · 10月30日 21:59

**「背景」** Nesformer 的直接灵感是 Divyansh Agrawal 的 qwenputer：后者把一颗 32 位 RISC-V CPU 及内存“编译”进 Qwen 3.5-4B 的权重中，并以模型的 Gated DeltaNet 层充当 RAM。Nesformer 沿用这一思路，但目标换成 NES 的 6502 CPU（2A03 芯片核心）、2 KB 工作 RAM 和卡带程序 ROM，把它们放进标准 Qwen3\_5ForCausalLM 检查点内。与插件或外部工具不同，这类实验追求的是让模型权重本身承载可执行的处理器状态与逻辑。

**「影响」** 对 AI 与系统实验者而言，这提供了一种可借鉴的做法：用模型权重承载确定性的 CPU 模拟，并通过 CLI 加载 ROM；但当前极慢的运行速度使其只适合演示和进一步研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://divagr.com/blog/qwenputer">Qwenputer : a fully functioning, deterministic RISC-V CPU inside...</a></li>
<li><a href="https://github.com/dbreunig/nesformer">GitHub - dbreunig/nesformer: An NES CPU compiled into the ...</a></li>

</ul>
</details>

**标签**: `#LLM weight embedding`, `#NES emulation`, `#Qwen`, `#experimental AI`, `#systems hacking`

---