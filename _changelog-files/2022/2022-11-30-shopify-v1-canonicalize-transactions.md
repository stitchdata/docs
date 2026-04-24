---
title: "Shopify (v1) update: Canonicalize transactions in OrderRefunds"
content-type: "changelog-entry"
date: 2022-11-30
entry-type: improvement
entry-category: integration
connection-id: shopify
connection-version: 1
pull-request: "https://github.com/singer-io/tap-shopify/pull/156"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to handle transactions containing keys with the same name but with a different case. For example: `token` and `Token`. An error will occur only if both keys are present and have different values.