---
title: BigQuery Data Loading Behavior
permalink: /data-structure/bigquery-data-loading-behavior
tags: [bigquery_destination]
layout: data-loading-headers
keywords: bigquery, google bigquery data warehouse, bigquery data warehouse, bigquery etl, etl to bigquery
summary: "Learn how Stitch will load data from your integrations and handle various scenarios into a BigQuery destination."

toc: false
category: "data loading"
type: "bigquery"
---
{% include misc/data-files.html %}

{% assign destination = site.destinations | where:"type","bigquery" | first %}