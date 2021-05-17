---
title: "Xero (v1) improvement: Improved handling of Xero API errors"
content-type: "changelog-entry"
date: 2021-04-09
entry-type: improvement
entry-category: integration
connection-id: xero
connection-version: 1
pull-request: "https://github.com/singer-io/tap-xero/pull/85"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added features to more gracefully handle error responses from the {{ this-connection.display_name }} (v{{ this-connection.this-version }}) API, including exponential backoffs on 429 errors, credential checking support, and more detailed error messages.