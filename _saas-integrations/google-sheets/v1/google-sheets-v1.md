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

title: Google Sheets
permalink: /integrations/saas/google-sheets
keywords: google-sheeets, integration, schema, etl google-sheeets, google-sheeets etl, google-sheeets schema
layout: singer
# input: false

key: "google-sheeets-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "google-sheeets"
display_name: "Google Sheets"

singer: true
status-url: "https://www.google.com/appsstatus#hl=en&v=status"

tap-name: "google-sheets"
repo-url: https://github.com/singer-io/tap-google-sheeets

this-version: "1.0"

api: |
  [Google Sheets v4 AP1](https://developers.google.com/sheets/api){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

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

  Stitch's {{ integration.display_name }} integration will generate tables containing data related to metadata and the individual sheets within a spreadsheet. Currently, the Stitch {{ integration.display_name }} integration replicates one spreadsheet at a time. To replicate another spreadsheet, you will need to create another {{ integration.display_name }} integration.


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
  - title: "Obtain your Spreadsheet ID"
    anchor: "obtain-spreadsheet-id"
    content: |
      1. Go to [{{ integration.display_name }}](http://sheets.google.com){:target="new"} and log into the Google account associated with the spreadsheet you are looking to integrate.
      2. Open the spreadsheet that you want to use in the integration.
      3. Your Spreadsheet ID is within the URL to the webpage. In the image below, the portion of the URL within the blue box is the Spreadsheet ID. Keep this readily available to continue with the integration.
      {% include layout/image.html file="/integrations/google-sheets-spreadsheet-id.png" alt="Google Sheets URL containing the Spreadsheet ID." enlarge=true max-width="850" %}
  - title: "add integration"
    content: |
      4. In the `Spreadsheet ID` field, enter your Spreadsheet ID you obtained from the [previous step](#obtain-spreadsheet-id). Please note that to integrate another spreadsheet, you'll need to repeat these steps over again with another {{ integration.display_name }} integration.
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"


# -------------------------- #
#     Replication Details    #
# -------------------------- #

  - title: Spreadsheet Setup
    anchor: "spreadsheet-setup"
    content: |
      For proper table replication in Stitch's {{ integration.display_name }} integration, all of your sheets must have column headers in the first row. Starting from row two is where your data should begin.


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/google-sheeets


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}