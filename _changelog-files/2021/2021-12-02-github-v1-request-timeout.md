---
title: "GitHub (v1) update: Request timeout"
content-type: "changelog-entry"
date: 2021-12-02
entry-type: improvement
entry-category: integration
connection-id: github
connection-version: 1
pull-request: "https://github.com/singer-io/tap-github/pull/147"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add a request timeout option with a default value of 300 seconds.