---
title: Redshift Data Loading Behavior
permalink: /data-structure/redshift-data-loading-behavior
layout: data-loading-headers
tags: 
keywords: redshift, amazon redshift, redshift data warehouse, redshift etl, etl to redshift
summary: "Learn how Stitch will load data from your integrations and handle various scenarios into a Redshift destination."

toc: false
type: "redshift"
category: "data loading"
---
{% include misc/data-files.html %}

{% assign destination = site.destinations | where:"type","redshift" | first %}