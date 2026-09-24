---
layout: default
title: "Horizon Summary: 2026-09-24 (ZH)"
date: 2026-09-24
lang: zh
---

> 从 1 条内容中筛选出 1 条重要资讯。

---

**科技新闻**
1. [F-Droid 2.0 发布：界面重构与 FPE 淘汰](#item-tech-news-1) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [F-Droid 2.0 发布：界面重构与 FPE 淘汰](https://f-droid.org/2026/09/24/f-droid-2.0-a-new-chapter-for-android-freedom.html) ⭐️ 8.0/10

F-Droid 项目发布了 2.0 版本，这是这一开源 Android 应用仓库的一次重大改版，核心变化包括重新设计的用户界面以及逐步淘汰 F-Droid Privileged Extension（FPE）。FPE 原本用于减少手动确认安装与自动更新时的交互，但长期被用户抱怨配置繁琐、容易出问题。作为注重软件自由与隐私的第三方应用分发渠道，F-Droid 的这次改版对使用 GrapheneOS、LineageOS 等自定义系统的用户尤为重要。社区讨论同时把焦点放在更长远的问题上：有评论追问，一旦 Google 明年推行平台收紧措施，F-Droid 这类第三方商店的前景会如何。需要注意的是，目前可获取的材料仅为公告本身与社区评论，除界面重构和 FPE 淘汰外，公告未披露更多技术细节。

hackernews · daveoc64 · 9月24日 15:26 · [社区讨论](https://news.ycombinator.com/item?id=49831968)

**「背景」** F-Droid 是面向 Android 的自由开源软件（FOSS）应用仓库及配套官方客户端，用户借此安装和更新开源应用。F-Droid Privileged Extension（FPE）是让 F-Droid 获得系统特权、从而静默完成应用安装与更新的扩展组件，但其配置历来麻烦；F-Droid 2.0 不再支持 FPE，即便已安装也不会调用，改为全面支持 Android 的“session”安装器机制。此次 2.0 还是一次完整的客户端重设计，采用三标签界面并支持由 DMA 驱动的后台自动更新，同时停止对 Android 6 设备的支持。

**「影响」** 对现有 F-Droid 用户和依赖替代分发的开发者而言，2.0 的界面重做与 FPE 淘汰直接降低了此前需改用 droid-ify 等第三方客户端、并费力配置 Privileged Extension 的使用门槛。更关键的长期后果来自 Google：自 2026 年 9 月起，巴西、印度尼西亚、新加坡和泰国认证设备上安装的应用须绑定已验证开发者，并计划于 2027 年及以后推向全球，这可能实质性压缩 F-Droid 赖以生存的侧载与替代分发空间，具体执行细节与最终适用范围仍有不确定性。

**「社区讨论」** 评论整体欢迎这次大改版，一位在 GrapheneOS 上使用 Droid-ify 多年的用户表示，自己正是因为 F-Droid 界面糟糕、特权扩展难以配置才转用第三方客户端，并对 FPE 被淘汰感到高兴。与此同时也有质疑与具体诉求：有人指出官方首张截图里 “Syncthing-For k” 出现异常断行，质疑改版展示的完成度；有人追问 Google 明年平台收紧后 F-Droid 的未来；还有用户希望能有更易用的 F/OSS 电子书阅读器，以及一个可在电脑上通过 adb 管理设备端应用的 F-Droid 命令行客户端。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://f-droid.org/2026/09/24/f-droid-2.0-a-new-chapter-for-android-freedom.html">F-Droid 2.0: A New Chapter for Android Freedom | F-Droid - Free and Open Source Android App Repository</a></li>
<li><a href="https://www.androidtablets.ca/f-droid-2-0-launches-with-ui-overhaul-and-automatic-updates/">F-Droid 2.0 launches with UI overhaul and automatic updates – Android Tablets</a></li>
<li><a href="https://daily.dev/posts/f-droid-2-0-a-new-chapter-for-android-freedom-sg3qpi8yd">F-Droid 2.0: A new chapter for Android freedom | daily.dev</a></li>
<li><a href="https://f-droid.org/en/2026/02/24/open-letter-opposing-developer-verification.html">An Open Letter Opposing Android Developer Verification | F-Droid - Free and Open Source Android App Repository</a></li>
<li><a href="https://startupfortune.com/android-developers-revolt-against-googles-2026-sideloading-registration-mandate/">Android developers revolt against Google&#x27;s 2026 sideloading registration mandate - Startup Fortune</a></li>
<li><a href="https://groundy.com/articles/keep-android-open-f-droid-s-fight-against-locked-down/">Keep Android Open: F-Droid&#x27;s Fight Against a Locked-Down Mobile Future · Groundy</a></li>

</ul>
</details>

**标签**: `#F-Droid`, `#Android`, `#open source`, `#app distribution`, `#mobile privacy`

---