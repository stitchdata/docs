---
title: "Xero (v1): Fail connection for deprecated streams"
content-type: "changelog-entry"
date: 2026-03-30
entry-type: deprecation
entry-category: integration
connection-id: xero
connection-version: 1
pull-request: "https://github.com/singer-io/tap-xero/pull/128"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fail connection for deprecated streams.