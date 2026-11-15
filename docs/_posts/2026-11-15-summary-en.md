---
layout: default
title: "Horizon Summary: 2026-11-15 (EN)"
date: 2026-11-15
lang: en
---

> From 3 items, 2 important content pieces were selected

---

**Technology News**
1. [Meta FAIR/NYU ablation finds vision-only parameters matter more than encoder pretraining](#item-tech-news-1) ⭐️ 8.0/10
2. [Open-source CUDA tuner claims 5x faster pageable copies on B300](#item-tech-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Meta FAIR/NYU ablation finds vision-only parameters matter more than encoder pretraining](https://www.reddit.com/r/MachineLearning/comments/1xx1k2o/meta_fair_nyu_unbundling_multimodal_vision/) ⭐️ 8.0/10

A Meta FAIR and NYU study trained more than 200 multimodal LLMs from scratch on the same data, with encoder pretraining charged to the same lifetime-compute budget, to separate three choices usually bundled in a vision encoder: separate pretraining, vision-only parameters, and placement before the LLM. The main comparisons used Qwen3-1.7B and 4B backbones with 0.4B parameters of vision capacity, a 0.6B–6.4B scaling ladder, 16 VQA benchmarks from Cambrian at 448 px, and 12 language benchmarks. Separate encoder pretraining was optional: four pretraining objectives at best tied a from-scratch encoder at matched compute, and even free pretraining did not help VQA, while pretraining MetaCLIP 6.5x longer raised ImageNet linear-probe accuracy from 80.4% to 84.4% but not VQA. Vision-only parameters were required—encoder-free models trailed at every size from 0.6B to 6.4B and needed about 3x compute to catch up, whereas giving the LLM the encoder&\#x27;s parameters improved text, not VQA—and placement before the LLM was optional: in-fusion zero-initialized vision-only weights in the first eight layers matched the encoder from 1.7B to 6.4B, cut time to first token by about 13%, and at 1.7B reached 45.0 VQA versus 44.4 for an encoder and 42.3 when text shared the weights. The Reddit post is an author summary whose content appears truncated, limiting assessment of the full methodology.

reddit · r/MachineLearning · /u/trungh98 · Nov 15, 17:38

**「Background」** Multimodal LLMs normally combine a language model with a vision encoder, often a CLIP-style network pretrained on image-text pairs, whose outputs are projected into the LLM. That standard recipe entangles three separate choices: separate encoder pretraining, parameters used only for vision tokens, and placing the encoder before the LLM. Published systems differ on these choices, but comparisons across models are confounded by differences in training data and compute budgets.

**「Impact」** Developers designing multimodal LLMs can treat separate vision-encoder pretraining and pre-LLM encoder placement as optional, but should budget dedicated vision-only parameters, since encoder-free designs may need roughly 3x compute to match.

<details><summary>References</summary>
<ul>
<li><a href="https://www.alphaxiv.org/">Explore | alphaXiv</a></li>

</ul>
</details>

**Tags**: `#multimodal LLMs`, `#vision encoders`, `#model pretraining`, `#empirical ablation`, `#model scaling`

---

<a id="item-tech-news-2"></a>
### [Open-source CUDA tuner claims 5x faster pageable copies on B300](https://www.reddit.com/r/MachineLearning/comments/1xx2n25/making_cudamemcpy_5x_faster_on_a_b300_p/) ⭐️ 7.0/10

A new open-source tool, cudamemcpy-tuner, claims to speed up pageable cudaMemcpy transfers on an NVIDIA B300. In a benchmark copying a 1 GB uint8 tensor from CPU to GPU and back with PyTorch, the reported CPU-to-GPU throughput rose from 10.2 GB/s to 51.5 GB/s, about 5x, after running \`cmt tune -- python bench.py\`. The author links a technical blog and GitHub repository, positioning the tuner as a way to improve a common memory-transfer bottleneck for GPU and ML workloads. The result is a single-project benchmark without independent validation, so the 5x claim should be treated as promising but not yet broadly verified.

reddit · r/MachineLearning · /u/makneeee · Nov 15, 18:20

**「Background」** CUDA host memory is pageable by default, and copying it to the GPU with cudaMemcpy requires the driver to first move the data through an internal pinned buffer, which adds overhead. Pinned host memory uses the same cudaMemcpy syntax but avoids that staging step, making it the standard technique for improving CPU-to-GPU transfer throughput.

**「Impact」** Developers and ML engineers moving pageable CPU tensors to GPUs on an NVIDIA B300 could see roughly 5x higher copy throughput \(10.2 to 51.5 GB/s\) if they adopt this open-source tuner, though the figure comes from a single project&\#x27;s own benchmark without independent validation.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/how-optimize-data-transfers-cuda-cc/">How to Optimize Data Transfers in CUDA C/C++ | NVIDIA Technical...</a></li>
<li><a href="https://jinseok-moon.github.io/p/pinned-memory/">Pageable vs. pinned data transfer | Jinseok Moon</a></li>

</ul>
</details>

**Tags**: `#CUDA`, `#GPU memory transfer`, `#performance optimization`, `#PyTorch`, `#open source tools`

---