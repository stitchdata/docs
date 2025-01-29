---
title: "Square (v2) bug fix: 'list' object has no 'startswith' attribute"
content-type: "changelog-entry"
date: 2025-01-23
entry-type: bug-fix
entry-category: integration
connection-id: square
connection-version: 2
pull-request: "https://github.com/singer-io/tap-square/pull/124"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix  the issue: the `list` object has no `startswith` attribute.