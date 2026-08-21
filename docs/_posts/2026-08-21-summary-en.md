---
layout: default
title: "Horizon Summary: 2026-08-21 (EN)"
date: 2026-08-21
lang: en
---

> From 7 items, 2 important content pieces were selected

---

**Technology News**
1. [Developer Accidentally Hijacks E.164 ARPA, Logs Military Calls](#item-tech-news-1) ⭐️ 8.0/10
2. [DeepSeek v4-flash-vision-exp adds vision input to flash model](#item-tech-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Developer Accidentally Hijacks E.164 ARPA, Logs Military Calls](https://lina.sh/blog/hijacking-e164-arpa) ⭐️ 8.0/10

A developer accidentally hijacked the E.164 ARPA DNS namespace, a public telephony routing system that is largely forgotten but still active, and logged hundreds of thousands of misdirected phone calls, including calls to military bases. The incident occurred because the developer obtained control of a subdomain within the e164.arpa zone, which is used for ENUM \(Telephone Number Mapping\) queries, and then observed traffic that was supposed to reach other parties. The finding exposes a real, exploitable infrastructure flaw: the E.164 ARPA system lacks enforcement and oversight, allowing misconfigurations or malicious takeovers to intercept sensitive call routing data. The developer reported the issue to authorities, but the response was minimal, and no reward was given, highlighting the systemic neglect of this legacy infrastructure.

hackernews · gavide · Aug 21, 13:11 · [Discussion](https://news.ycombinator.com/item?id=49387570)

**「Background」** E.164 ARPA is a DNS-based system \(ENUM\) that maps telephone numbers to internet services, such as SIP addresses, using the e164.arpa domain. It was designed to facilitate number portability and VoIP routing, but it never gained widespread public adoption and is now mostly used in private, commercial services over VPNs. The system remains technically active, and its lack of public visibility means that security vulnerabilities and misconfigurations can go unnoticed for years.

**「Impact」** The incident demonstrates that the E.164 ARPA infrastructure is vulnerable to accidental or malicious hijacking, potentially exposing call routing data for military and other sensitive numbers to unauthorized parties. This could have serious privacy and security implications for organizations relying on this legacy system, though the practical scope is limited by the system&\#x27;s low public usage.

**「Community Discussion」** Commenters expressed surprise that the author avoided legal trouble, noting that reporting such findings to authorities often leads to prosecution. Others appreciated the story as a rare example of infrastructure falling through the cracks, and some suggested the author should have set up a SIP server to test actual call termination. A few noted that similar systems like TRIP exist and remain underused, and there was general agreement that the issue was only addressed because military involvement was discovered.

**Tags**: `#DNS`, `#telephony`, `#security`, `#ENUM`, `#infrastructure`

---

<a id="item-tech-news-2"></a>
### [DeepSeek v4-flash-vision-exp adds vision input to flash model](https://api-docs.deepseek.com/guides/vision/) ⭐️ 7.0/10

DeepSeek has released v4-flash-vision-exp, an experimental version of its v4-flash model that adds vision input capabilities, addressing a previously known limitation. The model converts images into tokens based on their dimensions, which are billed together with text tokens, and automatically resizes images before inference: images below roughly 384×384 pixels are scaled up while larger images are scaled down, both preserving aspect ratio. This update is significant because v4-flash has been widely used for code tasks, and the text-only version had a tendency to falsely assume vision capabilities and invent text-based image analysis tools, breaking sessions when attempting to read screenshots. The announcement includes benchmarks, though the source content lacks detailed technical specifications beyond the image tokenization and resizing behavior.

hackernews · dares2573 · Aug 21, 10:33 · [Discussion](https://news.ycombinator.com/item?id=49386163)

**「Background」** DeepSeek&\#x27;s v4-flash model is a widely used, text-only language model favored for code tasks and agent workflows. The new experimental release, DeepSeek-v4-flash-vision-exp, adds vision input capabilities, allowing the model to process images by converting them into tokens billed alongside text tokens. Images are automatically resized before inference, with a cap of 384 billable tokens per image, and the model supports Chat Completions, Messages, and Responses API formats. This addresses a known limitation where the text-only model would sometimes incorrectly assume it had vision and invent image-analysis tools.

**「Impact」** Developers using DeepSeek v4-flash for code tasks, particularly those needing to analyze Playwright screenshots, gain a native vision capability that was previously missing, potentially reducing reliance on other models like Claude Sonnet for such tasks. However, the experimental model&\#x27;s reliability is not yet proven, as one user reports it fails a simple clock-reading test that a competing model handled nearly correctly, so users should verify performance on their specific use cases before adopting it.

**「Community Discussion」** Community feedback is mixed: one user finds the vision addition promising for screenshot analysis, while another reports a concrete failure on a clock-reading test, and a third notes that the text-only version&\#x27;s habit of hallucinating vision capabilities made this upgrade necessary. A user also questions whether the text-only version remains useful if the vision model matches its performance, suggesting cost or latency as possible reasons.

<details><summary>References</summary>
<ul>
<li><a href="https://api-docs.deepseek.com/news/news260821/">DeepSeek - V 4 - Flash - Vision - Exp Release... | DeepSeek API Docs</a></li>
<li><a href="https://runtimewire.com/article/deepseek-v4-flash-vision-api-image-billing">DeepSeek &#x27;s experimental vision model spans three formats, caps...</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#vision-language-model`, `#AI-model-release`, `#multimodal-AI`, `#developer-tools`

---