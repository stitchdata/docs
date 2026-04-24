---
title: "Xero (v1) improvement: Change endpoint to check access against"
content-type: "changelog-entry"
date: 2022-01-25
entry-type: improvement
entry-category: integration
connection-id: xero
connection-version: 1
pull-request: "https://github.com/singer-io/tap-xero/pull/98"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

To minimize the size of potential responses for our {{ this-connection.display_name }} (v{{ this-connection.this-version }} integration, we've updated the `check_platform_acces` function to use the **Currencies** endpoint.