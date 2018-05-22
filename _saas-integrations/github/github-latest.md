---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Github ## Find/replace SAAS-INTEGRATION with the display name (ex: Intercom)
permalink: /integrations/saas/github ## Find/replace saas-integration with the key name (ex: intercom)
tags: [saas_integrations]
keywords: github, integration, schema, etl github, github etl, github schema
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "github"
display_name: "Github"
singer: true
author: "Stitch"
author-url:
repo-url: https://github.com/singer-io/tap-github


# If there's more than 1 version available:
#   1. Uncomment the line below,
#   2. Create a version file in _data/taps/versions for the integration, using the template in the folder.

# this-version: ""

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: ""
certified: true # Stitch-supported integration

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url:
icon: /images/integrations/icons/github.svg
whitelist:
  tables: true
  columns: false


# -------------------------- #
#        API Details         #
# -------------------------- #

## Info about the integration's API that may affect either the speed of
## replication or the ability to replicate data at all.

## For example: Salesforce enforces a daily quota - once it's reached,
## Stitch is unable to replicate data until more quota is available.

## Details about the limitations go in the replication-notes content block.

enforces-api-limits: true/false


## If Stitch queries for X days each time due to attribution windows, enter the
## # of days here
## If it's the past day or 1 day, use "day"

attribution-window: "# days"

# -------------------------- #
#      Incompatiblities      #
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

schema-sections:
  - title: ""
    anchor: ""
    content: |

---
{% assign integration = page %}
{% include misc/data-files.html %}
