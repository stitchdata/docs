---
title: "Amazon S3 CSV (v1) bug fix: Corrected type checking for integers and numbers"
content-type: "changelog-entry"
date: 2021-06-16
entry-type: bug-fix
entry-category: integration
connection-id: "amazon-s3-csv"
connection-version: 1
pull-request: "https://github.com/singer-io/tap-s3-csv/pull/35"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Previously, data type checking for `integer` and `number` data types wasn't explicitly enforced, which resulted in some `integer` data being incorrectly typed. This has been corrected.