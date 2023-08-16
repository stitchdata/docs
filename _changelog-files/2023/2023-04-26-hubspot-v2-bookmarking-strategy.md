---
title: "HubSpot (v2) bug fix: Bookmarking strategy fix"
content-type: "changelog-entry"
date: 2023-04-26
entry-type: bug-fix
entry-category: integration
connection-id: hubspot
connection-version: 2
pull-request: "https://github.com/singer-io/tap-hubspot/pull/226"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've changed the way our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration bookmarks streams to avoid issues with records updated during a sync.