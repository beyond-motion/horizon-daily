---
layout: default
title: "Horizon Summary: 2026-08-02 (EN)"
date: 2026-08-02
lang: en
---

> From 6 items, 2 important content pieces were selected

---

**Technology News**
1. [Open Letters on AI Development and Open-Weight Models](#item-tech-news-1) ⭐️ 7.0/10
2. [OpenAI claims Astra solved ten stubborn math problems](#item-tech-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Open Letters on AI Development and Open-Weight Models](https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything) ⭐️ 7.0/10

On July 24, 2026, Microsoft shepherded an open letter titled &quot;Open Weights and American AI Leadership,&quot; signed by 235 AI-adjacent companies including NVIDIA, Amazon, Y Combinator, The Linux Foundation, and later OpenAI, arguing that open-weight AI models should not be banned because closed models create single points of failure and that distillation is a legitimate model-development technique. Anthropic did not sign, and three days later CEO Dario Amodei published a response that stopped short of advocating a ban on open-weights models but urged a crackdown on industrial-scale distillation and warned about authoritarian governments building more powerful models and misuse for cyberattacks or biological attacks. On July 28, 2026, &quot;Pacing the Frontier&quot; was published with signatures from 1,324 employees of frontier AI companies, including Jakub Pachocki, Ilya Sutskever, Dario Amodei, and Jack Clark, requesting that the U.S. government support an international effort to develop technical and governance tools to deliberately pace automated AI development. The letter highlights accelerating AI automation, including Anthropic producing 80% of its code with Claude Code, OpenAI&\#x27;s Sol reducing end-to-end serving costs by 20%, and Kimi K3 designing a chip to serve a nano model built on its own architecture.

rss · Simon Willison · Aug 2, 04:16

**「Background」** Open-weight AI models are models whose trained parameters are publicly released, allowing others to download, run, and modify them, in contrast to closed models that are available only through an API. By 2026, the US government and industry were debating whether to restrict open-weight models over safety and national-security concerns, especially amid competition with China and incidents like a US directive to suspend access to an open-weight model. The open letters described here respond to that policy debate, with Microsoft and 235 companies defending open weights and a separate employee petition calling for deliberate pacing of frontier AI development.

**「Impact」** The letters create visible industry pressure on the U.S. government to keep open-weight models legal and to develop governance for automated AI research, while Anthropic&\#x27;s refusal to sign exposes a sharp policy split among frontier labs over open weights and distillation.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/20/openai-is-scared-of-open-weight-models-should-the-us-be/">OpenAI is scared of open - weight models . Should the US be?</a></li>
<li><a href="https://btw.co/node/11741882/ai-model-debate/">AI Model Debate Trending #74 - Break The Web</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#open weights`, `#open source`, `#AI industry`, `#Microsoft`

---

<a id="item-tech-news-2"></a>
### [OpenAI claims Astra solved ten stubborn math problems](https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything) ⭐️ 7.0/10

OpenAI announced that an internal version of its upcoming Astra model solved ten mathematical problems that had seen no progress on the main result for at least a decade, with each solution costing under $2,000 at GPT-5.6 Sol token prices. The company published Lean 4 formalizations in the openai/ten-proofs repository, a paper describing the solutions, and an LLM-generated PDF that reconstructs how each proof came together from unpublished reasoning traces. Simon Willison calls the transparency decent but flags the absence of failure statistics—how many problems cost $2,000 without a solution—and says he wants to see the actual prompts. The announcement follows Anthropic&\#x27;s discovery of cryptographic weaknesses with Claude using Mythos Preview and has prompted many mathematicians online to describe a &\#x27;Deep Blue&\#x27; moment, including Kirwin Hampshire&\#x27;s essay &\#x27;The Dark Night of Mathematics&\#x27; about a profound spiritual crisis. Terence Tao has framed such AI-driven work as a shift toward &\#x27;big mathematics,&\#x27; with large-scale human-machine collaboration and AI handling much of the technical grunt work.

rss · Simon Willison · Aug 1, 20:34

**「Background」** Lean 4 is an interactive theorem prover that allows mathematicians to formally verify proofs, and OpenAI published Lean 4 formalizations of its claimed results in an open GitHub repository. The announcement follows broader efforts to apply AI to mathematics, such as Anthropic&\#x27;s recent use of Claude to discover cryptographic weaknesses, and has coincided with debates among mathematicians about the implications of AI-driven discoveries. OpenAI&\#x27;s post describes advances in geometry, cryptography, and complexity on problems that had seen no progress for at least a decade.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/ten-advances-in-mathematics/">Ten advances in mathematics and theoretical computer science</a></li>
<li><a href="https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/">Ten advances in mathematics and theoretical computer science</a></li>

</ul>
</details>

**Tags**: `#AI`, `#mathematics`, `#OpenAI`, `#theoretical computer science`, `#research`

---