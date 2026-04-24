---
title: "PostgreSQL (v1) integrations: Include schema name in destination table names"
content-type: "changelog-entry"
date: 2018-08-28
entry-type: "new-feature"
entry-category: "integration" 
connection-id: "postgres"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-postgres/pull/19"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

We've added a new setting to {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integrations:

![The include schema names in destination table names setting in Stitch]({{ site.baseurl }}/images/changelog/include-postgres-schema-names-destination-tables.png)

When checked, Stitch will include schema names from the source database in the destination table name when the table is created. For example: `<source_schema_name>__<table_name>`

Stitch loads all selected replicated tables to a single schema, preserving only the table name. If two tables canonicalize to the same name - even if they’re in different source databases or schemas - name collision errors can arise. Checking this setting can prevent these issues.

**Note**: This setting can not be changed after the integration is saved. Additionally, this setting may create table names that exceed your destination’s limits.