---
tap: "google-sheets"
version: "1"
key: "spreadsheet_metadata"

name: "spreadsheet_metadata"
doc-link: "https://developers.google.com/sheets/api/reference/rest"
singer-schema: "https://github.com/singer-io/tap-google-sheets/blob/master/tap_google_sheets/schemas/spreadsheet_metadata.json"
description: |
  The `{{ table.name }}` table contains metadata about the spreadsheet defined in the integration's settings.

replication-method: "Full Table"

api-method:
  name: "getSheets"
  doc-link: "https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/sheets#top_of_page"

attributes:
  - name: "spreadsheetId"
    type: "string"
    primary-key: true
    description: "The ID of the spreadsheet."
    foreign-key-id: "spreadsheet-id"

  - name: "properties"
    type: "object"
    description: "Overall properties of a spreadsheet."
    subattributes:
      - name: "autoRecalc"
        type: "string"
        description: "The amount of time to wait before volatile functions are recalculated."
        
      - name: "locale"
        type: "string"
        description: |
          The locale of the spreadsheet in one of the following formats:
            - an ISO 639-1 language code such as `en`
            - an ISO 639-2 language code such as `fil`, if no 639-1 code exists
            - a combination of the ISO language code and country code, such as `en_US`

      - name: "timeZone"
        type: "string"
        description: "The time zone of the spreadsheet, in CLDR format such as `America/New_York`. If the time zone isn't recognized, this may be a custom time zone such as `GMT-07:00`."

      - name: "title"
        type: "string"
        description: "The title of the spreadsheet."

  - name: "spreadsheetUrl"
    type: "string"
    description: "The url of the spreadsheet."
---