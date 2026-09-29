---
layout: default
title: "Horizon Summary: 2026-09-29 (ZH)"
date: 2026-09-29
lang: zh
---

> 从 8 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [EFF 报告：DraftKings 用 AI 定向瞄准问题赌徒](#item-tech-news-1) ⭐️ 7.0/10
2. [网页与移动端对话式 AI 智能体的隐私分析](#item-tech-news-2) ⭐️ 7.0/10
3. [Anthropic 发布 Claude Sonnet 5.5，同价提速并升级免费层](#item-tech-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [EFF 报告：DraftKings 用 AI 定向瞄准问题赌徒](https://www.eff.org/deeplinks/2026/09/draftkings-using-ai-supercharge-harms-online-behavioral-advertising) ⭐️ 7.0/10

电子前哨基金会（EFF）发布调查报告，指称在线博彩公司 DraftKings 利用 AI 对长期或问题赌徒进行行为定向投放。该报告将此事放在 AI 伦理与行业监管的议题框架下，认为这类技术应用会放大赌博成瘾造成的伤害。由于所提供的内容中没有报告正文，EFF 依据的具体技术手段、数据来源和证据细节目前无法核实。此事经 Hacker News 传播后引发了大量讨论，读者关注点集中在 AI 驱动的行为广告与在线博彩监管上。

hackernews · paimapi · 9月29日 16:30 · [社区讨论](https://news.ycombinator.com/item?id=49896050)

**「背景」** 行为定向广告（behavioral advertising）指依据对用户行为的追踪与推断来决定广告投放对象，电子前沿基金会（EFF）长期主张此类广告应被全面禁止，本次报告正是沿这一立场展开。据 EFF 及跟进报道，DraftKings 将 AI 用于自家博彩数据，以找出可能持续输钱的赌客并向其推送促销广告，其用于预测促销如何转化为客户输赢的模型最早于 2023 年年中开始搭建。相关报道指出，这一做法重新点燃了围绕行为定向广告监管的争论。

**「影响」** 对已经出现赌博问题迹象的用户来说，平台用 AI 做行为定向意味着能在其最脆弱的时点更精准地投放激励，从而加重成瘾与财务损失，并把监管审视的焦点引向博彩运营商对机器学习模型的使用。不过这一结论来自 EFF 的调查报道，在缺乏来源正文的情况下，具体模型与投放机制尚无法独立核实。

**「社区讨论」** 评论者普遍对该行业持强烈批评态度：有人援引 ProPublica 与赌博成瘾专家合作、以成瘾迹象测试 DraftKings 反应的报道，认为该公司缺乏伦理约束；也有人表示自己在数据科学研究生课程中就看到过凯撒娱乐通过建模识别“最有价值客户”、预测其流失并发放激励挽留的案例，说明此类做法在业内并非新事。另有评论质疑在线体育博彩与 iGaming 合法化本身，并批评监管对风险投资与赌博采取双重标准；还有一条评论以自嘲方式把 AI 订阅续费与赌博成瘾作类比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eff.org/deeplinks/2026/09/draftkings-using-ai-supercharge-harms-online-behavioral-advertising">DraftKings Is Using AI to Supercharge the Harms of Online...</a></li>
<li><a href="https://www.gambling.com/us/news/draftkings-ai-ad-targeting-draws-privacy-backlash">DraftKings AI Ad Targeting Draws Privacy Backlash</a></li>
<li><a href="https://futurism.com/artificial-intelligence/draftkings-ai-problem-gamblers">DraftKings Is Using AI to Identify Problem Gamblers and Get Them...</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#behavioral advertising`, `#online gambling`, `#machine learning`, `#tech regulation`

---

<a id="item-tech-news-2"></a>
### [网页与移动端对话式 AI 智能体的隐私分析](https://jorgegarciaherrero.com/wp-content/interactivos/20260916-Prompt-like-a-butterfly-sting-like-a-tracker-%28clean%29.pdf) ⭐️ 7.0/10

一份题为《A Privacy Analysis of Web and Mobile Conversational AI Agents》的隐私分析报告在 Hacker News 上引发关注，聚焦网页端与移动端对话式 AI 智能体中的提示词遥测、类追踪器行为以及薄弱的 URL 隐私保护等问题。由于该条目的原始 PDF 内容未随附提供，报告的具体测量方法、样本范围与结论细节无法在此核实。讨论中，有用户报告 ChatGPT 网页版会在用户尚未发送时，周期性把未完成的提示词发往 \`conversation/prepare\` 端点，这可能被用于缓存预热，也可能被用于追踪写作节奏、纠错习惯与尚在成形中的想法。另有用户指出，许多 AI 聊天服务把 URL 中的 UUID 等同于隐私保护，例如访问旧的 Perplexity 搜索链接会暴露完整对话。还有评论将其与本月早些时候围绕未公开草稿的争议相类比，认为本应保持私密的提示词与结果并未真正得到保护。

hackernews · damaru2 · 9月29日 09:03 · [社区讨论](https://news.ycombinator.com/item?id=49890226)

**「背景」** 对话式 AI 服务此前多以订阅或按量计费为主，用户与模型的交互一般被当作相对私密的内容。随着 OpenAI 等主要对话式 AI 提供商转向广告型商业模式，网页与移动端常见的追踪手段开始向对话式 AI 服务延伸，这正是该隐私分析所针对的变化。该研究由 IMDEA Networks 的 Narseo Vallina-Rodríguez 团队主导，论文已被隐私技术领域的学术会议 PoPETs 2027 接收，并经过同行评审。

**「影响」** 对使用网页版对话式 AI 的用户而言，社区报告显示未发送的提示词草稿与可分享的会话 URL 都可能泄露内容，仅凭 URL 中的 UUID 并不构成隐私保证。

**「社区讨论」** 评论整体对现有对话式 AI 的隐私实践持批评态度：有人把未发送提示词的预先传输视为潜在的追踪手段，有人批评以 UUID 代替访问控制，也有人据此主张开源本地模型的价值。同时，有评论对 AI 公司放任此类广告式机制感到意外，猜测相关机制较为仓促或受到盈利压力驱动；这些讨论以个人观察和类比为主，未提供系统性验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dspace.networks.imdea.org/handle/20.500.12761/2073">Prompt like a Butterfly, Sting like a Tracker: A Privacy Analysis of ...</a></li>
<li><a href="https://jorgegarciaherrero.com/en/prompt-like-a-butterfly-sting-like-a-tracker/">Infographic of the paper &quot; Prompt like a Butterfly , sting like a tracker &amp;quo...</a></li>

</ul>
</details>

**标签**: `#privacy`, `#conversational AI`, `#web tracking`, `#LLM telemetry`, `#mobile security`

---

<a id="item-tech-news-3"></a>
### [Anthropic 发布 Claude Sonnet 5.5，同价提速并升级免费层](https://simonwillison.net/2026/Sep/28/claude-sonnet-5-5/) ⭐️ 7.0/10

Anthropic 发布 Claude Sonnet 5.5，官方称其运行速度提升 30% 以上，大多数工作的成本最多降低 30%，定价与 Sonnet 5 相同，却在各项基准上均优于前者。Simon Willison 的实测显示，Sonnet 5.5 存在与 Opus 5.5 相同的缺陷：在“max”思考强度下，它为生成骑自行车的鹈鹕 SVG 消耗了 128,000 个 token（花费 1.28 美元）后耗尽额度并失败；而在“xhigh”强度下，它以 5.74 美分、41 秒生成了结构正确的鹈鹕（只是头盔形状不佳）。该模型在某些编码任务上已接近 Opus 5.5，包括社交网络上流行的 3D 动画技巧，并且在免费层 claude.ai 上也能生成基于 WebGL 的 3D 鹈鹕页面。Sonnet 5.5 现已成为 claude.ai 免费层所用模型，而 OpenAI 的 ChatGPT 免费层使用 Luna 5.6，Anthropic 由此在免费产品上更具能力优势；官方同时重申 Haiku 5.5 将在“未来几周内”推出。

rss · Simon Willison · 9月28日 22:07

**「背景」** Claude Sonnet 是 Anthropic 面向通用工作负载的中端模型，定位介于旗舰 Opus 与更轻量的 Haiku 之间。此次发布的 Sonnet 5.5 沿用 Sonnet 5 的定价——每百万输入 token 2 美元、每百万输出 token 10 美元，缓存读取每百万 0.20 美元——在价格不变的前提下提升速度与基准表现，其中 Terminal-Bench 4.0 得分 70.6%。Anthropic 同时表示，更轻量的 Haiku 5.5 将在“未来几周”推出。

**「影响」** claude.ai 免费层用户直接获得能力更强的默认模型，而在相同价格下，开发者的大多数调用有望更快、更便宜，不过“max”思考强度仍可能消耗大量 token 后失败，带来高额费用风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://computingforgeeks.com/claude-sonnet-5-5-released-features-benchmarks/">Claude Sonnet 5.5: Benchmarks, Pricing, Tested | ComputingForGeeks</a></li>
<li><a href="https://www.marktechpost.com/2026/09/28/anthropic-releases-claude-sonnet-5-5-70-6-on-terminal-bench-4-0-at-the-same-2-10-price/">Anthropic Releases Claude Sonnet 5.5: 70.6% on Terminal-Bench 4.0 at the Same $2/$10 Price - MarkTechPost</a></li>
<li><a href="https://www.digitalapplied.com/blog/claude-sonnet-5-5-launch-pricing-benchmarks-2026">Claude Sonnet 5.5: Pricing, Benchmarks and Safeguards</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude`, `#LLM`, `#AI models`, `#model release`

---