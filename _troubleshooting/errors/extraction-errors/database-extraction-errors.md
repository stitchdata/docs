---
title: Database Integration Extraction Error Reference
keywords: troubleshooting, integration, database integration, extraction error, common errors, 6 hour limit, table limit
tags: [database_integrations, troubleshooting_integrations, troubleshooting_errors]
layout: general

permalink: /troubleshooting/integrations/database-extraction-error-reference
redirect_from: 
  - /troubleshooting/integrations/common-extraction-errors
  - /troubleshooting/integrations/microsoft-sql-server-database-extraction-errors
  - /troubleshooting/integrations/mongodb-database-extraction-errors
  - /troubleshooting/integrations/mysql-database-extraction-errors
  - /troubleshooting/integrations/oracle-database-extraction-errors

summary: "Extraction errors for database integrations and how to resolve them."

level: "guide"
top-level: "replication"
# category: "extraction-errors"
type: "integration, error"
popular: true

intro: |
  When Stitch replicates data from a database integration, it will check for the required user permissions and database server settings. If permissions or server settings aren't properly defined, you may receive an error during the Extraction phase of the replication process.

  These errors will surface in the integration's [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}).

  In this reference:

  {% for section in page.sections %}
  - [{{ section.title }}](#{{ section.anchor }})
  {% endfor %}

sections:
  - title: "Common extraction errors"
    anchor: "common-error-reference"
    content: |
      {% assign errors = site.data.errors.extraction.common.databases | sort_natural:"message" %}

      The following errors are applicable to all database integrations that support Extraction Logs:

      {% include troubleshooting/error-messages.html display-name="Common" %}

  - title: "Microsoft SQL Server extraction errors"
    anchor: "microsoft-sql-server-error-reference"
    content: |
      {% assign errors = site.data.errors.extraction.databases.mssql.all | sort_natural:"message" %}

      {% include troubleshooting/error-messages.html top-anchor="microsoft-sql-server-error-reference" display-name="Microsoft SQL Server" %}

  - title: "MongoDB extraction errors"
    anchor: "mongodb-error-reference"
    content: |
      {% assign errors = site.data.errors.extraction.databases.mongo.all | sort_natural:"message" %}

      {% include troubleshooting/error-messages.html  top-anchor="mongodb-error-reference" display-name="MongoDB" %}

  - title: "MySQL extraction errors"
    anchor: "mysql-error-reference"
    content: |
      {% assign errors = site.data.errors.extraction.databases.mysql.all | sort_natural:"message" %}

      {% include troubleshooting/error-messages.html top-anchor="mysql-error-reference" display-name="MySQL" %}

  - title: "Oracle extraction errors"
    anchor: "oracle-error-reference"
    content: |
      {% assign errors = site.data.errors.extraction.databases.oracle.all | sort_natural:"message" %}

      {% include troubleshooting/error-messages.html top-anchor="oracle-error-reference" display-name="Oracle" %}
---
{% include misc/data-files.html %}