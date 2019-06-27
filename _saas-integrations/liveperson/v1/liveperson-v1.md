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

title: LivePerson
permalink: /integrations/saas/liveperson
tags: [saas_integrations]
keywords: liveperson, integration, schema, etl liveperson, liveperson etl, liveperson schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "liveperson"
display_name: "LivePerson"

singer: true 
tap-name: ""
repo-url: https://github.com/singer-io/tap-liveperson

# this-version: ""

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Open Beta"
certified: false

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: ""
icon: /images/integrations/icons/liveperson.svg

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

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
      # starting with 4., add instructions for additional fields in UI
  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/liveperson

# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |

---
{% assign integration = page %}
{% include misc/data-files.html %}
