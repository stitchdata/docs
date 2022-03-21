---
tap: "activecampaign"
version: "0.3"
key: ""

name: "email_activities"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/email_activities.json"
description: ""

replication-method: "Key-based Incremental"

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The email activity ID."
    #foreign-key-id: "email-activity-id"

  - name: "tstamp"
    type: "date-time"
    description: "The email activity timestamp."
    replication-key: true

  - name: "account"
    type: "integer"
    description: "The account ID."
    foreign-key-id: "account-id"
  - name: "cc_address"
    type: "string"
    description: ""
  - name: "contact"
    type: "integer"
    description: "The contact ID."
    foreign-key-id: "contact-id"
  - name: "d_id"
    type: "integer"
    description: ""
  - name: "deal"
    type: "integer"
    description: "The deal ID."
    foreign-key-id: "deal-id"
  - name: "from_address"
    type: "string"
    description: ""
  - name: "from_name"
    type: "string"
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

  - name: "user"
    type: "integer"
    description: ""
  - name: "userid"
    type: "integer"
    description: "The user ID."
    foreign-key-id: "user-id"
---