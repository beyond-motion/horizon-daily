---
layout: default
title: "Horizon Summary: 2026-10-02 (ZH)"
date: 2026-10-02
lang: zh
---

> 从 2 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [法院支持 EFF：犹他州 VPN 法要求技术上不可行](#item-tech-news-1) ⭐️ 7.0/10
2. [arXiv 将每月提交上限设为两篇](#item-tech-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [法院支持 EFF：犹他州 VPN 法要求技术上不可行](https://www.eff.org/deeplinks/2026/10/court-agrees-eff-utahs-vpn-law-demands-technical-impossibility) ⭐️ 7.0/10

在一起围绕犹他州 VPN 法律的案件中，法院支持了电子前哨基金会（EFF）的立场，认定该法律对平台提出了技术上无法实现的要求。按照 EFF 的说法，这部法律让平台陷入两难：要么在全国范围内彻底阻断所有 VPN 流量，要么完全退出犹他州。EFF 借此重申互联网流量总会绕过审查，而相关讨论则集中在 VPN 能否被可靠识别、州级管辖权的边界以及审查范围可能扩大的风险上。该裁决的具体判词细节、生效时间与后续法律程序在现有信息中尚不明确。

hackernews · hn\_acker · 10月1日 22:23 · [社区讨论](https://news.ycombinator.com/item?id=49927754)

**「背景」** 犹他州通过的一项法律要求商业实体实施“商业上合理的地理位置混淆检测系统”，并禁止网站提供使用 VPN 绕过这些检查的说明；EFF 主张这一检测要求构成技术上的不可能。随后，一名联邦法官发布初步禁令，暂停执行该法的 VPN 条款，认定其很可能违反美国宪法中禁止显著加重犹他州以外企业和个人负担的规定。该禁令是初步性的，相关法律争议仍在继续。

**「影响」** 若该裁决成立，平台将无需再为满足犹他州法律而尝试识别并阻断 VPN 流量，但犹他州用户能否继续访问相关服务，仍取决于后续法律程序与平台自身的应对方式。

**「社区讨论」** 评论者普遍质疑 VPN 能否被可靠识别，SoftTalker 指出任何人都可以通过随机的托管服务商进行代理；usernomdeguerre 则追问“互联网总会绕过审查”在伊朗、中国以及克什米尔等案例之后是否仍然成立。另有评论者 stefangordon 主张州政府对境外服务器上的行为本就没有管辖权，kramer2718 则认为这场胜利只是其中一役，并称政府追求这类控制权的原因并不只是色情内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eff.org/deeplinks/2026/10/court-agrees-eff-utahs-vpn-law-demands-technical-impossibility">Court Agrees with EFF: Utah’s VPN Law Demands a Technical ...</a></li>
<li><a href="https://briefly.co/anchor/Privacy_technologies/story/court-agrees-with-eff-utahs-vpn-law-demands-a-technical-impossibility">Court Agrees with EFF: Utah&#x27;s VPN Law Demands a Technical ...</a></li>
<li><a href="https://beforeitsnews.com/libertarian/2026/10/court-agrees-with-eff-utahs-vpn-law-demands-a-technical-impossibility-2854165.html">Court Agrees with EFF: Utah’s VPN Law Demands a Technical ...</a></li>

</ul>
</details>

**标签**: `#VPN`, `#internet policy`, `#privacy`, `#censorship`, `#EFF`

---

<a id="item-tech-news-2"></a>
### [arXiv 将每月提交上限设为两篇](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/) ⭐️ 7.0/10

arXiv 宣布将每位提交者每个日历月的投稿数量限制为最多两篇。该政策直接影响 AI/ML 等领域研究人员通过预印本快速传播成果的方式，因为 arXiv 是这些领域最常用的预印本平台之一。目前公开内容未提供更多执行细节，例如是否适用于更新已有论文版本、是否有例外或如何计算合著者提交。社区讨论普遍认为此举有助于抑制论文工厂和低质量投稿，但也担心大型实验室可能通过轮换作者来规避限制。

reddit · r/MachineLearning · Nunki08 · 10月2日 00:47 · [社区讨论](https://www.reddit.com/r/MachineLearning/comments/1wvg7yc/arxiv_now_limits_submitters_to_up_to_two/)

**「背景」** arXiv 是物理、数学、计算机科学等领域最常用的预印本平台，论文在正式同行评审前即公开，内容审核长期依赖志愿者版主。近年来生成式 AI 带来了大量低质量甚至由机器批量生成的投稿，维护方表示此举是为了公平分配版主的审核时间，并保护语料库免受不当投稿激增的冲击。此前 arXiv 并未对个人作者设置此类月度投稿硬性配额，新规正是针对这一背景出台的。

**「影响」** 该政策直接约束了所有 arXiv 投稿者的发布节奏：每人每个日历月最多提交两次，且同时最多只能有三个活跃提交，arXiv 表示此举是为把志愿审稿人的时间更公平地分摊给作者。不过社区讨论普遍质疑，拥有大量人力的实验室可能通过轮换署名作者来绕过这一限制，而更新已有论文版本是否计入配额也尚不明确。

**「社区讨论」** 评论总体支持该限制，认为它能减少论文工厂和低质量投稿，并改善 arXiv 阅读体验；也有人担心大型实验室会按人头轮换提交来规避。多位评论者还追问更新已有论文版本是否计入限额，并建议期刊（如已实行年度作者提交配额的 TMLR）采取类似配额。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/">arXiv has updated its rate limit policy for all submitters.</a></li>
<li><a href="https://startupfortune.com/arxiv-now-limits-every-researcher-to-two-paper-submissions-a-month/">arXiv now limits every researcher to two paper submissions a ...</a></li>
<li><a href="https://www.theregister.com/ai-and-ml/2026/10/02/arxiv-imposes-rate-limit-on-paper-submissions-to-stem-the-ai-slop-tide/5300899">ArXiv imposes rate limit on paper submissions to stem the AI ...</a></li>
<li><a href="https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/">arXiv has updated its rate limit policy for all submitters.</a></li>

</ul>
</details>

**标签**: `#arXiv`, `#research publishing`, `#rate limiting`, `#AI/ML community`, `#paper mills`

---