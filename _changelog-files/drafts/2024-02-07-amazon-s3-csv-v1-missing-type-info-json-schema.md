---
title: "Amazon S3 CSV (v1) bug fix: Missing type information in JSON schema"
content-type: "changelog-entry"
date: 2024-02-07
entry-type: bug-fix
entry-category: integration
connection-id: amazon-s3-csv
connection-version: 1
pull-request: "https://github.com/singer-io/tap-s3-csv/pull/62"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix an issue during the data loading process.
