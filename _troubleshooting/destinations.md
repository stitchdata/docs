---
title: Troubleshooting Destination Issues
keywords: troubleshooting, destination, trouble, issue, help
permalink: /troubleshooting/destinations/

summary: "Having trouble with your destination? Whether it's an issue with setup or connections, these are some of the most common causes of destination problems."
toc: false
feedback: false
---
{% include misc/data-files.html %}

{{ page.summary }}

---

{% assign sorted-docs = site.troubleshooting | sort:'title' %}

## Common Issues

{% for page in sorted-docs %}
{% if page.type contains "all-destinations" %}
### [{{ page.title }}]({{ page.url | prepend: site.baseurl }})
{{ page.summary }}
{% endif %}
{% endfor %}

---

## Amazon Redshift / Panoply

{% for page in sorted-docs %}
{% if page.type contains "redshift-destination" or page.type contains "panoply-destination" %}
### [{{ page.title }}]({{ page.url | prepend: site.baseurl }})
{{ page.summary }}
{% endif %}
{% endfor %}

---

{% comment %}
## Google BigQuery
{% for page in sorted-docs %}
{% if page.type contains "bigquery-destination" %}
### [{{ page.title }}]({{ page.url | prepend: site.baseurl }})
{{ page.summary }}
{% endif %}
{% endfor %}
---
{% endcomment %}

## PostgreSQL

{% for page in sorted-docs %}
{% if page.type contains "postgres-destination" %}
### [{{ page.title }}]({{ page.url | prepend: site.baseurl }})
{{ page.summary }}
{% endif %}
{% endfor %}