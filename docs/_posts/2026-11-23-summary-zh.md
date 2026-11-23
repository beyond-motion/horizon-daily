---
layout: default
title: "Horizon Summary: 2026-11-23 (ZH)"
date: 2026-11-23
lang: zh
---

> 从 5 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [Ladybird 浏览器项目进入 Alpha 阶段](#item-tech-news-1) ⭐️ 8.0/10
2. [GLM-5.4 发布：首个循环 Transformer 面向通用编码](#item-tech-news-2) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Ladybird 浏览器项目进入 Alpha 阶段](https://ladybird.org/posts/alpha/) ⭐️ 8.0/10

Ladybird 浏览器项目宣布进入 alpha 阶段，这是其从零构建独立浏览器引擎过程中的一个重要里程碑。该项目致力于提供不依赖现有主流引擎的开源浏览器实现，因此对浏览器引擎多样性和 Web 平台生态具有特别意义。当前版本仍不是面向生产环境的主流浏览器，功能与稳定性尚待继续完善。此次发布也引发了开发者社区对其实用性和安全性的集中讨论。

hackernews · janvdberg · 11月23日 16:13 · [社区讨论](https://news.ycombinator.com/item?id=50614249)

**「项目背景」** Ladybird 最初是 SerenityOS 爱好者操作系统的内置浏览器，2022 年成为独立的跨平台项目，现由美国 501\(c\)\(3\) 非营利组织 Ladybird Browser Initiative 依靠捐赠和赞助开发。从 SerenityOS 分叉后，项目不再坚持自研全部组件，而是引入第三方库来处理图像、音频、视频格式、加密和图形等通用功能，其中部分库也为其他浏览器所用。随着首个 alpha 版本临近，项目于 2026 年 6 月 5 日宣布不再接受公开 pull request，也不开放其他由非维护者提交补丁的渠道，理由是贡献质量参差，并且浏览器越接近发布越需要加强安全性。

**「影响」** 对使用 macOS 和 Linux 的开发者来说，现在可以实际试用一个并非从 Chromium、Gecko 或 WebKit 分支而来的独立引擎，并据此反馈网页兼容性问题；但官方仍将其定位为面向开发者的 alpha 版本，尚不适合用于登录、支付等敏感场景的日常浏览。

**「社区讨论」** 有社区成员实测后表示，多个网站（包括 YouTube 和 Google Maps）能够正确渲染，但页面滚动略有卡顿、部分站点运行较慢；也有人提到 Ladybird 改用 SQLite、Skia 等生产级依赖显著改善了浏览器表现。另有评论提醒 alpha 阶段应关注安全风险，建议避免用于需要登录、认证、支付或下载的场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ladybird_%28web_browser%29">Ladybird (web browser) - Wikipedia</a></li>
<li><a href="https://ladybird.org/">Ladybird</a></li>
<li><a href="https://ladybird.org/index.html?_hsenc=p2ANqtz--Bsp32Lwf1DeVtYTqRvmo2s8tDw1qi9ZnWR4WTC3HqRkpH0-4UW_UFJQGDraQ2G0fK3CFQfVb0QYMKk3qYqUITJfqv0A&amp;_hsmi=314104664">A truly independent - Ladybird Ladybird (web browser) — Edgepedia 67,377 stars and zero Chromium: I ran Ladybird alpha Ladybird: A new, independent browser engine — written from ... SerenityOS Creator Is Building an Independent, Standards ...</a></li>
<li><a href="https://github.com/LadybirdBrowser/ladybird">GitHub - LadybirdBrowser/ ladybird : Truly independent web browser</a></li>
<li><a href="https://ladybird.org/">Ladybird is a truly independent web browser , backed by a non-profit.</a></li>

</ul>
</details>

**标签**: `#browsers`, `#open-source`, `#web-engines`, `#ladybird`, `#software-engineering`

---

<a id="item-tech-news-2"></a>
### [GLM-5.4 发布：首个循环 Transformer 面向通用编码](https://z.ai/blog/glm-5.4) ⭐️ 8.0/10

智谱发布 GLM-5.4，将其定位为面向通用编码的模型，并称这是其首个采用循环 Transformer（loop transformer）的版本。随发布博客给出了较详细的技术披露，该消息在 Hacker News 获得 864 分和 307 条评论，讨论集中在循环架构能否缓解推理内存带宽瓶颈，以及仍有待解决的问题。有开发者报告，GLM-5.4 目前未通过 OpenRouter 或常规 Z.ai API 套餐提供，需改用 Coding Plan 才能获得可调用新模型的 API key。社区肯定其透明度，但也有人指出部分中国模型在简单任务上仍会进行冗长的“马拉松式思考”，实际体验和广泛影响尚待观察。

hackernews · foohis · 11月23日 10:06 · [社区讨论](https://news.ycombinator.com/item?id=50609685)

**「背景」** GLM 是智谱（Z.ai）的大模型系列，GLM-5.4 是该系列的最新旗舰，也是首个基于 Loop Transformer 架构构建的模型；官方称其智能水平可对标参数规模为 2T–3T 的模型。传统 Transformer 在推理时通常让每层权重只参与一次计算；循环 Transformer 则让部分层重复执行，从而以较少的新增参数获得更深的有效计算。据公开介绍，GLM-5.4 的 78 层中有 28 层会运行两次，并延续了 GLM-5.3 的 1M 上下文长度。

**「对开发者的影响」** 对打算使用该模型的开发者而言，GLM-5.4 已被纳入智谱的 Coding Plan（据称其 API 密钥与常规密钥用法相同），而它通过循环复用层来增加有效深度、避免独立参数按比例增长，目标是让更小的参数规模达到 2T–3T 参数级模型的能力并降低推理时的显存带宽开销，不过官方也承认模型仍存在限制。

**「社区讨论」** 评论者普遍赞赏智谱披露的技术细节，认为在西方公司趋于封闭的背景下，这种透明度有助于观察 SOTA LLM 的演进方向；也有人从推理内存带宽角度解释循环 Transformer 的动机，但承认仍有问题待解决。实际使用层面，开发者报告 GLM-5.4 暂未通过 OpenRouter 或常规 Z.ai API 套餐开放，需改用 Coding Plan，并抱怨部分中国模型在简单任务上也会进行冗长的“马拉松式思考”，显著拉长完成时间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.z.ai/guides/llm/glm-5.4">GLM - 5 . 4 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://www.youtube.com/watch?v=HVey00YZ5Xk">GLM - 5 . 4 Is Here: The First Loop Transformer , and What... - YouTube</a></li>
<li><a href="https://teamorouter.com/blogs/glm-5-4">GLM - 5 . 4 Released: Vision, Stronger Coding , and When the API Arrives</a></li>
<li><a href="https://z.ai/blog/glm-5.4">GLM-5.4: Toward Generalized Coding with Our First Loop ...</a></li>
<li><a href="https://www.techinasia.com/news/chinas-zhipu-added-glm54-coding-plan">China’s Zhipu said to have added GLM-5.4 to coding plan</a></li>

</ul>
</details>

**标签**: `#LLM architecture`, `#loop transformers`, `#coding models`, `#Zhipu GLM`, `#model release`

---