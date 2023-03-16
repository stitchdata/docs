---
tap: "activecampaign"
version: "0.3"
key: ""

name: "contact_custom_field_values"
doc-link: "https://developers.activecampaign.com/reference#fieldvalues"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/contact_custom_field_values.json"
description: |
  The `{{ table.name }}` table contains information about custom field values for your contacts in your {{ integration.display_name }} account.
  
replication-method: "Key-based Incremental"

api-method:
    name: "List all custom field values"
    doc-link: "https://developers.activecampaign.com/reference#list-all-custom-field-values-1"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The contact custom field value ID."
    #foreign-key-id: "contact-custom-field-value-id"

  - name: "udate"
    type: "date-time"
    description: "The custom field value's udate."
    replication-key: true

  - name: "cdate"
    type: "date-time"
    description: ""
  - name: "contact"
    type: "integer"
    description: "The contact ID."
    foreign-key-id: "contact-id"
  - name: "created_by"
    type: "integer"
    description: ""
  - name: "field"
    type: "integer"
    description: ""
  
  - name: "owner"
    type: "integer"
    description: ""
  
  - name: "updated_by"
    type: "integer"
    description: ""
  - name: "value"
    type: "string"
    description: ""
---
