---
title: "Shopify (v1) update: API version upgrade and schema changes"
content-type: "changelog-entry"
date: 2024-02-29
entry-type: updated-feature
entry-category: integration
connection-id: shopify
connection-version: 1
pull-request: "https://github.com/singer-io/tap-shopify/pull/187"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've upgraded our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration's Shopify SDK version to 12.4.0.

We've updated the {{ this-connection.display_name }} integration's API version from 2023-04 to 2024-01.

We've removed the `currency`, `accepts_marketing`, `accepts_marketing_updated_at`, and `marketing_opt_in_level` fields from the `abandoned_checkout` and `customers` tables.

New `poNumber` and `taxExempt` objects have been added to the `orders` table.