---
title: "Outbrain (v2): Exclude un-auth streams from catalog while discovery"
content-type: "changelog-entry"
date: 2026-08-25
entry-type: improvement
entry-category: integration
connection-id: outbrain
connection-version: 2
pull-request: "https://github.com/singer-io/tap-outbrain/pull/34"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to exclude un-auth streams from catalog while discovery.