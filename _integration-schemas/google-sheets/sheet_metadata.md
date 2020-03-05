---
tap: "google-sheets"
version: "1"
key: "sheet_metadata"

name: "sheet_metadata"
doc-link: "https://developers.google.com/sheets/api/reference/rest"
singer-schema: "https://github.com/singer-io/tap-google-sheets/blob/master/tap_google_sheets/schemas/sheet_metadata.json"
description: "This table contains metadata about the sheets within a spreadsheet."

replication-method: "Full Table"

api-method:
    name: "getSheets"
    doc-link: "https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/sheets#top_of_page"

attributes:
  - name: "columns"
    type: "object"
    description: ""
    subattributes:
      - name: "columnIndex"
        type: "integer"
        primary-key: true
        description: "The column index in the data table on which the filter is applied to."
        foreign-key-id: "column-index"
      - name: "columnLetter"
        type: "string"
        description: "The letter of the column."
      - name: "columnName"
        type: "string"
        description: "The header name in the column."
      - name: "columnType"
        type: "string"
        description: "The type of column"
      - name: "columnSkipped"
        type: "boolean"
        description: "Field that identifies if the column has been skipped."
      - name: "type"
        type: "string"
        description: ""
      - name: "format"
        type: "string"
        description: ""  

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

  - name: "gridProperties"
    type: "object"
    description: "The properties of a grid."
    subattributes:
      - name: "columnCount"
        type: "integer"
        description: "The number of columns in the grid."
      - name: "frozenColumnCount"
        type: "integer"
        description: "The number of columns that are frozen in the grid."
      - name: "frozenRowCount"
        type: "integer"
        description: "The number of rows that are frozen in the grid."
      - name: "rowCount"
        type: "integer"
        description: "The number of rows in the grid."

  - name: "index"
    type: "integer"
    description: "The index of the sheet within the spreadsheet."

  - name: "sheetType"
    type: "string"
    description: "The type of sheet. It can be be following values: `sheet_type_unspecified`, `object`, `grid`."

  - name: "sheetUrl"
    type: "string"
    description: "The url of the sheet."

  - name: "title"
    type: "string"
    description: "The title of the spreadsheet."
---
