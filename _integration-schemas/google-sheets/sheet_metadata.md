---
tap: "google-sheets"
version: "1.0"
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
        description: "The column index in the data table on which the filter is applied to."
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

  - name: "gridProperties"
    type: "object"
    description: ""
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
    description: |
      The index of the sheet within the spreadsheet. When adding or updating sheet properties, if this field is excluded then the sheet is added or moved to the end of the sheet list. When updating sheet indices or inserting sheets, movement is considered in "before the move" indexes. For example, if there were 3 sheets (S1, S2, S3) in order to move S1 ahead of S2 the index would have to be set to 2. A sheet index update request is ignored if the requested index is identical to the sheets current index or if the requested new index is equal to the current sheet index + 1.

  - name: "sheetId"
    type: "integer"
    description: "The ID of the sheet. Must be non-negative. This field cannot be changed once set."

  - name: "sheetType"
    type: "string"
    description: "The type of sheet. This field cannot be changed once set. It can be be following values . "

  - name: "sheetUrl"
    type: "string"
    description: "The url of the sheet. This field is read-only."

  - name: "spreadsheetId"
    type: "string"
    description: "The ID of the spreadsheet. This field is read-only."

  - name: "title"
    type: "string"
    description: "The title of the spreadsheet."
---
