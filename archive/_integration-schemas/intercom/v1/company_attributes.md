---
tap: "intercom"
version: "1"
key: "company-attribute"

name: "company_attributes"
doc-link: "https://developers.intercom.com/intercom-api-reference/v2.0/reference#data-attribute-model"
singer-schema: "https://github.com/singer-io/tap-intercom/blob/master/tap_intercom/schemas/company_attributes.json"
description: |
  The `{{ table.name }}` lists data attributes for a specified company in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "List all data attributes"
  doc-link: "https://developers.intercom.com/intercom-api-reference/v2.0/reference#list-data-attributes"

attributes:
  - name: "name"
    type: "string"
    primary-key: true
    description: "The name of the attribute."
    foreign-key-id: "attribute-name"

  - name: "admin_id"
    type: "integer"
    description: "The ID of the admin that created the attribute."
    foreign-key-id: "admin-id"

  - name: "api_writable"
    type: "boolean"
    description: "Indicates if the attribute can be updated via {{ integration.display_name }}'s API."

  - name: "archived"
    type: "boolean"
    description: "Indicates if the attribute is archived."

  - name: "created_at"
    type: "date-time"
    description: "The time the attribute was created."

  - name: "custom"
    type: "boolean"
    description: ""

  - name: "data_type"
    type: "string"
    description: |
      The type of data stored for the attribute. Possible values are:

      - `string`
      - `fixnum`
      - `float`
      - `boolean`
      - `date`
      - `options`

  - name: "description"
    type: "string"
    description: "The description for the attribute."

  - name: "full_name"
    type: "string"
    description: ""

  - name: "label"
    type: "string"
    description: "The name of the attribute."

  - name: "options"
    type: "array"
    description: "The pre-defined options for the attribute."
    subattributes:
      - name: "value"
        type: "varies"
        description: ""
  
  - name: "type"
    type: "string"
    description: "This will be `data_attribute`."

  - name: "ui_writable"
    type: "boolean"
    description: "Indicates if the attribute can be updated via {{ integration.display_name }}'s UI."

  - name: "updated_at"
    type: "date-time"
    description: "The last time the attribute was updated."
---