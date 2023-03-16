---
title: "PostgreSQL (v1) integrations: Fix selected-by-default behavior"
content-type: "changelog-entry"
date: 2018-09-19
entry-type: "bug-fix"
entry-category: "integration"
connection-id: "postgres"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-postgres/pull/23"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed an issue with {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integrations where columns marked as `selected-by-default` will now be replicated unless explicitly deselected.