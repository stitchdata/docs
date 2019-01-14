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

title: Toggl (v1.0)
permalink: /integrations/saas/toggl
tags: [saas_integrations]
keywords: toggl, integration, schema, etl toggl, toggl etl, toggl schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "toggl"
display_name: "Toggl"

singer: true 
tap-name: "Toggl"
repo-url: https://github.com/singer-io/tap-toggl

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Open Beta"
certified: false 

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
#status-url: "" # None available

# TODO: Add toggl.svg
icon: /images/integrations/icons/singer.svg

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

# attribution-window: "# days"
# attribution-is-configurable: 

# setup-name: ""

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |

setup-steps:
  - title: ""
    anchor: ""
    content: |

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/toggl
---
{% assign integration = page %}
{% include misc/data-files.html %}
