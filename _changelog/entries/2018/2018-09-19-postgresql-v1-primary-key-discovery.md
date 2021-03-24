---
title: "PostgreSQL (v1) integrations: Primary Key discovery"
content-type: "changelog-entry"
date: 2018-09-19
entry-type: "bug-fix"
entry-category: "integration"
connection-id: "postgres"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-postgres/pull/23"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

Previously, Primary Keys weren't detected during Discovery if other indices or unique constraints existed on the column. This has been corrected.