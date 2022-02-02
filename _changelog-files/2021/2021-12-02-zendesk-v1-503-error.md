---
title: "Zendesk (v1) update: Retry for 503 error"
content-type: "changelog-entry"
date: 2021-12-02
entry-type: improvement
entry-category: integration
connection-id: zendesk
connection-version: 1
pull-request: "https://github.com/singer-io/tap-zendesk/pull/95"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated how our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration handles `503` errors. Stitch will retry after a `503` error only if the `Retry-After` header is present in the response.