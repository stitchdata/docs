---
title: "Dixa (v1) update: Extend the `activity_logs` schema"
content-type: "changelog-entry"
date: 2022-07-30
entry-type: improvement
entry-category: integration
connection-id: dixa
connection-version: 1
pull-request: "https://github.com/singer-io/tap-dixa/pull/14"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by adding some missing fields in the `activity_logs` stream.