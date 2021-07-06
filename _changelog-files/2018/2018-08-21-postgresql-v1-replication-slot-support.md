---
title: "PostgreSQL (v1) integrations: Expanded replication slot support"
content-type: "changelog-entry"
date: 2018-08-21
entry-type: "updated-feature"
entry-category: "integration" 
connection-id: "postgres"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-postgres/pull/18"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

Stitch now supports Log-based Incremental Replication across multiple databases in a single {{ this-connection.display_name }} cluster. Previously, Stitch supported one replication slot per integration and required it to be named `stitch`. Now, Stitch will look for the replication slot you define before falling back to `stitch`.