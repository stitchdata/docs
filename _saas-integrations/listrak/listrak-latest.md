---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Listrak
permalink: /integrations/saas/listrak
tags: [saas_integrations]
keywords: listrak, integration, schema, etl listrak, listrak etl, listrak schema
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "listrak"
display_name: "Listrak"
singer: true 
repo-url: https://github.com/singer-io/tap-listrak

# this-version: ""

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: 
icon: /images/integrations/icons/listrak.svg
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
    content: |
      4. In the **Username** field, enter 
      5. In the **Password** field, enter the {{ integration.display_name }} user's password.
  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/listrak

# replication-sections:
#   - name: ""
#     anchor: ""
#     content: |

---
{% assign integration = page %}
{% include misc/data-files.html %}

