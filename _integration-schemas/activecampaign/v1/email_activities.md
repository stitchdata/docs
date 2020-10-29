---
tap: "activecampaign"
version: "0.x"
key: ""
name: "email_activities"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/email_activities.json"
description: ""
replication-method: ""
api-method:
    name: ""
    doc-link: ""
attributes:
  - name: "account"
    type: "integer"
    description: ""
  - name: "cc_address"
    type: "string"
    description: ""
  - name: "contact"
    type: "integer"
    description: ""
  - name: "d_id"
    type: "integer"
    description: ""
  - name: "deal"
    type: "integer"
    description: ""
  - name: "from_address"
    type: "string"
    description: ""
  - name: "from_name"
    type: "string"
    description: ""
  - name: "id"
    type: "integer"
    description: ""
  - name: "message"
    type: "string"
    description: ""
  - name: "message_html"
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
  - name: "relid"
    type: "integer"
    description: ""
  - name: "reltype"
    type: "string"
    description: ""
  - name: "subject"
    type: "string"
    description: ""
  - name: "subscriberid"
    type: "integer"
    description: ""
  - name: "to_address"
    type: "string"
    description: ""
  - name: "tstamp"
    type: "date-time"
    description: ""
  - name: "user"
    type: "integer"
    description: ""
  - name: "userid"
    type: "integer"
    description: ""
---