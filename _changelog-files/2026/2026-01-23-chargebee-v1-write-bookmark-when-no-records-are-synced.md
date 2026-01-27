---
title: "Chargebee (v1): Write bookmark when no records are synced"
content-type: "changelog-entry"
date: 2026-01-23
entry-type: imrpovement
entry-category: integration
connection-id: chargebee
connection-version: 1
pull-request: "https://github.com/singer-io/tap-chargebee/pull/120"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to write bookmark when no records are synced.