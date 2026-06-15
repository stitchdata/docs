---
title: "Marketo (v2): do not stream rows into tempfile on im-memory volume"
content-type: "changelog-entry"
date: 2026-06-11
entry-type: improvement
entry-category: integration
connection-id: marketo
connection-version: 2
pull-request: "https://github.com/singer-io/tap-marketo/pull/111"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to do not stream rows into tempfile on im-memory volume.