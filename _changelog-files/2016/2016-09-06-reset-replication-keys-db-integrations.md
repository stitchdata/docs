---
title: "Reset Replication Keys for database integrations"
content-type: "changelog-entry"
date: 2016-09-06
entry-type: new-feature
entry-category: "replication, integration"
connections:
  - id: "mongodb"
    type: "integration"
    version: "11-01-2016"

  - id: "mssql"
    type: "integration"
    version: "06-01-2016"

  - id: "mysql"
    type: "integration"
    version: "15-10-2015"

  - id: "postgres"
    type: "integration"
    version: "15-10-2015"
---

Need to completely re-replicate all incrementally replicated tables in a database integration? Now you can(!) via the **Integration Settings** page on any MySQL, PostgreSQL, Microsoft SQL Server, or MongoDB integration. Take care though - the re-replicated rows count towards your monthly caps.