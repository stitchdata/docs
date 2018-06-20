---
title: Amazon PostgreSQL RDS
keywords: amazon, amazon rds, rds, relational database services, database integration, etl rds, rds etl
tags: [database_integrations]
permalink: /integrations/databases/amazon-rds-postgresql
summary: "Connect and replicate data from your Amazon PostgreSQL RDS using Stitch's PostgreSQL integration."
microsites:
  - title: "{{ page.display_name }} to Postgres"
    url: "http://postgres.topostges.com/"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "postgresql-rds"
display_name: "PostgreSQL RDS"
author: "Stitch"
author-url: "https://www.stitchdata.com"

this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

frequency: "30 minutes"
tier: "Free"
port: 5432
db-type: "postgres"
icon: /images/integrations/icons/postgres-rds.svg

versions: "9.3+; 9.4+ for binlog" ## but 9.4+ is required to use log-based replication
ssh: true
ssl: true
sync-views: true
supports-binlog: true
whitelist:
  tables: true
  columns: true

setup-name: "PostgreSQL"

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

notice: |
  This guide describes how to connect {{ integration.display_name }} **as an input data source.**

  If you want to connect a {{ integration.display_name }} instance as a **destination**, refer to the [Connecting an {{ integration.display_name }} Destination guide]({{ link.destinations.setup.postgres-rds | prepend: site.baseurl }}).

requirements-list:
  - item: |
      **Permissions in Amazon Web Services (AWS) that allow you to**:

        - Create/manage Security Groups, which is required to whitelist Stitch's IP addresses.
        - View database details, which is required for retrieving the database's connection details.
  - item: |
      **If you want to use Log-based Replication**, you need:

      - **To be running PostgreSQL 9.4 or greater**. Earlier versions of PostgreSQL do not include logical replication functionality, which is required for Log-based Replication.
      
      - **The `rds_superuser` role in your {{ integration.display_name }} database, if you want to use Log-based Replication.** [This role](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.html#Appendix.PostgreSQL.CommonDBATasks.Roles){:target="new"} is required to grant the `rds_replication` privilege to Stitch's database user.
  - item: "**To be running PostgeSQL 9.3+ or greater**, or 9.4 or greater if you want to use Log-based Replication."
  - item: "**Permissions in PostgreSQL that allow you to create users.** This is required to create a database user for Stitch."
  - item: |
      **To verify if the database is a read replica, or follower**. While we always recommend connecting a replica over a production database, this also means you may need to verify some of its settings - specifically the `standby` settings - before connecting it to Stitch.

      Info about these settings can be found in the [Configure the database parameter group](#configure-database-parameter-group) section.

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "whitelist stitch ips"

  - title: "retrieve public key"

  - title: "create linux user"

  - title: "Configure database server settings"
    anchor: "server-settings"
    content: |
      {% include integrations/databases/setup/binlog/configure-server-settings-intro.html %}
    substeps:
      - title: "Configure the database parameter group"
        anchor: "configure-database-parameter-group"
        content: |
          {% include integrations/databases/setup/binlog/amazon-rds/postgresql-rds.html %}

      - title: "Define the backup retention period"
        anchor: "define-backup-retention-period"
        content: |
          {% include integrations/databases/setup/binlog/amazon-rds/define-database-settings.html content="backup-retention-period" %}

      - title: "Apply parameter changes and reboot the database"
        anchor: "apply-changes-reboot-database"
        content: |
          {% include integrations/databases/setup/binlog/amazon-rds/define-database-settings.html content="reboot-the-instance" %}

  - title: "Create a replication slot"
    anchor: "create-replication-slot"
    content: |
      {% include integrations/databases/setup/binlog/postgres-replication-slot.html %}

  - title: "Create a Stitch database user"
    anchor: "create-a-database-user"
    content: |
      Next, you'll create a dedicated database user for Stitch. This will ensure Stitch is visible in any logs or audits, and allow you to maintain your privilege hierarchy.

      {% include integrations/templates/create-database-user-tabs.html %}

  - title: "Locate RDS connection details in AWS"
    anchor: "locating-rds-database-details"
    content: |

      {% include shared/aws-connection-details.html %}

  - title: "connect stitch"

  - title: "replication frequency"

  - title: "sync data"
---
{% assign integration = page %}
{% include misc/data-files.html %}
