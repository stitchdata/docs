---
title: Troubleshooting Destination Issues
keywords: troubleshooting, destination, trouble, issue, help
permalink: /troubleshooting/destinations/

summary: "Having trouble with your destination? Whether it's an issue with setup or connections, these are some of the most common causes of destination problems."

layout: general
toc: false
feedback: false

intro: |
  {{ page.summary }}

sections:
  - title: "Common issues"
    anchor: "common-issues"
    content: |
      {% assign sorted-docs = site.troubleshooting | sort_natural:'title' %}

      {% for page in sorted-docs %}
      {% if page.type contains "all-destinations" %}
      <span class="h4">
      <a href="{{ page.url | prepend: site.baseurl }}">{{ page.title }}</a>
      </span>
      {{ page.summary }}
      {% endif %}
      {% endfor %}

  - title: "Amazon Redshift and Panoply issues"
    anchor: "amazon-redshift-panoply-issues"
    content: |
      {% for page in sorted-docs %}
      {% if page.type contains "redshift-destination" or page.type contains "panoply-destination" %}
      <span class="h4">
      <a href="{{ page.url | prepend: site.baseurl }}">{{ page.title }}</a>
      </span>
      {{ page.summary }}
      {% endif %}
      {% endfor %}

  # - title: "PostgreSQL issues"
  #   anchor: "postgresql-issues"
  #   content: |
  #     {% for page in sorted-docs %}
  #     {% if page.type contains "postgres-destination" %}
  #     <span class="h4">
  #     <a href="{{ page.url | prepend: site.baseurl }}">{{ page.title }}</a>
  #     </span>
  #     {{ page.summary }}
  #     {% endif %}
  #     {% endfor %}
---