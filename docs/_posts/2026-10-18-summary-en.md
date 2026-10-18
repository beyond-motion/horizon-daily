---
layout: default
title: "Horizon Summary: 2026-10-18 (EN)"
date: 2026-10-18
lang: en
---

> From 6 items, 3 important content pieces were selected

---

**Technology News**
1. [TempoPFN: Synthetic Pre-training of Linear RNNs for Zero-shot Forecasting](#item-tech-news-1) ⭐️ 8.0/10
2. [RepRapMicron Wiki Sparks Hacker News Interest in DIY Microfabrication](#item-tech-news-2) ⭐️ 7.0/10
3. [DeepSeek search and fetch API costs $0.75 per 1,000 requests](#item-tech-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [TempoPFN: Synthetic Pre-training of Linear RNNs for Zero-shot Forecasting](https://www.reddit.com/r/MachineLearning/comments/1x97v19/tempopfn_synthetic_pretraining_of_linear_rnns_for/) ⭐️ 8.0/10

A Reddit post announces TempoPFN, a NeurIPS 2026-accepted paper and open-source library for synthetic pre-training of linear RNNs for zero-shot time series forecasting. The work presents a library of synthetic time series generators and augmentations used to train time series foundation models, specifically a linear RNN. The authors are Vladyslav Moroshan, Julien Siems, Arber Zela, Timur Carstensen, and Frank Hutter, with resources available on arXiv \(2510.25502\), GitHub \(automl/TempoPFN\), and Hugging Face \(AutoML-org/TempoPFN\). The synthetic data has already been reused in Toto-2 and TS-ICL, indicating practical adoption by other foundation model efforts.

reddit · r/MachineLearning · /u/Yossarian\_1234 · Oct 18, 16:43

**「Background」** Foundation models for zero-shot time series forecasting aim to predict future values of previously unseen series without task-specific training, but they face challenges in efficient long-horizon prediction and reproducibility, and existing synthetic-data-only approaches have underperformed on challenging benchmarks. TempoPFN addresses this as a univariate time series foundation model built on linear RNNs with a GatedDeltaProduct architecture, which enables fully parallelizable training. Its approach relies on a synthetic data pipeline of generators and augmentations, rather than large collections of real-world series.

**「Impact」** Time-series forecasting researchers and developers gain an openly released synthetic-only pre-training pipeline and a 38M-parameter pretrained model that reaches 0.533 MASE on GIFT-Eval, beating TabPFN-TS \(0.544\) and Chronos Bolt \(0.574\), with the synthetic data already reused in Toto-2 and TS-ICL. The reported model is univariate, so the gains may not transfer directly to multivariate forecasting settings.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.25502">[ 2510 . 25502 ] TempoPFN : Synthetic Pre - training of Linear RNNs for...</a></li>
<li><a href="https://arxiv.org/html/2510.25502v3">TempoPFN : Synthetic Pre - training of Linear RNNs for Zero - shot ...</a></li>
<li><a href="https://paperswithcode.co/paper/2510.25502">TempoPFN : Synthetic Pre - training of Linear RNNs for Zero - shot ...</a></li>
<li><a href="https://arxiv.org/abs/2510.25502">[2510.25502] TempoPFN: Synthetic Pre-training of Linear RNNs ... GitHub - automl/TempoPFN: TempoPFN: Zero-shot Time Series ... TempoPFN: synthetic pre-training of linear RNNs… · AGI Hunt TempoPFN: Synthetic Pre-training of Linear RNNs for Zero-shot ... Toto - Time Series Optimized Transformer for ... - GitHub TempoPFN: Towards Synthetic Pre-training of Linear RNNs for... TempoPFN: Univariate Zero-Shot Forecasting</a></li>
<li><a href="https://github.com/automl/TempoPFN">GitHub - automl/TempoPFN: TempoPFN: Zero-shot Time Series ...</a></li>
<li><a href="https://agihunt.info/en/p/1a14fe903da7d7d171c210e6500">TempoPFN: synthetic pre-training of linear RNNs… · AGI Hunt</a></li>

</ul>
</details>

**Tags**: `#time-series-forecasting`, `#foundation-models`, `#synthetic-data`, `#linear-RNNs`, `#pre-training`

---

<a id="item-tech-news-2"></a>
### [RepRapMicron Wiki Sparks Hacker News Interest in DIY Microfabrication](https://github.com/VikOlliver/RepRapMicron/wiki) ⭐️ 7.0/10

A GitHub wiki page for RepRapMicron, an open-source micron-scale printing and fabrication project, was submitted to Hacker News. The supplied item is only a wiki landing page, so it provides no specific technical specifications, versions, dates, performance data, or fabrication results. The Hacker News discussion connects the project to precision manufacturing and the speculative possibility of DIY semiconductor work, including making custom chips or RAM. Those broader applications are presented by commenters as hopes or jokes rather than demonstrated capabilities.

hackernews · RobotToaster · Oct 18, 13:48 · [Discussion](https://news.ycombinator.com/item?id=50141076)

**「Background」** RepRap began as an open-source project to build self-replicating 3D printers that enthusiasts could assemble and reproduce themselves, bringing open fabrication to a wide audience. RepRapMicron, or μRepRap, extends that concept to micron-scale fabrication: it is a 3-axis mechanism accurate to a few microns with a feature size of roughly 10–20 μm, designed to work with standard 3D printer and CNC controllers and to be built by the average 3D printer or CNC enthusiast. The project is maintained by RepRap community developer Vik Olliver, and its wiki documents the hardware designs, toolheads, and control software.

**「Impact」** For hobbyist and open-source hardware developers, µRepRap&\#x27;s microscale printing results — including a 0.650 mm 3DBenchy produced in a 13-hour job — point toward desktop access to micron and sub-micron fabrication, though any path to practical DIY semiconductor work remains speculative.

**「Community Discussion」** Commenters compared the project to late-1790s machine-tool breakthroughs that made precision manufacturing repeatable, shared related video resources, and speculated about eventually enabling cheap, sustainable DIY chip or RAM production. One commenter questioned why piezoelectric actuators are not more widely used for micron-scale motion, citing their ability to apply useful force over tens to hundreds of micrometers and provide force feedback.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/VikOlliver/RepRapMicron">GitHub - VikOlliver/RepRapMicron: μRepRap - A 3D printer ...</a></li>
<li><a href="https://reprap.org/wiki/RepRapMicron">RepRapMicron - RepRap RepRapMicron Micron Scale 3D Printer by vik - Thingiverse RepRapMicron/Presentations/EverythingOpen_2026_as_presented ... RepRapMicron Micron Scale 3D Printer by vik - Thingiverse RepRapMicron Promises Micro-fabrication For Desktops With New ... RepRapMicron: an open-source microscale RepRap… · AGI Hunt</a></li>
<li><a href="https://www.thingiverse.com/thing:7029371/files">RepRapMicron Micron Scale 3D Printer by vik - Thingiverse</a></li>
<li><a href="https://reprap.org/wiki/RepRapMicron">RepRapMicron - RepRap</a></li>
<li><a href="https://hackaday.com/2025/08/22/reprapmicron-promises-micro-fabrication-for-desktops-with-new-prototype/">RepRapMicron Promises Micro- fabrication For Desktops... | Hackaday</a></li>
<li><a href="https://makeprintable.com/reprap-micron-achieves-0-650mm-3dbenchy-print/">RepRap Micron Achieves 0.650mm 3DBenchy Print - makeprintable</a></li>

</ul>
</details>

**Tags**: `#open-source hardware`, `#3D printing`, `#microfabrication`, `#RepRap`, `#semiconductor manufacturing`

---

<a id="item-tech-news-3"></a>
### [DeepSeek search and fetch API costs $0.75 per 1,000 requests](https://api-docs.deepseek.com/guides/search/) ⭐️ 7.0/10

DeepSeek has launched a search and fetch API priced at $0.75 per 1,000 successful requests, according to its API documentation. The service is aimed at developers building AI agents and retrieval-augmented generation systems that need programmatic web search and page-fetching capabilities. On Hacker News, the release prompted discussion about the cost of search infrastructure for AI, with commenters comparing it to alternatives and debating whether hosted providers are necessary. The pricing is notable because search APIs are a key component for search-augmented LLM applications, and the release adds a low-cost option for teams evaluating hosted search and fetch services.

hackernews · fagnerbrack · Oct 18, 06:50 · [Discussion](https://news.ycombinator.com/item?id=50138531)

**「Background」** Search and fetch APIs let AI agents and retrieval-augmented generation systems query the web and receive structured, ranked results for use in prompts or tool calls \[tool-1-2\]. DeepSeek has made its Search and Fetch interfaces publicly available through its API at a price of 5 yuan \(about $0.75\) per 1,000 requests \[tool-1-3\]. This enters a market where developers otherwise use other paid search APIs or scrape search engines directly, which users report often leads to blocking \[tool-1-1\].

**「Impact」** At $0.75 per 1,000 successful requests, DeepSeek&\#x27;s search and fetch API is priced well below the $5 Brave Search API and $12 Kagi API figures cited by commenters, which could materially lower per-query costs for teams building search-augmented AI agents and RAG pipelines. Because billing counts only successful requests, actual spend will depend on how often calls succeed in practice, and the comparison rests on community-reported figures rather than vendor documentation.

**「Community discussion」** Commenters compared DeepSeek&\#x27;s price favorably with Brave Search API at $5 and Kagi API at $12 per 1,000 requests, while questioning the need for hosted search providers when free self-hosted or scraping alternatives like SearXNG-based tools and oh-my-pi exist. Others argued that such APIs exist because Google does not offer a paid search API, and one commenter speculated that search API prices could eventually go negative as agent-driven search becomes a major influence channel.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50138531">DeepSeek search and fetch – $ 0 . 75 per 1000 successful requests</a></li>
<li><a href="https://api-docs.deepseek.com/api/search/">Search | DeepSeek API Docs</a></li>
<li><a href="https://www.globaltimes.cn/page/202610/1372476.shtml">DeepSeek unveils faster, cheaper AI model, with... - Global Times</a></li>
<li><a href="https://costbench.com/compare/brave-search-api-vs-kagi-search-api/">Brave Search API vs Kagi Search API Pricing (2026)</a></li>
<li><a href="https://costbench.com/software/ai-search-apis/brave-search-api/">Brave Search API Pricing 2026: Free-$30 per 1K queries</a></li>
<li><a href="https://api-dashboard.search.brave.com/app/plans">Pricing - api-dashboard.search.brave.com</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#search API`, `#AI agents`, `#pricing`, `#web search`

---