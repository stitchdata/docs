---
title: "Impact (v1) bug fix: Handle empty model_id"
content-type: "changelog-entry"
date: 2023-05-12
entry-type: bug-fix
entry-category: integration
connection-id: impact
connection-version: 1
pull-request: "https://github.com/singer-io/tap-impact/pull/23"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've changed the way our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration handles the absence of value for the  `model_id` field to avoid errors.