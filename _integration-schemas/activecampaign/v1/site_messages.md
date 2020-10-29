---
tap: "activecampaign"
version: "0.x"
key: ""
name: "site_messages"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/site_messages.json"
description: ""
replication-method: ""
api-method:
    name: ""
    doc-link: ""
attributes:
  - name: "automation"
    type: "integer"
    description: ""
  - name: "id"
    type: "integer"
    description: ""
  - name: "ldate"
    type: "date-time"
    description: ""
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
        subattributes: &id001 [
            ]
      - name: "initial"
        type: "object"
        description: ""
        subattributes: *id001
---
