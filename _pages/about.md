---
permalink: /
title: About
home: true
description: "Pengyuan Wu — Ph.D. student at Zhejiang University, researching robot learning, embodied navigation, and world models."
redirect_from:
  - /about/
---
<header class="intro-header">
  <p class="eyebrow">Robot learning · Embodied AI</p>
  <h1>Pengyuan Wu<span class="name-dot">.</span></h1>
  <p class="intro-subtitle">Building agents that adapt, imagine, and act.</p>
</header>

<div class="biography" markdown="1">
I am a Ph.D. student in **Computer Science and Technology** at [Zhejiang University](https://www.zju.edu.cn/english/), advised by **Prof. Xuelong Li**, and a joint Ph.D. researcher at [Shanghai Artificial Intelligence Laboratory](https://www.shlab.org.cn/).

My research focuses on **embodied intelligence**: learning robot policies that generalize to changing environments, using world models to reason about what comes next, and building 3D scenes and data for learning in simulation.

Previously, I received my B.Eng. in Automation from **Wuhan University** in 2025, where I worked with Prof. Xiangtao Zhuan.
</div>

<section class="research-section" aria-labelledby="research-heading">
  <div class="section-heading"><h2 id="research-heading">Research interests</h2><span class="section-index" aria-hidden="true">01 /</span></div>
  <div class="research-grid">
    {% for topic in site.data.profile.research %}
      <div class="research-topic"><span class="topic-label">{{ topic.label }}</span><h3>{{ topic.title }}</h3><p>{{ topic.description }}</p></div>
    {% endfor %}
  </div>
</section>

<section class="selected-papers" aria-labelledby="publications-heading">
  <div class="section-heading"><h2 id="publications-heading">Selected publications</h2><a href="{{ '/publications/' | relative_url }}">View all <span aria-hidden="true">↗</span></a></div>
  <p class="section-note">Peer-reviewed papers and public preprints. * Equal contribution.</p>
  {% for paper in site.data.papers %}{% if paper.featured %}{% include paper-card.html %}{% endif %}{% endfor %}
</section>

<section class="education-section" aria-labelledby="education-heading">
  <div class="section-heading"><h2 id="education-heading">Education</h2><span class="section-index" aria-hidden="true">03 /</span></div>
  {% for item in site.data.profile.education %}
    <div class="timeline-item"><div class="timeline-top"><h3>{{ item.institution }}</h3><span>{{ item.dates }}</span></div><p class="timeline-role">{{ item.degree }}</p><p class="timeline-detail">{{ item.detail }}</p></div>
  {% endfor %}
</section>

<section class="contact-section" aria-labelledby="contact-heading">
  <p class="eyebrow">Get in touch</p>
  <h2 id="contact-heading">Interested in embodied intelligence?</h2>
  <p>I welcome conversations about robot learning, navigation, and world models.</p>
  <a href="mailto:{{ site.author.email }}">{{ site.author.email }} <span aria-hidden="true">↗</span></a>
</section>
