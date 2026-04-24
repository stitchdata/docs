---
title: "Close.io (v1) update: Ignore future-dated bookmark values"
content-type: "changelog-entry"
date: 2022-09-08
entry-type: improvement
entry-category: integration
connection-id: closeio
connection-version: 1
pull-request: "https://github.com/singer-io/tap-closeio/pull/30"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to avoid writing future-dated `activities` records.