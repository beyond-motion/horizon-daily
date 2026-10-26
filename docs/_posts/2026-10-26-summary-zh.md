---
layout: default
title: "Horizon Summary: 2026-10-26 (ZH)"
date: 2026-10-26
lang: zh
---

> 从 6 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [Anthropic 提交 S-1：估值与需求成为焦点](#item-tech-news-1) ⭐️ 8.0/10
2. [Raschka 发布从零构建推理模型视频课程](#item-tech-news-2) ⭐️ 7.0/10
3. [PBT 不加速 grokking，但能逃离无效超参数区](#item-tech-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Anthropic 提交 S-1：估值与需求成为焦点](https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm) ⭐️ 8.0/10

Anthropic 的 S-1 文件已在 SEC EDGAR 上公开，表明这家主要 AI 实验室启动了公开披露进程。由于条目未提供文件正文，估值、营收、合同承诺等具体条款无法从原始材料核实。该文件受关注的原因在于，它可能系统披露 Anthropic 的业务、财务与战略，并检验市场对 AI 需求持续性的判断。现有讨论集中在高估值是否已透支增长，以及大规模算力与云服务承诺在需求不及预期时是否会造成财务压力。

hackernews · SiNTEx · 10月26日 13:04 · [社区讨论](https://news.ycombinator.com/item?id=50242939)

**「背景」** S-1 是美国公司申请首次公开募股（IPO）时向证券交易委员会提交的注册说明书，其中须披露经审计的财务数据、风险因素、募资用途和大额合同义务，因此它常被视为外界第一次系统了解一家未上市公司经营全貌的窗口。Anthropic 是开发 Claude 系列模型的人工智能实验室，此前长期以非上市身份运营，所以这份文件把它的收入、利润和长期算力采购承诺同时置于公开审视之下。据媒体报道，该公司的营收增长很快：2026 年上半年收入为 163 亿美元，上年同期为 11.6 亿美元，并且 2026 年第二季度首次实现 9.74 亿美元的 GAAP 营业利润，利润率为 8%；同时，该公司据称计划以最高 2 万亿美元的估值融资 1000 亿美元。

**「影响」** Anthropic 提交 S-1 并计划在纳斯达克上市，使潜在公开投资者必须用招股书披露的营收来检验报道中接近 2 万亿美元的估值，而不是只依赖私募市场的增长叙事。若发行推进，其估值与需求能否匹配将直接接受二级市场定价。

**「社区讨论」** 多位评论者对传闻中的高估值持怀疑态度：有人以亚马逊 IPO 后的长期回报作对照，认为当前价格已透支增长；也有人质疑，若 AI 最大化叙事成真，AI 公司是否还会遵守货币与所有权规则。另有评论把焦点放在需求能否支撑扩张上，提到对 Google、AWS、Broadcom、SpaceX 的巨额承诺，并将远期现金承诺、产品商品化和缺乏护城河的风险与 WeWork 的 S-1 相提并论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zerohedge.com/ai/anthropics-s-1-out-974-million-operating-profit-800-billion-compute-bill-and-elon-musk-landlord">Anthropic &#x27; s S - 1 Is Out: A $974 Million Operating Profit... | ZeroHedge</a></li>
<li><a href="https://www.fool.com/investing/2026/10/26/5-key-numbers-from-anthropic-s-s-1-filing/">5 Key Numbers From Anthropic &#x27; s S - 1 Filing | The Motley Fool</a></li>
<li><a href="https://www.anthropic.com/news/s1-sec">Anthropic files S-1 with the SEC for proposed initial public ...</a></li>
<li><a href="https://www.forbes.com/sites/ronschmelzer/2026/10/26/anthropics-ipo-what-its-s-1-reveals-about-the-ai-boom/">Anthropic&#x27;s IPO: What Its S-1 Reveals About The AI Boom - Forbes</a></li>

</ul>
</details>

**标签**: `#AI industry`, `#IPO filing`, `#Anthropic`, `#SEC filings`, `#business strategy`

---

<a id="item-tech-news-2"></a>
### [Raschka 发布从零构建推理模型视频课程](https://magazine.sebastianraschka.com/p/building-reasoning-models) ⭐️ 7.0/10

Sebastian Raschka 发布了一套从零构建推理模型的视频课程，并在 Hacker News 上引发了以正面评价为主的讨论。读者关注这套课程的学习价值，也提出了关于算力成本的实际问题，包括是否需要云端 GPU、本地电脑需要多强，以及为学习目的购置 PC 是否值得。评论中有人推荐 Raschka 的《Build Your Own LLM From Scratch》，并称其讲解直观、可读性强，能帮助读者把复杂概念真正串联起来。现有信息主要体现课程作为教学资源的价值，尚未给出明确的硬件门槛或费用结论。

hackernews · sgiannopoulos · 10月26日 15:11 · [社区讨论](https://news.ycombinator.com/item?id=50245138)

**「背景」** 推理模型是会在给出最终答案前生成中间推理步骤的 LLM，常见做法包括推理时扩展（如采样、自洽、自我修正）、强化学习以及从更强模型蒸馏。Sebastian Raschka 是机器学习教育者，擅长用 Python/PyTorch 从零实现来讲解 LLM；其相关课程和书从预训练模型出发，覆盖评估、推理时扩展、强化学习和蒸馏等环节。此次视频课程延续这种配套代码讲解方式，公开介绍称以 Qwen3 0.6B 为起点，在 MATH-500 上评估，并演示简化的 GRPO 强化学习流程。

**「影响」** 对希望从零理解推理模型实现的学习者而言，这套课程提供了一个以动手构建为核心的学习资源，但其实际算力成本和硬件门槛在讨论中仍未得到明确答案。

**「社区讨论」** Hacker News 评论整体评价积极，读者称其讲解直观、有助于让知识真正融会贯通，并推荐他的《Build Your Own LLM From Scratch》。主要疑问集中在完成课程或书籍所需的算力：是否需要云端 GPU、普通本地电脑是否足够，以及为此购置 PC 是否值得。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sebastianraschka.com/teaching/">Courses - Sebastian Raschka, PhD</a></li>
<li><a href="https://sebastianraschka.com/reasoning-from-scratch/">Build a Reasoning Model (From Scratch) | Sebastian Raschka, PhD</a></li>
<li><a href="https://www.youtube.com/watch?v=Kh9mqTzjuEQ">Build A Reasoning Model From Scratch 1: Motivation &amp; Code ... Building Reasoning Models from the Ground Up: A Video Course Build A Reasoning Model (From Scratch) - YouTube Sebastian Raschka Releases Video Course on Building Reasoning ... Build Your Own Reasoning Model: A Full Video Course</a></li>

</ul>
</details>

**标签**: `#LLMs`, `#reasoning models`, `#machine learning education`, `#from-scratch implementation`

---

<a id="item-tech-news-3"></a>
### [PBT 不加速 grokking，但能逃离无效超参数区](https://www.reddit.com/r/MachineLearning/comments/1xfqhfc/pbt_doesnt_make_grokking_faster_but_it_can_escape/) ⭐️ 7.0/10

一项 Reddit 实验报告在模 97 的加法 grokking 任务（35% 训练集、小型 MLP、20 个种群成员、20k 步、全批量）上比较了基于种群的训练（PBT）与网格/随机搜索，结论是 PBT 并不能加快 grokking。在相同算力和 3 个种子下，最佳固定网格单元达到 95% 验证准确率用了 317±29 步，而 PBT 用了 2667±2244 步，每个种子都更慢。在 lr 1e-4–1e-3、wd 0.01–0.08 的“死区”起始条件下，固定设置 0/3 能 grok，慢速 PBT 也为 0/3，但每 100 步以 ×0.5/×2 调整的快速 PBT 为 3/3，约 6850 步成功，路径是先降 lr 到底、再升 wd 到顶、随后升 lr。消融显示随机供体仍能逃离但更晚，无选择时种群会先 grok 再丢失；10 个种子下宽随机搜索达到 95% 的中位步数为 300，而 PBT 从死区出发为 6650，且 PBT 有时会塌缩到 lr 下限/wd 上限角落不再离开。将获胜 lr/wd 调度在不使用 PBT 的情况下重放，新初始化中 55/60 达到 95%，而固定在调度几何均值的常量旋钮为 0/60，说明结果来自调度而非权重复制；作者同时注明仅一个任务/模型/划分、每项 3–10 个种子且 p 值多大于 0.05、重放调度是事后赢家，尚未测试完全不存在 grokking 区域的超参数范围。

reddit · r/MachineLearning · /u/Virtual-Message-9739 · 10月26日 07:48

**「背景」** Grokking（延迟泛化）指模型先在训练集上过拟合，验证集性能却在很久之后才明显提升；模加法是研究这一现象的经典合成任务。Population-Based Training（PBT）维护一组并行训练副本，按验证指标定期挑选表现较好的成员，复制其权重并扰动超参数，从而在线搜索学习率和权重衰减等设置。该实验在模加法上比较 PBT 与网格搜索、随机搜索，因此需要区分“更快找到好超参数”和“从无解超参数区域中逃出”这两种目标。

**「影响」** 对研究 grokking 和超参数优化的 ML 实践者而言，在这类小型合成任务上不应把 PBT 当作加速手段；当搜索范围包含良好固定配置时应优先网格或随机搜索，而 PBT 更适合作为逃离无效超参数区的救援工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2407.12332">[2407.12332] Why Do You Grok? A Theoretical Analysis of Grokking ...</a></li>
<li><a href="https://www.alignmentforum.org/posts/N6WM6hs7RQMKDhYjB/a-mechanistic-interpretability-analysis-of-grokking">A Mechanistic Interpretability Analysis of Grokking</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#grokking`, `#population-based training`, `#hyperparameter optimization`, `#training dynamics`

---