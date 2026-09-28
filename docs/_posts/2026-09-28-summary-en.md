---
layout: default
title: "Horizon Summary: 2026-09-28 (EN)"
date: 2026-09-28
lang: en
---

> From 6 items, 2 important content pieces were selected

---

**Technology News**
1. [Simon Willison&\#x27;s Annotated Keynote Recaps 2026 LLM Developments](#item-tech-news-1) ⭐️ 7.0/10
2. [NeurIPS Paper Claims Adaptive Functional Gradient Descent Beats Neural Nets](#item-tech-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Simon Willison&\#x27;s Annotated Keynote Recaps 2026 LLM Developments](https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/) ⭐️ 7.0/10

Simon Willison published an annotated version of the closing keynote he gave at the WeAreDevelopers World Congress North America in San Jose on 25 September 2026, tying the year&\#x27;s LLM trends into a chronological tour; the post, dated 27 September 2026, links to the talk video on YouTube. In the portion of the deck supplied, Willison dates the start of his 2026 to November 2025, when Claude Opus 4.5 and GPT-5.1 arrived as incremental model improvements that nonetheless crossed an invisible line: paired with their coding agent harnesses — Claude Code, around since February 2025, and the slightly younger Codex — they moved from &quot;often make mistakes&quot; to &quot;reliable enough to use on a day-to-day basis.&quot; He illustrates the November state of the art with his long-running &quot;Generate an SVG of a pelican riding a bicycle&quot; test, noting that Claude still could not really draw a bicycle and the GPT-5.1 frame was poor, and he flags the 24 November 2025 first commit to an obscure GitHub repository called &quot;Warelay&quot; as something he would return to later. He also describes his 2026 New Year&\#x27;s resolution to &quot;be more ambitious&quot; and take on as many new projects as he likes, and lists predictions that it will become undeniable that LLMs write good code, that sandboxing will finally be solved, and that there will be a &quot;Challenger disaster&quot; for coding agent security. The supplied excerpt cuts off partway through the predictions slide, so the talk&\#x27;s later technical detail and specific claims cannot be verified from the provided content.

rss · Simon Willison · Sep 27, 23:54

**「Background」** The post is an &quot;annotated presentation&quot;: the slides from Simon Willison&\#x27;s closing keynote at the WeAreDevelopers World Congress North America in San Jose on 25 September 2026, published alongside his speaker notes as a chronological tour of LLM developments. The talk treats 2026 as having begun in November 2025, when Claude Opus 4.5 and GPT-5.1 shipped as incremental model upgrades that, paired with their respective coding-agent harnesses \(Claude Code, available since February 2025, and the newer Codex\), crossed from &quot;often make mistakes&quot; to &quot;reliable enough to use on a day-to-day basis.&quot; Willison&\#x27;s &quot;generate an SVG of a pelican riding a bicycle&quot; prompt is his long-running, self-described &quot;world&\#x27;s stupidest benchmark&quot; for informally eyeballing what new models can and cannot draw.

**「Impact」** For developers already using Claude Code and Codex, the November 2025 pairing of Claude Opus 4.5 and GPT-5.1 with those harnesses shifted agentic coding from &quot;often make mistakes&quot; to &quot;reliable enough to use on a day-to-day basis,&quot; which is why Willison reversed his usual &quot;stay focused&quot; resolution and deliberately took on more projects in 2026. He cautions that unlocking the full potential of these agents still requires extraordinary discipline and knowledge, so the widened scope of work comes with a matching rise in engineering demands.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/">2026 in LLMs (so far)</a></li>
<li><a href="https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/">2026 in LLMs (so far) - simonwillison.net</a></li>
<li><a href="https://simonwillison.net/tags/coding-agents/">Simon Willison on coding-agents</a></li>

</ul>
</details>

**Tags**: `#LLMs`, `#AI trends`, `#annotated talk`, `#Simon Willison`, `#2026 retrospective`

---

<a id="item-tech-news-2"></a>
### [NeurIPS Paper Claims Adaptive Functional Gradient Descent Beats Neural Nets](https://i.redd.it/wom07k9ih9sh1.gif) ⭐️ 7.0/10

A first-author Reddit post announced that the paper “Functional Gradient Descent with Adaptive Representations” has been accepted at NeurIPS. The post says functional gradient descent algorithms generally outperform neural nets but are hard to implement accurately because functional gradients are infinite-dimensional and must be approximated, and naive approximations converge to the wrong place. To address this, the authors formalize a broad class of approximation schemes called “adaptive representations,” which they claim provably ensure convergence to the global minimizer while being immediately implementable. The resulting algorithms are said to outperform corresponding neural nets often by an order of magnitude across several settings, though the author describes the work as a starting point with potential. The linked arXiv paper is 2606.16926, and commenters noted caveats, including that the global-optimality claim requires a functional convexity condition \(Polyak-Lojasiewicz\) and that practicality may be limited to low-dimensional problems.

reddit · r/MachineLearning · dccsillag0 · Sep 28, 13:23 · [Discussion](https://www.reddit.com/r/MachineLearning/comments/1wsejb7/functional_gradient_descent_with_adaptive/)

**「Background」** Functional gradient descent \(FGD\) performs gradient descent directly in function space instead of optimizing the parameters of a fixed representation such as a neural network, which yields highly nonconvex losses that complicate training and theoretical analysis, while FGD itself benefits from strong convergence results and a clean theory. Because functional gradients are infinite-dimensional, they must be approximated in practice, and naive approximations can converge to the wrong solution. The paper &quot;Functional Gradient Descent with Adaptive Representations&quot; \(arXiv:2606.16926, dated June 15, 2026\) formalizes a broad class of approximation schemes, termed adaptive representations, that are claimed to provably ensure convergence to the global minimizer while remaining immediately implementable.

**「Impact」** Researchers and practitioners evaluating functional gradient methods may gain an implementable framework with claimed order-of-magnitude gains over comparable neural nets, but its global-convergence guarantee appears conditional on a functional convexity assumption and its practical dimensionality limits remain unresolved.

**「Community Discussion」** Commenters were largely positive but raised caveats: one said the global-optimality claim should mention the required Polyak-Lojasiewicz functional convexity condition, another questioned whether the approach is practical only for low-dimensional problems, and a third asked whether it is a new optimizer comparable to Adamw or Muon. The supplied thread does not include author answers to those questions.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.16926">[2606.16926] Functional Gradient Descent with Adaptive Representations</a></li>
<li><a href="https://arxiv.org/html/2606.16926v1">Functional Gradient Descent with Adaptive Representations</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#optimization`, `#functional gradient descent`, `#neural networks`, `#NeurIPS`

---