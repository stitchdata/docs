---
tap-reference: "listrak"

version: "1"

foreign-keys:
  - id: "contact-id"
    attribute: "ContactID"
    table: "subscribed_contacts"
    all-foreign-keys:
      - table: "message_bounces"
      - table: "message_clicks"
      - table: "message_opens"
      - table: "message_reads"
      - table: "message_unsubs"
      - table: "subscribed_contacts"

  - id: "message-id"
    attribute: "MsgID"
    table: "messages"
    all-foreign-keys:
      - table: "message_bounces"
      - table: "message_clicks"
      - table: "message_opens"
      - table: "message_reads"
      - table: "message_sends"
      - table: "message_unsubs"
      - table: "messages"

  - id: "list-id"
    attribute: "ListID"
    table: "lists"
    all-foreign-keys:
      - table: "lists"
      - table: "messages"
      - table: "subscribed_contacts"
---