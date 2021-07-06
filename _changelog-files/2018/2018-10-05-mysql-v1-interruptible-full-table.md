---
title: "MySQL (v1) integrations: Interruptible Full Table replication"
content-type: "changelog-entry"
date: 2018-10-05
entry-type: updated-feature
entry-category: "integration"
connection-id: "mysql"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-mysql/pull/62"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Fullly replicating a table is now "interruptible," meaning that, if the table uses auto-incrementing Primary Keys, replication for the table can span multiple replication jobs.

Previously, a table using Full Table had to be fully replicated in a single job. If the job was interrupted for any reason, Stitch would replicate the table from the beginning during the next job.

Now, if a replication job is interrupted for a {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration, tables using Full Table Replication that have auto-incrementing Primary Keys will resume replication from the last replicated record instead of re-replicating the entire table.