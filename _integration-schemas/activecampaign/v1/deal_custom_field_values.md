---
tap: "activecampaign"
version: "1"
key: ""

name: "deal_custom_field_values"
doc-link: "https://developers.activecampaign.com/reference#dealcustomfielddata"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/deal_custom_field_values.json"
description: |
  The `{{ table.name }}` table contains information about custom field values for deals in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List all custom field values"
    doc-link: "https://developers.activecampaign.com/reference#list-all-custom-field-values"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The custom field value ID."
    #foreign-key-id: "deal-custom-field-value-id"

  - name: "updated_timestamp"
    type: "date-time"
    description: "The time the custom field was last updated."
    replication-key: true

  - name: "created_timestamp"
    type: "date-time"
    description: ""
  - name: "custom_field_id"
    type: "integer"
    description: "The custom field ID."
    foreign-key-id: "deal-custom-field-id"

  - name: "deal_custom_field_metum_id"
    type: "integer"
    description: ""
  - name: "deal_id"
    type: "integer"
    description: "The deal ID."
    foreign-key-id: "deal-id"
  - name: "field_value"
    type: "string"
    description: ""
  
---
