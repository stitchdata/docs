---
title: "Mambu (v4) update: Update table to full table"
content-type: "changelog-entry"
date: 2024-02-20
entry-type: updated-feature
entry-category: integration
connection-id: mambu
connection-version: 4
pull-request: "https://github.com/singer-io/tap-mambu/pull/111"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration. Our `clients` table’s replication method has been changed from key-based incremental to full table.