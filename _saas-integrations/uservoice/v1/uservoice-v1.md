---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: UserVoice (v1.0)
permalink: /integrations/saas/uservoice
tags: [saas_integrations]
keywords: uservoice, integration, schema, etl uservoice, uservoice etl, uservoice schema
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "uservoice"
display_name: "UserVoice"
singer: true 
repo-url: https://github.com/singer-io/tap-uservoice

# this-version: ""

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "In Development"
certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: 
whitelist:
  tables: true
  columns: false

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
# Each table has a its own .md file in /_integration-schemas/uservoice

schema-sections:
  - title: ""
    anchor: ""
    content: |

---
{% assign integration = page %}
{% include misc/data-files.html %}