---
title: "QuickBooks (v2): use batch queries to reduce api usage"
content-type: "changelog-entry"
date: 2025-11-06
entry-type: NOT FOUND
entry-category: integration
connection-id: quickbooks
connection-version: 2
pull-request: "https://github.com/singer-io/tap-quickbooks/pull/80"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to use batch queries to reduce api usage.