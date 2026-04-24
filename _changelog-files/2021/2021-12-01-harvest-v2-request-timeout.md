---
title: "Harvest (v2) update: Request timeout"
content-type: "changelog-entry"
date: 2021-12-01
entry-type: improvement
entry-category: integration
connection-id: harvest
connection-version: 2
pull-request: "https://github.com/singer-io/tap-harvest/pull/51"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add a request timeout option with a default value of 300 seconds.