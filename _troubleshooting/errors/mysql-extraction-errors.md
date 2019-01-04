---
title: MySQL Extraction Errors
keywords: troubleshooting, integration, database integration, mysql, binlog error, extraction error, mariadb, aurora, google cloudsql, rds
tags: [database_integrations, troubleshooting_integrations, troubleshooting_errors]

permalink: /troubleshooting/integrations/mysql-database-extraction-errors

summary: "When Stitch replicates data from a MySQL-backed database, it will check for the required user permissions and database server settings. If permissions or server settings aren't properly defined, an error may arise. In this article are the errors you might see and how to resolve them."
type: "database-integration, error"
---
{% include misc/data-files.html %}

{% assign errors = site.data.errors.database-extraction.mysql.all %}

When Stitch replicates data from a MySQL-backed database, it will check for the required user permissions and database server settings. If permissions or server settings aren't properly defined, you may receive an error during the Extraction phase of the replication process. These errors will surface in the integration's [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}).

---

## MySQL-backed databases {#mysql-databases}

The errors and troubleshooting steps in this article are applicable to the following database integrations:

{% assign all-mysql-databases = site.database-integrations | where:"db-type","mysql" %}

{% for database in all-mysql-databases %}
{% unless database.name == "magento" %}
- [{{ database.display_name }}]({{ database.url | prepend: site.baseurl }})
{% endunless %}
{% endfor %}

---

## Extraction error messages and troubleshooting {#errors-and-troubleshooting}

Below are the errors you might see if Stitch has trouble replicating data from a MySQL-backed database, as well as how to resolve them.

{% include troubleshooting/error-messages.html %}