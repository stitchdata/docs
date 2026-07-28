---
title: "Amazon S3 CSV (v1): Handle empty initial sync"
content-type: "changelog-entry"
date: 2026-03-16
entry-type: improvement
entry-category: integration
connection-id: s3
connection-version: 1
pull-request: "https://github.com/singer-io/tap-s3-csv/pull/87"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to handle empty initial sync.