---
title: "Pendo (v1): Skip `Do Not Process` visitor records"
content-type: "changelog-entry"
date: 2023-01-09
entry-type: updated-feature
entry-category: integration
connection-id: pendo
connection-version: 1
pull-request: "https://github.com/singer-io/tap-pendo/pull/115"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

{{ this-connection.display_name }} stops collecting events from visitors with the `donotprocess` flag, so we've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to skp those records during replication.