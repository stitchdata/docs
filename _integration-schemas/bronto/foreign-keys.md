---
tap-reference: "bronto"

# version: "1.0"

foreign-keys:
  - id: "contact-id"
    attribute: "contactId"
    table: "contact"
    join-on: "id"
    all-foreign-keys:
      - table: "contact"
        join-on: "id"
      - table: "inbound_activity"
      - table: "outbound_activity"

  - id: "delivery-id"
    attribute: "deliveryId"
    table: ""
    join-on: ""
    all-foreign-keys:
      - table: "inbound_activity"
      - table: "outbound_activity"


  - id: "list-id"
    attribute: "listId"
    table: "list"
    join-on: "id"
    all-foreign-keys:
      - table: "list"
        join-on: "id"
      # - table: "contacts__listIds"
      #   join-on: "value"
      - table: "inbound_activity"
      - table: "outbound_activity"

  - id: "inbound-activity-id"
    attribute: ""
    table: "inbound_activity"
    join-on: "id"
    all-foreign-keys:
      - table: "inbound_activity"
        join-on: "id"

  - id: "keyword-id"
    attribute: "keywordId"
    table: ""
    join-on: ""
    all-foreign-keys:
      # - table: "contact__SMSKeywordIDs"
      #   join-on: "SMSKeywordID"
      - table: "inbound_activity"
      - table: "outbound_activity"

  - id: "message-id"
    attribute: "messageId"
    table: ""
    join-on: ""
    all-foreign-keys:
      - table: "inbound_activity"
      - table: "outbound_activity"

  - id: "order-id"
    attribute: "orderId"
    table: ""
    join-on: ""
    all-foreign-keys:
      - table: "inbound_activity"
      - table: "outbound_activity"

  - id: "outbound-activity-id"
    attribute: ""
    table: "outbound_activity"
    join-on: "id"
    all-foreign-keys:
      - table: "outbound_activity"
        join-on: "id"

  - id: "segment-id"
    attribute: "segmentId"
    table: ""
    join-on: ""
    all-foreign-keys:
      - table: "inbound_activity"
      - table: "outbound_activity"

  - id: "workflow-id"
    attribute: "workflowId"
    table: ""
    join-on: ""
    all-foreign-keys:
      - table: "inbound_activity"
      - table: "outbound_activity"
---