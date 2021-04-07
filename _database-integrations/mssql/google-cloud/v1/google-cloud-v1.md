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

title: "Google CloudSQL SQL Server (v1)"
keywords: google-cloudsql-microsoft-sql-server, database integration, etl google-cloudsql-microsoft-sql-server, google-cloudsql-microsoft-sql-server etl
permalink: /integrations/databases/google-cloudsql-microsoft-sql-server
summary: "Connect and replicate data from your Google CloudSQL SQL Server database using Stitch's Microsoft SQL Server integration."

show-in-menus: true
key: "google-cloudsql-microsoft-sql-server-integration"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "google-cloudsql-microsoft-sql-server"
display_name: "CloudSQL SQL Server"
setup-name: "Microsoft SQL Server"

singer: true
tap-name: "Microsoft SQL Server"
repo-url: "https://github.com/singer-io/tap-mssql"

this-version: "1"

hosting-type: "google-cloudsql" ## amazon, microsoft, google, etc.

driver: "7.2.1.jre8"


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

##feature-summary: |
##Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.driver | flatify | strip }}. [TODO]


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

frequency: "30 minutes"
tier: "Standard"
port: 1433
db-type: "mssql"

## Stitch features

api-type: "platform.mssql"
versions: "2012 through 2017"
ssh: false
ssl: false

## General replication features

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true
select-all: false
select-all-reason: |
  {{ integration.display_name }} integrations don't currently support a default Replication Method, which is required to use the Select All feature. The default Replication Method setting is only available for integrations that support Log-based Incremental Replication.

table-level-reset: true

## Replication methods

define-replication-methods: true

log-based-replication-minimum-version: "n/a"
log-based-replication-master-instance: false
log-based-replication-master-instance-reason: "Google CloudSQL doesn't currently support Change Tracking for CloudSQL SQL Server."
log-based-replication-read-replica: false

## Other Replication Methods

key-based-incremental-replication: true
full-table-replication: true

view-replication: true


# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: "**Permissions in Google Cloud that allow you to modify the database's connection settings.** This is required to whitelist Stitch's IP addresses."
  
  - item: "**A database running {{ integration.display_name }} version {{ page.versions }}.** {{ integration.display_name }} 2012 is the miminum version that Stitch supports for this type of integration."


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

  - title: "Create a Stitch database user"
    anchor: "create-a-database-user"
    content: |
      In this step, you'll create a dedicated database user for Stitch. This will ensure Stitch is visible in any logs or audits, and allow you to maintain your privilege hierarchy.

      {% include integrations/templates/create-database-user-tabs.html %}
      
  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      In this step, you'll complete the setup by entering the database's connection details and defining replication settings in Stitch.

      {% for substep in step.substeps %}
      - [Step 4.{{ forloop.index }}: {{ substep.title | flatify }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Define the database connection details"
        anchor: "define-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="general" %}

      - title: "Create a replication schedule"
        anchor: "create-replication-schedule"
        content: |
          {% include integrations/shared-setup/replication-frequency.html %}

      - title: "Save the integration"
        anchor: "save-integration"
        content: |
          {% include shared/database-connection-settings.html type="finish-up" %}        

  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %}
---
{% assign integration = page %}
{% include misc/data-files.html %}
