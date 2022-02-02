---
title: "Shopify (v1) update: Product status now available!"
content-type: "changelog-entry"
date: 2021-05-28
entry-type: updated-feature
entry-category: integration
connection-id: shopify
connection-version: 1
pull-request: "https://github.com/singer-io/tap-shopify/pull/108"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new `status` field has been added to the `products` table of our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration.

This field indicates the current status [of a given product](https://shopify.dev/api/admin/rest/reference/products/product#index-2021-04){:target="new"}, including as `active`, `archived`, and `draft`.