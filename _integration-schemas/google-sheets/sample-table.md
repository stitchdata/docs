---
tap: "google-sheets"
version: "1"
key: "sample-table"

name: "sample_table"
doc-link: "https://developers.google.com/sheets/api/reference/rest"
singer-schema: ""
description: |
  This is an example of a table created from a sheet you set to replicate.

  For every sheet you set to replicate, Stitch will create a corresponding table in your destination. The table will contain the columns you select in Stitch, along with a few columns Stitch requires for replication.
  
  Refer to the [Data replication](#extraction--data-replication) section for more info about how this table replicates.

replication-method: "Key-based Incremental"

api-method:
  name: "getSheets"
  doc-link: "https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/sheets#top_of_page"

attributes:
  - name: "__sdc_row"
    type: "integer"
    primary-key: true
    description: |
      The number of the row in the spreadsheet.
#   foreign-key-id: "file-id"

  - name: "__sdc_sheet_id"
    type: "integer"
    description: "The ID of the sheet containing the record."
    foreign-key-id: "sheet-id"

  - name: "__sdc_spreadsheet_id"
    type: "string"
    description: "The ID of the spreadsheet containing the record."
    foreign-key-id: "spreadsheet-id"

  - name: "[COLUMNS_YOU_SELECT]"
    type: "varies"
    description: |
      A column will be created for every column set to replicate in Stitch.
---