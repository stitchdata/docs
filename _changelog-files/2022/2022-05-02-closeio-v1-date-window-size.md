---
title: "Close.io (v1) update: Updated window size"
content-type: "changelog-entry"
date: 2022-05-02
entry-type: updated-feature
entry-category: integration
connection-id: closeio
connection-version: 1
pull-request: "https://github.com/singer-io/tap-closeio/pull/27"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added a date window to the `activities` table in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration. The default window size is 15 days.