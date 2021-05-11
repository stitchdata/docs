---
title: "Shopify (v1) update: Field change in `definitions` table"
content-type: "changelog-entry"
date: 2021-04-15
entry-type: updated-feature
entry-category: integration
connection-id: shopify
connection-version: 1
pull-request: "https://github.com/singer-io/tap-shopify/pull/94"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

This fixes the `customer` field  in the  {{ this-connection.display_name }} integration's `definitions` table to accept null values.