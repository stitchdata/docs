---
title: Taboola (v1)
permalink: /integrations/saas/taboola
keywords: taboola, taboola integration, schema, etl taboola, taboola etl, taboola schema
summary: "Connection instructions and schema details for Stitch's Taboola integration."
layout: singer

key: "taboola-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "taboola"
display_name: "Taboola"

singer: true
repo-url: https://github.com/singer-io/tap-taboola
status-url: https://twitter.com/taboola?lang=en

this-version: "1"

api: |
  [{{ integration.display_name }} Backstage API](https://github.com/taboola/Backstage-API){:target="new"}

# -------------------------- #
#     Integration Details    #
# -------------------------- #

certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Standard"

api-type: "platform.taboola"

anchor-scheduling: true
cron-scheduling: true

table-selection: false
column-selection: false
select-all: false
select-all-reason: |
  As this integration doesn't support table or column selection, all available tables and columns are automatically replicated.

extraction-logs: true
loading-reports: true

# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: "**Access to the {{ integration.display_name }} API**."
  - item: |
      **The following API credentials:**

      - Taboola Account ID
      - Client ID
      - Client Secret

requirements-info: "Reach out to your {{ integration.display_name }} Account Manager for assistance. Once you receive this information, you can continue with the setup."

setup-steps:
  - title: "add integration"
    content: |
      4. In the **Username** field, enter your {{ integration.display_name }} username. This user must have access to the {{ integration.display_name }} API.
      5. In the **Password** field, enter your {{ integration.display_name }} password.
      6. In the **Account ID** field, enter your {{ integration.display_name }} account ID.
      7. In the **Client ID** field, enter your {{ integration.display_name }} client ID.
      8. In the **Client Secret** field, enter your {{ integration.display_name }} client secret.
  - title: "historical sync"
  - title: "replication frequency"
---
{% assign integration = page %}
{% include misc/data-files.html %}