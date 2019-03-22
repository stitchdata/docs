---
tap: "sendgrid-core"
version: "1.0"

name: "contacts"
doc-link: https://sendgrid.com/docs/API_Reference/Web_API_v3/Marketing_Campaigns/contactdb.html#Get-Recipients-Matching-Search-Criteria-GET
singer-schema: https://github.com/singer-io/tap-sendgrid/blob/master/tap_sendgrid/schemas/contacts.json
description: |
  The `{{ table.name }}` table contains info about the contacts in your SendGrid account.

  #### Contact custom fields

  Stitch's {{ integration.display_name }} integration will replicate any custom fields associated with contact records.

replication-method: "Key-based Incremental"

replication-key:
  name: "timestamp"

api-method:
  name: "List recipients"
  doc-link: "https://sendgrid.com/docs/API_Reference/Web_API_v3/Marketing_Campaigns/contactdb.html#Get-Recipients-Matching-Search-Criteria-GET" 

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The contact ID."
    # foreign-key-id: "contact-id"

  - name: "created_at"
    type: "integer"
    description: "The Unix timestamp of the time the contact was created."

  - name: "updated_at"
    type: "integer"
    description: "The Unix timestamp of the last time the contact was updated."

  - name: "email"
    type: "string"
    description: "The email address associated with the contact."
    foreign-key-id: "email-id"

  - name: "last_emailed"
    type: "integer"
    description: "The Unix timestamp of the last time the contact was emailed."

  - name: "last_clicked"
    type: "integer"
    description: "The Unix timestamp of the last time the contact clicked on an email."

  - name: "last_opened"
    type: "integer"
    description: "The Unix timestamp of the last time the contact opened an email."

  - name: "first_name"
    type: "string"
    description: "The first name of the contact."

  - name: "last_name"
    type: "string"
    description: "The last name of the contact."

  - name: "custom_fields"
    type: "array"
    description: "The custom fields associated with the contact."
    subattributes:
      - name: "[field_name]"
        type: "varies"
        description: |
          The custom field associated with the contact, where `[field_name]` is the name of the field in SendGrid.

          The data type of this field will vary and depends on the type in SendGrid. For example: If this is a text field in SendGrid the field will be a `STRING`.
---