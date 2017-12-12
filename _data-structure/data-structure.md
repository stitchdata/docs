---
title: Stitch Data Structure
permalink: /data-structure/
keywords: data structure, schema, data load, loading data
tags: [replication]
summary: "Resources for learning about how Stitch loads and organizes data into your destination."
toc: false
feedback: false
---
{% include misc/data-files.html %}

{{ page.summary }}

---

## Data Loading by Destination

Every destination handles data differently. Learn about what your destination supports, what it doesn’t, and how Stitch will load your data as a result.

{% assign data-loading = site.data-structure | where:"category","data loading" | sort:"title" %}

{% for page in data-loading %}
### [{{ page.title }}]({{ page.url | prepend: site.baseurl }})
{{ page.summary }}
{% endfor %}

---

## Additional Resources

These resources contain additional detail that builds upon the info covered in each destination's data loading guide. Learn more about how Stitch structures the schemas it creates for integrations, how structural changes are handled, how to resolve record rejections, and more.

{% for page in site.data-structure %}
{% if page.permalink != "/data-structure/" and page.category != "data loading" %}
{% unless page.title contains "Loading Data" %}
### [{{ page.title }}]({{ page.url | prepend: site.baseurl }})
{{ page.summary }}
{% endunless %}
{% endif %}
{% endfor %}