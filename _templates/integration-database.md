---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: DATABASE-INTEGRATION
keywords: database_integration, database integration, etl database_integration, database_integration etl
tags: [database_integrations]
permalink: /integrations/databases/database_integration
summary: "Connect and replicate data from your DATABASE-INTEGRATION database using Stitch's DATABASE-INTEGRATION integration."

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "database_integration"
display_name: "DATABASE_INTEGRATION"
author: "Stitch"
status: "Released"
frequency: "30 minutes"
tier: "Free" ## Free vs Paid Stitch plan
port: ## Database's default port - ex: 3306
db-type: "mysql" 	## mysql,postgres,mongo,mssql
icon: /images/integrations/icons/database_integration.svg

# -------------------------- #
#       Stitch Supports      #
# -------------------------- #

versions: "n/a" ## If Stitch only supports certain versions, enter them here
ssh: true	## true if Stitch supports SSH connections
ssl: false	## true if Stitch supports SSL connections
sync-views: false	## true if Stitch supports syncing database views

whitelist: ## indicates ability to select individual tables & columns for replication
  tables: "Yes"		## can the user whitelist tables?
  columns: "Yes"	## can the user whitelist columns?
---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}
In this article, we'll walk you through connecting your DATABASE-INTEGRATION database to Stitch. **You'll need some tech expertise to complete the setup**, so we recommend looping in a developer or a member of your tech team to help out if you haven't done this before.

Connecting an DATABASE-INTEGRATION database is a seven-step process:

1. [Whitelist the Stitch IP addresses](#whitelist-stitch-ips)
2. [Retrieve the Stitch Public Key](#retrieve-public-key) `*`
3. [Create a Stitch Linux user](#create-linux-user) `*`
4. [Create a database user for Stitch](#create-stitch-db-user)
5. [Enter the connection info into Stitch](#enter-connection-info)
6. [Define the Replication Frequency](#define-rep-frequency)
7. [Sync data & select Replication Methods](#syncing-data)

{% include integrations/databases/setup/db-sections.html %}
{% endcontentfor %}



{% contentfor replication-notes %}
{% include replication/databases/db-sync-queries.html %}
{% endcontentfor %}