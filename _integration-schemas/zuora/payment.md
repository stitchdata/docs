---
tap: "zuora"
version: 1.0

name: "payment"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/Payments
description: |
  The `payment` table contains info about customer payments.

replication-method: "Key-based Incremental"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The payment ID."

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the payment was last updated."

  - name: "accountId"
    type: "string"
    description: "The ID of the account associated with the payment."
    foreign-key: true
    ## foreign-keys:
    ##   - table-name: "account"
    ##     attribute: "id"

    ##   - table-name: "contact"
    ##     attribute: "accountId"

    ##   - table-name: "invoice"
    ##     attribute: "accountId"

    ##   - table-name: "refund"
    ##     attribute: "accountId"

    ##   - table-name: "subscription"
    ##     attribute: "accountId"

  - name: "amount"
    type: "number"
    description: "The total amount of the payment."

  - name: "appliedAmount"
    type: "string"
    description: "The applied amount of the payment."

  - name: "authTransactionId"
    type: "string"
    description: "The authorization transaction ID from the payment gateway."

  - name: "bankIdentificationNumber"
    type: "string"
    description: "The first six digits of the credit or debit card used for the payment, when applicable."

  - name: "cancelledOn"
    type: "date-time"
    description: "The date when the payment was cancelled."

  - name: "comment"
    type: "string"
    description: "The comments about the payment."

  - name: "createdById"
    type: "string"
    description: "The ID of the Zuora user who created the payment."

  - name: "createdDate"
    type: "date-time"
    description: "The date the payment was created."

  - name: "creditBalanceAmount"
    type: "number"
    description: "The amount that the payment transfers to the credit balance."

  - name: "currency"
    type: "string"
    description: "The currency the payment was in."

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in Zuora.

  - name: "effectiveDate"
    type: "date-time"
    description: "The date when the payment takes effect."

  - name: "gatewayId"
    type: "string"
    description: "The ID of the gateway instance that processes the payment."

  - name: "gatewayResponse"
    type: "string"
    description: "The message returned from the payment gateway for the payment."

  - name: "gatewayResponseCode"
    type: "string"
    description: "The code returned from the payment gateway for the payment."

  - name: "gatewayState"
    type: "string"
    description: |
      The status of the payment in the gateway. Possible values are:

      - `MarkedForSubmission`
      - `Submitted`
      - `Settled`
      - `NotSubmitted`
      - `FailedToSettle`

  - name: "markedForSubmissionOn"
    type: "date-time"
    description: "The date when a payment was marked and waiting for batch submission to the payment process."

  - name: "number"
    type: "string"
    description: "The unique identification number of the payment."

  - name: "paymentDate"
    type: "date-time"
    description: "The date when the payment takes effect."

  - name: "paymentId"
    type: "string"
    description: "The ID of the payment that is paymented."
    foreign-key: true
    ## foreign-keys:
    ##   - table-name: "payment"
    ##     attribute: "id"

  - name: "paymentMethodId"
    type: "string"
    description: "The unique ID of the payment method that the customer used to make the payment."
    foreign-key: true
    ## foreign-keys:
    ##   - table-name: "paymentMethod"
    ##     attribute: "id"

  - name: "paymentMethodSnapshotId"
    type: "string"
    description: "The unqiue ID of the payment method snapshot, which is a copy of the particular payment method used in a transaction."
    foreign-key: true
    ## foreign-keys:
    ##   - table-name: "paymentMethodSnapshot"
    ##     attribute: "id"

  - name: "paymentTransactionTime"
    type: "date-time"
    description: "The date when the payment was issued."

  - name: "referenceId"
    type: "string"
    description: "The transaction ID returned by the payment gateway for an electronic payment."

  - name: "refundAmount"
    type: "number"
    description: "The amount of the payment that is refunded, if applicable."

  - name: "secondpaymentReferenceId"
    type: "string"
    description: "The transaction ID returned by the payment gateway if there is an additional transaction for the payment."

  - name: "settledOn"
    type: "date-time"
    description: "The date when the payment was settled in the payment processor. This field is only applicable to Spectrum gateways."

  - name: "softDescriptor"
    type: "string"
    description: "A payment gateway-specific field that maps Zuora to other gateways."

  - name: "softDescriptorPhone"
    type: "string"
    description: "A payment gateway-specific field that maps Zuora to other gateways."

  - name: "status"
    type: "string"
    description: |
      The status of the payment. Possible values are:

      - `Processed`
      - `Canceled`
      - `Error`
      - `Processing`

  - name: "submittedOn"
    type: "date-time"
    description: "The date when the payment was submitted."

  - name: "success"
    type: "boolean"
    description: "If `true`, the request was processed successfully."

  - name: "type"
    type: "string"
    description: "The type of payment, either `External` or `Electronic`."

  - name: "unappliedAmount"
    type: "number"
    description: "The unapplied amount of the payment."

  - name: "updatedById"
    type: "string"
    description: "The ID of the Zuora user who last updated the payment."

---