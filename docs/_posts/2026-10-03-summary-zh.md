---
layout: default
title: "Horizon Summary: 2026-10-03 (ZH)"
date: 2026-10-03
lang: zh
---

> 从 2 条内容中筛选出 1 条重要资讯。

---

**科技新闻**
1. [Aleph Alpha 发布 Kolibri 开放权重模型](#item-tech-news-1) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Aleph Alpha 发布 Kolibri 开放权重模型](https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/) ⭐️ 7.0/10

Aleph Alpha 发布了开放权重模型 Kolibri，重点面向编码与智能体（agentic）任务，并随附一份被社区形容为「手把手教你造现代智能体 LLM」的详细技术报告。报告披露了数据集的构建方式与训练流程，还说明了为抑制幻觉而引入的 abstention 数据与 Merlin-Arthur 协议，使模型在答案不在上下文中时被训练为回答「我不知道」。Aleph Alpha 训练团队成员表示，这是该团队成立不到一年来的首次发布，团队强调迭代速度，并称后续还会有更多成果。社区方面，已有开发者将 Kolibri-1 托管上线供人免费试用；同时也有评论者指出，在 Kolibri 自身的测试框架与德语基准上，Qwen3.8 27B 以 79.9 比 70.8 超过 Kolibri，并质疑 Cohere 收购完成后该模型是否还能维持「主权」定位。

hackernews · bastitx · 10月3日 09:36 · [社区讨论](https://news.ycombinator.com/item?id=49942706)

**「背景」** Aleph Alpha 是一家德国 AI 公司，其发布的 Kolibri 定位为面向英语和德语的「主权」开放权重模型，以 Apache 2.0 许可发布。该模型采用混合专家（MoE）架构，总参数 78B、激活参数 3B，上下文窗口最高可达 1M token，主打主权与关键任务场景。所谓「主权 AI」通常指模型权重与运行可留在本地或本地区、不完全依赖外部供应商，Kolibri 正是以欧洲本土替代方案为卖点。

**「影响」** 对需要自主可控部署的开发者与机构而言，Kolibri 提供了一个可本地运行、技术报告与数据集披露完整的开放权重选项，在编程与代理任务上具备可用性，并宣称能以更小的规模达到接近更大模型的效率。不过官方评估也显示，密集模型 Qwen3.8 27B 在部分测试中得分高于 Kolibri，因此实际选型仍需按自身任务进行验证。

**「社区讨论」** 讨论普遍赞赏 Kolibri 技术报告的透明度与数据集披露程度，认为这种开放程度少见，并有开发者主动提供免费托管试用作为支持。质疑则集中在两点：其自家德语基准上 Qwen3.8 27B 的得分高于 Kolibri，以及 Cohere 收购完成后「主权开放权重」这一说法是否仍然成立。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/">Kolibri Has Landed: A Sovereign Open-Weight Model - Aleph Alpha</a></li>
<li><a href="https://theopenweights.com/news/kolibri-1-v2uw">Aleph Alpha releases Kolibri, a sovereign reasoning model · The Open ...</a></li>
<li><a href="https://aleph-alpha.com/en/kolibri/">Kolibri | Aleph Alpha</a></li>
<li><a href="https://localmodelwatch.tsuchitsuchi.com/en/2026/10/04/aleph-alpha-kolibri-open-weight-moe/">Aleph Alpha Releases Kolibri: A New Open-Weight MoE Model</a></li>

</ul>
</details>

**标签**: `#open-weight models`, `#LLM`, `#Aleph Alpha`, `#model transparency`, `#hallucination mitigation`

---