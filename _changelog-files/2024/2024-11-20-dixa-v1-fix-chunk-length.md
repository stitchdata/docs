---
title: "Dixa (v1) bug fix: Chunk length"
content-type: "changelog-entry"
date: 2024-11-20
entry-type: bug-fix
entry-category: integration
connection-id: dixa
connection-version: 1 
pull-request: "https://github.com/singer-io/tap-dixa/pull/21"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix the `InvalidChunkLength` error.