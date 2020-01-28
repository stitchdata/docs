---
title: Unable to Load Tables due to Source Database Access Level
keywords: tables to replicate, unable to load tables, table issues
permalink: /troubleshooting/too-many-tables-to-load-database-integration
summary: "Mitigate issues with tables displaying in the Tables to Replicate tab by limiting the authorizing database user's access to source tables."
layout: general
toc: false

key: "source-database-access-level-issue"

type: "database-integration, replication"
promote: "false"

intro: |
  If you're encountering issues with Stitch displaying tables in the **Tables to Replicate** tab for a database integration, the root cause may the number of tables the authorizing database user has access to in the source database.

sections:
  - title: "Symptoms"
    anchor: "symptoms"
    content: |
      - A blank **Tables to Replicate** tab with an **Unable to load tables** error
      - An extraction error similar to the following:

        ```shell
        main - INFO Exit status is: Discovery succeeded. Tap failed with code -9. Target succeeded.
        ```

  - title: "Cause"
    anchor: "cause"
    content: |
      The first phase in the replication process is called **Extraction**. The start of every extraction is called **discovery**, and at this time, Stitch detects the tables and columns available in the source. These are the same tables and columns that the Stitch database user - or the database user in the integration's **{{ app.page-names.int-details }}** page - has access to.

      If the authorizing database user has access to a large number of databases and tables, discovery may take some time. To ensure discovery can complete in a timely manner, we recommend limiting the database user's access only to the tables you want to replicate.

      Refer to the [Basic concepts and system overview]({{ link.getting-started.basic-concepts | prepend: site.baseurl | append: "#system-architecture" }}) guide for more info about Stitch's replication process.

  - title: "Solution"
    anchor: "solution"
    databases:
      - name: "Microsoft SQL Server"
        type: "mssql"
      - name: "MySQL"
        type: "mysql"
      - name: "PostgreSQL"
        type: "postgres"
      - name: "Oracle"
        type: "oracle"
    database-table: |
      <table class="attribute-list">
      {% for database in section.databases %}
      <tr>
      <td width="20%; fixed" align="right">
      <strong>{{ database.name }}</strong>
      </td>
      <td>
      <code>{{ site.data.taps.extraction.database-setup.user-privileges[database.type][command] | replace:"<","&lt;" | flatify | strip }}</code>
      </td>
      </tr>
      {% endfor %}
      </table>
    content: |
      Limit the authorizing database user's access only to the tables you want to replicate:

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Step 1: Identify the database user"
        anchor: "solution--identify-database-user"
        content: |
          To see which database user Stitch is using to connect to the database:

          1. Click into the integration from the {{ app.page-names.dashboard }}.
          2. Click the **Settings** tab.
          3. Locate the **User** or **Username** field.

          The name of the database user in this field will be used to complete the remaining steps.

      - title: "Step 2: Revoke the database user's current access"
        anchor: "solution--revoke-current-access"
        content: |
          {% include note.html type="single-line" content="**Note**: If you don't have appropriate `REVOKE` privileges or you're unsure how to complete this step, reach out to a member of your technical or database administration team before continuing." %}

          Next, revoke the database user's current access. This will remove the overly permissive access the user currently has in preparation for the next step.

          1. Log into your database as a user with the ability to revoke privileges.
          2. Locate your database in the table below.
          3. Run the appropriate command, replacing `<schema_name>` and `<stitch_username>` with the name of the schema and [database user from Step 1](#solution--identify-database-user), respectively:

             {% assign command = "revoke-select" %}

          {{ section.database-table | flatify }}

          **Note**: These commands will work for any database integration backed by one of the databases mentioned above. For example: The command for MySQL will also work on Amazon RDS MySQL, Amazon RDS Aurora MySQL, MariaDB, etc.

      - title: "Step 3: Grant new table-level privileges"
        anchor: "solution--limit-table-access"
        content: |
          To limit this database user's table access:

          1. Log into your database as a user with the ability to grant privileges.
          2. Locate your database in the table below.
          3. Run the appropriate command on every table you want to replicate, replacing `<database_name>`, `<schema_name>`, `<table_name>`, and `<stitch_username>` with the name of the database, schema, table, and [database user from Step 1](#solution--identify-database-user), respectively:

             {% assign command = "grant-select-on-table" %}

          {{ section.database-table | flatify | markdownify }}

             **Note**: These commands will work for any database integration backed by one of the databases mentioned above. For example: The command for MySQL will also work on Amazon RDS MySQL, Amazon RDS Aurora MySQL, MariaDB, etc.
---
{% include misc/data-files.html %}