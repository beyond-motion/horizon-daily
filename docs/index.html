---
layout: default
title: Home
---

<!-- Lead -->
<div class="lead">
AI 信息雷达每日精选 — 从全球 RSS 源中自动筛选、评分、生成中英双语简报。从喧嚣中筛出值得读的。
</div>

<!-- Article List — 按日期去重，一天一条 -->
{% assign seen_dates = "" %}
{% for post in site.posts %}
  {% assign post_date = post.date | date: "%Y-%m-%d" %}
  {% unless seen_dates contains post_date %}
    {% assign seen_dates = seen_dates | append: post_date | append: "," %}
    {% assign clean_date = post.date | date: "%Y年%-m月%-d日" %}
    {% assign eng_date = post.date | date: "%B %-d, %Y" %}
    {% assign month_short = post.date | date: "%b" %}
    {% assign day_num = post.date | date: "%d" %}
    {% assign zh_url = "" %}
    {% assign en_url = "" %}
    {% for p in site.posts %}
      {% assign pd = p.date | date: "%Y-%m-%d" %}
      {% if pd == post_date %}
        {% if p.lang contains "zh" %}{% assign zh_url = p.url %}{% endif %}
        {% if p.lang contains "en" %}{% assign en_url = p.url %}{% endif %}
      {% endif %}
    {% endfor %}
    <div class="article">
      <div class="article-num">
        {{ day_num }}
        <small>{{ month_short }}</small>
      </div>
      <div class="article-body">
        <h2><a href="{{ zh_url | default: en_url | relative_url }}">{{ clean_date }} AI 日报</a></h2>
        <div class="article-meta">
          {% if zh_url != "" %}<span class="tag">中文</span>{% endif %}
          {% if en_url != "" %}<span class="tag">EN</span>{% endif %}
          {{ eng_date }}
        </div>
        <p class="article-summary">
          {% if zh_url != "" %}<a href="{{ zh_url | relative_url }}">阅读中文版</a>{% endif %}
          {% if zh_url != "" and en_url != "" %} · {% endif %}
          {% if en_url != "" %}<a href="{{ en_url | relative_url }}">Read in English</a>{% endif %}
        </p>
      </div>
    </div>
  {% endunless %}
{% else %}
<div style="text-align:center;padding:60px 0;color:var(--brown-gray);">
  <p style="font-style:italic;font-size:16px;">暂无日报，请稍后再来</p>
</div>
{% endfor %}
