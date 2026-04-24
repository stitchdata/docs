---
title: "Amazon S3 CSV (v1): Refactor JSONL sampling/syncing to use singer-encodings"
content-type: "changelog-entry"
date: 2025-10-20
entry-type: improvement
entry-category: integration
connection-id: amazon-s3-csv
connection-version: 1
pull-request: "https://github.com/singer-io/tap-s3-csv/pull/82"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to refactor JSONL sampling/syncing to use singer-encodings.