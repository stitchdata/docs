---
title: "Microsoft SQL Server (v1): Log4j update"
content-type: "changelog-entry"
date: 2022-12-19
entry-type: improvement
entry-category: integration
connection-id: mssql
connection-version: 1
pull-request: "https://github.com/singer-io/tap-mssql/pull/84"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated the Log4j version in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration due to the vulnerability in [CVE-2020-9493](https://github.com/advisories/GHSA-prp9-9gxw-38j8).