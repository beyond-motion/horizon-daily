---
layout: default
title: "Horizon Summary: 2026-08-27 (ZH)"
date: 2026-08-27
lang: zh
---

> 从 3 条内容中筛选出 1 条重要资讯。

---

**科技新闻**
1. [Qwen3.8-Flash-Next：开源多模态 MoE 模型预览 Qwen4 架构](#item-tech-news-1) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Qwen3.8-Flash-Next：开源多模态 MoE 模型预览 Qwen4 架构](https://simonwillison.net/2026/Aug/26/qwen38-flash-next/) ⭐️ 8.0/10

Qwen 发布 Qwen3.8-Flash-Next，一个开放权重多模态 MoE 模型，并作为 Qwen4 架构的早期预览。模型总参数为 125B，但每次推理仅激活 6B 参数，因此带来显著性能提升。Simon Willison 在 DGX Spark 上使用 Unsloth 量化版本进行测试，包括 72.5GB 的 UD-IQ1\_S 和 78.9GB 的 UD-Q2\_K\_XL；他目前最喜欢的输出来自 UD-Q2\_K\_XL 的 xhigh 推理强度设置，生成了鹈鹕骑自行车的扁平矢量插画。该模型延续了 Qwen 的开放权重路线，适合在本地硬件上实验多模态 MoE 能力。

rss · Simon Willison · 8月26日 23:52

**「背景」** Qwen3.8-Flash-Next 是 Qwen 团队开源权重发布的多模态混合专家（MoE）模型，其定位与 Qwen3-Next 当年预览 Qwen3.5 架构类似，是 Qwen4 架构的早期预览。MoE 设计意味着模型总参数量为 1250 亿，但每次推理只激活约 60 亿参数，从而在保持较大知识容量的同时显著降低计算成本。此前 Qwen3-Next 引入的混合 Gated DeltaNet 与 Gated Attention 设计延续到了 Qwen3.5 至 Qwen3.8 系列，而该新模型则展示了下一代架构方向。

**「影响」** 对 AI/ML 开发者而言，该模型提供了可在 DGX Spark 等本地设备上通过量化运行的多模态 MoE 选项，并提前展示了 Qwen4 的架构方向；不过 Willison 仍在探索中，实际效果需更多测试验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/QwenLM/Qwen3.8-Flash-Next/">Qwen3.8-Flash-Next - GitHub</a></li>
<li><a href="https://qwen.ai/blog?id=qwen3.8-flash-next">Qwen3.8-Flash-Next: A New Architecture, Towards Ultimate Cost ...</a></li>
<li><a href="https://docs.sglang.io/cookbook/autoregressive/Qwen/Qwen3.8-Flash-Next">Qwen3.8-Flash-Next - SGLang Documentation</a></li>

</ul>
</details>

**标签**: `#Qwen`, `#open-weights`, `#MoE`, `#multimodal`, `#AI models`

---