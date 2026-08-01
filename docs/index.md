---
layout: default
title: Home
---

<!-- Lead -->
<div class="lead">
AI 信息雷达每日精选 — 从全球 RSS 源中自动筛选、评分、生成中英双语简报。从喧嚣中筛出值得读的。
</div>

<!-- Article List -->
{% for post in site.posts limit:20 %}
<div class="article">
  <div class="article-num">
    {{ forloop.index | minus: 1 | times: 0 | plus: post.date | date: "%d" }}
    <small>{{ post.date | date: "%b" }}</small>
  </div>
  <div class="article-body">
    <h2><a href="{{ post.url | relative_url }}">{{ post.date | date: "%Y年%m月%d日" }} AI 日报</a></h2>
    <div class="article-meta">
      <span class="tag">{{ post.lang | default: "ZH" }}</span>
      {{ post.date | date: "%B %d, %Y" }}
    </div>
    <p class="article-summary">
      {% assign lines = post.content | split: "item-tech-news" %}
      {% assign count = lines | size | minus: 1 | divided_by: 2 %}
      {% if post.lang contains "zh" %}
        中文版 · {{ count }} 条精选
      {% else %}
        English Edition · {{ count }} items
      {% endif %}
    </p>
  </div>
</div>
{% else %}
<div style="text-align:center;padding:60px 0;color:var(--brown-gray);">
  <p style="font-style:italic;font-size:16px;">暂无日报，请稍后再来</p>
</div>
{% endfor %}
