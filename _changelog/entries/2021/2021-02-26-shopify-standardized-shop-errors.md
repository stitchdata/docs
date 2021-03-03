---
title: "Shopify (v1) improvement: Standardized error messages"
content-type: "changelog-entry"
date: 2021-02-26
entry-type: bug-fix
entry-category: integration
connection-id: shopify
connection-version: 1
full-connection-version: "1.2.7"
pull-request: "https://github.com/singer-io/tap-shopify/pull/84"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Previously, error messages related to misconfigured {{ this-connection.display_name }} shops were unclear and non-standard in format. These errors have been standardized to provide a more consistent experience and message.