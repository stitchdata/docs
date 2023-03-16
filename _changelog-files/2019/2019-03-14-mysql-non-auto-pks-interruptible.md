---
title: "MySQL (v1) integrations: Allow non-auto-incrementing Primary Keys for Full Table"
content-type: "changelog-entry"
date: 2019-03-18
entry-type: updated-feature
entry-category: "integration"
connection-id: "mysql"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-mysql/pull/89"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Interruptible Full Table Replication now supports non-auto-incrementing Primary Keys!

[Previously](#2018-10-05-mysql-v1-integrations-interruptible-full-table-replication), this integration would only resume Full Table Replication if a table's Primary Keys were auto-incrementing. 

We've updated this feature to allow tables with non-auto-incrementing Primary Keys to be resumable if interrupted. Tables must have Primary Keys with one of the following data types to be interruptible if Full Table Replication is used:

- `BIGINT`
- `DATE`
- `DATETIME`
- `CHAR`
- `INT`
- `MEDIUMINT`
- `SMALLINT`
- `TIME`
- `TIMESTAMP`
- `TINYINT`
- `VARCHAR`