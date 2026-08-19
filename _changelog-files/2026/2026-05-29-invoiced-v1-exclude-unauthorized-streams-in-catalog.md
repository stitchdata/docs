---
title: "Invoiced (v1): Exclude unauthorized streams in catalog"
content-type: "changelog-entry"
date: 2026-05-29
entry-type: improvement
entry-category: integration
connection-id: invoiced
connection-version: 1
pull-request: "https://github.com/singer-io/tap-invoiced/pull/12"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to exclude unauthorized streams in catalog.