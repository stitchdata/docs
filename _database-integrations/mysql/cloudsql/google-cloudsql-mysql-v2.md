---
title: Google CloudSQL MySQL (v2)
keywords: google cloudsql, cloudsql, cloud sql, database integration, etl cloudsql, cloudsql etl, cloudsql mysql, cloudsql mysql etl
permalink: /integrations/databases/google-cloudsql-mysql/v2
summary: "Connect and replicate data from your Google CloudSQL MySQL database using Stitch's Google CloudSQL MySQL integration."

key: "cloudsql-mysql-integration"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "cloudsql-mysql"
display_name: "Google CloudSQL MySQL"
singer: true



this-version: "2"

hosting-type: "google-cloudsql"

driver: |
  [PyMySQL 0.7.11](https://pymysql.readthedocs.io/en/latest/){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #


certified: true

frequency: "30 minutes"
tier: "Standard"
port: 3306
db-type: "mysql"

## Stitch features
api-type: "platform.cloudsql"
versions: "n/a"
ssh: false
ssl: false

## General replication features

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true
select-all: "sometimes"
select-all-reason: "Log-based Incremental Replication must be enabled and set as the default Replication Method to use the Select All feature."

table-level-reset: true

## Replication methods

define-replication-methods: true
set-default-replication-method: true

log-based-replication-minimum-version: "5.6.2"
log-based-replication-master-instance: true

log-based-replication-read-replica: false
log-based-replication-read-replica-reason: "Google CloudSQL MySQL doesn't support binary logging on read replicas."

## Other Replication Methods

key-based-incremental-replication: true
full-table-replication: true

view-replication: true

# -------------------------- #
#      Feature Summary       #
# -------------------------- #

beta-copy: |
  {% assign all-mysql = site.database-integrations | where:"key","mysql-integration" %}
  {% assign mysql-overview = all-mysql | where:"content-type","database-category" | first %}
  
  **Note**: This version differs greatly than the previous version. Refer to the [Integration feature summary]({{ integration.url | prepend: site.baseurl | append: "#feature-summary" }}) and [version comparison documentation]({{ mysql-overview.url | prepend: site.baseurl | append: "#supported-features" }}) for more info.

feature-summary: |
  {% assign all-mysql = site.database-integrations | where:"key","mysql-integration" %}
  {% assign mysql-overview = all-mysql | where:"content-type","database-category" | first %}

  This version (v{{ integration.this-version }}) of Stitch's {{ integration.display_name }} integration optimizes replication by utilizing Avro schemas to write and validate data, thereby reducing the amount of time spent on data extraction and preparation. Compared to previous versions of the {{ integration.display_name }} integration, this version boasts increased performance and overall reduced replication time.

  Notable improvements and changes in this version also include:

  - **New column (field) naming rules.** Avro has specific rules that dictate how columns can be named. As a result, column names will be canonicalized to adhere to Avro rules and persisted to your destination using the Avro-friendly name. Refer to the [Column name transformations section](#data-replication--column-name-transformations) for more info.
  - **Improved handling of `JSON` data types**. In previous versions, these data types were treated as strings. This version will send them to your destination as JSON objects, which may result in [de-nesting]({{ link.destinations.storage.nested-structures | prepend: site.baseurl }}).

  To get a look at how this version compares to the previous version of {{ integration.display_name }}, refer to the [{{ integration.display_name }} version comparison documentation]({{ mysql-overview.url | prepend: site.baseurl | append: "#supported-features" }}).


# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

notice: |
  This article only applies to **MySQL-based** CloudSQL databases.

  If you want to connect a **PostgreSQL-based** CloudSQL instance, use [these instructions]({{ link.integrations.database-integration | prepend: site.baseurl | replace: "INTEGRATION","google-cloudsql-postgresql" }}).

requirements-list:
  - item: "**Permissions in Google Cloud that allow you to modify the database's connection settings.** This is required to whitelist Stitch's IP addresses."
  - item: |
      **The `CREATE USER` or `INSERT` privilege (for the `mysql` database).** The [`CREATE USER` privilege](https://dev.mysql.com/doc/refman/8.0/en/create-user.html){:target="new"} is required to create a database user for Stitch.
  - item: |
      **The `GRANT OPTION` privilege.** The [`GRANT OPTION` privilege](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_grant-option){:target="new"} is required to grant the necessary privileges to the Stitch database user.
  - item: |
      **If using Log-based Replication**, you'll need:

      - **A database running MySQL {{ integration.log-based-replication-minimum-version }} or greater** Earlier versions of MySQL do not include binlog replication functionality, which is required for Log-based Replication.
      - **To connect to the master instance.** [Google doesn't currently support binlog replication on read replicas](https://cloud.google.com/sql/docs/mysql/replication/create-replica){:target="new"}.

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Verify your Stitch account's data pipeline region"
    anchor: "verify-stitch-account-region"
    content: |
      {% include shared/whitelisting-ips/locate-region-ip-addresses.html first-step=true %}

  - title: "Configure database connection settings"
    anchor: "connect-settings"
    content: |
      {% include integrations/templates/configure-connection-settings.html %}

# https://cloud.google.com/sql/docs/mysql/configure-ip

  - title: "Configure Log-based Incremental Replication"
    anchor: "configure-log-based-incremental-replication"
    content: |
      {% include note.html type="single-line" content="**Note**: Skip this step if you're not planning to use Log-based Incremental Replication. [Click to skip ahead](#db-user)." %}

      {% include integrations/databases/setup/binlog/configure-server-settings-intro.html %}

      {% for substep in step.substeps %}
      - [Step 3.{{ forloop.index }}: {{ substep.title | flatify }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Enable automated backups and binary logging"
        anchor: "enable-automated-backups-binary-logging"
        content: |
          In this step, you'll enable automated backups and binary logging for the {{ integration.display_name }} database. This is required to use Log-based Incremental Replication.

          {% capture server-instructions %}
          {% include layout/inline_image.html type="right" file="integrations/cloudsql-enable-binary-logging.png" alt="" max-width="500px" %}
          1. On the **Instance details** page in Google Cloud Platform, click the **Edit** option at the top of the page.
          2. In the **Configuration options** section, open **Enable auto backups**.
          3. If unchecked, check the **Automate backups** option and select a window for automated backups.

             **Note**: This is required to use Log-based Incremental Replication.
          3. If unchecked, check the **Enable binary logging** option.
          4. Click **Save**.

          When binary logging is enabled, Google Cloud SQL will define the required server settings using their pre-defined defaults. Refer to the <a href="#server-settings-details" data-toggle="tab">Server settings list</a> tab for explanations of these parameters and their default values. **No other configuration is required on your part.**
          {% endcapture %}

          {% include integrations/templates/configure-server-settings.html %}

      - title: "Retrieve server IDs"
        anchor: "server-id"
        content: |
          {% include integrations/databases/setup/binlog/mysql-server-id.html %}

  - title: "Create a Stitch database user"
    anchor: "db-user"
    content: |
      {% include note.html type="single-line" content="**Note**: You must have the `CREATE USER` and `GRANT OPTION` privileges to complete this step." %} 

      Next, you'll create a dedicated database user for Stitch. This will ensure Stitch is visible in any logs or audits, and allow you to maintain your privilege hierarchy.

      {% include integrations/templates/create-database-user-tabs.html %}

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      In this step, you'll complete the setup by entering the database's connection details and defining replication settings in Stitch.

      {% for substep in step.substeps %}
      - [Step 5.{{ forloop.index }}: {{ substep.title | flatify }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Locate the database connection details in Google"
        anchor: "locate-database-connection-details"
        content: |
          In this step, you'll locate the {{ integration.display_name }} database's IP address in the Google Cloud Platform console. This will be used to complete the setup in Stitch.

          {% include shared/connection-details/google-cloudsql.html %}

      - title: "Define the database connection details in Stitch"
        anchor: "define-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="general" %}

      - title: "Select databases to discover"
        anchor: "filter-databases"
        content: |
          {% include note.html type="single-line" content="**Note**: Skip this step if you don't need to filter databases." %}

          Enter a database name in the field under **Filter databases in the source** to select the database that Stitch can discover. You can add multiple database names by clicking **Add another database**.

          If no database is specified, Stitch will discover all databases on the host.

      - title: "Define the Log-based Replication setting"
        anchor: "define-log-based-replication-setting"
        content: |
          {% include integrations/databases/setup/binlog/log-based-replication-default-setting.html %}

      - title: "Create a replication schedule"
        anchor: "create-replication-schedule"
        content: |
          {% include integrations/shared-setup/replication-frequency.html %}

      - title: "Save the integration"
        anchor: "save-integration"
        content: |
          {% include shared/database-connection-settings.html type="finish-up" %}

  - title: "Select data to replicate"
    anchor: "sync-data"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %}

# -------------------------- #
#      Replication Info      #
# -------------------------- #

replication-sections:
  - content: |
      In this section:

      {% for section in page.replication-sections %}
      {% if section.title %}
      - [{{ section.summary | flatify }}](#{{ section.anchor }})
      {% endif %}
      {% endfor %}

  - title: "Extraction"
    anchor: "extraction-details"
    summary: "Details about Extraction, including object and data type discovery and selecting data for replication"
    content: |
      For every table set to replicate, Stitch will perform the following during Extraction:

      {% for subsection in section.subsections %}
      - [{{ subsection.summary | flatify }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Discovery"
        anchor: "extraction--discovery"
        summary: "Discover table schemas and type discovered columns"
        content: |
          During Discovery, Stitch will:

          {% for sub-subsection in subsection.sub-subsections %}
          - [{{ sub-subsection.summary | flatify }}](#{{ sub-subsection.anchor }})
          {% endfor %}
        sub-subsections:
          - title: "Determining table schemas"
            anchor: "discovery--objects"
            summary: "Determine table schemas"
            content: |
              During this phase of Discovery, Stitch queries system tables to retrieve metadata about the objects the Stitch database user has access to. This metadata is used to determine which databases, tables, and columns to display in Stitch for replication.

              {{ site.data.taps.extraction.database-queries.mysql.structure-sync | flatify | markdownify }}

          - title: "Data typing"
            anchor: "discovery--data-types"
            summary: "Type the data in discovered columns"
            content: |
              Refer to the [{{ integration.display_name }} data types documentation]({{ mysql-overview.url | prepend: site.baseurl | append: "#data-types" }}) for more info about how {{ integration.display_name }} data is typed for selected columns.

      - title: "Data replication"
        anchor: "extraction--data-replication"
        summary: "Select records for replication"
        content: |
          During data replication, Stitch will:

          {% for sub-subsection in subsection.sub-subsections %}
          - [{{ sub-subsection.summary | flatify }}](#{{ sub-subsection.anchor }})
          {% endfor %}

        sub-subsections:
          - title: "Column name transformations"
            anchor: "data-replication--column-name-transformations"
            summary: "Transform column names to adhere to Avro rules"
            content: |
              To ensure column names are compatible with Avro, the integration will transform column names to adhere to Avro's rules. In Avro, [column names must](https://avro.apache.org/docs/current/spec.html#names){:target="new"}:

              - Start with one of the following:
                 - `A-Z`
                 - `a-z`
                 - `_` (underscore)
              - Contain only the following:
                 - Any characters in the list above (`A-Z`, `_`, etc)
                 - `0-9`

              If a column name contains an unsupported character, the integration will replace it with an underscore (`_`).
---
{% assign integration = page %}
{% include misc/data-files.html %}