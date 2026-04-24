---
title: "JIRA (v2) update: Add request timeout"
content-type: "changelog-entry"
date: 2022-02-15
entry-type: improvement
entry-category: integration
connection-id: jira
connection-version: 2
pull-request: "https://github.com/singer-io/tap-jira/pull/71"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add a request timeout option with a default value of 300 seconds.