---
title: Troubleshooting Integration Issues
keywords: troubleshooting, integration, trouble, issue, help, database integration, saas integration
permalink: /troubleshooting/integrations/

summary: "Having trouble connecting your database or SaaS integration? Investigating a data discrepancy? Here you'll find resources for some of the most common causes of connection troubles and data discrepancies related to integrations."
toc: false
feedback: false
---

{{ page.summary }}

---

## Common Integration Issues

{% assign sorted-docs = site.troubleshooting | sort:'title' %}

{% for page in sorted-docs %}
{% if page.type contains "all-integrations" %}
### [{{ page.title }}]({{ page.url | prepend: site.baseurl }})
{{ page.summary }}
{% endif %}
{% endfor %}

---

## Database Integrations

{% for page in sorted-docs %}
{% if page.type contains "database-integration" %}
### [{{ page.title }}]({{ page.url | prepend: site.baseurl }})
{{ page.summary }}
{% endif %}
{% endfor %}

---

## SaaS Integrations

{% for page in sorted-docs %}
{% if page.type contains "saas-integration" %}
### [{{ page.title }}]({{ page.url | prepend: site.baseurl }})
{{ page.summary }}
{% endif %}
{% endfor %}