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

title: QuickBooks (v1)
permalink: /integrations/saas/quickbooks/v1
keywords: quickbooks, integration, schema, etl quickbooks, quickbooks etl, quickbooks schema
layout: singer
input: false

key: "quickbooks-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "quickbooks"
display_name: "QuickBooks"

singer: true
status-url: "http://status.developer.intuit.com/"

tap-name: "QuickBooks" ## Ex: Intercom, not intercom
repo-url: https://github.com/singer-io/tap-quickbooks

this-version: "1"

api: |
  [{{ integration.display_name }} Online API](https://developer.intuit.com/app/developer/qbo/docs/develop){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.quickbooks"

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
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.
  
  **Note**: Currently, replicating data from {{ integration.display_name }} desktop apps isn't supported.

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

requirements-list:
  - item: "**An online {{ integration.display_name }} instance.** Desktop instances aren't currently supported."

setup-steps:
  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "authorize-stitch"
    content: |
      Lastly, you'll be directed to {{ integration.display_name }}' website to complete the setup.

      1. If you're not already signed into your {{ integration.display_name }} account, enter your credentials and click **Login**.
      2. A screen asking for authorization to {{ integration.display_name }} will display.
      3. Click **Authorize.**
      4. After the authorization process successfully completes, you'll be redirected back to Stitch.
      5. Click {{ app.buttons.finish-int-setup }}.
  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %}


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/quickbooks/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}
