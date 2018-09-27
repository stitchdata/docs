---
tap: "sendgrid-core"

name: "lists_members"
doc-link: 
singer-schema: https://github.com/singer-io/tap-sendgrid/blob/master/tap_sendgrid/schemas/lists_members.json
description: |
  The `lists_members` table contains info about members of your lists.

  #### List member custom fields

  Stitch's {{ integration.display_name }} integration will replicate any custom fields associated with list member records.

replication-method: "Full Table"

api-method:
  name: "List all list recipients"
  doc-link: "https://sendgrid.com/docs/API_Reference/Web_API_v3/Marketing_Campaigns/contactdb.html#List-Recipients-on-a-List-GET"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The ID of the list member."
    # foreign-key-id: "list-member-id"

  - name: "created_at"
    type: "integer"
    description: "The Unix timestamp of the time the list member was added to the list."

  - name: "updated_at"
    type: "integer"
    description: "The Unix timestamp of the last time the list member was updated."

  - name: "email"
    type: "string"
    description: "The email address of the list member."
    foreign-key-id: "email-id"

  - name: "list_id"
    type: "integer"
    description: "The ID of the list the member belongs to."
    foreign-key-id: "list-id"

  - name: "last_emailed"
    type: "integer"
    description: "The Unix timestamp of the last time the list member was emailed by one of your campaigns."

  - name: "last_clicked"
    type: "integer"
    description: "The Unix timestamp of the last time the list member clicked a link from one of your campaigns."

  - name: "last_opened"
    type: "integer"
    description: "The Unix timestamp of the last time the list member last opened an email from one of your campaigns."

  - name: "first_name"
    type: "string"
    description: "The first name of the list member."

  - name: "last_name"
    type: "string"
    description: "The last name of the list member."

  - name: "custom_fields"
    type: "array"
    description: "The custom fields associated with the list member."
    array-attributes:
      - name: "[field_name]"
        type: "varies"
        description: |
          The custom field associated with the list member, where `[field_name]` is the name of the field in SendGrid.

          The data type of this field will vary and depends on the type in SendGrid. For example: If this is a text field in SendGrid the field will be a `STRING`.
---