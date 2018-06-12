---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: AppsFlyer
permalink: /integrations/saas/appsflyer
tags: [saas_integrations]
keywords: appsflyer, integration, schema, etl appsflyer, appsflyer etl, appsflyer schema
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "appsflyer"
display_name: "AppsFlyer"
repo-url: https://github.com/singer-io/tap-appsflyer

# this-version: ""

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: http://status.appsflyer.com/
icon: /images/integrations/icons/appsflyer.svg
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
      4. In the **App ID** field, enter 
      5. In the **API Token** field, 
  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/appsflyer
---
{% assign integration = page %}
{% include misc/data-files.html %}