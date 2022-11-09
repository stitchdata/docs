---
tap: "activecampaign"
version: "0.3"
key: ""

name: "contact_custom_field_options"
doc-link: "https://developers.activecampaign.com/reference#fields"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/contact_custom_fields.json"
description: |
  The `{{ table.name }}` table contains information about custom field options for your contacts in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: "List all custom fields"
    doc-link: "https://developers.activecampaign.com/reference#retrieve-fields-1"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The contact custom field option ID."
    #foreign-key-id: "contact-custom-field-option-id"

  - name: "cdate"
    type: "date-time"
    description: ""
  - name: "field"
    type: "integer"
    description: ""
  
  - name: "isdefault"
    type: "integer"
    description: ""
  - name: "label"
    type: "string"
    description: ""
  - name: "orderid"
    type: "integer"
    description: "The order ID."
    foreign-key-id: "order-id"
  - name: "udate"
    type: "date-time"
    description: ""
  - name: "value"
    type: "string"
    description: ""
---
