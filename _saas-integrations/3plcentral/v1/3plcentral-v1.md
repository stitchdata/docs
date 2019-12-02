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

title: 3PL Central
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
tap-name: ""
repo-url: https://github.com/singer-io/tap-3plcentral

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Open Beta"
certified: true 

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: ""

anchor-scheduling: true
cron-scheduling: false

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: false

# attribution-window: "# days"
# attribution-is-configurable: 

# setup-name: ""

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
  - item: "**Base Url**. API URL to which /endpoints are appended. Example: 'http://secure-wms.com' "
  - item: "**Client ID**. A secure OAuth 2.0 identifier for each application/client."
  - item: "**Client Secret**. A secure OAuth 2.0 secret key for application/client authentication."
  - item: "**Customer ID**. Integer ID number for the customer organization."
  - item: "**Facility ID**. Integer ID number for the warehouse facility."
  - item: "**TPL Key**. A warehouse-specific 3PL key."
  - item: "**User Login**. Interger ID number for the user."

requirements-info:

setup-steps:
  - title: "Gather Requirements"
    anchor: "gather-requirements"
    content: |
      Log into your 3PL Central account and contact your account manager to collect the information needed from the requirements list.
  - title: "add integration"
    # content: |
      # starting with 4., add instructions for additional fields in UI
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/3plcentral


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}