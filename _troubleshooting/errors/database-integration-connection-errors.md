---
title: Database Integration Connection Errors
keywords: troubleshooting, integration, database integration, trouble, issue, help, error, errors, connection issue, connection
tags: [database_integrations, troubleshooting_integrations, troubleshooting_errors]

permalink: /troubleshooting/integrations/database-connection-errors
redirect_from: /troubleshooting/database-integration-connection-errors
## Some users may experience a blip while the redirect works - it's normal. 

summary: "Stitch periodically performs checks on the connection to your database to ensure the connection remains active and healthy. In this article are some of the most common errors you might see if Stitch has trouble performing the connection check to your database and how to resolve them."
type: "database-integration, error"
---
{% include misc/data-files.html %}

{% assign connection-checks = site.data.errors.connection-checks.errors %}

Stitch periodically performs checks on the connection to your database to ensure the connection remains active and healthy. Below are some of the most common errors you might see if Stitch has trouble performing the connection check to your database and how to resolve them.

{% include troubleshooting/error-messages.html %}