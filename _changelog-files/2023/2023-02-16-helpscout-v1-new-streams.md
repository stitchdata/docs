---
title: "Help Scout (v1): New streams"
content-type: "changelog-entry"
date: 2023-02-16
entry-type: new-feature
entry-category: integration
connection-id: helpscout
connection-version: 1
pull-request: "https://github.com/singer-io/tap-helpscout/pull/34"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Three new streams have been added to our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration:
- `teams`
- `team_users`
- `happiness_ratings`