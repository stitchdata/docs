---
tap-reference: "zuora"

version: "1.0"

foreign-keys:
  - attribute: "accountId"
    table: "account"
    join-on: "id"
    link: true

  - attribute: "accountingCodeId"
    table: "accountingCode"
    join-on: "id"

  - attribute: "accountingPeriod"
    table: "accountingPeriod"
    join-on: "id"

  - attribute: "accountReceivableAccountingCodeId"
    table: ""
    join-on: ""

  - attribute: "amendmentId"
    table: "amendment"
    join-on: "id"

  - attribute: "billingRunId"
    table: "billingRun"
    join-on: "id"

  - attribute: "billToContactId"
    table: "contact"
    join-on: "id"
    link: true

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

  - attribute: "invoiceId"
    table: "invoice"
    join-on: "id"

  - attribute: "invoiceOwnerId"
    table: "account"
    join-on: "id"

  - attribute: "invoiceTemplateId"
    table: ""
    join-on: ""

  - attribute: "journalEntryId"
    table: "journalEntry"
    join-on: "id"

  - attribute: "journalRunId"
    table: "journalRun"
    join-on: "id"

  - attribute: "parentAccountId"
    table: "account"
    join-on: "parentAccountId"
    link: true

  - attribute: "paymentId"
    table: "payment"
    join-on: "id"
    link: true

  - attribute: "paymentMethodId"
    table: "paymentMethod"
    join-on: "id"

  - attribute: "productId"
    table: "product"
    join-on: "id"
    link: true

  - attribute: "productRatePlanChargeId"
    table: "productRatePlanCharge"
    join-on: "id"

  - attribute: "productRatePlanId"
    table: "productRatePlan"
    join-on: "id"
    link: true

  - attribute: "ratePlanChargeId"
    table: "ratePlanCharge"
    join-on: "id"

  - attribute: "ratePlanId"
    table: "ratePlan"
    join-on: "id"
    link: true

  - attribute: "referenceId"
    table: ""
    join-on: ""

  - attribute: "refundId"
    table: "refund"
    join-on: "id"

  - attribute: "soldToContactId"
    table: "contact"
    join-on: "id"
    link: true

  - attribute: "sourceTransactionId"
    table: ""
    join-on: ""

  - attribute: "subscriptionId"
    table: "subscription"
    join-on: "id"
    link: true
---