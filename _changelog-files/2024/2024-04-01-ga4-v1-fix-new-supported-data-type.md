---
title: "Google Analytics (v1) bug fix: New supported data type"
content-type: "changelog-entry"
date: 2024-04-01
entry-type: bug-fix
entry-category: integration
connection-id: google-analytics-4
connection-version: 1
pull-request: "https://github.com/singer-io/tap-ga4/pull/102"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix an issue with the API. The `NUMBER` data type is now supported in the catalog for metric fields that are originally specified as `INTEGER` types in the {{ this-connection.display_name }} API.