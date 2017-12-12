---
title: Amazon RDS
keywords: amazon, amazon rds, rds, relational database services, database integration, etl rds, rds etl
tags: [database_integrations]
permalink: /integrations/databases/amazon-rds
summary: "Connect and replicate data from your Amazon RDS database using Stitch's RDS integration."

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "rds"
display_name: "RDS"
author: "Stitch"
author-url: "https://www.stitchdata.com"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

frequency: "30 minutes"
tier: "Free"
port: 
db-type: "rds"
icon: /images/integrations/icons/amazon-rds.svg

versions: "Depends on database type"
ssh: true
ssl: false
sync-views: false
whitelist:
  tables: true
  columns: true

# -------------------------- #
#           Notices          #
# -------------------------- #

notice: |
  This guide describes how to connect Amazon RDS **as an input data source.**

  If you want to connect a Postgres-RDS instance as a **destination**, refer to the [Connecting an RDS-Postgres Destination guide]({{ link.destinations.setup.postgres-rds | prepend: site.baseurl }}).

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: "**Permissions in AWS that allow you to create/manage Security Groups.** This is required to whitelist Stitch's IP addresses."
  - item: "**Permissions in AWS that allow you to view database details.** This is required for retrieving the database's connection details."
  - item: "**Database permissions that allow you to create users and grant privileges.** This is required to create a database user for Stitch and grant the permissions needed for replication."

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "whitelist stitch ips"

  - title: "retrieve public key"

  - title: "create linux user"

  - title: "create db user"

  - title: "Locate RDS Connection Details in AWS"
    anchor: "locating-rds-database-details"
    content: |

      The majority of this info can be found on the Database Details page in the AWS Console.

      1. Navigate to the **RDS Dashboard.**
      2. Select the RDS instance you want to connect to Stitch.
      3. Click the **Instance Actions** menu and select **See Details**.
      4. On this page, you'll need to locate these fields:

         - **Endpoint**
         - **Port**

      Below is a screen cap of this page with the required fields highlighted:

      ![Amazon RDS Database Details page.]({{ site.baseurl }}/images/integrations/amazon-rds-details-page.png)

      Leave this page open for now - you'll need it to complete the setup in the next step.

  - title: "connect stitch"

  - title: "replication frequency"

  - title: "sync data"
---
{% assign integration = page %}
{% include misc/data-files.html %}
