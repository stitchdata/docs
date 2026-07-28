---
title: Welcome to Stitch Documentation
layout: page
toc: false
enterprise: false
feedback: false
permalink: index.html
summary: "Guides and resources for setting up and managing your Stitch data pipeline."
---

{% include misc/data-files.html %}

<p class="intro">{{ site.description }} Not using Stitch yet? Start your <a href="https://www.qlik.com/us/trial/qlik-talend-cloud?utm_source=stitch">Qlik Talend Cloud® Free 14-Day Trial | Connect, Clean & Shape Your Data.</a></p>
<hr />

{% assign categories = site.documents | where:"level","category" | sort:"weight" %}

<ul class="tiles two-columns link-tiles">
{% for category in categories %}
	<li>
		<a href="{{ site.baseurl | append: category.url }}">
			<img src="{{ site.baseurl }}/images/icons/{{ category.icon }}.svg" style="max-height: 60px;" alt="{{ category.display-title }}">
			<strong>{{ category.display-title }}</strong>
			{{ category.display-summary | flatify }}
		</a>
	</li>
{% endfor %} 
</ul>