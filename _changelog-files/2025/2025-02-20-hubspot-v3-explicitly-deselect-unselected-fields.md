---
title: "HubSpot (v3): Fixed unselected fields"
content-type: "changelog-entry"
date: 2025-02-20
entry-type: bug-fix
entry-category: integration
connection-id: hubspot
connection-version: 3
pull-request: "https://github.com/singer-io/tap-hubspot/pull/266"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix the extraction of unselected fields.