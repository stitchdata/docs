---
title: "Shopify (v1) update: Request timeout"
content-type: "changelog-entry"
date: 2022-01-13
entry-type: improvement
entry-category: integration
connection-id: shopify
connection-version: 1
pull-request: "https://github.com/singer-io/tap-shopify/pull/129"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add a request timeout option with a default value of 300 seconds.