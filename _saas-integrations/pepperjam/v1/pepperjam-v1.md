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

title: Pepperjam
permalink: /integrations/saas/pepperjam
keywords: pepperjam, integration, schema, etl pepperjam, pepperjam etl, pepperjam schema
layout: singer
# input: false

key: "pepperjam-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "pepperjam"
display_name: "Pepperjam"

singer: true
status-url: ""

tap-name: "Pepperjam"
repo-url: https://github.com/singer-io/tap-pepperjam

this-version: "1"

api: |
  [{{ integration.display_name }} Advertiser API v20120402](https://support.pepperjam.com/s/advertiser-api-documentation){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false 

api-type: "platform.pepperjam"

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

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

setup-steps:
  - title: "Obtain your API key"
    anchor: "obtain-api-key"
    content: |
      1. Login to your {{ integration.display_name }} account.
      2. Hover over the **Developer Kit** menu and then click **API Keys**.
      3. Click **Generate New Key**.
      4. Keep note of your API Key - you will need it to complete the next step.
  - title: "add integration"
    content: |
      4. In the **API Key** field, enter the API key you obtained in [step 1](#obtain-api-key).
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data" ## remove this if the integration doesn't support at least table selection


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/pepperjam


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}
