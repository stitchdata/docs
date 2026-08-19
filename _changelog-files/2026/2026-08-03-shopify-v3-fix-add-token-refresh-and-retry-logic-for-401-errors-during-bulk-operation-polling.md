---
title: "Shopify (v3): Add token refresh and retry logic for 401 errors during bulk operation polling"
content-type: "changelog-entry"
date: 2026-08-03
entry-type: improvement
entry-category: integration
connection-id: shopify
connection-version: 3
pull-request: "https://github.com/singer-io/tap-shopify/pull/252"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add token refresh and retry logic for 401 errors during bulk operation polling.