---
title: "Yotpo (v2): Add backoff for ConnectionResetError"
content-type: "changelog-entry"
date: 2025-02-26
entry-type: improvement
entry-category: integration
connection-id: yotpo
connection-version: 2
pull-request: "https://github.com/singer-io/tap-yotpo/pull/59"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add backoff for ConnectionResetError.