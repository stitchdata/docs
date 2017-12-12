---
title: Troubleshooting Data Discrepancies
keywords: troubleshooting, integration, trouble, issue, help, data discrepancy, discrepancies, wrong data, incorrect data
permalink: /troubleshooting/data-discrepancies/

summary: "Data discrepancies can surface as missing records, incorrect values, or fields not being correctly typed. If something in your data warehouse doesn't look quite right, these resources will help you get to the root of the problem."
toc: false
feedback: false
---
{% include misc/data-files.html %}
{% assign troubleshooting = site.troubleshooting | sort:"title" %}


{{ page.summary }}

---

## Places to Start

Pinpointing the cause of a data discrepancy has the potential to require quite a bit of investigation. To increase efficiency, we recommend using these three resources to perform quick checks on some of the more obvious and common causes.

{% for page in troubleshooting %}
{% if page.type contains "discrepancy" %}
{% if page.title == "Data Discrepancy Troubleshooting Guide" or page.title == "Known Third-Party Issues" or page.title == "Third-Party Integration Downtime" %}
### [{{ page.title }}]({{ page.url | prepend: site.baseurl }})
{{ page.summary }}
{% endif %}
{% endif %}
{% endfor %}

---

## Additional & Integration-Specific Resources

{% for page in troubleshooting %}
{% if page.type contains "discrepancy" %}
{% unless page.title == "Data Discrepancy Troubleshooting Guide" or page.title == "Known Third-Party Issues" or page.title == "Third-Party Integration Downtime" %}
### [{{ page.title }}]({{ page.url | prepend: site.baseurl }})
{{ page.summary }}
{% endunless %}
{% endif %}
{% endfor %}