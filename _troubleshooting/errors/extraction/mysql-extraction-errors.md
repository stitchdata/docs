---
title: MySQL Extraction Errors
keywords: troubleshooting, integration, database integration, mysql, binlog error, extraction error, mariadb, aurora, google cloudsql, rds
tags: [database_integrations, troubleshooting_integrations, troubleshooting_errors]
permalink: /troubleshooting/integrations/mysql-database-extraction-errors
layout: general

summary: "When Stitch replicates data from a MySQL-based database, it will check for the required user permissions and database server settings. If permissions or server settings aren't properly defined, an error may arise. In this article are the errors you might see and how to resolve them."
type: "database-integration, error"

sections:
  - content: |
      When Stitch replicates data from a MySQL-based database, it will check for the required user permissions and database server settings. If permissions or server settings aren't properly defined, you may receive an error during the Extraction phase of the replication process. These errors will surface in the integration's [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}).

  - title: "Affected database integrations"
    anchor: "affected-database-integrations"
    content: |
      The errors and troubleshooting steps in this article are applicable to the following database integrations:

      {% assign all-mysql-databases = site.database-integrations | where:"db-type","mysql" %}

      {% for database in all-mysql-databases %}
      {% unless database.name == "magento" %}
      - [{{ database.display_name }}]({{ database.url | prepend: site.baseurl }})
      {% endunless %}
      {% endfor %}

  - title: "Extraction errors and troubleshooting"
    anchor: "errors-and-troubleshooting"
    content: |
      {% assign errors = site.data.errors.database-extraction.mysql.all | sort:"message" %}

      Below are the errors you might see if Stitch has trouble replicating data from a MySQL-based database, as well as how to resolve them.

      Errors are listed in alphabetical order.

      {% include troubleshooting/error-messages.html %}
---
{% include misc/data-files.html %}