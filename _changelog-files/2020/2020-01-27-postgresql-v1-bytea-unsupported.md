---
title: "PostgreSQL (v1) integrations: Correctly display BYTEA data as unsupported"
content-type: "changelog-entry"
date: 2020-01-27
entry-type: "bug-fix"
entry-category: "integration" 
connection-id: "postgres"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-postgres/pull/76"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

Previously, Stitch would display columns typed as `BYTEA` as available for selection, despite this data type currently being unsupported for {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integrations. With this fix, these columns will now correctly display as `UNSUPPORTED` in Stitch.