---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "google-sheets"

version: "1"

foreign-keys:
  - id: "file-id"
    table: "file_metadata"
    attribute: "id"
    all-foreign-keys:
      - table: "file_metadata"
        join-on: "id"

  - id: "spreadsheet-id"
    table: "spreadsheet_metadata"
    attribute: "spreadsheetId"
    all-foreign-keys:
      - table: "spreadsheet_metadata"
        join-on: "spreadsheetId"
      - table: "sheet_metadata"
        join-on: "spreadsheetId"
      - table: "sheets_loaded"
        join-on: "spreadsheetId"  


  - id: "sheet-id"
    table: "sheet_metadata"
    attribute: "sheetId"
    all-foreign-keys:
      - table: "sheet_metadata"
        join-on: "sheetId"
      - table: "sheets_loaded"
        join-on: "sheetId"


  - id: "column-index"
    table: "sheet_metadata"
    attribute: "columns.column-index"
    all-foreign-keys:
      - table: "sheet_metadata"
        join-on: "columns.column-index"

---