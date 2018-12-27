---
title: Selecting data to replicate
permalink: /replication/syncing-data
keywords: syncing, sync, replicate, replication, select data, sync data, sync table, sync column
tags: [replication]
layout: general

content-type: "select-data"
toc: true
weight: 1

summary: "After you connect an integration and Stitch performs a structure sync, the next thing you'll do is select tables and columns to replicate."

sections:
  - content: |
      {{ page.summary }} In this guide, we'll cover:

      - [Data selection support for each integration](#table-column-selection-support),
      - [How to set data to replicate](#set-data-to-replicate), and
      - [How to troubleshoot common data selection issues](#troubleshooting-common-issues)

  - title: "Table and column selection support"
    anchor: "table-column-selection-support"
    content: |
      {% include misc/icons.html %}

      Below is the level of support each integration has for table and column selection:

      - {{ supported | replace:"TOOLTIP","Supported" }} indicates that table/column selection is supported for the integration. **Note**: Only the data you select will be replicated. If nothing is selected, the integration will have a status of `Not Configured`.

      - {{ not-supported | replace:"TOOLTIP","Not supported" }} indicates that table and/or column selection isn't supported for the integration:

          - **For table selection**, all available tables and columns will be automatically set to replicate. For detailed info on the data Stitch replicates from [SaaS integrations]({{ site.baseurl }}/integrations/saas), check out the **Schema** section of any integration's guide.
          - **For column selection**, all available columns in the tables you select will be automatically set to replicate.

      {% include replication/integrations-with-whitelisting.html %}

  - title: "Set data to replicate"
    anchor: "set-data-to-replicate"
    content: |
      To set data to replicate, click into the integration from the {{ app.page-names.dashboard }} page and find the table or column you want to replicate. Then, {{ app.menu-paths.sync | replace: "Click","click" }} Keep in mind that:

      - **For database integration tables**, all columns will be set to replicate automatically.

         Additionally, you'll be prompted to select a [Replication Method]({{ link.replication.rep-methods | prepend: site.baseurl }}) for tables that you set to replicate.
      - **For SaaS integration tables that support column selection**, you can select columns by clicking on the **table name** and then tracking columns to replicate.

      **Note**: Parent objects - or objects that contain other objects - must be set to replicate for the objects they contain to replicate. For example: For a column to replicate, the table that contains it must also be selected. If applicable, so must the schema containing the table, and the database containing the schema.

    subsections:
      - title: "Select new and additional columns in already-selected tables"
        anchor: "select-database-views"
        content: |
          What happens when you've added a brand-new column in the data source or you want to replicate additional columns on an already-replicating table?

          For more info check out the [Syncing New and Additional Columns]({{ link.replication.syncing-new-columns | prepend: site.baseurl }}) guide.

      - title: "Select database views"
        anchor: "select-database-views"
        content: |
          While the steps for replicating a database view are almost the same as those for replicating a table, there are some slight differences.

          For more info check out the [Replicating Database Views]({{ link.replication.db-views | prepend: site.baseurl }}) guide.

  - title: "Troubleshooting common issues"
    anchor: "troubleshooting-common-issues"
    content: |
      In this section:

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}]({{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Missing objects"
        anchor: "missing-objects"
        content: |
          ```
          Stitch cannot detect any objects (databases, tables, etc.) at or below this level.
          ```

          If you receive this message or you can't find an object (database, table, column, etc.), [it's typically a permissions issue]({{ link.troubleshooting.missing-objects | prepend: site.baseurl }}).

      - title: "Not supported table/column messages"
        anchor: "not-supported-table-column-message"
        content: |
          If you see a status of `Not Supported` for a table or column in a database integration, there a few potential root causes:

          - **Insufficient permissions.** Verify that the Stitch user has all the required permissions as outlined in the **Setup** instructions for the database. Refer to the documentation for [your database]({{ site.baseurl }}/integrations/databases) for more info.

             After you grant the required permissions and a full replication cycle has completed, the table's **Sync Status** should change to `Supported` and be available for syncing.
          - **Unsupported column.** If a column is displayed as `Not Supported`, it may be that the column contains an [unsupported data type]({{ link.troubleshooting.unsupported-data-types | prepend: site.baseurl }}).

      - title: "Parent object not set to replicate"
        anchor: "parent-object-not-set-to-replicate"
        content: |
          ```
          The table containing these columns is not set to sync. Please sync the parent table to ensure replication of columns selected on this screen.
          ```

          If you receive this message, it means that the object above it isn't set to replicate. For example: The table that contains a selected column isn't set to replicate. [Parent objects must be selected for the objects they contain to also replicate](#set-data-to-replicate).
---
{% include misc/data-files.html %}