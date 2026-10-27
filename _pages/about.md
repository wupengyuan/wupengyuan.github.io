---
permalink: /
title: About
home: true
description: "Pengyuan Wu — Ph.D. student at Zhejiang University, researching robot learning, embodied navigation, and world models."
redirect_from:
  - /about/
---
<header class="intro-header">
  <h1>Pengyuan Wu</h1>
</header>

<div class="biography" markdown="1">
I am a Ph.D. student at [Zhejiang University](https://www.zju.edu.cn/english/), advised by [Prof. Xuelong Li](https://scholar.google.com/citations?user=ahUibskAAAAJ&hl=zh-CN). I am also enrolled in the joint Ph.D. training program at [Shanghai Artificial Intelligence Laboratory](https://www.shlab.org.cn/).

My research interests are robot learning, embodied navigation, and world models. I received my B.Eng. in Automation from Wuhan University in 2025.
</div>

<section class="publications-section" aria-labelledby="publications-heading">
  <div class="section-heading"><h2 id="publications-heading">Publications</h2></div>
  <p class="section-note">* Equal contribution.</p>
  {% for paper in site.data.papers %}{% include paper-card.html %}{% endfor %}
</section>

<section aria-labelledby="honors-heading">
  <div class="section-heading"><h2 id="honors-heading">Selected honors</h2></div>
  <ul class="award-list">{% for item in site.data.profile.awards %}<li><span class="award-year">{{ item.year }}</span><div>{{ item.title }}</div></li>{% endfor %}</ul>
</section>
