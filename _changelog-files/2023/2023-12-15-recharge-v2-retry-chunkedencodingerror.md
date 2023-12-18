---
title: "Recharge (v2) update: Retry for ChunkedEncodingError"
content-type: "changelog-entry"
date: 2023-12-15
entry-type: improvement
entry-category: integration
connection-id: recharge
connection-version: 2
pull-request: "https://github.com/singer-io/tap-recharge/pull/42"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved how our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration handles errors. The integration will now retry when a `ChunkedEncodingError` is encountered.