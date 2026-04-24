---
title: "Amazon S3 CSV (v1) bug fix: Missing documents"
content-type: "changelog-entry"
date: 2024-11-20
entry-type: bug-fix
entry-category: integration
connection-id: amazon-s3-csv
connection-version: 1
pull-request: "https://github.com/singer-io/tap-s3-csv/pull/67"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix the following issue:

CSV documents are missing, indicating a potential race condition. These documents were created or modified simultaneously with the extraction process, leading to a situation where the bookmark date advances, causing the documents to be missed during identification.