---
tap: "sendgrid-core"

name: "segments_members"
doc-link: 
singer-schema: https://github.com/singer-io/tap-sendgrid/blob/master/tap_sendgrid/schemas/segments_members.json
description: |
  The `segments_members` table contains info about the members of your segments.

  #### Segment member custom fields

  Stitch's {{ integration.display_name }} integration will replicate any custom fields associated with segment member records.

replication-method: "Full Table"

api-method:
  name: "List recipients on a segment"
  doc-link: "https://sendgrid.com/docs/API_Reference/Web_API_v3/Marketing_Campaigns/contactdb.html#List-Recipients-On-a-Segment-GET"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The ID of the segment member."
    # foreign-key-id: "segment-member-id"

  - name: "created_at"
    type: "integer"
    description: "The Unix timestamp of the time the segment member was added to the segment."

  - name: "updated_at"
    type: "integer"
    description: "The Unix timestamp of the last time the segment member was updated."

  - name: "email"
    type: "string"
    description: "The email address of the segment member."
    foreign-key-id: "email-id"

  - name: "segment_id"
    type: "integer"
    description: "The ID of the segment the member belongs to."
    foreign-key-id: "segment-id"

  - name: "last_emailed"
    type: "integer"
    description: "The Unix timestamp of the last time the segment member was emailed by one of your campaigns."

  - name: "last_clicked"
    type: "integer"
    description: "The Unix timestamp of the last time the segment member clicked a link from one of your campaigns."

  - name: "last_opened"
    type: "integer"
    description: "The Unix timestamp of the last time the segment member last opened an email from one of your campaigns."

  - name: "first_name"
    type: "string"
    description: "The first name of the segment member."

  - name: "last_name"
    type: "string"
    description: "The last name of the segment member."

  - name: "custom_fields"
    type: "array"
    description: "The custom fields associated with the segment member."
    subattributes:
      - name: "[field_name]"
        type: "varies"
        description: |
          The custom field associated with the segment member, where `[field_name]` is the name of the field in SendGrid.

          The data type of this field will vary and depends on the type in SendGrid. For example: If this is a text field in SendGrid the field will be a `STRING`.
---