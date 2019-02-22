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

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "oracle"
display_name: "Oracle"

singer: true
tap-name: "Oracle"
repo-url: ""

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

log-based-replication-minimum-version: "TODO"
log-based-replication-master-instance: true
log-based-replication-read-replica: true

## Other Replication Methods

key-based-incremental-replication: false
full-table-replication: true

view-replication: false


# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: |
      **Access to the `V$DATABASE` performance view.** This is required to verify setting configuration while setting up your {{ integration.display_name }} database. Refer to [{{ integration.display_name }}'s documentation](https://docs.oracle.com/cd/B19306_01/server.102/b14237/dynviews_1001.htm#i1398692){:target="new"} for more info on performance views.
  - item: |
      **`CREATE USER` and `GRANT` privileges.** The [`CREATE USER`](https://docs.oracle.com/cd/B19306_01/server.102/b14200/statements_8003.htm#i2065278){:target="new"} and [`GRANT`](https://docs.oracle.com/cd/B19306_01/server.102/b14200/statements_9013.htm#sthref9170){:target="new"} privileges are required to create a database user for Stitch and grant the necessary privileges to the user.
  - item: |
      **Appropriate `GRANT` or object permissions for the objects you want to replicate.** This is necessary to grant the privileges necessary for selecting data to the Stitch database user. Refer to [{{ integration.display_name }}'s documentation](https://docs.oracle.com/cd/B19306_01/server.102/b14200/statements_9013.htm#i2094944){:target="new"} for more info.
  - item: |
      **System administrator (`SYSDBA`) privileges, if replicating data incrementally.** This is necessary to complete steps required to use {{ integration.display_name }} LogMiner, which enables the use of Log-based Incremental Replication. Refer to [{{ integration.display_name }}'s documentation](https://docs.oracle.com/database/121/ADMQS/GUID-2033E766-8FE6-4FBA-97E0-2607B083FA2C.htm#ADMQS12004){:target="new"} for more info.
  - item: |
      **An existing Recovery Manager (RMAN) configuration, if replicating data incrementally.** RMAN is used to manage database backups and archive logs and is required to use Log-based Incremental Replication. Setting up RMAN is outside the scope of this tutorial. If you need help setting up and using RMAN, refer to [{{ integration.display_name }}'s documentation](https://docs.oracle.com/cd/B28359_01/backup.111/b28270/rcmquick.htm#BRADV89346){:target="new"} or loop in a member of your technical team.


# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "whitelist stitch ips"

  - title: "Retrieve the database's Oracle System ID"
    anchor: "retrieve-oracle-system-id"
    content: |
      An Oracle System ID (SID) is used to uniquely identify a specific database in your system. When you connect an {{ integration.display_name }} database to Stitch, you'll enter the SID of the database you want Stitch to extract data from into the **{{ app.page-names.int-settings }}** page.

      To retrieve your database's SID, log into your database as a user with access to the `SYS.V_$THREAD` performance view and run the following:

      ```sql
      SELECT INSTANCE FROM SYS.V_$THREAD
      ```

      The value returned by the query will be the database's SID. Keep this handy - you'll need it to complete the setup.

  - title: "Enable Log-based Incremental Replication with LogMiner"
    anchor: "enable-logminer"
    content: |
      {% include note.html type="single-line" content="**Note**: Some data types may not be supported for Log-based Incremental Replication. Refer to the [Data Type Mapping](#data-type-mapping) section for more info." %}

      {% capture full-table-notice %}
      **Note**: Log-based Incremental Replication via LogMiner is the only incremental replication method supported for {{ integration.display_name }} integrations at this time. If you choose not to enable this replication method, you will be required to use [Full Table Replication]({{ link.replication.full-table | prepend: site.baseurl }}).
      {% endcapture %}

      {% include note.html type="single-line" content=full-table-notice %}

      Log-based Incremental Replication is the most efficient way to replicate {{ integration.display_name }} data. Stitch uses Oracle's LogMiner package to query Oracle's archive logs and retrieve all inserts, updates, and deletes to your database. 

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

          If the result to the query in [Step 3.1](#verify-current-archiving-mode) is `NOARCHIVELOG`, then you'll need to enable `ARCHIVELOG` mode. **Skip this step if the result was `ARCHIVELOG`.**

          1. Shut down the database instance. The database and any associated instances must be shut down before the datbase's archiving mode can be changed.

             ```sql
             SHUTDOWN IMMEDIATE
             ```

          2. **If desired, back up the database.** [Oracle recommends backing up databases before any major changes](https://docs.oracle.com/database/121/ADMIN/archredo.htm#ADMIN-GUID-C12EA833-4717-430A-8919-5AEA747087B9){:target="new"}. Refer to [Oracle's documentation](https://docs.oracle.com/database/121/BRADV/rcmcncpt.htm#BRADV002){:target="new"} for more info.

          3. Start a new instance and mount (but not open) the database:

             ```sql
             STARTUP MOUNT
             ```

          4. Change the database's archiving mode and re-open it:

             ```sql
             ALTER DATABASE ARCHIVELOG;
             ALTER DATABASE OPEN;
             ```

      - title: "Configure RMAN backups"
        anchor: "configure-rman-backups"
        content: |
          {% capture configure-rman-step-notice %}
          1. System administrator (`SYSDBA`) privileges in {{ integration.display_name }}
          2. An existing Recovery Manager (RMAN) configuration. Setting up RMAN is outside the scope of this tutorial. If you need help setting up and using RMAN, refer to [{{ integration.display_name }}'s documentation](https://docs.oracle.com/cd/B28359_01/backup.111/b28270/rcmquick.htm#BRADV89346){:target="new"} or loop in a member of your technical team.
          {% endcapture %}
          {% include note.html first-line="**Note: This step requires:**" content=configure-rman-step-notice %}

          Next, you'll configure Recovery Manager (RMAN) backups. This setting defines how long the database will retain backups and archive logs, which is what Stitch will read from to perform Log-based Incremental Replication. Refer to [{{ integration.display_name }}'s documentation](https://docs.oracle.com/cd/B28359_01/backup.111/b28270/rcmquick.htm#BRADV89347){:target="new"} for more info about RMAN.

          Stitch recommends a retention period of at least 3 days, but strongly recommends 7. To specify the RMAN retention policy, run the following:

          ```sql
          {{ site.data.taps.extraction.database-setup.server-settings.oracle.rman-retention-policy | strip }}
          ```

          {% capture disk-storage-notice %}
          To ensure that archive log files don't consume all of your available disk space, you should also set the `DB_RECOVERY_FILE_DEST_SIZE` parameter to a value that agrees with your available disk quota. Refer to [{{ integration.display_name }}'s documentation](https://docs.oracle.com/cd/B28359_01/backup.111/b28270/rcmconfb.htm#BRADV89425){:target="new"} for more info about this parameter.
          {% endcapture %}

          {% include important.html type="single-line" content=disk-storage-notice %}

      - title: "Enable supplemental logging"
        anchor: "enable-supplemental-logging"
        content: |
          {% capture enable-supplemental-logging-step-notice %}
          **Note**: This step requires system administrator (`SYSDBA`) privileges in {{ integration.display_name }}.
          {% endcapture %}
          {% include note.html type="single-line" content=enable-supplemental-logging-step-notice %}

          In this step, you'll enable supplemental logging for the database. This ensures that columns are logged in redo log files, which is required by {{ integration.display_name }} to use LogMiner. Refer to [{{ integration.display_name }}'s documentation](https://docs.oracle.com/cd/B19306_01/server.102/b14215/logminer.htm#i1021068){:target="new"} for more info about supplemental logging.

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

      Next, you'll create a dedicated database user for Stitch. This will ensure Stitch is visible in any logs or audits, and allow you to maintain your privilege hierarchy.

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
        anchor: "define-log-based-replication-method"
        content: |
          {% include integrations/databases/setup/binlog/log-based-replication-default-setting.html type="default-replication-method" %}

      - title: "Create a replication schedule"
        anchor: "create-replication-schedule"
        content: |
          {% include integrations/shared-setup/replication-frequency.html %}

  - title: "replication frequency"

  - title: "sync data"

## ABOUT V_$LOGMNR_CONTENTS:
# If LogMiner is being used on the source database, then you can direct LogMiner to find and create a list of redo log files for analysis automatically. Use the CONTINUOUS_MINE option when you start LogMiner with the DBMS_LOGMNR.START_LOGMNR procedure, and specify a time or SCN range. Although this example specifies the dictionary from the online catalog, any LogMiner dictionary can be used.
# This is used (probably) to identify where to start the replication job using the saved max SCN value

# (DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=oracle-test.clcudnvirbnr.us-east-1.rds.amazonaws.com)(PORT=1521))(CONNECT_DATA=(SID=ORCL)))
---
{% assign integration = page %}
{% include misc/data-files.html %}