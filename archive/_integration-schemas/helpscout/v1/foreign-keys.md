---
tap-reference: "helpscout"

version: "1"

foreign-keys:
  - id: "conversation-id"
    attribute: "conversation_id"
    table: "conversations"
    all-foreign-keys:
      - table: "conversation_threads"
      - table: "conversations"
        join-on: "id"

  - id: "customer-id"
    attribute: "id"
    table: "customers"
    all-foreign-keys:
      - table: "conversation_threads"
        subattribute: "customer"
      - table: "conversations"
        subattribute: "primary_customer"
      - table: "customers"

  - id: "mailbox-folder-id"
    attribute: "folder_id"
    table: "mailbox_folders"
    all-foreign-keys:
      - table: "conversations"
      - table: "mailbox_folders"
        join-on: "id"

  - id: "mailbox-id"
    attribute: "mailbox_id"
    table: "mailboxes"
    all-foreign-keys:
      - table: "conversations"
      - table: "mailbox_fields"
      - table: "mailbox_folders"
      - table: "mailboxes"
        join-on: "id"
      - table: "wofkflows"

  - id: "user-id"
    attribute: "id"
    table: "users"
    all-foreign-keys:
      - table: "conversation_threads"
        subattribute: "assigned_to"
      - table: "conversation_threads"
        subattribute: "created_by"
      - table: "conversations"
        subattribute: "assignee"
      - table: "conversations"
        join-on: "closed_by"
      - table: "conversations"
        subattribute: "created_by"
      - table: "users"
---