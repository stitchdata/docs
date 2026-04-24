---
title: "Mixpanel (v1) update: Switch from multipleOf to singer.decimal"
content-type: "changelog-entry"
date: 2021-10-27
entry-type: improvement
entry-category: integration
connection-id: "mixpanel"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-mixpanel/pull/38"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to use the type `string` and format `singer.decimal` in funnels and revenue streams, instead of the type `number` and `'multipleOf': 1e-20`.

This change solves the issue where a schema mismatch error would be retuned when a value was out of range.