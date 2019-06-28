---
tap: "liveperson"
version: "1.0"
key: "skill"

name: "skills"
doc-link: "https://developers.liveperson.com/skills-api-overview.html"
singer-schema: "https://github.com/singer-io/tap-liveperson/blob/master/tap_liveperson/schemas/skills.json"
description: |
  The `{{ table.name }}` table contains info about the agent skills in your {{ integration.display_name }} account.

  **Note**: Stitch will query for and replicate deleted skills.

replication-method: "Key-based Incremental"

replication-key:
  name: "startTime"

api-method:
    name: "Get all skills"
    doc-link: "https://developers.liveperson.com/skills-api-methods-get-all-skills.html"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    #foreign-key-id: "skill-id"

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "pid"
    type: "string"
    description: ""
---