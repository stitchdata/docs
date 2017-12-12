---
title: Loading Data into Your Stitch Destination
permalink: /data-structure/loading-stitch-data-into-destinations
keywords: bigquery, panoply, redshift, postgres, postgresql, data warehouse, destination, data structure, loading data
tags: [replication]
summary: "Every destination handles data differently. Learn about what your destination supports, what it doesn't, and how Stitch will load your data as a result."

toc: true
feedback: false
---

{% include misc/data-files.html %}

{{ page.summary }}

{% assign data-loading = site.data-structure | where:"category","data loading" | sort:"title" %}

{% for page in data-loading %}
### [{{ page.title }}]({{ page.url | prepend: site.baseurl }})
{{ page.summary }}
{% endfor %}