---
title: "Outreach (v1): Exclude unauth streams from catalog in discovery"
content-type: "changelog-entry"
date: 2026-07-09
entry-type: improvement
entry-category: integration
connection-id: outreach
connection-version: 1
pull-request: "https://github.com/singer-io/tap-outreach/pull/45"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to exclude unauth streams from catalog in discovery.