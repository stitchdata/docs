---
title: "Shopify (v1) bug-fix: Remove duplicates of `build` fields"
content-type: "changelog-entry"
date: 2021-05-06
entry-type: bug-fix
entry-category: integration
connection-id: "shopify"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-shopify/pull/103"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Due to the case sensitivy of fields during the {{ this-connection.display_name }} replication job, Stitch failed to recognize that `build` and `Build` were the same field and would produce duplicate records. This bug-fix scans for, and removes those duplicates. 
