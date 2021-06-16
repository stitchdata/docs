---
title: "Pipedrive (v1) bug fix: Corrected Replication Method for tables"
content-type: "changelog-entry"
date: 2021-06-16
entry-type: "bug-fix"
entry-category: "integration, documentation"
connection-id: "pipedrive"
connection-version: 1
pull-request: "https://github.com/singer-io/tap-pipedrive/pull/90"
---

We've corrected the Replication Method for a few {{ this-connection.display-name }} tables in the docs. These tables were listed as using Key-based Incremental Replication, but in fact are Full Table:

- `activity_types`
- `filters`
- `pipelines`
- `stages`
- `users`