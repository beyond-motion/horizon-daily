---
layout: default
title: "Horizon Summary: 2026-08-24 (ZH)"
date: 2026-08-24
lang: zh
---

> 从 7 条内容中筛选出 4 条重要资讯。

---

**科技新闻**
1. [微软画图与照片应用暗藏 GUID 水印](#item-tech-news-1) ⭐️ 8.0/10
2. [IPFS 维护团队在 Shipyard 逐步收尾](#item-tech-news-2) ⭐️ 7.0/10
3. [你的可执行文件可以是一个 SQLite 数据库](#item-tech-news-3) ⭐️ 7.0/10
4. [Anthropic 最强模型遇冷，更便宜工具受青睐](#item-tech-news-4) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [微软画图与照片应用暗藏 GUID 水印](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

逆向工程发现，微软的 MS Paint 和 MS Photos 会在经过 AI 处理的图片中嵌入不可见的 GUID 水印，即使操作由本地模型完成、输出仅保存在本地也不例外。可见水印可以关闭，但隐形水印无法禁用，且会在后台静默添加，用户不会收到任何提示。目前尚不清楚该行为是否覆盖 AI 背景删除/移除等具体功能。由于 GUID 是唯一标识符，这一机制引发了对隐私、匿名性和法律追责的严重担忧。

hackernews · ComputerGuru · 8月24日 15:28 · [社区讨论](https://news.ycombinator.com/item?id=49421158)

**「背景」** 这项发现来自对微软画图（MS Paint）和照片（MS Photos）保存流程的逆向工程：当用户使用 AI 功能编辑或生成图像时，程序会根据 WatermarkSetting 决定是否叠加可见的 Copilot 标志，同时还会嵌入由服务器签发的 GUID 作为不可见水印，即使图像完全在本地生成也不例外。可见水印可以通过设置关闭，但不可见 GUID 水印无法禁用，并且会在后台静默添加，用户不会收到任何提示。此类水印通常用于追溯 AI 生成或编辑内容的来源，但也因此引发了对用户隐私和匿名性的担忧。

**「影响」** 任何使用 MS Paint 或 MS Photos 进行 AI 图像编辑的用户，都会在输出文件中获得一个无法关闭的隐形 GUID 标识，可能被用于关联到微软账户；该行为是否涵盖 AI 背景删除等操作仍不明确。

**「社区讨论」** 评论者认为 AI 水印话题本身是转移焦点，真正的问题是在用户不知情时嵌入唯一标识，可能让微软在收到版权传票时交出账户关联的个人信息。也有用户报告该水印被误触发并转而安装 Paint.net，并提到微软此前曾在 Azure DevOps 提交上错误添加 Copilot 水印的先例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/">Microsoft Paint and Photos Embed Server-Issued GUIDs as Invisible Watermarks in Locally-Generated Images :: Xusheng Li</a></li>

</ul>
</details>

**标签**: `#privacy`, `#watermarking`, `#Microsoft`, `#AI-generated content`, `#reverse engineering`

---

<a id="item-tech-news-2"></a>
### [IPFS 维护团队在 Shipyard 逐步收尾](https://ipshipyard.com/blog/2026-the-end-of-ipfs-at-shipyard/) ⭐️ 7.0/10

IPFS 维护方宣布在 Shipyard 逐步结束项目维护，引发关于去中心化网络基础设施未来的讨论。此前 Cloudflare 已停止对 IPFS 的支持，社区认为这一决定早有迹象。前维护者指出，有更可持续的 P2P 替代方案，如由前 Protocol Labs 开发者打造的 Iroh。评论还批评 IPNS 未能满足非静态 Web 应用需求，以及浏览器内可靠交付始终是痛点。目前官方未提供完整细节，具体时间表和后续维护安排尚不明确。

hackernews · iand · 8月24日 15:48 · [社区讨论](https://news.ycombinator.com/item?id=49421489)

**「背景」** IPFS（星际文件系统）是一种基于内容寻址的点对点协议，旨在为去中心化网络提供文件存储与分发能力。IPFS Shipyard 是 IPFS 社区用于托管实验性和孵化中项目的 GitHub 组织，其维护工作以尽力而为的方式进行，欢迎社区提交拉取请求。此次公告意味着 Shipyard 对 IPFS 的维护工作正在收尾，标志着这一去中心化基础设施项目进入新的阶段。

**「影响」** 对依赖 IPFS 生态的开发者与去中心化应用而言，维护力量收缩意味着基础设施支持、网关可用性和长期路线图的不确定性增加；社区提到的替代方案（如 Iroh）可能成为迁移方向，但迁移成本与兼容性仍需评估。

**「社区讨论」** 评论中既有前维护者的惋惜，也有对可持续性的质疑：有人推荐由前 Protocol Labs 开发者构建的 Iroh 作为更可持续的 P2P 选项，另一些人则认为 IPNS 方向失误、浏览器内可靠交付始终未解决，最终只能依赖 HTTP 网关，沦为“去中心化表演”。还有评论讽刺称，想向 Shipyard 反馈意见却要填写 Google 表单，与去中心化理念相悖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ipfs-shipyard">IPFS Shipyard · GitHub</a></li>

</ul>
</details>

**标签**: `#IPFS`, `#decentralized web`, `#open source`, `#p2p`, `#Protocol Labs`

---

<a id="item-tech-news-3"></a>
### [你的可执行文件可以是一个 SQLite 数据库](https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/) ⭐️ 7.0/10

Farid Zakaria 展示了一种 Linux 技巧：把 SQLite 数据库文件构造成可直接执行的可执行文件。方法是将文件格式中偏移 68 字节处的 4 字节 application ID 设为 SELF（Structured Executable &amp; Linkable Format），并把 ELF 可执行格式的各组成部分安排到多个 SQLite 表中（schema 见 selfdb 仓库）。配套的 self-exec 解释器（C 代码）会提取并执行所需部分；还可以通过 binfmt\_misc 注册，让内核在遇到匹配该二进制模式的文件时自动调用解释器。Farid 在 NixOS 上演示，非 NixOS 系统可通过向 /proc/sys/fs/binfmt\_misc/register 写入 &\#x27;:self:M:68:SELF::/usr/local/bin/self-exec:&\#x27; 完成注册。该技巧对系统程序员很有启发，但属于实验性 hack，而非主流行业变革。

rss · Simon Willison · 8月24日 11:38

**「背景」** SQLite 数据库文件在偏移 68 字节处有一个 4 字节的 application ID，通常用于标识文件类型；ELF 是 Linux 可执行文件的常见格式。binfmt\_misc 是 Linux 内核机制，允许通过自定义解释器识别并运行非标准二进制格式。

**「影响」** 对 Linux 系统程序员而言，这一模式提供了一种把数据库内容与可执行代码融合在同一文件中的新思路，可用于分发自带结构化数据的工具；但它依赖自定义解释器和 binfmt\_misc 注册，目前更接近实验性技巧而非通用标准。

**标签**: `#SQLite`, `#ELF`, `#Linux`, `#systems programming`, `#binfmt\_misc`

---

<a id="item-tech-news-4"></a>
### [Anthropic 最强模型遇冷，更便宜工具受青睐](https://simonwillison.net/2026/Aug/23/anthropics-best-ai-model-struggles-to-attract-users-as-cheaper-t/) ⭐️ 7.0/10

据英国《金融时报》援引知情人士数据，Anthropic 的 7 月年化收入已升至 650 亿美元，高于 5 月的 470 亿美元；该公司还告诉投资者，预计第三季度将按照此前宣布第二季度盈利的同一口径实现盈利，并拥有 6000 个年消费 10 万美元以上的客户。与此同时，OpenAI 的年化收入在当季迄今跃升 35%，目前已超过 400 亿美元，7 月发布的 GPT 5.6 扭转了年初的疲软表现。文章还引用了 Ramp AI 指数，该指数基于 7 万家使用 Ramp 信用卡公司的账单数据估算模型采用情况。2026 年 7 月 Anthropic 模型支出中，Opus 4.8 占 28.0%居首，Sonnet 4.6 占 8.3%，Fable 5 占 8.0%，而 7 月 24 日才发布的旗舰模型 Opus 5 仅占 3.5%，显示其成本可能限制了采用。

rss · Simon Willison · 8月23日 20:24

**「背景」** Anthropic 的 Claude 模型家族按规模与成本分为多个层级：Opus 面向复杂推理与编码任务，Sonnet 是均衡的中端模型，Haiku 主打低延迟轻量场景，而 2026 年新推出的 Fable 5 属于“Mythos 级”高端模型，能力更强但价格也更高。本文引用的 Ramp AI 指数基于 7 万家使用 Ramp 信用卡公司的账单数据估算模型采用率，因此能反映各模型在企业实际支出中的份额，而不仅是官方宣传或基准测试表现。

**「影响」** 对 Anthropic 而言，旗舰模型 Opus 5 因成本较高在 Ramp 企业账单数据中仅占 3.5%的模型支出，显示高价策略可能限制其采用，而 OpenAI 凭借 GPT 5.6 发布实现季度收入加速增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.usecarly.com/blog/claude-models-explained/">Claude Models Explained (2026): Opus vs Sonnet vs Haiku vs Fable</a></li>
<li><a href="https://datrick.com/claude-models-comparison">Claude Models Comparison 2026: Fable, Opus, Sonnet &amp; Haiku</a></li>
<li><a href="https://aiportalx.com/blog/claude-opus-4-8-vs-sonnet-5-vs-fable-5-anthropic-2026-lineup">Claude Opus 4.8 vs Sonnet 5 vs Fable 5: Anthropic&#x27;s 2026 ...</a></li>

</ul>
</details>

**标签**: `#AI industry`, `#Anthropic`, `#OpenAI`, `#business metrics`, `#model adoption`

---