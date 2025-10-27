---
title: "Amazon S3 CSV (v1): Update _sdc_extra column schema to be nullable"
content-type: "changelog-entry"
date: 2025-10-23
entry-type: improvement
entry-category: integration
connection-id: s3
connection-version: 1
pull-request: "https://github.com/singer-io/tap-s3-csv/pull/83"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to update _sdc_extra column schema to be nullable.