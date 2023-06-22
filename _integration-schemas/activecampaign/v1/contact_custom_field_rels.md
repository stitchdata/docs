---
tap: "activecampaign"
version: "1"
key: ""

name: "contact_custom_field_rels"
doc-link: "https://developers.activecampaign.com/reference#fields"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/contact_custom_fields.json"
description: |
  The `{{ table.name }}` table contains information about custom field relationships for your contacts in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: "List all custom fields"
    doc-link: "https://developers.activecampaign.com/reference#retrieve-fields-1"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The contact custom field relationship ID."
    #foreign-key-id: "contact-custom-field-rel-id"

  - name: "cdate"
    type: "date-time"
    description: ""
  - name: "dorder"
    type: "integer"
    description: ""
  - name: "field"
    type: "integer"
    description: ""
  
  - name: "relid"
    type: "integer"
    description: ""
---
