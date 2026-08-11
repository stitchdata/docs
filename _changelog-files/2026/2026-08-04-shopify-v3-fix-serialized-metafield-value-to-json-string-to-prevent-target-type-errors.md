---
title: "Shopify (v3): fix serialized metafield value to JSON string to prevent target type errors"
content-type: "changelog-entry"
date: 2026-08-04
entry-type: bug-fix
entry-category: integration
connection-id: shopify
connection-version: 3
pull-request: "https://github.com/singer-io/tap-shopify/pull/253"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix serialized metafield value to JSON string to prevent target type errors.