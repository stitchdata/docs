---
title: "Shopify (v1) bug fix: Fix for GraphQL"
content-type: "changelog-entry"
date: 2025-01-27
entry-type: bug-fix
entry-category: integration
connection-id: shopify
connection-version: 1
pull-request: "https://github.com/singer-io/tap-shopify/pull/195"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix the handling and logging errors for GraphQL.