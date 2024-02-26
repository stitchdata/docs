---
title: "Mambu (v4) update: None value support in list"
content-type: "changelog-entry"
date: 2024-01-23
entry-type: improvement
entry-category: integration
connection-id: mambu
connection-version: 4
pull-request: "https://github.com/singer-io/tap-mambu/pull/110"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to support the `None` value in the `users.access.permissions` list. Null values are allowed in the list.