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

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix the following error during the data loading process:

```
ERROR Target exited abnormally with status 1. Terminating tap.
INFO No tunnel subprocess to tear down
INFO Exit status is: Discovery succeeded. Tap succeeded. Target failed with 
code 1 and error message: "Error persisting data to Stitch: 400: {'error': 'Invalid JSON schema: key null: expected type is one of JSONObject, found: String'}".
```
