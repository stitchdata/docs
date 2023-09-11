---
title: "Outreach (v1) update: Request timeout"
content-type: "changelog-entry"
date: 2023-09-06
entry-type: improvement
entry-category: integration
connection-id: outreach
connection-version: 1
pull-request: "https://github.com/singer-io/tap-outreach/pull/30"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by adding a request timeout option with a default value of 300 seconds.