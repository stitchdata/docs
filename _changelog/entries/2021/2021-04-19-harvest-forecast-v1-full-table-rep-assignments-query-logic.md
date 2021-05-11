---
title: "Harvest Forecast (v1) improvements: Full Table Replication & query logic"
content-type: "changelog-entry"
date: 2021-04-19
entry-type: improvement
entry-category: integration
connection-id: harvest-forecast
connection-version: 1
pull-request: "https://github.com/singer-io/tap-harvest-forecast/pull/17"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated the `assignments` table query logic to align with our API expectations.

We've also improved support for Full Table Replication correcting the Full Table refresh function.