---
title: Database Integration Connection Errors
keywords: troubleshooting, integration, database integration, trouble, issue, help, error, errors, connection issue, connection
tags: [database_integrations, troubleshooting_integrations, troubleshooting_errors]
layout: general

permalink: /troubleshooting/integrations/database-connection-error-reference
redirect_from: 
  - /troubleshooting/database-integration-connection-errors
  - /troubleshooting/integrations/database-connection-errors

summary: "Resolve errors related to connecting to a database integration."
type: "database-integration, error"
category: "connection-errors"

level: "guide"
top-level: ""
popular: true

intro: |
  Stitch periodically performs checks on the connection to your database to ensure the connection remains active and healthy. Below are some of the most common errors you might see if Stitch has trouble performing the connection check to your database and how to resolve them.

  In this reference:

  {% for section in page.sections %}
  - [{{ section.title }}](#{{ section.anchor }})
  {% endfor %}

sections:
  - title: "Common connection errors"
    anchor: "common-error-reference"
    content: |
      {% assign errors = site.data.errors.connection.common.databases | sort_natural:"message" %}

      {% assign connection = "database" %}
      {% assign settings-page = "int-settings" %}

      The following errors are applicable to all database integrations:

      {% include troubleshooting/error-messages.html top-anchor="common-error-reference" display-name="Common" %}

  - title: "MongoDB connection errors"
    anchor: "mongodb-error-reference"
    content: |
      {% assign errors = site.data.errors.connection.databases.mongo | sort_natural:"message" %}

      {% include troubleshooting/error-messages.html top-anchor="mongodb-error-reference" display-name="MongoDB" %}
---
{% include misc/data-files.html %}