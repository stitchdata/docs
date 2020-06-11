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
  {% assign all-errors = site.troubleshooting | where_exp:"page","page.type contains 'error'" | sort_natural: "title" %}

  {{ page.summary }}

  {% for section in page.sections %}
  - [{{ section.title }}](#{{ section.anchor }}) - {{ section.summary }}
  {% endfor %}

sections:
  - title: "Account and billing errors"
    anchor: "account-billing-errors"
    summary: "Errors related to billing and account management"
    content: |
      {% assign account-errors = all-errors | where_exp:"page","page.type contains 'account'" %}

      {% for page in account-errors %}
      <span class="h4">
      <a href="{{ page.url | prepend: site.baseurl }}">{{ page.title }}</a>
      </span>
      {{ page.summary }}
      {% endfor %}

  - title: "Integration errors"
    anchor: "integration-errors"
    summary: "Errors applicable to integrations"
    content: |
      {% assign integration-errors = all-errors | where_exp:"page","page.type contains 'integration'" %}

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }}) - {{ subsection.summary | flatify }}
      {% endfor %}

    subsections:
      - title: "Connection errors"
        anchor: "integration-connection-errors"
        summary: &connection-errors "Errors arising from insufficient permissions, incorrect configuration, etc."
        content: |
          {% assign connection-errors = integration-errors | where:"category","connection-errors" %}

          {% for page in connection-errors %}
          <span class="h4">
          <a href="{{ page.url | prepend: site.baseurl }}">{{ page.title }}</a>
          </span>
          {{ page.summary }}
          {% endfor %}

      - title: "Extraction errors"
        anchor: "integration-extraction-errors"
        summary: "Errors that arise during Extraction. These will surface in an integration's Extraction Logs."
        content: |
          {% assign extraction-errors = integration-errors | where:"category","extraction-errors" %}

          {% for page in extraction-errors %}
          <span class="h4">
          <a href="{{ page.url | prepend: site.baseurl }}">{{ page.title }}</a>
          </span>
          {{ page.summary }}
          {% endfor %}

  - title: "Destination errors"
    anchor: "destination-errors"
    summary: "Errors applicable to destinations"
    content: |
      {% assign destination-errors = all-errors | where_exp:"page","page.type contains 'destination'" %}

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }}) - {{ subsection.summary | flatify }}
      {% endfor %}

    subsections:
      - title: "Connection errors"
        anchor: "destination-connection-errors"
        summary: *connection-errors
        content: |
          {% assign connection-errors = destination-errors | where:"category","connection-errors" %}

          {% for page in connection-errors %}
          <span class="h4">
          <a href="{{ page.url | prepend: site.baseurl }}">{{ page.title }}</a>
          </span>
          {{ page.summary }}
          {% endfor %}

      - title: "Loading errors"
        anchor: "destination-loading-errors"
        summary: "Errors that arise during Loading. These will surface in the Notifications tab and in an integration's Loading Reports."
        content: |
          {% assign loading-errors = destination-errors | where:"category","loading-errors" %}

          {% for page in loading-errors %}
          <span class="h4">
          <a href="{{ page.url | prepend: site.baseurl }}">{{ page.title }}</a>
          </span>
          {{ page.summary }}
          {% endfor %}
---