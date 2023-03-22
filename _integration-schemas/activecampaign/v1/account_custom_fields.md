---
tap: "activecampaign"
version: "1"
key: ""

name: "account_custom_fields"
doc-link: "https://developers.activecampaign.com/reference#custom-account-fields-1"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/account_custom_fields.json"
description: |
  The `{{ table.name }}` table contains information about account custom fields in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List all custom fields"
    doc-link: "https://developers.activecampaign.com/reference#list-all-custom-fields"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The custom field ID."
    foreign-key-id: "custom-field-id"
  
  - name: "updated_timestamp"
    type: "date-time"
    description: "The time the custom field was last updated."
    replication-key: true

  - name: "created_timestamp"
    type: "date-time"
    description: ""
  - name: "display_order"
    type: "integer"
    description: ""
  - name: "field_default"
    type: "string"
    description: ""
  - name: "field_default_currency"
    type: "string"
    description: ""
  - name: "field_label"
    type: "string"
    description: ""
  - name: "field_options"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
  - name: "field_type"
    type: "string"
    description: ""
  - name: "hide_field_flag"
    type: "boolean"
    description: ""
  - name: "is_form_visible"
    type: "boolean"
    description: ""
  - name: "is_required"
    type: "boolean"
    description: ""
  - name: "known_field_id"
    type: "integer"
    description: ""
  - name: "personalization"
    type: "string"
    description: ""
---
