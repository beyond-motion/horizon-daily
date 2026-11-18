---
layout: default
title: "Horizon Summary: 2026-11-18 (EN)"
date: 2026-11-18
lang: en
---

> From 8 items, 5 important content pieces were selected

---

**Technology News**
1. [Critical unauthenticated RCE disclosed in Nginx HTTP/2](#item-tech-news-1) ⭐️ 8.0/10
2. [Microsoft announces seven AI models focused on scalable price-performance](#item-tech-news-2) ⭐️ 7.0/10
3. [Quad9 leaves France over DNS-blocking obligations](#item-tech-news-3) ⭐️ 7.0/10
4. [External sandboxes for coding agents keep execution isolated from the agent](#item-tech-news-4) ⭐️ 7.0/10
5. [OpenAI releases GPT-6.2 Astra and Sol with cheaper Astra pricing](#item-tech-news-5) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Critical unauthenticated RCE disclosed in Nginx HTTP/2](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities) ⭐️ 8.0/10

A critical unauthenticated remote code execution vulnerability in Nginx HTTP/2 handling has been disclosed under CVE-2026-123633 and CVE-2026-123007, with urgent patching or workaround guidance. Exposure is limited to configurations with HTTP/2 enabled, which is not the default; discussion cites W3Techs data indicating about 12% of servers use HTTP/2. A fix reportedly landed in the open-source repository about a week before disclosure, and the commit credited Xint.io. Commenters criticized the absence of an earlier public advisory given that disabling HTTP/2 is a straightforward mitigation.

hackernews · speedping · Nov 18, 15:19 · [Discussion](https://news.ycombinator.com/item?id=50547374)

**「Background」** NGINX is a widely used web server and reverse proxy, and its HTTP/2 support first shipped in version 1.9.5. The two flaws at issue are in NGINX itself, meaning an application&\#x27;s own code can be secure while the server remains exposed, and both are rated Critical with a CVSS 4.0 score of 9.2. CVE-2026-123007 dates back to that first HTTP/2 release and persisted through affected versions, while CVE-2026-123633 involves HTTP/2 requests forwarded to an upstream backend server.

**「Impact」** Administrators running NGINX Open Source or NGINX Plus with HTTP/2 enabled for client connections face unauthenticated remote code execution and must patch or disable HTTP/2 immediately, with the flaw rated 9.2 under CVSS 4.0. Exposure is narrower than NGINX&\#x27;s overall footprint, since HTTP/2 is not enabled by default and community estimates put adoption at roughly 12% of servers.

**「Community discussion」** The thread largely agrees the flaw is serious but notes that the default-off HTTP/2 requirement substantially narrows exposure. A recurring concern is disclosure timing and the lack of a public service announcement during the reported week between the fix and public disclosure, alongside shared links for checking vulnerable hosts and emergency workarounds.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities">Unauthenticated Remote Code Execution in NGINX ... | Wiz Blog</a></li>
<li><a href="https://xint.io/blog/nginx2root-remote-code-execution">NGINX 2 Root: New Remote Code Execution Vulnerabilities in nginx ...</a></li>
<li><a href="https://cybersecuritynews.com/nginx-http-2-vulnerabilities/">NGINX HTTP/2 Flaws Could Allow Memory Corruption and Remote ...</a></li>
<li><a href="https://app.opencve.io/cve/CVE-2026-123633">CVE-2026-123633 - Vulnerability Details - OpenCVE</a></li>
<li><a href="https://www.rapid7.com/db/vulnerabilities/cve-2026-123633/">CVE-2026-123633: F5: When NGINX Plus or NGINX Open ... - Rapid7</a></li>

</ul>
</details>

**Tags**: `#nginx`, `#security`, `#remote-code-execution`, `#http2`, `#vulnerability`

---

<a id="item-tech-news-2"></a>
### [Microsoft announces seven AI models focused on scalable price-performance](https://microsoft.ai/news/microsoft-ignite-2026/) ⭐️ 7.0/10

Microsoft announced seven new AI models at Ignite 2026, positioning the lineup around scalable price-performance. The supplied material provides only headline-level positioning, with no technical benchmarks, model-by-model capabilities, or detailed availability information. The release is notable as a broad model rollout from Microsoft, but its practical performance and scope remain unclear from the available account. Hacker News discussion was mixed, combining early hands-on interest in the coding model MAI Code 2 with skepticism about Microsoft’s strategy and transparency.

hackernews · gmays · Nov 18, 16:08 · [Discussion](https://news.ycombinator.com/item?id=50548021)

**「Background」** Microsoft Ignite is the company&\#x27;s annual enterprise technology conference, where it typically details new AI and cloud products. At the 2026 event, Microsoft introduced seven specialized AI models—including MAI Code 2 for coding, along with models for vulnerability discovery and image generation—positioned as lower-cost alternatives to frontier systems. Microsoft said MAI Code 2 reaches 98% of the coding quality of GPT-6.1 Sol at about 40% of the price, and 96% of Opus 5.5&\#x27;s performance at just 5% of the price.

**「Impact」** Developers weighing coding-model costs gain a concrete alternative in MAI Code 2, which Microsoft claims delivers 96% of Claude Opus 5.5’s performance at 5% of its price—a vendor-reported tradeoff that could lower expenses for routine coding tasks if it holds in practice.

**「Community discussion」** Commenters were mixed: one reported positive hands-on results with MAI Code 2, saying it was roughly comparable to Opus or Sol, while others questioned Microsoft’s strategy, urging open-source or open-weight releases and criticizing the keynote as shallow or uninnovative. One commenter also asked why the models were absent from the Artificial Analysis index.

<details><summary>References</summary>
<ul>
<li><a href="https://microsoft.ai/news/microsoft-ignite-2026/">Seven new world class models at scalable ... | Microsoft AI</a></li>
<li><a href="https://forklog.com/en/microsoft-unveils-ai-models-for-coding-and-cybersecurity/">Microsoft unveils AI models for coding and cybersecurity | ForkLog</a></li>
<li><a href="https://finance.yahoo.com/markets/article/microsoft-ignite-focuses-on-ai-models-for-specific-tasks-lowering-costs-for-enterprise-203433266.html">Microsoft &#x27;s AI pitch at Ignite : Cheaper models as business &#x27;token...</a></li>
<li><a href="https://felloai.com/mai-code-2/">MAI Code 2: Price, Benchmarks and Copilot Plans - felloai.com</a></li>
<li><a href="https://www.zdnet.com/innovation/microsoft-ai-coding-model-rivals-claude-opus-5-5-ignite/">Microsoft says its new AI coding model rivals Claude Opus 5.5 ...</a></li>

</ul>
</details>

**Tags**: `#Microsoft`, `#AI models`, `#model releases`, `#price-performance`, `#AI coding`

---

<a id="item-tech-news-3"></a>
### [Quad9 leaves France over DNS-blocking obligations](https://techstackups.com/articles/quad9-leaves-france-dns-blocking/) ⭐️ 7.0/10

Quad9 has withdrawn from France after DNS-blocking obligations tied to piracy enforcement, according to the item’s analysis summary. The episode frames DNS resolvers as an enforcement point for copyright law and raises questions about censorship, privacy, and the wider implications for internet infrastructure. The supplied material does not detail the court ruling, timing, or specific domains involved.

hackernews · ritzaco · Nov 18, 13:18 · [Discussion](https://news.ycombinator.com/item?id=50545958)

**「Background」** Quad9 is a global public recursive DNS resolver that filters domains associated with malware and phishing. The dispute centers on a French court order favoring beIN Sports that would require DNS-level blocking of piracy-related domains, making a public resolver an enforcement intermediary. Rather than comply, Quad9 reportedly plans to stop serving users in France on November 24, 2026.

**「Impact」** Quad9 users in France will need to switch to another DNS provider after the nonprofit resolver stops serving the country rather than comply with a beIN Sports domain-blocking order. The withdrawal also shows that DNS-level blocking mandates can push independent privacy-focused resolvers out of a national market.

**「Community discussion」** Commenters debate whether the French court is misapplying the law or faithfully enforcing a bad statute, with one arguing that non-prosecution anti-piracy measures are a backdoor to suppressing speech. Another questions the practical logic of withdrawal given that Quad9 reportedly cannot reliably identify French users.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Quad9">Quad 9 - Wikipedia</a></li>
<li><a href="https://techstackups.com/articles/quad9-leaves-france-dns-blocking/">Quad 9 Is Leaving France : Why DNS Resolvers Are... | Tech Stackups</a></li>
<li><a href="https://blog.cloudflare.com/quad9-withdrawal-from-france/">Quad9’s withdrawal from France: A canary in the coal mine</a></li>
<li><a href="https://techstackups.com/articles/quad9-leaves-france-dns-blocking/">Quad9 Is Leaving France: Why DNS Resolvers Are the Wrong ...</a></li>

</ul>
</details>

**Tags**: `#DNS`, `#internet governance`, `#privacy`, `#censorship`, `#Quad9`

---

<a id="item-tech-news-4"></a>
### [External sandboxes for coding agents keep execution isolated from the agent](https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/) ⭐️ 7.0/10

Simon Willison, working with Prime Radiant, introduced an “external sandbox” pattern in which code executed by a coding agent runs inside a dedicated sandbox while the agent itself remains outside it. The project released three sandbox server implementations: a Node.js server using v86 to run Alpine Linux in WebAssembly; a Python web server running Alpine Linux in an Apple Containers instance; and a Python web server using Microsoft’s Quicksand library, which bundles QEMU and Alpine Linux in a Python package. All three expose the same localhost API, which can be configured in Pi, Claude Code, or Codex so those agents send code execution calls to the sandbox. The sandboxes also include an optional HTTP/HTTPS allow-list proxy for controlling which hosts agent code can reach, plus a credential replacement mechanism for making authenticated API calls without sharing a secret with the agent; the proxy can be reconfigured while the sandbox is running. The stated motivation is to make it safer to try local models without a mistake or prompt-injection attack causing damaging actions, though the supplied excerpt does not detail the sandbox mechanisms further or provide independent evaluation.

rss · Simon Willison · Nov 17, 22:52

**「Background」** AI coding agents often execute commands and code on the same machine they run on, so a mistake or prompt-injection attack can reach the developer&\#x27;s files and credentials. Sandboxing limits that exposure by confining execution to an isolated environment. The external sandbox pattern separates the two: the agent stays outside the sandbox and sends code-execution requests into it, allowing tools such as Pi, Claude Code, and Codex to use a shared localhost API and optionally restrict outbound network access.

**「Impact」** Developers using Pi, Claude Code, or Codex can route agent-executed code to a separate sandbox through a common localhost API, with host allow-listing and credential replacement limiting network access and secret exposure.

**Tags**: `#ai-agents`, `#sandboxing`, `#security`, `#prompt-injection`, `#developer-tools`

---

<a id="item-tech-news-5"></a>
### [OpenAI releases GPT-6.2 Astra and Sol with cheaper Astra pricing](https://simonwillison.net/2026/Nov/17/gpt62-astra-and-sol/) ⭐️ 7.0/10

OpenAI released GPT-6.2 Astra, described as its new frontier model for hard projects, and GPT-6.2 Sol, an efficient, versatile model for everyday work, both available in the API as \`gpt-6.2-astra\` and \`gpt-6.2-sol\`. Astra is priced at $8 per million input tokens and $40 per million output tokens—80% of GPT-6 Astra&\#x27;s $10/$50 and matching Claude Fable 5.2—with cached input at $0.40 per million versus $1 for the older model, while Sol stays at $2/$10, half the price of GPT-5.6 Sol. Simon Willison shipped LLM 0.38 with support for the new models, but his informal pelican and Yonkers-mech tests found neither model matched Claude Fable 5.2 or Gemini 4 Carbon at the mech-morphing prompt. He also reported mixed early reception: Astra is not scoring as high as Fable 5.2 on various benchmarks, and reviewers including Theo Browne have complained that its communication style can be confusing, such as asking users about obscure internal implementation details during long agentic runs.

rss · Simon Willison · Nov 17, 22:38

**「Background」** OpenAI divides the GPT-6.2 release into two tiers: GPT-6.2 Astra, described as the frontier model for the hardest projects, and GPT-6.2 Sol, described as the cheaper, efficient model for everyday work. They follow GPT-6 Astra and GPT-6.1 Sol, respectively, and are available through the API as gpt-6.2-astra and gpt-6.2-sol. API pricing is quoted per million tokens with separate input, cached-input, and output rates, and the LLM tool&\#x27;s 0.38 release added support for the new model IDs.

**「Impact」** Developers running long or agentic sessions through the API can cut costs with \`gpt-6.2-astra\`, priced at $8/$40 per million input/output tokens—20% below GPT-6 Astra—and $0.40 per million cached input tokens, down from $1, with support available immediately in LLM 0.38.

**Tags**: `#OpenAI`, `#GPT-6.2`, `#API pricing`, `#model release`, `#LLM tooling`

---