---
tap: "activecampaign"
version: "0.3"
key: ""

name: "site_messages"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/site_messages.json"
description: ""

replication-method: "Key-based Incremental"

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The side message ID."
    #foreign-key-id: "site-message-ID"

  - name: "ldate"
    type: "date-time"
    description: "The side message ldate."
    replication-key: true

  - name: "automation"
    type: "integer"
    description: "The automation ID."
    foreign-key-id: "automation-id"
  
  - name: "name"
    type: "string"
    description: ""
  - name: "template"
    type: "object"
    description: ""
    subattributes:
      - name: "detailed"
        type: "object"
        description: ""

      - name: "initial"
        type: "object"
        description: ""
---
