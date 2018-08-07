---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Yotpo
permalink: /integrations/saas/yotpo
tags: [saas_integrations]
keywords: yotpo, integration, schema, etl yotpo, yotpo etl, yotpo schema
layout: singer
input: true

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "yotpo"
display_name: "Yotpo"

singer: true
tap-name: "Yotpo"
repo-url: https://github.com/singer-io/tap-yotpo

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: "http://status.yotpo.com/"
icon: /images/integrations/icons/yotpo.svg

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: 
column-selection: 

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
# Each table has a its own .md file in /_integration-schemas/yotpo

# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |

---
{% assign integration = page %}
{% include misc/data-files.html %}

