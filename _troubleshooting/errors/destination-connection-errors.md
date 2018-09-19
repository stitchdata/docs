---
title: Destination Connection Errors
keywords: troubleshooting, destination, destination, trouble, issue, help, error, errors, connection issue, connection
tags: [troubleshooting_destinations, troubleshooting_integrations, troubleshooting_errors]

permalink: /troubleshooting/destinations/destination-connection-errors
redirect_from: /troubleshooting/destination-connection-errors

summary: "Stitch periodically performs checks on the connection to your destination to ensure the connection remains active and healthy. In this article are some of the most common errors you might see if Stitch has trouble performing the connection check to your destination and how to resolve them."
type: "all-destinations, error"
---
{% include misc/data-files.html %}

{% assign errors = site.data.errors.connection-checks.errors | where:"applies-to","both" %}

Stitch periodically performs checks on the connection to your destination to ensure the connection remains active and healthy. Below are some of the most common errors you might see if Stitch has trouble performing the connection check to your destination and how to resolve them.

{% include troubleshooting/error-messages.html %}