---
title: Oracle Extraction Error Reference
keywords: troubleshooting, integration, database integration, oracle, binlog error, extraction error, rds
tags: [database_integrations, troubleshooting_integrations, troubleshooting_errors]
layout: general

permalink: /troubleshooting/integrations/oracle-database-extraction-errors

summary: "When Stitch replicates data from an Oracle-backed database, it will check for the required user permissions and database server settings. If permissions or server settings aren't properly defined, an error may arise. In this article are the errors you might see and how to resolve them."

type: "database-integration, error"

category: "extraction-errors"
integration-type: "database"
integration-display-name: "Oracle"
integration-db-type: "oracle"

intro: |
  When Stitch replicates data from an Oracle-backed database, it will check for the required user permissions and database server settings. If permissions or server settings aren't properly defined, you may receive an error during the Extraction phase of the replication process. These errors will surface in the integration's [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}).

sections:
  - title: "Applicable integrations"
    anchor: "oracle-backed-databases"
    content: |
     {% assign oracle-databases = site.database-integrations | where:"db-type","oracle" %}

     The errors and troubleshooting steps in this article are applicable to the following database integrations:

     {% for database in oracle-databases %}
     - [{{ database.title }}]({{ database.url | prepend: site.baseurl }})
     {% endfor %}

  - title: "Extraction errors and troubleshooting"
    anchor: "extraction-errors-and-troubleshooting"
    content: |
      {% assign errors = site.data.errors.extraction.databases.oracle.all %}

      Below are the errors you might see if Stitch has trouble replicating data from an Oracle-backed database, as well as how to resolve them.

      {% include troubleshooting/error-messages.html %}
---
{% include misc/data-files.html %}