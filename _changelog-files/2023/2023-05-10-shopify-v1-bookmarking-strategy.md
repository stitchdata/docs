---
title: "Shopify (v1) bug fix: Bookmarking strategy fix"
content-type: "changelog-entry"
date: 2023-05-10
entry-type: bug-fix
entry-category: integration
connection-id: shopify
connection-version: 1
pull-request: "https://github.com/singer-io/tap-shopify/pull/166"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've changed the way our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration bookmarks streams to avoid issues when a sync is interrupted.