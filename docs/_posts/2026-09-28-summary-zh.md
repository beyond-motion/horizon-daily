---
layout: default
title: "Horizon Summary: 2026-09-28 (ZH)"
date: 2026-09-28
lang: zh
---

> 从 6 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [Simon Willison 回顾 2026 年 LLM 进展](#item-tech-news-1) ⭐️ 7.0/10
2. [函数梯度下降结合自适应表示获 NeurIPS 接收](#item-tech-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Simon Willison 回顾 2026 年 LLM 进展](https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/) ⭐️ 7.0/10

Simon Willison 于 2026 年 9 月 25 日在圣何塞举行的 WeAreDevelopers World Congress North America 上发表闭幕主旨演讲，按时间顺序梳理 2026 年迄今的大语言模型发展，并于 9 月 27 日发布带注释的幻灯片与讲稿，视频同步上传 YouTube。他把 2026 年的起点定在 2025 年 11 月：Claude Opus 4.5 与 GPT-5.1 相继发布，虽属渐进式改进，但与各自的编程智能体框架（2025 年 2 月问世的 Claude Code 和稍晚的 Codex）配合后，从“经常出错”变为“足以日常可靠使用”。他仍用“生成骑自行车的鹈鹕 SVG”这一自嘲式基准测试新模型，认为 11 月时两款模型画出的自行车与鹈鹕依然很糟；他还提到 2025 年 11 月 24 日冷门 GitHub 仓库 Warelay 的首次提交（演讲后续会再谈及），以及 12 月假期开发者试用新模型组合、1 月纷纷投入实践。他今年的新年决心改为“更有野心、想接多少新项目就接多少”，并列出 2026 年预测，包括 LLM 写出好代码将无可否认、沙箱问题终获解决、编程智能体安全可能出现“挑战者号式”灾难、鸮鹦鹉繁殖季表现优异，以及教皇将就 LLM 的经济影响表态。需要注意的是，所提供的内容在幻灯片 009 处被截断，其后的技术细节与结论无法从现有材料核实。

rss · Simon Willison · 9月27日 23:54

**「背景」** Simon Willison 长期在其博客上跟踪并评测大语言模型，并习惯把演讲整理成「带注释的幻灯片」（annotated talk）：每张幻灯片配图并附上文字说明，完整视频另行发布在 YouTube，这次演讲的视频也已上传。本文对应的是 2026 年 9 月 25 日他在圣何塞 WeAreDevelopers World Congress North America 上的闭幕主题演讲，按时间顺序回顾 2026 年（截至演讲时）LLM 领域发生的事件，并说明这一年他如何调整自己的项目计划。文中反复提到的「编码智能体」指 Claude Code（2025 年 2 月问世）与更晚出现的 Codex 这类把模型接入工具链、可自主完成编码任务的产品，而他把 2025 年 11 月发布的 Claude Opus 4.5 与 GPT-5.1 视为一个关键转折点。

**「影响」** 对开发者而言，Claude Opus 4.5 与 GPT-5.1 搭配各自的编码智能体（Claude Code、Codex）已从“经常出错”跨越到“可靠到足以日常使用”，使 2026 年初起把大量新项目交给智能体推进成为可行选择；但 Willison 同时提醒，要真正释放其潜力仍需极强的纪律与知识储备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/">2026 in LLMs (so far)</a></li>
<li><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/">2026 in LLMs (so far) - simonwillison.net</a></li>
<li><a href="https://simonwillison.net/tags/coding-agents/">Simon Willison on coding-agents</a></li>

</ul>
</details>

**标签**: `#LLMs`, `#AI trends`, `#annotated talk`, `#Simon Willison`, `#2026 retrospective`

---

<a id="item-tech-news-2"></a>
### [函数梯度下降结合自适应表示获 NeurIPS 接收](https://i.redd.it/wom07k9ih9sh1.gif) ⭐️ 7.0/10

一篇由第一作者在 Reddit 发布的帖子宣布，论文《Functional Gradient Descent with Adaptive Representations》已被 NeurIPS 接收。作者指出，函数梯度下降算法通常优于神经网络，但因函数梯度是无限维的、实践中必须近似，朴素近似会导致收敛到错误位置。为此，他们形式化了一类广泛的近似方案，称为“自适应表示”，并声称这些方案可证明收敛到全局最优解，同时可直接实现。作者称，由此得到的算法在多种设置下常比对应的神经网络性能高出一个数量级，并认为这条研究路线仍有很大潜力，论文链接为 arXiv:2606.16926。评论中有人提醒，全局最优性声明需要补充 Polyak-Lojasiewicz 等功能凸性条件。

reddit · r/MachineLearning · dccsillag0 · 9月28日 13:23 · [社区讨论](https://www.reddit.com/r/MachineLearning/comments/1wsejb7/functional_gradient_descent_with_adaptive/)

**「背景」** 函数优化问题通常通过优化固定表示（如神经网络）的参数来求解，这会产生高度非凸的损失，使训练和理论分析都变得复杂。另一条路线是函数梯度下降（FGD），即直接在函数空间中进行梯度下降，它具有较强的收敛结果和干净的理论。但函数梯度是无限维的，实践中必须加以近似，而朴素近似会导致收敛到错误的位置；该论文正是将一类近似方案形式化为“自适应表示”，以在可立即实现的同时保证收敛。

**「影响」** 对机器学习和优化研究者而言，该工作提供了可实现的函数梯度下降近似框架，并声称在多种设置下相对对应神经网络常有一个数量级的性能优势，但其全局最优性结论仍受 Polyak-Lojasiewicz 等功能凸性条件限制。

**「社区讨论」** 评论整体正面，认为该想法新颖且让人联想到 PDE 求解器中的自适应细化；同时有人追问局限性、是否只适合低维场景，以及它是否属于比 AdamW、Muon 更好的新型优化器。一位评论者特别指出，介绍中的全局最优性声明需要补充 Polyak-Lojasiewicz 等功能凸性条件，否则会误导非凸全局优化研究者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.16926">[2606.16926] Functional Gradient Descent with Adaptive Representations</a></li>
<li><a href="https://arxiv.org/html/2606.16926v1">Functional Gradient Descent with Adaptive Representations</a></li>
<li><a href="https://bytez.com/docs/arxiv/2606.16926/paper">Bytez</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#optimization`, `#functional gradient descent`, `#neural networks`, `#NeurIPS`

---