---
title: Account & Security
permalink: /account-security/
keywords: billing, plan, change plan, cancel, cancel account, delete, remove
summary: "Resources for everything account-related: Managing billing details, inviting team members, security info, and more."
feedback: false

---

{% include misc/data-files.html %}

{{ page.summary }}

---

{% assign sections = "getting-started|account-settings|team-members|notifications|billing|security" | split:"|" %}

{% for section in sections %}

## {{ section | capitalize | replace:"-"," " }}

{% assign pages = site.account-security | where:"type",section | sort:"weight" %}

{% for page in pages %}
<span class="h3"><a href="{{ page.url | prepend: site.baseurl }}">{{ page.title | capitalize | replace:"stitch","Stitch" | replace:"faq","FAQ" | replace:"api","API" }}</a></span>
{{ page.summary }}
{% endfor %}

{% unless forloop.last == true %}
---
{% endunless %}
{% endfor %}