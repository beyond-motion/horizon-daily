---
layout: default
title: "Horizon Summary: 2026-08-31 (ZH)"
date: 2026-08-31
lang: zh
---

> 从 4 条内容中筛选出 1 条重要资讯。

---

**科技新闻**
1. [解读 ChatGPT Work：云版与本地版两个产品](#item-tech-news-1) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [解读 ChatGPT Work：云版与本地版两个产品](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/) ⭐️ 7.0/10

Simon Willison 分析了 OpenAI 于 7 月 9 日发布的 ChatGPT Work，指出它实际上是两个不同产品：运行在云端的 Work Cloud 和通过桌面应用（原 Codex）访问本机文件与程序的 Work Local。Work 目前仅向每月 20 美元及以上的付费订阅者开放，免费用户和每月 8 美元的 Go 用户无法使用。Work Cloud 提供 Chat 所没有的多项能力，包括选择 GPT-5.6 Sol、Luna、Terra 模型及不同推理等级、可访问互联网的代码执行环境、完整的无头 Chrome 浏览器、跨会话持久化文件系统、发布 ChatGPT Sites、运行子代理会话以及定时提示自动化。其中，代码执行环境默认可访问全部域名，并能克隆 GitHub 仓库、安装依赖后与外部网络交互；浏览器工具还能在登录时让用户接管输入密码和 2FA 验证码，避免凭据经过模型。作者认为 OpenAI 官方关于“何时用 Chat、何时用 Work”的说明几乎无用，更关键的区别在于 Work 拥有 Chat 缺失的这些功能。

rss · Simon Willison · 8月30日 23:59

**「背景」** ChatGPT Work 是 OpenAI 在 2025 年 7 月推出的面向“有明确结果的任务”的产品，与普通 ChatGPT Chat 并列呈现为独立标签。它分为云端和本地桌面两个形态，其中本地形态由原 Codex 应用改造而来，目的是让非软件开发者也能使用类似 Codex 的本地文件与程序操作能力。

**「影响」** 对于每月 20 美元及以上的 ChatGPT 付费订阅者，Work Cloud 将原本受限的 AI 容器扩展为可自由访问互联网、运行完整浏览器并操作真实网站的工具，显著提升了自动化研究、数据抓取和网页交互类任务的可行性。不过，作者也指出部分功能（如定时自动化）可能已出现在 Chat 中，且模型计费与 Codex 额度相关，实际可用范围仍需进一步验证。

**标签**: `#ChatGPT`, `#OpenAI`, `#AI tools`, `#product analysis`, `#software engineering`

---