---
layout: default
title: "Horizon Summary: 2026-11-10 (ZH)"
date: 2026-11-10
lang: zh
---

> 从 7 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [DeepMind 发布 AlphaProof Code 形式化验证代理](#item-tech-news-1) ⭐️ 8.0/10
2. [Blender 5.3 发布，新增高斯泼溅支持](#item-tech-news-2) ⭐️ 7.0/10
3. [SWE-Pair：一次修复两个真实 Bug 的编码智能体基准](#item-tech-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [DeepMind 发布 AlphaProof Code 形式化验证代理](https://deepmind.google/blog/introducing-alphaproof-code/) ⭐️ 8.0/10

DeepMind 发布博客介绍 AlphaProof Code，一个用于代码形式化验证的 AI 代理；目前可获得的原文细节有限，其具体方法、基准和验证范围尚无法核实。该工具尝试让 AI 生成形式化证明，而不仅是生成代码，因而在 Hacker News 引发“证明到底证明了什么”的讨论。争论焦点是：验证是否只证明实现符合给定规格，却不检验规格本身，以及“零 bug”结论是否可信。有评论者以一个有 bug 历史的非平凡人工编写库为例，怀疑定理写错或只证明了窄性质；也有人追问它与普通编码代理迭代编写 Lean 或 Rocq 代码的区别。还有实践者提醒，AI 写 Lean 并不完美，可能“作弊”。

hackernews · ilreb · 11月10日 12:11 · [社区讨论](https://news.ycombinator.com/item?id=50439193)

**「背景」** 形式化验证是用数学规范描述程序应满足的性质，再用机器可检验的证明来确认实现符合规范，而不只是依赖测试覆盖。DeepMind 的 AlphaProof Code 是一个多智能体 AI 框架，用于形式化软件规范与验证，并以 libsignal（Signal 协议的参考实现）为案例，在机器码层面证明其关键安全属性。为检验系统能否区分正确与有缺陷的代码，团队在隔离版 Signal 代码中重新引入两个此前已修复的真实漏洞，系统均生成了“有漏洞版本不安全”的机器检验证明；此前形式化验证通常集中在较小的代码范围，这次则尝试覆盖更大的真实代码库。

**「影响」** 对使用 Lean、Rocq 等证明助手做代码验证的开发者而言，若该代理只证明实现符合给定规格，而不检验规格本身，那么规格错误仍会漏过，“零 bug”结论也不能等同于系统无缺陷。

**「社区讨论」** 评论中既有对 AI 辅助形式化验证方向的肯定，也有对结论可信度的强烈质疑：hedora 怀疑“零 bug”源于定理写错或只证明窄性质，thibsrn 追问其与普通编码代理的区别，r0ze-at-hn 提醒 AI 写 Lean 可能“作弊”，andai 则举例称编码代理曾在测试全绿的情况下把重构做反。Mizza 则预计两三年内运行未验证软件会像今天使用明文 HTTP 一样显得不可接受。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/blog/introducing-alphaproof-code/">Formal Verification of Signal’s Protocol with... — Google DeepMind</a></li>
<li><a href="https://google-deepmind.github.io/code-verification/">AlphaProof Code : Verifying Signal’s Security at the Machine- Code ...</a></li>
<li><a href="https://www.wired.com/story/a-new-ai-tool-from-google-deepmind-formally-verified-the-signal-protocol/">A New AI Tool From Google DeepMind Proved the Signal... | WIRED</a></li>

</ul>
</details>

**标签**: `#formal verification`, `#AI for code`, `#DeepMind`, `#Lean`, `#program verification`

---

<a id="item-tech-news-2"></a>
### [Blender 5.3 发布，新增高斯泼溅支持](https://www.blender.org/download/releases/5-3/) ⭐️ 7.0/10

开源 3D 创作套件 Blender 发布 5.3 版本，新增 Gaussian Splat（高斯泼溅）支持，并带来几何节点中的 Bundle 功能改进。该更新把高斯泼溅纳入主流开源建模与动画工具，对图形及 AI 相关工作流具有现实意义。社区评论称高斯泼溅集成成熟、在 Apple 硬件上速度快，包含 400 万 splats 的场景也能正常使用；几何节点 Bundle 与列表、闭包结合后，被认为对复杂管线和工作流帮助很大。上述性能与成熟度目前主要来自用户试用反馈，尚缺少可比的量化数据。

hackernews · amlib · 11月10日 16:15 · [社区讨论](https://news.ycombinator.com/item?id=50442426)

**「背景」** 3D Gaussian Splatting 是一种把场景表示为大量三维高斯点、通常从照片重建并在新视角下渲染的技术。Blender 是开源三维创作套件，5.3 将 3D Gaussian Splat 作为原生能力引入：可从 PLY 和 SPZ 文件导入，并可在 Workbench、EEVEE 和 Cycles 中渲染，但目前尚不支持导出。几何节点（Geometry Nodes）是 Blender 的程序化工作流系统，此次更新中的 bundle 等能力面向复杂管线中的数据组织与复用。

**「影响」** 对从事实景捕捉和视觉特效的 Blender 用户来说，5.3 原生支持高斯泼溅的导入、编辑与渲染，意味着以往需要在多个外部工具之间来回切换的扫描场景流程，现在可以集中到 Blender 内部完成；不过官方把这一能力定位为初步实现，并表示后续仍有开发计划。

**「社区讨论」** 评论整体持积极态度：有用户称在 M4 上试用包含 400 万 splats 的场景时，集成成熟、速度快且界面一致，也有人认为几何节点 Bundle 配合列表和闭包显著简化了复杂管线，但学习门槛不低。讨论中还出现对三角形泼溅等替代路线的兴趣，以及对 Blender 捐款支持的呼吁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.blender.org/download/releases/5-3/">5 . 3 — Blender</a></li>
<li><a href="https://80.lv/articles/blender-5-3-is-getting-native-3d-gaussian-splat-support">Blender 5 . 3 Is Getting Native 3D Gaussian Splat Support</a></li>
<li><a href="https://code.blender.org/2026/10/splatting-the-gaussians-into-blender/">Splatting the Gaussians into Blender — Blender Developers Blog</a></li>
<li><a href="https://zgian.com/blender-5-3-gaussian-splatting-vfx/">Blender 5.3 Gaussian Splatting: New VFX Tools - zgian.com</a></li>

</ul>
</details>

**标签**: `#Blender`, `#Gaussian Splatting`, `#3D graphics`, `#open source`, `#geometry nodes`

---

<a id="item-tech-news-3"></a>
### [SWE-Pair：一次修复两个真实 Bug 的编码智能体基准](https://www.reddit.com/r/MachineLearning/comments/1xsuqem/swepair_a_codingagent_benchmark_where_every_task/) ⭐️ 7.0/10

Reddit 用户发布 SWE-Pair 基准，包含来自 69 个 Python 项目的 161 个任务，每个任务要求编码智能体同时修复两个真实 Bug。帖子报告称，成本最低的组合排名最高：DeepSeek V4.1 Flash 在中等推理强度下解决 90% 任务，约每个已解决任务 6 美分；GPT-6 Luna 在最高推理强度下解决 78%，约 23 美分。提高推理强度并未带来收益：DeepSeek 在最高强度下得分为 88%，略低于中等强度，成本却高出 1.7 倍。任务数据集、全部智能体运行结果和 Harbor 运行命令均已公开，但这些结果来自项目发布方，尚非独立评测。

reddit · r/MachineLearning · /u/heyitsdannyle · 11月10日 18:33

**「背景」** 编码智能体基准通常用真实代码库中的修复任务来评估模型能否定位缺陷、修改代码并通过测试；例如 DeepSWE 以 113 个任务衡量编码智能体。SWE-Pair 延续这一思路，但把每个任务设计成同时修复两个真实 Python 缺陷，并用解决率和每个已解决任务的成本来衡量模型，因此能反映多缺陷调试与推理投入之间的取舍。该基准由 69 个 Python 项目中的 161 个任务组成，并公开数据集与运行记录以便复现。

**「影响」** 对正在选型编码智能体的开发者而言，该基准及其成本数据表明，提高推理强度未必更划算，应结合目标任务上的成功率与单位已解决任务成本来评估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://maxxbench.unlap.ai/research/coding-sandboxes/">DeepSeek V 4 . 1 Flash Uses a Network Bypass in... | MaxxBench</a></li>

</ul>
</details>

**标签**: `#coding agents`, `#benchmarks`, `#LLM evaluation`, `#software engineering`, `#cost efficiency`

---