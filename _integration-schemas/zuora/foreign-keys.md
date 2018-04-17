---
tap-reference: "zuora"

version: "1.0"

foreign-keys:
  - attribute: "accountId"
    table: "account"
    join-on: "id"

  - attribute: "accountingCodeId"
    table: "accountingCode"
    join-on: "id"

  - attribute: "accountingPeriodId"
    table: "accountingPeriod"
    join-on: "id"

  - attribute: "accountReceivableAccountingCodeId"
    table: "accountingCode"
    join-on: "Id"

  - attribute: "amendmentId"
    table: "amendment"
    join-on: "id"

  - attribute: "billingRunId"
    table: "billingRun"
    join-on: "id"

  - attribute: "billToContactId"
    table: "contact"
    join-on: "id"

  - attribute: "billToContactSnapshotId"
    table: "contactSnapshot"
    join-on: "id"

  - attribute: "cashOnAccountAccountingCodeId"
    table: "accountingCode"
    join-on: "id"

  - attribute: "contactId"
    table: "contact"
    join-on: "id"

  - attribute: "communicationProfileId"
    table: "communicationProfile"
    join-on: "id"

  - attribute: "creatorInvoiceOwnerId"
    table: "account"
    join-on: "id"

  - attribute: "defaultPaymentMethodId"
    table: "paymentMethod"
    join-on: "id"

  - attribute: "discountRatePlanChargeId"
    table: "ratePlanCharge"
    join-on: "id"

  - attribute: "invoiceId"
    table: "invoice"
    join-on: "id"

  - attribute: "invoiceOwnerId"
    table: "account"
    join-on: "id"

  - attribute: "invoiceItemId"
    table: "invoiceItem"
    join-on: "id"

  - attribute: "journalEntryId"
    table: "journalEntry"
    join-on: "id"

  - attribute: "journalRunId"
    table: "journalRun"
    join-on: "id"

  - attribute: "parentAccountId"
    table: "account"
    join-on: "parentAccountId"

  - attribute: "paymentId"
    table: "payment"
    join-on: "id"

  - attribute: "paymentMethodId"
    table: "paymentMethod"
    join-on: "id"

  - attribute: "paymentRunId"
    table: "paymentRun"
    join-on: "id"

  - attribute: "productId"
    table: "product"
    join-on: "id"

  - attribute: "productRatePlanChargeId"
    table: "productRatePlanCharge"
    join-on: "id"

  - attribute: "productRatePlanId"
    table: "productRatePlan"
    join-on: "id"

  - attribute: "ratePlanChargeId"
    table: "ratePlanCharge"
    join-on: "id"

  - attribute: "ratePlanId"
    table: "ratePlan"
    join-on: "id"

  - attribute: "recognizedRevenueAccountingCodeId"
    table: "accountingCode"
    join-on: "id"

  - attribute: "refundId"
    table: "refund"
    join-on: "id"

  - attribute: "salesTaxPayableAccountingCodeId"
    table: "accountingCode"
    join-on: "id"

  - attribute: "soldToContactId"
    table: "contact"
    join-on: "id"

  - attribute: "soldToContactSnapshotId"
    table: "contactSnapshot"
    join-on: "id"

  - attribute: "sourceTransactionId"
    table: ""
    join-on: ""

  - attribute: "subscriptionId"
    table: "subscription"
    join-on: "id"

  - attribute: "usageId"
    table: "usage"
    join-on: "id"
---