---
layout: default
title: Home
---

<div class="masthead">
  <div class="masthead-date">AI Daily Brief · Horizon Radar</div>
  <div class="masthead-tagline">AI 每日精选 — 从喧嚣中筛出值得读的</div>
</div>

<ul class="article-list">
  {% for post in site.posts limit:20 %}
    <li>
      <a class="article-card" href="{{ post.url | relative_url }}">
        <div class="article-card-meta">{{ post.date | date: "%Y年%m月%d日" }}</div>
        <div class="article-card-title">{{ post.title }}</div>
      </a>
    </li>
  {% else %}
    <li style="padding:40px 0;text-align:center;color:var(--ink-muted);">
      <em>暂无日报，请稍后再来</em>
    </li>
  {% endfor %}
</ul>
