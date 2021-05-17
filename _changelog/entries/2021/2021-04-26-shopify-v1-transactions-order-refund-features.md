---
title: "Shopify (v1): Improvements to order_refunds and transactions tables"
content-type: "changelog-entry"
date: 2021-04-26
entry-type: updated-feature
entry-category: integration
connection-id: shopify
connection-version: 1
pull-request: "https://github.com/singer-io/tap-shopify/pull/97"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've made some improvements to how the `transactions` and `order_refunds` tables replicate in {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integrations:

- Bookmarking has been added to the `order_refunds` and `transactions` tables
- Error handling added to the `transactions` table to avoid 429 errors