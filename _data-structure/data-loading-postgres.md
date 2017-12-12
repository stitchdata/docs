---
title: PostgreSQL Data Loading Behavior
permalink: /data-structure/postgresql-data-loading-behavior
tags: [postgresql_destination]
layout: data-loading-headers
keywords: postgres, postgres data warehouse, postgres etl, etl to postgres, postgresql data warehouse, postgresql destination
summary: "Learn how Stitch will load data from your integrations and handle various scenarios into a PostgreSQL destination."

toc: false
type: "postgres"
category: "data loading"
---
{% include misc/data-files.html %}

{% assign destination = site.destinations | where:"type","postgres" | first %}