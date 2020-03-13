---
title: Troubleshooting Errors
keywords: troubleshooting, trouble, issue, help, error, errors, notification
permalink: /troubleshooting/error-notifications/

summary: "If you’ve received an in-app or email error notification, here’s where you’ll find the resources you need to get things back on track."

layout: general
toc: false
feedback: false

intro: |
  {% include misc/data-files.html %}
  {% assign sorted-docs = site.troubleshooting | sort_natural:'title' %}

  {{ page.summary }}

  {% for section in page.sections %}
  - [{{ section.title }}](#{{ section.anchor }})
  {% endfor %}

sections:
  - title: "Account and billing errors"
    anchor: "account-billing-errors"
    content: |
      {% for page in sorted-docs %}
      {% if page.type contains "account" and page.type contains "error" %}
      <span class="h4">
      <a href="{{ page.url | prepend: site.baseurl }}">{{ page.title }}</a>
      </span>
      {{ page.summary }}
      {% endif %}
      {% endfor %}

  - title: "Destination errors"
    anchor: "destination-errors"
    content: |
      {% for page in sorted-docs %}
      {% if page.type contains "destination" and page.type contains "error" %}
      <span class="h4">
      <a href="{{ page.url | prepend: site.baseurl }}">{{ page.title }}</a>
      </span>
      {{ page.summary }}
      {% endif %}
      {% endfor %}

  - title: "Integration errors"
    anchor: "integration-errors"
    content: |
      {% for page in sorted-docs %}
      {% if page.type contains "integration" and page.type contains "error" %}
      <span class="h4">
      <a href="{{ page.url | prepend: site.baseurl }}">{{ page.title }}</a>
      </span>
      {{ page.summary }}
      {% endif %}
      {% endfor %}
---