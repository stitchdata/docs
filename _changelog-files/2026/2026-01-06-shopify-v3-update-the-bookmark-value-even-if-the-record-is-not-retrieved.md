---
title: "Shopify (v3): update the bookmark value even if the record is not retrieved"
content-type: "changelog-entry"
date: 2026-01-06
entry-type: improvement
entry-category: integration
connection-id: shopify
connection-version: 3
pull-request: "https://github.com/singer-io/tap-shopify/pull/247"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to update the bookmark value even if the record is not retrieved.