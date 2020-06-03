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
tier: "Free"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

## Row usage details

row-usage-hog: true
row-usage-hog-reasons:
  data-structure: true
  data-volume: true
  lots-of-full-table: false

# attribution-window: "# days"
# attribution-is-configurable: 

# setup-name: ""


# -------------------------- #
#      Querying Details      #
# -------------------------- #

## Pepperjam's attribution windows. Stitch queries for
## this number of days during each replication job to
## account for any updates to existing records made during
## this time.

replication-notes: true
attribution-window: "30 days"
attribution-is-configurable: false


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
      1. Login to you {{ integration.display_name }} account.
      2. Hover over the **Developer Kit** menu and then click **API Keys**.
      3. Click **Generate New Key**.
      4. Keep note of your API Key - you will need it to complete the next step.
  - title: "add integration"
    content: |
      4. In the **API Key** field, paste the API key you obtained in [step 1](#obtain-api-key).
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data" ## remove this if the integration doesn't support at least table selection


# -------------------------- #
#      Replication Info      #
# -------------------------- #

replication-sections:
  - title: "Attribution windows and data extraction"
    anchor: "attribution-windows-data-extraction"
    content: |
      Stitch replicates data in this way to account for updates made to existing records within an attribution window, thus ensuring you won’t make decisions based on stale (or false) data. As a result, you may see a higher number of replicated rows than what’s being generated in Pepperjam.

      Setting the Replication Frequency to a higher frequency - like 30 minutes - can result in re-replicating recent data and contribute to greater row usage. Replicating fewer tables or selecting a lower frequency can help keep your row count low.

      In the sections below are examples of how attribution windows impact how Stitch extracts data during historical and ongoing replication jobs.

      {% include integrations/saas/ads-append-only-replication.html type="report-tables" %}

  - title: "Pepperjam tables with attribution windows"
    anchor: "tables-with-attribution"
    content: |
      Below is the list of tables in this integration with attribution windows:
      {% assign all-tables = site.integration-schemas | where:"tap","pepperjam" %}
      {% assign tables-with-attribution = all-tables | where:"attribution-window",true %}

      {% for table in tables-with-attribution %}
      - {{ table.name }} - {{ table.attribution-window-days }} days
      {% endfor %}

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