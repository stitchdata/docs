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

title: iLevel (v1)
permalink: /integrations/saas/ilevel
keywords: ilevel, integration, schema, etl ilevel, ilevel etl, ilevel schema
layout: singer
# input: false

key: "ilevel-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "ilevel"
display_name: "iLevel"

singer: true
status-url: ""

tap-name: "iLevel"
repo-url: https://github.com/singer-io/tap-ilevel

this-version: "1"

api: |
  [2019 SOAP API WSDL](https://services.ilevelsolutions.com/DataService/Service/2019/Q1/DataService.svc?singleWsdl){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.ilevel"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data from the [{{ integration.display_name }} Portfolio Monitoring Platform](https://ihsmarkit.com/products/ilevel.html){:target="new"} by IHS Markit using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Web Services access in {{ integration.display_name }}.** Reach out to {{ integration.display_name }} support to enable this in your {{ integration.display_name }} account. Once enabled, you can continue with the setup in Stitch.

setup-steps:
  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      5. In the **Username** field, enter the {{ integration.display_name }} API user's username.
      6. In the **Password** field, enter the {{ integration.display_name }} API user's password.
      7. **Optional**: If connecting to a sandbox environment, check **Connect to a sandbox environment**.

  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}

  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %} 


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/saas-integration
---
{% assign integration = page %}
{% include misc/data-files.html %}