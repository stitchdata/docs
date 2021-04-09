---
title: "Salesforce (v1): Improved OPERATION_TOO_LARGE error messaging"
content-type: "changelog-entry"
date: 2021-03-16
entry-type: improvement
entry-category: integration
connection-id: "salesforce"
connection-version: 1
pull-request: "https://github.com/singer-io/tap-salesforce/pull/98"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated the {{ this-connection.display_name }} integration to log `OPERATION_TOO_LARGE` errors more clearly. The following error will now display in the **Extraction Logs** when this issue is encountered:

```shell
OPERATION_TOO_LARGE: exceeded 100000 distinct who/what's. Consider asking your Salesforce System Administrator to provide you with the `View All Data` profile permission. (Stream: [STREAM_NAME])
```