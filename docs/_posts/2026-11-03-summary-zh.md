---
layout: default
title: "Horizon Summary: 2026-11-03 (ZH)"
date: 2026-11-03
lang: zh
---

> 从 10 条内容中筛选出 5 条重要资讯。

---

**科技新闻**
1. [Qwen 3.8 27B 在笔记本上复现权重解读实验](#item-tech-news-1) ⭐️ 8.0/10
2. [Postman 被指静默安装 AI 插件并共享 API 数据](#item-tech-news-2) ⭐️ 7.0/10
3. [The &\#x27;Astra can read and write weights to improve Qwen&\#x27; post is misleading](#item-tech-news-3) ⭐️ 7.0/10
4. [飞机背景噪声可精确定位视频拍摄地点](#item-tech-news-4) ⭐️ 7.0/10
5. [LLM 0.37 发布：新模型、端点配置与嵌入改进](#item-tech-news-5) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Qwen 3.8 27B 在笔记本上复现权重解读实验](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/) ⭐️ 8.0/10

Simon Willison 在 2026 年 11 月 3 日的博客中介绍论文《Sparks of Weight-Space Programming》：作者 Rikiya Takehi、Jayden Teoh、Alex Zhang 和 Omar Khattab 提出“权重空间编程”，称 GPT-6 Astra 等前沿模型仅凭原始浮点权重就能判断网络被训练来做什么，并能在不写训练循环的情况下从零生成小型游戏网络，或原生编辑 Qwen3.5-0.8B 约 0.016% 的权重以修复推理循环，使 MATH-500 从 7.9% 升至 48.1%、IFEval 提升 3 倍。Willison 用自己笔记本上的 Qwen 3.8 27B 复现论文中“只看权重猜游戏”的无工具实验；该模型为 17GB 的 Q4\_K\_M 量化版，通过 LM Studio 和 llm-lmstudio 插件运行，并需调大默认 8192 上下文和超时。处理 Pac-Man 提示耗时 46 分 12 秒、消耗 43,506 个推理 token 后，Qwen 正确给出 Pac-Man 式 8x8 迷宫游戏描述并自评 72% 置信度；它还在 1 小时 4 分 54 秒内识别出 Pong，而 Kimi K3.1 Pro 用 9 分 41 秒、19,493 个推理 token 猜中 Breakout。不过所给摘录被截断，这些非凡主张尚未完全证实；Matthew Honnibal 批评论文混淆“无工具读权重”和“借助代码改权重”，Sean Goedecke 则认为 Qwen3.5-0.8B 的改进案例只是重复人类研究者会采取的步骤。

rss · Simon Willison · 11月3日 16:29

**「背景」** “权重空间编程”（Weight-Space Programming）是 Rikiya Takehi、Jayden Teoh、Alex Zhang 和 Omar Khattab 在 2026 年 11 月提出的概念，指让大语言模型直接阅读和改写神经网络的原始浮点权重，而不是通过运行代码或训练循环来操作模型。传统上，权重被视为难以直接解释的参数集合，LLM 主要处理文本和代码；该研究尝试用模型自身的推理来理解每部分权重的作用。相关结果仍属早期，主要来自单一模型，但团队公开了提示、回答和评估过程，便于复核。

**「影响」** 对本地模型用户来说，这意味着不必依赖云端前沿模型：用约 17GB 的 Qwen 3.8 27B，配合 LM Studio、llm-lmstudio 插件并调大上下文窗口，就能尝试仅凭原始权重推断网络行为，代价是单次推理耗时 46 分钟至 1 小时以上，并消耗数万推理 token。不过已有外部评论（如 Sean Goedecke）指出，论文中 Qwen3.5-0.8B 的权重修改示例实际上重复了人类研究者会采取的步骤，因此这类能力的实际边界仍有争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rikiyat.github.io/">Rikiya Takehi</a></li>
<li><a href="https://www.datacamp.com/blog/weight-space-programming">Weight-Space Programming: How LLMs Edit Network Weights</a></li>
<li><a href="https://www.seangoedecke.com/llms-are-not-superhuman-at-reading-and-writing-neural-network-weights/">LLMs are not superhuman at reading and writing neural network ...</a></li>

</ul>
</details>

**标签**: `#LLM interpretability`, `#weight-space programming`, `#model weights`, `#research paper`, `#local LLMs`

---

<a id="item-tech-news-2"></a>
### [Postman 被指静默安装 AI 插件并共享 API 数据](https://github.com/postmanlabs/postman-app-support/issues/14370) ⭐️ 7.0/10

一则提交到 Postman 官方 GitHub 支持仓库的 issue 指控 Postman 会在未明确告知的情况下自动安装 AI 插件，并尝试共享全部 API 数据。该 issue 在 Hacker News 引发大量讨论，焦点包括隐私、客户端臃肿以及是否迁移到替代工具；但目前没有独立验证或深入技术分析来证实这些指控。Postman 是广泛使用的 API 开发工具，若指控成立，可能涉及开发者的 API 密钥、请求内容和组织数据暴露风险；在得到确认前应将其视为未经证实的社区报告。

hackernews · sidgarimella · 11月3日 17:22 · [社区讨论](https://news.ycombinator.com/item?id=50354960)

**「背景」** Postman 是开发者常用的 API 调试与协作平台，早期以轻量级接口测试工具著称，后来扩展出账号体系、订阅和 AI 辅助等功能。Codex 与 Claude Code 是可调用外部工具和数据源的 AI 编程代理，MCP 是这类代理连接外部服务的协议，插件和启动钩子会在代理运行时注入配置。此次争议涉及的桌面端行为，正是 Postman 是否在用户不知情时把这些集成写入本机环境；相关指控还提到共享 API 数据，但已有分析对数据共享部分提出质疑。

**「影响」** 对于处理敏感 API 数据的团队，这一尚未经独立验证的指控已产生实际后果：有社区成员称其所在医疗机构的网络安全团队因此将 Postman 判定为不合规，团队在一夜之间迁移到 Bruno 等可将请求定义存入 Git 的替代工具。由于缺乏独立技术验证，Postman 究竟会上传哪些数据、范围多大仍不明确，受影响团队在评估风险时需自行核实。

**「社区讨论」** 评论整体对 Postman 的臃肿、强制登录、订阅和 AI 功能表示不满，多人称已迁移到 Bruno，并提到可将请求定义存入 Git；一名医疗行业用户称其所在机构的网络安全团队因此取消 Postman 认证，团队一夜之间完成迁移。也有评论认为这类工具本身已不再必要，反映出讨论更多基于使用体验和隐私担忧，而非对指控的技术验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/postmanlabs/postman-app-support/issues/14370">[SEVERE] Desktop auto-installs Codex/Claude plugins ... - GitHub</a></li>
<li><a href="https://explainx.ai/blog/postman-desktop-auto-installs-codex-claude-code-plugins-self-approved-hook-issue-14370-2026">Postman Auto-Installs Codex and Claude Code Plugins: What to ...</a></li>
<li><a href="https://dev.to/frankchu/postman-installed-itself-into-codex-and-claude-e38">Postman installed itself into Codex and Claude - DEV Community</a></li>

</ul>
</details>

**标签**: `#Postman`, `#privacy`, `#API tooling`, `#developer tools`, `#security`

---

<a id="item-tech-news-3"></a>
### [The &\#x27;Astra can read and write weights to improve Qwen&\#x27; post is misleading](https://honnibal.dev/blog/astra-read-write-misleading) ⭐️ 7.0/10

A rebuttal post arguing that claims about &\#x27;Astra reading and writing weights to improve Qwen&\#x27; are misleading, sparking expert discussion that reframes the result as reasoning-loop reduction rather than genuine model improvement.

hackernews · syllogism · 11月3日 12:21 · [社区讨论](https://news.ycombinator.com/item?id=50351111)

**标签**: `#mechanistic-interpretability`, `#llm-steering`, `#research-critique`, `#reasoning-models`, `#ai-research-claims`

---

<a id="item-tech-news-4"></a>
### [飞机背景噪声可精确定位视频拍摄地点](https://simonwillison.net/2026/Nov/3/a-sound-that-leaks-your-exact-location/) ⭐️ 7.0/10

Colsto 在 YouTube 视频中演示了一种 OSINT 方法：从视频音轨中提取几乎不可察觉的飞机背景噪声，并推导出各架飞机的多普勒曲线。随后，他将这些曲线与 ADS-B 航班数据交叉比对，利用飞机的速度、距离以及不同航班之间的间隔，推断视频的精确拍摄位置。Simon Willison 称这是一项巧妙的技术演示，并指出该技术具有明显的隐私影响。该条目本身只是简要指向视频，并未提供完整的技术细节或复现步骤。

rss · Simon Willison · 11月3日 05:32

**「背景」** ADS-B 是飞机广播自身位置、速度等数据的监视技术，因此公开的航班轨迹可与录音中的飞机噪声相互印证。飞机掠过时，声音频率会因多普勒效应先升后降，频谱图可用来估算飞机的速度和最接近点的斜距。Colsto 的演示还利用两次飞越之间 920 秒的间隔和一段静音约束筛选候选航班，从而把视频定位到具体地点。

**「影响」** 这意味着在飞机航线下录制并公开发布的音视频，可能仅凭约 60 秒的背景飞机噪声与公开 ADS-B 数据被定位到约 100 米范围，从而削弱创作者对“环境声不会泄露位置”的隐私预期；但该方法依赖足够清晰的过顶航班和可匹配的航班数据，并非所有录音都适用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=UytYrhYLOKI">I discovered a sound that leaks your exact location ... - YouTube</a></li>
<li><a href="https://www.techradar.com/computing/cyber-security/youtuber-discovers-aircraft-noise-trick-that-can-geolocate-your-videos-to-within-100m-doppler-effect-pinpoints-locations-from-just-60-seconds-of-audio">YouTuber discovers aircraft noise trick that can geolocate ...</a></li>

</ul>
</details>

**标签**: `#privacy`, `#OSINT`, `#audio forensics`, `#ADS-B`, `#YouTube`

---

<a id="item-tech-news-5"></a>
### [LLM 0.37 发布：新模型、端点配置与嵌入改进](https://simonwillison.net/2026/Nov/2/llm/) ⭐️ 7.0/10

Simon Willison 的 LLM 命令行工具和 Python 库发布 0.37 版，包含约两个月积累的功能与修复。此版本新增 gpt-6.1-sol 和 gpt-6.1-terra 模型，并加入 llm openai endpoint add 命令，便于配置使用 OpenAI 兼容端点的其他模型。若用户未自行设置默认模型，默认模型将切换为 gpt-6-luna，其价格为上一默认模型 gpt-5.6-luna 的一半。嵌入功能现在支持不同二进制内容具有不同 content-type，这是 Gemini Embedding 2 等可嵌入文本、音频、图像和视频的模型所需要的。该版本还包含来自 12 位作者的修复，几乎全部由 AI 辅助完成；作者表示审查负担没有预期中那么大。

rss · Simon Willison · 11月2日 23:49

**「背景」** LLM 是 Simon Willison 开发的开源命令行工具和 Python 库，用于通过远程 API 或本地安装的模型访问 OpenAI、Anthropic Claude、Google Gemini、Qwen、DeepSeek、Mistral 等多家大语言模型。它同时提供 CLI 和 Python 接口，因此 0.37 版本的功能变化会直接影响在终端、脚本和 Python 项目中调用模型的开发者。

**「影响」** 对使用 LLM 的开发者而言，新命令降低了接入 OpenAI 兼容服务的配置成本，默认模型切换可减少调用费用，而嵌入内容类型支持使 Gemini Embedding 2 的多模态嵌入更可用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/simonw/llm">GitHub - simonw/ llm : Access large language models from the...</a></li>
<li><a href="https://llm.datasette.io/">LLM : A CLI utility and Python library for interacting with Large...</a></li>

</ul>
</details>

**标签**: `#LLM CLI`, `#Python library`, `#OpenAI-compatible endpoints`, `#embeddings`, `#release`

---