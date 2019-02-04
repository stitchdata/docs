---
tap: "clubspeed"
version: "1.0"

name: "payments"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/payments.json"
description: |
  The `{{ table.name }}` table contains info about collected payments.

replication-method: "Key-based Incremental"

attributes:
  - name: "paymentId"
    type: "integer"
    primary-key: true
    description: "The payment ID."
    foreign-key-id: "payment-id"

  - name: "payDate"
    type: "date-time"
    replication-key: true
    description: "The timestamp at which the payment was collected."

  - name: "cardType"
    type: "string"
    description: "The type of credit card used to make the payment. This will usually be populated only if `payType` is `Credit`."

  - name: "checkId"
    type: "integer"
    description: "The ID of the check for which payment was applied."
    foreign-key-id: "check-id"

  - name: "customerId"
    type: "integer"
    description: "The ID of the customer that made the payment."
    foreign-key-id: "customer-id"

  - name: "extCardType"
    type: "string"
    description: "The card or payment processor type for the payment."

  - name: "payAmount"
    type: "number"
    description: "The monetary amount of the payment."

  - name: "payStatus"
    type: "integer"
    description: |
      The status of the payment. Possible values are:

      - `1` - Paid
      - `2` - Void

  - name: "payTax"
    type: "number"
    description: "The monetary amount of the payment which was applied to tax. **Note**: `payAmount` is inclusive of this value."

  - name: "payTerminal"
    type: "string"
    description: "The terminal at which the payment was collected."

  - name: "payType"
    type: "integer"
    description: |
      The type of the payment which was collected. Possible values are:

      - `1` - Cash
      - `2` - Credit
      - `3` - External / Third Party Processor
      - `4` - Gift Card
      - `5` - Voucher
      - `6` - Complementary

  - name: "transaction"
    type: "string"
    description: "A reference to a transaction number, typically one which was returned from a third party processor."

  - name: "userId"
    type: "integer"
    description: "The ID of the user that created the payment."
    foreign-key-id: "user-id"

  - name: "voidDate"
    type: "date-time"
    description: "The timestamp at which the payment was voided."

  - name: "voidNotes"
    type: "string"
    description: "The notes as to why the payment was voided."

  - name: "voidTerminal"
    type: "string"
    description: "The terminal where the payment was voided."

  - name: "voidUser"
    type: "integer"
    description: "The ID of the user that voided the payment."
    foreign-key-id: "user-id"
---