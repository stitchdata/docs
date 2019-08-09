---
tap: "netsuite"
version: "1.0"

name: "Vendor"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/vendor.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Vendor.json"
description: |
  The `{{ table.name }}` table contains info about the vendors in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "vendor"

replication-method: "Key-based Incremental"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "vendor-id"

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "accountNumber"
    type: "string"
    description: ""

  - name: "addressbookList"
    type: "varies"
    description: ""

  - name: "altEmail"
    type: "string"
    description: ""

  - name: "altName"
    type: "string"
    description: ""

  - name: "altPhone"
    type: "string"
    description: ""

  - name: "balance"
    type: "number, string"
    description: ""

  - name: "balancePrimary"
    type: "number, string"
    description: ""

  - name: "bcn"
    type: "string"
    description: ""

  - name: "billPay"
    type: "boolean, string"
    description: ""

  - name: "category"
    type: "varies"
    description: ""

  - name: "comments"
    type: "string"
    description: ""

  - name: "companyName"
    type: "string"
    description: ""

  - name: "creditLimit"
    type: "number, string"
    description: ""

  - name: "currency"
    type: "varies"
    description: ""

  - name: "currencyList"
    type: "varies"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "dateCreated"
    type: "date-time"
    description: ""

  - name: "defaultAddress"
    type: "string"
    description: ""

  - name: "eligibleForCommission"
    type: "boolean, string"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "emailPreference"
    type: "varies"
    description: ""

  - name: "emailTransactions"
    type: "boolean, string"
    description: ""

  - name: "entityId"
    type: "string"
    description: ""

  - name: "expenseAccount"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "fax"
    type: "string"
    description: ""

  - name: "faxTransactions"
    type: "boolean, string"
    description: ""

  - name: "firstName"
    type: "string"
    description: ""

  - name: "giveAccess"
    type: "boolean, string"
    description: ""

  - name: "globalSubscriptionStatus"
    type: "varies"
    description: ""

  - name: "homePhone"
    type: "string"
    description: ""

  - name: "image"
    type: "varies"
    description: ""

  - name: "incoterm"
    type: "varies"
    description: ""

  - name: "is1099Eligible"
    type: "boolean, string"
    description: ""

  - name: "isAccountant"
    type: "boolean, string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "isJobResourceVend"
    type: "boolean, string"
    description: ""

  - name: "isPerson"
    type: "boolean, string"
    description: ""

  - name: "laborCost"
    type: "number, string"
    description: ""

  - name: "lastName"
    type: "string"
    description: ""

  - name: "legalName"
    type: "string"
    description: ""

  - name: "middleName"
    type: "string"
    description: ""

  - name: "mobilePhone"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "openingBalance"
    type: "number, string"
    description: ""

  - name: "openingBalanceAccount"
    type: "varies"
    description: ""

  - name: "openingBalanceDate"
    type: "date-time"
    description: ""

  - name: "password"
    type: "string"
    description: ""

  - name: "password2"
    type: "string"
    description: ""

  - name: "payablesAccount"
    type: "varies"
    description: ""

  - name: "phone"
    type: "string"
    description: ""

  - name: "phoneticName"
    type: "string"
    description: ""

  - name: "pricingScheduleList"
    type: "varies"
    description: ""

  - name: "printOnCheckAs"
    type: "string"
    description: ""

  - name: "printTransactions"
    type: "boolean, string"
    description: ""

  - name: "purchaseOrderAmount"
    type: "number, string"
    description: ""

  - name: "purchaseOrderQuantity"
    type: "number, string"
    description: ""

  - name: "purchaseOrderQuantityDiff"
    type: "number, string"
    description: ""

  - name: "receiptAmount"
    type: "number, string"
    description: ""

  - name: "receiptQuantity"
    type: "number, string"
    description: ""

  - name: "receiptQuantityDiff"
    type: "number, string"
    description: ""

  - name: "representingSubsidiary"
    type: "varies"
    description: ""

  - name: "requirePwdChange"
    type: "boolean, string"
    description: ""

  - name: "rolesList"
    type: "varies"
    description: ""

  - name: "salutation"
    type: "string"
    description: ""

  - name: "sendEmail"
    type: "boolean, string"
    description: ""

  - name: "subscriptionsList"
    type: "varies"
    description: ""

  - name: "subsidiary"
    type: "varies"
    description: ""

  - name: "taxIdNum"
    type: "string"
    description: ""

  - name: "taxItem"
    type: "varies"
    description: ""

  - name: "terms"
    type: "varies"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "unbilledOrders"
    type: "number, string"
    description: ""

  - name: "unbilledOrdersPrimary"
    type: "number, string"
    description: ""

  - name: "url"
    type: "string"
    description: ""

  - name: "vatRegNumber"
    type: "string"
    description: ""

  - name: "workCalendar"
    type: "varies"
    description: ""
---