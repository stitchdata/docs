---
tap: "zuora"
version: "1"

name: "refund"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/Refunds
description: |
  The `{{ table.name }}` table contains info about refunds, or transactions where money is returned to a customer.

replication-method: "Key-based Incremental"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The refund ID."
    foreign-key-id: "refund-id"

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the refund was last updated."

  - name: "accountId"
    type: "string"
    description: "The ID of the account associated with the refund."
    foreign-key-id: "account-id"

  - name: "amount"
    type: "number"
    description: "The total amount of the refund."

  - name: "billToContactId"
    type: "string"
    description: "The ID of the billing contact for the associated account."
    foreign-key-id: "bill-to-contact-id"

  - name: "cancelledOn"
    type: "date-time"
    description: "The date when the refund was canceled."

  - name: "comment"
    type: "string"
    description: "The comments about the refund."

  - name: "createdById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who created the refund."

  - name: "createdDate"
    type: "date-time"
    description: "The date the refund was created."

  - name: "creditMemoId"
    type: "string"
    description: "The ID of the credit memo that is refunded."
    # foreign-key-id: "credit-memo-id"

  - name: "defaultPaymentMethodId"
    type: "string"
    description: "The ID of the default payment method for the associated account."
    foreign-key-id: "default-payment-method-id"

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in {{ integration.display_name }}.

  - name: "gatewayId"
    type: "string"
    description: "The ID of the gateway instance that processes the refund."

  - name: "gatewayResponse"
    type: "string"
    description: "The message returned from the payment gateway for the refund."

  - name: "gatewayResponseCode"
    type: "string"
    description: "The code returned from the payment gateway for the refund."

  - name: "gatewayState"
    type: "string"
    description: |
      The status of the refund in the gateway. Possible values are:

      - `MarkedForSubmission`
      - `Submitted`
      - `Settled`
      - `NotSubmitted`
      - `FailedToSettle`

  - name: "markedForSubmissionOn"
    type: "date-time"
    description: "The date when a refund was marked and waiting for batch submission to the payment process."

  - name: "methodType"
    type: "string"
    description: |
      The method used to issue an external refund to a customer. Possible values are:

      - `ACH`
      - `Cash`
      - `Check`
      - `CreditCard`
      - `PayPal`
      - `WireTransfer`
      - `DebitCard`
      - `CreditCardReferenceTransaction`
      - `BankTransfer`
      - `Other`

  - name: "number"
    type: "string"
    description: "The unique identification number of the refund."

  - name: "parentAccountId"
    type: "string"
    description: "The ID of the parent customer account for the associated account. This field is used when customer hierarchy is enabled in {{ integration.display_name }}."
    foreign-key-id: "parent-account-id"

  - name: "paymentId"
    type: "string"
    description: "The ID of the payment that is refunded."
    foreign-key-id: "pamyent-id"

  - name: "paymentMethodId"
    type: "string"
    description: "The unique ID of the payment method that the customer used to make the refund."
    foreign-key-id: "payment-method-id"

  - name: "paymentMethodSnapshotId"
    type: "string"
    description: "The unqiue ID of the payment method snapshot, which is a copy of the particular payment method used in a transaction."
    # foreign-key-id: "payment-method-snapshot-id"

  - name: "reasonCode"
    type: "string"
    description: "The code identifying the reason for the transaction."

  - name: "referenceId"
    type: "string"
    description: "The transaction ID returned by the payment gateway for an electronic refund."
    # foreign-key-id: "reference-id"

  - name: "refundDate"
    type: "date-time"
    description: "The date when the refund takes effect."

  - name: "refundTransactionTime"
    type: "date-time"
    description: "The date when the refund was issued."

  - name: "secondRefundReferenceId"
    type: "string"
    description: "The transaction ID returned by the payment gateway if there is an additional transaction for the refund."

  - name: "settledOn"
    type: "date-time"
    description: "The date when the refund was settled in the payment processor. This field is only applicable to Spectrum gateways."

  - name: "softDescriptor"
    type: "string"
    description: "A payment gateway-specific field that maps {{ integration.display_name }} to other gateways."

  - name: "softDescriptorPhone"
    type: "string"
    description: "A payment gateway-specific field that maps {{ integration.display_name }} to other gateways."

  - name: "soldToContactId"
    type: "string"
    description: "The ID of the person who bought the subscription associated with the account."
    foreign-key-id: "sold-to-contact-id"

  - name: "status"
    type: "string"
    description: |
      The status of the refund. Possible values are:

      - `Processed`
      - `Canceled`
      - `Error`
      - `Processing`

  - name: "submittedOn"
    type: "date-time"
    description: "The date when the refund was submitted."

  - name: "success"
    type: "boolean"
    description: "If `true`, the request was processed successfully."

  - name: "type"
    type: "string"
    description: "The type of refund, either `External` or `Electronic`."

  - name: "updatedById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who last updated the refund."
---