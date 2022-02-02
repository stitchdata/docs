---
title: "PostgreSQL (v1) integrations: Correctly type BIGINT[] data for Log-based Incremental Replication"
content-type: "changelog-entry"
date: 2019-10-22
entry-type: "bug-fix"
entry-category: "integration" 
connection-id: "postgres"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-postgres/pull/69"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

Previously, Log-based Incremental Replication was incorrectly typing data types of `INT8[]` as `STRING` during data type conversion. This has been corrected.