---
tap: "clubspeed"
version: "1.0"

name: "gift_card_history"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/gift_card_history.json"
description: |
  The `{{ table.name }}` table acts as a transactional log for keeping track of each change that occurs with gift cards.

  {% capture replication-note %}
  **Note**: In {{ integration.display_name }}, each gift card is registered as a [`customer`](#customers). This means that each gift card identifier should be considered a `customerId` in this table.
  {% endcapture %}

  {% include note.html type="single-line" content=replication-note %}

replication-method: "Key-based Incremental"

attributes:
  - name: "giftCardHistoryId"
    type: "integer"
    primary-key: true
    description: "The gift card history ID."
    # foreign-key-id: "gift-card-history-id"

  - name: "transactionDate"
    type: "date-time"
    replication-key: true
    description: "The date at which the transaction occurred."

  - name: "checkDetailId"
    type: "integer"
    description: "The check line item that resulted in this change."
    foreign-key-id: "check-detail-id"

  - name: "checkId"
    type: "integer"
    description: "The check which resulted in this change."
    foreign-key-id: "check-id"

  - name: "customerId"
    type: "integer"
    description: "The holder of the gift card. **Note**: This may correspond to either a standard gift card or a member card on a customer account."
    foreign-key-id: "customer-id"

  - name: "ipAddress"
    type: "string"
    description: "The IP address of the machine from which the change originated."

  - name: "notes"
    type: "string"
    description: "Any notes for the transaction."

  - name: "points"
    type: "number"
    description: "The number of changed points for this transaction."

  - name: "type"
    type: "integer"
    description: |
      The type of the transaction. Possible values are:

      - `0` - Sold gift card
      - `1` - Transferred gift card in
      - `9` - Void sold gift card
      - `10` - Paid with gift card
      - `11` - Void paid with gift card
      - `12` - Refunded to gift card
      - `13` - Sold gift card external
      - `14` - Void sold gift card external
      - `15` - Paid with gift card external
      - `16` - Void paid with gift card external
      - `17` - Refunded to gift card external
      - `18` - Invoice paid

  - name: "userId"
    type: "integer"
    description: "The ID of the user that recorded the transaction."
    foreign-key-id: "user-id"
---