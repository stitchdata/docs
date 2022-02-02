---
title: "PostgreSQL (v1) integrations: Correctly use SSL connections"
content-type: "changelog-entry"
date: 2020-02-27
entry-type: "bug-fix"
entry-category: "integration" 
connection-id: "postgres"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-postgres/pull/80"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed an issue with {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integrations where SSL connections weren't being used, even if the **SSL** option was checked in Stitch. If checked, Stitch will now correctly use and enforce SSL when connecting to the database.