---
title: "PostgreSQL (v2) update: Google CloudSQL PostgreSQL now available!"
content-type: "changelog-entry"
date: 2021-07-08
entry-type: new-feature
entry-category: integration
connection-id: "postgres"
connection-version: "2"
# pull-request: ""
---
{% assign this-connection = site.database-integrations | find:"key","cloudsql-postgres-integration" %}

A new version (v2) of our Google CloudSQL PostgreSQL integration is now available!

Along with all of the new features in v2 of the PostgreSQL integration (which this integration is based on), we've also added support for:

- SSL connections
- Log-based Incremental Replication

Learn more in our [Google CloudSQL PostgreSQL integration documentation]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}). 