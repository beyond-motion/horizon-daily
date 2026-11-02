---
layout: default
title: "Horizon Summary: 2026-11-02 (EN)"
date: 2026-11-02
lang: en
---

> From 8 items, 1 important content pieces were selected

---

**Technology News**
1. [Laptop-scale replication: paired captions beat next-token prediction](#item-tech-news-1) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Laptop-scale replication: paired captions beat next-token prediction](https://www.reddit.com/r/MachineLearning/comments/1xlzoze/smallscale_check_of_good_views_beat_nexttoken/) ⭐️ 7.0/10

A Reddit user ran a laptop-scale replication of Balestriero and LeCun&\#x27;s 2026 claim that training text models on &quot;good views&quot; \(two different captions of the same image\) aligns them to image models faster than bad views \(one caption with masked spans\) or next-token prediction, using human-written COCO captions instead of machine-generated ones to rule out image information leaking into the text. The setup used 10,000 COCO photos with five human captions each \(8,000 train, 1,000 validation, 1,000 test\), frozen DINOv2-base image embeddings computed once, and the same 4-layer, width-256, 11M-parameter text encoder for all three conditions, trained for 3,000 steps at batch 256 with a VICReg-style variance/covariance anti-collapse loss rather than the paper&\#x27;s SIGReg; only the training pairs differed, and the text models never saw an image. Scored by mutual 10-nearest-neighbor overlap between caption and DINOv2 embeddings on the 1,000 test photos \(chance 0.010\), good views reached 0.320 versus 0.192 for bad views and 0.148 for next-token prediction at the same learning speed \(mean of 3 seeds\), and a per-method learning-rate search with one seed gave 0.328 / 0.196 / 0.168 with the ordering unchanged. Retrieval \(R@1 with one fitted rotation\) showed a smaller gap of 0.084 versus 0.063 versus 0.057. The author notes limits: 11M parameters and 8,000 photos rather than the paper&\#x27;s 109M or 72B, good views require knowing which captions describe the same photo, a single dataset and image model, next-token prediction&\#x27;s best speed sat at the top of the searched range, and the extra speed step was added after seeing the first search, as noted in the repository.

reddit · r/MachineLearning · /u/Traditional\_Frame763 · Nov 2, 15:08

**「Background」** The Platonic representation hypothesis holds that models trained on different modalities or objectives can converge toward a shared representation of the world. In Balestriero and LeCun&\#x27;s October 2026 paper, &quot;good views&quot; are two observations of the same scene, as opposed to &quot;bad views&quot; made from parts of a single observation; the authors argue such paired views let joint-embedding predictive architectures \(JEPAs\) align modalities far more sample-efficiently than next-token prediction. Their headline experiments used a 109M-parameter text JEPA and reported stronger cross-modal alignment than language models up to 72B parameters, with good views needing roughly 42 times fewer training samples.

**「Impact」** For researchers tracking the good-views claim, this suggests the ranking survives at 11M parameters on human captions, but the much narrower retrieval gap and untested scaling leave open whether the advantage holds at the paper&\#x27;s 109M to 72B scales.

<details><summary>References</summary>
<ul>
<li><a href="https://aiweekly.co/editors-blog/found-first-lecun-proves-platonic-representation-hypothesis-good-views-need-42x">LeCun Proves Platonic Representation Hypothesis; Good Views ...</a></li>
<li><a href="https://emergent.sh/news/lecun-paper-proves-jepas-converge-same">LeCun Paper Proves JEPAs Converge to Same Representation</a></li>
<li><a href="https://news.lavx.hu/article/jepas-prove-platonic-representations-come-from-good-views-not-scale">JEPAs Prove Platonic Representations Come From Good Views ...</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#self-supervised-learning`, `#vision-language`, `#replication`, `#representation-learning`

---