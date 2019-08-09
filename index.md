---
title: Welcome to Stitch Documentation
layout: page-no-edit
toc: false
enterprise: false
permalink: index.html
summary: "Guides and resources for setting up and managing your Stitch data pipeline."
---
{% include misc/data-files.html %}

<p class="intro">{{ site.description }} Not using Stitch yet? Start your <a href="https://www.stitchdata.com/signup/">free trial.</a></p> 
<hr />

{% assign categories = site.documents | where:"level","category" | sort:"weight" %}

<ul class="tiles">
{% for category in categories %}
	<li style="width: 45%">
		<a href="{{ site.baseurl | append: category.url }}">
			<img src="{{ site.baseurl }}/images/icons/{{ category.icon }}.svg" style="max-height: 60px;" alt="TODO">
		</a>
		<strong>{{ category.display-title }}</strong><br>
		{{ category.display-summary | flatify }}
	</li>
{% endfor %} 
</ul>