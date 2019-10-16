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

title: Mambu
permalink: /integrations/saas/mambu
keywords: mambu, integration, schema, etl mambu, mambu etl, mambu schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "mambu"
display_name: "Mambu"

singer: true 
tap-name: "mambu"
repo-url: https://github.com/singer-io/tap-mambu

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Open Beta"
certified: false 

historical: "1 year"
frequency: "one hour"
tier: "Free"
status-url: "https://status.mambu.com/"

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
  - item: "**API Access Enabled Account**. The {{ integration.display_name }} integration requires an account login with API Access. In {{ integration.display_name }}'s system API access can be granted to any existing user. Although, {{ integration.display_name }} suggests a new user be created just for APIs."
  - item: "**Subdomain**. This is required to link the {{ integration.display_name }} client account to Stitch."

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
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/mambu


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}