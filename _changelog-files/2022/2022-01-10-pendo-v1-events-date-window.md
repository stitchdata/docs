---
title: "Pendo (v1) update: Configurable date window"
content-type: "changelog-entry"
date: 2022-01-10
entry-type: improvement
entry-category: integration
connection-id: pendo
connection-version: 1
pull-request: "https://github.com/singer-io/tap-pendo/pull/89"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by adding a date window with a configurable size to the `Events` stream.