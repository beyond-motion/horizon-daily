---
layout: default
title: "Horizon Summary: 2026-11-13 (EN)"
date: 2026-11-13
lang: en
---

> From 7 items, 2 important content pieces were selected

---

**Technology News**
1. [Scaling TorchTitan to a 1T-Parameter MoE on 384 GH200 GPUs](#item-tech-news-1) ⭐️ 8.0/10
2. [Reverse-engineering a Coway purifier for local control](#item-tech-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Scaling TorchTitan to a 1T-Parameter MoE on 384 GH200 GPUs](https://www.reddit.com/r/MachineLearning/comments/1xvce5h/scaling_to_1t_moe_on_torchtitan_p/) ⭐️ 8.0/10

Over several months working with TorchTitan and PyTorch maintainers, the author scaled training of a roughly 1T-parameter mixture-of-experts model to about 1,300 tokens/s per GPU on 384 GH200 GPUs, a 14X improvement over their starting point. They chose 384-way FSDP plus 4-way expert parallelism kept inside each node, avoiding pipeline parallelism to shorten iteration time; on JUPITER, InfiniBand delivered about 25 GB/s per GPU, and their baseline 84-second step spent 68 seconds waiting on the network. Reported lessons include full activation checkpointing for a 4X gain, offloading checkpoint activations to Grace, using Muon to reach 64k-token sequences, and FlexShard whole-expert sharding so Newton-Schulz can run locally; moving Newton-Schulz to the GPU despite host-resident parameters cut the optimizer step from 42 seconds to about 2 seconds and raised throughput 35%. They also bucketed rows by attention cost to reduce the worst-rank imbalance from 7.9X to 1.15X average \(+13%\), used group-limited routing for +7% while noting its training impact is still uncertain, and replaced FP32 reduce-scatter with a bf16 expert-gradient all-to-all that matches the FP32 reduce-scatter up to summation order while halving bytes on the wire. FP8 expert all-gather with blockwise scales added 18%, and fixing a PyTorch caching-allocator side-stream issue eliminated allocator retries across all 384 ranks, reduced peak reserved memory by 13.5 GiB, and improved throughput 21%.

reddit · r/MachineLearning · /u/f14-bertolotti · Nov 13, 16:28

**「Background」** Mixture-of-experts \(MoE\) models increase parameter count by routing each token to only a subset of expert subnetworks, so only a fraction of the model is active per token. TorchTitan is PyTorch&\#x27;s native large-scale training platform, composing FSDP, which shards weights and gathers them just in time, with expert parallelism, which places experts on different GPUs and sends tokens to them; the EUROPA consortium used it to train a near-1T-parameter MoE on the public JUPITER supercomputer&\#x27;s GH200 GPUs. Because inter-node bandwidth is much lower than intra-node links, techniques such as FlexShard, activation offload, and communication overlap become central to performance.

**「Impact」** For ML systems engineers training large MoEs, the account provides concrete TorchTitan optimizations and failure modes—especially node-local expert parallelism, whole-expert sharding, GPU-side Muon, and allocator-stream debugging—that target InfiniBand bottlenecks on GH200 clusters.

<details><summary>References</summary>
<ul>
<li><a href="https://pytorch.org/blog/training-a-1t-parameter-moe-on-eu-public-infrastructure-with-pytorch-and-torchtitan/">Training a 1T-Parameter MoE on EU public ... - PyTorch</a></li>
<li><a href="https://github.com/pytorch/torchtitan">GitHub - pytorch/torchtitan: A PyTorch native platform for ...</a></li>

</ul>
</details>

**Tags**: `#distributed training`, `#mixture-of-experts`, `#PyTorch`, `#GPU scaling`, `#FSDP/expert parallelism`

---

<a id="item-tech-news-2"></a>
### [Reverse-engineering a Coway purifier for local control](https://scottjg.com/posts/2026-11-11-reverse-engineering-my-coway-air-purifier-to-ditch-the-cloud/) ⭐️ 7.0/10

A detailed write-up documents reverse-engineering a Coway air purifier to replace cloud dependency with local control. The project is presented as a practical way to ditch the cloud for a smart-home device. The discussion around it highlights broader IoT security weaknesses and the growing role of LLM-assisted development in making tedious device-hacking work more accessible.

hackernews · scottjg · Nov 12, 22:03 · [Discussion](https://news.ycombinator.com/item?id=50474959)

**「Background」** Coway&\#x27;s Airmega IconS normally relies on the vendor&\#x27;s cloud service for app and smart-home control, so an unreliable service or restricted account can leave owners without local access. The project relies on two concepts: a man-in-the-middle proxy intercepts traffic between the purifier and Coway&\#x27;s servers, and TLS trust depends on root certificates, making a device vulnerable if it downloads its root CA over plain HTTP and that certificate can be replaced. This fits a broader &quot;de-clouding&quot; effort to bypass manufacturer servers and control IoT devices locally.

**「Impact」** Owners of this Coway purifier model gain a documented, unofficial path to local control that removes the vendor cloud dependency, though it requires hands-on reverse-engineering rather than a supported feature.

**「Community discussion」** Commenters focused on how LLM-assisted reverse engineering exposes longstanding IoT weaknesses, with one noting that the fan downloads its root CA certificate over plain HTTP and was always vulnerable to man-in-the-middle attacks. Others shared practical alternatives and experiences, including a DIY Corsi-Rosenthal box, converting Haier AC ESP32 modules to ESPHome, and relying on central HVAC or other purifiers.

<details><summary>References</summary>
<ul>
<li><a href="https://daily.dev/posts/reverse-engineering-my-coway-air-purifier-to-ditch-the-cloud-mpuska7qb">Reverse Engineering My Coway Air Purifier to Ditch the Cloud</a></li>
<li><a href="https://www.machucavalley.tech/blog/reverse-engineering-coway-air-purifier-declouding/">Breaking the Tether: Why I Reverse Engineered My Coway Air ...</a></li>
<li><a href="https://zeli.app/story/50474959">Hacker Cuts Coway Air Purifier · 29 HN comments | Zeli</a></li>

</ul>
</details>

**Tags**: `#reverse engineering`, `#IoT security`, `#smart home`, `#local control`, `#LLM-assisted development`

---