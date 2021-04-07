---
title: "PostgreSQL (v2) integrations: Key-based Incremental Replication now available!"
content-type: "changelog-entry"
date: 2021-03-30
entry-type: updated-feature
entry-category: integration
connection-id: postgres
connection-version: 2
pull-request: "https://github.com/stitchdata/docs/pull/624"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

{% assign all-postgres = site.database-integrations | where:"key","postgres-integration" %}
{% assign postgres-overview = all-postgres | where:"content-type","database-category" | first %}

The v{{ this-connection.this-version }} version of our {{ this-connection.display_name }} integration, which is currently in open beta, now supports Key-based Incremental Replication. All of Stitch's supported Replication Methods are now available for this version - go try it out!
