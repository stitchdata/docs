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

title: DATABASE-INTEGRATION
keywords: database_integration, database integration, etl database_integration, database_integration etl
permalink: /integrations/databases/database_integration
summary: "Connect and replicate data from your DATABASE-INTEGRATION database using Stitch's DATABASE-INTEGRATION integration."

show-in-menus: true
key: "database_integration-integration"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "database_integration"
display_name: "DATABASE-INTEGRATION"

singer: true
tap-name: ""
repo-url: ""

this-version: ""

hosting-type: "" ## amazon, microsoft, google, etc.

driver: |
  [](){:target="new"}


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.driver | flatify | strip }}. [TODO]


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true/false

frequency: "30 minutes"
tier: "Free/Standard/Enterprise"
port: ## Database's default port - ex: 3306
db-type: ""

## Stitch features

api-type: ""
versions: "n/a"
ssh: true/false
ssl: true/false

## General replication features

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true
table-level-reset: true

## Replication methods

define-replication-methods: true/false

log-based-replication-minimum-version: ""
log-based-replication-master-instance: true/false
log-based-replication-read-replica: true/false

## Other Replication Methods

key-based-incremental-replication: true/false
full-table-replication: true/false

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