---
title: "Iterable (v1): Excluded unauth streams from catalog in discovery"
content-type: "changelog-entry"
date: 2026-07-01
entry-type: improvement
entry-category: integration
connection-id: iterable-core
connection-version: 1
pull-request: "https://github.com/singer-io/tap-iterable/pull/34"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to excluded unauth streams from catalog in discovery.