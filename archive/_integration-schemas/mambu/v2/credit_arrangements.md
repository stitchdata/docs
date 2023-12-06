---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "mambu"
version: "2"
key: "credit-arrangement"

name: "credit_arrangements"
doc-link: "https://api.mambu.com/?shell#welcome"
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/credit_arrangements.json"
description: |
  This table contains information about credit arrangements.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "Get all credit arrangements (v2.0)"
  doc-link: "https://api.mambu.com/?http#creditarrangements-getall"

replication-method: "Key-based Incremental"


# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The unique credit arrangement ID."

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
    description: "The amount of credit used. This is the difference taken from the amount and available credit amount."

  - name: "creation_date"
    type: "date-time"
    description: "The date the credit arrangement was created."

  - name: "custom_fields"
    type: "array"
    description: ""
    subattributes:
      - name: "field_set_id"
        type: "string"
        foreign-key-id: "custom-field-set-id"
        description: ""

      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "custom-field-id"

      - name: "value"
        type: "string"
        description: ""

  - name: "encoded_key"
    type: "string"
    description: "The encoded key of the credit arrangement. This value is auto-generated and unique."
    foreign-key-id: "credit-arrangement-key"

  - name: "expire_date"
    type: "date-time"
    description: "The date the credit arrangement expires."

  - name: "holder_key"
    type: "string"
    description: |
      The encoded key of the client or group.

      Depending on the `holder_type` value, this will be a foreign key to either the [`clients`](#clients) or [`groups`](#groups) table.

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
    description: |
      The state of the credit arrangement. Possible values are:
      
      - `Pending Approval`
      - `Approved`
      - `Active`
      - `Closed`

  - name: "sub_state"
    type: "string"
    description: "The substate of the credit arrangement. This will either be `Withdrawn` or `Rejected` when the `state` of the arrangement is `Closed`."
---