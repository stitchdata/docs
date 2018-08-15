---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: DoubleClick Campaign Manager
permalink: /integrations/saas/doubleclick-campaign-manager
tags: [saas_integrations]
keywords: doubleclick campaign manager, integration, schema, etl doubleclick campaign manager, doubleclick campaign manageretl, doubleclick campaign manager schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "doubleclick-campaign-manager"
display_name: "DoubleClick Campaign Manager"

singer: true 
tap-name: "doubleclick-campaign-manager"
repo-url: https://github.com/singer-io/tap-doubleclick-campaign-manager

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: "https://ads.google.com/status#hl=en&v=status"

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true
column-selection: false

# attribution-window: "# days"
# attribution-is-configurable: 

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
# Each table has a its own .md file in /_integration-schemas/doubleclick-campaign-manager

# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |

---
{% assign integration = page %}
{% include misc/data-files.html %}