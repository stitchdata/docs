---
title: "New Xero (v1) feature: Retry logic"
content-type: "changelog-entry"
date: 2021-04-05
entry-type: new-feature
entry-category: integration
connection-id: xero
connection-version: 1
pull-request: "https://github.com/singer-io/tap-xero/pull/83"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

Retry logic was added to the filter function to be able to retry certain {{ this-connection.display_name }} (v{{ this-connection.this-version }}) error responses.