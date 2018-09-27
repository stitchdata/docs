---
tap: "uservoice"
# version: "1.0"

name: "teams"
doc-link: https://developer.uservoice.com/docs/api/v2/reference/#/Teams
singer-schema: https://github.com/singer-io/tap-uservoice/blob/master/tap_uservoice/streams/teams.py
description: |
  The `{{ table.name }}` table contains info about the teams in your {{ integration.display_name }} account. {{ integration.display_name }} admins and contributors can be assigned to teams to organize feedback the feedback they capture by department, such as Sales, Support, or Product.

replication-method: "Key-based Incremental"

replication-key:
  name: "updated_before + updated_after"

api-method:
  name: List teams
  doc-link: https://developer.uservoice.com/docs/api/v2/reference/#list-

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The team ID."
    foreign-key-id: "team-id"

  - name: "name"
    type: "string"
    description: "The name of the team."

  - name: "members_count"
    type: "integer"
    description: "The total number of users associated with the team."
---