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
I am a Ph.D. student at [Zhejiang University](https://www.zju.edu.cn/english/), advised by Prof. Xuelong Li, and a joint Ph.D. researcher at [Shanghai AI Laboratory](https://www.shlab.org.cn/).

My research interests are robot learning, embodied navigation, and world models. I received my B.Eng. in Automation from Wuhan University in 2025.
</div>

<section class="selected-papers" aria-labelledby="publications-heading">
  <div class="section-heading"><h2 id="publications-heading">Selected publications</h2><a href="{{ '/publications/' | relative_url }}">All publications</a></div>
  <p class="section-note">* Equal contribution.</p>
  {% for paper in site.data.papers %}{% if paper.featured %}{% include paper-card.html %}{% endif %}{% endfor %}
</section>
