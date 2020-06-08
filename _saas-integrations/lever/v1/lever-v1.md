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

title: Lever
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
  [Lever v1](https://hire.lever.co/developer/documentation){:target="new"}


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

# attribution-window: "# days"
# attribution-is-configurable: 

# setup-name: ""


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Incompatibilities     #
# -------------------------- #

## uncomment section below if integration is compatible with any Stitch destinations
## if incompatible with multiple destinations, create a section for each destination

## incompatible:
  ## [redshift]: "always,sometimes,never"
  ## reason: "copy" 

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Super Admin** privileges. Your role in {{ integration.display_name }} needs to be Super Admin in order to obtain an API Key.

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
      7. Keep your API key readily available for the next step.

      {% note.html type="single-line" content="**Note**: Once you save your API key, you cannot change it's access settings. To update access setting, you must generate a new API key." %}

  - title: "add integration"
    content: |
      4. In the **Token** field, paste the API Key you obtained in [step 1](#obtain-api-token).
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data" ## remove this if the integration doesn't support at least table selection


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/lever


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}