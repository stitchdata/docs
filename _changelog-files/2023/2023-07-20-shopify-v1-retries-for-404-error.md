---
title: "Shopify (v1) bug fix: Add retries for 404 error"
content-type: "changelog-entry"
date: 2023-07-20
entry-type: bug-fix
entry-category: integration
connection-id: shopify
connection-version: 1
pull-request: "https://github.com/singer-io/tap-shopify/pull/159"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed an issue in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by adding retries in case a `404` error occurs.