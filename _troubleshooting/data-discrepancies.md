---
title: Troubleshooting Data Discrepancies
keywords: troubleshooting, integration, trouble, issue, help, data discrepancy, discrepancies, wrong data, incorrect data
permalink: /troubleshooting/data-discrepancies/

summary: "Data discrepancies can surface as missing records, incorrect values, or fields not being correctly typed. If something in your data warehouse doesn't look quite right, these resources will help you get to the root of the problem."

layout: general
toc: false
feedback: false

intro: |
  {{ page.summary }}

sections:
  - title: "Places to start"
    anchor: "places-to-start"
    content: |
      Pinpointing the cause of a data discrepancy has the potential to require quite a bit of investigation. To increase efficiency, we recommend using these three resources to perform quick checks on some of the more obvious and common causes.

      {% assign sorted-docs = site.troubleshooting | sort_natural:'title' %}

      {% for page in sorted-docs %}
      {% if page.type contains "discrepancy" %}
      {% if page.title == "Data Discrepancy Troubleshooting Guide" or page.title == "Known Third-Party Issues" or page.title == "Third-Party Integration Downtime" %}
      <span class="h4">
      <a href="{{ page.url | prepend: site.baseurl }}">{{ page.title }}</a>
      </span>
      {{ page.summary }}
      {% endif %}
      {% endif %}
      {% endfor %}

  - title: "Additional resources"
    anchor: "additional-resources"
    content: |
      Pinpointing the cause of a data discrepancy has the potential to require quite a bit of investigation. To increase efficiency, we recommend using these three resources to perform quick checks on some of the more obvious and common causes.

      {% assign sorted-docs = site.troubleshooting | sort_natural:'title' %}

      {% for page in sorted-docs %}
      {% if page.type contains "discrepancy" %}
      {% unless page.title == "Data Discrepancy Troubleshooting Guide" or page.title == "Known Third-Party Issues" or page.title == "Third-Party Integration Downtime" %}
      <span class="h4">
      <a href="{{ page.url | prepend: site.baseurl }}">{{ page.title }}</a>
      </span>
      {{ page.summary }}
      {% endunless %}
      {% endif %}
      {% endfor %}
---