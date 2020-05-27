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
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **A header row with unique column values in the first row of every sheet you want to replicate.** If there are multiple headers not in the first row, your worksheet data may not be replicated correctly. Headers that aren't in the first row may be extracted as column data.
  - item: |
      **A full row of data in the second row of every sheet you want to replicate.** Data must begin in the second row of the sheet. Values in this row may not be `NULL` or [issues will arise during Extraction](#discovery--objects).
      
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
  - content: |
      In this section:

      {% for section in page.replication-sections %}
      {% if section.title %}
      - [{{ section.summary | flatify }}](#{{ section.anchor }})
      {% endif %}
      {% endfor %}

  - title: "Extraction"
    anchor: "extraction-details"
    summary: "Details about Extraction, including object discovery and selecting data for replication"
    content: |
      For every table set to replicate, Stitch will perform the following during Extraction:

      {% for subsection in section.subsections %}
      - [{{ subsection.summary | flatify }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Discovery"
        anchor: "extraction--discovery"
        summary: "Discover table schemas and type discovered columns"
        content: |
          During Discovery, Stitch will:

          {% for sub-subsection in subsection.sub-subsections %}
          - [{{ sub-subsection.summary | flatify }}](#{{ sub-subsection.anchor }})
          {% endfor %}
        sub-subsections:
          - title: "Determining table schemas"
            anchor: "discovery--objects"
            summary: "Determine table schemas"
            content: |
              At the start of each replication job, Stitch will check the sheets's header row and first data row (the second row in the sheet) for data.

              To be detected and properly replicated, every sheet set to replicate must have:

              1. Column headers with unique values in the first row. If there are duplicate column names, Stitch will skip the sheet and surface a [duplicate column name error]({{ link.troubleshooting.google-sheets-extraction-errors | prepend: site.baseurl }}#duplicate-column-names).

                 For example: Two columns in the header row can't be named `customer_id`. Uniqueness must not rely on case. While `customer_id` and `Customer_ID` may be unique due to case differences, this may still cause errors during extraction and loading. For this reason, column names must be completely unique.
              2. A full row of data in the second row. If any column in this row contains a `NULL` value, Stitch will skip the sheet and surface a [malformed sheet message during extraction]({{ link.troubleshooting.google-sheets-extraction-errors | prepend: site.baseurl }}#malformed-sheet).

              If the sheet doesn't contain a header row and a second row of data, Stitch will skip the sheet and surface an [empty sheet message during extraction]({{ link.troubleshooting.google-sheets-extraction-errors | prepend: site.baseurl }}#empty-sheet).

      - title: "Data replication"
        anchor: "extraction--data-replication"
        summary: "Select records (files) for replication"
        content: |
          After discovery is completed, Stitch will move onto extracting data from the sheets set to replicate.

          {% assign file-name = "spreadsheet" %}
          {% assign file-note = "This includes all sheets in the spreadsheet that are set to replicate, regardless of whether they have been modified." %}

          {% include replication/extraction/file-modification-replication-keys.html %}

          To reduce row usage, consider [scheduling the integration to replicate less frequently](#define-rep-frequency).

  - title: "Loading"
    anchor: "loading-details"
    summary: "Details about how data replicated from {{ integration.display_name }} is loaded into a destination"
    content: |
      For every sheet you set to replicate, Stitch will create a table in your destination. These tables will contain the columns you select for replication, along with some system columns created by Stitch. Refer to the [sample table](#sample-table) in the next section for an example.


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/google-sheets
---
{% assign integration = page %}
{% include misc/data-files.html %}