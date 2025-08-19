---
title: "Microsoft SQL Server (v1): Add a retry for deadlock error"
content-type: "changelog-entry"
date: 2025-04-28
entry-type: bug-fix
entry-category: integration
connection-id: mssql
connection-version: 1
pull-request: "https://github.com/singer-io/tap-mssql/pull/91"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our { this-connection.display_name } (v{ this-connection.this-version }) integration to add a retry for deadlock error.