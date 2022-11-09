---
title: "Pendo (v1) update: Set default Include Anonymous Visitors value"
content-type: "changelog-entry"
date: 2022-09-08
entry-type: improvement
entry-category: integration
connection-id: pendo
connection-version: 1
pull-request: "https://github.com/singer-io/tap-pendo/pull/111"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by setting a default `false` value for the `Include Anonymous Visitors` parameter. 