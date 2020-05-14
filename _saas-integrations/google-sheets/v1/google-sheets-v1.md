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

key: "google-sheets-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "google-sheets"
display_name: "Google Sheets"

singer: true
status-url: "https://www.google.com/appsstatus#hl=en&v=status"

tap-name: "Google Sheets"
repo-url: https://github.com/singer-io/tap-google-sheets

this-version: "1"

api: |
  [Google Sheets v4 AP1](https://developers.google.com/sheets/api){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

api-type: "platform.google-sheets"

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

  Stitch's {{ integration.display_name }} integration will generate tables containing data related to metadata and the individual sheets within a spreadsheet.

  **Note**: There are a few limitations:

  - Currently, the {{ integration.display_name }} integration replicates one spreadsheet at a time. To replicate another spreadsheet, you will need to create another {{ integration.display_name }} integration in Stitch.
  - The `IMPORTRANGE()` function in {{ integration.display_name }} isn't currently supported. This integration identifies new and updated data using a spreadsheet's last `updated_at` value, which the `IMPORTRANGE()` doesn't update when used.
  - Spreadsheets from shared **Team Drives** aren't currently supported. Permission errors will surface during extraction if you connect a spreadsheet from a Team Drive.


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
      **One header row** in your worksheets. If there are multiple headers that are not in the first row, your worksheet data may not be replicated correctly. Headers that aren't in the first row may be extracted as column data.
      
setup-steps:
  - title: "Obtain your spreadsheet ID"
    anchor: "obtain-spreadsheet-id"
    content: |
      1. Go to [{{ integration.display_name }}](http://sheets.google.com){:target="new"} and log into the Google account associated with the spreadsheet you are looking to integrate.
      2. Open the spreadsheet that you want to use in the integration.
      3. Your Spreadsheet ID is within the URL to the webpage. In the image below, the portion of the URL within the blue box is the Spreadsheet ID. Keep this readily available to continue with the integration.
      {% include layout/image.html file="/integrations/google-sheets-spreadsheet-id.png" alt="Google Sheets URL containing the Spreadsheet ID." enlarge=true max-width="850" %}
  - title: "add integration"
    content: |
      4. In the **Spreadsheet ID** field, enter your Spreadsheet ID you obtained from the [previous step](#obtain-spreadsheet-id). **Note**: To integrate another spreadsheet, you'll need to repeat these steps over again with another {{ integration.display_name }} integration.
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"


# -------------------------- #
#     Replication Details    #
# -------------------------- #

replication-sections:  
  - title: "Spreadsheet Setup"
    anchor: "spreadsheet-setup"
    content: |
      For proper table replication in Stitch's {{ integration.display_name }} integration, all of your sheets must have column headers in the first row. Row two is where your data should begin.

  - title: "Replication Outputs for your Individual Sheets"
    anchor: "replication-outputs"
    content: |
      Stitch's {{ integration.display_name }} integration will output tables containing metadata about your spreadsheet, as well as replications of your individual sheets. For each sheet, the integration will output the schema of its resources, based on the column headers and datatypes in row two. It will also output a record for all columns that have columns headers and for each row of data.

      The primary key in each row of a sheet is the row number. The field for the primary key is `__sdc_row`. The foreign keys included in the sheet are connected to the **Spreadsheet Metadata**, `__sdc_spreadsheet_id`, and the **Sheet Metadata**, `__sdc_sheet_id`.

  - title: "Empty Worksheets"
    anchor: "empty-worksheets"
    content: |
      In discovery and sync mode of your Stitch {{ integration.display_name }} integration, Stitch will check the worksheets' header and first data row (the second row) for data. If there is no data in either of those rows, Stitch will skip that worksheet for replication.




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
