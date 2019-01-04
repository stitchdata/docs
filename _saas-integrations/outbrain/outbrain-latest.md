---
title: Outbrain (v1.0)
permalink: /integrations/saas/outbrain
tags: [saas_integrations]
keywords: outbrain, integration, schema, etl outbrain, outbrain etl, outbrain schema
summary: "Connection instructions and schema details for Stitch's Outbrain integration."
layout: singer

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "outbrain"
display_name: "Outbrain"
singer: true
author: "Fishtown Analytics"
author-url: http://fishtownanalytics.com/
repo-url: https://github.com/singer-io/tap-outbrain

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: 
icon: /images/integrations/icons/outbrain.svg

table-selection: false
column-selection: false

anchor-scheduling: true
extraction-logs: true
loading-reports: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "add integration"
    content: |
      4. In the **Account ID** field, enter your Outbrain Account (or Marketer) ID. 

         You can find this by looking at the URL when you're logged into your Outbrain account. The Account ID looks something like this: `0f4b02153ee75f3c9dc4fc128ab041962` and is located between `marketers` and `campaigns`, if you're looking at the Overview dashboard:

         `https://my.outbrain.com/amplify/site/marketers/[account-id-will-be-here]/campaigns/overview`

      5. In the **Username** field, enter your Outbrain username.
      6. In the **Password** field, enter your Outbrain password.

  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#        Table Schemas       #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/outbrain

---
{% assign integration = page %}
{% include misc/data-files.html %}