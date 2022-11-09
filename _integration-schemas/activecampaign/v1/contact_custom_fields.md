---
tap: "activecampaign"
version: "0.3"
key: ""

name: "contact_custom_fields"
doc-link: "https://developers.activecampaign.com/reference#fields"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/contact_custom_fields.json"
description: |
  The `{{ table.name }}` table contains information about custom fields for your contacts in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: "List all custom fields"
    doc-link: "https://developers.activecampaign.com/reference#retrieve-fields-1"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The contact custom field ID."
    #foreign-key-id: "contact-custom-field-id"

  - name: "cdate"
    type: "date-time"
    description: ""
  - name: "cols"
    type: "integer"
    description: ""
  - name: "defval"
    type: "string"
    description: ""
  - name: "descript"
    type: "string"
    description: ""
  
  - name: "isrequired"
    type: "integer"
    description: ""
  - name: "ordernum"
    type: "integer"
    description: ""
  - name: "perstag"
    type: "string"
    description: ""
  - name: "rows"
    type: "integer"
    description: ""
  - name: "service"
    type: "string"
    description: ""
  - name: "show_in_list"
    type: "integer"
    description: ""
  - name: "title"
    type: "string"
    description: ""
  - name: "type"
    type: "string"
    description: ""
  - name: "udate"
    type: "date-time"
    description: ""
  - name: "visible"
    type: "integer"
    description: ""
---
