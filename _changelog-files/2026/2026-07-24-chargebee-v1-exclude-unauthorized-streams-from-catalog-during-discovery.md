---
title: "Chargebee (v1): Exclude unauthorized streams from catalog during discovery"
content-type: "changelog-entry"
date: 2026-07-24
entry-type: improvement
entry-category: integration
connection-id: chargebee
connection-version: 1
pull-request: "https://github.com/singer-io/tap-chargebee/pull/125"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to exclude unauthorized streams from catalog during discovery.