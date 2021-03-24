---
title: "PostgreSQL (v1) integrations: PG 10 now supported for Logical Replication"
content-type: "changelog-entry"
date: 2018-08-03
entry-type: "updated-feature"
entry-category: "integration" 
connection-id: "postgres"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-postgres/pull/15"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

Stitch now supports {{ this-connection.display_name }} 10 when using Log-based Incremental Replication. Previously, Stitch supported {{ this-connection.display_name }} 9.4.x - 9.9.x.