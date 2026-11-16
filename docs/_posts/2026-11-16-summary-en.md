---
layout: default
title: "Horizon Summary: 2026-11-16 (EN)"
date: 2026-11-16
lang: en
---

> From 9 items, 1 important content pieces were selected

---

**Technology News**
1. [Marimba: Frozen ASR Encoder for Calibrated Speech Queries](#item-tech-news-1) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Marimba: Frozen ASR Encoder for Calibrated Speech Queries](https://www.reddit.com/r/MachineLearning/comments/1xxsqro/marimba_a_system_one_model_for_speech_r/) ⭐️ 7.0/10

Marimba is a speech-query model introduced in a follow-up paper \(arXiv:2611.18330\) that answers typed questions about an 8-second audio window with calibrated probabilities, using one frozen Qwen3-ASR-0.6B encoder pass for all question types. Term spotting is zero-shot from the decoder&\#x27;s greedy and four beam hypotheses and then Platt-calibrated, while language, turn-end, speaker-change, and speaker-count tasks use the ASR model&\#x27;s own scores or small readouts on frozen layers. On the same 1,000 public questions, Marimba matches or beats Qwen3-Omni \(30B-A3B\) on 6 of 9 tests, though Qwen3-Omni remains better on Speech Commands; the authors note the turn-end readout was trained on Smart Turn data, making that row in-distribution only for Marimba. It reports 100% language ID on 300 FLEURS clips and speaker-change AUROC of 0.966–0.980 on AMI and VoxConverse, above ECAPA, and beats pyannote 3.1 on speaker count. It loses on turn-end detection with 0.930 AUROC versus Smart Turn v3.2&\#x27;s 0.982 on Smart Turn&\#x27;s own test set, ties on ICSI meetings at 0.716 versus 0.712, and fails to generalize to unseen tasks such as CochlScene scene classification, where every head is at chance; code and Apache-2.0 weights are released.

reddit · r/MachineLearning · /u/solanotodesch · Nov 16, 15:47

**「Background」** Marimba follows a line of “typed decision” models such as Jev, which return probabilities over declared options instead of free text but do not accept audio; Marimba applies that idea to speech. It uses a single frozen Qwen3-ASR-0.6B encoder pass over each 8-second audio window, with small readouts and a question-conditioned head producing calibrated answers to typed questions such as yes/no, multiple-choice, or score. It is therefore not a speech-to-text system and does not output speaker identities or timelines.

**「Impact」** Developers building speech-query pipelines can get calibrated, per-question answers from a single frozen Qwen3-ASR-0.6B encoder pass per 8-second window, matching or beating the 30B-A3B Qwen3-Omni on 6 of 9 public tests, but they should not expect the same readouts to transfer to unseen tasks—scene classification sits at chance—or to beat Smart Turn v3.2 on turn-end detection \(AUROC 0.930 vs 0.982\).

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2611.18330v1">marimba: A System One Model for Speech - arXiv.org</a></li>
<li><a href="https://github.com/Charcot-AI/marimba-api">GitHub - Charcot-AI/marimba-api: Marimba: typed, calibrated ...</a></li>
<li><a href="https://arxiv.org/abs/2509.17765">[2509.17765] Qwen3-Omni Technical Report - arXiv.org</a></li>

</ul>
</details>

**Tags**: `#speech recognition`, `#audio models`, `#calibrated probabilities`, `#model efficiency`, `#research paper`

---