---
title: "Yotpo (v1) bug fix: Corrected Replication Method for tables"
content-type: "changelog-entry"
date: 2021-06-16
entry-type: "bug-fix"
entry-category: "integration, documentation"
connection-id: "yotpo"
connection-version: 1
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've corrected the Replication Method for a few {{ this-connection.display_name }} tables in the docs. These tables were listed as using Key-based Incremental Replication, but in fact are Full Table:

- `products`
- `unsubscribers`