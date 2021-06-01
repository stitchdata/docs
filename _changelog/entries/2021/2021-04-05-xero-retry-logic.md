---
title: "Xero (v1) improvement: Improved error handling with retry logic"
content-type: "changelog-entry"
date: 2021-04-05
entry-type: improvement
entry-category: integration
connection-id: xero
connection-version: 1
pull-request: "https://github.com/singer-io/tap-xero/pull/83"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added retry logic to {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integrations. This allows the integration to automatically retry API requests when it receives certain errors from the {{ this-connection.display_name }} API.