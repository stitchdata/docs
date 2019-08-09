---
tap-reference: "salesforce-marketing-cloud"

version: "1.0"

foreign-keys:
  - id: "campaign-id"
    attribute: ""
    table: "campaign"
    all-foreign-keys:
      - table: "campaign"
        join-on: "ID"

  - id: "content-area-id"
    attribute: ""
    table: "content_area"
    all-foreign-keys:
      - table: "content_area"
        join-on: "ID"
      - table: "email"
        subtable: "ContentAreaIDs"
        join-on: "value"

  - id: "email-id"
    attribute: "EmailID"
    table: "email"
    all-foreign-keys:
      - table: "email"
        join-on: "ID"
      - table: "email"
        join-on: "ClonedFromID"
      - table: "send"

  - id: "folder-id"
    attribute: "CategoryID"
    table: "folder"
    all-foreign-keys:
      - table: "content_area"
      - table: "email"
      - table: "folder"
        join-on: "ID"
      - table: "folder"
        join-on: "ParentFolder"
      - table: "list"
        join-on: "Category"

  - id: "list-id"
    attribute: "ListID"
    table: "list"
    all-foreign-keys:
      - table: "list"
        join-on: "ID"
      - table: "list_send"
      - table: "list_subscriber"
      - table: "subscriber"
        subtable: "ListIDs"
        join-on: "value"

  - id: "send-id"
    attribute: "SendID"
    table: "event"
    all-foreign-keys:
      - table: "event"
      - table: "list_send"
      - table: "send"
        join-on: "ID"
      
  - id: "subscriber-key"
    attribute: "SubscriberKey"
    table: "subscriber"
    all-foreign-keys:
      - table: "event"
      - table: "list_subscriber"
      - table: "subscriber"
        join-on: "ID"
--- 