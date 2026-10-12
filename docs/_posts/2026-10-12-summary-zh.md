---
layout: default
title: "Horizon Summary: 2026-10-12 (ZH)"
date: 2026-10-12
lang: zh
---

> 从 4 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [Python 3.15 发布：新增惰性导入，3.10 停止支持](#item-tech-news-1) ⭐️ 9.0/10
2. [Meta 发布 Muse Wonder，社区质疑视觉基准表现](#item-tech-news-2) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Python 3.15 发布：新增惰性导入，3.10 停止支持](https://simonwillison.net/2026/Oct/12/python-3-15/) ⭐️ 9.0/10

Python 3.15 已发布，官方 What&\#x27;s new 指南由 3.14 和 3.15 发布经理 Hugo van Kemenade 整理；同时 Python 3.10 已不再受支持，因此维护跨版本兼容开源软件的 Simon Willison 表示可以告别 3.10 并开始采用 3.11 的特性。3.15 的亮点包括 PEP 810 显式惰性导入，允许 \`lazy import json\` 和 \`lazy from pathlib import Path\`，模块会在后续代码首次使用这些符号时才导入，以缓解插件等场景的启动开销。PEP 798 为推导式加入 \`\[\*sublist for sublist in lists\]\` 等解包语法，扩展自 2015 年 Python 3.5 落地的 PEP 448。标准库把原 cProfile 追踪分析器更名为 profiling.tracing，并新增名为 Tachyon 的采样分析器 profiling.sampling，可附加到已有进程以低开销采样，示例在 2.65 秒内采集 2,651 个样本、采样率约 999.98 样本/秒、错误率 0.19，99.9% 直接耗时落在 KqueueSelector.select，并可生成火焰图、热图和 Firefox profiler 格式。性能方面，Miguel Grinberg 针对 3.15.0rc3 的测试显示整体与 3.14 大致相同，但实验性 JIT 在 Fibonacci 测试中比标准 3.15 解释器快 1.2 倍，这是他首次观察到 JIT 有意义的性能提升；文章还介绍了用 uv 升级到 Python 3.15 的命令序列，但原文在升级 uv 处截断。

rss · Simon Willison · 10月12日 18:15

**「背景」** Python 由 CPython 发布，新版本通常带来语法与标准库变化；3.10 已停止支持意味着库作者可以逐步放弃兼容并采用 3.11 起的特性。PEP（Python Enhancement Proposal）是 Python 社区提出和记录语言变更的机制，PEP 810、798、448 分别对应本次惰性导入、推导式解包和早期解包泛化。采样分析器通过周期性抓取调用栈估算函数耗时，与需要插桩的追踪分析器不同，适合低开销观察运行中的进程。

**「影响」** 对维护跨版本兼容库和 CLI 插件生态的开发者而言，Python 3.10 支持结束使 3.11 成为新的兼容下限，而 PEP 810 惰性导入可直接降低加载重型依赖插件带来的启动延迟。

**标签**: `#Python`, `#programming languages`, `#open source`, `#software engineering`, `#lazy imports`

---

<a id="item-tech-news-2"></a>
### [Meta 发布 Muse Wonder，社区质疑视觉基准表现](https://research.meta.ai/blog/muse-wonder) ⭐️ 8.0/10

Meta AI 研究博客发布文章介绍名为 Muse Wonder 的模型，相关讨论在 Hacker News 获得 282 分和 127 条评论。评论者把它与 Opus 5.5、Sonnet 或 Haiku，以及此前的 Muse Spark 1.2 和 Muse 1.3 进行对比，重点测试图像转 HTML 和 SVG 生成等视觉任务。jjcm 称 Muse Wonder 在图像转 HTML 上远不如 Opus 5.5，更接近 Sonnet 或 Haiku，并表示鉴于其公布的基准分数原本期待更高。simonw 用“鹈鹕”SVG 测试作比较，提到 Muse Spark 1.2 在 8 月、Muse 1.3 在 9 月的表现，并称 1.3 似乎偏好动画。另有评论者称登录 Meta 账号时在授权界面看到无关开发者的资料，担心资料和邮箱被暴露，并称无法访问账户设置；还有人指出定价页面位于 dev.meta.ai。

hackernews · meetpateltech · 10月12日 16:48 · [社区讨论](https://news.ycombinator.com/item?id=50059115)

**「背景」** Meta 此前已以 Muse 为名推出面向个人用户的 AI 智能体，官方将其定位为不只回答问题、还能主动承接任务与项目的助手，并配套提供开发者产品入口。在这一产品线中，Muse Wonder 是 Meta AI 研究博客新介绍的模型，而 Hacker News 上的讨论者把它与更早的 Muse Spark 1.2、Muse 1.3 以及 Opus 5.5、Sonnet、Haiku 等其他前沿模型放在同一维度上比较。这类横向对比通常围绕图像转 HTML、SVG 生成等视觉任务展开，因此对 Muse Wonder 的评价也集中在其公开基准分数与实测表现之间的落差上。

**「影响」** 对打算把 Muse Wonder 用于图像转 HTML、SVG 生成等视觉任务的开发者来说，社区实测显示其表现明显落后于 Opus 5.5、更接近 Sonnet 或 Haiku 一档，与官方公布的基准分数存在落差，因此不宜仅凭榜单数字选型。另有一位开发者报告，从 dev.meta.ai 登录其 Meta 账号时看到与自己无关的其他开发者资料，若情况属实，则意味着使用该平台可能带来个人资料与邮箱外泄的风险。

**「社区讨论」** 社区整体对 Muse Wonder 的前沿定位与公布基准持保留态度：图像转 HTML 被指不如 Opus 5.5，SVG 生成测试提供了与 Muse Spark 1.2、Muse 1.3 的可比样本，但尚无统一结论。评论还出现账号/隐私异常的实际体验担忧，以及更多公司接近前沿可避免权力过度集中的观点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/">Introducing Muse : The World’s First Personal AI Agent Built for Everyone</a></li>
<li><a href="http://muse.ai/">muse . ai</a></li>
<li><a href="https://www.meta.ai/">meta . ai</a></li>

</ul>
</details>

**标签**: `#AI models`, `#LLM`, `#Meta`, `#vision models`, `#benchmarks`

---