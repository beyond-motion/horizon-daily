---
layout: default
title: "Horizon Summary: 2026-11-13 (ZH)"
date: 2026-11-13
lang: zh
---

> 从 7 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [TorchTitan 在 384 块 GH200 上训练约 1T MoE](#item-tech-news-1) ⭐️ 8.0/10
2. [逆向工程 Coway 空气净化器以摆脱云端依赖](#item-tech-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [TorchTitan 在 384 块 GH200 上训练约 1T MoE](https://www.reddit.com/r/MachineLearning/comments/1xvce5h/scaling_to_1t_moe_on_torchtitan_p/) ⭐️ 8.0/10

一位实践者分享了将 TorchTitan/PyTorch 扩展到约 1 万亿参数 MoE 的训练报告：在 384 块 GH200 上达到每 GPU 约 1,300 tokens/s，较起点提升 14 倍，但该结果来自作者自述的工程案例。其方案采用 384 路 FSDP 加 4 路专家并行，并把专家并行限制在节点内；放弃流水线并行是为了避免大量微批带来的长步时和慢迭代，而在 JUPITER 上 InfiniBand 每 GPU 约 25 GB/s，基线单步 84 秒中有 68 秒耗在网络等待。为填补空闲算力，作者使用全量激活检查点带来 4 倍提升、经 900 GB/s C2C 链路把检查点卸载到 Grace、并改用 Muon 优化器将序列长度推到 64k；FlexShard 按完整专家分片让 Newton-Schulz 本地执行，GPU 版 Newton-Schulz 修复把优化器步从 42 秒降到约 2 秒并提升 35% 吞吐。其他优化包括按注意力成本分桶使最慢 rank 从平均的 7.9 倍降到 1.15 倍（+13%）、组限制路由带来 +7% 但对训练质量影响尚无定论、专家梯度改用 bf16 all-to-all 后在本地以 fp32 累加，以及 FP8 专家 all-gather（+18%）和节点内 dense 权重重分片。作者还发现缓存分配器按 CUDA 流分池导致约 21 GiB 显存滞留在侧流，通过 FSDP2 的 unshard\_async\_op 等修复后分配重试从 384 个 rank 降为零、峰值保留显存减少 13.5 GiB、吞吐提升 21%；整体表明共享的 Hopper 机器在普通用户权限下也能承载前沿规模训练，但仍受节点间带宽制约。

reddit · r/MachineLearning · /u/f14-bertolotti · 11月13日 16:28

**「背景」** TorchTitan 是 PyTorch 原生的大规模训练代码库，可在同一套模型代码中组合 FSDP、专家并行等多种并行策略。MoE（混合专家）让每个 token 只路由到少量专家，从而扩大总参数量；因此，1T 参数模型仍必须跨多张 GPU 切分权重和专家。JUPITER 是采用 GH200 的欧洲公共超算，其节点内 NVLink 与节点间 InfiniBand 的带宽差距很大，使跨节点通信成为这类训练的主要约束。

**「影响」** 对在 GH200/Hopper 集群上使用 TorchTitan 的团队，这些结果表明优先优化节点间通信、采用整专家分片并修复侧流分配，能直接转化为吞吐提升；相关 unshard\_async\_op 修复正推进为公开 API。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pytorch.org/blog/training-a-1t-parameter-moe-on-eu-public-infrastructure-with-pytorch-and-torchtitan/">Training a 1T-Parameter MoE on EU public ... - PyTorch</a></li>
<li><a href="https://github.com/pytorch/torchtitan">GitHub - pytorch/torchtitan: A PyTorch native platform for ...</a></li>

</ul>
</details>

**标签**: `#distributed training`, `#mixture-of-experts`, `#PyTorch`, `#GPU scaling`, `#FSDP/expert parallelism`

---

<a id="item-tech-news-2"></a>
### [逆向工程 Coway 空气净化器以摆脱云端依赖](https://scottjg.com/posts/2026-11-11-reverse-engineering-my-coway-air-purifier-to-ditch-the-cloud/) ⭐️ 7.0/10

作者 scottjg 发布文章，记录自己如何逆向工程一台 Coway 空气净化器，目标是用本地控制取代对云端的依赖。文章围绕设备逆向工程和本地接管展开，属于个人项目，而非厂商发布的产品或安全公告。目前可见信息未披露具体型号、固件版本、通信协议和实现步骤，因此这些技术细节无法核实。该项目的意义在于呈现智能家居设备在隐私、可控性和断网可用性上的取舍，并引发了关于 IoT 安全弱点和 LLM 辅助逆向的讨论。

hackernews · scottjg · 11月12日 22:03 · [社区讨论](https://news.ycombinator.com/item?id=50474959)

**「背景」** Coway Airmega IconS 这类智能空气净化器通常依赖厂商云服务与手机 App 通信，用户若想接入 Home Assistant 或实现本地自动化，往往需要绕过云端。逆向这类设备的一种常见路径是中间人拦截：让设备连接受控 Wi-Fi，再通过代理观察和篡改其 TLS 流量，因此设备如何获取和信任根证书成为关键切入点。近年来，LLM 被用来加速协议分析、脚本编写和嵌入式配置，降低了硬件逆向与“去云化”改造的门槛。

**「影响」** 对 Coway 空气净化器的用户来说，这个项目提供了一个可行路径：用本地控制替代云端依赖，代价是需要自己完成硬件和固件层面的逆向工作；而固件通过明文 HTTP 下载根 CA 证书这一细节也说明，这类设备本来就存在中间人攻击面。LLM 辅助只是降低了逆向的门槛，并不能修复设备端本身的信任缺陷。

**「社区讨论」** 有评论指出，该风扇通过明文 HTTP 下载根 CA 证书，长期存在被中间人攻击的风险，并认为 LLM 正在降低逆向工程中繁琐环节的门槛；也有人分享用 ESP32 和 ESPHome 接管海尔空调、给净化器接线实现本地控制等经验，并讨论 Corsi-Rosenthal 箱式风扇、中央 HVAC 等替代方案。整体看，讨论肯定本地控制的实用价值，但对具体设备的安全设计和替代方案仍有不同侧重。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://daily.dev/posts/reverse-engineering-my-coway-air-purifier-to-ditch-the-cloud-mpuska7qb">Reverse Engineering My Coway Air Purifier to Ditch the Cloud</a></li>
<li><a href="https://www.machucavalley.tech/blog/reverse-engineering-coway-air-purifier-declouding/">Breaking the Tether: Why I Reverse Engineered My Coway Air ...</a></li>
<li><a href="https://zeli.app/story/50474959">Hacker Cuts Coway Air Purifier · 29 HN comments | Zeli</a></li>

</ul>
</details>

**标签**: `#reverse engineering`, `#IoT security`, `#smart home`, `#local control`, `#LLM-assisted development`

---