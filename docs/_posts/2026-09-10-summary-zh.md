---
layout: default
title: "Horizon Summary: 2026-09-10 (ZH)"
date: 2026-09-10
lang: zh
---

> 从 5 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [Shopify 从 React Native 迁回原生移动开发](#item-tech-news-1) ⭐️ 8.0/10
2. [Calif Research 称借 AI 两天写出微信通话零点击蠕虫 RCE](#item-tech-news-2) ⭐️ 8.0/10
3. [微软将 Rust 列为公司一级语言](#item-tech-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Shopify 从 React Native 迁回原生移动开发](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify 工程博客发布文章，详述其移动开发从 React Native 迁回原生（Native）的决策。此举逆转了此前高调的 React Native 迁移，在 Hacker News 上引发了关于跨平台与原生开发权衡的广泛讨论。由于原文内容未提供，迁移的具体范围、技术实现、时间线和性能数据等细节尚无法确认。该案例对正在评估跨平台与原生移动开发策略的团队具有参考意义，但应视为工程案例分析而非突破性技术变革。

hackernews · fnthawar2 · 9月10日 14:09 · [社区讨论](https://news.ycombinator.com/item?id=49643982)

**「背景」** React Native 是 Meta 开源的跨平台移动开发框架，允许用 JavaScript/React 编写同时运行于 iOS 和 Android 的应用，长期以来被企业视为复用 Web 团队、降低人力成本的方案。Shopify 曾在 2025 年将旗下最大的两个应用 Shopify Mobile 与 Shopify Point of Sale（POS）迁移到 React Native 的新架构（New Architecture），期间维持每周发布并服务数百万商家。但到 2026 年，Shopify 表示编码智能体（coding agents）改变了构建移动应用的两次成本结构，因此决定从 React Native 回到 Swift 和 Kotlin 原生开发；其 Shop 应用已完成这一反向迁移，从概念验证到发布仅用 12 周。

**「影响」** 这一转向意味着 Shopify 的移动团队将放弃其 2020 年出于“避免同一功能开发两次、让开发者跨技术栈工作”而采用的 React Native 共享代码库，改为分别维护 iOS 与 Android 原生实现，移动端招聘与工程分工也随之向平台专属工程师倾斜。由于本条仅提供了文章标题与检索摘要、未附正文，具体迁移范围、时间表与性能收益尚无法确认。

**「社区讨论」** 评论普遍认为跨平台与原生之争本质是资源约束下的工程决策，没有绝对答案；有人指出 RN 主要优势是让 Web 开发者参与移动端，但随着 AI 生成原生代码能力增强，这一优势正在减弱。多位开发者分享了从 RN 迁移到原生的类似经历，并提醒跨平台框架未必能降低人力成本，反而可能导致体验妥协。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://shopify.engineering/back-to-native">Native is now the future of mobile at Shopify (2026) - Shopify</a></li>
<li><a href="https://shopify.engineering/react-native-new-architecture">Migrating to React Native&#x27;s New Architecture (2025) - Shopify</a></li>
<li><a href="https://shopify.engineering/shop-app-migration">Migrating Shop app from React Native to native (2026) - Shopify</a></li>
<li><a href="https://shopify.engineering/back-to-native">Native is now the future of mobile at Shopify (2026) - Shopify</a></li>

</ul>
</details>

**标签**: `#React Native`, `#native mobile development`, `#cross-platform development`, `#Shopify`, `#software engineering tradeoffs`

---

<a id="item-tech-news-2"></a>
### [Calif Research 称借 AI 两天写出微信通话零点击蠕虫 RCE](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 8.0/10

Calif Research 发布了一段 WeWorm 演示，声称这是首个通过微信通话在 iOS 和 Android 上传播的零点击蠕虫：受害者无需接听电话，甚至完全不用触碰手机，即便接听也听不到任何声音，攻击依然成功。该团队表示，他们与 AI 协作，在约两天内找到漏洞并写出首个远程代码执行（RCE）利用，之后又用一周时间构建出蠕虫，并强调以往这种规模的蠕虫需要更大的团队投入数月才能完成。Calif Research 称 AI 已经能完成其中大部分工作，人类团队只负责判断攻击目标以及如何安全测试。不过目前公开的只是一份简短的公告与演示摘要，既没有披露具体技术细节，也没有经过独立验证，因此其真实影响与“首个”等表述仍需谨慎看待。

rss · Simon Willison · 9月10日 00:56

**「背景知识」** 零点击（zero-click）漏洞指的是攻击者无需受害者接听电话、点击链接或对手机做任何操作即可完成利用的攻击方式，而蠕虫（worm）则指能够自我复制、自动向其他设备或账号传播的恶意程序；两者结合意味着受害者一旦被呼叫，账号就可能被接管并继续向联系人扩散。微信（WeChat）是用户规模达十亿量级的即时通讯应用，其语音通话功能在 iOS 与 Android 两端都构成攻击面。远程代码执行（RCE）指攻击者在目标设备上运行任意代码，是此类利用链中危害最高的环节之一，Calif Research 称其借助 AI 分别完成了 Android 与 iOS 的 RCE 利用。

**「影响」** 若该演示属实，微信通话这一零点击攻击面会让 iOS 与 Android 用户在完全不接听、不交互的情况下暴露于远程代码执行风险，而据 Bishop Fox 与 PhantomByte 的分析，AI 辅助的零日开发正在把同类漏洞的利用成本与补丁窗口显著压缩。由于 Calif Research 目前只发布演示与声明，未提供技术细节或独立验证，上述影响仍属待证实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://calif.io/research/weworm">WeWorm | Calif</a></li>
<li><a href="https://blog.calif.io/p/weworm">WeWorm</a></li>
<li><a href="https://www.helpnetsecurity.com/2026/09/08/wechat-weworm-vulnerability-exploit-account-hijacking/">&quot;Zero-click&quot; WeChat worm could hijack accounts and spread via a single call - Help Net Security</a></li>
<li><a href="https://calif.io/research/weworm">WeWorm | Calif</a></li>
<li><a href="https://bishopfox.com/podcasts/ai-zero-day-exploit-ci-cd-supply-chain-poisoning-and-vibe-coded-data-exposure">AI Zero - Day Exploit , CI/CD Supply Chain Poisoning, and… | Bishop Fox</a></li>
<li><a href="https://articles.phantom-byte.com/five-days-to-zero-day-ai-exploit-threat-model.html">Five Days to Zero - Day : AI Exploit Threat Model - PhantomByte</a></li>

</ul>
</details>

**标签**: `#AI security`, `#zero-click exploit`, `#mobile security`, `#WeChat`, `#AI-assisted exploit development`

---

<a id="item-tech-news-3"></a>
### [微软将 Rust 列为公司一级语言](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 7.0/10

微软已将 Rust 列为公司内部的一级（Tier-1）语言，这一消息通过 Rust 基金会发布的一篇客座文章对外公布。此举被视为大型厂商在系统编程语言选择上的一次战略性承诺，与微软方面长期强调的内存安全方向一致——相关讨论中援引的数据称约 70% 的 CVE 属于内存安全问题。Rust 由此获得与 C++、C\# 等既有语言并列的定位，也意味着微软在其庞大的产品组合与工具链中为 Rust 预留了更正式的位置。需要注意，这是组织与政策层面的定位声明，而非新的技术发布、版本更新或研究成果，因此其影响更多是方向性的。

hackernews · mmastrac · 9月10日 13:39 · [社区讨论](https://news.ycombinator.com/item?id=49643546)

**「背景」** Rust 是由 Mozilla 发起、现由 Rust 基金会维护的系统编程语言，其内存安全设计可避免大量缓冲区溢出、释放后使用等常见漏洞。微软多年来已向 Rust 项目投入数百万美元，Azure CTO Mark Russinovich 也曾公开阐述其在原生代码上的战略方向；据相关统计，微软约 70% 的 CVE 属于内存安全问题，该比例与 Google、Apple 和 Linux 内核的情况相近。此次 Tier-1 认定意味着 Rust 与 C++、C\# 和 TypeScript 并列，成为微软内部开发可获得安全工具链构建、开发者工具、质量流程及安全合规支持的语言之一。

**「影响」** 对在 Windows、Azure 与 MSVC 工具链上开发的团队而言，Rust 升为微软一级语言意味着它从可选的试验性选项变为官方重点支持方向，新项目的语言选型与内存安全合规审查更可能默认纳入 Rust，微软同时把大规模 C/C++ 代码向 Rust 迁移作为安全驱动的既定目标。不过这是一项战略定位公告，具体工具链支持范围与迁移时间表并未在文中说明，实际影响取决于后续落地。

**「社区讨论」** 评论普遍认为这是 Rust 走向成熟的标志，有人强调它已不再是“快速迭代、边做边坏”的新生语言，而是能与 C++、C\# 正面竞争的严肃选项，相比 Zig、Odin 等同样主打“更好的 C/C++”的新语言更少粗糙之处。讨论还补充了两点外部背景：微软内部提出的到 2030 年借自动化工具转换 10 亿行代码的目标（“1 名工程师、1 个月、100 万行代码”），以及 DARPA 资助的多个团队用不同方案自动将 C 代码转为 Rust 的工作；同时有人提到关于 MSVC 集成 Rust 的传闻终于有了公开消息。也有评论借机吐槽 Windows 自带天气应用占用超过 1GB 内存，认为语言层面的改进未必能立刻反映到此类产品体验上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/">Guest Post: Rust Is Tier-1 Language at Microsoft</a></li>
<li><a href="https://newzino.com/story/rust-is-tier-1-language-at-microsoft-d647be">Microsoft makes Rust a Tier-1 language for internal ...</a></li>
<li><a href="https://rustify.rs/articles/rust-memory-safety-nsa-cisa-2026">Rust &amp; Memory Safety: What NSA, CISA &amp; White House Say (2026)</a></li>
<li><a href="https://www.buildmvpfast.com/blog/rust-replacing-cpp-cloud-infrastructure-microsoft-azure-2026">Microsoft Rust Mandate Azure C++ Migration 2026</a></li>
<li><a href="https://www.globalbrandsmagazine.com/microsoft-shifts-from-c-to-rust/">Microsoft Shifts from C++ to Rust by 2030: Key Insights</a></li>

</ul>
</details>

**标签**: `#Rust`, `#Microsoft`, `#memory safety`, `#programming languages`, `#industry adoption`

---