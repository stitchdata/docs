---
title: "Amazon S3 CSV (v1) update: Add credentials_cache_path property"
content-type: "changelog-entry"
date: 2025-02-05
entry-type: updated-feature
entry-category: integration
connection-id: amazon-s3-csv
connection-version: 1
pull-request: "https://github.com/singer-io/tap-s3-csv/pull/70"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add the `credentials_cache_path` property to define where the JSONFileCache is stored.