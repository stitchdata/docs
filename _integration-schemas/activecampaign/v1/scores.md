---
tap: "activecampaign"
version: "0.3"
key: ""

name: "scores"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/scores.json"
description: |
  The `{{ table.name }}` table contains information about prioritization scores on leads in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List all scores"
    doc-link: "https://developers.activecampaign.com/reference#list-all-scores"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The score ID."
    #foreign-key-id: "score-id"

  - name: "mdate"
    type: "date-time"
    description: "The time the score was last modified."
    replication-key: true

  - name: "cdate"
    type: "date-time"
    description: ""
  - name: "descript"
    type: "string"
    description: ""
  
  - name: "name"
    type: "string"
    description: ""
  - name: "reltype"
    type: "string"
    description: ""
  - name: "status"
    type: "integer"
    description: ""
---
