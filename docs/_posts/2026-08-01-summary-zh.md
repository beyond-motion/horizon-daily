---
layout: default
title: "Horizon Summary: 2026-08-01 (ZH)"
date: 2026-08-01
lang: zh
---

> 从 10 条内容中筛选出 5 条重要资讯。

---

**科技新闻**
1. [DeepSeek 发布 V4-Flash-0731：304B 参数、低价高性能](#item-tech-news-1) ⭐️ 8.0/10
2. [无状态 MCP 2.0 让 Simon Willison 重燃兴趣，并催生新工具](#item-tech-news-2) ⭐️ 8.0/10
3. [Simon Willison 在 Oxide and Friends 畅谈开放权重革命](#item-tech-news-3) ⭐️ 8.0/10
4. [电梯调度算法的技术剖析与目的楼层派送结论](#item-tech-news-4) ⭐️ 7.0/10
5. [smevals：用于评估模型、提示词和测试框架的小型评测套件](#item-tech-news-5) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [DeepSeek 发布 V4-Flash-0731：304B 参数、低价高性能](https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything) ⭐️ 8.0/10

DeepSeek 发布了 V4 系列最新模型 DeepSeek-V4-Flash-0731，拥有 3040 亿参数，Hugging Face 上体积为 167GB，官方称其“智能体能力大幅增强”。Artificial Analysis 将其排在 4280 亿参数的 MiniMax M3 之前，且输入价格仅每百万 token 0.14 美元、输出价格每百万 token 0.27 美元，被认为是目前性价比最高的模型之一。Simon Willison 通过 OpenRouter 测试发现，默认推理级别生成“鹈鹕骑自行车”图片效果不佳，但将 reasoning\_effort 设为 high 后输出质量明显提升。该模型在 Artificial Analysis 的智能指数与单任务成本对比图上，处于极具吸引力的性价比区间，超过它的模型单任务成本多在 0.4 至 3 美元。

rss · Simon Willison · 7月31日 23:59

**「背景」** DeepSeek 于 2026 年 4 月 24 日首次发布 V4 Flash，作为 V4 家族中较小的成员：这是一款 284B 参数的 MoE 模型，每 token 激活 13B 参数，具备 1M token 上下文窗口，权重采用 MIT 许可证；同期发布的 V4 Pro 则为 1.6T 参数。2026 年 7 月 31 日发布的 V4 Flash 0731 是后续的重新后训练检查点，属于官方正式版本，将 deepseek-v4-flash API 从预览状态推进到公开测试阶段，并据称显著提高了智能体相关评测得分。

**「影响」** 对 AI 开发者和用户而言，该模型以极低价格提供了接近更大闭源模型的智能水平，显著降低了高质量推理和智能体任务的成本门槛。实际使用中需注意推理级别对输出质量影响明显，复杂任务应显式设置 reasoning\_effort 为 high。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.digitalapplied.com/blog/deepseek-v4-flash-0731-official-release-agent-benchmarks">DeepSeek V4 Flash 0731: Official Release, Agent Benchmarks</a></li>
<li><a href="https://www.modemguides.com/blogs/ai-news/deepseek-v4-flash-official-release">DeepSeek V4-Flash 0731: What Changed and What You Can Run</a></li>
<li><a href="https://www.developersdigest.tech/blog/deepseek-v4-flash-0731-opencode-guide">DeepSeek V4 Flash 0731: The Official Release, Benchmarks, and How to Run It in OpenCode - Developers Digest</a></li>

</ul>
</details>

**标签**: `#deepseek`, `#large-language-models`, `#ai`, `#machine-learning`, `#open-source`

---

<a id="item-tech-news-2"></a>
### [无状态 MCP 2.0 让 Simon Willison 重燃兴趣，并催生新工具](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything) ⭐️ 8.0/10

Simon Willison 在 2026 年 7 月 31 日的文章中表示，2026 年 7 月 28 日发布的 Model Context Protocol（MCP）2.0 规范（即 Stateless MCP）是 MCP 自推出以来最重大的变化，重新点燃了他对该协议的兴趣。与旧版有状态 MCP 需要先发送 initialize 请求获取 Mcp-Session-Id、再发送第二次请求调用工具不同，无状态 MCP 只需单个 HTTP 请求，通过 MCP-Protocol-Version、Mcp-Method 和 Mcp-Name 等头信息直接调用工具，无需维护服务器端会话状态，更适合构建可扩展的 Web 应用。他因此构建了两个新工具：mcp-explorer 是一个可通过 uvx 直接运行的 Python CLI，用于交互式探索和调用 MCP 服务器；datasette-mcp 是一个 Datasette 插件，为任意 Datasette 实例新增 /-/mcp 端点，目前提供 list\_databases\(\)、get\_database\_schema\(database\_name\) 和只读的 execute\_sql\(database\_name, sql\) 三个工具。他已在 datasette.simonwillison.net/-/mcp 运行该插件，并记录了将其接入 ChatGPT 和 Claude 的方法。

rss · Simon Willison · 7月31日 23:13

**「背景」** MCP 是 Anthropic 于 2024 年 11 月推出的协议，用于以标准方式向大语言模型驱动的智能体框架暴露工具。2025 年它曾获得大量关注，但随后被 Anthropic 的 Skills 概念部分掩盖，因为具备终端和 curl 访问能力的智能体似乎能以更灵活的方式实现 MCP 的多数功能。无状态 MCP 通过减少实现客户端和服务器的复杂度，让工具调用更易于审计和控制，也使得能在笔记本电脑上运行的较小模型更容易使用这些工具。

**「影响」** 对于使用 MCP 的开发者而言，无状态 MCP 显著降低了客户端与服务端的实现复杂度，免除了会话 ID 管理和同会话后端路由的负担，同时使 mcp-explorer 和 datasette-mcp 这类新工具能够快速落地，用户可以直接用 uvx 浏览和调用 MCP 工具，并让 ChatGPT 或 Claude 等智能体通过只读 SQL 查询访问 Datasette 实例。

**标签**: `#MCP`, `#Model Context Protocol`, `#AI agents`, `#software engineering`, `#Simon Willison`

---

<a id="item-tech-news-3"></a>
### [Simon Willison 在 Oxide and Friends 畅谈开放权重革命](https://simonwillison.net/2026/Jul/31/oxide-and-friends/#atom-everything) ⭐️ 8.0/10

Simon Willison 在 2026 年 7 月 31 日的博客文章中总结了他与 Bryan Cantrill、Adam Leventhal 在 Oxide and Friends 播客上的对话，主题是“开放权重革命”。他们回顾了 Kimi K3 证明开放权重模型可与专有前沿模型匹敌、意外的网络安全攻击，以及几乎所有 AI 大人物联名签署的《开放权重与美国 AI 领导力》公开信，其中 Anthropic 是显著例外。Willison 指出这期节目在录制几天后便已过时，因为 DeepSeek V4 Flash 0731 和 Anthropic 自身的网络安全事件本应入选话题。他们还聊到了 Golden Gate Claude、Zizians、阿拉米达野生火鸡袭击、苏联马尔堡病毒研究和铅犯罪假说等话题，并回顾了 2026 年 1 月的预测，新增了一条预测：今年年底前教皇会就开放模型发表言论。

rss · Simon Willison · 7月31日 21:33

**「背景」** 开放权重（open-weight）模型指公开模型权重、允许下载与二次开发的大语言模型，与封闭的专有前沿模型相对。Kimi K3 于 2026 年 7 月 27 日开放权重（沿用 K2 的 Modified MIT 许可），参数量达 2.8T，以每百万 token 15 美元的定价与专有模型竞争；同期 DeepSeek V4 Flash 等开放权重模型也在基准与成本上逼近美国闭源模型。这波进展与多家 AI 公司签署支持开放权重的公开信、以及 Anthropic 作为明显例外等事件，共同构成该播客讨论的行业背景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.vals.ai/models/kimi_kimi-k3">Kimi K 3</a></li>
<li><a href="https://datamy.co/resources/blog/kimi-k3-chinese-open-weight-vs-us-frontier-enterprise-2026">Will Kimi K 3 Flip the Table on Anthropic and OpenAI? | DataMy</a></li>
<li><a href="https://bota.chat/kimi-k3/">Kimi K 3 Explained: 2.8T Params, $15/M Tokens, Open</a></li>

</ul>
</details>

**标签**: `#open-weights`, `#AI`, `#podcast`, `#Simon Willison`, `#industry-policy`

---

<a id="item-tech-news-4"></a>
### [电梯调度算法的技术剖析与目的楼层派送结论](https://john.fun/elevators) ⭐️ 7.0/10

《Elevators》是发布在 john.fun 上的技术文章，用模拟方式剖析电梯调度算法，对比不同调度策略，并对目的楼层派送（Destination Dispatch）给出出人意料的比较结果。文章还将电梯问题与磁盘寻道中的 SCAN 调度、软件工程中的队列策略联系起来，并借助交互式演示帮助读者理解实际影响。这篇内容在 Hacker News 上引发了关于算法假设、现实客流模式和调度器设计的热烈讨论。

hackernews · Jrh0203 · 7月31日 15:17 · [社区讨论](https://news.ycombinator.com/item?id=49124218)

**「背景」** 电梯调度算法用于决定多部电梯如何响应楼层呼叫，常见的策略包括传统上下行扫描（类似磁盘调度中的 SCAN 算法）和目的地派梯（乘客在进入电梯前输入目标楼层）。该文章所在的 john.fun 站点还提供互动模拟和谜题项目，帮助直观理解这些算法在实际场景中的表现。

**「影响」** 对从事电梯控制系统或类似调度问题的工程师而言，文章提供了一个直观的模拟参考，提示不应假设目的楼层派送总是更优，而须根据实际客流模式评估算法。

**「社区讨论」** 评论区的共识是文章主题有趣且与磁盘调度 SCAN 直接相关，也有人推荐 Elevatorsaga 模拟游戏；主要分歧在于目的楼层派送表现较差是否源于随机目的地假设，现实中人们往往集中去往地面层或集体去同一楼层。另有用户分享了高层建筑电梯饱和以及住宅电梯联动不便的实际体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://john.fun/">John.fun</a></li>
<li><a href="https://upstract.com/x/fcf19264873998d7">Elevators - upstract.com</a></li>

</ul>
</details>

**标签**: `#algorithms`, `#elevator-scheduling`, `#simulation`, `#disk-scheduling`, `#software-engineering`

---

<a id="item-tech-news-5"></a>
### [smevals：用于评估模型、提示词和测试框架的小型评测套件](https://simonwillison.net/2026/Jul/31/smevals/#atom-everything) ⭐️ 7.0/10

Simon Willison 宣布与 Prime Radiant 应用 AI 研究实验室合作推出 smevals，这是一个新的开源小型评测套件，用于对不同模型配置运行评测并自动评分。工具通过 uvx 命令使用，例如 \`uvx smevals run path-to-eval/ -m gpt-5.5 -m claude-opus-4.6\` 可运行评测，\`uvx smevals grade\` 进行评分，\`uvx smevals serve\` 启动本地 Web 服务器查看结果，或通过 \`smevals build\` 生成可托管的静态 HTML 报告。评测以包含 YAML 文件的目录形式定义，并引入了 eval、task、config、run、grader、check 等明确概念；Willison 还提供了一个评估模型写俳句能力的示例报告。这是 Willison 多年来针对评估方法的第三次迭代，他认为该方案目前感觉最合适，并计划继续扩展。

rss · Simon Willison · 7月31日 21:15

**「背景信息」** 评估套件用于系统衡量模型、提示词或智能体流程在特定任务上的表现，是开发 LLM 应用时对比不同配置的重要工具。Willison 表示他多年来一直在探索自己认可的评估方法，smevals 是这一探索的第三个版本，其特点是运行与评分分离，并允许通过 YAML 文件灵活定义评测任务和检查条件。

**「影响」** 对于需要快速比较不同模型或提示词配置的 AI 工程师，smevals 提供了一个低门槛、可复现的本地评测工作流，能够直接嵌入开发和测试流程。

**标签**: `#evals`, `#LLM`, `#tooling`, `#machine-learning`, `#open-source`

---