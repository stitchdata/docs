---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas/
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Workday RaaS
permalink: /integrations/saas/workday-raas
keywords: workday-raas, integration, schema, etl workday-raas, workday-raas etl, workday-raas schema
layout: singer
# input: false

key: "workday-raas-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "workday-raas"
display_name: "Workday RaaS"

singer: true
status-url: ""

tap-name: "workday-raas"
repo-url: https://github.com/singer-io/tap-workday-raas

this-version: "1"

api: |
  [RaaS API](https://community.workday.com/api){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

api-type: "platform.workday-raas" 

historical: "1 year"
frequency: "1 hour"
tier: "Enterprise"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

# attribution-window: "# days"
# attribution-is-configurable: 

# setup-name: ""


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data from your defined  reports using the {{ integration.api | flatify | strip }}. For more information on this integration's table creation, refer to the [Schema](#schema) section.


# -------------------------- #
#      Incompatibilities     #
# -------------------------- #

## uncomment section below if integration is compatible with any Stitch destinations
## if incompatible with multiple destinations, create a section for each destination

## incompatible:
  ## [redshift]: "always,sometimes,never"
  ## reason: "copy" 

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "Retrieve your report URL"
    anchor: "retrieve-report-url"
    content: |
      1. Login to your {{ integration.display_name }} account.
      2. Navigate to your reports.
      3. Select the report you want to replicate in Stitch and ensure that the **Enable As Web Service** box is checked.
      4. Copy the report URL and keep it available for the next step.

      If you would like to replicate multiple reports, repeat steps 3 and 4.

  - title: "add integration"
    content: |
      4. In the **Username** field, enter the username for your {{ integration.display_name }} account.
      5. In the **Password** field, enter the password for your {{ integration.display_ name }} account.
      6. In the **Report** field, enter the name you would like to name your table. Since this integration replicates data from reports, Stitch converts them into tables.
      7. In the **Report** field, enter the report URL you obtained in [step 1](#retrieve-report-url).

      If you would like to replicate more reports, click on **Configure another report**.

  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data" ## remove this if the integration doesn't support at least table selection


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/saas-integration


# Remove this if you don't need it:
schema-sections:
 - title: "Workday RaaS table creation"
   anchor: "table-creation"
   content: |
     To replicate your report data, this integration requires you to first define a report within your Workday tenant. The URL for that report is what Stitch uses to extract your data and then transform them into tables.

---
{% assign integration = page %}
{% include misc/data-files.html %}