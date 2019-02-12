---
title: Table Structural Changes
permalink: /data-structure/table-structural-changes
layout: general
keywords: redshift, amazon redshift, postgresql, varchar, varchar widening, column splitting, postgres, panoply, bigquery, structure change, schema change, column split

summary: "From time to time, Stitch will encounter data that can't be loaded losslessly into the destination table in your destination. When this happens, Stitch may have to alter the structure of the table in order to successfully load the data."
toc: true
weight: 3


sections:
  - content: |
      {{ page.summary }}

  - title: "Reasons for table structural changes"
    anchor: "structural-change-reasons"
    content: |
      Stitch may need to perform table alterations for several reasons, including:

      - [`VARCHAR` data of varying widths](#varchar-column-widening),
      - [Multiple data types in a source table column](#columns-mixed-data-types), and
      - [Column additions or removals in the source table](#adding-removing-columns)
      
      In this guide are examples of how Stitch will behave in each of these scenarios for each currently supported destination type.


# --------------------------- #
#        EXAMPLE TABLE        #
# --------------------------- #

  - title: "Examples in this guide"
    anchor: "examples-in-this-guide"
    content: |
      The examples in this guide will use an example table named `{{ site.data.dataloading.examples.example-table.name }}` to demonstrate Stitch's behavior for each scenario.

      Excluding [the `_sdc` columns]({{ link.destinations.storage.sdc-columns | prepend: site.baseurl }}), Stitch determines this is the structure of the `{{ site.data.dataloading.examples.example-table.name }}` table:

      {% include replication/templates/example-table-extracted-rows.html table-type="table-schema" %}


# --------------------------- #
#      VARCHAR WIDENING       #
# --------------------------- #

  - title: "VARCHAR column widening"
    anchor: "varchar-column-widening"
    content: |
      To preserve your destination's performance and reduce disk usage, Stitch uses the smallest possible `VARCHAR` column when storing string data.

      For example: If the maximum width of a string column across all records is currently 127, Stitch will type the destination column as `VARCHAR(128)`.

      As string data can vary in width, Stitch will take different actions to accommodate the data, depending on the destination in use. See below for an example.

    subsections:
      - title: "VARCHAR column widening example: First replication job"
        anchor: "varchar-column-widening--first-replication-job"
        content: |
          During the first replication job, Stitch extracts the following records for the [`{{ site.data.dataloading.examples.example-table.name }}` table](#examples-in-this-guide):

          {% include replication/templates/example-table-extracted-rows.html table-type="extraction" job-type="first-job" example-type="varchar-widening" %}

      - title: "VARCHAR column widening example: Second replication job"
        anchor: "varchar-column-widening-columns--second-replication-job"
        content: |
          During the next replication job, Stitch extracts the records in the table below. In this example, the `name` column contains data that exceeds its previously known width:

          {% include replication/templates/example-table-extracted-rows.html table-type="extraction" job-type="second-job" example-type="varchar-widening" %}

      - title: "VARCHAR column widening example: New table structure"
        anchor: "varchar-column-widening--new-table-structure"
        content: |
          How Stitch loads the data depends on the type destination being used. Click the tabs below to see how accommodating this data works for each destination.

          {% include replication/templates/table-schema-changes-tabs.html example-type="varchar-widening" %}


# --------------------------- #
#      MIXED DATA TYPES       #
# --------------------------- #

  - title: "Columns with mixed data types"
    anchor: "columns-mixed-data-types"
    content: |
      Stitch requires that there only be one data type per column to properly type, load, and store data. If a column contains multiple data types, Stitch will create additional columns and append the data type to the column name. See below for an example.

    subsections:
      - title: "Mixed data types example: First replication job"
        anchor: "mixed-data-types--first-replication-job"
        content: |
          During the first replication job, the following rows are extracted for the [`{{ site.data.dataloading.examples.example-table.name }}` table](#examples-in-this-guide):

          {% include replication/templates/example-table-extracted-rows.html table-type="extraction" job-type="first-job" example-type="mixed-data-types" %}

      - title: "Mixed data types example: Second replication job"
        anchor: "mixed-data-types--second-replication-job"
        content: |
          During the next replication job, the following rows are extracted:

          {% include replication/templates/example-table-extracted-rows.html table-type="extraction" job-type="second-job" example-type="mixed-data-types" %}

          Stitch will detect that the data types in these newly replicated rows differ than the ones from the initial replication job. In this case:

          - `age` was originally a `BIGINT`, but can sometimes be a decimal
          - `has_magic` was originally a `BOOLEAN`, but can sometimes be a string

      - title: "Mixed data types example: New table structure"
        anchor: "mixed-data-types--new-table-structure"
        content: |
          To accommodate the data, Stitch will create a new column for the newly detected data type and store the data for that data type in the new column.

          How columns are named as a result of "splitting" mixed data types depends on the type of destination being used. Click the tabs below to see how accommodating this data works for each destination.

          {% include replication/templates/table-schema-changes-tabs.html example-type="mixed-data-types" %}


# --------------------------- #
#   ADDING/REMOVING COLUMNS   #
# --------------------------- #

  - title: "Adding and removing columns"
    anchor: "adding-removing-columns"
    content: |
      {% capture log-based-incremental-notice %}
      **Note**: **This section is not applicable to Log-based Incremental Replication**. This section only applies when Key-based Incremental or Full Table Replication is being used. Refer to the [Log-based Incremental Replication guide]({{ link.replication.log-based-incremental | prepend: site.baseurl }}) for info about schema changes and Log-based Incremental Replication.
      {% endcapture %}
      {% include note.html type="single-line" content=log-based-incremental-notice %}

      - **Adding columns**: When a new column is added to a source table and selected for replication, Stitch will append the column to the end of the destination table. 

         For Key-based Incremental tables, data for the column will be replicated onward from the saved [Replication Key ]({{ link.replication.rep-keys | prepend: site.baseurl }}). Default `NULLs` will be placed in existing rows unless:

          1. A historical backfill in the source updated the records' Replication Key values, or
          2. A [table-level reset]({{ link.replication.reset-rep-keys | prepend: site.baseurl }}) is performed and a full re-replication is queued

      - **Removing columns**: When a column is removed in the source or de-selected from replication, Stitch will place default `NULLs` in the column going forward. Columns will not be removed from the destination.

  - title: "Additional resources"
    anchor: "additional-resources"
    subsections:
      - title: "Identify record rejections"
        anchor: "identify-record-rejections"
        content: |
          If Stitch is unable to load data into a table, it'll look like data is missing in your destination.

          When this occurs, check the [Rejected records table]({{ link.destinations.storage.rejected-records | prepend: site.baseurl }}) for the integration. This can help you pinpoint the root cause of the problem and unblock your data.

      - title: "Redshift/Panoply dependent views"
        anchor: "redshift-panoply-dependent-views"
        content: |
          When a table's structure has changed and Stitch needs to load data into the new structure, an `ALTER` command will be issued. To successfully run this command, dependent views must be temporarily 'dropped' to allow Stitch to re-create the table. If you receive an error that looks like the following, dependent views may be the root cause:

          ```sql
          ERROR: cannot drop table SCHEMA.TABLE column type because other objects depend on it

          Hint: Use DROP ... CASCADE to drop the dependent objects too.
          ``` 

          While an hour or two is usually sufficient to complete the process, some very large tables may require more time. **This [troubleshooting guide]({{ link.troubleshooting.view-dependency-errors | prepend: site.baseurl }}) will walk you through how to locate the dependent views and temporarily drop them.**
---