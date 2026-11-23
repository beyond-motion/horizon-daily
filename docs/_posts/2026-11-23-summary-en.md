---
layout: default
title: "Horizon Summary: 2026-11-23 (EN)"
date: 2026-11-23
lang: en
---

> From 5 items, 2 important content pieces were selected

---

**Technology News**
1. [Ladybird browser engine enters alpha](#item-tech-news-1) ⭐️ 8.0/10
2. [Zhipu releases GLM-5.4 loop transformer for coding](#item-tech-news-2) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Ladybird browser engine enters alpha](https://ladybird.org/posts/alpha/) ⭐️ 8.0/10

The Ladybird browser project has entered alpha, marking a significant milestone for an independent browser engine built from scratch. The alpha designation indicates an early testing stage rather than a production-ready browser, while the project remains notable for pursuing a separate engine and greater web-platform diversity. The supplied material did not include detailed technical specifications for the alpha release.

hackernews · janvdberg · Nov 23, 16:13 · [Discussion](https://news.ycombinator.com/item?id=50614249)

**「Background」** Ladybird began as the browser for the SerenityOS hobby operating system, became a standalone cross-platform project in 2022, and is developed by the Ladybird Browser Initiative, a US 501\(c\)\(3\) nonprofit funded entirely by donations and sponsorships. After forking from SerenityOS, it was no longer bound by that project&\#x27;s from-scratch culture and began using third-party libraries for common functionality such as image/audio/video formats, encryption, and graphics. The project had said it was targeting a first alpha for Linux and macOS in Summer 2026, aimed at developers and early adopters.

**「Impact」** For developers and early adopters on macOS and Linux, the alpha provides a genuinely independent engine—not a Chromium, Gecko, or WebKit fork—to test against real sites, but it should be treated as experimental rather than a production browsing environment.

**「Community discussion」** Commenters who tried the alpha reported that many sites, including YouTube and Google Maps, rendered correctly, though some noted lag and slightly jerky scrolling. Others welcomed an alternative browser not tied to Google&\#x27;s ads, discussed the shift from self-developed libraries to production-grade components such as SQLite and Skia, and asked what precautions are appropriate for alpha software, especially for logins, payments, and downloads.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ladybird_%28web_browser%29">Ladybird (web browser) - Wikipedia</a></li>
<li><a href="https://ladybird.org/">Ladybird</a></li>
<li><a href="https://ladybird.org/index.html?_hsenc=p2ANqtz--Bsp32Lwf1DeVtYTqRvmo2s8tDw1qi9ZnWR4WTC3HqRkpH0-4UW_UFJQGDraQ2G0fK3CFQfVb0QYMKk3qYqUITJfqv0A&amp;_hsmi=314104664">A truly independent - Ladybird Ladybird (web browser) — Edgepedia 67,377 stars and zero Chromium: I ran Ladybird alpha Ladybird: A new, independent browser engine — written from ... SerenityOS Creator Is Building an Independent, Standards ...</a></li>
<li><a href="https://github.com/LadybirdBrowser/ladybird">GitHub - LadybirdBrowser/ ladybird : Truly independent web browser</a></li>
<li><a href="https://ladybird.org/">Ladybird is a truly independent web browser , backed by a non-profit.</a></li>

</ul>
</details>

**Tags**: `#browsers`, `#open-source`, `#web-engines`, `#ladybird`, `#software-engineering`

---

<a id="item-tech-news-2"></a>
### [Zhipu releases GLM-5.4 loop transformer for coding](https://z.ai/blog/glm-5.4) ⭐️ 8.0/10

Zhipu has released GLM-5.4, which it describes as its first loop transformer and positions around generalized coding. The release provides unusually detailed technical disclosure, and the Hacker News post drew 864 points and 307 comments. Commenters discussed loop transformers as an architecture that reuses weights across repeated computation, potentially easing the memory-bandwidth bottleneck that dominates inference. The excerpt does not provide benchmark results or establish broad paradigm-shifting impact, and commenters said unresolved issues remain.

hackernews · foohis · Nov 23, 10:06 · [Discussion](https://news.ycombinator.com/item?id=50609685)

**「Background」** Loop transformers are an architecture in which some layers are evaluated more than once during inference instead of every layer running exactly once. GLM-5.4 is Z.ai&\#x27;s first flagship built on this design; Z.ai says 28 of its 78 layers run twice and claims intelligence comparable to 2T–3T-parameter models, positioning the release as the start of its “Generalized Coding” line. The model is listed with a 1M context length, matching GLM-5.3, while Z.ai says recent work scaled both the loop and the model size.

**「Impact」** Developers evaluating coding models can test a system Zhipu says reaches 2T–3T-parameter-class intelligence by reusing layers across passes to add effective depth without a proportional rise in unique parameters, though the company acknowledges limitations and the parity claim remains vendor-reported.

**「Discussion」** Commenters praised Zhipu&\#x27;s transparency and detailed technical disclosure as a contrast to more closed Western labs, while treating loop transformers as a promising direction with problems still to solve. Practical concerns included one commenter reporting that GLM-5.4 was not available through OpenRouter or the regular Z.ai API plan and required the Coding Plan, plus long, self-checking &quot;marathon thinking&quot; sessions that can dramatically increase time to completion.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.z.ai/guides/llm/glm-5.4">GLM - 5 . 4 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://www.youtube.com/watch?v=HVey00YZ5Xk">GLM - 5 . 4 Is Here: The First Loop Transformer , and What... - YouTube</a></li>
<li><a href="https://teamorouter.com/blogs/glm-5-4">GLM - 5 . 4 Released: Vision, Stronger Coding , and When the API Arrives</a></li>
<li><a href="https://z.ai/blog/glm-5.4">GLM-5.4: Toward Generalized Coding with Our First Loop ...</a></li>
<li><a href="https://www.techinasia.com/news/chinas-zhipu-added-glm54-coding-plan">China’s Zhipu said to have added GLM-5.4 to coding plan</a></li>

</ul>
</details>

**Tags**: `#LLM architecture`, `#loop transformers`, `#coding models`, `#Zhipu GLM`, `#model release`

---