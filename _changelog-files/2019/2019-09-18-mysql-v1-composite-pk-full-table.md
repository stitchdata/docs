---
title: "MySQL (v1) integrations: Fix composite Primary Key sorting for Full Table Replication"
content-type: "changelog-entry"
date: 2019-09-18
entry-type: updated-feature
entry-category: "integration"
connection-id: "mysql"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-mysql/pull/108"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Previously, the method used to bookmark Stitch's place while replicating tables with composite Primary Keys resulted in some records being skipped. We've updated the query the integration uses to properly account for composite keys, ensuring replication will resume in the correct place.