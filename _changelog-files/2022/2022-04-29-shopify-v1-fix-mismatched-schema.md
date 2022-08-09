---
title: "Shopify (v1) bug fix: Fixed mismatched schema transformation error"
content-type: "changelog-entry"
date: 2022-04-29
entry-type: bug-fix
entry-category: integration
connection-id: shopify
connection-version: 1
pull-request: "https://github.com/singer-io/tap-shopify/pull/149"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

For fields that are not originally found in the {{ this-connection.display_name }} schema catalog, it will be removed and added to the `patternProperties` object attribute to acknowledge that it was an extra field.