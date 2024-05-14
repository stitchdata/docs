---
title: "Chargebee (v1) update: New field in subscriptions schema"
content-type: "changelog-entry"
date: 2024-04-29
entry-type: updated-feature
entry-category: integration
connection-id: chargebee
connection-version: 1
pull-request: "https://github.com/singer-io/tap-chargebee/pull/109"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add the `discount` field to the `subscriptions` schema.