---
title: "Google BigQuery (v1) destinations: Partitioned table support"
content-type: "changelog-entry"
date: 2018-12-10
entry-type: new-feature
entry-category: destination
connection-id: bigquery
connection-version: 1
---

{{ site.data.changelog.metadata.single-destination | flatify }}

Stitch now supports loading to {{ this-connection.display_name }} partitioned tables and ingestion-time partitioned tables with and without clustering. We’ve added instructions to our [docs for converting existing tables into partitioned and clustered tables]({{ site.data.urls.destinations.storage.bigquery-partitioning | prepend: site.baseurl | prepend: site.home }}).