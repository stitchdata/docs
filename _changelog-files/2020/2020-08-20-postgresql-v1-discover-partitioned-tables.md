---
title: "PostgreSQL (v1) integrations: Include partitioned tables in discovery"
content-type: "changelog-entry"
date: 2020-08-20
entry-type: "bug-fix"
entry-category: "integration" 
connection-id: "postgres"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-postgres/pull/101"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

Previously, partitioned tables weren't being detected during Discovery for {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integrations. This has been corrected.