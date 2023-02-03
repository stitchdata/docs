---
tap: "activecampaign"
version: "0.3"
key: ""

name: "deal_groups"
doc-link: "https://developers.activecampaign.com/reference#pipelines"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/deal_groups.json"
description: |
  The `{{ table.name }}` table contains information about deal pipelines in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List all pipelines"
    doc-link: "https://developers.activecampaign.com/reference#list-all-pipelines"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The pipeline ID."
    foreign-key-id: "pipeline-id"

  - name: "udate"
    type: "date-time"
    description: "The pipeline udate."
    replication-key: true

  - name: "allgroups"
    type: "string"
    description: ""
  - name: "allusers"
    type: "string"
    description: ""
  - name: "autoassign"
    type: "string"
    description: ""
  - name: "cdate"
    type: "date-time"
    description: ""
  - name: "currency"
    type: "string"
    description: ""
  
  - name: "stages"
    type: "integer"
    description: "The stage ID."
    foreign-key-id: "stage-id"

  - name: "stages"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "integer"
        description: ""
  - name: "title"
    type: "string"
    description: ""

---
