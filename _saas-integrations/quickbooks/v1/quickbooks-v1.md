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

title: Quickbooks (v1)
permalink: /integrations/saas/quickbooks
keywords: quickbooks, integration, schema, etl quickbooks, quickbooks etl, quickbooks schema
layout: singer
# input: false

key: "quickbooks-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "quickbooks"
display_name: "Quickbooks"

singer: true
status-url: ""

tap-name: "Quickbooks" ## Ex: Intercom, not intercom
repo-url: https://github.com/singer-io/tap-quickbooks

this-version: "1"

api: |
  [](){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: ""

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
  - item: ""
  - item: ""

requirements-info:

setup-steps:
  - title: ""
    anchor: ""
    content: |
      [Add content]
  - title: "add integration"
    # content: |
      # starting with 4., add instructions for additional fields in UI. EX:
      # 4. In the [FIELD_NAME] field, [instructions]
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data" ## remove this if the integration doesn't support at least table selection


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/quickbooks/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}