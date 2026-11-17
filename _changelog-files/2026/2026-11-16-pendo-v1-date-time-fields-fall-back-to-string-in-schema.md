---
title: "Pendo (v1): date-time fields fall back to string in schema"
content-type: "changelog-entry"
date: 2026-11-16
entry-type: improvement
entry-category: integration
connection-id: pendo
connection-version: 1
pull-request: "https://github.com/singer-io/tap-pendo/pull/146"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to date-time fields fall back to string in schema.