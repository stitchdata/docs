---
title: "Mixpanel (v1) bug fix: Add retries for ChunkedEncodingError"
content-type: "changelog-entry"
date: 2023-08-02
entry-type: bug-fix
entry-category: integration
connection-id: mixpanel
connection-version: 1
pull-request: "https://github.com/singer-io/tap-mixpanel/pull/61"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed an issue in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by adding retries in case a `ChunkedEncodingError` error occurs.