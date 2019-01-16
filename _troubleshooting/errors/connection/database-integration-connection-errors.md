---
title: Database Integration Connection Errors
keywords: troubleshooting, integration, database integration, trouble, issue, help, error, errors, connection issue, connection
tags: [database_integrations, troubleshooting_integrations, troubleshooting_errors]
layout: general

permalink: /troubleshooting/integrations/database-connection-errors
redirect_from: /troubleshooting/database-integration-connection-errors
## Some users may experience a blip while the redirect works - it's normal. 

summary: "Stitch periodically performs checks on the connection to your database to ensure the connection remains active and healthy. In this article are some of the most common errors you might see if Stitch has trouble performing the connection check to your database and how to resolve them."
type: "database-integration, error"

sections:
  - content: |
      Stitch periodically performs checks on the connection to your database to ensure the connection remains active and healthy. Below are some of the most common errors you might see if Stitch has trouble performing the connection check to your database and how to resolve them.

  - title: "Using this guide"
    anchor: "using-this-guide"
    content: |
      In the next section is a list of the connection errors that might arise for database integrations in Stitch. Every error in this list will have the following info:

      {% include troubleshooting/error-messages.html content-type="error-fields" %}

  - title: "Error list"
    anchor: "error-list"
    content: |
      {% assign type = "database" %}
      {% assign page-name = app.page-names.int-settings %}

      {% assign common-errors = site.data.errors.connection-check.common-database.all %}
      {% assign errors = site.data.errors.connection-check.databases.all | concat: common-errors | sort: "message" %}

      {% include troubleshooting/error-messages.html %}

  - title: "Contacting support"
    anchor: "contact-support"
    content: |
      To help us troubleshoot the problem quickly, we ask that you provide us with the following:

      1. **The exact error you received.** The full text or a screenshot is ideal.
      2. **The type of database experiencing the issue.** For example: MySQL-RDS.
      3. **The display name of the integration in Stitch.** This helps our team quickly identify the correct integration when pulling up your account.
      4. **Verification that Stitch's IP addresses have been correctly whitelisted.**
    subsections:
      - title: "Don't see the error here?"
        anchor: "missing-error"
        content: |
          If the error you received isn't listed here, contact support and then [let us know through a GitHub issue]({{ site.github_issue }}{:target="new"}.
---
{% include misc/data-files.html %}