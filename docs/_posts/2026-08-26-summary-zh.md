---
layout: default
title: "Horizon Summary: 2026-08-26 (ZH)"
date: 2026-08-26
lang: zh
---

> 从 7 条内容中筛选出 4 条重要资讯。

---

**科技新闻**
1. [GLM-5.3-Flash：更小更便宜的开放权重模型](#item-tech-news-1) ⭐️ 8.0/10
2. [Qwen3.8-Flash-Next 开源模型发布，自托管性能获社区好评](#item-tech-news-2) ⭐️ 8.0/10
3. [AWS 收购 DuckLabs，DuckDB 仍归基金会](#item-tech-news-3) ⭐️ 7.0/10
4. [EVE Online 启动从 Stackless Python 2.7 到 Python 3 的迁移](#item-tech-news-4) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [GLM-5.3-Flash：更小更便宜的开放权重模型](https://z.ai/blog/glm-5.3-flash) ⭐️ 8.0/10

Z.ai 发布了 GLM-5.3-Flash，这是一个更小、更便宜的开放权重模型变体，据称性能接近 GLM-5.3，同时大幅降低参数量和推理成本。该模型权重已发布在 Hugging Face 上，并支持在中国芯片上部署。此次发布延续了中国实验室快速迭代开放模型的趋势，可能让开发者和组织以更低成本获得接近旗舰模型的性能。具体技术细节和基准数据仍以 Z.ai 官方发布为准。

hackernews · Philpax · 8月26日 14:08 · [社区讨论](https://news.ycombinator.com/item?id=49449507)

**「背景」** GLM-5.3-Flash 是智谱（Z.ai）于 2026 年 8 月 26 日发布的开源权重模型，属于 GLM-5 系列，采用 MIT 许可证，并作为此前“Ox Alpha”匿名预览的正式版本。该模型为 320B 总参数、18B 激活参数的混合专家架构，支持 100 万 token 上下文，具备原生多模态推理能力，API 定价为每百万 token 0.15 美元（输入）和 0.50 美元（输出），同时已在 Hugging Face 上开放权重，并部署于国产芯片上。

**「影响」** 据 Z.ai 发布信息，对使用开放权重模型的开发者和组织而言，GLM-5.3-Flash 以更低参数量和成本提供接近 GLM-5.3 的性能，可能显著降低推理费用，并支持在中国芯片上部署。

**「社区讨论」** Hacker News 社区讨论普遍认为该模型性价比突出：有评论者引用独立基准称它比 Luna xhigh 更聪明且更便宜，虽不如 Luna max 聪明但价格更低，大幅优于 DeepSeek V4 Flash，甚至能以极低成本匹配 V4 Pro，大致相当于 sol medium。也有评论者提醒注意 Z.ai 服务条款中宽泛且永久的输入输出许可、模糊的禁止条款，并有人提供了 Hugging Face 权重链接和部署尝试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/z-ai/glm-5.3-flash">GLM 5.3 Flash - API Pricing &amp; Providers | OpenRouter</a></li>
<li><a href="https://www.testingcatalog.com/z-ai-launches-glm-5-3-flash-under-mit-license/">Z.ai launches GLM-5.3-Flash under MIT license</a></li>
<li><a href="https://www.explainx.ai/blog/glm-5-3-flash-ox-alpha-official-launch-august-2026">GLM-5.3-Flash Launch — Ox Alpha Was Zhipu (MIT) | explainx.ai Blog | explainx.ai</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source models`, `#GLM`, `#machine learning`, `#inference cost`

---

<a id="item-tech-news-2"></a>
### [Qwen3.8-Flash-Next 开源模型发布，自托管性能获社区好评](https://qwen.ai/blog?id=qwen3.8-flash-next) ⭐️ 8.0/10

Qwen3.8-Flash-Next 是一个新发布的开源权重模型，社区早期测试显示其在自托管场景下表现强劲。多名测试者通过 llama.cpp 临时分支或自定义配置成功运行该模型：在 IQ4\_XS 量化下约为 23.54 token/s，在 Ryzen 395/Strix Halo 上约为 22 token/s，并报告其输出质量和速度均优于 Qwen3.8 27B，甚至足以让部分用户考虑从 Qwen3.6 35B 迁移，尽管 35B 仍然更快。社区还指出，Unsloth 发布的权重默认不包含视觉支持，但用户可以自行加回。由于官方文章细节尚未提供，以上性能和兼容性信息主要来自社区实测，仍需以正式发布说明为准。

hackernews · tosh · 8月26日 12:52 · [社区讨论](https://news.ycombinator.com/item?id=49448210)

**「背景」** Qwen3.8-Flash-Next 是阿里巴巴 Qwen 团队发布的一个实验性开源权重模型，官方称其为未来 Qwen4 架构的预览版，核心是对大型语言模型各组件的交互方式进行了重新设计。该模型采用 176B 总参数、6B 激活参数的混合专家（MoE）结构，是这一新架构下的首个开源权重发布，并已获得 NVIDIA GB300 NVL72 的 day-0 支持，主要用于智能体编码等场景。社区已通过 llama.cpp 的临时分支和 Unsloth 的 GGUF 权重实现本地部署，因此该模型对自托管用户具有实际可用性。

**「影响」** 对自托管用户和 llama.cpp 使用者而言，Qwen3.8-Flash-Next 提供了在消费级硬件上以约 22–23.5 token/s 运行的更强开源替代方案，可能推动从 Qwen3.8 27B 或 Qwen3.6 35B 的迁移；但性能数据来自社区早期测试，且 Unsloth 权重需自行恢复视觉能力。

**「社区讨论」** 早期测试者普遍认为该模型在速度和输出质量上优于 Qwen3.8 27B，并分享了 llama.cpp 集成、量化配置和实测速度；也有评论将其置于中美开源策略对比中，认为中国公司更倾向于开源模型发布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen/Qwen3.8-Flash-Next · Hugging Face</a></li>
<li><a href="https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF">unsloth/Qwen3.8-Flash-Next-GGUF · Hugging Face</a></li>
<li><a href="https://www.orcarouter.ai/blog/qwen-3-8-flash-next-leak">Qwen3.8-Flash-Next Is Out: Qwen4 Architecture Confirmed</a></li>

</ul>
</details>

**标签**: `#qwen`, `#open-source-llm`, `#llama.cpp`, `#self-hosting`

---

<a id="item-tech-news-3"></a>
### [AWS 收购 DuckLabs，DuckDB 仍归基金会](https://ducklabs.com/news/2026/08/26/ducklabs-to-join-aws) ⭐️ 7.0/10

AWS 宣布收购 DuckLabs，即 DuckDB 背后的商业实体；开源 DuckDB 项目本身仍由 DuckDB 基金会持有，基金会将继续掌握开源 DuckDB 的知识产权。此次收购对数据库和开源生态意义重大，因为 DuckDB 近年来非常流行，而 AWS 是主要云厂商之一。DuckLabs 从研究机构分拆时设立了 DuckDB 基金会，该基金会持有开源 DuckDB 的全部知识产权，收购不会改变这一安排。具体整合方式、团队去向和产品路线图尚未公布。

hackernews · onderkalaci · 8月26日 12:59 · [社区讨论](https://news.ycombinator.com/item?id=49448321)

**「背景」** DuckDB 是一个开源的分析型数据库，以嵌入式、高性能和易用性著称，由荷兰阿姆斯特丹的 DuckLabs 公司主导开发。DuckLabs 是从荷兰国家数学与计算机科学研究中心（CWI）孵化出来的商业实体，而 DuckDB 开源项目的知识产权则由独立的非营利组织 DuckDB Foundation 持有。此次 AWS 宣布收购的是 DuckLabs 公司本身，而非 DuckDB 开源项目，因此 DuckDB 的开源代码和基金会治理结构预计将继续保留。

**「影响」** 对 DuckDB 用户和开发者而言，开源项目及其知识产权仍由 DuckDB 基金会持有，因此许可证和项目治理不会因收购而直接改变；此次收购主要影响 DuckLabs 的商业化路线。

**「社区讨论」** 评论者普遍指出标题有误导性：AWS 收购的是 DuckLabs，不是 DuckDB，开源代码仍由 DuckDB 基金会所有。也有人认为 AWS 对计算和存储的中立态度适合 DuckDB 发展，但另一些评论担心 AWS 内部文化会损害团队，并推荐 Apache DataFusion 作为替代。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aboutamazon.com/news/company-news/aws-ducklabs">AWS to acquire DuckLabs, the Amsterdam-based company behind DuckDB</a></li>

</ul>
</details>

**标签**: `#AWS`, `#DuckDB`, `#acquisition`, `#databases`, `#open source`

---

<a id="item-tech-news-4"></a>
### [EVE Online 启动从 Stackless Python 2.7 到 Python 3 的迁移](https://simonwillison.net/2026/Aug/25/eve-online-move-to-python-3/) ⭐️ 7.0/10

EVE Online 宣布开始从 Stackless Python 2.7 向 Python 3 迁移。该游戏自 2003 年上线以来一直运行在 Stackless Python 上，上一次大版本升级是 2010 年升级到 Stackless Python 2.7。迁移将先用 futurize 脚本处理约 240 万行代码，再人工审查约 2 万个 Python 2 与 Python 3 行为差异点，例如整数除法 1 / 2 在 Python 2 中为 0、在 Python 3 中为 0.5。公告未说明如何替换 Stackless 本身，但去年大会上他们介绍了在 EVE Frontier 的 Carbon 引擎中用开源的 carbonengine/scheduler 库取代 Stackless 的方案。

rss · Simon Willison · 8月25日 22:59

**「背景」** Stackless Python 是 Python 的一个分支，通过微线程等方式提供大规模并发支持，EVE Online 长期依赖它承载大量玩家同服的场景。由于代码量庞大且 Stackless 与标准 CPython 存在差异，从 Python 2.7 升级到 Python 3 不仅是语法迁移，还涉及运行时与调度机制的替换。

**「影响」** 对 EVE Online 开发团队而言，这意味着进入一个需要逐点核对约 2 万个行为差异的长期迁移过程；对 Python 社区而言，这是大型遗留代码库升级的又一实例。由于公告未给出 Stackless 的替代方案，迁移的最终架构仍存在不确定性。

**标签**: `#Python`, `#EVE Online`, `#migration`, `#Stackless Python`, `#software engineering`

---