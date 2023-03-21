---
tap: "activecampaign"
version: "0.4"
key: ""

name: "account_custom_field_values"
doc-link: "https://developers.activecampaign.com/reference#custom-account-field-values"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/account_custom_field_values.json"
description: |
  The `{{ table.name }}` table contains information about your account custom fields' values in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List all custom field values"
    doc-link: "https://developers.activecampaign.com/reference#list-all-custom-field-values-2"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The custom field value ID."
    #foreign-key-id: 

  - name: "updated_timestamp"
    type: "date-time"
    description: "The time the custom field value was last updated."
    replication-key: true

  - name: "account_custom_field_metum_id"
    type: "integer"
    description: ""
  - name: "account_id"
    type: "integer"
    description: "The account ID."
    foreign-key-id: "account-id"
  - name: "created_timestamp"
    type: "date-time"
    description: ""
  - name: "custom_field_id"
    type: "integer"
    description: "The custom field ID."
    foreign-key-id: "custom-field-id"
  - name: "field_value"
    type: "string"
    description: ""
---
