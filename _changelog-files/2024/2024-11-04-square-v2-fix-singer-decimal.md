---
title: "Square (v2) bug fix: Removed invalid `singer-decimal` formats"
content-type: "changelog-entry"
date: 2024-11-04
entry-type: bug-fix
entry-category: integration
connection-id: square
connection-version: 2
pull-request: "https://github.com/singer-io/tap-square/pull/120"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by removing the invalid `singer-decimal` formats from the `locations` schema.