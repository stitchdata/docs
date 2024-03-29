---
tap: "google-sheets"
version: "1"
key: "file-metadata"

name: "file_metadata"
doc-link: "https://developers.google.com/sheets/api/reference/rest"
singer-schema: "https://github.com/singer-io/tap-google-sheets/blob/master/tap_google_sheets/schemas/file_metadata.json"
description: |
  The `{{ table.name }}` table contains metadata about the spreadsheet defined in the integration's settings.

replication-method: "Full Table"

api-method:
  name: "getSheets"
  doc-link: "https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/sheets#top_of_page"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The file ID."
#   foreign-key-id: "file-id"

  - name: "modifiedTime"
    type: "date-time"
    description: "The date and time the file was last modified."

  - name: "createdTime"
    type: "date-time"
    description: "The date the file was created."

  - name: "driveId"
    type: "string"
    description: "The ID of the drive containing the file."

  - name: "lastModifyingUser"
    type: "object"
    description: "The user who last modified the file."
    subattributes:
      - name: "displayName"
        type: "string"
        description: "The user's display name."

      - name: "emailAdress"
        type: "string"
        description: "The user's email address."

      - name: "kind"
        type: "string"
        description: "The type of user."

  - name: "name"
    type: "string"
    description: "The name of the file."

  - name: "teamDriveId"
    type: "string"
    description: "The team drive ID."

  - name: "version"
    type: "integer"
    description: "The version of the file."
---