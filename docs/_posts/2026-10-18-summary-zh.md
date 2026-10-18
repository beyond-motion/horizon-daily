---
layout: default
title: "Horizon Summary: 2026-10-18 (ZH)"
date: 2026-10-18
lang: zh
---

> 从 6 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [TempoPFN：线性 RNN 合成预训练用于零样本时间序列预测](#item-tech-news-1) ⭐️ 8.0/10
2. [RepRapMicron 微米级开源制造项目](#item-tech-news-2) ⭐️ 7.0/10
3. [DeepSeek 推出按成功请求计费的搜索与抓取 API](#item-tech-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [TempoPFN：线性 RNN 合成预训练用于零样本时间序列预测](https://www.reddit.com/r/MachineLearning/comments/1x97v19/tempopfn_synthetic_pretraining_of_linear_rnns_for/) ⭐️ 8.0/10

Reddit 用户 /u/Yossarian\_1234 发帖介绍论文 TempoPFN，称其已被 NeurIPS 2026 接收，核心内容是提供一套合成时间序列生成器与数据增强方法，用于预训练时间序列基础模型，论文中具体采用的是线性 RNN，目标是实现零样本（zero-shot）时间序列预测。作者为 Vladyslav Moroshan、Julien Siems、Arber Zela、Timur Carstensen 和 Frank Hutter，并同步开源了代码库、模型与相关资源。帖子称这些合成数据已被 Toto-2 和 TS-ICL 使用，说明该方法在其他基础模型中已获得复用。公开资源包括 arXiv 论文 2510.25502、GitHub 仓库 automl/TempoPFN 以及 Hugging Face 上的 AutoML-org/TempoPFN。帖子本身未给出具体基准测试结果、性能数据或与现有方法的量化对比。

reddit · r/MachineLearning · /u/Yossarian\_1234 · 10月18日 16:43

**「背景」** 时间序列基础模型的目标是在不针对具体数据集重新训练的前提下完成零样本预测，但长期以来，高效的长程预测与结果可复现性一直是难点，而以往仅依赖合成数据的方案在较困难的基准上表现不佳。TempoPFN 采用线性 RNN（GatedDeltaProduct 架构）构建单变量时间序列基础模型，借助完全可并行化的训练流程和一套完整的合成数据流水线来实现零样本预测。该工作的核心贡献之一正是这套合成时间序列生成器与数据增强方法。

**「影响」** 对时间序列研究者与开发者而言，该工作开源了完整的训练与推理代码、合成数据生成流程以及 38M 参数的预训练模型，使其无需真实数据即可复现纯合成预训练，并且其合成数据已被 Toto-2 与 TS-ICL 采用，说明影响已超出单一模型。不过 TempoPFN 目前是单变量预测模型，其在多变量场景下的适用性尚未得到验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.25502">[ 2510 . 25502 ] TempoPFN : Synthetic Pre - training of Linear RNNs for...</a></li>
<li><a href="https://arxiv.org/html/2510.25502v3">TempoPFN : Synthetic Pre - training of Linear RNNs for Zero - shot ...</a></li>
<li><a href="https://paperswithcode.co/paper/2510.25502">TempoPFN : Synthetic Pre - training of Linear RNNs for Zero - shot ...</a></li>
<li><a href="https://arxiv.org/abs/2510.25502">[2510.25502] TempoPFN: Synthetic Pre-training of Linear RNNs ... GitHub - automl/TempoPFN: TempoPFN: Zero-shot Time Series ... TempoPFN: synthetic pre-training of linear RNNs… · AGI Hunt TempoPFN: Synthetic Pre-training of Linear RNNs for Zero-shot ... Toto - Time Series Optimized Transformer for ... - GitHub TempoPFN: Towards Synthetic Pre-training of Linear RNNs for... TempoPFN: Univariate Zero-Shot Forecasting</a></li>
<li><a href="https://github.com/automl/TempoPFN">GitHub - automl/TempoPFN: TempoPFN: Zero-shot Time Series ...</a></li>
<li><a href="https://agihunt.info/en/p/1a14fe903da7d7d171c210e6500">TempoPFN: synthetic pre-training of linear RNNs… · AGI Hunt</a></li>

</ul>
</details>

**标签**: `#time-series-forecasting`, `#foundation-models`, `#synthetic-data`, `#linear-RNNs`, `#pre-training`

---

<a id="item-tech-news-2"></a>
### [RepRapMicron 微米级开源制造项目](https://github.com/VikOlliver/RepRapMicron/wiki) ⭐️ 7.0/10

用户 RobotToaster 在 Hacker News 上提交了一个指向 GitHub 上 RepRapMicron 项目 wiki 的条目，该项目被描述为源自 RepRap 的开源微米级打印/制造计划，讨论将其与精密制造乃至 DIY 半导体工作联系起来。由于提供的来源只是一个 GitHub wiki 落地页，没有可用的正文内容，因此目前无法确认其具体工艺、精度、版本、兼容性或性能数据。该条目之所以受到关注，是因为它可能代表一种面向微米尺度制造的开源硬件路径，但其实际能力与行业影响尚未得到证实。

hackernews · RobotToaster · 10月18日 13:48 · [社区讨论](https://news.ycombinator.com/item?id=50141076)

**「背景」** RepRap 是一个开源 3D 打印项目，目标是让普通人也能自行搭建并复制 3D 打印机。RepRapMicron（μRepRap）是该项目的延伸，试图把这种开放式制造能力推进到微米尺度，让微小尺度制造也能广泛普及。据项目资料，它是一套三轴 3D 打印机构，精度可达数微米、特征尺寸约 10μm–20μm，可配合标准 3D 打印机与 CNC 控制器使用，并可由普通的 3D 打印或 CNC 爱好者自行搭建。

**「影响」** 对开源硬件爱好者和小型开发者而言，µRepRap 的目标是把微米乃至亚微米级制造能力带到桌面，就像当年 RepRap 普及 3D 打印那样，从而让停留在软件里的芯片设计有可能被低成本、可持续地实际打印出来。不过目前公开的实测成果仅是一次耗时 13 小时、长 0.650mm 的 3DBenchy 打印，距可用于 DIY 芯片制造仍有明显差距。

**「社区讨论」** 评论者把该项目类比为 1790 年代 Ramsden、Maudslay 和 Wilkinson 在精密刻度、螺纹切削和镗孔方面的突破，认为这可能把微米级制造从手工技艺推向可重复生产；也有人提到相关 YouTube 系列及其前置技术。另一些评论则对 DIY 芯片制造表示期待或调侃，例如“18 个月后就能自己做 RAM”，并提出如果打印机真能低成本、可持续地打印芯片设计，硬件领域可能出现有趣转折，同时有人质疑为何不更多使用可在数十微米尺度施力并带力反馈的压电致动器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/VikOlliver/RepRapMicron">GitHub - VikOlliver/RepRapMicron: μRepRap - A 3D printer ...</a></li>
<li><a href="https://reprap.org/wiki/RepRapMicron">RepRapMicron - RepRap RepRapMicron Micron Scale 3D Printer by vik - Thingiverse RepRapMicron/Presentations/EverythingOpen_2026_as_presented ... RepRapMicron Micron Scale 3D Printer by vik - Thingiverse RepRapMicron Promises Micro-fabrication For Desktops With New ... RepRapMicron: an open-source microscale RepRap… · AGI Hunt</a></li>
<li><a href="https://www.thingiverse.com/thing:7029371/files">RepRapMicron Micron Scale 3D Printer by vik - Thingiverse</a></li>
<li><a href="https://reprap.org/wiki/RepRapMicron">RepRapMicron - RepRap</a></li>
<li><a href="https://hackaday.com/2025/08/22/reprapmicron-promises-micro-fabrication-for-desktops-with-new-prototype/">RepRapMicron Promises Micro- fabrication For Desktops... | Hackaday</a></li>
<li><a href="https://makeprintable.com/reprap-micron-achieves-0-650mm-3dbenchy-print/">RepRap Micron Achieves 0.650mm 3DBenchy Print - makeprintable</a></li>

</ul>
</details>

**标签**: `#open-source hardware`, `#3D printing`, `#microfabrication`, `#RepRap`, `#semiconductor manufacturing`

---

<a id="item-tech-news-3"></a>
### [DeepSeek 推出按成功请求计费的搜索与抓取 API](https://api-docs.deepseek.com/guides/search/) ⭐️ 7.0/10

DeepSeek 推出了搜索与抓取（search and fetch）API，定价为每 1000 次成功请求 0.75 美元。该服务面向需要联网搜索与网页抓取的 AI 代理和 RAG 开发者，计费口径强调“成功请求”。它在 Hacker News 上引发了对成本、替代方案以及面向 AI 代理的搜索 API 经济性的讨论。有评论给出价格对比：Brave Search API 为 5 美元，Kagi API 为 12 美元，认为 DeepSeek 的定价明显更低。目前可用信息主要来自 DeepSeek 的 API 文档和社区评论，未提供更多技术细节或性能数据。

hackernews · fagnerbrack · 10月18日 06:50 · [社区讨论](https://news.ycombinator.com/item?id=50138531)

**「背景」** 搜索 API 是让 AI 智能体与检索增强生成（RAG）应用以结构化形式获取网页检索结果的基础设施，通常按调用量计费。由于 Google 长期未提供付费的通用搜索 API，开发者此前多依赖 Brave、Kagi 等第三方服务，或自行编写抓取网页的封装，而后者常被搜索引擎拦截。DeepSeek 是中国 AI 模型厂商，此次在其 API 中新增 Search 与 Fetch 接口，公开定价为每 1000 次请求 5 元人民币（约 0.75 美元），Search 接口返回按相关性排序的结构化结果列表。

**「影响」** 对构建检索增强生成（RAG）或搜索型 AI 代理的开发者而言，DeepSeek 按每 1000 次成功请求 0.75 美元计费且只对成功请求收费，按社区评论给出的对比数字，约为 Brave Search API（每 1000 次 5 美元）和 Kagi API（12 美元）的十分之一量级，有望显著压低代理搜索调用的单位成本。不过竞品价格来自评论者而非官方文档，且 Brave 的公开定价按档位从免费额度到约每 1000 次查询 30 美元不等，选型时仍需核对各家最新定价、限额与调用条款。

**「社区讨论」** 评论普遍把 DeepSeek 的 0.75 美元定价视为对 Brave（5 美元）和 Kagi（12 美元）等托管搜索 API 的低价竞争，但也有人质疑这类服务的实际使用场景，认为 SearXNG 等自建免费方案对个人更划算。另有观点推测搜索 API 未来可能因 SEO 和代理流量竞争而出现负价格，并指出这些服务存在的一个原因是 Google 不提供付费搜索 API；还有人建议 DeepSeek 在下一代模型中使用来源感知训练。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50138531">DeepSeek search and fetch – $ 0 . 75 per 1000 successful requests</a></li>
<li><a href="https://api-docs.deepseek.com/api/search/">Search | DeepSeek API Docs</a></li>
<li><a href="https://www.globaltimes.cn/page/202610/1372476.shtml">DeepSeek unveils faster, cheaper AI model, with... - Global Times</a></li>
<li><a href="https://costbench.com/software/ai-search-apis/brave-search-api/">Brave Search API Pricing 2026: Free-$30 per 1K queries</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#search API`, `#AI agents`, `#pricing`, `#web search`

---