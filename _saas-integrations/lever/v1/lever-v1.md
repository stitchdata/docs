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

title: Lever (v1)
permalink: /integrations/saas/lever
keywords: lever, integration, schema, etl lever, lever etl, lever schema
layout: singer
# input: false

key: "lever-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "lever"
display_name: "Lever"

singer: true
status-url: "https://status.lever.co/"

tap-name: "Lever"
repo-url: https://github.com/singer-io/tap-lever

this-version: "1"

api: |
  [Lever API (v1)](https://hire.lever.co/developer/documentation){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

api-type: "platform.lever"

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

requirements-list:
  - item: |
      **Super Admin** privileges. Your role in {{ integration.display_name }} must be Super Admin in order to obtain an API Key.

setup-steps:
  - title: "Obtain your API token"
    anchor: "obtain-api-token"
    content: |
      1. Login to your {{ integration.display_name }} account.
      2. Hover over your account icon in the upper right corner of the page and click on **SETTINGS**.
      3. On the settings page, click on **API Credentials**
      4. On the API Credentials page, locate the **Generate New Key** link in the {{ integration.display_name }} API credentials section.
      5. If you would like your key to access confidential information, click on the **Allow access to confidential data** toggle. If not, skip to the next step.
      6. Click **DONE**.
      
      Keep your API key readily available for the next step.

      {% include note.html type="single-line" content="**Note**: Once you save your API key, you cannot change its access settings. You'll need to generate a new API key to change access settings." %}

  - title: "add integration"
    content: |
      4. In the **Token** field, paste the API Key you obtained in [Step 1](#obtain-api-token).
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/lever/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}
