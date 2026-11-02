---
title: "HubSpot (v4): Handle POST 403 responses like GET so discovery skips forbidden streams"
content-type: "changelog-entry"
date: 2026-10-28
entry-type: improvement
entry-category: integration
connection-id: hubspot
connection-version: 4
pull-request: "https://github.com/singer-io/tap-hubspot/pull/311"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to handle POST 403 responses like GET so discovery skips forbidden streams.