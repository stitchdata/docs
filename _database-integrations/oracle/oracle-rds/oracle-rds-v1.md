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

title: Amazon Oracle RDS (v1)
keywords: oracle, oracle rds, database integration, etl oracle, oracle etl
permalink: /integrations/databases/amazon-oracle-rds
summary: "Connect and replicate data from your Amazon Oracle RDS database using Stitch's Oracle integration."
show-in-menus: true

key: "amazon-oracle-rds-integration"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "oracle-rds"
display_name: "Amazon Oracle RDS"

singer: true
tap-name: "Oracle"
repo-url: "https://github.com/singer-io/tap-oracle"

this-version: "1"

hosting-type: "amazon"

driver: |
  [cx_Oracle 6.1](https://cx-oracle.readthedocs.io/en/latest/){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

enterprise: true
enterprise-cta:
  feature: "Oracle integrations "
  title: "{{ site.data.strings.enterprise.title.are-an | prepend: page.enterprise-cta.feature }}"
  copy: "{{ site.data.strings.enterprise.copy.are-an | prepend: page.enterprise-cta.feature | flatify }}"

setup-name: "Oracle"

frequency: "30 minutes"
tier: "Enterprise"
port: 1521
db-type: "oracle"

## Stitch features
api-type: "platform.oracle"
versions: "n/a"
ssh: true
ssl: false

## General replication features

anchor-scheduling: true
cron-scheduling: true

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
log-based-replication-maximum-version: "18c"
log-based-replication-master-instance: true
log-based-replication-read-replica: false

## Other Replication Methods

key-based-incremental-replication: true
full-table-replication: true

view-replication: false


# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: |
      **Privileges in Amazon Web Services (AWS) that allow you to**:

        - **Create/manage Security Groups**. This is required to whitelist Stitch's IP addresses.
        - **Modify database instances**. This is required to enable settings required for incremental replication.
        - **View database details**. This is required to retrieve the database's connection details.

  - item: |
      **Privileges in the {{ integration.display_name }} database that allow you to**:

        - **Access the `V$DATABASE` and `V_$THREAD` performance views.** These are required to verify setting configuration while setting up your {{ integration.display_name }} database and to retrieve the database's Oracle System ID. Refer to [{{ integration.display_name }}'s documentation]({{ site.data.taps.links[integration.db-type]reference-docs.vdatabase }}){:target="new"} for more info on performance views.
        
        - **Create users and grant privileges.** The [`CREATE USER`]({{ site.data.taps.links[integration.db-type]reference-docs.create-user }}){:target="new"} and [`GRANT`]({{ site.data.taps.links[integration.db-type]reference-docs.grant }}){:target="new"} privileges are required to create a database user for Stitch and grant the necessary privileges to the user.

        - **`GRANT` access to the objects you want to replicate.**  This is necessary to grant the privileges necessary for selecting data to the Stitch database user. Refer to [{{ integration.display_name }}'s documentation]({{ site.data.taps.links[integration.db-type]reference-docs.grant }}){:target="new"} for more info.

  - item: |
      **If using Log-based Incremental Replication, you need**:

      - **A database using Oracle {{ integration.log-based-replication-minimum-version }} through {{ integration.log-based-replication-maximum-version }}**. Versions earlier than {{ integration.log-based-replication-minimum-version }} and later than {{ integration.log-based-replication-maximum-version }} don't include LogMiner functionality, which is required for Log-based Incremental Replication.


# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Configure database connection settings"
    anchor: "connect-settings"
    content: |
      {% include integrations/templates/configure-connection-settings.html %}

  - title: "Enable Log-based Incremental Replication with LogMiner"
    anchor: "enable-logminer"
    content: |
      {% include note.html type="single-line" content="**Note**: Skip this step if you're not planning to use Log-based Incremental Replication. [Click to skip ahead](#db-user)." %}

      {% include integrations/databases/setup/binlog/configure-server-settings-intro.html %}

      {% for substep in step.substeps %}
      - [Step 2.{{ forloop.index }}: {{ substep.title }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Enable AWS automated backups"
        anchor: "enable-aws-automated-backups"
        content: |
          {% capture rds-backup-requirement %}
          1. Privileges in AWS that allow you to modify database instances.
          2. Rebooting the database for changes to take effect. Perform this step during off-peak hours to minimize disruptions.
          {% endcapture %}
          {% include note.html first-line="**Note: This step requires**:" content=rds-backup-requirement %}

          {% include integrations/databases/setup/binlog/amazon-rds/define-database-settings.html content="backup-retention-period" starting-point="sign-in" %}

          {% include integrations/databases/setup/binlog/amazon-rds/define-database-settings.html content="reboot-the-instance" %}

      - title: "Define ARCHIVELOG retention hours"
        anchor: "define-archivelog-retention-hours"
        content: |
          In addition to the [backup retention period](#define-backup-retention-period), you also need to define the `archivelog retention hours` setting. This parameter specifies the number of hours the database server should retain archive logs.

          To specify the number of hours, use the [rdsadmin.rdsadmin_util.set_configuration]({{ site.data.taps.links.oracle.amazon-oracle-rds.archivelog-retention-hours }}){:target="new"} procedure when logged into the {{ integration.display_name }} master instance.

          In this example, archive logs will be retained for seven days (`24 hours x 7 days = 168 hours`):

          ```sql
          {{ site.data.taps.extraction.database-setup.server-settings.oracle.log-mode.rds | strip }}
          ```

          Stitch recommends a minimum of three days for the retention period, but strongly recommends seven.

      - title: "Enable supplemental logging"
        anchor: "enable-supplemental-logging"
        content: |
          In this step, you'll enable supplemental logging for the database. This ensures that columns are logged in redo log files when changes are made to the database, which is required by {{ integration.display_name }} to use LogMiner. Refer to [{{ integration.display_name }}'s documentation]({{ site.data.taps.links[integration.db-type]supplemental-logging }}){:target="new"} for more info about supplemental logging.

          To enable supplemental logging, run:

          ```sql
          {{ site.data.taps.extraction.database-setup.server-settings.oracle.supplemental-logging.rds | strip }}
          ```

          The result should be `PL/SQL procedure successfully completed`.

          Next, verify that supplemental logging was successfully enabled by running the following query:

          ```sql
          {{ site.data.taps.extraction.database-setup.server-settings.oracle.supplemental-logging.command | strip }}
          ```

          If the result is `YES`, supplemental logging was successfully enabled.

  - title: "Create a Stitch {{ integration.display_name }} database user"
    anchor: "db-user"
    content: |
      {% capture create-db-user-step-notice %}
      **Note**: This step requires `CREATE USER` and `GRANT` privileges in {{ integration.display_name }}.
      {% endcapture %}

      {% include note.html type="single-line" content=create-db-user-step-notice %} 

      Next, you'll create a dedicated database user for Stitch. This will ensure Stitch is visible in any logs or audits and allow you to maintain your privilege hierarchy.

      {% include integrations/templates/create-database-user-tabs.html %}

  - title: "Retrieve the database's Oracle System ID"
    anchor: "retrieve-oracle-system-id"
    content: |
      {% include integrations/databases/setup/binlog/oracle-retrieve-sid.html %}

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      In this step, you'll complete the setup by entering the database's connection details and defining replication settings in Stitch.

      {% for substep in step.substeps %}
      - [Step 5.{{ forloop.index }}: {{ substep.title | flatify }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Locate the database connection details in AWS"
        anchor: "locate-connection-details"
        content: |
          {% include shared/connection-details/amazon.html type="connection-details" %}

      - title: "Define the database connection details in Stitch"
        anchor: "define-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="general" %}

      - title: "Define the SSH connection details"
        anchor: "ssh-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="ssh" %}

      - title: "Define the default replication method"
        anchor: "define-default-replication-method"
        content: |
          {% include integrations/databases/setup/binlog/log-based-replication-default-setting.html type="default-replication-method" %}

      - title: "Create a replication schedule"
        anchor: "create-replication-schedule"
        content: |
          {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Select data to replicate"
    anchor: "sync-data"
    content: |
      {% include integrations/databases/setup/syncing.html %}


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
    anchor: "logminer-replication-integration"
    content: |
      Stitch uses {{ integration.display_name }}'s [LogMiner package]({{ site.data.taps.links[integration.name]logminer }}){:target="new"} to replicate data incrementally. This means that when Log-based Incremental is selected as the Replication Method for a table, Stitch will only replicate new or updated data for the table during each replication job.

      To identify new and updated data, Stitch uses {{ integration.display_name }}'s [Approximate Commit System Change Numbers]({{ site.data.taps.links[integration.name]reference-docs.commit-scn }}){:target="new"}, or SCNs, as [Replication Keys]({{ link.replication.rep-keys | prepend: site.baseurl }}). When reading from the database's logs, records with an SCN value greater than the maximum SCN from the previous job will be replicated.

      Refer to the [Log-based Incremental Replication documentation]({{ link.replication.log-based-incremental | prepend: site.baseurl }}) for a more detailed explanation, examples, and the limitations associated with this replication method.

  - title: "Data types"
    anchor: "data-types"
    content: |
      {% include replication/templates/data-types/integration-specific-data-types.html specific-types=true display-intro=true version="1.0" version-column-headers=false %}

---
{% assign integration = page %}
{% include misc/data-files.html %}
