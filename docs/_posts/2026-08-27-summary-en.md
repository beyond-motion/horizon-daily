---
layout: default
title: "Horizon Summary: 2026-08-27 (EN)"
date: 2026-08-27
lang: en
---

> From 3 items, 1 important content pieces were selected

---

**Technology News**
1. [Qwen3.8-Flash-Next: Open-Weight Multimodal MoE Previews Qwen4](#item-tech-news-1) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Qwen3.8-Flash-Next: Open-Weight Multimodal MoE Previews Qwen4](https://simonwillison.net/2026/Aug/26/qwen38-flash-next/) ⭐️ 8.0/10

Qwen released Qwen3.8-Flash-Next, an open-weights multimodal mixture-of-experts model that also serves as an early preview of the architecture planned for Qwen4. The model has 125B total parameters but only 6B active per token, which provides a significant inference performance boost. Simon Willison tested it on an NVIDIA DGX Spark using Unsloth&\#x27;s quantized GGUF versions, including the 72.5GB UD-IQ1\_S and 78.9GB UD-Q2\_K\_XL checkpoints, and generated pelican-themed images with both. His favorite result came from the UD-Q2\_K\_XL quantized model using the xhigh reasoning effort setting.

rss · Simon Willison · Aug 26, 23:52

**「Background」** Qwen3.8-Flash-Next is an open-weights multimodal Mixture-of-Experts \(MoE\) model released by the Qwen team as an early preview of the architecture that Qwen4 will be built on. It has 125 billion total parameters but only 6 billion active per token, which is what gives it a significant efficiency boost. This follows the same pattern as Qwen3-Next, which previously previewed the hybrid Gated DeltaNet and Gated Attention design that later carried through the Qwen3.5, Qwen3.6, Qwen3.7, and Qwen3.8 series.

**「Impact」** The release gives self-hosting developers an early, open-weights look at Qwen4&\#x27;s architecture, with Unsloth&\#x27;s quantized GGUF files making the 125B-parameter model practical to run on a DGX Spark.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/QwenLM/Qwen3.8-Flash-Next/">Qwen3.8-Flash-Next - GitHub</a></li>
<li><a href="https://qwen.ai/blog?id=qwen3.8-flash-next">Qwen3.8-Flash-Next: A New Architecture, Towards Ultimate Cost ...</a></li>
<li><a href="https://docs.sglang.io/cookbook/autoregressive/Qwen/Qwen3.8-Flash-Next">Qwen3.8-Flash-Next - SGLang Documentation</a></li>

</ul>
</details>

**Tags**: `#Qwen`, `#open-weights`, `#MoE`, `#multimodal`, `#AI models`

---