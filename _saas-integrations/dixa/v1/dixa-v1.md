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

title: Dixa (v1)
permalink: /integrations/saas/dixa ## Add if there are multiple versions: /vVERSION
keywords: dixa, integration, schema, etl dixa, dixa etl, dixa schema
layout: singer
# input: false

key: "dixa-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "dixa"
display_name: "Dixa"

singer: true
status-url: "https://status.dixa.io/"

tap-name: "Dixa" ## Ex: Intercom, not intercom
repo-url: https://github.com/singer-io/tap-dixa

this-version: "1"

api: |
  [{{ integration.display_name }} API](https://docs.dixa.io/openapi){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.dixa"

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
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


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
  - title: "Generate a Dixa API token"
    anchor: "generate-api-token"
    content: |
      1. Log into your {{ integration.display_name }} account.
      2. Go to  **Settings** page.
      3. Scroll to the **Manage** section and then click **Integrations".
      4. In the **API Tokens** card, click **Configure API tokens**.
      5. Click **Add API Token**.
      6. Give the API token a name, like `Stitch Integration`, to make it easy to find in your list of tokens. Choose **Dixa API** as the API version. Click **Add API Token**.
      7. Copy the API token, and have it readily available for the next step.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **API Token** field, paste the API token you copied from [step 1](#retrieve-api-token).

  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}

  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

## remove this if the integration doesn't support at least table selection
  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %} 


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/dixa


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}