---
tap: "mambu"
version: "1.0"

name: "branches"
doc-link: "https://api.mambu.com/?shell#welcome"
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/branches.json"
description: "This table contains information about Branches."

replication-method: "Key-based Incremental"

api-method:
    name: "Branches"
    doc-link: "https://api.mambu.com/?shell#branches"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The unique branch ID."
#    foreign-key-id: "branch-id"

  - name: "last_modified_date"
    type: "date-time"
    replication-key: true
    description: "The last date and time that the branch was modified."

  - name: "addresses"
    type: "array"
    description: "A list of branch addresses."
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
    
  - name: "branch_holidays"
    type: "array"
    description: "A list of branch holidays."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "date"
        type: "string"
        description: ""

      - name: "encoded_key"
        type: "string"
        description: ""

      - name: "is_anually_recurring"
        type: "boolean"
        description: ""

      - name: "creation_date"
        type: "string"
        description: ""
        
  - name: "creation_date"
    type: "date-time"
    description: "The branch creation date."

  - name: "custom_field_sets"
    type: "array"
    description: ""
    subattributes:
      - name: "custom_field_set_id"
        type: "string"
        foreign-key-id: "custom-field-set-id"
        description: ""

      - name: "custom_field_values"
        type: "array"
        description: ""

        subattributes:
          - name: "custom_field_id"
            type: "string"
            foreign-key-id: "custom-field-id"
            description: ""

          - name: "custom_field_value"
            type: "string"
            description: ""

  - name: "email_address"
    type: "string"
    description: "The branch email address."

  - name: "encoded_key"
    type: "string"
    description: "The entity's encoded key. This value is generated and globally unique."
    foreign-key-id: "branch-encoded-key"

  - name: "name"
    type: "string"
    description: "The branch name."

  - name: "notes"
    type: "string"
    description: "Notes about the branch."

  - name: "phone_number"
    type: "string"
    description: "The branch phone number."

  - name: "state"
    type: "string"
    description: "The branch state."
---