---
tap: "google-sheets"
version: "1"
key: "sheets_loaded"

name: "sheets_loaded"
doc-link: "https://developers.google.com/sheets/api/reference/rest"
singer-schema: "https://github.com/singer-io/tap-google-sheets/blob/master/tap_google_sheets/schemas/sheets_loaded.json"
description: "This table contains table contains information about the individual sheets loaded."

replication-method: "Full Table"

api-method:
    name: "getSheets"
    doc-link: "https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/sheets#top_of_page"

attributes:
  - name: "sheetId"
    type: "integer"
    primary-key: true
    description: "The ID of the sheet."
    foreign-key-id: "sheet-id"

  - name: "spreadsheetId"
    type: "string"
    primary-key: true
    description: "The ID of the spreadsheet."
    foreign-key-id: "spreadsheet-id"

  - name: "lastRowNumber"
    type: "integer"
    description: "The number of the last row."

  - name: "loadDate"
    type: "date-time"
    description: "The date the sheets were loaded."

  - name: "title"
    type: "string"
    description: "The title of the spreadsheet."
---
