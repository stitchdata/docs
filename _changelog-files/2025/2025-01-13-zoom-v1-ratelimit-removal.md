---
title: "Zoom (v1) update: Ratelimit removal"
content-type: "changelog-entry"
date: 2025-01-13
entry-type: updated-feature
entry-category: integration
connection-id: zoom
connection-version: 1
pull-request: "https://github.com/singer-io/tap-zoom/pull/33"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by removing the `ratelimit` dependency.