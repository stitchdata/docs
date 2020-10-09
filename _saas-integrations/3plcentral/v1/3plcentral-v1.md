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

title: 3PL Central (v1)
permalink: /integrations/saas/3plcentral
keywords: 3plcentral, integration, schema, etl 3plcentral, 3plcentral etl, 3plcentral schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "3plcentral"
display_name: "3PL Central"

singer: true 
tap-name: "3PL Central"
repo-url: https://github.com/singer-io/tap-3plcentral

this-version: "1"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

historical: "1 year"
frequency: "1 hour"
tier: "Standard"
status-url: ""

api-type: "platform.3plcentral"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "Request API credentials from {{ integration.display_name }}"
    anchor: "request-api"
    content: |
      1. Log into your {{ integration.display_name }} account and request the following information from your account manager:
      - **Base URL**: The API URL to which endpoints are appended.
      - **Client ID**: Your secure OAuth 2.0 identifier.
      - **Client Secret**: Your secure OAuth 2.0 secret key.
      - **Customer ID**: The integer ID number for your customer organization.
      - **Facility ID**: The integer ID number for your warehouse facility.
      - **TPL Key**: Your warehouse-specific {{ integration.display_name }} key.
      - **User Login**: The interger ID number for your user account.
      
      2. Keep this information available so you can add the integration in the next step.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. Enter the information you requested from [Step 1](#request-api) into the corresponding fields in Stitch.
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
# Each table has a its own .md file in /_integration-schemas/3plcentral
---
{% assign integration = page %}
{% include misc/data-files.html %}