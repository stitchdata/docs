---
title: "Zendesk Support (v1) bug fix: Infinite Loop for users stream"
content-type: "changelog-entry"
date: 2023-05-25
entry-type: bug-fix
entry-category: integration
connection-id: zendesk
connection-version: 1
pull-request: "https://github.com/singer-io/tap-zendesk/pull/103"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed an issue in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration which was causing infinite loops in the `users` stream.