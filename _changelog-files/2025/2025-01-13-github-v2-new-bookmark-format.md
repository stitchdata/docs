---
title: "GitHub (v2) update: New bookmark format"
content-type: "changelog-entry"
date: 2025-01-13
entry-type: improvement
entry-category: integration
connection-id: github
connection-version: 2
pull-request: "https://github.com/singer-io/tap-github/pull/212"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by
updating the `translate_state function` to convert old bookmarks into the new bookmark format
`{bookmarks {stream_name {repository ...}}}`.