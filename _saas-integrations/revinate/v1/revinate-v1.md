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

title: Revinate
permalink: /integrations/saas/revinate
keywords: revinate, integration, schema, etl revinate, revinate etl, revinate schema
summary: "Connection instructions, replication info, and schema details for Stitch's Revinate integration."
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "revinate"
display_name: "Revinate"

singer: true 
tap-name: "Revinate"
repo-url: https://github.com/singer-io/tap-revinate

this-version: "1.0"

api: |
  [{{ integration.display_name }} Porter API](https://porter.revinate.com/documentation){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false 

historical: "1 year"
frequency: "1 hour"
tier: "Free"

anchor-scheduling: true
cron-scheduling: false

extraction-logs: true
loading-reports: true

table-selection: false
column-selection: false

attribution-window: "1 week"

# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **A {{ integration.display_name }} account with API access.** Reach out to your {{ integration.display_name }} sales representative or account manager to obtain the correct permissions.
  - item: |
      **A {{ integration.display_name }} API token and secret**. To obtain these credentials, reach out to your {{ integration.display_name }} sales representative or account manager.

setup-steps:
  - title: "add integration"
    content: |
      4. In the **Username** field, enter your {{ integration.display_name }} username.
      5. In the **API Key** field, paste your {{ integration.display_name }} API key. Your {{ integration.display_name }} API token must be obtained through [your {{ integration.display_name }} sales representative or account manager](#setup-requirements).
      6. In the **API Secret** field, paste your {{ integration.display_name }} API secret. Your {{ integration.display_name }} API secret must be obtained through [your {{ integration.display_name }} sales representative or account manager](#setup-requirements).
  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#      Replication Info      #
# -------------------------- #

replication-sections:
  - title: "Extraction overview"
    anchor: "extraction-overview"
    content: |
      When Stitch runs a replication job for {{ integration.display_name }}, a few things will happen:

      1. First, Stitch will get all the hotels that the [authenticating user](#add-stitch-data-source) has access to.
      2. Stitch will [replicate review snapshot data](#replicate-review-snapshots) (`hotel_reviews_snapshot`, `hotel_reviews_snapshot_by_site`, `hotel_reviews_snapshot_by_time`) for the hotel.
      3. Stitch will replicate data about the hotel (`hotels`).
      3. Stitch will repeat steps 2-3 until review snapshot and hotel data has been replicated for all accessible hotels.
      4. Stitch will replicate review data (`reviews`) based on the last saved `updated_at` value, which is the table's Replication Key.

  - title: "Replicating review snapshots"
    anchor: "replicate-review-snapshots"
    content: |
      When Stitch extracts review snapshot data, it will do so using an **Attribution Window** of **{{ integration.attribution-window }}**. This means that during each replication job, Stitch will replicate snapshot data for that last completed week. For example: If the integration is scheduled to run every 30 minutes, then snapshot data for the last week will be replicated every 30 minutes.

      This is applicable to the `hotel_reviews_snapshot`, `hotel_reviews_snapshot_by_site`, and `hotel_reviews_snapshot_by_time` tables.

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/revinate
---
{% assign integration = page %}
{% include misc/data-files.html %}