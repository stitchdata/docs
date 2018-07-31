---
title: Stitch Webhook Integrations
keywords: webhook integration, etl webhook integration, webhook integration etl, app etl, cloud app etl
layout: general
summary: "Resources & guides for connecting your webhook apps and services to Stitch. Setup instructions, replication info, and schema details for each of Stitch's webhook integrations."
permalink: /integrations/webhooks/
sidebar: not-stitch

toc: false
input: false
feedback: false

sections:
  - content: |
      With Stitch, you can consolidate data from a variety of webhook apps into a [single destination]({{ site.baseurl }}/destinations).

  - title: "Historical webhook data"
    anchor: "historical-webhook-data"
    content: |
      Webhook data is sent in real-time, which means that only records created after you set up the integration in Stitch will be replicated to your data warehouse. 

      While most webhook integrations don't retain historical data due to this as-it-happens approach, some apps may allow you to replay data and send it to Stitch. This is dependent on if the app has this feature, however. 

      If you want to replay historical webhook data and send it to Stitch, contact that app's support for assistance.

  - title: "Append-Only Replication and querying"
    anchor: "append-only-replication"
    content: |
      The majority of Stitch's webhook integrations replicate data in an Append-Only fashion. {{ site.data.tooltips.append-only-rep }}

      While data stored using this method can provide insights and historical details about how rows change over time, grabbing the latest data does require a different querying strategy than usual. [Refer to the Querying Append-Only Tables guide for more details.]({{ link.replication.append-only-querying | prepend: site.baseurl }})

      See the Replication Methods guide for [an example and in-depth explanation of Append-Only replication]({{ link.replication.rep-methods | prepend: site.baseurl | append:"##-only-incremental-replication" }}).

  - title: "All webhook integrations"
    anchor: "all-webhook-integrations"
    content: |
      If you don't see what you're looking for in the list below, check out the Singer project. A simple, composable, open-source ETL standard, Singer allows you to extract data from any source. Check out the [Roadmap]({{ site.singer-roadmap }}){:target} or [GitHub repo]({{ site.singer-github }}){:target="new"} to see what's currently being worked on.


      Additionally, Stitch's Import API or Incoming Webhooks integrations can be used to extract data from sources that don't currently have a native integration.

      {% include integrations/templates/integration-category-tiles.html type="where-is-integration" which-integrations="all" %}
    subsections:
      - content: |
          {% include integrations/templates/integration-category-tiles.html type="webhooks" %}
---
{% include misc/data-files.html %}