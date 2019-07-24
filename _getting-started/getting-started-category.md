---
title: Getting Started
permalink: /getting-started/
keywords: getting started get started stitch onboarding new user set up stitch
summary: "Resources and guides for learning about Stitch and setting up your own data pipeline."
feedback: false

layout: page
sidebar: stitch

level: "category"
icon: "user-profile"
weight: 2
display-title: "Getting Started"
display-summary: "todo"

key: "getting-started"

---

{% include misc/data-files.html %}

{{ page.summary }}

---

{% assign guides = site.getting-started | where_exp:"guide","guide.title != page.title" |sort:"weight" %}

{% for guide in guides %}
<span class="h3"><a href="{{ guide.url | prepend: site.baseurl }}">{{ guide.title }}</a></span>
{{ guide.summary }}
{% endfor %}