---
title: "PostgreSQL (v2) update: Google CloudSQL PostgreSQL now available!"
content-type: "changelog-entry"
date: 2021-07-08
entry-type: new-feature
entry-category: integration
connection-id: "cloudsql-postgres"
connection-version: "2"
pull-request: ""
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new version (v{{ this-connection.this-version }}) of our {{ this-connection.display_name }} integration is now available!

Along with all of the new features in v2 of the PostgreSQL integration (which this integration is based on), we've also added support for:

- SSL connections
- Log-based Incremental Replication

Learn more about the integration in our [{{ this-connection.display_name }} integration documentation]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}). 