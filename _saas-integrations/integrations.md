---
title: Stitch Integrations
tags: [getting_started]
keywords: integrations, etl saas app, etl saas service, etl database, database etl, integration, data source
layout: general
permalink: /integrations/
summary: "Use Stitch's native database & SaaS, Import API, or webhook integrations to connect and replicate your data."

toc: false
input: false
feedback: false

sections:
  - content: |
      With Stitch, you can consolidate data from a variety of databases, SaaS apps, and services into [a single destination]({{ site.baseurl }}/destinations).
  - title: "Destination and integration compatibility"
    anchor: "destination-integration-compatibility"
    content: |
      Some integrations may be partially or fully incompatible with some of the destinations offered by Stitch. For example: some destinations don’t support storing multiple data types in the same column. If a SaaS integration sends over a column with mixed data types, [some destinations may reject the data]({{ link.destinations.storage.rejected-records | prepend: site.baseurl }}).

      To see if the integrations you're using are compatible with your destination, check out the [Destination and Integration Compatibility Guide]({{ link.destinations.overviews.compatibility | prepend: site.baseurl }}).
  - title: "All Stitch integrations"
    anchor: "all-stitch-integrations"
    content: |
      If you don't see what you're looking for in the list below, check out the Singer project. A simple, composable, open-source ETL standard, Singer allows you to extract data from any source. Check out the [Roadmap]({{ site.singer-roadmap }}){:target} or [GitHub repo]({{ site.singer-github }}){:target="new"} to see what's currently being worked on.

      Additionally, Stitch's Import API or Incoming Webhooks integrations can be used to extract data from sources that don't currently have a native integration.

      {% include integrations/templates/integration-category-tiles.html type="where-is-integration" which-integrations="all" %}
    subsections:
      - content: |
          {% include integrations/templates/integration-category-tiles.html type="all-integrations" %}
---
{% include misc/data-files.html %}