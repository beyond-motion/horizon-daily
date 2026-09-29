---
layout: default
title: "Horizon Summary: 2026-09-29 (EN)"
date: 2026-09-29
lang: en
---

> From 8 items, 3 important content pieces were selected

---

**Technology News**
1. [EFF Report Alleges DraftKings Uses AI to Target Chronic Gamblers](#item-tech-news-1) ⭐️ 7.0/10
2. [Privacy analysis of web and mobile conversational AI agents](#item-tech-news-2) ⭐️ 7.0/10
3. [Anthropic Releases Claude Sonnet 5.5, Now Powering claude.ai&\#x27;s Free Tier](#item-tech-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [EFF Report Alleges DraftKings Uses AI to Target Chronic Gamblers](https://www.eff.org/deeplinks/2026/09/draftkings-using-ai-supercharge-harms-online-behavioral-advertising) ⭐️ 7.0/10

An Electronic Frontier Foundation report alleges that DraftKings uses AI-driven behavioral advertising to target chronic gamblers, an item the analysis frames as an AI-ethics and tech-regulation concern rather than a technical breakthrough. The central claim is that such targeting can supercharge harms for users already showing signs of problem gambling. No detailed technical description of the models, data sources, or targeting mechanisms is available in the supplied excerpt, so the specific methods remain unverified here. The item also notes that the piece drew extensive debate on Hacker News.

hackernews · paimapi · Sep 29, 16:30 · [Discussion](https://news.ycombinator.com/item?id=49896050)

**「Background」** Behavioral advertising uses data collected about a person&\#x27;s past activity to select the ads they see, and the Electronic Frontier Foundation has long argued that the practice should be banned outright. EFF&\#x27;s report applies that position to online sports betting, describing DraftKings as using AI on its own betting data to find and target gamblers likely to lose money. Reporting on the same claims says DraftKings began building a model in mid-2023 to predict how promotions would translate into a customer&\#x27;s wins or losses.

**「Impact」** According to the EFF report, DraftKings&\#x27; use of AI-driven behavioral targeting would fall hardest on users already exhibiting signs of problem gambling, strengthening the case for treating algorithmic ad targeting in gambling as a consumer-protection and regulatory matter. The supplied excerpt contains no technical detail or company response, so the specific targeting methods and their measured effects on at-risk users remain unverified.

**「Community Discussion」** Commenters largely accepted the premise, with one citing a ProPublica investigation that worked with gambling-addiction experts to test how DraftKings responds to signs of a gambling problem, and another recalling a data science graduate course that studied how Caesars Entertainment modeled its &quot;most valuable customers&quot; and intervened when they appeared ready to leave. Others argued that legalizing sports betting and online gambling was a mistake, contrasted the lack of protections for gamblers with accredited-investor requirements for risky investments, and drew a sardonic parallel to compulsive use of AI subscription plans.

<details><summary>References</summary>
<ul>
<li><a href="https://www.eff.org/deeplinks/2026/09/draftkings-using-ai-supercharge-harms-online-behavioral-advertising">DraftKings Is Using AI to Supercharge the Harms of Online...</a></li>
<li><a href="https://www.gambling.com/us/news/draftkings-ai-ad-targeting-draws-privacy-backlash">DraftKings AI Ad Targeting Draws Privacy Backlash</a></li>
<li><a href="https://futurism.com/artificial-intelligence/draftkings-ai-problem-gamblers">DraftKings Is Using AI to Identify Problem Gamblers and Get Them...</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#behavioral advertising`, `#online gambling`, `#machine learning`, `#tech regulation`

---

<a id="item-tech-news-2"></a>
### [Privacy analysis of web and mobile conversational AI agents](https://jorgegarciaherrero.com/wp-content/interactivos/20260916-Prompt-like-a-butterfly-sting-like-a-tracker-%28clean%29.pdf) ⭐️ 7.0/10

The linked PDF presents a privacy analysis of conversational AI agents on the web and mobile, and the Hacker News discussion adds community reports of tracking-like prompt telemetry and weak privacy protections. Commenters report that ChatGPT on the web periodically sends unfinished prompts to a \`conversation/prepare\` endpoint before the user sends them, potentially to pre-warm a cache or to track writing cadence, error-correction style, and evolving ideas. Another commenter says Perplexity equates a UUID in the URL with privacy, yet visiting a past Perplexity search URL exposes the full conversation. The discussion also compares the issue to unpublished drafts in private OpenAI Codex sessions and argues that prompts and results that should stay private often do not. The item did not include the paper&\#x27;s full text, so its detailed findings and methodology are not summarized here.

hackernews · damaru2 · Sep 29, 09:03 · [Discussion](https://news.ycombinator.com/item?id=49890226)

**「Background」** Conversational AI agents are chat-based assistants on web and mobile platforms, and the item examines them through the peer-reviewed paper “Prompt like a Butterfly, Sting like a Tracker,” which was accepted at PoPETs 2027 and led by Narseo Vallina-Rodríguez’s team. The paper’s premise is that as prominent providers such as OpenAI adopt advertising-based business models, traditional web and mobile tracking techniques are expanding into conversational AI services, making prompt and interaction telemetry a privacy issue. The accompanying community thread frames the practical stakes with reports of tracking-like prompt telemetry, including unfinished prompts sent before submission and AI chat URLs whose UUIDs expose full conversations.

**「Impact」** For users of web-based conversational AI services, the reported behavior means unfinished prompts and URL-accessible conversation histories may be exposed or analyzed before users intend to share them, depending on the provider.

**「Community discussion」** Commenters broadly agree that conversational AI services offer weak privacy, with concrete examples of pre-send prompt telemetry and URL-based conversation exposure; one commenter argues this makes open models the necessary alternative, while another speculates that ad/tracking mechanisms are rushed or driven by profitability demands. The thread includes concern that AI companies hoard data even when ad companies are competitors, alongside a humorous comparison to Milhouse telling secrets to Groundskeeper Willie.

<details><summary>References</summary>
<ul>
<li><a href="https://dspace.networks.imdea.org/handle/20.500.12761/2073">Prompt like a Butterfly, Sting like a Tracker: A Privacy Analysis of ...</a></li>
<li><a href="https://jorgegarciaherrero.com/en/prompt-like-a-butterfly-sting-like-a-tracker/">Infographic of the paper &quot; Prompt like a Butterfly , sting like a tracker &amp;quo...</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#conversational AI`, `#web tracking`, `#LLM telemetry`, `#mobile security`

---

<a id="item-tech-news-3"></a>
### [Anthropic Releases Claude Sonnet 5.5, Now Powering claude.ai&\#x27;s Free Tier](https://simonwillison.net/2026/Sep/28/claude-sonnet-5-5/) ⭐️ 7.0/10

Anthropic released Claude Sonnet 5.5, a same-priced successor to Sonnet 5 that the company says &quot;runs 30%+ faster, and costs up to 30% less for most work&quot;; Simon Willison notes it appears to beat Sonnet 5 on every benchmark and should be cheaper to run. Sonnet 5.5 reproduces the same failure seen in Opus 5.5 at &quot;max&quot; thinking effort: the pelican-riding-a-bicycle SVG task consumed 128,000 tokens at a cost of $1.28 before running out of tokens and failing to produce an SVG. At &quot;xhigh&quot; effort the same task produced a good result in 41 seconds for 5.74 cents, and Willison reports Sonnet 5.5 is almost as good as Opus 5.5 on some coding tasks, including viral 3D animation tricks. Sonnet 5.5 is now the model behind the free tier on claude.ai, which Willison contrasts with OpenAI&\#x27;s ChatGPT free tier running Luna 5.6, calling Anthropic&\#x27;s free offering the more capable one at present. Anthropic&\#x27;s announcement reiterates that Haiku 5.5 will arrive &quot;in the coming weeks.&quot;

rss · Simon Willison · Sep 28, 22:07

**「Background」** Anthropic&\#x27;s Claude family is organized into tiers — Haiku, Sonnet and Opus — where Sonnet serves as the mid-tier workhorse, and point releases such as 5.5 generally retain the tier&\#x27;s pricing while improving capability. Sonnet 5.5 keeps Sonnet 5&\#x27;s price of $2 per million input tokens and $10 per million output tokens, with cache reads at $0.20 per million. The release is also positioned in a competitive market: the item notes that Sonnet 5.5 now backs the free tier on claude.ai, that Anthropic says Haiku 5.5 will arrive &quot;in the coming weeks&quot;, and that the author hopes it will be price-competitive with OpenAI&\#x27;s GPT-6 Luna.

**「Impact」** Developers and free-tier claude.ai users get a model that is reportedly faster and up to 30% cheaper at the same price while matching or exceeding Sonnet 5 on benchmarks, though the max-thinking-effort token exhaustion bug remains a practical cost and reliability risk for anyone pushing the highest effort settings.

<details><summary>References</summary>
<ul>
<li><a href="https://computingforgeeks.com/claude-sonnet-5-5-released-features-benchmarks/">Claude Sonnet 5.5: Benchmarks, Pricing, Tested | ComputingForGeeks</a></li>
<li><a href="https://www.digitalapplied.com/blog/claude-sonnet-5-5-launch-pricing-benchmarks-2026">Claude Sonnet 5.5: Pricing, Benchmarks and Safeguards</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#Claude`, `#LLM`, `#AI models`, `#model release`

---