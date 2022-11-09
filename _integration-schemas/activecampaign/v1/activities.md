---
tap: "activecampaign"
version: "0.3"
key: ""

name: "activities"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/activities.json"
description: ""

replication-method: "Key-based Incremental"

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The activity ID."
    #foreign-key-id: "activity-id"

  - name: "tstamp"
    type: "date-time"
    description: "The activity timestamp."
    replication-key: true  

  - name: "json_data"
    type: "string"
    description: ""
  - name: "permission"
    type: "string"
    description: ""
  - name: "reference"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
      - name: "type"
        type: "string"
        description: ""
  - name: "reference_action"
    type: "string"
    description: ""
  - name: "reference_id"
    type: "integer"
    description: ""
  - name: "reference_model_name"
    type: "string"
    description: ""
  - name: "reference_type"
    type: "string"
    description: ""
  - name: "subscriberid"
    type: "integer"
    description: ""
  
  - name: "user"
    type: "integer"
    description: ""
  - name: "userid"
    type: "integer"
    description: "The user ID."
    foreign-key-id: "user-id"
---
