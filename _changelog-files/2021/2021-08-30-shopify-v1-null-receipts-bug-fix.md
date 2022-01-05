---
title: "Shopify (v1) bug fix: Handling of null receipts"
content-type: "changelog-entry"
date: 2021-08-30
entry-type: bug-fix
entry-category: integration
connection-id: shopify
connection-version: 1
pull-request: "https://github.com/singer-io/tap-shopify/pull/119"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed behavior that was leading to crashes inside the canonicalize method in Stitch's {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration.

We've changed the integration to safely handle cases where a receipt could be `null`.