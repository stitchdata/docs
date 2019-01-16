---
title: Destination Connection Errors
keywords: troubleshooting, destination, destination, trouble, issue, help, error, errors, connection issue, connection
tags: [troubleshooting_destinations, troubleshooting_errors]
layout: general

permalink: /troubleshooting/destinations/destination-connection-errors
redirect_from: /troubleshooting/destination-connection-errors

summary: "Stitch periodically performs checks on the connection to your destination to ensure the connection remains active and healthy. In this article are some of the most common errors you might see if Stitch has trouble performing the connection check to your destination and how to resolve them."
type: "all-destinations, error"

sections:
  - content: |
      Stitch periodically performs checks on the connection to your database to ensure the connection remains active and healthy. Below are some of the most common errors you might see if Stitch has trouble performing the connection check to your database and how to resolve them.

  - title: "Using this guide"
    anchor: "using-this-guide"
    content: |
      In the next section is a list of the connection errors that might arise for destinations in Stitch. Every error in this list will have the following info:

      {% include troubleshooting/error-messages.html content-type="error-fields" %}

  - title: "Error list"
    anchor: "error-list"
    content: |
      {% assign type = "destination" %}
      {% assign page-name = app.page-names.dw-settings %}

      {% assign common-errors = site.data.errors.connection-check.common-database.all %}
      {% assign errors = site.data.errors.connection-check.destinations.all | concat: common-errors | sort: "message" %}

      {% include troubleshooting/error-messages.html content-type="error-list" %}

  - title: "Contacting support"
    anchor: "contact-support"
    content: |
      To help us troubleshoot the problem quickly, we ask that you provide us with the following:

      1. **The exact error you received.** The full text or a screenshot is ideal.
      2. **The type of destination experiencing the issue.** For example: Redshift, PostgreSQL-RDS.
      3. **Verification that Stitch's IP addresses have been correctly whitelisted,** if applicable to your destination type.

    subsections:
      - title: "Don't see the error here?"
        anchor: "missing-error"
        content: |
          If the error you received isn't listed here, contact support and then [let us know through a GitHub issue]({{ site.github_issue }}{:target="new"}.
---
{% include misc/data-files.html %}