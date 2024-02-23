---
title: "MongoDB (v3) bug fix: Session timeout"
content-type: "changelog-entry"
date: 2024-01-11
entry-type: bug-fix
entry-category: integration
connection-id: mongodb
connection-version: 3
pull-request: "https://github.com/singer-io/tap-mongodb/pull/110"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix an issue with the session timeout. The session is now refreshed every ten minutes during oplog queries.