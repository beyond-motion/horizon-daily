---
layout: default
title: "Horizon Summary: 2026-09-20 (ZH)"
date: 2026-09-20
lang: zh
---

> 从 5 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [Qwen Image 2.1：7B 开放权重、文本渲染提升但许可更严](#item-tech-news-1) ⭐️ 7.0/10
2. [交互式演示：ReLU 网络如何学习不同函数](#item-tech-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Qwen Image 2.1：7B 开放权重、文本渲染提升但许可更严](https://qwen.ai/blog?id=qwen-image-2.1) ⭐️ 7.0/10

Qwen Image 2.1 发布，是一款开放权重文生图模型，参数量约 7B，明显小于 Qwen-Image 1 的 20B；在开放权重模型中属于较小的一档，已知 Z-Image Turbo 约 6B 仍更小。评论者称其亮点包括原生透明度支持与文本渲染改进，有开发者用自建测试框架将它与 gpt-image-2 对比，认为其文本渲染远好于当前其他开放权重模型，小字号文本保真度也不错。但该项目采用了比此前部分 Qwen 模型（如 Apache 许可）更严格的许可证，成为主要争议与使用限制。目前公告缺少深入技术细节，实际能力、许可范围和本地运行方式仍需以官方资料和实测为准。

hackernews · jmillikin · 9月20日 13:09 · [社区讨论](https://news.ycombinator.com/item?id=49775499)

**「背景」** Qwen 是阿里巴巴旗下的模型系列，此前已推出 Qwen-Image 系列文本到图像模型：Qwen-Image 1 拥有 200 亿参数，而 Qwen-Image 2.0 于 2026 年 2 月发布，具备原生 2K 输出、透明图像、高质量文字渲染与编辑能力。开源权重图像模型长期以来在图像内文字渲染方面弱于闭源商业模型，原生透明背景支持也较为罕见，因此这两点成为评价新模型时的关键参照。此外，以往多数 Qwen 模型采用 Apache 等相对宽松的许可，许可证条款的松紧是该社区持续关注的背景因素。

**「影响」** 对图像生成开发者而言，7B 的规模加上 ComfyUI 第 0 天原生支持、Hugging Face 可下载权重以及 vLLM-Omni 路径，使本地部署的门槛明显降低，而更强的文本渲染与原生透明度直接利好提示词转 UI 等设计类工作流。不过该模型采用的许可证较此前 Qwen 系列更为严格，商业使用与再分发可能受限。

**「社区讨论」** 讨论中的主要共识是文本渲染和原生透明度对开放权重模型很有吸引力，本地生成图像质量也令人印象深刻，甚至有人认为本地图像生成目前比本地代码生成更领先；主要担忧是新许可证比一些旧 Qwen 模型更严格，另有用户询问如何在本地像 llama-server 一样部署该模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/QwenLM/Qwen-Image-2.1">GitHub - QwenLM/Qwen-Image-2.1: Qwen&#x27;s most powerful open ...</a></li>
<li><a href="https://blog.comfy.org/p/qwen-image-21-in-comfyui-open-weight">Qwen-Image-2.1 in ComfyUI: Open-Weight Image Generation and ...</a></li>
<li><a href="https://kie.ai/blog/what-is-qwen-image-2-1">What Is Qwen - Image - 2 . 1 ? Native 2K Editing</a></li>
<li><a href="https://www.orcarouter.ai/blog/qwen-image-2-1-vs-flux-3">Qwen - Image 2 . 1 vs FLUX 3: two image models you can&#x27;t use</a></li>
<li><a href="https://github.com/QwenLM/Qwen-Image-2.1">QwenLM/ Qwen - Image - 2 . 1 : Qwen &#x27;s most powerful open -source image ...</a></li>

</ul>
</details>

**标签**: `#Qwen`, `#text-to-image`, `#open-weight models`, `#generative AI`, `#licensing`

---

<a id="item-tech-news-2"></a>
### [交互式演示：ReLU 网络如何学习不同函数](https://i.redd.it/cwnmw2lc7kqh1.gif) ⭐️ 7.0/10

Reddit 用户 microscope1024 发布了一个交互式神经网络演示，让用户可以更改网络架构以及网络尝试逼近的目标函数，并附上博文与演示链接 https://blog.lukesalamone.com/posts/can-a-neural-net-learn。作者指出，带 ReLU 激活的全连接网络会生成分段线性函数；单隐藏层可产生的最大分段数为 1 加上该层宽度，例如输入“3”时最多有 4 段。若再添加一个隐藏层，最大分段数会相乘，因此“3 3”最多为 4×4=16 段，但训练后网络很少达到这一上限。该帖在社区中获得了积极反馈，多位评论者认为它对理解函数逼近和网络容量很有教学价值。

reddit · r/MachineLearning · microscope1024 · 9月19日 23:12 · [社区讨论](https://www.reddit.com/r/MachineLearning/comments/1wl0l7j/i_wanted_to_watch_a_neural_network_learn_p/)

**「背景知识」** ReLU（修正线性单元）是神经网络中最常用的激活函数之一，其输出由若干直线段拼接而成，因此全连接 ReLU 网络的整体输出必然是一个分段线性函数，可表达的“折线段”数量受各层宽度限制。按该帖给出的规律，单个隐藏层宽度为 w 时最多产生 w+1 个线性分段，若再接一个隐藏层则最大分段数按各层上限相乘（如“3 3”理论上可达 4×4=16 段），但实际训练后网络很少达到这一上限。历史上隐藏层的核心价值最早体现在 XOR 这类线性不可分问题上：单层感知机无法拟合，加入隐藏层后才能给出正确映射，而可交互的架构与激活函数实验（如 Google 的神经网络互动练习与各类神经网络可视化玩具）长期被用作教学工具。

**「影响」** 对机器学习学习者和教师而言，这个演示把隐藏层宽度与深度同可学习分段数的关系具体化，可作为课堂或自学中理解 ReLU 网络表达能力的直观工具。

**「社区讨论」** 评论总体认可其教学价值，有人称会用于向学生展示神经网络，也有人表示自己早年学习时缺少这类直观示例；同时有人指出帖子下存在无端负面评论并为其辩护。讨论还建议增加 L1/L2 或 dropout 可视化，以观察稀疏性、彩票假说和局部最小值等现象，并提到单层无法学习 XOR、加入隐藏层后才可解决的经典例子。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.google.com/machine-learning/crash-course/neural-networks/interactive-exercises">Neural networks: Interactive exercises | Machine Learning | Google for Developers</a></li>
<li><a href="https://nnplayground.com/">Neural network visualized</a></li>

</ul>
</details>

**标签**: `#neural networks`, `#interactive visualization`, `#machine learning education`, `#function approximation`, `#ReLU networks`

---