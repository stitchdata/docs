---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

# Need some help?

# See this how-to for instructions on filling out the template:
#     

# See this reference guide for more info on the parameters in this template:
#     
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
display_name: "DATABASE-INTEGRATION"

singer: true
tap-name: ""
repo-url: ""

# this-version: ""

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true/false

frequency: "30 minutes"
tier: "Free"
port: ## Database's default port - ex: 3306
db-type: "mysql" 	## mysql,postgres,mongo,mssql

## Stitch features

versions: "n/a"
ssh: true/false
ssl: false/false

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

binlog-replication: false
view-replication: true/false

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: ""
  - item: ""

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
	- title: ""
	  anchor: ""
	  content: ""

  - title: "connect stitch"

  - title: "replication frequency"

  - title: "sync data"
---
{% assign integration = page %}
{% include misc/data-files.html %}