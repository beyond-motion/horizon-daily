---
layout: default
title: "Horizon Summary: 2026-11-03 (EN)"
date: 2026-11-03
lang: en
---

> From 10 items, 5 important content pieces were selected

---

**Technology News**
1. [Local Qwen 3.8 27B identifies games from raw model weights](#item-tech-news-1) ⭐️ 8.0/10
2. [Postman faces privacy backlash over alleged silent AI plugin installs](#item-tech-news-2) ⭐️ 7.0/10
3. [The &\#x27;Astra can read and write weights to improve Qwen&\#x27; post is misleading](#item-tech-news-3) ⭐️ 7.0/10
4. [Aircraft noise in videos can reveal exact locations via ADS-B](#item-tech-news-4) ⭐️ 7.0/10
5. [LLM 0.37 Adds Models, Endpoint Command, Embeddings Fixes](#item-tech-news-5) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Local Qwen 3.8 27B identifies games from raw model weights](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/) ⭐️ 8.0/10

Simon Willison reports that Qwen 3.8 27B, running locally through LM Studio with a long context window, inferred that a set of raw neural-network weights came from a simplified Pac-Man game, returning the answer after 46 minutes 12 seconds and 43,506 reasoning tokens with 72% stated confidence; it also identified Pong in about 1 hour 5 minutes. The experiment follows a paper by Rikiya Takehi, Jayden Teoh, Alex Zhang, and Omar Khattab that coins “Weight-Space Programming” and claims GPT-6 Astra can read raw weights to identify what a network was trained to do and can write small game-playing networks from scratch that outperform networks trained with PPO for 100 million steps. The paper also claims Astra improved Qwen3.5-0.8B on MATH-500 from 7.9% to 48.1% by natively editing 0.016% of its weights, and tripled IFEval, without writing training loops. Willison separates the no-tools weight-reading question from code-assisted weight editing, while Matthew Honnibal called the paper misleading for conflating the two and Sean Goedecke argued that the Qwen3.5-0.8B example follows steps a human ML researcher would take. The supplied excerpt is truncated and does not substantiate the full paper, so the broader capability claims remain contested.

rss · Simon Willison · Nov 3, 16:29

**「Background」** A neural network&\#x27;s learned behavior is encoded in its weights, large arrays of floating-point numbers that are normally adjusted by training algorithms rather than read or edited directly. &quot;Weight-Space Programming&quot; is the term proposed by Rikiya Takehi, Jayden Teoh, Alex Zhang, and Omar Khattab for having an LLM inspect or modify those raw weight values without gradient-based training. The work was published on Takehi&\#x27;s blog in November 2026, and the team released its prompts, responses, and evaluations, though the results are early and centered on a single frontier model.

**「Local reproducibility, limited practicality」** Developers can now reproduce the paper&\#x27;s weight-reading experiment on consumer hardware: a 17GB Qwen 3.8 27B build running locally identified Pac-Man after 46 minutes and Pong after about 65 minutes. However, the need for a larger-than-default context window and hour-long run times make this a slow, anecdotal proof of concept rather than a practical workflow, and critics such as Sean Goedecke argue the demonstrated ability falls short of superhuman weight comprehension.

<details><summary>References</summary>
<ul>
<li><a href="https://rikiyat.github.io/">Rikiya Takehi</a></li>
<li><a href="https://todayforai.com/en/items/art-59862493-ccf">MIT Proposes Weight-Space Programming: LLMs Directly Edit ...</a></li>
<li><a href="https://www.datacamp.com/blog/weight-space-programming">Weight-Space Programming: How LLMs Edit Network Weights</a></li>
<li><a href="https://www.seangoedecke.com/llms-are-not-superhuman-at-reading-and-writing-neural-network-weights/">LLMs are not superhuman at reading and writing neural network ...</a></li>

</ul>
</details>

**Tags**: `#LLM interpretability`, `#weight-space programming`, `#model weights`, `#research paper`, `#local LLMs`

---

<a id="item-tech-news-2"></a>
### [Postman faces privacy backlash over alleged silent AI plugin installs](https://github.com/postmanlabs/postman-app-support/issues/14370) ⭐️ 7.0/10

A GitHub issue alleges that Postman silently auto-installs AI plugins and attempts to share all API data, though the claims have not been independently verified in the supplied material. The report drew significant Hacker News discussion focused on privacy, application bloat, and alternatives to Postman. Commenters described moving to Bruno, citing performance, the ability to store request definitions in git, and one healthcare team&\#x27;s cybersecurity decertification of Postman. Others criticized Postman&\#x27;s funding, valuation, mandatory logins, subscriptions, and AI features as signs of a tool that has drifted from its lightweight origins.

hackernews · sidgarimella · Nov 3, 17:22 · [Discussion](https://news.ycombinator.com/item?id=50354960)

**「Background」** Postman is a widely used API development and testing client; the issue concerns its desktop app installing plugins into AI coding agents such as OpenAI Codex and Claude Code, alongside a user-wide plugin, a startup instruction hook, a remote MCP connection, and a separately installed Postman CLI. MCP \(Model Context Protocol\) is the mechanism these coding agents use to connect to external tools and data sources, which is why a remote MCP connection could let an agent route API work through Postman. A subsequent third-party review of the installer code at the pinned revision disputed the data-sharing portion of the original report, leaving the extent of any data exposure contested.

**「Security and procurement fallout」** Developers and organizations that route sensitive API data through Postman may face renewed security scrutiny; one healthcare commenter said their cyber team decertified the tool and staff switched to Bruno overnight, though the underlying allegations remain unverified.

**「Community discussion」** Commenters broadly agreed that Postman had become slow and bloated, and several said they migrated to Bruno; a healthcare worker said Postman was decertified by their cyber team, while another noted persistent sales outreach after the switch. The thread also tied the behavior to Postman&\#x27;s funding and valuation pressure, though those claims were anecdotal.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/postmanlabs/postman-app-support/issues/14370">[SEVERE] Desktop auto-installs Codex/Claude plugins ... - GitHub</a></li>
<li><a href="https://explainx.ai/blog/postman-desktop-auto-installs-codex-claude-code-plugins-self-approved-hook-issue-14370-2026">Postman Auto-Installs Codex and Claude Code Plugins: What to ...</a></li>
<li><a href="https://dev.to/frankchu/postman-installed-itself-into-codex-and-claude-e38">Postman installed itself into Codex and Claude - DEV Community</a></li>

</ul>
</details>

**Tags**: `#Postman`, `#privacy`, `#API tooling`, `#developer tools`, `#security`

---

<a id="item-tech-news-3"></a>
### [The &\#x27;Astra can read and write weights to improve Qwen&\#x27; post is misleading](https://honnibal.dev/blog/astra-read-write-misleading) ⭐️ 7.0/10

A rebuttal post arguing that claims about &\#x27;Astra reading and writing weights to improve Qwen&\#x27; are misleading, sparking expert discussion that reframes the result as reasoning-loop reduction rather than genuine model improvement.

hackernews · syllogism · Nov 3, 12:21 · [Discussion](https://news.ycombinator.com/item?id=50351111)

**Tags**: `#mechanistic-interpretability`, `#llm-steering`, `#research-critique`, `#reasoning-models`, `#ai-research-claims`

---

<a id="item-tech-news-4"></a>
### [Aircraft noise in videos can reveal exact locations via ADS-B](https://simonwillison.net/2026/Nov/3/a-sound-that-leaks-your-exact-location/) ⭐️ 7.0/10

Simon Willison highlighted a YouTube video by Colsto demonstrating an OSINT technique that extracts nearly imperceptible aircraft background noise from a video&\#x27;s soundtrack to determine where the video was recorded. The method derives Doppler curves from the faint plane sounds and cross-references them against ADS-B flight data, using aircraft speed, distance, and the gaps between different flights to narrow down the location. Willison describes it as a &quot;genius piece of OSINT&quot; with clear privacy implications, since everyday recordings can carry location-revealing acoustic traces that are not obvious to the person filming. The item is a brief pointer to the video rather than a full technical write-up, and it does not present independent validation or detail the accuracy limits of the approach.

rss · Simon Willison · Nov 3, 05:32

**「Background」** ADS-B is a widely used aircraft surveillance system in which planes broadcast position, altitude, speed, and identity; because those signals are public, flight histories can be looked up or reconstructed. The Doppler effect shifts the frequency of sound from a moving source, so a plane&\#x27;s faint engine or airframe noise produces a changing pitch signature in a recording. By measuring those Doppler curves in a spectrogram and matching them to ADS-B tracks—using constraints such as velocity, closest-approach distance, and the interval between two flyovers—an analyst can infer where the recording was made.

**「Impact」** Creators and privacy-conscious users who publish videos or audio with faint aircraft overflight noise can now be geolocated to within roughly 100 meters from as little as 60 seconds of recording, so such soundtracks should be stripped or sanitized before release. The technique still depends on detectable aircraft noise and the availability of matching ADS-B flight data for the time and region.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=UytYrhYLOKI">I discovered a sound that leaks your exact location ... - YouTube</a></li>
<li><a href="https://www.techradar.com/computing/cyber-security/youtuber-discovers-aircraft-noise-trick-that-can-geolocate-your-videos-to-within-100m-doppler-effect-pinpoints-locations-from-just-60-seconds-of-audio">YouTuber discovers aircraft noise trick that can geolocate ...</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#OSINT`, `#audio forensics`, `#ADS-B`, `#YouTube`

---

<a id="item-tech-news-5"></a>
### [LLM 0.37 Adds Models, Endpoint Command, Embeddings Fixes](https://simonwillison.net/2026/Nov/2/llm/) ⭐️ 7.0/10

LLM 0.37, a release of Simon Willison&\#x27;s command-line tool and Python library, packages about two months of accumulated features and fixes. It adds support for the gpt-6.1-sol and gpt-6.1-terra models and introduces the \`llm openai endpoint add\` command to simplify configuring additional models that use OpenAI-compatible endpoints. For users who have not set their own default, the default model changes to gpt-6-luna, which costs half as much as the previous default, gpt-5.6-luna. Embeddings support now accepts different content types for binary content, which the release says is needed for models such as Gemini Embedding 2 that can embed text, audio, images, and video; the release also includes fixes from 12 authors, almost all AI-assisted.

rss · Simon Willison · Nov 2, 23:49

**「Background」** LLM is Simon Willison&\#x27;s open-source command-line tool and Python library for working with large language models, including OpenAI, Anthropic&\#x27;s Claude, Google&\#x27;s Gemini, Qwen, Gemma, Kimi, DeepSeek, and Mistral, both through remote APIs and as models installed and run locally. The project is distributed via GitHub, PyPI, and Homebrew, and is extensively documented. Embeddings, one focus of this release, are vector representations used to search, cluster, or compare content, and some embedding models can handle modalities such as text, audio, images, and video in addition to plain text.

**「Impact」** Developers using LLM gain a simpler way to configure OpenAI-compatible models and a cheaper default when they have not set their own, while embeddings workflows can handle mixed content types.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/simonw/llm">GitHub - simonw/ llm : Access large language models from the...</a></li>
<li><a href="https://llm.datasette.io/">LLM : A CLI utility and Python library for interacting with Large...</a></li>
<li><a href="https://seamusbarnes.github.io/til/2025/01/13/simon-willison-llm/">Generate Plain-Language System Summaries using Simon ...</a></li>

</ul>
</details>

**Tags**: `#LLM CLI`, `#Python library`, `#OpenAI-compatible endpoints`, `#embeddings`, `#release`

---