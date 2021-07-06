---
title: "Shopify (v1) bug fix: Allow null values for `definitions.customer` field"
content-type: "changelog-entry"
date: 2021-04-15
entry-type: bug-fix
entry-category: integration
connection-id: shopify
connection-version: 1
pull-request: "https://github.com/singer-io/tap-shopify/pull/94"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Previously, the `customer` object in the `definitions` table would only accept populated values. If the integration encountered a `null` value, Extraction would fail. This has been fixed.