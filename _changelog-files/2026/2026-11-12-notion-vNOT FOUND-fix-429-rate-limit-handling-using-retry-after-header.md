---
title: "NOT FOUND (vNOT FOUND): Fix 429 rate limit handling using Retry-After header"
content-type: "changelog-entry"
date: 2026-11-12
entry-type: bug-fix
entry-category: integration
connection-id: NOT FOUND
connection-version: NOT FOUND
pull-request: "https://github.com/singer-io/tap-notion/pull/20"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix 429 rate limit handling using Retry-After header.