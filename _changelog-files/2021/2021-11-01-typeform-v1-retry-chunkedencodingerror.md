---
title: "Typeform (v1) update: Retry for ChunkedEncodingError"
content-type: "changelog-entry"
date: 2021-11-01
entry-type: improvement
entry-category: integration
connection-id: typeform
connection-version: 1
pull-request: "https://github.com/singer-io/tap-typeform/pull/52"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved how our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration handles errors. The integration will now retry when a `ChunkedEncodingError` is encountered.