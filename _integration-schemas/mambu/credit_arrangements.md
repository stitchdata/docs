---
tap: "mambu"
version: "1.0"

name: "credit_arrangements"
doc-link: "https://api.mambu.com/?shell#welcome"
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/credit_arrangements.json"
description: "This table contains information about Credit Arrangements."

replication-method: "Key-based Incremental"

api-method:
    name: "Credit Arrangements"
    doc-link: "https://api.mambu.com/?shell#creditarrangements"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The unique credit arrangement ID."
#    foreign-key-id: "credit-arrangement-id"

  - name: "last_modified_date"
    type: "date-time"
    description: "The last date and time that the credit arrangement was modified."
    replication-key: true

  - name: "amount"
    type: "number"
    description: "The maximum credit amount the client can be exposed to."

  - name: "approved_date"
    type: "date-time"
    description: "The date the credit arrangement was approved."

  - name: "available_credit_amount"
    type: "number"
    description: "The amount of credit available in the arrangement."

  - name: "consumed_credit_amount"
    type: "number"
    description: "The amount of credit used. This is the difference taken from the amount and availible credit amount."

  - name: "creation_date"
    type: "date-time"
    description: "The date the credit arrangement was created."

  - name: "custom_field_sets"
    type: "array"
    description: ""
    subattributes:
      - name: "custom_field_set_id"
        type: "string"
        description: ""
        foreign-key-id: "custom-field-set-id"
      - name: "custom_field_values"
        type: "array"
        description: ""
        subattributes:
          - name: "custom_field_id"
            type: "string"
            description: ""
            foreign-key-id: "custom-field-id"
          - name: "custom_field_value"
            type: "string"
            description: ""

  - name: "encoded_key"
    type: "string"
    description: "The encoded key of the credit arrangement. This value is auto-generated and unique."

  - name: "expire_date"
    type: "date-time"
    description: "The date the credit arrangement expires."

  - name: "holder_key"
    type: "string"
    description: "The encoded key of the client or group."
    foreign-key-id: "holder-key"

  - name: "holder_type"
    type: "string"
    description: "The line of credit holder's type - client or group."

  - name: "notes"
    type: "string"
    description: "The description of the credit arrangement."

  - name: "start_date"
    type: "date-time"
    description: "The start date from which the credit arrangement becomes active."

  - name: "state"
    type: "string"
    description: "The state of the credit agrrangement - Pending Approval, Approved, Active or Closed."

  - name: "sub_state"
    type: "string"
    description: "The substate of the credit agrrangment. This will either be Withdrawn or Rejected when the state of the arrangement is Closed."
---
