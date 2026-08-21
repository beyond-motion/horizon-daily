---
layout: default
title: "Horizon Summary: 2026-08-21 (ZH)"
date: 2026-08-21
lang: zh
---

> 从 7 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [意外劫持 E.164 ARPA 域名，记录数十万通打往军事基地的电话](#item-tech-news-1) ⭐️ 8.0/10
2. [DeepSeek v4-flash-vision-exp 发布，为 Flash 模型加入视觉能力](#item-tech-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [意外劫持 E.164 ARPA 域名，记录数十万通打往军事基地的电话](https://lina.sh/blog/hijacking-e164-arpa) ⭐️ 8.0/10

一名开发者意外劫持了 E.164 ARPA DNS 记录，导致数百通电话被错误路由至军事基地，并记录了数十万条此类通话日志。这一事件暴露了 E.164 ARPA/ENUM 系统这一基本被遗忘但仍活跃的基础设施漏洞。作者通过实际调查发现，该 DNS 区域配置存在严重错误，且缺乏有效监管，使得任何人都可能利用此漏洞进行电话路由劫持。尽管作者主动报告了问题，但并未获得奖励，且相关机构在涉及军事基地后才重视此事。该事件凸显了电话路由与 DNS 基础设施之间长期被忽视的安全隐患。

hackernews · gavide · 8月21日 13:11 · [社区讨论](https://news.ycombinator.com/item?id=49387570)

**「背景」** E.164 ARPA 是用于电话号码到域名映射的 DNS 区域，旨在支持 ENUM（电话号码映射）服务，使电话系统能够通过 DNS 查询路由呼叫。然而，该技术从未广泛采用，逐渐被边缘化，但相关基础设施仍部分存在，且可通过私有服务访问。由于缺乏维护和监管，这些遗留系统容易受到配置错误或恶意利用。

**「影响」** 该事件表明，E.164 ARPA 基础设施的配置错误可导致电话路由被意外劫持，影响涉及军事基地等敏感机构的通话，并可能造成隐私泄露或安全风险。尽管作者未受惩罚，但此类漏洞的发现和报告过程缺乏明确奖励机制，可能阻碍未来类似问题的主动披露。

**「社区讨论」** 社区评论指出，E.164 ARPA 并非完全死亡，而是几乎不公开，可通过 VPN 访问私有服务获取号码移植信息。有用户惊讶于作者未因此入狱，认为通常报告此类问题会面临法律风险。另有评论建议作者应设置 SIP 服务器以验证是否产生实际通话终止，并提及 TRIP 协议作为相关替代方案。整体上，社区认为此类漏洞长期存在且无人关注，直到涉及军事才被重视，作者未获奖励令人遗憾。

**标签**: `#DNS`, `#telephony`, `#security`, `#ENUM`, `#infrastructure`

---

<a id="item-tech-news-2"></a>
### [DeepSeek v4-flash-vision-exp 发布，为 Flash 模型加入视觉能力](https://api-docs.deepseek.com/guides/vision/) ⭐️ 7.0/10

DeepSeek 发布了 v4-flash-vision-exp 实验性模型，为其广受欢迎的 v4-flash 模型新增了视觉输入能力。该模型将图像按尺寸转换为 token，并与文本 token 一起计费；推理前所有图像会自动按比例缩放，小于约 384×384 像素的图像会被放大，更大的图像则被缩小。这一更新解决了此前 v4-flash 模型无法处理图像、甚至可能虚构图像分析工具的已知局限。社区反馈显示，该模型在读取时钟等简单视觉任务上仍存在失败案例，但整体被视为有前景的升级。官方公告还附带了基准测试结果，但具体数据未在本次内容中提供。

hackernews · dares2573 · 8月21日 10:33 · [社区讨论](https://news.ycombinator.com/item?id=49386163)

**「背景」** DeepSeek 此前发布的 v4-flash 系列模型以文本处理为主，在代码生成等任务上受到开发者欢迎，但缺乏视觉输入能力，导致其在处理截图、图像等场景时存在明显局限。此次发布的 deepseek-v4-flash-vision-exp 是 DeepSeek 推出的实验性多模态模型，在原有 flash 模型基础上新增了视觉理解能力，支持 Chat Completions、Messages 和 Responses 三种 API 格式，并将每张图像按尺寸转换为最多 384 个可计费的 V4-Flash token。该模型旨在缩小与 Anthropic Opus 4.8 等主流多模态模型在智能体工作流方面的差距，同时 DeepSeek 还同步发布了对其提供开箱即用支持的 DeepSeek Harness 0.1.1 工具。

**「影响」** 对于依赖 DeepSeek v4-flash 进行代码任务和自动化测试的开发者，这一更新填补了视觉能力的空白，使其无需切换到其他模型即可处理截图和图像输入，但时钟读取等基础视觉任务的失败表明其视觉精度仍不及某些竞品（如 Qwen3.8 27B），实际使用中需谨慎验证。

**「社区讨论」** 开发者普遍欢迎这一更新，认为它解决了 v4-flash 无法查看 Playwright 截图等实际痛点，但也有用户指出其在简单时钟识别测试中失败，而 Qwen3.8 27B 几乎能正确回答，显示视觉能力仍有明显短板。另有用户询问既然新模型能覆盖文本功能并增加视觉，文本专用版本是否还有存在必要，引发关于成本与延迟的讨论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://api-docs.deepseek.com/news/news260821/">DeepSeek - V 4 - Flash - Vision - Exp Release... | DeepSeek API Docs</a></li>
<li><a href="https://runtimewire.com/article/deepseek-v4-flash-vision-api-image-billing">DeepSeek &#x27;s experimental vision model spans three formats, caps...</a></li>
<li><a href="https://www.roic.ai/news/deepseek-unveils-experimental-multimodal-model-challenging-anthropic-08-21-2026">DeepSeek Unveils Experimental Multimodal Model ... | Roic News</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#vision-language-model`, `#AI-model-release`, `#multimodal-AI`, `#developer-tools`

---