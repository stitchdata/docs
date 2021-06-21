---
tap: "mambu"
version: "1"
key: ""

name: "activities"
doc-link: "https://support.mambu.com/docs/activities-api"
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/activities.json"
description: "This table contains information about Activities."

replication-method: "Key-based Incremental"

api-method:
    name: "GET Activities"
    doc-link: "https://support.mambu.com/docs/activities-api"

attributes:
  - name: "encoded_key"
    type: "string"
    primary-key: true
    description: "The unique encoded key."
#    foreign-key-id: "activities-encoded-key"

  - name: "timestamp"
    type: "date-time"
    description: "The time of the activity."  

  - name: "branch_name"
    type: "string"
    description: ""
  - name: "client_key"
    type: "string"
    description: ""
  - name: "client_name"
    type: "string"
    description: ""
  
  - name: "field_changes"
    type: "null"
    description: ""
  - name: "loan_account_name"
    type: "string"
    description: ""
  - name: "loan_product_name"
    type: "string"
    description: ""
  - name: "notes"
    type: "string"
    description: ""
  
  - name: "transaction_ID"
    type: "integer"
    description: ""
  - name: "type"
    type: "string"
    description: ""
  - name: "user_key"
    type: "string"
    description: ""
  - name: "user_name"
    type: "string"
    description: ""
---
