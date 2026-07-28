---
title: "Harvest (v3): Add explicit HarvestBackoffError handling to avoid throttling"
content-type: "changelog-entry"
date: 2026-06-12
entry-type: improvement
entry-category: integration
connection-id: harvest
connection-version: 3
pull-request: "https://github.com/singer-io/tap-harvest/pull/74"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add explicit HarvestBackoffError handling to avoid throttling.