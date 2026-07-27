---
title: "Amazon S3 CSV (v1): fix Parquet discovery OOM"
content-type: "changelog-entry"
date: 2026-07-20
entry-type: bug-fix
entry-category: integration
connection-id: s3
connection-version: 1
pull-request: "https://github.com/singer-io/tap-s3-csv/pull/92"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix Parquet discovery OOM.