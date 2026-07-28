---
title: "Shopify (v3): Add exponential backoff retry logic for Shopify bulk operations in progress"
content-type: "changelog-entry"
date: 2025-12-15
entry-type: improvement
entry-category: integration
connection-id: shopify
connection-version: 3
pull-request: "https://github.com/singer-io/tap-shopify/pull/246"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add exponential backoff retry logic for Shopify bulk operations in progress.