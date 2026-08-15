---
layout: default
title: "Horizon Summary: 2026-08-15 (ZH)"
date: 2026-08-15
lang: zh
---

> 从 3 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [Codex 自动研究循环实现 232 倍内核加速](#item-tech-news-1) ⭐️ 7.0/10
2. [不要分类，要幻觉：用向量匹配大规模标签](#item-tech-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Codex 自动研究循环实现 232 倍内核加速](https://sankalp.bearblog.dev/autoresearch/) ⭐️ 7.0/10

开发者 tosh 在 bearblog 上发文，描述使用 Codex 驱动自动研究循环来优化一个内核，最终取得了 232 倍的性能提升。这一案例展示了 AI 辅助性能优化在特定负载上的巨大潜力，但现有内容不足以验证完整技术细节，因此该结果不能直接推广到所有场景。社区评论进一步提醒，这类自动化优化容易针对特定输入过拟合，泛化性和鲁棒性仍是关键限制。

hackernews · tosh · 8月15日 11:00 · [社区讨论](https://news.ycombinator.com/item?id=49309549)

**「背景」** 这篇文章讲述作者使用 OpenAI Codex 以“自动研究”循环方式优化一个内核，最终实现 232 倍提速。文章解释了为什么这类问题适合自动研究，并详细记录了如何让 Codex 提出突破性想法、引入思路多样性以跳出局部最优；其中还涉及 QR 分解所需的 Householder 反射等数学背景。

**「影响」** 对于尝试用 AI 智能体进行性能优化的开发者，这个案例提供了量化的加速证据，但必须结合代表性输入和验证器进行测试，避免社区中观察到的“只对特定输入有效”的失败模式。

**「社区讨论」** 评论者 Almondsetat 尝试让智能体对半废弃的视频压缩编解码器运行 benchmark/profile/verify/research/improve 循环；augment\_me 指出竞赛中 10 个顶尖方案里有 8 个在非竞赛输入上完全失效，只有懂 GPU 编程的专家在合理范围内调整的方案才保持稳健。themeiguoren 建议先用单元测试和黄金值防止回归，并用火焰图人工引导优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sankalp.bearblog.dev/autoresearch/">Auto - research with codex : How I achieved a 232 x Faster Kernel ...</a></li>

</ul>
</details>

**标签**: `#AI-assisted development`, `#performance optimization`, `#kernel`, `#Codex`, `#software engineering`

---

<a id="item-tech-news-2"></a>
### [不要分类，要幻觉：用向量匹配大规模标签](https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/) ⭐️ 7.0/10

Simon Willison 在 2026 年 8 月 14 日的博文中介绍了 Doug Turnbull 提出的“不要分类，要幻觉”方法：面对自己博客上多达 1,856 个标签、无法一次性喂给 LLM 让模型选择匹配标签的情况，可以反过来让模型先不看现有词汇表，直接想象出可能合适的新标签，再用向量嵌入把这些“幻觉”标签映射到现有标签中最接近的实体上。Turnbull 给出的示例提示会先展示目标标签体系的层级结构，例如“Furniture / Living Room Furniture / Coffee Tables &amp; End Tables / Coffee Tables”，再针对查询“brown coffee table”生成从未见过的分类建议。这种做法的关键是利用嵌入向量衡量语义相似度，从而在超大标签词汇表上完成分类，而无需把整个标签列表放进提示词。Willison 认为这是一个巧妙且实用的技巧，对使用大型标签体系的 AI 实践者尤其有用。

rss · Simon Willison · 8月14日 21:54

**「背景」** 在传统的 LLM 分类任务中，如果候选标签数量巨大（例如 Simon Willison 博客有 1,856 个标签），就无法一次性把所有标签都塞进提示词并要求模型从中选择。Doug Turnbull 提出的方法是不让模型在固定词表中做分类，而是先让模型自由“幻觉”出可能适合的标签，再利用向量嵌入将这些虚构标签与现有词表中的真实标签进行相似度匹配，从而映射到系统允许的合法标签。这种思路借鉴了向量搜索常见的方法，避免了对超大词表的直接约束分类。

**「影响」** 对需要在超大标签体系下进行内容打标或产品分类的开发者、搜索与推荐系统工程师而言，该方法可用少量提示词和向量检索替代“把所有候选标签塞进 LLM”的高成本方案；实际效果仍取决于标签向量质量和相似度阈值设置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://softwaredoug.com/blog/2026/08/10/hypothetical-classifications">Don &#x27; t classify . Hallucinate ! | Doug Turnbull &#x27;s Blog</a></li>
<li><a href="https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/">Don &#x27; t classify . Hallucinate ! | Simon Willison’s Weblog</a></li>

</ul>
</details>

**标签**: `#LLM classification`, `#embeddings`, `#tagging`, `#prompt engineering`, `#vector search`

---