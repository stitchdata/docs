---
tap: "shippo"

name: "transactions"
doc-link: https://goshippo.com/docs/reference#transactions
singer-schema: https://github.com/singer-io/tap-shippo/blob/master/tap_shippo/schemas/transactions.json
description: |
  The `transactions` table contains info about transactions, which are the purchases of shipping labels from a shipping provider for a specific service.

replication-method: "Key-based Incremental"
api-method:
  name: listAllTransactions
  doc-link: https://goshippo.com/docs/reference?version=2016-10-25#transactions-list

attributes:
  - name: "object_id"
    type: "string"
    primary-key: true
    description: "The transaction ID."

  - name: "object_updated"
    type: "date-time"
    description: "The time the transaction was last updated."

  - name: "object_state"
    type: "string"
    description: |
      Indicates the validity of the transaction based on the given data, regardless of what the carrier returns.

      Possible values include `VALID` and `INVALID`.

  - name: "object_status"
    type: "string"
    description: |
      The status of the transaction. Possible values:

      - `WAITING`
      - `QUEUED`
      - `SUCCESS`
      - `ERROR`
      - `REFUNDED`
      - `REFUNDPENDING`
      - `REFUNDREJECTED`

  - name: "object_created"
    type: "date-time"
    description: "The time the transaction was created."

  - name: "object_owner"
    type: "string"
    description: "The username of the user who created the transaction."

  - name: "test"
    type: "boolean"
    description: "Indicates if the transaction was created in test mode."

  - name: "rate"
    type: "string"
    description: "The ID of the rate object for which a label has to be obtained."

  - name: "tracking_number"
    type: "string"
    description: |
      The carrier-specific tracking number that can be used to track the shipment. A value will only be returned if:

      - The rate is for a trackable shipment, and
      - The transaction has been processed successfully.

  - name: "tracking_status"
    type: "object"
    description: "The latest tracking information for the shipment."
    object-attributes:
      - name: "value"
        type: "string"
        description: "The tracking status."

  - name: "tracking_history"
    type: "array"
    description: "A list of tracking events for the shipment the transaction is associated with."
    array-attributes:

  - name: "tracking_url_provider"
    type: "string"
    description: "The URL used to track the item on the carrier-provided tracking website."

  - name: "label_url"
    type: "string"
    description: "The URL for the label in the format defined in the account settings."

  - name: "commercial_invoice_url"
    type: "string"
    description: |
      The URL for the commercial invoice for this transaction as a PDF. Values are only returned if:
      
      - The transaction has been processed successfully, and
      - The shipment is international

  - name: "metadata"
    type: "string"
    description: "Additional information about the transaction."

  - name: "messages"
    type: "array"
    description: "Details about messages associated with the transaction."
    array-attributes:
      - name: "code"
        type: "string"
        description: "The ID of the message. This may not always be available."

      - name: "source"
        type: "string"
        description: "The source of the message."

      - name: "text"
        type: "string"
        description: "The text of the message."
---