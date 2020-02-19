---
title: Destination Data Loading Errors
keywords: troubleshooting, destination, trouble, issue, help, error, errors
permalink: /troubleshooting/destinations/destination-data-loading-errors
tags: [troubleshooting_destinations, troubleshooting_errors]

summary: "If you received an error notification from Stitch about writing to your data warehouse, that means we ran into an issue loading your data. There can be a variety of reasons for this, each of which is specific to the type of destination you're using."
type: "all-destinations, error, replication"
toc: false
---
{% include misc/data-files.html %}

{{ page.summary }}

---

## Errors by Destination Type

**Data loading errors are specific to the destination, or data warehouse**. Select the destination you're using from the list below for troubleshooting steps for that destination.

{% for page in site.troubleshooting %}
{% if page.title contains "Data Loading" and page.title != "Destination Data Loading Errors" %}
- [{{ page.title }}]({{ page.url | prepend: site.baseurl }})
{% endif %}
{% endfor %}

---

## Find Your Destination Type

Not sure what destination you're using? You can find out by navigating to the {{ app.page-names.dw-settings }} page.

Click the {{ app.menu-paths.destination-settings }} at the top of the screen.

The settings form on this page will indicate which destination you have. For example: If you're using PostgreSQL as your destination, the heading at the top of the form will say "PostgreSQL."