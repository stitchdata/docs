---
title: Destination Connection Error Reference
keywords: troubleshooting, destination, destination, trouble, issue, help, error, errors, connection issue, connection
tags: [troubleshooting_destinations, troubleshooting_integrations, troubleshooting_errors]
layout: general

permalink: /troubleshooting/destinations/destination-connection-error-reference
redirect_from: 
  - /troubleshooting/destination-connection-errors
  - /troubleshooting/destinations/destination-connection-errors

summary: "Resolve errors related to connecting to your Stitch destination."
type: "all-destinations, error"

level: "guide"
top-level: ""
# category: "connection-errors"
type: "all-destinations, destination, error"
popular: true

intro: |
  Stitch periodically performs checks on the connection to your destination to ensure the connection remains active and healthy. Below are some of the most common errors you might see if Stitch has trouble performing the connection check to your destination and how to resolve them.

  In this reference:

  {% for section in page.sections %}
  - [{{ section.title }}](#{{ section.anchor }})
  {% endfor %}

sections:
  - title: "Common connection errors"
    anchor: "common-error-reference"
    content: |
      {% assign errors = site.data.errors.connection.common.destinations | sort_natural:"message" %}

      {% assign connection = "destination" %}
      {% assign settings-page = "dw-settings" %}

      The following errors are applicable to all destinations:

      {% include troubleshooting/error-messages.html top-anchor="common-error-reference" display-name="Common" %}

  - title: "Amazon S3 connection errors"
    anchor: "amazon-s3-error-reference"
    content: |
      {% assign errors = site.data.errors.connection.destinations.amazon-s3 | sort_natural:"message" %}

      {% include troubleshooting/error-messages.html top-anchor="amazon-s3-error-reference" display-name="Amazon S3" %}
---
{% include misc/data-files.html %}