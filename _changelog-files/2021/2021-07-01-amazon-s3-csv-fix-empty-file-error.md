---
title: "Amazon S3 CSV (v1) bug fix: Empty file error handling"
content-type: "changelog-entry"
date: 2021-07-01
entry-type: bug-fix
entry-category: integration
connection-id: "amazon-s3-csv"
connection-version: 1
pull-request: "https://github.com/singer-io/tap-s3-csv/pull/38"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Previously, the {{ this-connection.display_name }} integration would not run when replicating a catalog where multiple CSV files were empty. This has been corrected. The integration will now run catalogs without schemas.