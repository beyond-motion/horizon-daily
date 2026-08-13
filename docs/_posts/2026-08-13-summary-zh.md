---
layout: default
title: "Horizon Summary: 2026-08-13 (ZH)"
date: 2026-08-13
lang: zh
---

> 从 5 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [DRAM 利用技术发布：或可深度攻破 AMD 老架构](#item-tech-news-1) ⭐️ 8.0/10
2. [City2Graph：将城市地理数据转为异构图神经网络的 Python 库](#item-tech-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [DRAM 利用技术发布：或可深度攻破 AMD 老架构](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 8.0/10

安全研究员 Christopher Domas（GitHub 用户 xoreaxeaxeax）发布了名为 skitter-creek-bath-salts 的 DRAM 利用技术，展示了在 DRAM 层面绕过或突破 CPU 保护边界的攻击面，可能实现深度系统入侵。该项目通过逆向内存控制器寄存器实现，目前确认针对较老的 AMD 低功耗架构 AMD16h（如 2013 年的 Jaguar）；README 同时提到 Zen 3 的内存控制器基址不同，因此新平台是否受影响尚不确定。研究人员还计划在 Black Hat 大会上做配套演讲。该工作表明 DRAM 本身已成为巨大的攻击面，尤其对已经获得 ring 0 权限的攻击者而言，可能进一步打开原本隐藏在“负环”中的硬件资源。

hackernews · matt\_d · 8月13日 14:17 · [社区讨论](https://news.ycombinator.com/item?id=49286341)

**「背景」** DRAM 控制器在现代 CPU 中负责管理内存访问，并可能使用地址加扰（address scrambling）等技术来隐藏物理布局。安全研究员 Christopher Domas 公开了名为“skitter-creek-bath-salts”的项目，针对 AMD Family 16h（Jaguar，2013 年的低功耗架构）的 DRAM 控制器：通过翻转一个配置位，可将物理地址重定向，从而让运行在 ring 0 的代码访问 CPU 上原本被隐藏的资源，如 PSP、C6 状态、微码和 SMM 等。该研究利用“DRAM 加扰”机制打开了超出普通内核权限的“负 ring”攻击面，并在 Black Hat 大会上进行配套演讲。

**「影响」** 对于使用 AMD Jaguar 等受影响架构的系统，一旦攻击者获得 ring 0 权限，就可能利用该技术继续突破硬件保护，影响固件安全研究和主机安全团队；但新 CPU 的实际受影响范围仍缺少公开证据，需要等待作者后续的 Black Hat 分享。

**「社区讨论」** 评论者普遍期待 Black Hat 配套演讲，并称赞 Christopher Domas 的逆向工程讲解能力；也有用户感叹现代 DRAM 的复杂性和专有二进制固件扩大了攻击面。与此同时，关于影响范围存在疑问：有评论指出 README 只确认 AMD Jaguar，并提到 Zen 3 基址不同，因此无法确定攻击在哪些新 CPU 上有效；另有评论推测 Xbox 和 PlayStation 的安全团队可能会对此感到紧张。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/xoreaxeaxeax/skitter-creek-bath-salts">GitHub - xoreaxeaxeax/ skitter - creek - bath - salts : Unlocking...</a></li>

</ul>
</details>

**标签**: `#hardware-security`, `#DRAM`, `#exploitation`, `#reverse-engineering`, `#systems`

---

<a id="item-tech-news-2"></a>
### [City2Graph：将城市地理数据转为异构图神经网络的 Python 库](https://www.reddit.com/gallery/1vn8oya) ⭐️ 7.0/10

City2Graph 是一个新发布的 Python 库，用于将地理空间城市数据转换为异构图，以支持空间分析、网络分析和图神经网络（GeoAI）。该库支持从 OpenStreetMap、Overture Maps、GTFS、GBFS 等数据源构建形态、交通、出行、邻近性和连通性图，并能与 PyTorch Geometric 的 Data/HeteroData 直接互转，同时支持与 NetworkX 和 rustworkx 的相互转换。其描述论文已正式发表，项目已公开在 GitHub 上。该工具为城市数据分析与图学习之间提供了实用的桥梁。

reddit · r/MachineLearning · Tough\_Ad\_6598 · 8月13日 11:59 · [社区讨论](https://www.reddit.com/r/MachineLearning/comments/1vn8oya/city2graph_a_python_library_for_heterogeneous/)

**「背景」** 图神经网络（GNN）是一种直接在图上进行机器学习的模型，而城市系统数据（如建筑、街道、交通站点）天然可以建模为节点和边；传统做法常将不同要素强行压入单一同构图，但城市中要素类型多样，异构图能更自然地表达建筑、街道、公交线路等不同实体及其关系。City2Graph 正是为此设计的开源 Python 库，可将 OpenStreetMap、Overture Maps、GTFS、GBFS 等地理空间数据转换为异构图，并通过保留几何与属性的转换函数输出到 PyTorch Geometric 的 Data/HeteroData，用于空间分析和 GeoAI 任务（例如用 GraphSAGE 等模型推断城市功能区）。其文档和示例展示了形态学图构建、多种邻近/连通性定义以及同构/异构训练管线。

**「影响」** 对城市数据科学家和 GNN 研究者而言，City2Graph 降低了将真实城市数据用于异构图神经网络的门槛，并提供了与 PyTorch Geometric 的直接集成，可加速 GeoAI 原型开发。

**「社区讨论」** 社区反响热烈，多数评论表示赞赏，认为将城市建模为异构图比统一图结构更自然；也有用户请求用更简单的解释，另有人称其为今年看到的最佳库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://livrepository.liverpool.ac.uk/3199917/">City 2 Graph : A Python library for Heterogeneous Graph Neural ...</a></li>
<li><a href="https://hrgpt.in/ai_news/a-coding-implementation-on-spatial-graph-neural-networks-for-urban-function-inference-using-city2graph-osmnx-and-pytorch-geometric/">A Coding Implementation on Spatial Graph Neural Networks ... - hrgpt.in</a></li>
<li><a href="http://city2graph.net/api/morphology.html">Morphology — GeoAI with Graph Neural Network (GNN) in Python</a></li>

</ul>
</details>

**标签**: `#geospatial`, `#graph-neural-networks`, `#urban-computing`, `#python`, `#open-source`

---