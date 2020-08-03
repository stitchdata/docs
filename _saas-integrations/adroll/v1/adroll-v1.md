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

title: AdRoll (v1)
permalink: /integrations/saas/adroll
keywords: adroll, integration, schema, etl adroll, adroll etl, adroll schema
layout: singer
# input: false

key: "adroll-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "adroll"
display_name: "AdRoll"

singer: true
status-url: "https://status.adroll.com/"

tap-name: "AdRoll"
repo-url: https://github.com/singer-io/tap-adroll

this-version: "1"

api: |
  [NextRoll CRUD API](https://developers.nextroll.com/docs/crud-api/index.html){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

api-type: "platform.adroll"

historical: "1 year"
frequency: "1 hour"
tier: "Free"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "add integration"
  - title: "historical sync"
  - title: "replication frequency"
  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "grant-stitch-authorization"
    content: |
      1. In Stitch, click the **Authorize** button. You'll be prompted to sign into your {{ integration.display_name }} account.
      2. A screen explaining what you're authorizing will display. **Note**: Stitch will only ever read your {{ integration.display_name }} data, and cannot create or modify records in {{ integration.display_name }}.
      3. Click **Sign in with {{ integration.display_name }}** to sign into your {{ integration.display_name }} account.
      4. After the authorization process successfully completes, you'll be directed back to Stitch.
      5. Click {{ app.buttons.finish-int-setup }}.
  - title: "track data"


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/adroll/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}