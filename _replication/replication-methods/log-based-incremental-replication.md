---
title: Log-based Incremental Replication
permalink: /replication/replication-methods/log-based-incremental
keywords: replicate, replication, replication method, stitch replicates data
tags: [replication]
layout: general

content-type: "replication-methods"
toc: true
weight: 4

summary: "Available for select database integrations, Log-based Incremental Replication is a replication method in which Stitch identifies modifications to records - including inserts, updates, and deletes - using a database’s binary log files. This guide contains an overview of how Log-based Incremental Replication works, when it should be used, its limitations, and how to enable it for a supporting database integration."


# --------------------------- #
#  REPLICATION METHOD DETAILS #
# --------------------------- #

## For info about this Replication Method, see:
## _data/taps/extraction/replication-methods/log-based-replication.yml



example-table:
  - id: "1"
    name: "Finn"
    age: "15"
    type: "human"

  - id: "2"
    name: "Jake"
    age: "9"
    type: "dog"

  - id: "3"
    name: "Bubblegum"
    age: "19"
    type: "princess"


# --------------------------- #
#       CONTENT SECTIONS      #
# --------------------------- #

sections:
  - content: |
      {% include note.html type="single-line" content="**Note**: Log-based Replication is available only for MySQL and PostgreSQL-backed databases that support binary log replication." %}

      {{ site.data.tooltips.log-based-incremental-rep }} A binary log file is a record of events that occur within a database.

      In this guide, we'll cover:

      1. [How it works (with examples)](#how-log-based-incremental-replication-works),
      2. [When it should be used](#when-log-based-incremental-replication),
      3. [Limitations of this Replication Method](#limitations), and
      4. [How to enable it for your database integration](#enabling-log-based-replication)

  - title: "How {{ page.title }} works"
    anchor: "how-log-based-incremental-replication-works"
    content: |
      There are two types of binary log replication: Statement and row-based. Stitch uses a row-based approach, which means that when rows are modified via [a supported event type](#limitation-2--database-event-types), the entire row is written to the binary log file as a log message.

      During a replication job, Stitch iterates over each message in sequence, or in the same order that the messages were written to the binary log. Data is extracted for any messages that correspond to tables that have been tracked for replication. This means that all tables using {{ page.table }} are extracted from the source database simultaneously as one seamless process.

      To ensure only new and updated data is selected for replication, Stitch will use a binary log's Log Sequence Number (LSN) to 'bookmark' its place in a log file. This value is used to resume replicating data where a previous replication job ended.

    subsections:
      - title: "Historical replication jobs"
        anchor: "historical-replication-jobs"
        content: |
          During the historical replication job for a table using {{ page.title }}, two things will happen:

          1. Stitch will retrieve and store the maximum LSN from the binary logs.
          2. Stitch will use a `SELECT`-based approach to replicate the table in full. If this were a SQL query, it would look like this:

             ```sql
             SELECT column_you_selected_1,
                    column_you_selected_2,
                    [...]
               FROM schema.table
             ```

      - title: "Ongoing replication jobs"
        anchor: "ongoing-replication-jobs"
        content: |
          After the historical replication of a table is complete, Stitch will read updates for the table from the database's binary logs. During ongoing replication jobs using {{ page.title }}, a few things will happen:

          1. Using the maximum LSN from the previous job - in this case, the historical replication job - Stitch will begin reading log messages in the binary file. Data for tables set to replicate is extracted. 
          2. At the end of the replication job, Stitch bookmarks its place in the log file by storing its current LSN.
          3. During the **next** replication job, Stitch will resume reading data with a **greater** LSN than the LSN from the previous job.
          4. At the end of the replication job, Stitch bookmarks its place in the log file again.
          5. Repeat.

  - title: "When {{ page.title }} should be used"
    anchor: "when-log-based-incremental-replication"
    content: |
      {{ page.title }} may be a good fit if:

      1. The database is a MySQL or PostgreSQL-backed database [that supports {{ page.title }}](#limitation-1--availability). 
      2. Data is contained in a table, [not a view](#limitation-6--views-are-unsupported).
      3. Modifications to records are made only using [supported event types](#limitation-2--database-event-types).
      4. The structure of the table changes infrequently, if at all. Refer to the [Limitations section](#limitation-4--structural-changes) below for more info.

      If {{ page.title }} isn't appropriate, [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }}) may be a suitable alternative.

  - title: "Limitations of {{ page.title }}"
    anchor: "limitations"
    content: |
      Before you select {{ page.title }} as the Replication Method for a table, you should be aware of the limitations this method can have. Being aware of these limitations can help prevent data discrepancies, replication issues, and ensure your data is replicated in the most efficient manner possible.

      The limitations of {{ page.title }} are:

      {% for subsection in section.subsections %}
      - [{{ subsection.title | remove: "Limitation " | remove: ": " | remove:"1" | remove: "2" | remove: "3" | remove: "4" | remove: "5" | remove: "6" }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Limitation 1: Only available for certain MySQL and PostgreSQL databases"
        anchor: "limitation-1--availability"
        content: |
          {% include misc/support-icons.html %}
          {{ page.title }} is available only for certain MySQL and PostgreSQL-backed databases. While the original implementations of MySQL and PostgreSQL databases support {{ page.title }} some cloud versions may not.

          The table below lists the variations of MySQL and PostgreSQL databases that Stitch supports and whether those variations support {{ page.title }}.

          **Note**: The table below only indicates whether a **master** database instance supports {{ page.title }}. Refer to the documentation for the database for info about read replica support.

          {% assign binlog-databases = "mysql|postgres" | split:"|" %}
          {% assign all-databases = site.database-integrations | where:"input",true %}

          <table class="attribute-list">
          {% for binlog-database in binlog-databases %}
          {% assign databases = all-databases | where:"db-type",binlog-database | sort: "title" %}
          <tr>
          <td>
          <strong>{{ binlog-database | replace:"mysql","MySQL" | replace:"postgres","PostgreSQL" | append: "-backed databases" }}</strong>
          </td>
          <td>
          {% if forloop.first == true %}<strong>{{ page.title }} Support</strong>{% endif %}
          </td>
          </tr>
          {% for database in databases %}
          <tr>
          <td>
          <a href="{{ database.url | prepend: site.baseurl }}">{{ database.title }}</a>
          </td>
          <td>
          {% case database.binlog-replication %}
          {% when true %}
          Supported {{ supported | replace:"TOOLTIP","Log-based Incremental Replication is supported for this database." }}
          {% when false %}
          Unsupported {{ not-supported | | replace:"TOOLTIP","Log-based Incremental Replication is not supported for this database."}}
          {% endcase %}
          </td>
          </tr>
          {% endfor %}
          {% endfor %}
          </table>

      - title: "Limitation 2: Only works with specific database event types"
        anchor: "limitation-2--database-event-types"
        content: |
          {{ page.title }} reads data from a database's binary log and then replicates the changes. In order to replicate data, the event that caused a change to the data must be written to the binary log.

          For MySQL and PostgreSQL-backed databases, only the following event types are written to a database's binary log:

          - `DELETE`
          - `INSERT`
          - `UPDATE`

          This means that if data is modified using an event type not listed here, it won't be written to the database's binary log or subsequently detected by {{ page.title }}.

          For example: If a data in a table is modified using `ALTER`, the changes won't be written to the binary log or identified by Stitch.

      - title: "Limitation 3: Logs can age out and stop replication"
        anchor: "limitation-3--log-retention"
        content: |
          Binary log files, by default, are not stored indefinitely on a database server. The amount of time a log file is stored depends on the database's log retention settings.

          Log retention settings specify the amount of time before a binary log file is automatically removed from the database server.

          [TODO-Need more explanation here]

      - title: "Limitation 4: Structural changes require manual intervention"
        anchor: "limitation-4--structural-changes"
        content: |
          Any time the structure of a source table changes, you'll need to [reset the table from the {{ app.page-names.table-settings }} page]({{ link.replication.reset-rep-keys | prepend: site.baseurl }}). This will queue a full re-replication of the table and ensure that structural changes are correctly captured.

          Structure changes can include adding new fields, removing fields, changing a data type, etc. Resetting the table is required due to how messages in binary logs are structured and how Stitch's integrations validate table schemas when extracting data. When a structural change occurs without a table being reset, an extraction error similar to the following will surface in the [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}):

          ```
          2018-10-16 21:20:55,902Z target - CRITICAL Error persisting data for table
          "[table_name]": Record 0 did not conform to schema
          ```

          For this reason, Stitch recommends using {{ page.title }} with tables with structures that don't change frequently.

          ##### Schema violation errors, explained {#schema-violation-errors}

          Messages in binary logs are ordinal and don't contain field information. This means that field values in log messages are in the same order as the fields in the source table, but the messages don't contain data about which values belong to each field.

          Because of this and [how extraction is performed using {{ page.title }}](#how-log-based-incremental-replication-works), changes in structure will cause extraction errors.

          For example, consider this table:

          {% assign example-1-fields = "id|name|type" | split:"|" %}

          <table class="attribute-list">
          <tr>
          {% for field in example-1-fields %}
          <td>
          <strong>{{ field }}</strong>
          </td>
          {% endfor %}
          </tr>
          {% for example-record in page.example-table %}
          <tr>
          {% for field in example-1-fields %}
          <td>
          {{ example-record[field] }}
          </td>
          {% endfor %}
          </tr>
          {% endfor %}
          </table>

          The values for these fields might look like this in a binary log:

          ```
          1,Finn,human,2,Jake,dog,3,Bubblegum,princess
          ```

          Stitch's MySQL and PostgreSQL integrations use JSON schema validation to ensure that values in log messages are attributed to the correct fields when data is loaded into your destination. For this reason, schema changes in a source - whether it's changing a column's data type or re-ordering columns - will cause an extraction error to occur.

          As {{ page.title }} is a seamless process, an extraction error for any one table in a replication job will disrupt replication from any other tables using {{ page.title }}.

          If the column order or data types of a source table change in any capacity, the integration will not persist new or updated records that use this updated schema, as it does not have a means of attributing values to their proper fields based on the ordinal set when compared to the expected schema that was previously detected.

          Let's look at an example. Here's the same table from before, now with a new `age` column:

          {% assign example-2-fields = "id|name|age|type" | split:"|" %}

          <table class="attribute-list">
          <tr>
          {% for field in example-2-fields %}
          <td>
          <strong>{{ field }}</strong>
          </td>
          {% endfor %}
          </tr>
          {% for example-record in page.example-table %}
          <tr>
          {% for field in example-2-fields %}
          <td>
          {{ example-record[field] }}
          </td>
          {% endfor %}
          </tr>
          {% endfor %}
          </table>

          And the values in the binary log:

          ```
          1,Finn,15,human,2,Jake,9,dog,3,Bubblegum,19,princess
          ```

          Where Stitch previously detected three columns, the log messages now contain data for four columns. Because the log messages don't contain field information and are read in order, Stitch would be unable to determine what column the `15`, `9`, and `19` values are for.

      - title: "Limitation 5: Cannot be used with views"
        anchor: "limitation-5--views-are-unsupported"
        content: |
          {{ page.title }} can't be used with database views, as modifications to views are not written to binary log files.

          Stitch recommends using [Key-based Incremental Replication]({{ link.replication.key-based-rep | prepend: site.baseurl }}) instead, where possible.

  - title: "Enable {{ page.title }}"
    anchor: "enabling-log-based-replication"
    content: |
      Using {{ page.title }} requires a specific database configuration. Instructions for configuring the required settings varies from database to database.

      For setup instructions, refer to the documentation for your database:

      {% assign all-databases = site.database-integrations | where:"input",true %}
      {% assign only-binlog-databases = all-databases | where:"binlog-replication",true | sort: "title" %}

      {% for database in only-binlog-databases %}
      - [{{ database.title }}]({{ database.url | prepend: site.baseurl }})
      {% endfor %}
---
{% include misc/data-files.html %}
{% include misc/support-icons.html %}