---
tap: "liveperson"
version: "1.0"
key: "user"

name: "users"
doc-link: "https://developers.liveperson.com/users-api-overview.html"
singer-schema: "https://github.com/singer-io/tap-liveperson/blob/master/tap_liveperson/schemas/users.json"
description: |
  The `{{ table.name }}` table contains info about the users in your {{ integration.display_name }} account. This includes agents, agent managers, administrators, and campaign managers.

  **Note**: Stitch will query for and replicate deleted users.

replication-method: "Key-based Incremental"

replication-key:
  name: "startTime"

api-method:
    name: "Get all users"
    doc-link: "https://developers.liveperson.com/users-api-methods-get-all-users.html"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    #foreign-key-id: "user-id"

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "loginName"
    type: "string"
    description: ""

  - name: "pid"
    type: "string"
    description: ""
---