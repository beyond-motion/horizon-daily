---
layout: default
title: Home
---

<div class="home-hero">
  <div class="home-kicker">AI Daily Brief</div>
  <h1 class="home-headline">从喧嚣中筛出值得读的</h1>
  <p class="home-subtitle">Horizon 信息雷达每日精选 — 全球科技前沿，人工评分筛选。</p>
</div>

<ul class="article-list">
  {% for post in site.posts limit:20 %}
    {% assign raw_count = post.content | split: "item-tech-news" | size | minus: 1 %}
    {% assign item_count = raw_count | divided_by: 2 %}
    {% assign clean_date = post.date | date: "%Y年%m月%d日" %}
    <li>
      <a class="article-card" href="{{ post.url | relative_url }}">
        <div class="article-kicker">每日精选 · {{ item_count }} 条</div>
        <div class="article-title">{{ clean_date }} AI 日报</div>
        <div class="article-meta">{{ post.date | date: "%B %d, %Y" }}</div>
      </a>
    </li>
  {% else %}
    <li style="padding:48px 0;text-align:center;color:var(--gray-500);">
      <em>暂无日报，请稍后再来</em>
    </li>
  {% endfor %}
</ul>
