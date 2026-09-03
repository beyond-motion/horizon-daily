---
layout: default
title: "Horizon Summary: 2026-09-03 (ZH)"
date: 2026-09-03
lang: zh
---

> 从 4 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [Audacity 4.0 发布：基于 Qt6 的开源音频编辑器重大更新](#item-tech-news-1) ⭐️ 8.0/10
2. [第三级 .name 域名终止提案引发争议](#item-tech-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Audacity 4.0 发布：基于 Qt6 的开源音频编辑器重大更新](https://github.com/audacity/audacity/releases/tag/Audacity-4.0.0) ⭐️ 8.0/10

Audacity 4.0.0 已作为开源音频编辑器的主要版本发布，其最大变化是采用 Qt6 重写用户界面。此次发布受到广泛关注，既因为这是这款常用桌面软件的重要技术转向，也因为它重新引发了关于项目方向与早期遥测争议的讨论。新版在 GitHub 上以 Audacity-4.0.0 标签提供；社区中有人称赞界面更干净，也有人指出 Linux 下 JACK/Pipewire 的集成方式仍未改变。具体性能数据和完整兼容性限制需以官方发布说明为准。

hackernews · ClydeN · 9月3日 10:53 · [社区讨论](https://news.ycombinator.com/item?id=49548395)

**「背景」** Audacity 是一款历史悠久的开源音频编辑器，此前版本长期基于 wxWidgets 图形界面库。Muse Group 在 2021 年收购该项目后曾加入遥测功能，引发社区担忧并催生了 Tenacity、Sneedacity 等分支。Audacity 4.0 将界面重写为 Qt6，并复用了 MuseScore Studio 4 的框架，同时引入 Windows ASIO 支持和旧版项目导入能力。

**「影响」** 对依赖 JACK/Pipewire 的 Linux 家庭录音室用户来说，4.0 的更新日志没有解决他们长期抱怨的临时 JACK 客户端问题，因此升级后核心工作流可能不会有明显改善。

**「社区讨论」** 评论中有人推荐 Muse 软件主管的开发讲解视频，并认为 4.0 的界面更干净、修复了不少问题。另一些用户则持保留态度，抱怨 JACK/Pipewire 集成方式未变，并继续追问 Tenacity、Sneedacity 等分叉项目以及 audio.com 相关功能的走向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linuxcompatible.org/story/audacity-40-beta-4-ships-with-qt6-ui-windows-asio-and-legacy-imports">Audacity 4.0 Beta 4 Ships With Qt6 UI, Windows ASIO, and Legacy Imports</a></li>
<li><a href="https://www.warp2search.net/story/audacity-40-beta-4-ships-with-qt6-ui-windows-asio-and-legacy-imports">Audacity 4.0 Beta 4 Ships With Qt6 UI, Windows ASIO, and Legacy Imports</a></li>
<li><a href="https://www.phoronix.com/news/Audacity-4.0-Released">Audacity 4.0 Audio Editor Released With Qt6 Based UI - Phoronix</a></li>

</ul>
</details>

**标签**: `#audacity`, `#open-source`, `#audio-editing`, `#qt6`, `#release`

---

<a id="item-tech-news-2"></a>
### [第三级 .name 域名终止提案引发争议](https://neil.fraser.name/news/2026/09/03/) ⭐️ 7.0/10

一项提案拟终止第三级 .name 域名（形如 x.y.name）的注册，并释放对应的 y.name 二级域；现有第三级注册将被终止，但 .name 顶级域本身和第二级 .name 域名不受影响。该政策若实施，将影响大量现有持有者，并引发关于域名抢注、DNS 安全和互联网治理的争议。评论中的一种主流意见认为，应当停止新注册但继续兑现现有注册，同时保留相关二级域以避免抢注。目前提案细节尚不完整，是否会为现有注册设置过渡期或保留二级域也未明确。

hackernews · pavel\_lishin · 9月3日 14:54 · [社区讨论](https://news.ycombinator.com/item?id=49550772)

**「背景」** .name 是 ICANN 于 2000 年首轮批准的一个通用顶级域（gTLD），由 Verisign 运营。该域名体系允许注册形如 x.y.name 的第三级域名，并曾提供对应的个性化电子邮件转发服务。2026 年 5 月，Verisign 提出停止销售第三级域名及相关邮件服务；2026 年 7 月 28 日，ICANN 批准了这一请求，Verisign 将单方面终止现有第三级注册，使相应的第二级域名（y.name）重新开放注册。

**「影响」** 现有第三级 .name 域名持有者将直接失去其注册的域名，而拥有第二级 .name 域名的用户不受影响；若提案通过，被释放的二级域可能面临抢注风险。

**「社区讨论」** 评论普遍认为终止现有注册的做法不合理，建议停止新注册但继续兑现现有注册，并继续保留相关二级域；也有讨论指出 .name 的二级结构本身存在 cookie 与安全风险，并有人借此呼吁采用去中心化的域名解析方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/.name">.name - Wikipedia</a></li>
<li><a href="https://domainincite.com/31699-verisign-to-delete-name-3lds-and-email-addresses">Verisign to delete .name 3LDs and email addresses - Domain Incite</a></li>

</ul>
</details>

**标签**: `#domain names`, `#DNS`, `#ICANN`, `#web infrastructure`, `#internet policy`

---