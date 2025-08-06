---
title: "Impact (v1): Update for Actions and ActionUpdates"
content-type: "changelog-entry"
date: 2024-12-16
entry-type: improvement
entry-category: integration
connection-id: impact
connection-version: 1
pull-request: "https://github.com/singer-io/tap-impact/pull/33"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to forbid queries for `Actions` or `ActionUpdates` cannot have a `StartDate` exceeding 3 years in the past.