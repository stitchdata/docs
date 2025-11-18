---
title: "Shopify (v3): Clean up state file for failed Bulk operations"
content-type: "changelog-entry"
date: 2025-11-10
entry-type: improvement
entry-category: integration
connection-id: shopify
connection-version: 3
pull-request: "https://github.com/singer-io/tap-shopify/pull/244"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to clean up state file to fix failed Bulk operations.