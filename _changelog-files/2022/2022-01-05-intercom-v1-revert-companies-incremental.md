---
title: "Intercom (v1) bug fix: Reverted companies stream to incremental"
content-type: "changelog-entry"
date: 2022-01-05
entry-type: bug-fix
entry-category: integration
connection-id: intercom
connection-version: 1
pull-request: "https://github.com/singer-io/tap-intercom/pull/44"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed a bug in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration, the `companies` stream was reverted to work as an incremental stream.