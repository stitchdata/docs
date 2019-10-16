---
tap: "mambu"
version: "1.0"

name: "centres"
doc-link: "https://api.mambu.com/?shell#welcome"
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/centres.json"
description: "This table contains information about Centers."

replication-method: "Key-based Incremental"

api-method:
    name: "Centres"
    doc-link: "https://api.mambu.com/?shell#centres"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The unique center ID."
#    foreign-key-id: "center-id"

- name: "last_modified_date"
    type: "date-time"
    description: "The last date and time that the center was modified."
    replication-key: true

  - name: "addresses"
    type: "array"
    description: "The list of addresses for a center."
    subattributes:
      - name: "country"
        type: "string"
        description: ""
      - name: "parent_key"
        type: "string"
        description: ""
      - name: "city"
        type: "string"
        description: ""
      - name: "latitude"
        type: "number"
        description: ""
      - name: "postcode"
        type: "string"
        description: ""
      - name: "index_in_list"
        type: "integer"
        description: ""
      - name: "encoded_key"
        type: "string"
        description: ""
      - name: "region"
        type: "string"
        description: ""
      - name: "line2"
        type: "string"
        description: ""
      - name: "line1"
        type: "string"
        description: ""
      - name: "longitude"
        type: "number"
        description: ""    

  - name: "assigned_branch_key"
    type: "string"
    description: "The encoded key of the branch that the center is assigned to."
    foreign-key-id: "branch-encoded-key"

  - name: "creation_date"
    type: "date-time"
    description: "The center creation date."

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
    description: "The encoded key of the entity. This value is generated and globally unique."

  - name: "meeting_day"
    type: "string"
    description: "The day of the week that repayments are collected."

  - name: "name"
    type: "string"
    description: "The center name."

  - name: "notes"
    type: "string"
    description: "Notes about the center."

  - name: "state"
    type: "string"
    description: "The center state."
---
