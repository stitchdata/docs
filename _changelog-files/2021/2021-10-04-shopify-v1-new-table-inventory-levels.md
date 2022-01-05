---
title: "Shopify (v1) update: New Inventory Levels table!"
content-type: "changelog-entry"
date: 2021-10-04
entry-type: updated-feature
entry-category: integration
connection-id: shopify
connection-version: 1
pull-request: "https://github.com/singer-io/tap-shopify/pull/114"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added a new table to our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration!

The new `inventory_levels` table contains info about the account inventory levels accesible to the user who authorized the {{ this-connection.display_name }} integration in Stitch.
