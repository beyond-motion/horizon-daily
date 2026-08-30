---
layout: default
title: "Horizon Summary: 2026-08-30 (EN)"
date: 2026-08-30
lang: en
---

> From 4 items, 3 important content pieces were selected

---

**Technology News**
1. [Tencent&\#x27;s Hy4 Preview: 770B-Parameter Open-Weight LLM with 1M Context](#item-tech-news-1) ⭐️ 8.0/10
2. [100-year-old SPC beats SOTA time series anomaly detection on TSB-AD](#item-tech-news-2) ⭐️ 8.0/10
3. [EU Commission Revives Encryption Backdoor Push in ProtectEU Strategy](#item-tech-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Tencent&\#x27;s Hy4 Preview: 770B-Parameter Open-Weight LLM with 1M Context](https://simonwillison.net/2026/Aug/29/hy4/) ⭐️ 8.0/10

Tencent released Hy4 Preview, an open-weight text-only LLM with 770B total parameters, 49B active parameters, and a 1M-token context window. The model is available on Hugging Face as a 1.56TB download, a large jump from Tencent&\#x27;s July Hy3 release, which had 295B total parameters, 21B active parameters, 256K context, and a 598GB footprint. Its chat template exposes two reasoning-effort settings: &quot;high&quot; \(the default\) and &quot;no\_think&quot; \(reasoning disabled\). Simon Willison tested the default high-reasoning mode through OpenRouter with an SVG-generation prompt and observed a reasoning trace written in slightly truncated English, which he attributes to token efficiency in hidden reasoning text. The release matters as a major scale increase in open-weight models from a Chinese vendor, though it lacks vision input.

rss · Simon Willison · Aug 29, 23:53

**「Background」** Open-weight LLMs publish trained model weights so developers can download, fine-tune, and self-host them, unlike API-only models. The large gap between total and active parameters indicates a sparse or mixture-of-experts architecture that stores all parameters but activates only a subset per token, while the context window is the number of tokens the model can process at once. Tencent&\#x27;s Hy series are open-weight models hosted on Hugging Face, with Hy4 Preview following Hy3 from July.

**「Impact」** Developers and researchers can now experiment with a frontier-scale open-weight text model with a 1M-token context via Hugging Face or OpenRouter, but the 1.56TB size and text-only input constrain practical self-hosting and multimodal use.

**Tags**: `#LLM`, `#Tencent`, `#open-weights`, `#Hugging Face`, `#AI`

---

<a id="item-tech-news-2"></a>
### [100-year-old SPC beats SOTA time series anomaly detection on TSB-AD](https://www.reddit.com/r/MachineLearning/comments/1w1wt1s/you_can_beat_sota_time_series_anomaly_detection/) ⭐️ 8.0/10

Eamonn Keogh posted on r/MachineLearning that simple Statistical Process Control \(SPC\), a roughly 100-year-old method, can beat state-of-the-art time series anomaly detection \(TSAD\) methods on most datasets in Paparrizos&\#x27; TSB-AD-M benchmark, with perfect results on the shown ECG trace and even more trivial TAO traces. He argues the benchmark is too trivial to support meaningful claims and that much apparent progress in TSAD over the last decade is illusory. He says he has done 90% of the work to introduce more challenging TSAD problems, including sled dogs, Tuna, Fuel Cells, and Smart Manufacturing. The post is a critique of benchmark validity rather than a new method.

reddit · r/MachineLearning · eamonnkeogh · Aug 29, 20:16

**「Background」** TSB-AD is a widely used time-series anomaly detection benchmark that aggregates heterogeneous datasets from multiple domains and ranks methods by metrics such as average VUS-PR. Statistical process control \(SPC\) is a roughly century-old quality-control technique that monitors a process for deviations from expected behavior using control limits. Eamonn Keogh, a prominent researcher known for time-series methods such as DTW and the Matrix Profile, argues that simple SPC can outperform state-of-the-art TSAD methods on TSB-AD, suggesting the benchmark is too easy to support strong claims.

**「Impact」** The critique pressures TSAD researchers and reviewers to stop treating TSB-AD-M as a gold standard and to adopt harder benchmarks such as Keogh&\#x27;s proposed sled dogs, Tuna, Fuel Cells, and Smart Manufacturing datasets.

**「Community Discussion」** Commenters largely agreed, praising the direct benchmark check and noting the claim is not new \(citing arXiv:2009.13807\). Some also questioned whether TSAD is well-posed, asked what good benchmarks would be, and observed that similar issues appear beyond time series.

<details><summary>References</summary>
<ul>
<li><a href="https://thedatumorg.github.io/TSB-AD/">TSB-AD</a></li>
<li><a href="https://www.researchgate.net/publication/395274485_TSB-AutoAD_Towards_Automated_Solutions_for_Time-Series_Anomaly_Detection">TSB-AutoAD: Towards Automated Solutions for Time-Series Anomaly Detection | Request PDF</a></li>

</ul>
</details>

**Tags**: `#time series anomaly detection`, `#benchmarks`, `#statistical process control`, `#machine learning research`, `#TSB-AD`

---

<a id="item-tech-news-3"></a>
### [EU Commission Revives Encryption Backdoor Push in ProtectEU Strategy](https://reclaimthenet.org/eu-protecteu-strategy-encryption-backdoor-law-enforcement) ⭐️ 7.0/10

The European Commission has reportedly revived proposals for encryption backdoors in its ProtectEU strategy, according to Reclaim The Net. The renewed push for lawful access mechanisms has drawn concern from technologists who argue it would weaken security and privacy. The report frames the move as part of a broader EU security agenda, but the source is an advocacy outlet and the item lacks deep technical analysis. No official text or concrete implementation details were provided in the item.

hackernews · nickslaughter02 · Aug 30, 15:12 · [Discussion](https://news.ycombinator.com/item?id=49499394)

**「Background」** ProtectEU is the European Commission&\#x27;s internal security strategy, announced in June 2025, which includes a roadmap for &\#x27;effective and lawful access&\#x27; to encrypted data for law enforcement. The proposal revives a long-running debate over &\#x27;lawful access&\#x27; mechanisms, often described by critics as encryption backdoors, that would let authorities read end-to-end encrypted communications. The Commission says the roadmap follows recommendations from its High-Level Group on access to data, while more than 40 organisations have signed an open letter opposing the approach.

**「Community Discussion」** Commenters on Hacker News criticized the proposal, arguing the Commission already has excessive power and that Parliament cannot initiate legislation, allowing the Commission to repackage rejected ideas. Others warned that weakening encryption is especially dangerous amid AI security concerns and cited Cambridge Analytica as evidence of how diminished privacy can be exploited; one commenter expressed fear about being punished for refusing to allow authorities to read private messages.

<details><summary>References</summary>
<ul>
<li><a href="https://home-affairs.ec.europa.eu/policies/internal-security/lawful-access-data/encryption_en">Encryption - Migration and Home Affairs - European Commission</a></li>
<li><a href="https://reclaimthenet.org/eu-protecteu-strategy-encryption-backdoor-law-enforcement">EU&#x27;s ProtectEU Plan Renews Push for Encryption Backdoors</a></li>
<li><a href="https://opsecinsider.com/protecteu-encryption-roadmap/">ProtectEU Encryption Roadmap: EU Pushes Lawful Access</a></li>

</ul>
</details>

**Tags**: `#encryption`, `#EU policy`, `#privacy`, `#cybersecurity`, `#surveillance`

---