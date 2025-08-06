---
title: "GitHub (v1) update: Support of objects in the parent field"
content-type: "changelog-entry"
date: 2021-11-30
entry-type: improvement
entry-category: integration
connection-id: github
connection-version: 1
pull-request: "https://github.com/singer-io/tap-github/pull/149"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add support of objects for the `parent` field in the `teams` stream.