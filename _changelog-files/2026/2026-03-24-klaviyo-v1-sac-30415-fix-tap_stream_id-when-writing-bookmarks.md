---
title: "Klaviyo (v1): Fix tap_stream_id when writing bookmarks"
content-type: "changelog-entry"
date: 2026-03-24
entry-type: bug-fix
entry-category: integration
connection-id: klaviyo
connection-version: 1
pull-request: "https://github.com/singer-io/tap-klaviyo/pull/83"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix `tap_stream_id` when writing bookmarks.