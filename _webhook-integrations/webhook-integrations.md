---
title: Stitch Webhook Integrations
keywords: webhook integration, etl webhook integration, webhook integration etl, app etl, cloud app etl
layout: integration-category
summary: "Resources & guides for connecting your webhook apps and services to Stitch. Setup instructions, replication info, and schema details for each of Stitch's webhook integrations."
permalink: /integrations/webhooks/
sidebar: not-stitch

toc: false
input: false
integration-type: "webhook"
feedback: false
---
{% include misc/data-files.html %}


{% contentfor intro %}
With Stitch, you can consolidate data from a variety of webhook apps into a [single data warehouse]({{ site.baseurl }}/destinations).
{% endcontentfor %}

{% contentfor more-info %}
## Historical Webhook Data {#historical-webhook-data}

Webhook data is sent in real-time, which means that only records created after you set up the integration in Stitch will be replicated to your data warehouse. 

While most webhook integrations don't retain historical data due to this as-it-happens approach, some apps may allow you to replay data and send it to Stitch. This is dependent on if the app has this feature, however. 

If you want to replay historical webhook data and send it to Stitch, contact that app's support for assistance.

---

## Append-Only Replication & Querying {#append-only-replication}

The majority of Stitch's webhook integrations replicate data in an Append-Only fashion. {{ site.data.tooltips.append-only-rep }}

While data stored using this method can provide insights and historical details about how rows change over time, grabbing the latest data does require a different querying strategy than usual. [Refer to the Querying Append-Only Tables guide for more details.]({{ link.replication.append-only-querying | prepend: site.baseurl }})

See the Replication Methods guide for [an example and in-depth explanation of Append-Only replication]({{ link.replication.rep-methods | prepend: site.baseurl | append:"##-only-incremental-replication" }}).
{% endcontentfor %}