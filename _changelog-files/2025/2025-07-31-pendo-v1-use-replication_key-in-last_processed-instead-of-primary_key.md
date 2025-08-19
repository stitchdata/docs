---
title: "Pendo (v1): Use replication_key in last_processed instead of primary_key"
content-type: "changelog-entry"
date: 2025-07-31
entry-type: improvement
entry-category: integration
connection-id: pendo
connection-version: 1
pull-request: "https://github.com/singer-io/tap-pendo/pull/133"
---
{ site.data.changelog.metadata.single-integration | flatify }

We've improved our { this-connection.display_name } (v{ this-connection.this-version }) integration to use replication_key in last_processed instead of primary_key.