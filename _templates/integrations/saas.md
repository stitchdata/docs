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

title: SAAS-INTEGRATION ## Find/replace SAAS-INTEGRATION with the display name (ex: Intercom)
permalink: /integrations/saas/saas-integration ## Find/replace saas-integration with the key name (ex: intercom)
tags: [saas_integrations]
keywords: saas-integration, integration, schema, etl saas-integration, saas-integration etl, saas-integration schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "saas-integration"
display_name: "SAAS-INTEGRATION"

singer: true 
tap-name: ""
repo-url: https://github.com/singer-io/tap-saas-integration

# this-version: ""

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Closed Beta/Open Beta/Released/Deprecated"
certified: true 

historical: "1 year"
frequency: "30 minutes"
tier: "Free/Paid"
status-url: ""
icon: /images/integrations/icons/saas-integration.svg

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true/false
column-selection: true/false

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
# Each table has a its own .md file in /_integration-schemas/saas-integration

# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |

---
{% assign integration = page %}
{% include misc/data-files.html %}