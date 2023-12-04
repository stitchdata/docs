---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "mambu"
version: "1"
key: "activity"

name: "activities"
doc-link: "https://support.mambu.com/docs/activities-api"
singer-schema: "https://github.com/singer-io/tap-mambu/tree/v1.3.3/tap_mambu/schemas/activities.json"
description: |
  This table contains information about activities.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "Get all activities (v1.0)"
  doc-link: "https://api.mambu.com/v1/#activities-get-all-activities"

replication-method: "Key-based Incremental"


# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "encoded_key"
    type: "string"
    primary-key: true
    description: "The unique encoded key."
#    foreign-key-id: "activities-encoded-key"

  - name: "timestamp"
    type: "date-time"
    replication-key: true
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
    type: "array"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "transaction_id"
        type: "integer"
        description: ""

      - name: "field_change_name"
        type: "string"
        description: ""

      - name: "original_value"
        type: "string"
        description: ""

      - name: "new_value"
        type: "string"
        description: ""

      - name: "clientKey"
        type: "string"
        description: ""

      - name: "branchKey"
        type: "string"
        description: ""

      - name: "loanProductKey"
        type: "string"
        description: ""

      - name: "loanAccountKey"
        type: "string"
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