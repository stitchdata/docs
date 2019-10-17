---
tap: "mambu"
version: "1.0"

name: "clients"
doc-link: "https://api.mambu.com/?shell#welcome"
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/clients.json"
description: "This table contains information about Clients."

replication-method: "Key-based Incremental"

api-method:
    name: "Clients"
api-method:
  name: "Get all clients"
  doc-link: "https://api.mambu.com/?http#clients-getall"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The unique client ID."
#    foreign-key-id: "client-id"

  - name: "last_modified_date"
    type: "date-time"
    description: "The last date and time that the client was modified."
    replication-key: true

  - name: "activation_date"
    type: "date-time"
    description: "The first date that the client was set as active."

  - name: "addresses"
    type: "array"
    description: ""
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

  - name: "approved_date"
    type: "date-time"
    description: "The date when the client was approved."

  - name: "assigned_centre_key"
    type: "string"
    description: "Ended key of the center that the client is assigned to."
    foreign-key-id: "client-encoded-key"

  - name: "assigned_user_key"
    type: "string"
    description: "The encoded key of the user that the client is assigned to."
    foreign-key-id: "user-encoded-key"

  - name: "birth_date"
    type: "date"
    description: "The date that the client born."

  - name: "client_role_key"
    type: "string"
    description: "The role which describes the client's use within the system."

  - name: "closed_date"
    type: "date-time"
    description: "The date that the client was closed."

  - name: "creation_date"
    type: "date-time"
    description: "The date that the client was created."

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

  - name: "email_address"
    type: "string"
    description: "The client's email address."

  - name: "encoded_key"
    type: "string"
    description: "The encoded key of the client. This value is generated and globally unique."

  - name: "first_name"
    type: "string"
    description: "The client's first name."

  - name: "gender"
    type: "string"
    description: "The client's gender."

  - name: "group_loan_cycle"
    type: "integer"
    description: "The number of paid and closed accounts for this client's group."

  - name: "home_phone"
    type: "string"
    description: "The client's home phone number."

  - name: "id_documents"
    type: "array"
    description: ""
    subattributes:
      - name: "identification_document_template_key"
        type: "string"
        description: ""
      - name: "issuing_authority"
        type: "string"
        description: ""
      - name: "client_key"
        type: "string"
        description: ""
      - name: "document_type"
        type: "string"
        description: ""
      - name: "index_in_list"
        type: "integer"
        description: ""
      - name: "valid_until"
        type: "string"
        description: ""
      - name: "encoded_key"
        type: "string"
        description: ""
      - name: "document_id"
        type: "string"
        description: ""              

  - name: "last_name"
    type: "string"
    description: "The client's last name."

  - name: "middle_name"
    type: "string"
    description: "The client's middle name."

  - name: "migration_event_key"
    type: "string"
    description: "The encoded key of the migration event that the client is assigned to."

  - name: "mobile_phone"
    type: "string"
    description: "The client's mobile phone number."

  - name: "notes"
    type: "string"
    description: "Notes about the client."

  - name: "preferred_language"
    type: "string"
    description: "The client's preferred language selection in Mambu."

  - name: "profile_picture_key"
    type: "string"
    description: "The encoded key of the client's profile picture."

  - name: "profile_signature_key"
    type: "string"
    description: "The encoded key of the client's profile signature."

  - name: "state"
    type: "string"
    description: "The state of the client's workflow status."
---
