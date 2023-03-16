---
tap: "helpscout"
version: "1"
key: ""

name: "teams"
doc-link: ""
singer-schema: https://github.com/singer-io/tap-helpscout/tree/master/tap_helpscout/schemas/teams.json
description: "This report contains information about all the different teams in the company."

replication-method: "Key-based Incremental"

api-method:
    name: "List teams"
    doc-link: "https://developer.helpscout.com/mailbox-api/endpoints/teams/list-teams/"

table-key-properties: "id"
valid-replication-keys: "updated_at"

attributes:
  - name: "created_at"
    type: "date-time"
    description: "Creation date"

  - name: "id"
    type: "integer"
    description: "Team ID"
    primary-key: true

  - name: "initials"
    type: "string"
    description: "Team initials"

  - name: "mention"
    type: "string"
    description: "Details about the team"

  - name: "name"
    type: "string"
    description: "Team name"

  - name: "photo_url"
    type: "string"
    description: "Photo URL of the team's logo"

  - name: "timezone"
    type: "string"
    description: "Timezone of the team"

  - name: "updated_at"
    type: "date-time"
    description: "Date of last update"
    replication-key: true
---