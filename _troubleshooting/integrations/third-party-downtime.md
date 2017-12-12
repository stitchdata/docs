---
title: Third-Party Integration Downtime
keywords: integration troubleshooting
tags: [troubleshooting_integrations]
permalink: /troubleshooting/third-party-integration-downtime

summary: "From time to time, some of the applications and databases we integrate with may experience downtime. During these outages, Stitch may be unable to successfully connect to your data source and replicate your data."
type: "all-integrations, discrepancy, error"
---
{% include misc/data-files.html %}

{{ page.summary }}

If you receive an error or notice some missing data, downtime may be the root cause. We recommend checking out the status page for the integration in question to see if they've reported any issues.

In addition, many of the integrations listed below allow you to subscribe to their updates. That way, if a problem arises on the provider's end, you'll be the first to know.

{% assign integrations = site.documents | where:"input","true" %}

{% for integration in integrations %}
{% if integration.status-url != null %}
- [{{ integration.display_name }}]({{ integration.status-url }})
{% endif %}
{% endfor %}