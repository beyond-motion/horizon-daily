---
layout: default
title: "Horizon Summary: 2026-09-11 (ZH)"
date: 2026-09-11
lang: zh
---

> 从 7 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [trynix.dev：在浏览器中运行任意 Nix 包](#item-tech-news-1) ⭐️ 7.0/10
2. [Shopify 移动应用从 React Native 回归原生 Swift 与 Kotlin](#item-tech-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [trynix.dev：在浏览器中运行任意 Nix 包](https://simonwillison.net/2026/Sep/10/trynix/) ⭐️ 7.0/10

Farid Zakaria 发布了他称为 Nix 工作中“magnum opus”的 trynix.dev，它通过 WebAssembly 在浏览器内运行一个由 qemu-wasm 驱动的 x86\_64 Linux 虚拟机，并可启动任意 Nix 包，涵盖过去 13 年的版本。这些环境可通过 URL 寻址，例如访问 https://trynix.dev/?pkg=python3%403.6.2 并点击“Load”，就能获得一个运行 2017 年 Python 3.6.2 的交互式 shell。Zakaria 还在其上构建了 trynix-preview——一个 GitHub Action，会在拉取请求下评论一个链接，让审查者直接在浏览器中启动该 PR 的构建，无需服务器。Simon Willison 在短评中重点介绍了该工具，指出其潜在工作流包括通过启动 PR 来审查代码。

rss · Simon Willison · 9月10日 23:44

**「背景」** Nix 是一个声明式包管理器与构建系统，其软件包集合 nixpkgs 已积累约 13 年的历史版本，因此具体软件包可以按版本精确定位。qemu-wasm 将 QEMU 模拟器编译为 WebAssembly，使 x86\_64 Linux 虚拟机能够直接在浏览器标签页中启动，无需任何服务器端支持。trynix.dev 把这一机制与 nixpkgs-multiverse 索引结合，让用户不必在本地安装 Nix 就能启动 nixpkgs 历史上发布过的任意包。

**「影响」** 对于需要验证拉取请求或复现旧版软件环境的开发者而言，这一工具把环境启动的成本降到只需一个浏览器链接，不再依赖服务器或本地 Nix 安装；不过它也受限于 WebAssembly 环境下的性能与浏览器能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Sep/10/trynix/">Any Nix package, live in your browser</a></li>
<li><a href="https://fzakaria.com/2026/09/04/any-nix-package-live-in-your-browser">Any Nix package, live in your browser | Farid Zakaria’s Blog</a></li>
<li><a href="https://trynix.dev/">trynix — boot anything nixpkgs ever shipped, in your browser</a></li>

</ul>
</details>

**标签**: `#Nix`, `#WebAssembly`, `#qemu-wasm`, `#Browser-based VMs`, `#Reproducible environments`

---

<a id="item-tech-news-2"></a>
### [Shopify 移动应用从 React Native 回归原生 Swift 与 Kotlin](https://simonwillison.net/2026/Sep/10/shopify-react-native/) ⭐️ 7.0/10

Shopify 工程团队宣布，其移动应用将从 React Native 迁回 Swift 与 Kotlin 两套独立原生代码库。Shopify 在 2020 年从原生转向 React Native，当时的三个理由是避免同一功能重复开发、让开发者能跨栈工作，以及减少追赶功能对等所耗时间。团队表示，原生依然意味着在两个平台上构建和维护软件，这项成本并未消失，改变的是 AI 代理如今能完成足够多的实现、翻译、测试和评审工作，因此不再是 2020 年那样的决定性因素。Shopify 同时是三个重要 React Native 库的维护者：react-native-skia 与 flash-list 正在寻找新的归属方，而 restyle 因“用户基数小于我们其他库”将于 2026 年底归档。

rss · Simon Willison · 9月10日 21:11

**「背景」** React Native 是 Meta 推出的跨平台移动框架，用 JavaScript/React 编写一套代码即可同时构建 iOS 与 Android 应用；Shopify 曾在 2020 年从原生转向它，目的是不必重复实现同一功能、让开发者跨技术栈工作，并减少追赶功能对等的开销。2026 年 9 月 10 日，Shopify Engineering 发文宣布改回分别维护 Swift 与 Kotlin 原生代码库，表示原生仍意味着要在两个平台上构建和维护软件、这项成本并未消失，但 AI 智能体如今已能承担足够多的实现、翻译、测试与审查工作，使其不再是决定性因素。Shopify 同时是 react-native-skia、flash-list 和 restyle 三个重要 React Native 库的维护者，其中前两个正在寻找新的归属，而 restyle 因用户规模较小将于 2026 年底归档。

**「影响」** 依赖这些库的 React Native 开发者将面临 restyle 于 2026 年底归档、react-native-skia 与 flash-list 需要新维护方的过渡期，而其他正在权衡跨平台与原生路线的移动团队则获得了一个以 AI 编码代理降低双平台维护成本为论据的新参考案例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://shopify.engineering/back-to-native">Native is now the future of mobile at Shopify ( 2026 ) - Shopify</a></li>
<li><a href="https://sesamedisk.com/shopify-switching-from-react-native-to/">Shopify Switching from React Native - Sesame Disk</a></li>
<li><a href="https://digitechbytes.com/technology-news-gadgets/shopify-is-moving-from-react-native-back-to-swift-and-kotlin/">Shopify Is Moving From React Native Back To Swift And Kotlin</a></li>

</ul>
</details>

**标签**: `#React Native`, `#mobile development`, `#AI coding agents`, `#Shopify`, `#native apps`

---