---
title: "Codat (v1) update: Update key for company stream"
content-type: "changelog-entry"
date: 2022-08-11
entry-type: bug-fix
entry-category: integration
connection-id: codat
connection-version: 1
pull-request: "https://github.com/singer-io/tap-codat/pull/14"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by updating the key `companies` with `results` in the `company` stream after an update in the {{ this-connection.display_name }} API.