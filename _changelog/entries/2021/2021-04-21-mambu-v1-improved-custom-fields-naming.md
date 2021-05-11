---
title: "Mambu (v1) improvement: Improved custom fields' names"
content-type: "changelog-entry"
date: 2021-04-21
entry-type: improvement
entry-category: integration
connection-id: mambu
connection-version: 1
pull-request: "https://github.com/singer-io/tap-mambu/pull/43"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved the naming of custom fields by reducing their size. Removing unnecessary characters and field names improves the {{ this-connection.display_name }} integration's compatibility with Postgres.