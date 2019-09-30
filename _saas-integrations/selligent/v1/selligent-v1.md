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

title: Selligent
permalink: /integrations/saas/selligent
keywords: selligent, integration, schema, etl selligent, selligent etl, selligent schema
layout: singer
# input: true

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "selligent"
display_name: "Selligent"

singer: true 
tap-name: "Selligent"
repo-url: https://github.com/singer-io/tap-selligent

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false 

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: ""

anchor-scheduling: true
cron-scheduling: false

extraction-logs: true
loading-reports: true

table-selection: false
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
  - item: "**Personal {{ integration.display_name }} API Key**. This is required to connect {{ integration.display_name }} to Stitch."

requirements-info:

setup-steps:
  - title: "Obtain {{ integration.display_name }} API Key"
    anchor: "API-Key"
    content: |
      Contact your Selligent account manager to obtain the API key for your organization.
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
# Each table has a its own .md file in /_integration-schemas/selligent


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}
