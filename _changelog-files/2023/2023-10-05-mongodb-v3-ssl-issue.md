---
title: "MongoDB (v3) bug fix: SSL issue"
content-type: "changelog-entry"
date: 2023-10-05
entry-type: bug-fix
entry-category: integration
connection-id: mongodb
connection-version: 3
pull-request: "https://github.com/singer-io/tap-mongodb/pull/107"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix an issue with connection parameters when using SSL.