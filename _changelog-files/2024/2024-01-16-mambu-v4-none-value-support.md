---
title: "Mambu (v4) update: None value support"
content-type: "changelog-entry"
date: 2024-01-16
entry-type: improvement
entry-category: integration
connection-id: mambu
connection-version: 4
pull-request: "https://github.com/singer-io/tap-mambu/pull/109"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by adding the `None` value support in `HashableDict`. A `None` value is now added at the end of a list before the list is hashed.