---
layout: default
title: Home
---

<div class="masthead">
  <div class="masthead-date">AI Daily Brief · Horizon Radar</div>
  <div class="masthead-tagline">AI 每日精选 — 从喧嚣中筛出值得读的</div>
</div>

<div id="lang-zh" class="lang-section">

<ul class="article-list">
  {% assign zh_posts = site.posts | where: "lang", "zh" %}
  {% for post in zh_posts limit:20 %}
    {% assign raw_count = post.content | split: "item-tech-news" | size | minus: 1 %}
    {% assign item_count = raw_count | divided_by: 2 %}
    <li>
      <a class="article-card" href="{{ post.url | relative_url }}">
        <div class="article-card-meta">{{ post.date | date: "%Y年%m月%d日" }} · {{ item_count }} 条精选</div>
        <div class="article-card-title">
          {{ post.date | date: "%m月%d日" }} AI 日报
        </div>
      </a>
    </li>
  {% else %}
    <li style="padding:40px 0;text-align:center;color:var(--ink-muted);">
      <em>暂无日报，请稍后再来</em>
    </li>
  {% endfor %}
</ul>

</div>

<div id="lang-en" class="lang-section hidden">

<ul class="article-list">
  {% assign en_posts = site.posts | where: "lang", "en" %}
  {% for post in en_posts limit:20 %}
    {% assign raw_count = post.content | split: "item-tech-news" | size | minus: 1 %}
    {% assign item_count = raw_count | divided_by: 2 %}
    <li>
      <a class="article-card" href="{{ post.url | relative_url }}">
        <div class="article-card-meta">{{ post.date | date: "%B %d, %Y" }} · {{ item_count }} stories</div>
        <div class="article-card-title">
          AI Daily · {{ post.date | date: "%b %d" }}
        </div>
      </a>
    </li>
  {% else %}
    <li style="padding:40px 0;text-align:center;color:var(--ink-muted);">
      <em>No digests yet, check back later</em>
    </li>
  {% endfor %}
</ul>

</div>
