---
title: "Typeform (v2) update: Ratelimit removal"
content-type: "changelog-entry"
date: 2025-01-09
entry-type: improvement
entry-category: integration
connection-id: typeform
connection-version: 2
pull-request: "https://github.com/singer-io/tap-typeform/pull/83"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by removing the `ratelimit` dependency.