---
title: Stitch Destinations
permalink: /destinations/
tags: [getting_started]
keywords: destination, destinations, data warehouse, data warehouses, warehouse, stitch etl, etl
summary: "After your data is replicated, you'll need a place to store it. Stitch supports some of the most popular databases currently available for use as data warehouses. We call them destinations, but the purpose is the same: a central repository for all your data."

content-type: "destination-general"

layout: page
toc: false
feedback: false
type: "all"
destination: false


enterprise-cta:
  title: "Need multiple destinations?"
  url: "?utm_medium=docs&utm_campaign=multiple-destinations"
  copy: |
    As part of an Enterprise plan, you can configure Stitch to route different data sources to different destinations based on your needs. [Contact Stitch Sales for more info]({{ site.sales | append: page.enterprise-cta.url }}).
---
{% include misc/data-files.html %}

When Stitch replicates your data, we'll load it into the destination - or data warehouse - of your choosing. A data warehouse is a central repository of integrated data from disparate sources.

It's important to note that Stitch itself is **not** a data warehouse. Stitch is a data pipeline (or ETL tool) that enables you to replicate data from various sources and consolidate it into a single location. **A destination is required to use Stitch.**

---

## Comparing destinations

If you're new to data warehousing or want to see how Stitch's destination offerings compare to each other, look no further.

Our [Choosing a Destination]({{ link.destinations.overviews.choose-destination | prepend: site.baseurl }}) guide will help you choose the best Stitch destination for your data warehousing needs, from ensuring your data sources are compatible to staying within your budget.

In addition, our [Data Strategy Guide]({{ site.data-strategy }}) is a great place to start if you want some guidance on analytical vs. transactional databases.

---

## Current destinations

Stitch currently allows you to connect **one destination per account**. In addition, data will not begin replicating until you've successfully connected a destination and at least one integration.

{% include enterprise-cta.html %}

{% include destinations/destination-tiles.html %}

---

## Change destinations

Sometimes, you may want to replicate data to a different location than what you initially connected to Stitch. Whether you're simply switching to a new database or trying a different destination entirely, [you can easily change your destination in Stitch]({{ link.destinations.switch-destinations | prepend: site.baseurl }}).

---

## Suggest a destination

Don't see your destination of choice listed here? We'd love to hear from you! Please [reach out to us](mailto:{{ site.support }}) with your suggestion.