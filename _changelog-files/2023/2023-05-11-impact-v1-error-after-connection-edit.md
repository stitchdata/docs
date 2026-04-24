---
title: "Impact (v1) bug fix: Error after editing connection"
content-type: "changelog-entry"
date: 2023-05-11
entry-type: bug-fix
entry-category: integration
connection-id: impact
connection-version: 1
pull-request: "https://github.com/singer-io/tap-impact/pull/22"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed an issue in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration that set the `model_id` field to `None` after the connection was edited.