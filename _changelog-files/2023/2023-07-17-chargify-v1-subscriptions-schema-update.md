---
title: "Chargify (v1) bug fix: Update subscriptions schema"
content-type: "changelog-entry"
date: 2023-07-17
entry-type: bug-fix
entry-category: integration
connection-id: chargify
connection-version: 1
pull-request: "https://github.com/singer-io/tap-chargify/pull/49"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated the `subscriptions` schema in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix the data type for the `portal_invite_last_accepted_at` field. 