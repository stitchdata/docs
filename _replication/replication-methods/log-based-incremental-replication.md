---
title: Log-based Incremental Replication
permalink: /replication/replication-methods/log-based-incremental
keywords: replicate, replication, replication method, stitch replicates data, change data capture, logical replication, log replication, binary replication, binary database repli8cation
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

feature-details:
  - database: "Microsoft SQL Server"
    db-type: "mssql"
    name: "Change Tracking"
    link: "https://docs.microsoft.com/en-us/sql/relational-databases/track-changes/about-change-tracking-sql-server?view=sql-server-2017"

  - database: "MongoDB"
    db-type: "mongo"
    name: "OpLog"
    link: "https://docs.mongodb.com/manual/core/replica-set-oplog/"

  - database: "MySQL"
    db-type: "mysql"
    name: "Binary log file position based replication, or binlog"
    link: "https://dev.mysql.com/doc/refman/5.7/en/binlog-replication-configuration-overview.html"

  - database: "Oracle"
    db-type: "oracle"
    name: "LogMiner"
    link: "https://docs.oracle.com/cd/B19306_01/server.102/b14215/logminer.htm"

  - database: "PostgreSQL"
    db-type: "postgres"
    name: "Logical replication"
    link: "https://www.postgresql.org/docs/10/logical-replication.html"

supported-database-list: |
  {%- for feature in page.feature-details -%}
  {% if forloop.last == true %}{{ feature.database | prepend: "and " | append: "-backed" }}
  {% else %}{{ feature.database | append: ", " }}{% endif %}
  {%- endfor -%}

sections:
  - content: |
      {% capture notice %}
      **Note**: Log-based Incremental Replication is available only for {{ page.supported-database-list | flatify | strip }} databases that support log-based replication.
      {% endcapture %}

      {% include note.html type="single-line" content=notice %}

      {{ site.data.tooltips.log-based-incremental-rep }} A log file is a record of events that occur within a database.

      In this guide, we'll cover:

      1. [Some useful terminology](#log-based-incremental-replication-terminology), 
      2. [How it works (with examples)](#how-log-based-incremental-replication-works),
      3. [When it should be used](#when-log-based-incremental-replication),
      4. [Limitations of this Replication Method](#limitations), and
      5. [How to enable it for your database integration](#enabling-log-based-replication)

  - title: "{{ page.title }} terminology"
    anchor: "log-based-incremental-replication-terminology"
    content: |
      - **Log file** - A file in a database containing a list of changes made to the database. Log files are made up of log messages.
      - **Log message** - A single change made to a database. For example: An `UPDATE` to a record.
      - **Log position ID** - A unique identifier corresponding to the position of a log message in a log file. These values are incremental, increasing as log messages are generated.

         - In **Microsoft SQL Server**, this is called the **Change Tracking Version**. As [Microsoft's documentation](https://docs.microsoft.com/en-us/sql/relational-databases/track-changes/work-with-change-tracking-sql-server?view=sql-server-2017#version-numbers){:target="new"} notes, this concept is similar to `rowversion`.
         - In **MongoDB**, this is a field in the database log named `ts`. The `ts` field is a combination of a timestamp and an ordinal (integer counter) value. For example: `"ts": Timestamp(1412180887, 1)` The timestamp is in seconds since the Unix epoch, and the ordinal is used to differentiate between entries that occured during the same second.
         - In **MySQL and PostgreSQL**, this is called a **Log Sequence Number (LSN)**.
         - In **Oracle**, this is called a **System Change Number (SCN)**.
      - **Replication job** - {{ site.data.tooltips.replication-job }}
      - **Historical replication job** - {{ site.data.tooltips.historical-replication-job }}

      In addition to these general terms, each database refers to its log replication feature by a different name. Stitch uses the following database features to perform Log-based Incremental Replication:

      {% for feature in page.feature-details %}
      - **{{ feature.database }}**: [{{ feature.name }}]({{ feature.link }}){:target="new"}
      {% endfor %}


  - title: "How {{ page.title }} works"
    anchor: "how-log-based-incremental-replication-works"
    content: |
      There are two types of log replication: Statement and row-based. Stitch uses a row-based approach, which means that when rows are modified via [a supported event type](#limitation-2--database-event-types), the entire row is written to the log file as a log message.

      During a replication job, Stitch iterates over each log message in sequence, or in the same order that the log messages were written to the log. Data is extracted for any log messages that correspond to tables that have been tracked for replication. This means that all tables using {{ page.title }} are extracted from the source database simultaneously as one seamless process.

      To ensure only new and updated data is selected for replication, Stitch will use a log's [log position ID](#log-based-incremental-replication-terminology) to 'bookmark' its place in a log file. This value is used to resume replicating data where a previous replication job ended.

    subsections:
      - title: "Historical replication jobs"
        anchor: "historical-replication-jobs"
        content: |
          During the [historical replication job](#log-based-incremental-replication-terminology) for a table using {{ page.title }}, two things will happen:

          1. Stitch will retrieve and store the maximum log position from the logs.
          2. Stitch will use a `SELECT`-based approach to replicate the table in full. If this were a SQL query, it would look like this:

             ```sql
             SELECT id,
                    column_you_selected_1,
                    column_you_selected_2,
                    [...]
               FROM schema.table
              WHERE id < [max primary key value]
              ORDER BY id
             ```
             
             **Note**: Stitch will automatically omit the `WHERE` clause in this statement if the table has no Primary Key or a Primary Key that is not sortable. 

      - title: "Ongoing replication jobs"
        anchor: "ongoing-replication-jobs"
        content: |
          After the historical replication of a table is complete, Stitch will read updates for the table from the database's logs. During ongoing replication jobs using {{ page.title }}, a few things will happen:

          1. Using the maximum log position ID from the previous job - in this case, the historical replication job - Stitch begins reading log messages in the binary file. Data for tables set to replicate is extracted. 
          2. At the end of the replication job, Stitch bookmarks its place in the log file by storing its current log position ID.
          3. During the **next** replication job, Stitch will resume reading data with a **greater** log position ID than the log position ID from the previous job.
          4. At the end of the replication job, Stitch bookmarks its place in the log file again.
          5. Repeat.

  - title: "When {{ page.title }} should be used"
    anchor: "when-log-based-incremental-replication"
    content: |
      {{ page.title }} may be a good fit if:

      1. The database is a {{ page.supported-database-list | flatify | strip }} database [that supports {{ page.title }}](#limitation--availability). 
      2. Data is contained in a table, [not a view](#limitation--views-are-unsupported).
      3. Modifications to records are made only using [supported event types](#limitation--database-event-types).
      4. The structure of the table changes infrequently, if at all. Refer to the [Limitations section](#limitation--structural-changes) below for more info.
      5. You're aware that, for PostgreSQL, only [master instances](#limitation--only-supports-master-instances-postgresql) support {{ page.title }} and that retaining [binary log files will increase the database's disk space usage](#limitation--disk-space-usage-postgresql).

      If {{ page.title }} isn't appropriate, [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }}) may be a suitable alternative.

  - title: "Limitations of {{ page.title }}"
    anchor: "limitations"
    content: |
      Before you select {{ page.title }} as the Replication Method for a table, you should be aware of the limitations this method can have. Being aware of these limitations can help prevent data discrepancies, replication issues, and ensure your data is replicated in the most efficient manner possible.

      The limitations of {{ page.title }} are:

      {% for subsection in section.subsections %}
      - [{{ subsection.title | remove: "Limitation " | flatify | remove: ": " | remove:"1" | remove: "2" | remove: "3" | remove: "4" | remove: "5" | remove: "6" | remove: "7" | remove: "8" }}](#{{ subsection.anchor }})
      {% endfor %}

## SUPPORTED DATABASES
    subsections:
      - title: "Limitation {{ forloop.index }}: Only available for certain databases"
        anchor: "limitation--availability"
        content: |
          {% include misc/icons.html %}
          {{ page.title }} is available only for certain {{ page.supported-database-list | flatify | strip }} databases. While the original implementations of these databases support {{ page.title }} some cloud versions may not.

          In the table below are the databases Stitch supports and whether {{ page.title }} can be used in Stitch for each one.

          - {{ supported | replace:"TOOLTIP","Supported" }} indicates that if the database/instance type meets the **Minimum version** requirement, {{ page.title }} can be used in Stitch.

          - {{ not-supported | replace:"TOOLTIP","Not supported" }} indicates that the database/instance type cannot be used in Stitch, even if the **Minimum version** requirement is met. This may be due to:

              - The provider not having support for binary logging (MySQL) or logical replication (PostgreSQL), which is what Stitch uses to perform {{ page.title }}.
              - The provider not allowing server settings to be configured in the manner Stitch requires. Refer to the documentation for the database for configuration requirements.
              - The provider not allowing binary logging on read replicas.

              **Note**: If public-facing information about the lack of support is available, a link to it will display next to the {{ not-supported | replace:"TOOLTIP","Not supported" }} icon.

          {% include replication/log-based-replication-database-support.html %}

## SUPPORTED EVENT TYPES
      - title: "Limitation {{ forloop.index }}: Only works with specific database event types"
        anchor: "limitation--database-event-types"
        content: |
          {{ page.title }} reads data from a database's log and then replicates the changes. In order to replicate data, the event that caused a change to the data must be written to the log.

          Stitch will read the following event types from logs:

          - `DELETE`
          - `INSERT`
          - `UPDATE`

          This means that if data is modified using an event type not listed here, it won't be written to the database's log or subsequently detected by {{ page.title }}.

          For example: If data in a table is modified using `ALTER`, the changes won't be written to the log or identified by Stitch.

## STRUCTURAL CHANGES
      - title: "Limitation {{ forloop.index }}: Structural changes require manual intervention (Microsoft SQL Server, MySQL, PostgreSQL, Oracle)"
        anchor: "limitation--structural-changes"
        content: |
          {% include note.html type="single-line" content="**Note**: This section is applicable only to **Microsoft SQL Server, MySQL, Oracle**, and **PostgreSQL**-backed database integrations." %}

          Any time the structure of a source table changes, you'll need to [reset the table from the {{ app.page-names.table-settings }} page]({{ link.replication.reset-rep-keys | prepend: site.baseurl }}). This will queue a full re-replication of the table and ensure that structural changes are correctly captured.

          Structural changes can include adding new columns, removing columns, changing a data type, etc. Resetting the table is required due to how messages in logs are structured and how Stitch's integrations validate table schemas when extracting data. When a structural change occurs without a table being reset, an extraction error similar to the following will surface in the [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}):

          ```
          {{ site.data.errors.database-extraction.mysql.raw-error.schema-violation | lstrip | rstrip }}
          ```

          For this reason, Stitch recommends using {{ page.title }} with tables that have structures that don't change frequently.

        sub-subsections:
          - title: "Schema violation errors, explained"
            anchor: "schema-violation-errors"
            content: |
              Messages in database logs are ordinal and don't contain field information. This means that column values in log messages are in the same order as the columns in the source table, but the messages don't contain data about which values belong to each column.

              Because of this and [how extraction is performed using {{ page.title }}](#how-log-based-incremental-replication-works), changes in a table's structure will cause extraction errors.

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

              Stitch's Microsoft SQL Server, MySQL, Oracle, and PostgreSQL integrations use JSON schema validation to ensure that values in log messages are attributed to the correct fields when data is loaded into your destination. For this reason, schema changes in a source - whether it's changing a column's data type or re-ordering columns - will cause an extraction error to occur.

              If the column order or data types of a source table change in any capacity, the integration will not persist new or updated records that use this updated schema, as it does not have a means of attributing values to their proper columns based on the ordinal set when compared to the expected schema that was previously detected.

              As {{ page.title }} is a seamless process, an extraction error for any one table in a replication job will disrupt replication from any other tables using {{ page.title }}.

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

              And the values in the log:

              ```
              1,Finn,15,human,2,Jake,9,dog,3,Bubblegum,19,princess
              ```

              Where Stitch previously detected three columns, the log messages now contain data for four columns. Because the log messages don't contain field information and are read in order, Stitch would be unable to determine what column the `15`, `9`, and `19` values are for.

## VIEWS
      - title: "Limitation {{ forloop.index }}: Cannot be used with views"
        anchor: "limitation--views-are-unsupported"
        content: |
          {{ page.title }} can't be used with database views, as modifications to views are not written to log files.

          Stitch recommends using [Key-based Incremental Replication]({{ link.replication.key-based-rep | prepend: site.baseurl }}) instead, where possible.

## MYSQL/ORACLE RETENTION PERIOD
      - title: "Limitation {{ forloop.index }}: Logs can age out and stop replication (Microsoft SQL Server, MySQL, and Oracle)"
        anchor: "limitation--log-retention"
        content: |
          {% include note.html type="single-line" content="**Note**: This section is applicable only to **Microsoft SQL Server, MySQL,** and **Oracle**-backed database integrations." %}

          Log files, by default, are not stored indefinitely on a database server. The amount of time a log file is stored depends on the database's log retention settings.

          Log retention settings specify the amount of time before a log file is automatically removed from the database server. When a log file is removed from the server before Stitch can read from it, replication will be unable to proceed. 

          When this occurs, an extraction error similar to the following will surface in the [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}):

          - **For MySQL databases**:
            ```
            {{ site.data.errors.database-extraction.mysql.raw-error.log-retention-purge | strip }}
            ```

          - **For Oracle databases**:
            ```
            {{ site.data.errors.database-extraction.oracle.raw-error.missing-logfile | strip }}
            ```

          To resolve the error, you'll need to [reset the integration from the {{ app.page-names.int-settings }} page]({{ link.replication.reset-rep-keys | prepend: site.baseurl }}). **Note**: This is different than resetting an individual table.

          This error can be caused by a few things:

          1. **The log file is purged before historical replication completes**. This is because the maximum [log position ID](#log-based-incremental-replication-terminology) is saved at the start of [historical replication jobs](#log-based-incremental-replication-terminology), so Stitch knows where to begin reading from the database logs after historical data is replicated.
          2. **The log retention settings are set to too short of a time period**. Stitch recommends a minimum of **3 days**, but **7 days** is preferred to account for resolving potential issues without losing logs.

             - **For Microsoft SQL Server databases**, this is the `CHANGE_RETENTION` setting.
             - **For MysQL databases**, these are the `expire_logs_days` or `binlog_expire_logs_seconds` settings.
             - **For Oracle databases**:
                - **For self-hosted Oracle databases**, this is the [RMAN retention policy setting]({{ site.baseurl }}/integrations/databases/oracle#configure-rman-backups).
                - **For Oracle-RDS databases**, these are the [AWS automated backup]({{ site.baseurl }}/integrations/databases/amazon-oracle-rds#enable-aws-automated-backups) and [`archivelog retention hours`]({{ site.baseurl }}/integrations/databases/amazon-oracle-rds#define-archivelog-retention-hours) settings.
          3. **Any critical error that prevents Stitch from replicating data**, such as a connection issue that prevents Stitch from connecting to the database or a [schema violation](#limitation-3--structural-changes). If the error persists past the log retention period, the log will be purged before Stitch can read it.

## POSTGRES INCREASE DISK SPACE
      - title: "Limitation {{ forloop.index }}: Will increase source disk space usage (PostgreSQL)"
        anchor: "limitation--disk-space-usage-postgresql"
        content: |
          {% include note.html type="single-line" content="This section is applicable only to **PostgreSQL**-backed database integrations." %}

          PostgreSQL {{ page.title }} uses PostgreSQL's logical replication feature. Logical replication uses a replication slot, which represents a stream of changes made to a given database.

          According to [PostgreSQL's documentation](https://www.postgresql.org/docs/11/logicaldecoding-explanation.html#LOGICALDECODING-REPLICATION-SLOTS){:target="new"}, replication slots will prevent removal of required resources even if no connection is using them:

          > Replication slots persist across crashes and know nothing about the state of their consumer(s). They will prevent removal of required resources even when there is no connection using them. This consumes storage because neither required WAL nor required rows from the system catalogs can be removed by VACUUM as long as they are required by a replication slot.

          This means that log files (Write Ahead Log (WAL), for PostgreSQL) aren't removed from the replication slot until they're consumed. In this case, until Stitch reads them during a replication job.

          While Stitch will issue a `flush_lsn` command after messages have been read, an increase in disk space usage is to be expected when using {{ page.title }} due to how PostgreSQL replication slots function. The amount of disk space usage depends on the number of updates made to the database, how quickly Stitch proceeds with replication, and whether any errors that prevent replication arise.

          The greatest increase in disk space usage typically occurs during the switch from historical replication (`SELECT`-based replication) to consuming the database's logs. Disk space usage may spike, but it typically levels off over time.

          **Note**: If you decide to permanently disable Log-based Incremental Replication for your PostgreSQL database, remove the replication slot to prevent further unnecessary disk space consumption.

## POSTGRES MASTER INSTANCE
      - title: "Limitation {{ forloop.index }}: Can only be used with a master instance (PostgreSQL)"
        anchor: "limitation--only-supports-master-instances-postgresql"
        content: |
          {% include note.html type="single-line" content="This section is applicable only to **PostgreSQL**-based database integrations." %}
          
          For PostgreSQL-backed databases, Log-based replication will only work on master instances due to a feature gap in PostgreSQL 10. [Based on their forums](https://commitfest.postgresql.org/12/788/){:target="new"}, PostgreSQL is working on adding support for using logical replication on a read replica to a future version.

          If you're concerned about the increase in [disk space usage](limitation-6--disk-space-usage-postgresql) and the impact this may have, consider connecting a read replica and using [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }}) instead.

          Otherwise, we recommend monitoring the instance's disk space usage during the first few replication jobs to minimize any negative impact on your database's performance.

## MULTIPLE CONNECTIONS TO REPLICATION SLOT
      - title: "Limitation {{ forloop.index }}: Multiple connections to a replication slot can cause data loss in Stitch (PostgreSQL)"
        anchor: "limitation--replication-slot-data-loss-postgresql"
        content: |
          {% include note.html type="single-line" content="This section is applicable only to **PostgreSQL**-based database integrations." %}

          As previously mentioned, {{ page.title }} for PostgreSQL requires a replication slot which Stitch can read log files from. When changes are made to a database, they are written to the log file in the replication slot.

          Each change to the database is written to the database's replication slot exactly once.
          
          As log files are removed from the replication slot once they're consumed, this means that once the change is read, the record of it is purged.

          If multiple connections - whether it's multiple integrations in Stitch, or connections elsewhere - are using the same replication slot, data loss can occur as each connection will only receive some of the updates made to the database.

          According to [PostgreSQL's documentation](https://www.postgresql.org/docs/11/logicaldecoding-explanation.html#LOGICALDECODING-REPLICATION-SLOTS){:target="new"}:

          > A logical slot will emit each change just once in normal operation... Multiple independent slots may exist for a single database. Each slot has its own state, allowing different consumers to receive changes from different points in the database change stream. For most applications, a separate slot will be required for each consumer.
          > A logical replication slot knows nothing about the state of the receiver(s). **It's even possible to have multiple different receivers using the same slot at different times; they'll just get the changes following on from when the last receiver stopped consuming them. Only one receiver may consume changes from a slot at any given time.**

          This means that if one connection reads the changes from the replication slot, Stitch will only be able to extract the changes from when the other connection stopped consuming them.

          To avoid data loss caused by this scenario, Stitch recommends creating a dedicated replication slot for PostgreSQL database you want to connect.

  - title: "Enable {{ page.title }}"
    anchor: "enabling-log-based-replication"
    content: |
      Using {{ page.title }} requires a specific database configuration. Instructions for configuring the required settings varies from database to database.

      For setup instructions, refer to the documentation for your database:

      {% assign all-databases = site.database-integrations | where:"input",true %}
      {% assign only-binlog-databases = all-databases | where:"log-based-replication-master-instance",true | sort: "title" %}

      {% for database in only-binlog-databases %}
      - [{{ database.title }}]({{ database.url | prepend: site.baseurl }})
      {% endfor %}
---
{% include misc/data-files.html %}
{% include misc/icons.html %}