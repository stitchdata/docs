---
title: testing
permalink: /testing/
---

{% assign intercom-tables = site.integration-schemas | where:"tap","intercom" %}

{% assign this-versions-tables = intercom-tables | where:"version","15-10-2015" %}

{% for table in this-versions-tables %}
- {{ table.name }} : {{ table.version }}
{% endfor %}