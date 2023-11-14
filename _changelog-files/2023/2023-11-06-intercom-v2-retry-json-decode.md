---
title: "Intercom (v2) bug fix: Add retry logic for JSON decode errors"
content-type: "changelog-entry"
date: 2023-11-06
entry-type: bug-fix
entry-category: integration
connection-id: intercom
connection-version: 2
pull-request: "https://github.com/singer-io/tap-intercom/pull/66"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed an issue in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by adding a a response doesn't return any JSON content.