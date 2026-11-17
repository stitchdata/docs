---
title: "Pendo (v1): Fall back to string for date-time fields in schema"
content-type: "changelog-entry"
date: 2026-11-16
entry-type: improvement
entry-category: integration
connection-id: pendo
connection-version: 1
pull-request: "https://github.com/singer-io/tap-pendo/pull/146"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fall back to string for date-time fields in the schema.