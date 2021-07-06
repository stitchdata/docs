---
title: "Microsoft SQL Server (v1) bug fix: Quoting Replication Key columns in incremental queries"
content-type: "changelog-entry"
date: 2021-05-17
entry-type: bug-fix
entry-category: integration, replication
connection-id: "mssql"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-mssql/pull/59"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Previously, the names of Replication Key columns weren't being quoted when used in incremental queries. If a column name contained spaces, this would cause an error in the query and extraction to fail. This fix ensures Replication Key columns are properly quoted.