---
title: "New Xero (v1) feature: New handling of error conditions"
content-type: "changelog-entry"
date: 2021-04-09
entry-type: new-feature
entry-category: integration
connection-id: xero
connection-version: 1
pull-request: "https://github.com/singer-io/tap-xero/pull/85"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

We've added a features to more gracefully handle error conditions from the {{ this-connection.display_name }} (v{{ this-connection.this-version }}) API, including validation authorization and adding a more detailed error messages.