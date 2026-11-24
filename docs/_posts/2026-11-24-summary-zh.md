---
layout: default
title: "Horizon Summary: 2026-11-24 (ZH)"
date: 2026-11-24
lang: zh
---

> 从 6 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [Ladybird 首个 alpha 发布：macOS 与 Linux 可直接安装](#item-tech-news-1) ⭐️ 8.0/10
2. [GPT-6.2 Astra 自主识别 1808 年匿名素描本作者](#item-tech-news-2) ⭐️ 7.0/10
3. [Z.ai 发布首个循环 Transformer 模型 GLM-5.4](#item-tech-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Ladybird 首个 alpha 发布：macOS 与 Linux 可直接安装](https://simonwillison.net/2026/Nov/23/ladybird/) ⭐️ 8.0/10

Ladybird 发布了首个 alpha 版本，macOS 和 Linux 用户现在可以直接安装，无需自行编译。该项目自研 HTML 解析、CSS 引擎、布局、JavaScript 和 WebAssembly 等核心组件，但仍使用 HarfBuzz、Skia、ffmpeg 和 SQLite 等外部库。Simon Willison 试用后称其速度很快、界面轻量，WASM 视频压缩工具和 Pyodide REPL 可正常运行，但 Datasette Lite 在调用 \`navigator.serviceWorker.startMessages\` 时报错，他已提交 issue，源码中也有相应 FIXME。2026 年 10 月的更新将样式和布局移到独立线程、加入新的 JavaScript JIT，并让新的 WebAssembly 引擎在 JetStream 3 WASM 基准上提升 7 倍；WPT 通过数增加 75,650 项至 2,184,722 项，超过 Safari、略低于 Firefox，官方称大部分增量来自 AI 编码代理。官方同时警告这是 alpha，部分网站会无法使用且浏览器有时会崩溃，用户可从浏览器内报告损坏站点并选择是否发送崩溃报告。

rss · Simon Willison · 11月23日 21:46

**「背景」** Ladybird 是一个源自 SerenityOS 的独立浏览器项目，以自行实现浏览器引擎的绝大多数核心组件为目标。首个 alpha 的意义在于，它从需要自行编译的源码项目变成了可直接安装的早期版本，让外部用户能够开始测试这套独立引擎。

**「影响」** 对 macOS 和 Linux 用户及 Web 开发者而言，Ladybird 首次提供了无需编译即可评估这套独立引擎的入口，但其 alpha 阶段的崩溃和站点兼容性缺口意味着现阶段更适合测试与反馈，而非作为日常主力浏览器。

**标签**: `#Ladybird`, `#web browsers`, `#open source`, `#browser engines`, `#alpha release`

---

<a id="item-tech-news-2"></a>
### [GPT-6.2 Astra 自主识别 1808 年匿名素描本作者](https://simonwillison.net/2026/Nov/24/astra-historical-mystery/) ⭐️ 7.0/10

Simon Willison 转述历史学教授 Mark Humphries 的案例研究称，GPT-6.2 Astra 在极少提示下，用 22 分钟自主查明耶鲁大学贝内克图书馆所藏匿名 1808 年素描本的作者。模型利用公开的一手和二手资料，在纸质档案中发现一条鲜为人知的来源，并预测查阅该来源可验证其假设，最终结果支持了假设。Astra 注意到一份日记提到夏博子爵（vicomte de Chabot）在素描本所记附近河流日期前五天到访，并建议查阅仅可通过克利夫兰州立大学订购的 Chabot 旅行日志来确认作者身份。Humphries 认为这项新来源本身对加拿大史和毛皮贸易史研究具有重要价值，并预计历史学界对智能体系统的信心冲击会比数学界温和，因为历史研究强调不断重新解释过去，而非追求单一普适真理。

rss · Simon Willison · 11月24日 16:53

**「背景」** 贝内克图书馆是耶鲁大学收藏珍本与手稿的图书馆；这本 1808 年的匿名素描本记录了一段从蒙特利尔到苏必利尔湖的旅程，两个多世纪未能确定作者，且仅有四幅带日期的图像可作为线索。历史学教授 Mark Humphries 将这一档案问题交给 GPT-6.2 Astra；该模型作为可自主检索公开一手和二手资料的 AI 代理，会先提出假设，再寻找档案证据加以验证。这正是此次案例的方法背景，也是它受到关注的原因。

**「影响」** 对档案与历史研究人员而言，这一案例显示智能体可在数十分钟内完成原本需人工交叉检索的来源考证，并产生可进一步核验的新史料线索；但结论仍来自单一案例和二手转述，尚不足以证明其可普遍复现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=Lfgz2tLJGEM">Mark Humphries fed an 1808 Yale sketchbook to GPT-6.2 Astra # ...</a></li>
<li><a href="https://blockchain.news/ainews/gpt-6-2-astra-traced-1808-sketchbook-to-vicomte-de-chabot">GPT-6.2 Astra traced 1808 sketchbook to vicomte de Chabot</a></li>
<li><a href="https://hellomarvisaitoday.com/articles/b6013a51-1c51-4040-b16f-d8b5f590cc9f">GPT-6.2 Astra IDs 1808 sketchbook author in 22 minutes</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#historical research`, `#GPT-6.2 Astra`, `#case study`

---

<a id="item-tech-news-3"></a>
### [Z.ai 发布首个循环 Transformer 模型 GLM-5.4](https://simonwillison.net/2026/Nov/23/glm-54/) ⭐️ 7.0/10

Z.ai 发布 GLM-5.4，这是其首个采用循环 Transformer 架构的模型，也是近期第二款引发关注的此类模型；Thinking Machines Lab 的 Inkling 2 Mini 于 11 月 20 日也采用了循环结构。GLM-5.4 让一组共享权重的层在一次前向传播中多次运行并细化隐藏状态，从而在不增加参数量的情况下加深网络。该模型目前尚未开放权重，Z.ai 表示将在完成必要安全加固后负责任地开源；现阶段它只能通过 Coding Plan 订阅使用，普通 API 尚不能直接访问，但两者共用位于 https://api.z.ai/api/v1 的 OpenAI 兼容 Responses API。Simon Willison 用自建的 llm-glm 插件进行了测试，发现其绘图质量与 GLM-5.3 相近，而 GLM-5.1 和 5.2 的独特风格在 5.3 之后明显消失；他还提到已有的 llm-zai 插件尚未支持新模型。

rss · Simon Willison · 11月23日 23:40

**「背景」** 在标准 Transformer 中，每一层在一次前向传播中只运行一次；循环 Transformer 则让一组共享权重的层重复执行多轮，反复细化隐藏状态，从而在不增加参数量的情况下加深有效网络深度。Z.ai 于 2026 年 11 月 23 日发布的 GLM-5.4 是其首个采用该架构的旗舰模型，官方称其智能水平可与 2T-3T 参数级模型相比。此前 Thinking Machines Lab 于 11 月 20 日发布的 Inkling 2 Mini 也采用循环结构，对每个 token 将中间层运行三次，显示这一思路在当月连续进入新模型。

**「影响」** 希望试用 GLM-5.4 的开发者目前只能通过 Z.ai 的 Coding Plan 订阅访问，普通 API 尚未开放，模型权重也尚未公开；官方称需完成安全加固后才会有条件开源。由于发布时既无基准测试数据也无公开定价，其编程能力提升幅度暂时无法独立验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://z.ai/blog/glm-5.4">GLM-5.4: Toward Generalized Coding with Our First Loop ...</a></li>
<li><a href="https://dev.to/amananandrai/loop-transformers-thinking-deeper-without-getting-bigger-glm-54-inkling-2-mini-501m">Loop Transformers: Thinking Deeper Without Getting Bigger ...</a></li>
<li><a href="https://www.orcarouter.ai/blog/glm-5-4-release-what-we-know">GLM - 5 . 4 Arrives on Z . ai &#x27;s Coding Plan: No Benchmarks Yet</a></li>

</ul>
</details>

**标签**: `#looped transformers`, `#LLM architecture`, `#GLM-5.4`, `#Z.ai`, `#AI model releases`

---