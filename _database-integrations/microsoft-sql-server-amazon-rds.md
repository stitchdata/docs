---
title: Amazon Microsoft SQL Server RDS
keywords: amazon, amazon rds, rds, relational database services, database integration, etl rds, rds etl
tags: [database_integrations]
permalink: /integrations/databases/amazon-rds-microsoft-sql-server
summary: "Connect and replicate data from your Amazon Microsoft SQL Server RDS using Stitch's Microsoft SQL Server integration."

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "sql-server-rds"
display_name: "SQL Server RDS"
author: "Stitch"
author-url: "https://www.stitchdata.com"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

frequency: "30 minutes"
tier: "Free"
port: 1433
db-type: "mssql"
icon: /images/integrations/icons/mssql-rds.svg

versions: "n/a"
ssh: false
ssl: true
sync-views: true
whitelist:
  tables: true
  columns: true

setup-name: "Microsoft SQL Server"

binlog-replication: false

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: |
      **Permissions in Amazon Web Services (AWS) that allow you to**:

        - Create/manage Security Groups, which is required to whitelist Stitch's IP addresses.
        - View database details, which is required for retrieving the database's connection details.
  - item: "**Permissions in {{ integration.display_name }} that allow you to create/manage users.** This is required to create the Stitch database user."
  - item: |
      **A database that uses case-insensitive collation**. [More info about collation can be found here in Microsoft's documentation](https://docs.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support#Collation_Defn).

## Based on this AWS doc, enabling mixed mode auth shouldn't be necessary:
## https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerWinAuth.html

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "whitelist stitch ips"

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
