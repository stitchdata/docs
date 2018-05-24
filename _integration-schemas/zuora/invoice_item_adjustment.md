---
tap: "zuora"
version: 1.0 

name: "invoiceItemAdjustment"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/Invoice-Items
description: |
  The `invoiceItemAdjustment` table contains info about adjustments applied to invoice line items.

replication-method: "Key-based Incremental"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The ID of the adjustment."

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the adjustment was last updated."

  - name: "accountId"
    type: "string"
    description: "The ID of the account associated with the adjustment."
    foreign-key: true

  - name: "accountingCode"
    type: "string"
    description: "The accounting code for the invoice item."

  - name: "accountingPeriodId"
    type: "string"
    description: "The ID of the accounting period associated with the invoice."
    foreign-key: true

  - name: "accountReceivableAccountingCodeId"
    type: "string"
    description: "The ID of the accounts receivable accounting code associated with the invoice."
    foreign-key: true

  - name: "adjustmentDate"
    type: "date-time"
    description: "The date when the adjustment was applied."

  - name: "adjustmentNumber"
    type: "string"
    description: "A unique identifier for the adjustment."

  - name: "amendmentId"
    type: "string"
    description: "The ID of the amendment associated with the invoice item."
    foreign-key: true

  - name: "amount"
    type: "double"
    description: "The amount of the adjustment."

  - name: "billToContactId"
    type: "string"
    description: "The ID of the person to bill for the account."
    foreign-key: true

  - name: "cancelledById"
    type: "string"
    description: "The ID of the Zuora user who canceled the adjustment."

  - name: "cancelledDate"
    type: "date-time"
    description: "The date when the adjustment was canceled."

  - name: "comment"
    type: "string"
    description: "Comments about the adjustment."

  - name: "createdById"
    type: "string"
    description: "The ID of the Zuora user who created the adjustment."

  - name: "createdDate"
    type: "date-time"
    description: "The date the adjustment was created."

  - name: "customerName"
    type: "string"
    description: "The name of the account that owns the associated invoice."

  - name: "customerNumber"
    type: "string"
    description: "The unique account number of the customer's account."

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in Zuora.

  - name: "invoiceId"
    type: "string"
    description: "The ID of the invoice associated with the adjustment."
    foreign-key: true

  - name: "invoiceItemName"
    type: "string"
    description: "The name of the invoice item's charge."

  - name: "invoiceNumber"
    type: "string"
    description: "The unique ID for the invoice that contains the invoice item."

  - name: "journalEntryId"
    type: "string"
    description: "The journal entry ID associated with the adjustment."
    foreign-key: true

  - name: "journalRunId"
    type: "string"
    description: "The ID of the journal run associated with the adjustment."
    foreign-key: true

  - name: "parentAccountId"
    type: "string"
    description: "The ID of the parent customer account for this account. This field is used when customer hierarchy is enabled in Zuora."
    foreign-key: true

  - name: "productId"
    type: "string"
    description: "The ID of the product associated with the adjustment."
    foreign-key: true

  - name: "productRatePlanChargeId"
    type: "string"
    description: "The ID of the rate plan charge associated with the adjustment."
    foreign-key: true

  - name: "ratePlanChargeId"
    type: "string"
    description: "The ID of the rage plan charge that's associated with the adjustment."
    foreign-key: true

  - name: "ratePlanId"
    type: "string"
    description: "The ID of the rate plan associated with the adjustment."
    foreign-key: true

  - name: "reasonCode"
    type: "string"
    description: "Associates the adjustment with a specific revenue recognition code."

  - name: "recognizedRevenueAccountingCodeId"
    type: "date-time"
    description: "The ID of the accounting code used for recognized revenue."
    foreign-key: true

  - name: "referenceId"
    type: "string"
    description: "A code to reference an object external to Zuora."

  - name: "salesTaxPayableAccountingCodeId"
    type: "string"
    description: "The ID of the accounting code used for sales tax payable."
    foreign-key: true

  - name: "serviceEndDate"
    type: "date-time"
    description: "The end date of the service period associated with the adjustment. Service will end one second before the date in this value."

  - name: "serviceStartDate"
    type: "date-time"
    description: "The start date of the service period associated with the adjustment."

  - name: "soldToContactId"
    type: "string"
    description: "The ID of the person who bought the subscription associated with the account."
    foreign-key: true

  - name: "sourceId"
    type: "string"
    description: "The ID of the item specified in the `sourceType` field."

  - name: "sourceType"
    type: "string"
    description: "The type of adjustment. Possible values are `InvoiceDetail`, `Tax`"

  - name: "status"
    type: "string"
    description: |
      The status of the invoice item adjustment. Possible values are:

      - `Canceled`
      - `Processed`

  - name: "subscriptionId"
    type: "string"
    description: "The ID of the subscription associated with the adjustment."
    foreign-key: true

  - name: "taxationItemId"
    type: "string"
    description: "The ID of the associated taxation record."
    foreign-key: true

  - name: "transferredToAccounting"
    type: "string"
    description: |
      Indicates if the adjustment has been transferred to an external accounting system. Possible values are:

      - `Processing`
      - `Yes`
      - `Error`
      - `Ignore`

  - name: "updatedById"
    type: "string"
    description: "The ID of the Zuora user who last updated the adjustment."
---