---
title: "Shopify (v3): Optimize Refund and Transactions sync by fetching only updated parent objects"
content-type: "changelog-entry"
date: 2025-04-24
entry-type: improvement
entry-category: integration
connection-id: shopify
connection-version: 3
pull-request: "https://github.com/singer-io/tap-shopify/pull/212"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to optimize Refund and Transactions sync by fetching only updated parent objects.