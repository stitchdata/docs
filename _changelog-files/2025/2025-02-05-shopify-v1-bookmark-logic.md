---
title: "Shopify (v1): Update bookmark logic for transactions and order_refunds"
content-type: "changelog-entry"
date: 2025-02-05
entry-type: improvement
entry-category: integration
connection-id: shopify
connection-version: 1
pull-request: "https://github.com/singer-io/tap-shopify/pull/197"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to update the bookmark logic for `transactions` and `order_refunds`.