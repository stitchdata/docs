---
title: "Zendesk Support (v2) bug fix: Backoff for errors"
content-type: "changelog-entry"
date: 2023-06-05
entry-type: bug-fix
entry-category: integration
connection-id: zendesk
connection-version: 2
pull-request: "https://github.com/singer-io/tap-zendesk/pull/131"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed an issue in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by adding a backoff in case `ProtocolError` or `ChunkedEncodingError` errors occur.