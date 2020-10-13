---
tap: "intercom"
version: "1"
key: "team"

name: "teams"
doc-link: "https://developers.intercom.com/intercom-api-reference/reference#teams-model"
singer-schema: "https://github.com/singer-io/tap-intercom/blob/master/tap_intercom/schemas/teams.json"
description: |
  The `{{ table.name }}` table contains information about teams in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "List all teams"
  doc-link: "https://developers.intercom.com/intercom-api-reference/reference#list-teams"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The team ID."
    foreign-key-id: "team-id"

  - name: "admin_ids"
    type: "array"
    description: "The admins that belong to the team."
    subattributes:
      - name: "id"
        type: "string"
        description: "The admin ID."
        foreign-key-id: "admin-id"
  
  - name: "name"
    type: "string"
    description: "The name of the team."

  - name: "type"
    type: "string"
    description: "This will be `team`."
---