---
title: Microsoft SQL Server Extraction Errors
keywords: troubleshooting, integration, database integration, oracle, binlog error, extraction error, rds
tags: [database_integrations, troubleshooting_integrations, troubleshooting_errors]
layout: general

permalink: /troubleshooting/integrations/microsoft-sql-server-database-extraction-errors

summary: "When Stitch replicates data from a Microsoft SQL Server-backed database, it will check for the required user permissions and database server settings. If permissions or server settings aren't properly defined, an error may arise. In this article are the errors you might see and how to resolve them."
type: "database-integration, error"

intro: |
  When Stitch replicates data from an Microsoft SQL Server-backed database, it will check for the required user permissions and database server settings. If permissions or server settings aren't properly defined, you may receive an error during the Extraction phase of the replication process. These errors will surface in the integration's [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}).

sections:
  - title: "Microsoft SQL Server-backed databases"
    anchor: "microsoft-sql-server-backed-databases"
    content: |
      {% assign all-databases = site.database-integrations | where:"input",true %}
      {% assign mssql-databases = all-databases | where:"db-type","mssql" %}

      The errors and troubleshooting steps in this article are applicable to the following database integrations:

      {% for database in mssql-databases %}
      - [{{ database.title }}]({{ database.url | prepend: site.baseurl }})
      {% endfor %}

  - title: "Extraction errors and troubleshooting"
    anchor: "extraction-errors-and-troubleshooting"
    content: |
      {% assign errors = site.data.errors.database-extraction.mssql.all %}

      Below are the errors you might see if Stitch has trouble replicating data from an Microsoft SQL Server-backed database, as well as how to resolve them.

      {% include troubleshooting/error-messages.html %}
---
{% include misc/data-files.html %}