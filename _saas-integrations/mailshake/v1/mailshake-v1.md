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

title: Mailshake (v1)
permalink: /integrations/saas/mailshake
keywords: mailshake, integration, schema, etl mailshake, mailshake etl, mailshake schema
layout: singer
# input: false

key: "mailshake-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "mailshake"
display_name: "Mailshake"

singer: true
status-url: ""

tap-name: "Mailshake"
repo-url: https://github.com/singer-io/tap-mailshake

this-version: "1"


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.mailshake"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

# Row usage details

row-usage-hog: false
row-usage-hog-reasons:
  data-structure: false
  data-volume: false
  lots-of-full-table: false


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "Retrieve your {{ integration.display_name }} API key"
    anchor: "retrieve-api-key"
    content: |
      1. Sign into your {{ integration.display_name }} account.
      2. Click **Extensions > API**.
      3. If your account already has an API key, it will display in the **Your Access** section of the page.

         Otherwise, click the **Create API Key** button. Your API key will display on the page.

      Keep this page open - you'll need it to complete the next step.
  - title: "add integration"
    content: |
      4. In the **API Key** field, paste the {{ integration.display_name }} API key you retrieved in [Step 1](#retrieve-api-key).
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/helpscout/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}