---
title: Troubleshooting Integration Issues
keywords: troubleshooting, integration, trouble, issue, help, database integration, saas integration
permalink: /troubleshooting/integrations/

summary: "Having trouble connecting your database or SaaS integration? Investigating a data discrepancy? Here you'll find resources for some of the most common causes of connection troubles and data discrepancies related to integrations."

layout: general
toc: false
feedback: false

intro: |
  {{ page.summary }}

sections:
  - title: "Common integration issues"
    anchor: "common-integration-issues"
    content: |
      {% assign sorted-docs = site.troubleshooting | sort_natural:'title' %}

      {% for page in sorted-docs %}
      {% if page.type contains "all-integrations" %}
      <span class="h4">
      <a href="{{ page.url | prepend: site.baseurl }}">{{ page.title }}</a>
      </span>
      {{ page.summary }}
      {% endif %}
      {% endfor %}

  - title: "Database integration issues"
    anchor: "database-integration-issues"
    content: |
      {% for page in sorted-docs %}
      {% if page.type contains "database-integration" %}
      <span class="h4">
      <a href="{{ page.url | prepend: site.baseurl }}">{{ page.title }}</a>
      </span>
      {{ page.summary }}
      {% endif %}
      {% endfor %}

  - title: "SaaS integration issues"
    anchor: "saas-integration-issues"
    content: |
      {% for page in sorted-docs %}
      {% if page.type contains "saas-integration" %}
      <span class="h4">
      <a href="{{ page.url | prepend: site.baseurl }}">{{ page.title }}</a>
      </span>
      {{ page.summary }}
      {% endif %}
      {% endfor %}
---