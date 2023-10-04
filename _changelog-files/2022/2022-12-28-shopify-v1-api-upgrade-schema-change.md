---
title: "Shopify (v1) update: API version upgrade and schema changes"
content-type: "changelog-entry"
date: 2022-12-28
entry-type: updated-feature
entry-category: integration
connection-id: shopify
connection-version: 1
pull-request: "https://github.com/singer-io/tap-shopify/pull/157"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've upgraded our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration's ShopifyAPI and SDK version to 12.0.1.

We've removed the `last_order_id`, `last_order_name`, `orders_count`, and `total_spent` fields from the `customer` object in the `orders` table.

A new `email_marketing_consent` object has been added to the `customers` and `orders` tables.