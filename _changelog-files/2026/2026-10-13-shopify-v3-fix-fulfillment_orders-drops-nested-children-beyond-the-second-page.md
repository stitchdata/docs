---
title: "Shopify (v3): Fix: fulfillment_orders drops nested children beyond the second page"
content-type: "changelog-entry"
date: 2026-10-13
entry-type: bug-fix
entry-category: integration
connection-id: shopify
connection-version: 3
pull-request: "https://github.com/singer-io/tap-shopify/pull/259"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix: fulfillment_orders drops nested children beyond the second page.