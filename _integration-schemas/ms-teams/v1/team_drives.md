---
tap: "ms-teams"
version: "1"
key: ""

name: "team_drives"
doc-link: "https://docs.microsoft.com/en-us/graph/api/drive-get?view=graph-rest-beta&tabs=http#get-the-document-library-associated-with-a-group"
singer-schema: "https://github.com/singer-io/tap-ms-teams/blob/master/tap_ms_teams/schemas/team_drives.json"
description: |
  The `{{ table.name }}` table contains information about the drive that your team is on in your Microsoft account.
  
replication-method: "Key-based Incremental"

api-method:
    name: "Get the document library associated with a group"
    doc-link: "https://docs.microsoft.com/en-us/graph/api/drive-get?view=graph-rest-beta&tabs=http#get-the-document-library-associated-with-a-group"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The drive ID."
    #foreign-key-id: "drive-id"

  - name: "last_modified_date_time"
    type: "string"
    description: "The time the drive was last modified."
    replication-key: true

  - name: "created_by"
    type: "object"
    description: ""
    subattributes:
      - name: "user"
        type: "object"
        description: ""
        subattributes:
          - name: "display_name"
            type: "string"
            description: ""
  - name: "drive_type"
    type: "string"
    description: ""
  
  - name: "name"
    type: "string"
    description: ""
  - name: "owner"
    type: "object"
    description: ""
    subattributes:
      - name: "group"
        type: "object"
        description: ""
        subattributes:
          - name: "display_name"
            type: "string"
            description: ""
          - name: "email"
            type: "string"
            description: ""
          - name: "id"
            type: "string"
            description: "The group ID."
            foreign-key-id: "group-id"
  - name: "quota"
    type: "object"
    description: ""
    subattributes:
      - name: "deleted"
        type: "integer"
        description: ""
      - name: "remaining"
        type: "number"
        description: ""
      - name: "state"
        type: "string"
        description: ""
      - name: "total"
        type: "number"
        description: ""
      - name: "used"
        type: "integer"
        description: ""
  - name: "web_url"
    type: "string"
    description: ""
---
