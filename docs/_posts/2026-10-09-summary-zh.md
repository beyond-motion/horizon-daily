---
layout: default
title: "Horizon Summary: 2026-10-09 (ZH)"
date: 2026-10-09
lang: zh
---

> 从 10 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [Cloudflare 收购 Deno，社区关注其运行时未来](#item-tech-news-1) ⭐️ 8.0/10
2. [Oxide Computer 宣布 4.45 亿美元 D 轮融资](#item-tech-news-2) ⭐️ 7.0/10
3. [Matthew Green 警告 AI 意外或远超公钥加密标准更替速度](#item-tech-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Cloudflare 收购 Deno，社区关注其运行时未来](https://deno.com/blog/cloudflare) ⭐️ 8.0/10

Cloudflare 已收购由 Node.js 创始人 Ryan Dahl 创建的 JavaScript/TypeScript 运行时 Deno。据社区评论引用的一篇博客文章，Cloudflare 将在未来一年内继续支持 Deno 运行时，每月发布包含缺陷修复和安全更新的版本，此后将结束对 Deno 运行时的开发；Deno 仍将保持开源，并欢迎其他人继续开发。这一收购是近期开发者工具领域一系列整合与收购事件中的最新一例，社区评论还列举了 Cursor、Astral/uv、Stainless、Bun、Astro.js、VoidZero、NuxtLabs 等案例。由于缺乏官方源内容，上述关于开发终止的表述来自社区引述，具体条款和后续安排仍待确认。

hackernews · ilreb · 10月9日 13:03 · [社区讨论](https://news.ycombinator.com/item?id=50019911)

**「背景」** Deno 是由 Node.js 创始人 Ryan Dahl 与 Bert Belder 共同创建的 JavaScript/TypeScript 运行时，它将运行时和包管理器集成在单个可执行文件中，旨在作为 Node.js 的替代方案。Deno 团队后来推出 Deno Deploy 和 celld（一种分布式 Durable Objects 实现），而 Cloudflare 的 Workers 平台依赖其 workerd 运行时。此次收购后，Deno 团队（包括 Ryan Dahl 和 Bert Belder）将主导把 celld 的分布式 Durable Objects 实现合并进 workerd，使 Workers 支持自托管部署中的对象放置、路由和多机持久存储。

**「影响」** 对于使用 Deno Deploy 的开发者，最直接的后果是该服务将在六个月内关停，付费客户将获得迁移到 Cloudflare Workers 的支持，而 Deno 运行时本身仍保持开源并可由社区继续开发。

**「社区讨论」** 多位评论者对 Deno 被收购感到惋惜，认为这实际上是一次“acquihire”并可能导致 Deno 运行时开发停止，同时担忧 npm 兼容性引入的臃肿和风险投资压力改变了其最初愿景。也有评论指出 Deno 仍将开源、欢迎他人接手，并将其置于近期开发者工具整合浪潮中看待。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Deno_%28software%29">Deno (software) - Wikipedia</a></li>
<li><a href="https://www.brocker.org/deno-joins-cloudflare-self-hosted-workers">Deno joins Cloudflare to simplify self-hosted Workers</a></li>
<li><a href="https://deno.com/blog/cloudflare">Deno is joining Cloudflare | Deno</a></li>
<li><a href="https://deno.com/blog/cloudflare">Deno is joining Cloudflare | Deno</a></li>

</ul>
</details>

**标签**: `#JavaScript runtime`, `#acquisitions`, `#Cloudflare`, `#Deno`, `#developer tooling consolidation`

---

<a id="item-tech-news-2"></a>
### [Oxide Computer 宣布 4.45 亿美元 D 轮融资](https://oxide.computer/blog/our-445m-series-d) ⭐️ 7.0/10

Oxide Computer 宣布完成 4.45 亿美元 D 轮融资，这一消息在 Hacker News 上引发大量讨论。该轮融资被视为这家系统/硬件与本地云基础设施公司的重要进展，但公告本身属于企业融资消息，而非技术深度发布。当前材料未提供公告原文，因此融资用途、估值、投资方及具体条件等细节均未披露。社区讨论主要围绕 Oxide 的公司定位、融资策略和基础设施市场展开。

hackernews · ahlCVA · 10月9日 13:12 · [社区讨论](https://news.ycombinator.com/item?id=50020014)

**「背景」** Oxide Computer 是一家提供本地部署云（on-prem cloud）的公司，主打将硬件与软件整合为机架级系统；该公司在 2023 年发布了其称为全球首款商用 Cloud Computer 的产品。其产品定位为“你拥有的云”，即软硬件一体化、用于规模化基础设施。据披露，这轮 4.45 亿美元 D 轮融资由 Eclipse 领投，现有投资者参投，并用于在交付前采购组件、扩大制造和机架级计算机交付。

**「影响」** 对计划采购本地云基础设施的企业客户而言，这笔资金将主要用于零部件采购、制造产能扩张以及现有和未来订单的交付，意味着 Oxide 的订单履约能力有望得到直接支撑。该轮由 Eclipse 领投，现有投资方参与，表明机构资本继续押注企业自有数据中心承载超大规模式云能力的路线。

**「社区讨论」** 评论总体正面：有用户称 Oxide 是“最鼓舞人心的公司之一”，并称赞其沟通风格与融资公告的思考深度；也有人质疑为何不走债务或贸易融资路线，担心引入更多股东本身也是风险。另有评论以将 Firestore 应用迁移到 SQLite 的经历，讨论代理式编程正在削弱对 AWS 和 Google Cloud 的锁定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.yahoo.com/technology/articles/oxide-raises-445m-series-d-130000230.html?fr=sycsrp_catchall">Oxide Raises $445M Series D as the Company Proves Vision of ...</a></li>
<li><a href="https://runtimewire.com/article/oxide-computer-445m-series-d-backlog-working-capital">Oxide Computer raises $445M to buy hardware before delivery</a></li>
<li><a href="https://oxide.computer/">Oxide Computer Company</a></li>
<li><a href="https://www.hpcwire.com/off-the-wire/oxide-introduces-innovative-cloud-computer-bridging-the-gap-between-hardware-and-software-for-on-prem-solutions/">HPCwire - Since 1987 – Covering the Fastest Computers in the ...</a></li>
<li><a href="https://finance.yahoo.com/technology/articles/oxide-raises-445m-series-d-130000230.html?fr=sycsrp_catchall">Oxide Raises $445M Series D as the Company Proves Vision of ...</a></li>
<li><a href="https://www.citybiz.co/article/917002/oxide-raises-445-million-series-d-to-expand-on-premises-cloud-infrastructure-manufacturing/">Oxide Raises $445 Million Series D to Expand On-Premises ...</a></li>

</ul>
</details>

**标签**: `#hardware`, `#data center infrastructure`, `#venture capital`, `#systems software`, `#on-prem cloud`

---

<a id="item-tech-news-3"></a>
### [Matthew Green 警告 AI 意外或远超公钥加密标准更替速度](https://simonwillison.net/2026/Oct/9/matthew-green/) ⭐️ 7.0/10

密码学家 Matthew Green 在 Twitter 上提出一个被其自称为“最坏情况”的警告：他认为我们生活在 Minicrypt（公钥加密不可能实现的假想世界）的概率约为 1%，而“在功能上对现有公钥加密算法失去信心”的概率约为 15%。Simon Willison 引用该推文并补充说明，Minicrypt 是 Russell Impagliazzo 提出的假想世界，在其中公钥加密无法实现。Green 强调的核心问题是速度差：AI 产生意外发现的速度，与人类更换标准的速度（即便有最好的 AI 辅助）相差数个数量级。他因此主张必须提前做好准备，因为只有事先准备才能在遭遇这类意外后恢复过来。

rss · Simon Willison · 10月9日 15:02

**「背景：Minicrypt 与公钥加密信心」** Minicrypt 是密码学家 Russell Impagliazzo 提出的假想世界：在其中单向函数存在，但公钥加密在数学上不可能实现。Matthew Green 是知名密码学家，他所说的“失去对公钥加密的信心”并不指加密本身变得不可能或我们身处 Minicrypt，而是指很快会出现显著改进对标准化方案攻击的新密码分析结果——原本被视为具有 128 位安全性的方案，实际可能只提供 96 或 108 位安全性。这一担忧的现实背景是，互联网与数字资产广泛依赖 RSA、椭圆曲线等公钥加密标准来保护通信和钱包安全。

**「影响」** 对依赖 RSA、ECC 等现有公钥加密的组织而言，这一警告意味着迁移与应急准备需要提前完成：一旦这些算法失去信任，标准替换的周期将远长于 AI 制造意外的时间，而仓促引入抗量子算法还可能带来旧硬件与既有系统的兼容问题。需要说明的是，1% 与 15% 的概率是 Green 个人的推测性判断，并非已证实的算法破解或研究成果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tech.yahoo.com/cybersecurity/articles/top-cryptographer-warns-ai-could-115747099.html">Top Cryptographer Warns AI Could Break the Math Behind Crypto ...</a></li>
<li><a href="https://agihunt.info/en/p/1a11d1439a5beb7ab92ded8df30">Cryptographer Matthew Green: losing public-key… · AGI Hunt</a></li>
<li><a href="https://x.com/matthew_d_green/status/2108282817343824147">Matthew Green on X: &quot;So what does “losing public-key ...</a></li>
<li><a href="https://www.nist.gov/cryptography">What is cryptography ? Cryptography uses mathematical techniques...</a></li>
<li><a href="https://www.researchgate.net/publication/388882504_Quantum_Computing_and_Cryptography_Preparing_for_the_Post-Quantum_Era">(PDF) Quantum Computing and Cryptography : Preparing for the...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#AI risk`, `#public-key encryption`, `#standards`, `#security`

---