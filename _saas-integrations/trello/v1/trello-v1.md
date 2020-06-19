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

title: Trello
permalink: /integrations/saas/trello
keywords: trello, integration, schema, etl trello, trello etl, trello schema
layout: singer
# input: false

key: "trello-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "trello"
display_name: "Trello"

singer: true
status-url: "https://trello.status.atlassian.com/"

tap-name: "Trello"
repo-url: https://github.com/singer-io/tap-trello

this-version: "1"

api: |
  [Trello REST API](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

api-type: "platform.trello"

historical: "1 year"
frequency: "1 hour"
tier: "Free"

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

requirements-info: |
  The {{ integration.display_name }} integration only requires your {{ integration.display_name }} login to connect to Stitch. This is done through OAuth authentication.

setup-steps:
  - title: "add integration"
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data" ## remove this if the integration doesn't support at least table selection


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/trello


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}