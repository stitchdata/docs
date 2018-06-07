---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Bronto
permalink: /integrations/saas/bronto
tags: [saas_integrations]
keywords: bronto, integration, schema, etl bronto, bronto etl, bronto schema
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "bronto"
display_name: "Bronto"
singer: true 
author: "Stitch"
author-url: https://www.stitchdata.com
repo-url: https://github.com/singer-io/tap-bronto

# this-version: ""

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false # Stitch-supported integration

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: 
icon: /images/integrations/icons/bronto.svg
whitelist:
  tables: true
  columns: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **A valid and active API token with Read permissions**

# From Bronto's docs (though this doesn't all seem super relevant):
# http://dev.bronto.com/gettingstarted/soap-how-to-get-started/how-to-access-the-api/
# Account must have the API feature enabled
# Must have at least one API token created
#    - Create API tokens from an administrator account, and specify access on them
# What permissions? Access Type: Read is all we need
# Click "Add Access Token" and type in a name
# Under Permissions & Settings, Select "Read", and ensure that "Token is active?" is checked

# If you have Professional or Core edition account, go to Home->Settings->Data Exchange in the Bronto application

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

