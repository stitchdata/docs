---
title: MySQL Extraction Errors
keywords: troubleshooting, integration, database integration, mysql, binlog error, extraction error, mariadb, aurora, google cloudsql, rds
tags: [database_integrations, troubleshooting_integrations, troubleshooting_errors]

permalink: /troubleshooting/integrations/mysql-database-extraction-errors

summary: "When Stitch replicates data from a MySQL-backed database, it will check for the required user permissions and database server settings. In this article are the extraction errors you might see if Stitch has trouble replicating data from a MySQL database and how to resolve them."
type: "database-integration, error"
---
{% include misc/data-files.html %}

{% assign errors = site.data.errors.database-extraction.mysql.errors %}

When Stitch replicates data from a MySQL-backed database, it will check for the required user permissions and database server settings.

Below are the errors you might see if Stitch has trouble replicating data from a MySQL-backed database, as well as how to resolve them.

{% include troubleshooting/error-messages.html %}