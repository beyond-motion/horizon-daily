---
layout: default
title: "Horizon Summary: 2026-11-20 (ZH)"
date: 2026-11-20
lang: zh
---

> 从 8 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [PostgreSQL 19 发布：新增 WAIT FOR LSN 备库一致性](#item-tech-news-1) ⭐️ 9.0/10
2. [Levent Alpöge 宣称证明广义黎曼猜想，尚待验证](#item-tech-news-2) ⭐️ 8.0/10
3. [Architect Labs 的 AI 设计 CPU 架构引发争论](#item-tech-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [PostgreSQL 19 发布：新增 WAIT FOR LSN 备库一致性](https://simonwillison.net/2026/Nov/19/postgresql-19/) ⭐️ 9.0/10

PostgreSQL 19 已正式发布，发布时间比通常的 9 月晚约两个月；作者称主要原因是团队需要集中处理大量由 AI 报告的安全漏洞问题。此次发布中最受关注的新功能是 WAIT FOR LSN：当应用把读请求发送到备库时，会话可以先等待备库把预写日志（WAL）重放到指定的日志序列号（LSN），再执行查询，从而实现“读己之写”一致性。典型用法是在主库执行写入后，用 pg\_current\_wal\_insert\_lsn\(\) 取得 LSN（例如 0/0306EE20），将其保存下来，并在后续请求中于备库执行 WAIT FOR LSN &\#x27;0/0306EE20&\#x27; WITH \(TIMEOUT &\#x27;0.1s&\#x27;\)；其中超时参数可选，若超时后备库仍未追上，就会返回错误。作者指出，这一模式在 Wikipedia/MediaWiki 基于 MySQL 复制的手写实现中已有先例。

rss · Simon Willison · 11月19日 20:43

**「背景」** PostgreSQL 是广泛使用的开源关系型数据库；它的流复制会把主库产生的预写日志（WAL）发送到备库并由备库重放，因此把读请求发给备库时，可能读到落后于主库的数据。所谓“read-your-writes”一致性，是指应用刚在主库完成写入后，后续从备库读取时也应能看到这次写入。PostgreSQL 19 的 WAIT FOR LSN 让备库会话先等待 WAL 重放到指定日志序列号（LSN），再执行查询，从而把这种一致性保障做成数据库内建能力。

**「影响」** 对于将读请求分流到备库的应用，WAIT FOR LSN 把读己之写一致性交给数据库原生处理，可减少自行轮询复制位点或重试的代码；代价是应用需在请求间保存并传递 LSN，且设置超时后若备库未及时追上会直接报错。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.postgresql.org/about/news/postgresql-19-released-3449/">PostgreSQL : PostgreSQL 19 Released !</a></li>
<li><a href="https://dev.to/franckpachot/read-your-writes-on-replicas-postgresql-wait-for-lsn-and-mongodb-causal-consistency-4he2">Read ‑ your ‑ writes on replicas: PostgreSQL WAIT FOR LSN and...</a></li>

</ul>
</details>

**标签**: `#PostgreSQL`, `#databases`, `#open source`, `#replication`, `#WAIT FOR LSN`

---

<a id="item-tech-news-2"></a>
### [Levent Alpöge 宣称证明广义黎曼猜想，尚待验证](https://alpo.ge/remark.pdf) ⭐️ 8.0/10

Levent Alpöge 在个人网站发布 PDF，声称证明了广义黎曼猜想；目前该声明尚未经过同行评审或形式化验证，Hacker News 讨论将其视为高风险、待核实的数学声明。讨论的核心之一是其 Lean 形式化规模：有评论者称归档约 1.3GB、约 1500 万行代码，需分 14 个分片下载后合并解压。另一焦点是 AI 辅助数学：有评论者强调 Alpöge 的资历及其引导 AI 发现数学结果的能力，也有人引用 Terence Tao 此前的怀疑，认为当前 AI 尚不足以单独攻克黎曼猜想。还有评论者指出另有一份据称完全由人类完成的证明，并批评相关标题仅以“Anthropic 员工”指代 Alpöge，可能误导读者并淡化其数学家身份。

hackernews · iamronaldo · 11月20日 14:16 · [社区讨论](https://news.ycombinator.com/item?id=50574968)

**「背景」** 黎曼猜想断言黎曼ζ函数的所有非平凡零点都位于临界线 Re\(s\)=1/2 上；广义黎曼猜想则把这一断言推广到狄利克雷 L 函数等更广泛的 L 函数。Lean 是交互式定理证明助手，可用于把数学证明形式化并逐步进行机器检验。2026 年 11 月 20 日，Levent Alpöge 在个人网站发布 PDF 和据称用于检验各步骤的 Lean 代码，宣称他与 Claude 找到了黎曼猜想及广义形式的证明，但该声明当时仍属未经核实的个人发布。

**「影响」** 对 Lean 形式化社区和数论研究者而言，最直接的后果是必须独立构建并审查这份约 1.3GB、1500 万行的归档；在验证完成前，它只能被视为待核实的声明，而不能作为证明依据。

**「社区讨论」** 讨论中，有评论者高度评价 Alpöge 的资历，认为他若宣称证明就值得认真对待；但也有人引用 Terence Tao 近期对 AI 攻克黎曼猜想的怀疑，形成“人类与 AI 可能突破”与“当前 AI 仍不够”的对照。另有评论者指出存在一份据称完全由人类完成的证明，并抱怨标题以“Anthropic 员工”指代 Alpöge 会误导读者、把功劳归于公司。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://explainx.ai/blog/levent-alpoge-anthropic-riemann-hypothesis-claude-lean-proof-claimed-vs-verified-2026">Riemann Hypothesis Proof Claim: Claimed vs Verified ...</a></li>
<li><a href="https://www.unite.ai/levent-alpoges-unverified-riemann-claim-puts-claudes-lean-code-in-focus/">Levent Alpöge’s Unverified Riemann Claim Puts Claude’s Lean ...</a></li>

</ul>
</details>

**标签**: `#Generalized Riemann Hypothesis`, `#Lean formalization`, `#AI-assisted mathematics`, `#proof verification`, `#Hacker News`

---

<a id="item-tech-news-3"></a>
### [Architect Labs 的 AI 设计 CPU 架构引发争论](https://architectlabs.com/blog/frostbite) ⭐️ 7.0/10

Architect Labs 在博客中宣称，Frostbite 是一种由 AI 设计并验证、基于 interaction nets 的 CPU 架构，相关帖子在 Hacker News 引发技术讨论。发帖者强调 interaction nets 是与 1940 年代 Harvard 架构不同的基础范式，但承认该实现能否真正支持它、能否达到宣称性能仍不确定。讨论中的主要质疑包括：证据仅为公司博客、“AI 发现”标题夸大了 AI 的作用，以及基准使用顺序执行 CPU 而非现代乱序设计、测试程序数量偏少。还有评论指出，数据流架构 WaveScalar 在 20 多年前已探索类似方向，CGRA/数据流处理器也与部分 AI 推理加速器相似。目前可核验的材料主要是公司博客与社区评论，尚缺独立评测。

hackernews · shioyama · 11月20日 10:01 · [社区讨论](https://news.ycombinator.com/item?id=50572503)

**「背景」** Frostbite 是 Architect Labs 公布的实验性通用处理器架构，声称从零开始由人工智能设计。它围绕交互网络（interaction nets）构建：官方将其特性概括为每一步计算都是局部的、每个依赖都显式表达、每个值恰好只有一个所有者，并希望借此获得阶跃式的 CPU 性能提升。交互网络是一类基于图重写的计算模型，与主流指令流 CPU 的执行假设不同，因此理解 Frostbite 需要把“AI 设计”与“交互网络架构是否可行、性能是否成立”分开看。

**「影响」** 在获得独立复现、与乱序 CPU 的对比以及更大程序集上的验证之前，Frostbite 的性能与实用性主张仍难以评估。

**「社区讨论」** 评论区对“AI 发现架构”的叙事分歧明显。发帖者 shioyama 希望大家先关注 interaction nets 这一不同范式，并承认实现与性能仍待验证；jkhdigital 认为核心洞见来自人类、AI 的贡献在于把研究文献工程化，pizza234 质疑顺序执行基线、测试规模和相对 WaveScalar 的新颖性，metalsiliconYT 则将其类比为 CGRA/数据流处理器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://architectlabs.com/blog/frostbite">Introducing Frostbite : A new CPU architecture ... | Architect Labs</a></li>
<li><a href="https://runet.news/news/90299">Стартап Architect Labs представил процессорную... — Runet</a></li>

</ul>
</details>

**标签**: `#CPU architecture`, `#AI-assisted design`, `#interaction nets`, `#hardware verification`

---