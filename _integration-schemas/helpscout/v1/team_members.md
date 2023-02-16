---
tap: "helpscout"
version: "1"
key: ""

name: "team_members"
doc-link: ""
singer-schema: https://github.com/singer-io/tap-helpscout/tree/master/tap_helpscout/schemas/team_members.json
description: "This report contains information about team members."

api-method:
    name: "List team members"
    doc-link: "https://developer.helpscout.com/mailbox-api/endpoints/teams/list-team-members/"

replication-method: "Full Table"

table-key-properties: "team_id, user_id"
valid-replication-keys: ""

attributes:
  - name: "team_id"
    type: "integer"
    description: "ID of the team"
    primary-key: true

  - name: "user_id"
    type: "integer"
    description: "ID of the User"
    primary-key: true
---