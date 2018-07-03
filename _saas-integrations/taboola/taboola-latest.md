---
title: Taboola
permalink: /integrations/saas/taboola
tags: [saas_integrations]
keywords: taboola, taboola integration, schema, etl taboola, taboola etl, taboola schema
summary: "Connection instructions and schema details for Stitch's Taboola integration."
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "taboola"
display_name: "Taboola"
singer: true 
author: "Fishtown Analytics"
author-url: http://fishtownanalytics.com/
repo-url: https://github.com/singer-io/tap-taboola
status-url: https://twitter.com/taboola?lang=en

# this-version:

# -------------------------- #
#     Integration Details    #
# -------------------------- #

status: "Released"
certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
icon: /images/integrations/icons/taboola.svg

## Features in Stitch
whitelist:
  tables: false
  columns: false
anchor-scheduling: true
cron-scheduling: true
extraction-logs: true
loading-reports: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: "**Access to the Taboola API**."
  - item: |
      **The following API credentials:**

      - Taboola Account ID
      - Client ID
      - Client Secret

requirements-info: "Reach out to your Taboola Account Manager for assistance. Once you receive this information, you can continue with the setup."

setup-steps:
  - title: "add integration"
    content: |
      4. In the **Username** field, enter your Taboola username. This user must have access to the Taboola API.
      5. In the **Password** field, enter your Taboola password.
      6. In the **Account ID** field, enter your Taboola account ID.
      7. In the **Client ID** field, enter your Taboola client ID.
      8. In the **Client Secret** field, enter your Taboola client secret.
  - title: "historical sync"
  - title: "replication frequency"

---
{% assign integration = page %}
{% include misc/data-files.html %}