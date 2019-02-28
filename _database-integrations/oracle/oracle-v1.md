---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/databases/
## FOR INSTRUCTIONS & REFERENCE INFO

# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Oracle
keywords: oracle, database integration, etl oracle, oracle etl
permalink: /integrations/databases/oracle
summary: "Connect and replicate data from your Oracle database using Stitch's Oracle integration."
show-in-menus: true

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "oracle"
display_name: "Oracle"

singer: true
tap-name: "Oracle"
repo-url: "https://github.com/singer-io/tap-oracle"

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

frequency: "30 minutes"
tier: "Enterprise"
port: 1521
db-type: "oracle"

## Stitch features

versions: "n/a"
ssh: true
ssl: true

## General replication features

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true
table-level-reset: true

## Replication methods

define-replication-methods: true

set-default-replication-method: true
default-replication-method-required: true

log-based-replication-minimum-version: "8.0"
log-based-replication-master-instance: true
log-based-replication-read-replica: false

## Other Replication Methods

key-based-incremental-replication: false
full-table-replication: true

view-replication: false


# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: |
      **Privileges in the {{ integration.display_name }} database that allow you to**:

        - **Access the `V$DATABASE` and `V_$THREAD` performance views.** These are required to verify setting configuration while setting up your {{ integration.display_name }} database and to retrieve the database's Oracle System ID. Refer to [{{ integration.display_name }}'s documentation]({{ site.data.taps.links[integration.db-type]reference-docs.vdatabase }}){:target="new"} for more info on performance views.
        
        - **Create users and grant privileges.** The [`CREATE USER`]({{ site.data.taps.links[integration.name]reference-docs.create-user }}){:target="new"} and [`GRANT`]({{ site.data.taps.links[integration.db-type]reference-docs.grant }}){:target="new"} privileges are required to create a database user for Stitch and grant the necessary privileges to the user.

        - **`GRANT` access to the objects you want to replicate.**  This is necessary to grant the privileges necessary for selecting data to the Stitch database user. Refer to [{{ integration.display_name }}'s documentation]({{ site.data.taps.links[integration.db-type]reference-docs.grant }}){:target="new"} for more info.

        - **Use System administrator (`SYSDBA`) privileges, if replicating data incrementally.** This is necessary to complete steps required to use {{ integration.display_name }} LogMiner, which enables the use of Log-based Incremental Replication. Refer to [{{ integration.display_name }}'s documentation]({{ site.data.taps.links[integration.db-type]reference-docs.system-admin }}){:target="new"} for more info.
      
  - item: |
      **An existing Recovery Manager (RMAN) configuration, if replicating data incrementally.** RMAN is used to manage database backups and archive logs and is required to use Log-based Incremental Replication. Setting up RMAN is outside the scope of this tutorial. If you need help setting up and using RMAN, refer to [{{ integration.display_name }}'s documentation]({{ site.data.taps.links[integration.db-type]recovery-manager }}){:target="new"} or loop in a member of your technical team.


# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Configure database connection settings"
    anchor: "connect-settings"
    content: |
      {% include integrations/templates/configure-connection-settings.html %}

  - title: "Retrieve the database's Oracle System ID"
    anchor: "retrieve-oracle-system-id"
    content: |
      {% include integrations/databases/setup/binlog/oracle-retrieve-sid.html %}

  - title: "Enable Log-based Incremental Replication with LogMiner"
    anchor: "enable-logminer"
    content: |
      {% include integrations/databases/setup/binlog/configure-server-settings-intro.html %}

      {% for substep in step.substeps %}
      - [Step 3.{{ forloop.index }}: {{ substep.title }}](#{{ substep.anchor }})
      {% endfor %} 

    substeps:
      - title: "Verify the database's current archiving mode"
        anchor: "verify-current-archiving-mode"
        content: |
          To check the database's current mode, run:

          ```sql
          {{ site.data.taps.extraction.database-setup.server-settings.oracle.log-mode.command | strip }}
          ```

          {{ site.data.taps.extraction.database-setup.server-settings.oracle.log-mode.result.archivelog }} Skip to [Step 3.3 to configure RMAN backups](#configure-rman-backups).

          {{ site.data.taps.extraction.database-setup.server-settings.oracle.log-mode.result.noarchivelog }} Move onto to [Step 3.2](#enable-archivelog-mode) for instructions.

      - title: "Enable ARCHIVELOG mode"
        anchor: "enable-archivelog-mode"
        content: |
          {% capture enable-archive-step-notice %}
          1. System administrator (`SYSDBA`) privileges in {{ integration.display_name }}
          2. Restarting the database. Stitch recommends performing this step during off-peak hours to minimize disruptions.
          {% endcapture %}
          {% include note.html first-line="**Note: This step requires:**" content=enable-archive-step-notice %}

          If the result to the query in [Step 3.1](#verify-current-archiving-mode) is `NOARCHIVELOG`, then you'll need to enable `ARCHIVELOG` mode. **Skip to [Step 3.3](#configure-rman-backups) if the result was `ARCHIVELOG`.**

          1. Shut down the database instance. The database and any associated instances must be shut down before the datbase's archiving mode can be changed.

             ```sql
             SHUTDOWN IMMEDIATE
             ```

          2. **If desired, back up the database.** [Oracle recommends backing up databases before any major changes]({{ site.data.taps.links[integration.name]change-archive-mode }}){:target="new"}. Refer to [Oracle's documentation]({{ site.data.taps.links[integration.name]recovery-manager-backups }}){:target="new"} for more info.

          3. Start a new instance and mount (but not open) the database:

             ```sql
             STARTUP MOUNT
             ```

          4. Change the database's archiving mode and re-open it:

             ```sql
             ALTER DATABASE ARCHIVELOG
             ALTER DATABASE OPEN
             ```

      - title: "Configure RMAN backups"
        anchor: "configure-rman-backups"
        content: |
          {% capture configure-rman-step-notice %}
          1. System administrator (`SYSDBA`) privileges in {{ integration.display_name }}
          2. An existing Recovery Manager (RMAN) configuration. Setting up RMAN is outside the scope of this tutorial. If you need help setting up and using RMAN, refer to [{{ integration.display_name }}'s documentation](https://docs.oracle.com/cd/B28359_01/backup.111/b28270/rcmquick.htm#BRADV89346){:target="new"} or loop in a member of your technical team.
          {% endcapture %}
          {% include note.html first-line="**Note: This step requires:**" content=configure-rman-step-notice %}

          Next, you'll configure Recovery Manager (RMAN) backups. This setting defines how long the database will retain backups and archive logs, which is what Stitch will read from to perform Log-based Incremental Replication. Refer to [{{ integration.display_name }}'s documentation]({{ site.data.taps.links[integration.name]recovery-manager }}){:target="new"} for more info about RMAN.

          Stitch recommends a retention period of at least 3 days, but strongly recommends 7. To specify the RMAN retention policy, run the following:

          ```sql
          {{ site.data.taps.extraction.database-setup.server-settings.oracle.rman-retention-policy | strip }}
          ```

          {% capture disk-storage-notice %}
          To ensure that archive log files don't consume all of your available disk space, you should also set the `DB_RECOVERY_FILE_DEST_SIZE` parameter to a value that agrees with your available disk quota. Refer to [{{ integration.display_name }}'s documentation]({{ site.data.taps.links[integration.name]reference-docs.db-recovery-file-dest-size }}){:target="new"} for more info about this parameter.
          {% endcapture %}

          {% include important.html type="single-line" content=disk-storage-notice %}

      - title: "Enable supplemental logging"
        anchor: "enable-supplemental-logging"
        content: |
          {% capture enable-supplemental-logging-step-notice %}
          **Note**: This step requires system administrator (`SYSDBA`) privileges in {{ integration.display_name }}.
          {% endcapture %}
          {% include note.html type="single-line" content=enable-supplemental-logging-step-notice %}

          In this step, you'll enable supplemental logging for the database. This ensures that columns are logged in redo log files, which is required by {{ integration.display_name }} to use LogMiner. Refer to [{{ integration.display_name }}'s documentation]({{ site.data.taps.links[integration.name]supplemental-logging }}){:target="new"} for more info about supplemental logging.

          Stitch supports supplemental logging at the database and table level. **Note**: You do not need to enable both. Select the level you want to use for supplemental logging (database or table) and follow the steps below:

          - **At the database level**, this means that any time a change is made to a table in the database, it will be logged in the redo log files.

            To enable supplemental logging **at the database level**, run:

            ```sql
            ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS
            ```

          - **At the table level**, this means that only changes made to the specified table will be logged in the redo log files. By only applying logging to the tables you want to replicate through Stitch, this may reduce the overall disk space used by redo log files.

            To enable supplemental logging **at the table level**, run the following for **every table you want to replicate through Stitch**:

            ```sql
            ALTER TABLE <SCHEMA_NAME>.<TABLE_NAME> ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS
            ```

          Next, verify that supplemental logging was successfully enabled by running the following query:

          ```sql
          {{ site.data.taps.extraction.database-setup.server-settings.oracle.supplemental-logging.command | strip }}
          ```

          If the returned value is `YES` or `IMPLICIT`, supplemental logging is enabled.


  - title: "Create a Stitch {{ integration.display_name }} database user"
    anchor: "db-user"
    content: |
      {% capture create-db-user-step-notice %}
      **Note**: This step requires `CREATE USER` and `GRANT` privileges in {{ integration.display_name }}.
      {% endcapture %}

      {% include note.html type="single-line" content=create-db-user-step-notice %} 

      Next, you'll create a dedicated database user for Stitch. This will ensure Stitch is visible in any logs or audits and allow you to maintain your privilege hierarchy.

      {% include integrations/templates/create-database-user-tabs.html %}

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      In this step, you'll complete the setup by entering the database's connection details and defining replication settings in Stitch.

    substeps:
      - title: "Define the database connection details"
        anchor: "define-connection-details"
        content: |
          {% include integrations/databases/setup/database-integration-settings.html type="general" %}

      # - title: "Define the SSH connection details"
      #   anchor: "ssh-connection-details"
      #   content: |
      #     {% include integrations/databases/setup/database-integration-settings.html type="ssh" %}

      - title: "Define the SSL connection details"
        anchor: "ssl-connection-details"
        content: |
          {% include integrations/databases/setup/database-integration-settings.html type="ssl" %}

      - title: "Define default replication method"
        anchor: "define-default-replication-method"
        content: |
          {% include integrations/databases/setup/binlog/log-based-replication-default-setting.html type="default-replication-method" %}

      - title: "Create a replication schedule"
        anchor: "create-replication-schedule"
        content: |
          {% include integrations/shared-setup/replication-frequency.html %}

  - title: "sync data"


# -------------------------- #
#     REPLICATION DETAILS    #
# -------------------------- #

replication-sections:
  - content: |
      {% for section in integration.replication-sections %}
      {% if section.title %}
      - [{{ section.title }}]({{ section.anchor }})
      {% endif %}
      {% endfor %}

  - title: "Overview of Log-based Incremental Replication using LogMiner"
    anchor: "logminer-replication-overview"
    content: |
      Stitch uses {{ integration.display_name }}'s [LogMiner package]({{ site.data.taps.links[integration.name]logminer }}){:target="new"} to replicate data incrementally. This means that when Log-based Incremental is selected as the Replication Method for a table, Stitch will only replicate new or updated data for the table during each replication job.

      To identify new and updated data, Stitch uses {{ integration.display_name }}'s [Approximate Commit System Change Numbers]({{ site.data.taps.links[integration.name]reference-docs.commit-scn }}){:target="new"}, or SCNs, as [Replication Keys]({{ link.replication.rep-keys | prepend: site.baseurl }}). When reading from the database's logs, records with an SCN value greater than the maximum SCN from the previous job will be replicated.

      Refer to the [Log-based Incremental Replication documentation]({{ link.replication.log-based-incremental | prepend: site.baseurl }}) for a more detailed explanation, examples, and the limitations associated with this replication method.

      **Note**: Stitch currently supports Log-based Incremental and Full Table Replication for {{ integration.display_name }} integrations. Other replication methods are not currently supported.

  - title: "Data typing and LogMiner (Log-based Incremental Replication)"
    anchor: "data-typing-logminer-replication"
    content: |
      {{ integration.display_name }}'s LogMiner packages supports the data types listed in the table below. Refer to [{{ integration.display_name }}'s documentation]({{ site.data.taps.links[integration.name]logminer-supported-datatypes }}){:target="new"} for more info.

      **Only columns with the data types listed below are able to be selected and replicated through Stitch**. Columns with data types not in this list will show as `UNSUPPORTED` in Stitch. For reference, you can view the code for data typing in Stitch's {{ integration.display_name }} integrations in the [Singer {{ integration.display_name }} GitHub repository](https://github.com/singer-io/tap-oracle/blob/master/tap_oracle/__init__.py){:target="new"}.

      {% assign attributes="name|stored-as" | split:"|" %}

      <table class="attribute-list">
      <tr>
      <td width="40%; fixed" align="right">
      <strong>{{ integration.display_name }} data type</strong>
      </td>
      <td>
      <strong>Stitch data type mapping</strong>
      </td>
      </tr>
      {% for data-type in site.data.taps.extraction.data-types[integration.name]logminer.supported %}
      <tr>
      {% for attribute in attributes %}
      {% assign attribute-number = forloop.index %}
      {% if forloop.first == true %}
      <td width="40%; fixed" align="right">
      {% else %}
      <td>
      {% endif %}
      {{ data-type[attribute] | upcase }}{% if attribute-number == 2 and data-type.formatted-as %} (formatted as {{ data-type.formatted-as | upcase }}){% endif %}
      </td>
      {% endfor %}
      </tr>
      {% endfor %}
      </table>
---
{% assign integration = page %}
{% include misc/data-files.html %}